# Telegram Phase 1B privacy-safe logging contract r01

Status: non-production candidate. This contract does not authorize deployment or live Telegram traffic.

## Closed allowlist

Application logs may contain only the fields implemented by `PrivacySafeLogger`:

- `event`: bounded operational enum;
- `status`: bounded operational enum;
- `error_class`: bounded generic error enum;
- `http_status`: non-negative integer;
- `request_bytes`: non-negative integer;
- `transport`: `fake` or `real_blocked`.

No arbitrary string value from an inbound update is accepted by the logger.

## Forbidden persistent log material

Application/debug/error/retry logs must not contain or persist:

- raw Telegram update JSON or request body;
- raw comment/message text;
- audience user IDs;
- usernames, first/last/display names;
- peer/client IP address;
- request headers, including future webhook secret;
- query string;
- bot token or credential contents;
- local-variable dumps or traceback dumps carrying request objects;
- retry/dead-letter bodies.

The candidate has no application retry queue or dead-letter body store. Error responses are generic and never echo the request payload.

## Debug/crash boundary

`runtime_app.py` does not log exception text, traceback or locals. Unexpected exceptions are reduced to the bounded `internal_error` class.

The candidate systemd unit sets `LimitCORE=0`. SIS must independently verify the effective unit property and host coredump behavior after a separately authorized non-production deployment. Application privacy PASS does not substitute for that host check.

## Journal boundary

Candidate application output is JSON-lines to stdout/stderr for journald. The application emits only the allowlisted fields above. SIS should verify the instantiated unit has no wrapper, proxy, service manager or debug tooling that captures stdin/body/locals outside this contract.

## Proxy boundary

The application listener contract is exactly `127.0.0.1:8782` and path `/telegram/webhook`.

If a reverse proxy is later provisioned, its access/error log format must exclude request bodies, request headers, query strings, upstream bodies, and credential values. A proxy may log bounded transport metadata such as status/bytes/duration only if SIS confirms it cannot include Telegram payload or audience identity.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть application logging side SIS B2 без live Telegram/production
СТАТУС: candidate_privacy_safe_logging_contract
