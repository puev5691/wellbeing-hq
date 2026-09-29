#!/usr/bin/env python3
import io
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("dialogue_mvp.py")
SPEC = importlib.util.spec_from_file_location("dialogue_mvp", MODULE_PATH)
dialogue_mvp = importlib.util.module_from_spec(SPEC)
sys.modules["dialogue_mvp"] = dialogue_mvp
SPEC.loader.exec_module(dialogue_mvp)
Config = dialogue_mvp.Config
DialogueApplication = dialogue_mvp.DialogueApplication
OpenAIResponsesAdapter = dialogue_mvp.OpenAIResponsesAdapter
ProviderFailure = dialogue_mvp.ProviderFailure
SafeLogger = dialogue_mvp.SafeLogger
Store = dialogue_mvp.Store

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


def update(uid=1, user=101, chat=DISCUSSION_ID, text="Привет", thread=0, trigger="mention", chat_type="supergroup"):
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
        msg["reply_to_message"] = {"message_id": 77, "from": {"id": BOT_ID, "is_bot": True}}
    elif trigger == "ambient":
        msg["text"] = text
    else:
        raise AssertionError("unknown synthetic trigger")
    if thread:
        msg["message_thread_id"] = thread
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
        return 700 + len(self.calls)


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
        for n in range(1, 9): self.call(update(n, text="turn" + str(n)))
        count = self.store.db.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
        self.assertLessEqual(count, self.cfg.max_history_messages)
        self.assertLessEqual(len(self.provider.calls[-1][1]), self.cfg.max_history_messages)


if __name__ == "__main__":
    unittest.main(verbosity=2)
