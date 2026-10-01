#!/usr/bin/env python3
import io
import importlib.util
import json
import sqlite3
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("dialogue_mvp.py")
SPEC = importlib.util.spec_from_file_location("dialogue_mvp", MODULE_PATH)
dialogue_mvp = importlib.util.module_from_spec(SPEC)
sys.modules["dialogue_mvp"] = dialogue_mvp
SPEC.loader.exec_module(dialogue_mvp)
Config = dialogue_mvp.Config
BoundaryError = dialogue_mvp.BoundaryError
DialogueApplication = dialogue_mvp.DialogueApplication
OpenAIResponsesAdapter = dialogue_mvp.OpenAIResponsesAdapter
ProviderFailure = dialogue_mvp.ProviderFailure
SafeLogger = dialogue_mvp.SafeLogger
Store = dialogue_mvp.Store
TelegramSendEvidence = dialogue_mvp.TelegramSendEvidence
parse_update = dialogue_mvp.parse_update

DISCUSSION_ID = -1002429106148
BOT_ID = 8866633840
BOT_USERNAME = "WBNP_Media_Bot"


def config(path: str) -> Config:
    return Config.from_dict({
        "schema": "TELEGRAM_ENTITY_DIALOGUE_MVP_R02", "environment": "test",
        "database_path": path, "testers_allow_path": "/etc/wellbeing/telegram-single-entity-pilot/testers.allow",
        "allowed_chat_types": ["supergroup"], "discussion_chat_id": DISCUSSION_ID,
        "bot_user_id": BOT_ID, "bot_username": BOT_USERNAME, "activation_command": "ask",
        "model": "gpt-5.6-luna", "max_output_tokens": 512,
        "provider_timeout_seconds": 30, "telegram_timeout_seconds": 10,
        "poll_timeout_seconds": 25, "poll_retry_seconds": 5, "max_input_bytes": 4096,
        "max_history_messages": 12, "max_history_bytes": 32768, "max_update_records_per_conversation": 256,
        "fallback_text": "Сейчас не получилось ответить. Попробуйте позднее.",
        "entity_bootstrap_path": "/opt/wellbeing/telegram-single-entity-mvp-r02/entity_bootstrap.txt",
    }, (101, 202))


def utf16_units(value: str) -> int:
    return len(value.encode("utf-16-le")) // 2


def update(uid=1, user=101, chat=DISCUSSION_ID, text="Привет", thread=0, direct_topic=0,
           trigger="mention", chat_type="supergroup", reply_target=77, reply_thread=None,
           is_automatic_forward=False):
    msg = {"message_id": uid + 100, "chat": {"id": chat, "type": chat_type},
           "from": {"id": user, "first_name": "SHOULD_NOT_PERSIST"}}
    if trigger == "mention":
        token = "@" + BOT_USERNAME
        msg["text"] = token + " " + text
        msg["entities"] = [{"type": "mention", "offset": 0, "length": utf16_units(token)}]
    elif trigger == "mention_after_emoji":
        token = "@" + BOT_USERNAME
        prefix = "🙂 "
        msg["text"] = prefix + token + " " + text
        msg["entities"] = [{"type": "mention", "offset": utf16_units(prefix), "length": utf16_units(token)}]
    elif trigger == "command":
        token = "/ask@" + BOT_USERNAME
        msg["text"] = token + " " + text
        msg["entities"] = [{"type": "bot_command", "offset": 0, "length": utf16_units(token)}]
    elif trigger == "reply":
        msg["text"] = text
        msg["reply_to_message"] = {"message_id": reply_target, "from": {"id": BOT_ID, "is_bot": True}}
        if reply_thread is not None:
            msg["reply_to_message"]["message_thread_id"] = reply_thread
    elif trigger == "ambient":
        msg["text"] = text
    else:
        raise AssertionError("unknown synthetic trigger")
    if thread:
        msg["message_thread_id"] = thread
    if direct_topic:
        msg["direct_messages_topic"] = {"topic_id": direct_topic, "user": {"id": 999, "first_name": "DO_NOT_PERSIST"}}
    if is_automatic_forward:
        msg["is_automatic_forward"] = True
    return {"update_id": uid, "message": msg}


class FakeProvider:
    def __init__(self, fail=False): self.calls = []; self.fail = fail
    def respond(self, instructions, history):
        self.calls.append((instructions, history))
        if self.fail: raise ProviderFailure("synthetic")
        return "Ответ " + str(len(self.calls))


class FakeTelegram:
    def __init__(self, fail=False): self.calls = []; self.fail = fail
    def send_text(self, chat_id, thread_id, direct_topic_id, text):
        self.calls.append((chat_id, thread_id, direct_topic_id, text))
        if self.fail: raise dialogue_mvp.TelegramFailure("synthetic")
        return TelegramSendEvidence(
            returned_message_id=700 + len(self.calls), returned_chat_id=chat_id,
            returned_message_thread_id=thread_id if thread_id else None,
            returned_direct_topic_id=direct_topic_id if direct_topic_id else None,
            returned_is_topic_message=True if thread_id else None,
        )


class FakeHTTP:
    def __init__(self, result): self.result = result; self.calls = []
    def post(self, *args): self.calls.append(args); return self.result


class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cfg = config(str(Path(self.tmp.name) / "state.sqlite"))
        self.provider = FakeProvider(); self.telegram = FakeTelegram(); self.log = io.StringIO()
        self.store = Store(self.cfg.database_path)
        self.app = DialogueApplication(self.cfg, self.store, self.provider, self.telegram,
                                       "Ты тестовая Сущность.", SafeLogger(self.log))

    def tearDown(self):
        self.store.db.close(); self.tmp.cleanup()

    def call(self, payload):
        return self.app.process_update(payload)

    def test_correct_discussion_chat_admitted(self):
        code, out = self.call(update())
        self.assertEqual((code, out["outcome"]), (200, "replied"))
        self.assertEqual(self.telegram.calls[0][0], DISCUSSION_ID)

    def test_explicit_mention_accepted_and_removed_from_prompt(self):
        self.call(update(text="Содержательный вопрос"))
        self.assertEqual(self.provider.calls[0][1][-1]["content"], "Содержательный вопрос")

    def test_reply_to_bot_accepted(self):
        code, out = self.call(update(trigger="reply"))
        self.assertEqual((code, out["outcome"]), (200, "replied"))

    def test_explicit_command_accepted(self):
        code, out = self.call(update(trigger="command", text="Вопрос"))
        self.assertEqual((code, out["outcome"]), (200, "replied"))
        self.assertEqual(self.provider.calls[0][1][-1]["content"], "Вопрос")

    def test_utf16_mention_offset(self):
        code, out = self.call(update(trigger="mention_after_emoji"))
        self.assertEqual((code, out["outcome"]), (200, "replied"))

    def test_ambient_nonaddressed_message_ignored(self):
        code, out = self.call(update(trigger="ambient"))
        self.assertEqual((code, out["outcome"]), (200, "ignored_not_addressed"))
        self.assertFalse(self.provider.calls); self.assertFalse(self.telegram.calls)

    def test_other_chat_rejected_before_effect(self):
        code, out = self.call(update(chat=-1009999999999))
        self.assertEqual((code, out["outcome"]), (422, "rejected"))
        self.assertFalse(self.provider.calls); self.assertFalse(self.telegram.calls)

    def test_unlisted_tester_rejected_before_effect(self):
        code, _ = self.call(update(user=303))
        self.assertEqual(code, 422)
        self.assertFalse(self.provider.calls); self.assertFalse(self.telegram.calls)

    def test_multi_turn_same_thread_context(self):
        self.call(update(1, text="Меня зовут А.", thread=11))
        self.call(update(2, text="Как меня зовут?", thread=11))
        history = self.provider.calls[1][1]
        self.assertEqual([x["role"] for x in history], ["user", "assistant", "user"])
        self.assertEqual(history[0]["content"], "Меня зовут А.")

    def test_different_thread_isolation(self):
        self.call(update(1, thread=11)); self.call(update(2, thread=22))
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_exact_replay_no_second_effect(self):
        payload = update(); self.call(payload)
        code, out = self.call(payload)
        self.assertEqual((code, out["outcome"]), (200, "duplicate"))
        self.assertEqual(len(self.provider.calls), 1); self.assertEqual(len(self.telegram.calls), 1)

    def test_update_id_collision(self):
        self.call(update(1, text="A")); code, out = self.call(update(1, text="B"))
        self.assertEqual((code, out["outcome"]), (409, "update_id_conflict"))

    def test_non_message_update_rejects_before_effect(self):
        code, _ = self.call({"update_id": 1, "channel_post": {"text": "x"}})
        self.assertEqual(code, 422); self.assertFalse(self.provider.calls)

    def test_provider_failure_visible_fallback(self):
        self.provider.fail = True
        code, out = self.call(update())
        self.assertEqual((code, out["outcome"]), (200, "fallback_sent"))
        self.assertEqual(self.telegram.calls[0][3], self.cfg.fallback_text)

    def test_send_failure_is_uncertain_and_no_blind_retry(self):
        self.telegram.fail = True; payload = update()
        code, out = self.call(payload)
        self.assertEqual((code, out["outcome"]), (503, "manual_reconciliation_required"))
        code2, out2 = self.call(payload)
        self.assertEqual((code2, out2["outcome"]), (503, "manual_reconciliation_required"))
        self.assertEqual(len(self.provider.calls), 1)

    def test_input_bound(self):
        code, _ = self.call(update(text="я" * 5000))
        self.assertEqual(code, 422); self.assertFalse(self.provider.calls)

    def test_raw_identity_and_text_not_logged(self):
        self.call(update(text="СЕКРЕТНЫЙ_ТЕКСТ")); log = self.log.getvalue()
        self.assertNotIn("СЕКРЕТНЫЙ", log); self.assertNotIn("101", log)
        self.assertNotIn("SHOULD_NOT_PERSIST", log)

    def test_openai_shape_and_output(self):
        response = {"status": "completed", "output": [{"type": "reasoning"}, {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "OK"}]}]}
        http = FakeHTTP(response); adapter = OpenAIResponsesAdapter(b"key", "gpt-5.6-luna", 512, 30, http)
        self.assertEqual(adapter.respond("sys", [{"role": "user", "content": "hi"}]), "OK")
        body = http.calls[0][2]
        self.assertEqual(body["tools"], []); self.assertIs(body["store"], False)
        self.assertEqual(body["max_output_tokens"], 512)

    def test_reasoning_only_is_not_candidate(self):
        http = FakeHTTP({"status": "completed", "output": [{"type": "reasoning", "summary": []}]})
        adapter = OpenAIResponsesAdapter(b"key", "gpt-5.6-luna", 512, 30, http)
        with self.assertRaises(ProviderFailure):
            adapter.respond("sys", [{"role": "user", "content": "hi"}])

    def test_closed_config_unknown_field(self):
        raw = json.loads(Path(__file__).with_name("config.example.json").read_text())
        raw["surprise"] = 1
        with self.assertRaises(Exception): Config.from_dict(raw, (101,))

    def test_exact_mapping_cannot_be_reconfigured(self):
        raw = json.loads(Path(__file__).with_name("config.example.json").read_text())
        raw["discussion_chat_id"] = -1001
        with self.assertRaises(Exception): Config.from_dict(raw, (101,))

    def test_poll_shape(self):
        http = FakeHTTP({"ok": True, "result": [update(5)]})
        adapter = dialogue_mvp.TelegramBotAdapter(b"token", 10, http)
        self.assertEqual(adapter.get_updates(5, 25)[0]["update_id"], 5)
        body = http.calls[0][2]
        self.assertEqual(body, {"offset": 5, "limit": 10, "timeout": 25, "allowed_updates": ["message"]})

    def test_poll_offset_is_durable(self):
        self.assertEqual(self.store.poll_offset(), 0)
        self.store.set_poll_offset(42)
        self.assertEqual(self.store.poll_offset(), 42)

    def test_transcript_is_pruned_and_request_is_bounded(self):
        for n in range(1, 9): self.call(update(n, text="turn" + str(n), thread=11))
        count = self.store.db.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
        self.assertLessEqual(count, self.cfg.max_history_messages)
        self.assertLessEqual(len(self.provider.calls[-1][1]), self.cfg.max_history_messages)

    # Routing observability r0.1 matrix T1-T9.
    def test_t1_same_chat_thread_topic_same_conversation_key(self):
        first = parse_update(update(41, thread=17, direct_topic=3001), self.cfg)
        second = parse_update(update(42, thread=17, direct_topic=3001), self.cfg)
        self.assertEqual(first.conversation_key, second.conversation_key)

    def test_t2_different_thread_changes_conversation_key(self):
        first = parse_update(update(41, thread=17), self.cfg)
        second = parse_update(update(42, thread=18), self.cfg)
        self.assertNotEqual(first.conversation_key, second.conversation_key)

    def test_t3_different_direct_topic_changes_conversation_key(self):
        first = parse_update(update(41, direct_topic=3001), self.cfg)
        second = parse_update(update(42, direct_topic=3002), self.cfg)
        self.assertNotEqual(first.conversation_key, second.conversation_key)

    def test_t4_trigger_class_is_deterministic_and_persisted(self):
        expected = ((51, "reply", "reply-to-bot"), (52, "command", "command"), (53, "mention", "exact-mention"))
        for uid, trigger, classification in expected:
            self.call(update(uid, trigger=trigger))
            row = self.store.db.execute("SELECT trigger_class FROM updates WHERE update_id=?", (uid,)).fetchone()
            self.assertEqual(row[0], classification)

    def test_t5_successful_send_persists_only_minimal_routing_projection(self):
        self.call(update(61, thread=17, direct_topic=3001, text="routing"))
        diagnostic = self.store.routing_diagnostic(61)
        self.assertEqual(diagnostic, {
            "update_id": 61, "inbound_message_id": 161, "message_thread_id": 17,
            "direct_topic_id": 3001, "trigger_class": "exact-mention",
            "conversation_key": parse_update(update(61, thread=17, direct_topic=3001, text="routing"), self.cfg).conversation_key,
            "outbound_message_id": 701, "returned_chat_id": DISCUSSION_ID,
            "returned_message_thread_id": 17, "returned_direct_topic_id": 3001,
            "returned_is_topic_message": True, "state": "COMMITTED", "error_class": None,
        })
        self.assertEqual(set(diagnostic), set(Store.DIAGNOSTIC_FIELDS))

    def test_t5_bot_api_message_is_projected_not_retained(self):
        response = {"ok": True, "result": {
            "message_id": 777, "message_thread_id": 17,
            "direct_messages_topic": {"topic_id": 3001, "user": {"id": 9, "username": "DROP_ME"}},
            "chat": {"id": DISCUSSION_ID, "title": "DROP_ME"}, "is_topic_message": True,
            "text": "DROP_ME", "from": {"username": "DROP_ME"},
        }}
        adapter = dialogue_mvp.TelegramBotAdapter(b"token", 10, FakeHTTP(response))
        evidence = adapter.send_text(DISCUSSION_ID, 17, 3001, "safe")
        self.assertEqual(evidence, TelegramSendEvidence(777, DISCUSSION_ID, 17, 3001, True))
        self.assertNotIn("DROP_ME", repr(evidence))

    def test_t6_send_success_metadata_persistence_failure_is_uncertain_no_resend(self):
        payload = update(71, thread=17)
        original = self.store.commit_turn
        def fail_commit(event, reply, evidence):
            raise BoundaryError("synthetic_routing_metadata_persistence_failure")
        self.store.commit_turn = fail_commit
        code, out = self.call(payload)
        self.assertEqual((code, out["outcome"]), (503, "manual_reconciliation_required"))
        row = self.store.db.execute("SELECT state,error_class FROM updates WHERE update_id=71").fetchone()
        self.assertEqual(tuple(row), ("OUTCOME_UNKNOWN", "reply_routing_persistence_failed"))
        code2, out2 = self.call(payload)
        self.assertEqual((code2, out2["outcome"]), (503, "manual_reconciliation_required"))
        self.assertEqual((len(self.provider.calls), len(self.telegram.calls)), (1, 1))
        self.store.commit_turn = original

    def test_t7_privacy_no_raw_update_identity_or_provider_response_in_routing_storage_or_logs(self):
        payload = update(81, text="ALLOWED_DIALOGUE_TEXT", thread=17, direct_topic=3001)
        payload["message"]["from"]["username"] = "DO_NOT_PERSIST_USERNAME"
        self.call(payload)
        update_row = dict(self.store.db.execute("SELECT * FROM updates WHERE update_id=81").fetchone())
        serialized = json.dumps(update_row, sort_keys=True)
        self.assertNotIn("DO_NOT_PERSIST", serialized)
        self.assertNotIn("ALLOWED_DIALOGUE_TEXT", serialized)
        self.assertNotIn("DO_NOT_PERSIST", self.log.getvalue())
        self.assertNotIn("raw_update", set(update_row))
        self.assertNotIn("provider_response", set(update_row))

    def test_t8_r02_database_migration_is_additive_idempotent_and_history_readable(self):
        old_path = str(Path(self.tmp.name) / "old-r02.sqlite")
        db = sqlite3.connect(old_path)
        db.executescript("""
        CREATE TABLE updates(update_id INTEGER PRIMARY KEY,request_digest TEXT NOT NULL,state TEXT NOT NULL,
          conversation_key TEXT NOT NULL,telegram_message_id INTEGER,error_class TEXT);
        CREATE TABLE messages(conversation_key TEXT NOT NULL,sequence INTEGER NOT NULL,role TEXT NOT NULL,
          content TEXT NOT NULL,PRIMARY KEY(conversation_key,sequence),CHECK(role IN ('user','assistant')));
        CREATE TABLE runtime_meta(key TEXT PRIMARY KEY,value INTEGER NOT NULL);
        INSERT INTO updates VALUES(5,'digest','COMMITTED','legacy-key',101,NULL);
        INSERT INTO messages VALUES('legacy-key',1,'user','legacy-history');
        """)
        db.commit(); db.close()
        migrated = Store(old_path)
        try:
            self.assertEqual(migrated.db.execute("SELECT content FROM messages").fetchone()[0], "legacy-history")
            self.assertEqual(migrated.db.execute("SELECT telegram_message_id FROM updates").fetchone()[0], 101)
            first_columns = migrated._column_names()
        finally:
            migrated.db.close()
        migrated_again = Store(old_path)
        try:
            self.assertEqual(migrated_again._column_names(), first_columns)
            legacy = migrated_again.routing_diagnostic(5)
            self.assertEqual(legacy["state"], "COMMITTED")
            self.assertIsNone(legacy["inbound_message_id"])
        finally:
            migrated_again.db.close()

    def test_t9_diagnostic_is_bounded_read_only_projection(self):
        self.call(update(91, thread=22))
        diagnostic = self.store.routing_diagnostic(91)
        self.assertEqual(tuple(diagnostic), Store.DIAGNOSTIC_FIELDS)
        forbidden = {"request_digest", "telegram_message_id", "text", "username", "display_name", "raw_update", "provider_response"}
        self.assertFalse(forbidden.intersection(diagnostic))

    def test_t9_cli_diagnostic_needs_no_credentials_and_returns_bounded_json(self):
        self.call(update(92, thread=23))
        allow_path = Path(self.tmp.name) / "testers.allow"
        bootstrap_path = Path(self.tmp.name) / "bootstrap.txt"
        config_path = Path(self.tmp.name) / "runtime.json"
        allow_path.write_text("101\n", encoding="ascii")
        bootstrap_path.write_text("bounded", encoding="utf-8")
        raw = json.loads(Path(__file__).with_name("config.example.json").read_text())
        raw.update({"database_path": self.cfg.database_path, "testers_allow_path": str(allow_path),
                    "entity_bootstrap_path": str(bootstrap_path), "environment": "test"})
        config_path.write_text(json.dumps(raw), encoding="utf-8")
        stdout, old_argv = io.StringIO(), sys.argv
        try:
            sys.argv = ["dialogue_mvp.py", "diagnose-routing", "--config", str(config_path), "--update-id", "92"]
            with redirect_stdout(stdout):
                self.assertEqual(dialogue_mvp.main(), 0)
        finally:
            sys.argv = old_argv
        result = json.loads(stdout.getvalue())
        self.assertEqual(tuple(sorted(result)), tuple(sorted(Store.DIAGNOSTIC_FIELDS)))
        self.assertEqual(result["update_id"], 92)

    # Conversation-root r0.1 implementation matrix T1-T16.
    def _root_row(self, update_id):
        return self.store.db.execute(
            "SELECT stable_conversation_root_id,root_conversation_key,root_derivation_class,"
            "root_evidence_update_id,inbound_reply_to_message_id,inbound_reply_to_message_thread_id,"
            "conversation_key,message_thread_id,direct_topic_id,state,outbound_message_id,returned_chat_id "
            "FROM updates WHERE update_id=?", (update_id,),
        ).fetchone()

    def _raw_relation_count(self, chat_id, outbound_message_id):
        return self.store.db.execute(
            "SELECT COUNT(*) FROM updates WHERE returned_chat_id=? AND outbound_message_id=?",
            (chat_id, outbound_message_id),
        ).fetchone()[0]

    def test_root_t01_initial_linked_discussion_command_establishes_observed_anchor(self):
        self.call(update(201, trigger="command", thread=110, text="turn-one"))
        row = self._root_row(201)
        self.assertEqual(row["root_derivation_class"], "OBSERVED_LINKED_THREAD_ANCHOR")
        self.assertIsNotNone(row["stable_conversation_root_id"])
        expected = dialogue_mvp.root_conversation_key(row["stable_conversation_root_id"])
        self.assertEqual(row["root_conversation_key"], expected)
        self.assertEqual(expected, __import__("hashlib").sha256(
            ("tg-dialogue-root-r01\0" + row["stable_conversation_root_id"]).encode()).hexdigest())
        self.assertNotEqual(row["conversation_key"], row["root_conversation_key"])

    def test_root_t02_changed_thread_direct_known_reply_inherits_same_root(self):
        self.call(update(202, trigger="command", thread=110, text="alpha"))
        first = self._root_row(202)
        outbound = first["outbound_message_id"]
        self.call(update(203, trigger="reply", thread=outbound, reply_target=outbound, text="beta"))
        second = self._root_row(203)
        self.assertEqual(second["root_derivation_class"], "PROVEN_OUTBOUND_LINEAGE")
        self.assertEqual(second["stable_conversation_root_id"], first["stable_conversation_root_id"])
        self.assertEqual(second["root_conversation_key"], first["root_conversation_key"])
        history = self.provider.calls[1][1]
        self.assertEqual([x["role"] for x in history], ["user", "assistant", "user"])
        self.assertEqual(history[0]["content"], "alpha")

    def test_root_t03_same_root_observation_requires_exact_same_anchor(self):
        self.call(update(204, trigger="command", thread=120, text="one"))
        first = self._root_row(204)
        self.call(update(205, trigger="command", thread=120, text="two"))
        second = self._root_row(205)
        self.assertEqual(second["root_derivation_class"], "SAME_ROOT_OBSERVATION")
        self.assertEqual(second["stable_conversation_root_id"], first["stable_conversation_root_id"])
        self.assertEqual(second["root_evidence_update_id"], first["root_evidence_update_id"])

    def test_root_t04_reply_target_from_other_root_follows_target_not_observed_thread(self):
        self.call(update(206, trigger="command", thread=130, text="root-A"))
        a = self._root_row(206)
        self.call(update(207, trigger="command", thread=140, text="root-C"))
        c = self._root_row(207)
        self.assertNotEqual(a["stable_conversation_root_id"], c["stable_conversation_root_id"])
        self.call(update(208, trigger="reply", thread=140, reply_target=a["outbound_message_id"], text="target-A"))
        r = self._root_row(208)
        self.assertEqual(r["stable_conversation_root_id"], a["stable_conversation_root_id"])
        self.assertNotEqual(r["stable_conversation_root_id"], c["stable_conversation_root_id"])
        history = self.provider.calls[2][1]
        self.assertEqual(history[0]["content"], "root-A")
        self.assertNotIn("root-C", [x["content"] for x in history])

    def test_root_t05_unknown_reply_target_isolated_no_history_merge(self):
        self.call(update(209, trigger="command", thread=150, text="known"))
        self.call(update(210, trigger="reply", thread=150, reply_target=999999, text="unknown-target"))
        r = self._root_row(210)
        self.assertEqual(r["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_root_t06_legacy_row_without_root_never_guessed_into_lineage(self):
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,telegram_message_id,error_class,"
            "inbound_message_id,message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (190, "legacy-digest", "COMMITTED", "legacy-key", 900, None, 290, 160, 0,
             "command", 900, DISCUSSION_ID),
        )
        self.call(update(211, trigger="reply", thread=160, reply_target=900, text="legacy-reply"))
        r = self._root_row(211)
        self.assertEqual(r["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertEqual(len(self.provider.calls[0][1]), 1)
        legacy = self.store.db.execute("SELECT conversation_key,stable_conversation_root_id FROM updates WHERE update_id=190").fetchone()
        self.assertEqual(legacy["conversation_key"], "legacy-key")
        self.assertIsNone(legacy["stable_conversation_root_id"])

    def test_root_t07_duplicate_replay_one_effect_and_same_persisted_root(self):
        payload = update(212, trigger="command", thread=170, text="dup")
        self.call(payload)
        before = self._root_row(212)
        code, out = self.call(payload)
        after = self._root_row(212)
        self.assertEqual((code, out["outcome"]), (200, "duplicate"))
        self.assertEqual(before["stable_conversation_root_id"], after["stable_conversation_root_id"])
        self.assertEqual((len(self.provider.calls), len(self.telegram.calls)), (1, 1))

    def test_root_t08_post_send_root_relation_persistence_failure_outcome_unknown_no_resend(self):
        payload = update(213, trigger="command", thread=180, text="uncertain")
        original = self.store.commit_turn
        def fail_commit(event, reply, evidence):
            raise BoundaryError("synthetic_root_relation_persistence_failure")
        self.store.commit_turn = fail_commit
        code, out = self.call(payload)
        root_before = self.store.root_decision(213)
        code2, out2 = self.call(payload)
        root_after = self.store.root_decision(213)
        self.store.commit_turn = original
        self.assertEqual((code, out["outcome"]), (503, "manual_reconciliation_required"))
        self.assertEqual((code2, out2["outcome"]), (503, "manual_reconciliation_required"))
        self.assertEqual(root_before, root_after)
        self.assertEqual((len(self.provider.calls), len(self.telegram.calls)), (1, 1))
        state = self.store.db.execute("SELECT state FROM updates WHERE update_id=213").fetchone()[0]
        self.assertEqual(state, "OUTCOME_UNKNOWN")

    def test_root_t09_cross_chat_never_merges(self):
        linked = dialogue_mvp.stable_root_id("linked_discussion", DISCUSSION_ID, 0, "observed_thread", 190)
        other = dialogue_mvp.stable_root_id("linked_discussion", DISCUSSION_ID - 1, 0, "observed_thread", 190)
        self.assertNotEqual(linked, other)
        code, _ = self.call(update(214, chat=DISCUSSION_ID - 1, trigger="command", thread=190))
        self.assertEqual(code, 422)
        self.assertFalse(self.provider.calls)
        self.assertFalse(self.telegram.calls)

    def test_root_t10_direct_topic_change_is_mode_scoped_no_merge(self):
        self.call(update(215, trigger="command", thread=200, direct_topic=3001, text="topic-a"))
        a = self._root_row(215)
        self.call(update(216, trigger="command", thread=200, direct_topic=3002, text="topic-b"))
        b = self._root_row(216)
        self.assertNotEqual(a["stable_conversation_root_id"], b["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_root_t11_privacy_persists_only_bounded_reply_root_scalars(self):
        payload = update(217, trigger="command", thread=210, text="SAFE_TRANSCRIPT")
        payload["message"]["from"]["username"] = "DROP_USERNAME"
        self.call(payload)
        row = dict(self.store.db.execute("SELECT * FROM updates WHERE update_id=217").fetchone())
        serialized = json.dumps(row, sort_keys=True)
        self.assertNotIn("DROP_USERNAME", serialized)
        self.assertNotIn("SAFE_TRANSCRIPT", serialized)
        forbidden = {"raw_update", "full_message", "username", "display_name", "provider_response"}
        self.assertFalse(forbidden.intersection(row))
        required = {"inbound_reply_to_message_id", "inbound_reply_to_message_thread_id",
                    "stable_conversation_root_id", "root_derivation_class", "root_evidence_update_id"}
        self.assertTrue(required.issubset(row))

    def test_root_t12_parameterized_exact_fixture_no_numeric_semantic_hardcode(self):
        A = 31337
        self.call(update(218, trigger="command", thread=A, text="fixture-turn1"))
        first = self._root_row(218)
        B = first["outbound_message_id"]
        self.assertNotEqual(A, B)
        self.call(update(219, trigger="reply", thread=B, reply_target=B, reply_thread=A, text="fixture-turn2"))
        second = self._root_row(219)
        self.assertEqual(second["message_thread_id"], B)
        self.assertEqual(second["inbound_reply_to_message_id"], B)
        self.assertEqual(second["root_derivation_class"], "PROVEN_OUTBOUND_LINEAGE")
        self.assertEqual(second["stable_conversation_root_id"], first["stable_conversation_root_id"])
        self.assertEqual(second["root_conversation_key"], first["root_conversation_key"])
        self.assertEqual(self.provider.calls[1][1][0]["content"], "fixture-turn1")

    def test_root_t13_ambiguous_outbound_lookup_isolated_no_wrong_merge(self):
        self.call(update(220, trigger="command", thread=220, text="base"))
        base = self._root_row(220)
        fake_root = "f" * 64
        fake_key = dialogue_mvp.root_conversation_key(fake_root)
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id,"
            "stable_conversation_root_id,root_derivation_class,root_evidence_update_id,root_conversation_key) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (191, "ambiguous", "COMMITTED", "legacy-ambiguous", None, 291, 999, 0, "command",
             base["outbound_message_id"], DISCUSSION_ID, fake_root, "OBSERVED_LINKED_THREAD_ANCHOR", 191, fake_key),
        )
        self.call(update(221, trigger="reply", thread=220, reply_target=base["outbound_message_id"], text="ambiguous"))
        r = self._root_row(221)
        self.assertEqual(r["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertNotEqual(r["stable_conversation_root_id"], base["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    # I1 correction regressions: raw cardinality before eligibility.
    def test_i1_t1_eligible_rooted_plus_legacy_null_duplicate_no_merge(self):
        self.call(update(301, trigger="command", thread=301, text="base-i1-t1"))
        base = self._root_row(301)
        target = base["outbound_message_id"]
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (401, "i1-t1-null", "COMMITTED", "legacy-null", None, 501, 301, 0, "command",
             target, DISCUSSION_ID),
        )
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 2)
        self.call(update(302, trigger="reply", thread=301, reply_target=target, text="reply-i1-t1"))
        row = self._root_row(302)
        self.assertEqual(row["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertNotEqual(row["stable_conversation_root_id"], base["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_i1_t2_eligible_rooted_plus_ineligible_state_duplicate_no_merge(self):
        self.call(update(303, trigger="command", thread=303, text="base-i1-t2"))
        base = self._root_row(303)
        target = base["outbound_message_id"]
        fake_root = "a" * 64
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id,"
            "stable_conversation_root_id,root_derivation_class,root_evidence_update_id,root_conversation_key) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (402, "i1-t2-state", "SENDING", "ineligible-state", None, 502, 303, 0, "command",
             target, DISCUSSION_ID, fake_root, "OBSERVED_LINKED_THREAD_ANCHOR", 402,
             dialogue_mvp.root_conversation_key(fake_root)),
        )
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 2)
        self.call(update(304, trigger="reply", thread=303, reply_target=target, text="reply-i1-t2"))
        row = self._root_row(304)
        self.assertEqual(row["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertNotEqual(row["stable_conversation_root_id"], base["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_i1_t3_eligible_rooted_plus_mode_conflicting_duplicate_no_merge(self):
        self.call(update(305, trigger="command", thread=305, text="base-i1-t3"))
        base = self._root_row(305)
        target = base["outbound_message_id"]
        fake_root = "b" * 64
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id,"
            "stable_conversation_root_id,root_derivation_class,root_evidence_update_id,root_conversation_key) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (403, "i1-t3-mode", "COMMITTED", "mode-conflict", None, 503, 305, 3001, "command",
             target, DISCUSSION_ID, fake_root, "OBSERVED_LINKED_THREAD_ANCHOR", 403,
             dialogue_mvp.root_conversation_key(fake_root)),
        )
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 2)
        self.call(update(306, trigger="reply", thread=305, reply_target=target, text="reply-i1-t3"))
        row = self._root_row(306)
        self.assertEqual(row["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertNotEqual(row["stable_conversation_root_id"], base["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_i1_t4_unique_eligible_row_proves_outbound_lineage(self):
        self.call(update(307, trigger="command", thread=307, text="base-i1-t4"))
        base = self._root_row(307)
        target = base["outbound_message_id"]
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 1)
        self.call(update(308, trigger="reply", thread=target, reply_target=target, text="reply-i1-t4"))
        row = self._root_row(308)
        self.assertEqual(row["root_derivation_class"], "PROVEN_OUTBOUND_LINEAGE")
        self.assertEqual(row["stable_conversation_root_id"], base["stable_conversation_root_id"])
        self.assertEqual(row["root_conversation_key"], base["root_conversation_key"])
        self.assertEqual(self.provider.calls[1][1][0]["content"], "base-i1-t4")

    def test_i1_t5_unique_legacy_null_row_no_merge(self):
        target = 9905
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (404, "i1-t5-null", "COMMITTED", "legacy-null-unique", None, 504, 309, 0, "command",
             target, DISCUSSION_ID),
        )
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 1)
        self.call(update(309, trigger="reply", thread=309, reply_target=target, text="reply-i1-t5"))
        row = self._root_row(309)
        self.assertEqual(row["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertEqual(len(self.provider.calls[0][1]), 1)

    def test_i1_t6_zero_raw_match_no_merge(self):
        target = 9906
        self.assertEqual(self._raw_relation_count(DISCUSSION_ID, target), 0)
        self.call(update(310, trigger="reply", thread=310, reply_target=target, text="reply-i1-t6"))
        row = self._root_row(310)
        self.assertEqual(row["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertEqual(len(self.provider.calls[0][1]), 1)

    def test_root_t14_conflicting_anchor_without_lineage_isolated(self):
        self.call(update(222, trigger="command", thread=230, text="anchor"))
        anchor = self._root_row(222)
        fake_root = "e" * 64
        fake_key = dialogue_mvp.root_conversation_key(fake_root)
        self.store.db.execute(
            "INSERT INTO updates(update_id,request_digest,state,conversation_key,error_class,inbound_message_id,"
            "message_thread_id,direct_topic_id,trigger_class,outbound_message_id,returned_chat_id,"
            "stable_conversation_root_id,root_derivation_class,root_evidence_update_id,root_conversation_key) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (192, "conflict-anchor", "COMMITTED", "legacy-conflict", None, 292, 230, 0, "command",
             9992, DISCUSSION_ID, fake_root, "OBSERVED_LINKED_THREAD_ANCHOR", 192, fake_key),
        )
        self.call(update(223, trigger="command", thread=230, text="new"))
        r = self._root_row(223)
        self.assertEqual(r["root_derivation_class"], "ISOLATED_UNRESOLVED")
        self.assertNotEqual(r["stable_conversation_root_id"], anchor["stable_conversation_root_id"])
        self.assertEqual(len(self.provider.calls[1][1]), 1)

    def test_root_t15_auto_forward_deferred_no_root_no_tester_widening_no_effect(self):
        # Even an otherwise allowlisted/addressed synthetic event is diverted before claim/root/provider/send.
        payload = update(224, user=101, trigger="command", thread=240, is_automatic_forward=True)
        code, out = self.call(payload)
        self.assertEqual((code, out["outcome"]), (200, "ignored_not_addressed"))
        self.assertEqual(self.cfg.allowed_user_ids, (101, 202))
        self.assertEqual(self.store.db.execute("SELECT COUNT(*) FROM updates").fetchone()[0], 0)
        self.assertEqual((len(self.provider.calls), len(self.telegram.calls)), (0, 0))

    def test_root_t16_forum_and_linked_discussion_namespaces_are_distinct(self):
        linked = dialogue_mvp.stable_root_id("linked_discussion", DISCUSSION_ID, 0, "observed_thread", 250)
        forum = dialogue_mvp.stable_root_id("forum", DISCUSSION_ID, 0, "observed_thread", 250)
        self.assertNotEqual(linked, forum)
        self.assertNotIn("PROVEN_AUTO_FORWARD_ROOT", dialogue_mvp.ROOT_DERIVATION_CLASSES)

    def test_root_decision_is_durable_before_provider_history_effect(self):
        observed = []
        def inspect(instructions, history):
            row = self.store.db.execute(
                "SELECT state,stable_conversation_root_id,root_conversation_key,root_derivation_class "
                "FROM updates WHERE update_id=225").fetchone()
            observed.append(tuple(row))
            return "ok"
        self.provider.respond = inspect
        self.call(update(225, trigger="command", thread=260, text="ordering"))
        self.assertEqual(observed[0][0], "CLAIMED")
        self.assertIsNotNone(observed[0][1])
        self.assertIsNotNone(observed[0][2])
        self.assertEqual(observed[0][3], "OBSERVED_LINKED_THREAD_ANCHOR")

    def test_root_fallback_committed_outbound_is_eligible_lineage(self):
        self.provider.fail = True
        self.call(update(226, trigger="command", thread=270, text="fallback-root"))
        first = self._root_row(226)
        self.assertEqual(first["state"], "FALLBACK_COMMITTED")
        self.provider.fail = False
        self.call(update(227, trigger="reply", thread=271, reply_target=first["outbound_message_id"], text="after-fallback"))
        second = self._root_row(227)
        self.assertEqual(second["root_derivation_class"], "PROVEN_OUTBOUND_LINEAGE")
        self.assertEqual(second["stable_conversation_root_id"], first["stable_conversation_root_id"])

    def test_root_migration_from_current_observability_schema_additive_idempotent_no_backfill(self):
        path = str(Path(self.tmp.name) / "observability-predecessor.sqlite")
        db = sqlite3.connect(path)
        db.executescript("""
        CREATE TABLE updates(
          update_id INTEGER PRIMARY KEY,request_digest TEXT NOT NULL,state TEXT NOT NULL,
          conversation_key TEXT NOT NULL,telegram_message_id INTEGER,error_class TEXT,
          inbound_message_id INTEGER,message_thread_id INTEGER,direct_topic_id INTEGER,trigger_class TEXT,
          outbound_message_id INTEGER,returned_chat_id INTEGER,returned_message_thread_id INTEGER,
          returned_direct_topic_id INTEGER,returned_is_topic_message INTEGER
        );
        CREATE TABLE messages(conversation_key TEXT NOT NULL,sequence INTEGER NOT NULL,role TEXT NOT NULL,
          content TEXT NOT NULL,PRIMARY KEY(conversation_key,sequence),CHECK(role IN ('user','assistant')));
        CREATE TABLE runtime_meta(key TEXT PRIMARY KEY,value INTEGER NOT NULL);
        INSERT INTO updates VALUES(5,'digest','COMMITTED','historical-r02',101,NULL,111,110,0,'command',112,
          -1002429106148,NULL,NULL,NULL);
        INSERT INTO messages VALUES('historical-r02',1,'user','legacy-history');
        """)
        db.commit(); db.close()
        first = Store(path)
        try:
            cols1 = first._column_names()
            row = first.db.execute("SELECT conversation_key,stable_conversation_root_id,root_conversation_key FROM updates WHERE update_id=5").fetchone()
            self.assertEqual(row["conversation_key"], "historical-r02")
            self.assertIsNone(row["stable_conversation_root_id"])
            self.assertIsNone(row["root_conversation_key"])
            self.assertEqual(first.db.execute("SELECT content FROM messages").fetchone()[0], "legacy-history")
        finally:
            first.db.close()
        second = Store(path)
        try:
            self.assertEqual(second._column_names(), cols1)
            row = second.db.execute("SELECT conversation_key,stable_conversation_root_id,root_conversation_key FROM updates WHERE update_id=5").fetchone()
            self.assertEqual(tuple(row), ("historical-r02", None, None))
        finally:
            second.db.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
