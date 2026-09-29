#!/usr/bin/env python3
"""Closed-pilot Telegram -> Entity -> OpenAI dialogue runtime candidate r0.1.

Python 3.10+, standard library only. Network transports are dependency-injected;
offline tests use fakes and perform no network or credential access.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import sqlite3
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol, TextIO

SCHEMA = "TELEGRAM_ENTITY_DIALOGUE_MVP_R01"
MAX_PROVIDER_RESPONSE_BYTES = 65_536
TELEGRAM_TEXT_LIMIT = 4096
CREDENTIAL_SLOTS = ("telegram_bot_token", "openai_api_key")


class BoundaryError(RuntimeError):
    pass


class InputRejected(ValueError):
    pass


class ProviderFailure(RuntimeError):
    pass


class TelegramFailure(RuntimeError):
    pass


def _require_exact_int(value: Any, code: str) -> int:
    if type(value) is not int:
        raise InputRejected(code)
    return value


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def clip_telegram_text(text: str) -> str:
    if type(text) is not str or not text.strip():
        raise ProviderFailure("assistant_text_missing")
    text = text.strip()
    return text if len(text) <= TELEGRAM_TEXT_LIMIT else text[: TELEGRAM_TEXT_LIMIT - 1] + "…"


@dataclass(frozen=True)
class Config:
    environment: str
    database_path: str
    testers_allow_path: str
    allowed_user_ids: tuple[int, ...]
    allowed_chat_ids: tuple[int, ...]
    allowed_chat_types: tuple[str, ...]
    model: str
    max_output_tokens: int
    provider_timeout_seconds: int
    telegram_timeout_seconds: int
    poll_timeout_seconds: int
    poll_retry_seconds: int
    max_input_bytes: int
    max_history_messages: int
    max_history_bytes: int
    max_update_records_per_conversation: int
    fallback_text: str
    entity_bootstrap_path: str

    @classmethod
    def from_dict(cls, raw: Any, allowed_ids: tuple[int, ...]) -> "Config":
        expected = {
            "schema", "environment", "database_path", "testers_allow_path", "allowed_chat_types",
            "model", "max_output_tokens", "provider_timeout_seconds", "telegram_timeout_seconds",
            "poll_timeout_seconds", "poll_retry_seconds", "max_input_bytes", "max_history_messages",
            "max_history_bytes", "max_update_records_per_conversation", "fallback_text", "entity_bootstrap_path",
        }
        if type(raw) is not dict or set(raw) != expected or raw.get("schema") != SCHEMA:
            raise BoundaryError("config_schema_invalid")
        if raw["environment"] not in ("closed_pilot", "test"):
            raise BoundaryError("environment_invalid")
        if type(raw["database_path"]) is not str or not raw["database_path"].startswith("/"):
            raise BoundaryError("database_path_must_be_absolute")
        if type(raw["testers_allow_path"]) is not str or not raw["testers_allow_path"].startswith("/"):
            raise BoundaryError("testers_allow_path_must_be_absolute")
        if type(allowed_ids) is not tuple or not allowed_ids or any(type(x) is not int for x in allowed_ids) or len(allowed_ids) != len(set(allowed_ids)):
            raise BoundaryError("tester_allowlist_invalid")
        if (type(raw["allowed_chat_types"]) is not list or not raw["allowed_chat_types"]
                or any(type(x) is not str for x in raw["allowed_chat_types"])
                or set(raw["allowed_chat_types"]) - {"private"}):
            raise BoundaryError("allowed_chat_types_invalid")
        if type(raw["model"]) is not str or not raw["model"].strip():
            raise BoundaryError("model_invalid")
        limits = {
            "max_output_tokens": (64, 4096), "provider_timeout_seconds": (1, 120),
            "telegram_timeout_seconds": (1, 60), "max_input_bytes": (1, 16384),
            "max_history_messages": (2, 64), "max_history_bytes": (1024, 262144),
            "poll_timeout_seconds": (1, 50), "poll_retry_seconds": (1, 60),
            "max_update_records_per_conversation": (64, 4096),
        }
        for name, (low, high) in limits.items():
            value = raw[name]
            if type(value) is not int or not low <= value <= high:
                raise BoundaryError(name + "_invalid")
        if type(raw["fallback_text"]) is not str or not raw["fallback_text"].strip() or len(raw["fallback_text"]) > TELEGRAM_TEXT_LIMIT:
            raise BoundaryError("fallback_text_invalid")
        if type(raw["entity_bootstrap_path"]) is not str or not raw["entity_bootstrap_path"].startswith("/"):
            raise BoundaryError("entity_bootstrap_path_must_be_absolute")
        return cls(
            environment=raw["environment"], database_path=raw["database_path"], testers_allow_path=raw["testers_allow_path"],
            allowed_user_ids=allowed_ids, allowed_chat_ids=allowed_ids,
            allowed_chat_types=tuple(raw["allowed_chat_types"]), model=raw["model"],
            max_output_tokens=raw["max_output_tokens"], provider_timeout_seconds=raw["provider_timeout_seconds"],
            telegram_timeout_seconds=raw["telegram_timeout_seconds"], poll_timeout_seconds=raw["poll_timeout_seconds"],
            poll_retry_seconds=raw["poll_retry_seconds"], max_input_bytes=raw["max_input_bytes"],
            max_history_messages=raw["max_history_messages"], max_history_bytes=raw["max_history_bytes"],
            max_update_records_per_conversation=raw["max_update_records_per_conversation"],
            fallback_text=raw["fallback_text"], entity_bootstrap_path=raw["entity_bootstrap_path"],
        )


class SafeLogger:
    """Allowlisted operational events only: no content, identity, token, URL or exception text."""
    EVENTS = {"request", "provider", "telegram", "runtime"}
    OUTCOMES = {"accepted", "rejected", "complete", "fallback", "duplicate", "conflict", "uncertain", "ready", "stopped"}

    def __init__(self, stream: TextIO | None = None):
        self.stream = stream if stream is not None else io.StringIO()

    def emit(self, event: str, outcome: str, status: int = 0) -> None:
        if event not in self.EVENTS or outcome not in self.OUTCOMES or type(status) is not int or status < 0:
            raise BoundaryError("log_value_not_allowlisted")
        self.stream.write(json.dumps({"event": event, "outcome": outcome, "status": status}, sort_keys=True, separators=(",", ":")) + "\n")
        self.stream.flush()


@dataclass(frozen=True)
class InboundMessage:
    update_id: int
    message_id: int
    chat_id: int
    user_id: int
    chat_type: str
    thread_id: int
    direct_topic_id: int
    text: str
    update_digest: str

    @property
    def conversation_key(self) -> str:
        return hashlib.sha256(f"tg-dialogue-r01\0{self.chat_id}\0{self.thread_id}\0{self.direct_topic_id}".encode()).hexdigest()


def parse_update(raw: Any, config: Config) -> InboundMessage:
    if type(raw) is not dict or type(raw.get("update_id")) is not int or type(raw.get("message")) is not dict:
        raise InputRejected("text_message_required")
    msg = raw["message"]
    chat = msg.get("chat")
    sender = msg.get("from")
    if type(chat) is not dict or type(sender) is not dict or type(msg.get("text")) is not str:
        raise InputRejected("text_message_required")
    chat_id = _require_exact_int(chat.get("id"), "chat_id_invalid")
    user_id = _require_exact_int(sender.get("id"), "user_id_invalid")
    message_id = _require_exact_int(msg.get("message_id"), "message_id_invalid")
    chat_type = chat.get("type")
    if chat_type not in config.allowed_chat_types or chat_id not in config.allowed_chat_ids or user_id not in config.allowed_user_ids:
        raise InputRejected("tester_not_admitted")
    # The r0.1 closed pilot is private-chat only. This closes sender/chat ambiguity.
    if chat_type == "private" and chat_id != user_id:
        raise InputRejected("private_identity_mismatch")
    text = msg["text"].strip()
    if not text or len(text.encode("utf-8")) > config.max_input_bytes:
        raise InputRejected("text_size_invalid")
    thread_id = msg.get("message_thread_id", 0)
    if type(thread_id) is not int or thread_id < 0:
        raise InputRejected("thread_id_invalid")
    topic = msg.get("direct_messages_topic")
    direct_topic_id = 0
    if topic is not None:
        if type(topic) is not dict or type(topic.get("topic_id")) is not int or topic["topic_id"] <= 0:
            raise InputRejected("direct_topic_invalid")
        direct_topic_id = topic["topic_id"]
    return InboundMessage(raw["update_id"], message_id, chat_id, user_id, chat_type, thread_id,
                          direct_topic_id, text, digest(raw))


class Provider(Protocol):
    def respond(self, instructions: str, history: list[dict[str, str]]) -> str: ...


class Telegram(Protocol):
    def send_text(self, chat_id: int, thread_id: int, direct_topic_id: int, text: str) -> int: ...


class JsonHttpsTransport:
    def post(self, url: str, headers: dict[str, str], body: dict[str, Any], timeout: int, max_bytes: int) -> dict[str, Any]:
        request = urllib.request.Request(url, data=canonical_bytes(body), headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
                data = response.read(max_bytes + 1)
                if len(data) > max_bytes:
                    raise BoundaryError("response_too_large")
                if not 200 <= response.status < 300:
                    raise BoundaryError("remote_http_failure")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise BoundaryError("remote_transport_failure") from exc
        try:
            parsed = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BoundaryError("remote_json_invalid") from exc
        if type(parsed) is not dict:
            raise BoundaryError("remote_json_invalid")
        return parsed


class OpenAIResponsesAdapter:
    ENDPOINT = "https://api.openai.com/v1/responses"

    def __init__(self, api_key: bytes, model: str, max_output_tokens: int, timeout: int, transport: JsonHttpsTransport | None = None):
        if not api_key.strip():
            raise BoundaryError("openai_credential_empty")
        try:
            self.api_key = api_key.decode("utf-8")
        except UnicodeError as exc:
            raise BoundaryError("openai_credential_invalid") from exc
        self.model = model
        self.max_output_tokens = max_output_tokens
        self.timeout = timeout
        self.transport = transport or JsonHttpsTransport()

    def respond(self, instructions: str, history: list[dict[str, str]]) -> str:
        body = {
            "model": self.model, "instructions": instructions, "input": history,
            "max_output_tokens": self.max_output_tokens, "store": False, "tools": [],
        }
        try:
            response = self.transport.post(self.ENDPOINT, {
                "Authorization": "Bearer " + self.api_key, "Content-Type": "application/json",
            }, body, self.timeout, MAX_PROVIDER_RESPONSE_BYTES)
        except BoundaryError as exc:
            raise ProviderFailure("provider_transport_failure") from exc
        if response.get("status") != "completed":
            raise ProviderFailure("provider_response_not_completed")
        if type(response.get("output")) is not list:
            raise ProviderFailure("provider_output_invalid")
        parts: list[str] = []
        for item in response.get("output", []):
            if type(item) is dict and item.get("type") == "message" and item.get("role") == "assistant":
                if type(item.get("content")) is not list:
                    raise ProviderFailure("provider_output_invalid")
                for content in item["content"]:
                    if type(content) is dict and content.get("type") == "output_text" and type(content.get("text")) is str:
                        parts.append(content["text"])
        return clip_telegram_text("".join(parts))


class TelegramBotAdapter:
    def __init__(self, bot_token: bytes, timeout: int, transport: JsonHttpsTransport | None = None):
        if not bot_token.strip():
            raise BoundaryError("telegram_credential_empty")
        try:
            self.bot_token = bot_token.decode("utf-8")
        except UnicodeError as exc:
            raise BoundaryError("telegram_credential_invalid") from exc
        self.timeout = timeout
        self.transport = transport or JsonHttpsTransport()

    def get_updates(self, offset: int, poll_timeout: int) -> list[dict[str, Any]]:
        try:
            response = self.transport.post(
                f"https://api.telegram.org/bot{self.bot_token}/getUpdates",
                {"Content-Type": "application/json"},
                {"offset": offset, "limit": 10, "timeout": poll_timeout, "allowed_updates": ["message"]},
                poll_timeout + self.timeout, MAX_PROVIDER_RESPONSE_BYTES,
            )
        except BoundaryError as exc:
            raise TelegramFailure("get_updates_transport_failure") from exc
        result = response.get("result")
        if response.get("ok") is not True or type(result) is not list or any(type(x) is not dict for x in result):
            raise TelegramFailure("get_updates_failed")
        return result

    def send_text(self, chat_id: int, thread_id: int, direct_topic_id: int, text: str) -> int:
        body: dict[str, Any] = {"chat_id": chat_id, "text": clip_telegram_text(text)}
        if thread_id:
            body["message_thread_id"] = thread_id
        if direct_topic_id:
            body["direct_messages_topic_id"] = direct_topic_id
        try:
            response = self.transport.post(
                f"https://api.telegram.org/bot{self.bot_token}/sendMessage",
                {"Content-Type": "application/json"}, body, self.timeout, MAX_PROVIDER_RESPONSE_BYTES,
            )
        except BoundaryError as exc:
            raise TelegramFailure("send_message_transport_failure") from exc
        result = response.get("result")
        if response.get("ok") is not True or type(result) is not dict or type(result.get("message_id")) is not int:
            raise TelegramFailure("send_message_failed")
        return result["message_id"]


class Store:
    def __init__(self, path: str):
        self.lock = threading.RLock()
        self.db = sqlite3.connect(path, isolation_level=None, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS updates(
          update_id INTEGER PRIMARY KEY, request_digest TEXT NOT NULL, state TEXT NOT NULL,
          conversation_key TEXT NOT NULL, telegram_message_id INTEGER, error_class TEXT
        );
        CREATE TABLE IF NOT EXISTS messages(
          conversation_key TEXT NOT NULL, sequence INTEGER NOT NULL, role TEXT NOT NULL,
          content TEXT NOT NULL, PRIMARY KEY(conversation_key,sequence),
          CHECK(role IN ('user','assistant'))
        );
        CREATE TABLE IF NOT EXISTS runtime_meta(
          key TEXT PRIMARY KEY, value INTEGER NOT NULL
        );
        """)

    def poll_offset(self) -> int:
        with self.lock:
            row = self.db.execute("SELECT value FROM runtime_meta WHERE key='poll_offset'").fetchone()
            return int(row[0]) if row else 0

    def set_poll_offset(self, value: int) -> None:
        if type(value) is not int or value < 0:
            raise BoundaryError("poll_offset_invalid")
        with self.lock:
            self.db.execute(
                "INSERT INTO runtime_meta(key,value) VALUES('poll_offset',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (value,),
            )

    def claim(self, event: InboundMessage) -> str:
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                row = self.db.execute("SELECT * FROM updates WHERE update_id=?", (event.update_id,)).fetchone()
                if row:
                    if row["request_digest"] != event.update_digest:
                        self.db.execute("ROLLBACK")
                        return "CONFLICT"
                    self.db.execute("COMMIT")
                    return "DUPLICATE" if row["state"] in ("COMMITTED", "FALLBACK_COMMITTED") else "UNCERTAIN"
                self.db.execute("INSERT INTO updates(update_id,request_digest,state,conversation_key) VALUES(?,?,?,?)",
                                (event.update_id, event.update_digest, "CLAIMED", event.conversation_key))
                self.db.execute("COMMIT")
                return "CLAIMED"
            except Exception:
                self.db.execute("ROLLBACK")
                raise

    def history(self, conversation_key: str, config: Config, reserve_bytes: int = 0) -> list[dict[str, str]]:
        with self.lock:
            rows = self.db.execute("SELECT role,content FROM messages WHERE conversation_key=? ORDER BY sequence DESC LIMIT ?",
                                   (conversation_key, config.max_history_messages - 1)).fetchall()[::-1]
        selected: list[dict[str, str]] = []
        total = 0
        budget = max(0, config.max_history_bytes - reserve_bytes)
        for row in reversed(rows):
            size = len(row["content"].encode("utf-8"))
            if total + size > budget:
                break
            selected.append({"role": row["role"], "content": row["content"]})
            total += size
        return selected[::-1]

    def mark(self, update_id: int, state: str, error_class: str | None = None) -> None:
        with self.lock:
            self.db.execute("UPDATE updates SET state=?,error_class=? WHERE update_id=?", (state, error_class, update_id))

    def has_unresolved(self, conversation_key: str, exclude_update_id: int) -> bool:
        with self.lock:
            return self.db.execute(
                "SELECT 1 FROM updates WHERE conversation_key=? AND update_id<>? AND state NOT IN ('COMMITTED','FALLBACK_COMMITTED') LIMIT 1",
                (conversation_key, exclude_update_id),
            ).fetchone() is not None

    def commit_turn(self, event: InboundMessage, reply: str, telegram_message_id: int) -> None:
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                row = self.db.execute("SELECT state FROM updates WHERE update_id=?", (event.update_id,)).fetchone()
                if not row or row["state"] != "SENDING":
                    raise BoundaryError("ledger_state_invalid")
                sequence = self.db.execute("SELECT COALESCE(MAX(sequence),0) FROM messages WHERE conversation_key=?",
                                           (event.conversation_key,)).fetchone()[0]
                self.db.execute("INSERT INTO messages VALUES(?,?,?,?)", (event.conversation_key, sequence + 1, "user", event.text))
                self.db.execute("INSERT INTO messages VALUES(?,?,?,?)", (event.conversation_key, sequence + 2, "assistant", reply))
                self.db.execute("UPDATE updates SET state='COMMITTED',telegram_message_id=? WHERE update_id=?",
                                (telegram_message_id, event.update_id))
                self._prune_locked(event.conversation_key, self._active_config)
                self.db.execute("COMMIT")
            except Exception:
                self.db.execute("ROLLBACK")
                raise

    def bind_config(self, config: Config) -> None:
        self._active_config = config

    def prune(self, conversation_key: str, config: Config) -> None:
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                self._prune_locked(conversation_key, config)
                self.db.execute("COMMIT")
            except Exception:
                self.db.execute("ROLLBACK")
                raise

    def _prune_locked(self, conversation_key: str, config: Config) -> None:
        keep_messages = config.max_history_messages
        self.db.execute(
            "DELETE FROM messages WHERE conversation_key=? AND sequence NOT IN "
            "(SELECT sequence FROM messages WHERE conversation_key=? ORDER BY sequence DESC LIMIT ?)",
            (conversation_key, conversation_key, keep_messages),
        )
        self.db.execute(
            "DELETE FROM updates WHERE conversation_key=? AND state IN ('COMMITTED','FALLBACK_COMMITTED') AND update_id NOT IN "
            "(SELECT update_id FROM updates WHERE conversation_key=? ORDER BY update_id DESC LIMIT ?)",
            (conversation_key, conversation_key, config.max_update_records_per_conversation),
        )


class DialogueApplication:
    def __init__(self, config: Config, store: Store, provider: Provider, telegram: Telegram,
                 instructions: str, logger: SafeLogger):
        if not instructions.strip() or len(instructions.encode("utf-8")) > 16_384:
            raise BoundaryError("entity_bootstrap_invalid")
        self.config, self.store, self.provider, self.telegram = config, store, provider, telegram
        self.instructions, self.logger = instructions, logger
        self.store.bind_config(config)
        self._lock_guard = threading.Lock()
        self._conversation_locks: dict[str, threading.Lock] = {}

    def _conversation_lock(self, key: str) -> threading.Lock:
        with self._lock_guard:
            return self._conversation_locks.setdefault(key, threading.Lock())

    def process_update(self, raw: Any) -> tuple[int, dict[str, Any]]:
        try:
            event = parse_update(raw, self.config)
        except (InputRejected, ValueError):
            self.logger.emit("request", "rejected", 422)
            return 422, {"ok": False, "outcome": "rejected"}
        claim = self.store.claim(event)
        if claim == "CONFLICT":
            self.logger.emit("request", "conflict", 409)
            return 409, {"ok": False, "outcome": "update_id_conflict"}
        if claim == "DUPLICATE":
            self.logger.emit("request", "duplicate", 200)
            return 200, {"ok": True, "outcome": "duplicate"}
        if claim == "UNCERTAIN":
            self.logger.emit("request", "uncertain", 503)
            return 503, {"ok": False, "outcome": "manual_reconciliation_required"}
        with self._conversation_lock(event.conversation_key):
            if self.store.has_unresolved(event.conversation_key, event.update_id):
                self.store.mark(event.update_id, "OUTCOME_UNKNOWN", "prior_turn_unresolved")
                self.logger.emit("request", "uncertain", 503)
                return 503, {"ok": False, "outcome": "manual_reconciliation_required"}
            history = self.store.history(event.conversation_key, self.config, len(event.text.encode("utf-8")))
            history.append({"role": "user", "content": event.text})
            try:
                reply = self.provider.respond(self.instructions, history)
                self.store.mark(event.update_id, "SENDING")
                sent_id = self.telegram.send_text(event.chat_id, event.thread_id, event.direct_topic_id, reply)
                self.store.commit_turn(event, reply, sent_id)
                self.logger.emit("request", "complete", 200)
                return 200, {"ok": True, "outcome": "replied"}
            except ProviderFailure:
                self.store.mark(event.update_id, "SENDING_FALLBACK", "provider_failure")
                try:
                    sent_id = self.telegram.send_text(event.chat_id, event.thread_id, event.direct_topic_id, self.config.fallback_text)
                    with self.store.lock:
                        self.store.db.execute("UPDATE updates SET state='FALLBACK_COMMITTED',telegram_message_id=? WHERE update_id=?",
                                              (sent_id, event.update_id))
                    self.store.prune(event.conversation_key, self.config)
                    self.logger.emit("provider", "fallback", 200)
                    return 200, {"ok": True, "outcome": "fallback_sent"}
                except TelegramFailure:
                    self.store.mark(event.update_id, "OUTCOME_UNKNOWN", "fallback_send_unknown")
            except (TelegramFailure, BoundaryError):
                self.store.mark(event.update_id, "OUTCOME_UNKNOWN", "reply_send_unknown")
        self.logger.emit("request", "uncertain", 503)
        return 503, {"ok": False, "outcome": "manual_reconciliation_required"}


def credential(slot: str) -> bytes:
    if slot not in CREDENTIAL_SLOTS:
        raise BoundaryError("credential_slot_invalid")
    root = os.environ.get("CREDENTIALS_DIRECTORY")
    if not root:
        raise BoundaryError("credentials_directory_missing")
    try:
        value = (Path(root) / slot).read_bytes().rstrip(b"\r\n")
    except OSError as exc:
        raise BoundaryError("credential_unavailable") from exc
    if not value or len(value) > 16_384:
        raise BoundaryError("credential_invalid")
    return value


def load_allowlist(path: str) -> tuple[int, ...]:
    try:
        lines = Path(path).read_text(encoding="ascii").splitlines()
    except (OSError, UnicodeError) as exc:
        raise BoundaryError("tester_allowlist_unavailable") from exc
    values: list[int] = []
    for line in lines:
        if not line or not line.isdecimal():
            raise BoundaryError("tester_allowlist_invalid")
        value = int(line)
        if value <= 0:
            raise BoundaryError("tester_allowlist_invalid")
        values.append(value)
    if not values or len(values) != len(set(values)):
        raise BoundaryError("tester_allowlist_invalid")
    return tuple(values)


def load_runtime(config_path: str, stream: TextIO) -> tuple[Config, Store, DialogueApplication]:
    raw = json.loads(Path(config_path).read_text(encoding="utf-8"))
    if type(raw) is not dict or type(raw.get("testers_allow_path")) is not str:
        raise BoundaryError("config_schema_invalid")
    config = Config.from_dict(raw, load_allowlist(raw["testers_allow_path"]))
    if config.environment != "closed_pilot":
        raise BoundaryError("closed_pilot_environment_required")
    instructions = Path(config.entity_bootstrap_path).read_text(encoding="utf-8")
    store = Store(config.database_path)
    telegram = TelegramBotAdapter(credential("telegram_bot_token"), config.telegram_timeout_seconds)
    app = DialogueApplication(
        config, store,
        OpenAIResponsesAdapter(credential("openai_api_key"), config.model, config.max_output_tokens, config.provider_timeout_seconds),
        telegram, instructions, SafeLogger(stream),
    )
    return config, store, app


def poll_forever(config: Config, store: Store, app: DialogueApplication, telegram: TelegramBotAdapter) -> None:
    offset = store.poll_offset()
    while True:
        try:
            updates = telegram.get_updates(offset, config.poll_timeout_seconds)
            for raw in updates:
                update_id = raw.get("update_id")
                if type(update_id) is not int or update_id < offset:
                    app.logger.emit("telegram", "rejected", 0)
                    continue
                app.process_update(raw)
                offset = update_id + 1
                store.set_poll_offset(offset)
        except TelegramFailure:
            app.logger.emit("telegram", "uncertain", 0)
            time.sleep(config.poll_retry_seconds)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("check-config", "poll"))
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    try:
        raw = json.loads(Path(args.config).read_text(encoding="utf-8"))
        if type(raw) is not dict or type(raw.get("testers_allow_path")) is not str:
            raise BoundaryError("config_schema_invalid")
        config = Config.from_dict(raw, load_allowlist(raw["testers_allow_path"]))
        if args.command == "check-config":
            Path(config.entity_bootstrap_path).read_text(encoding="utf-8")
            print(json.dumps({"ok": True, "schema": SCHEMA}, separators=(",", ":")))
            return 0
        config, store, app = load_runtime(args.config, sys.stdout)
        app.logger.emit("runtime", "ready", 0)
        try:
            poll_forever(config, store, app, app.telegram)
        finally:
            store.db.close(); app.logger.emit("runtime", "stopped", 0)
        return 0
    except (BoundaryError, OSError, ValueError, json.JSONDecodeError, sqlite3.Error):
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
