import ast
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from gateway import FakeTransport, Gateway, RuntimeConfig, SANDBOX_DB_PATH, TelegramBotAdapter
from runtime_app import (
    CREDENTIAL_SLOTS,
    LISTEN_HOST,
    LISTEN_PORT,
    PrivacySafeLogger,
    RuntimeApplication,
    RuntimeBoundaryError,
    build_transport,
    credential_path,
    validate_listen_contract,
)

CHANNEL = -1007770001111
DISCUSSION = -1007770002222
SYNTHETIC_USER_ID = 9876543210123
SYNTHETIC_USERNAME = "synthetic_private_user_71f2"
SYNTHETIC_NAME = "Synthetic Private Person 71f2"
SYNTHETIC_COMMENT = "SYNTHETIC_RAW_COMMENT_71f2_DO_NOT_LOG"


def cfg(db_path):
    return RuntimeConfig.from_dict({
        "environment": "test",
        "channel_key": "wbnp-experimental",
        "channel_username": "synthetic_channel",
        "channel_chat_id": CHANNEL,
        "discussion_linked": True,
        "discussion_chat_id": DISCUSSION,
        "bot_identity": "synthetic-test-bot-metadata-only",
        "webhook_endpoint": "http://127.0.0.1:8782/telegram/webhook",
        "privacy_mode": "aggregate_only",
        "sandbox_db_path": db_path,
    })


class RuntimePrivacyTests(unittest.TestCase):
    def make(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        db_path = os.path.join(td.name, "gateway.sqlite3")
        config = cfg(db_path)
        transport = FakeTransport()
        gateway = Gateway(db_path, config, TelegramBotAdapter(config, transport))
        stream = io.StringIO()
        logger = PrivacySafeLogger(stream)
        app = RuntimeApplication(gateway, logger)
        self.addCleanup(gateway.db.close)
        return app, gateway, transport, stream, db_path

    def seed_thread(self, gateway):
        gateway.db.execute("INSERT INTO publications(publication_id,revision,content_hash) VALUES ('p1',1,'x')")
        gateway.db.execute("INSERT INTO deliveries(publication_id,distribution_target,external_chat_id,external_message_id,delivery_state,content_hash) VALUES ('p1','telegram:test',?,101,'delivered_verified','x')", (CHANNEL,))
        gateway.db.execute("INSERT INTO aggregates(publication_id,distribution_target) VALUES ('p1','telegram:test')")
        gateway.db.execute("INSERT INTO discussion_threads(publication_id,distribution_target,discussion_chat_id,discussion_root_message_id,origin_channel_chat_id,origin_channel_message_id) VALUES ('p1','telegram:test',?,201,?,101)", (DISCUSSION, CHANNEL))
        gateway.db.commit()

    def synthetic_comment_body(self, update_id=1001, thread=201):
        return json.dumps({
            "update_id": update_id,
            "message": {
                "message_id": 202,
                "message_thread_id": thread,
                "chat": {"id": DISCUSSION},
                "from": {
                    "id": SYNTHETIC_USER_ID,
                    "username": SYNTHETIC_USERNAME,
                    "first_name": SYNTHETIC_NAME,
                },
                "text": SYNTHETIC_COMMENT,
            },
        }).encode("utf-8")

    def assert_forbidden_absent(self, text):
        self.assertNotIn(str(SYNTHETIC_USER_ID), text)
        self.assertNotIn(SYNTHETIC_USERNAME, text)
        self.assertNotIn(SYNTHETIC_NAME, text)
        self.assertNotIn(SYNTHETIC_COMMENT, text)

    def test_success_log_does_not_contain_identity_or_comment(self):
        app, gateway, _, stream, _, = self.make()
        self.seed_thread(gateway)
        status, response = app.handle_payload_bytes(self.synthetic_comment_body())
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(response), {"ok": True, "outcome": "processed"})
        logs = stream.getvalue()
        self.assert_forbidden_absent(logs)
        self.assertIn('"status":"accepted"', logs)
        self.assertEqual(gateway.db.execute("SELECT comments_count FROM aggregates WHERE publication_id='p1'").fetchone()[0], 1)

    def test_validation_error_log_and_response_do_not_echo_payload(self):
        app, _, _, stream, _ = self.make()
        status, response = app.handle_payload_bytes(self.synthetic_comment_body(update_id=1002, thread=999999))
        self.assertEqual(status, 422)
        self.assert_forbidden_absent(stream.getvalue())
        self.assert_forbidden_absent(response.decode("utf-8"))
        self.assertEqual(json.loads(response), {"ok": False, "outcome": "rejected"})

    def test_malformed_request_does_not_echo_raw_body(self):
        app, _, _, stream, _ = self.make()
        raw = ("{\"update_id\":1003,\"text\":\"" + SYNTHETIC_COMMENT + "\",\"username\":\"" + SYNTHETIC_USERNAME).encode("utf-8")
        status, response = app.handle_payload_bytes(raw)
        self.assertEqual(status, 400)
        self.assert_forbidden_absent(stream.getvalue())
        self.assert_forbidden_absent(response.decode("utf-8"))

    def test_no_identity_or_comment_persisted_in_sqlite(self):
        app, gateway, _, _, db_path = self.make()
        self.seed_thread(gateway)
        status, _ = app.handle_payload_bytes(self.synthetic_comment_body(update_id=1004))
        self.assertEqual(status, 200)
        gateway.db.commit()
        gateway.db.execute("PRAGMA wal_checkpoint(FULL)")
        data = Path(db_path).read_bytes()
        for forbidden in (str(SYNTHETIC_USER_ID), SYNTHETIC_USERNAME, SYNTHETIC_NAME, SYNTHETIC_COMMENT):
            self.assertNotIn(forbidden.encode("utf-8"), data)

    def test_logger_rejects_arbitrary_fields(self):
        logger = PrivacySafeLogger(io.StringIO())
        with self.assertRaises(RuntimeBoundaryError):
            logger.emit(event="webhook_request", status="accepted", raw_body=SYNTHETIC_COMMENT)

    def test_logger_rejects_arbitrary_string_value(self):
        logger = PrivacySafeLogger(io.StringIO())
        with self.assertRaises(RuntimeBoundaryError):
            logger.emit(event="webhook_request", status=SYNTHETIC_COMMENT)

    def test_production_environment_refused_by_accepted_config(self):
        with self.assertRaises(Exception):
            RuntimeConfig.from_dict({
                "environment": "production",
                "channel_key": "x",
                "channel_chat_id": CHANNEL,
                "discussion_linked": False,
                "bot_identity": "x",
                "privacy_mode": "aggregate_only",
                "sandbox_db_path": SANDBOX_DB_PATH,
            })

    def test_loopback_contract_is_exact(self):
        validate_listen_contract(LISTEN_HOST, LISTEN_PORT)
        with self.assertRaises(RuntimeBoundaryError):
            validate_listen_contract("0.0.0.0", LISTEN_PORT)
        with self.assertRaises(RuntimeBoundaryError):
            validate_listen_contract(LISTEN_HOST, LISTEN_PORT + 1)

    def test_fake_transport_only_candidate_requires_no_credentials(self):
        logger = PrivacySafeLogger(io.StringIO())
        transport = build_transport("fake", logger)
        self.assertIsInstance(transport, FakeTransport)

    def test_real_transport_missing_credentials_fails_closed(self):
        logger = PrivacySafeLogger(io.StringIO())
        old = os.environ.pop("CREDENTIALS_DIRECTORY", None)
        try:
            with self.assertRaises(RuntimeBoundaryError):
                build_transport("real", logger)
        finally:
            if old is not None:
                os.environ["CREDENTIALS_DIRECTORY"] = old

    def test_real_transport_still_not_implemented_with_synthetic_credentials(self):
        logger = PrivacySafeLogger(io.StringIO())
        with tempfile.TemporaryDirectory() as td:
            for slot in CREDENTIAL_SLOTS:
                Path(td, slot).write_text("synthetic-not-a-real-secret", encoding="utf-8")
            old = os.environ.get("CREDENTIALS_DIRECTORY")
            os.environ["CREDENTIALS_DIRECTORY"] = td
            try:
                for slot in CREDENTIAL_SLOTS:
                    self.assertEqual(credential_path(slot), Path(td) / slot)
                with self.assertRaisesRegex(RuntimeBoundaryError, "real_transport_not_implemented_in_r01"):
                    build_transport("real", logger)
            finally:
                if old is None:
                    os.environ.pop("CREDENTIALS_DIRECTORY", None)
                else:
                    os.environ["CREDENTIALS_DIRECTORY"] = old

    def test_sandbox_db_path_constant_unchanged(self):
        self.assertEqual(SANDBOX_DB_PATH, "/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3")

    def test_no_network_client_imports_in_runtime_candidate(self):
        source = Path(__file__).with_name("runtime_app.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported.add(node.module or "")
        forbidden = {"requests", "urllib.request", "aiohttp", "httpx", "telegram", "telegram.ext"}
        self.assertTrue(imported.isdisjoint(forbidden), imported & forbidden)


if __name__ == "__main__":
    unittest.main(verbosity=2)
