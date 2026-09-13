from __future__ import annotations

import argparse
import hmac
import io
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, TextIO

from gateway import (
    ConfigError,
    FakeTransport,
    Gateway,
    RuntimeConfig,
    SANDBOX_DB_PATH,
    TelegramBotAdapter,
    ValidationError,
)

SERVICE_PRINCIPAL = "wellbeing-tg-p1b"
SERVICE_UNIT = "wellbeing-telegram-phase1b-sandbox.service"
WORKING_DIRECTORY = "/opt/wellbeing/telegram-phase1b-runtime-r01"
CONFIG_PATH = "/etc/wellbeing/telegram-phase1b/runtime.json"
LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 8782
WEBHOOK_PATH = "/telegram/webhook"
MAX_BODY_BYTES = 262_144
CREDENTIAL_SLOTS = ("telegram_bot_token", "telegram_webhook_secret")


class RuntimeBoundaryError(RuntimeError):
    pass


class RequestRejected(ValueError):
    pass


class PrivacySafeLogger:
    """JSON-lines logger with a closed field/value vocabulary.

    It deliberately cannot accept arbitrary strings from requests, exceptions,
    headers, query strings, identities, comments, or transport payloads.
    """

    _EVENTS = {
        "runtime_start",
        "runtime_stop",
        "webhook_request",
        "http_access",
        "credential_check",
        "transport_boundary",
    }
    _STATUSES = {
        "ready",
        "accepted",
        "rejected",
        "complete",
        "missing",
        "present",
        "blocked",
    }
    _ERROR_CLASSES = {
        "none",
        "request_rejected",
        "validation_error",
        "config_error",
        "runtime_boundary_error",
        "internal_error",
    }
    _TRANSPORTS = {"fake", "real_blocked"}
    _FIELDS = {
        "event",
        "status",
        "http_status",
        "request_bytes",
        "error_class",
        "transport",
    }

    def __init__(self, stream: TextIO | None = None):
        self.stream = stream if stream is not None else io.StringIO()

    def emit(self, **fields: Any) -> None:
        unknown = set(fields) - self._FIELDS
        if unknown:
            raise RuntimeBoundaryError("logging_field_not_allowlisted")
        event = fields.get("event")
        status = fields.get("status")
        error_class = fields.get("error_class", "none")
        transport = fields.get("transport")
        if event not in self._EVENTS:
            raise RuntimeBoundaryError("logging_event_not_allowlisted")
        if status not in self._STATUSES:
            raise RuntimeBoundaryError("logging_status_not_allowlisted")
        if error_class not in self._ERROR_CLASSES:
            raise RuntimeBoundaryError("logging_error_class_not_allowlisted")
        if transport is not None and transport not in self._TRANSPORTS:
            raise RuntimeBoundaryError("logging_transport_not_allowlisted")
        for key in ("http_status", "request_bytes"):
            if key in fields and (not isinstance(fields[key], int) or fields[key] < 0):
                raise RuntimeBoundaryError("logging_integer_field_invalid")
        record = {
            "event": event,
            "status": status,
            "error_class": error_class,
        }
        for key in ("http_status", "request_bytes", "transport"):
            if key in fields:
                record[key] = fields[key]
        self.stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
        self.stream.flush()


def _error_class(exc: BaseException) -> str:
    if isinstance(exc, RequestRejected):
        return "request_rejected"
    if isinstance(exc, ValidationError):
        return "validation_error"
    if isinstance(exc, ConfigError):
        return "config_error"
    if isinstance(exc, RuntimeBoundaryError):
        return "runtime_boundary_error"
    return "internal_error"


def validate_listen_contract(host: str, port: int) -> None:
    if host != LISTEN_HOST:
        raise RuntimeBoundaryError("loopback_listen_required")
    if port != LISTEN_PORT:
        raise RuntimeBoundaryError("listen_port_must_match_contract")


def credential_path(slot: str) -> Path:
    if slot not in CREDENTIAL_SLOTS:
        raise RuntimeBoundaryError("unknown_credential_slot")
    directory = os.environ.get("CREDENTIALS_DIRECTORY")
    if not directory:
        raise RuntimeBoundaryError("credential_directory_required")
    return Path(directory) / slot


def read_runtime_credential(slot: str) -> bytes:
    path = credential_path(slot)
    try:
        value = path.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeBoundaryError("required_credential_missing") from exc
    if not value.strip():
        raise RuntimeBoundaryError("required_credential_empty")
    if len(value) > 16_384:
        raise RuntimeBoundaryError("credential_too_large")
    return value.rstrip(b"\r\n")


def build_transport(mode: str, logger: PrivacySafeLogger):
    if mode == "fake":
        logger.emit(event="transport_boundary", status="ready", transport="fake")
        return FakeTransport()
    if mode != "real":
        raise RuntimeBoundaryError("unsupported_transport_mode")
    # A future real transport may only consume credentials through systemd's
    # runtime credential directory. r01 intentionally has no network transport.
    missing = False
    for slot in CREDENTIAL_SLOTS:
        try:
            read_runtime_credential(slot)
        except RuntimeBoundaryError:
            missing = True
            break
    if missing:
        logger.emit(event="credential_check", status="missing", transport="real_blocked")
        raise RuntimeBoundaryError("real_transport_credentials_unavailable")
    logger.emit(event="credential_check", status="present", transport="real_blocked")
    raise RuntimeBoundaryError("real_transport_not_implemented_in_r01")


def compare_webhook_secret(candidate: bytes, expected: bytes) -> bool:
    # Helper for a future separately authorized real mode. Never logs either side.
    return hmac.compare_digest(candidate, expected)


class RuntimeApplication:
    def __init__(self, gateway: Gateway, logger: PrivacySafeLogger):
        if gateway.config.environment not in {"sandbox", "test"}:
            raise RuntimeBoundaryError("nonproduction_environment_required")
        if gateway.config.privacy_mode != "aggregate_only":
            raise RuntimeBoundaryError("aggregate_only_required")
        if gateway.config.environment == "sandbox" and gateway.db_path != SANDBOX_DB_PATH:
            raise RuntimeBoundaryError("sandbox_db_path_must_match_contract")
        self.gateway = gateway
        self.logger = logger

    def handle_payload_bytes(self, body: bytes) -> tuple[int, bytes]:
        size = len(body)
        if size == 0:
            exc = RequestRejected("empty_body")
            self._log_rejection(size, 400, exc)
            return 400, self._response(False, "invalid_request")
        if size > MAX_BODY_BYTES:
            exc = RequestRejected("body_too_large")
            self._log_rejection(size, 413, exc)
            return 413, self._response(False, "invalid_request")
        try:
            # Decode and parse only in memory. No body, payload, headers, peer,
            # query string, identity, or comment text is passed to the logger.
            payload = json.loads(body.decode("utf-8"))
            del body
            if not isinstance(payload, dict):
                raise RequestRejected("json_object_required")
            self.gateway.ingest_update(payload)
            # Drop the parsed payload reference before emitting the success log.
            del payload
            self.logger.emit(
                event="webhook_request",
                status="accepted",
                http_status=200,
                request_bytes=size,
            )
            return 200, self._response(True, "processed")
        except (UnicodeDecodeError, json.JSONDecodeError, RequestRejected) as exc:
            self._log_rejection(size, 400, exc)
            return 400, self._response(False, "invalid_request")
        except ValidationError as exc:
            self._log_rejection(size, 422, exc)
            return 422, self._response(False, "rejected")
        except (ConfigError, RuntimeBoundaryError) as exc:
            self._log_rejection(size, 503, exc)
            return 503, self._response(False, "runtime_unavailable")
        except Exception as exc:  # fail closed; no traceback/local dump logging
            self._log_rejection(size, 500, exc)
            return 500, self._response(False, "internal_error")

    def _log_rejection(self, size: int, status_code: int, exc: BaseException) -> None:
        self.logger.emit(
            event="webhook_request",
            status="rejected",
            http_status=status_code,
            request_bytes=size,
            error_class=_error_class(exc),
        )

    @staticmethod
    def _response(ok: bool, outcome: str) -> bytes:
        return (json.dumps({"ok": ok, "outcome": outcome}, separators=(",", ":")) + "\n").encode("utf-8")


class RuntimeHTTPServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, handler, application: RuntimeApplication):
        super().__init__(address, handler)
        self.application = application


class WebhookHandler(BaseHTTPRequestHandler):
    server_version = "Phase1BSandbox/0.1"
    sys_version = ""

    def do_POST(self):
        if self.path != WEBHOOK_PATH:
            self._send(404, RuntimeApplication._response(False, "not_found"))
            return
        content_type = self.headers.get("Content-Type", "")
        if content_type.split(";", 1)[0].strip().lower() != "application/json":
            self._send(415, RuntimeApplication._response(False, "invalid_request"))
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length < 0 or length > MAX_BODY_BYTES:
            # Do not read or echo an oversized body.
            status = 413 if length > MAX_BODY_BYTES else 400
            self.server.application.logger.emit(
                event="webhook_request",
                status="rejected",
                http_status=status,
                request_bytes=max(length, 0),
                error_class="request_rejected",
            )
            self._send(status, RuntimeApplication._response(False, "invalid_request"))
            return
        body = self.rfile.read(length)
        status, response = self.server.application.handle_payload_bytes(body)
        del body
        self._send(status, response)

    def do_GET(self):
        self._send(405, RuntimeApplication._response(False, "method_not_allowed"))

    def log_message(self, fmt, *args):
        # Disable BaseHTTPRequestHandler's peer/path/user-agent formatted log.
        # Access evidence is reduced to an operational allowlist only.
        self.server.application.logger.emit(
            event="http_access",
            status="complete",
            http_status=getattr(self, "_last_status", 0),
        )

    def _send(self, status: int, body: bytes):
        self._last_status = status
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


def load_nonsecret_config(path: str) -> RuntimeConfig:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return RuntimeConfig.from_dict(raw)


def build_application(config: RuntimeConfig, transport_mode: str, logger: PrivacySafeLogger) -> RuntimeApplication:
    if config.environment not in {"sandbox", "test"}:
        raise RuntimeBoundaryError("nonproduction_environment_required")
    transport = build_transport(transport_mode, logger)
    adapter = TelegramBotAdapter(config, transport)
    gateway = Gateway(config.sandbox_db_path, config, adapter)
    return RuntimeApplication(gateway, logger)


def run_server(config_path: str, host: str, port: int, transport_mode: str, logger: PrivacySafeLogger) -> None:
    validate_listen_contract(host, port)
    config = load_nonsecret_config(config_path)
    if config.environment != "sandbox":
        raise RuntimeBoundaryError("sandbox_environment_required_for_service")
    app = build_application(config, transport_mode, logger)
    logger.emit(event="runtime_start", status="ready", transport="fake" if transport_mode == "fake" else "real_blocked")
    server = RuntimeHTTPServer((host, port), WebhookHandler, app)
    try:
        server.serve_forever(poll_interval=0.5)
    finally:
        server.server_close()
        app.gateway.db.close()
        logger.emit(event="runtime_stop", status="complete")


def main() -> int:
    p = argparse.ArgumentParser(description="Telegram Phase 1B non-production privacy-safe webhook runtime candidate")
    p.add_argument("--config", default=CONFIG_PATH)
    p.add_argument("--listen-host", default=LISTEN_HOST)
    p.add_argument("--listen-port", type=int, default=LISTEN_PORT)
    p.add_argument("--transport", choices=("fake", "real"), default="fake")
    args = p.parse_args()
    logger = PrivacySafeLogger(stream=os.fdopen(os.dup(1), "w", encoding="utf-8", closefd=True))
    try:
        run_server(args.config, args.listen_host, args.listen_port, args.transport, logger)
    except (ConfigError, RuntimeBoundaryError, OSError, ValueError):
        # Deliberately no exception text or traceback: it may contain local/runtime data.
        logger.emit(event="runtime_stop", status="blocked", error_class="runtime_boundary_error")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
