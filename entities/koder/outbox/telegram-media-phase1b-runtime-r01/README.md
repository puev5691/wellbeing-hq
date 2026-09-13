# Telegram Media Gateway Phase 1B runtime/privacy candidate r01

Status: bounded non-production candidate; fake transport only; zero live Telegram; zero real credentials; no host deployment.

Base privacy package is accepted at:
`entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
commit `cd81bbd98a4be334388f95ea948427d91fa82a05`.

This package keeps the accepted `gateway.py`, `test_gateway.py`, `cleanup_sandbox.py`, `test_cleanup.py` and `runtime-config.schema.json` byte-identical and adds only the runtime/application boundary required to remediate SIS blocker B2.

Core additions:

- `runtime_app.py`: loopback-only webhook application candidate wrapping accepted `Gateway`;
- `test_runtime_app.py`: synthetic privacy/logging/runtime tests;
- `LOGGING-CONTRACT.md`: closed allowlist logging contract;
- `RUNTIME-CONTRACT.md`: exact SIS service principal, paths, permissions, credentials, no-core and proxy requirements;
- `systemd/wellbeing-telegram-phase1b-sandbox.service`: non-installed candidate unit.

Hard boundaries:

- privacy mode remains exactly `aggregate_only`;
- exact sandbox DB remains `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- listener contract is `127.0.0.1:8782` only;
- candidate unit blocks non-loopback IP traffic;
- `real` transport is intentionally not implemented and fails closed;
- no Telegram API client or webhook registration exists in r01;
- no credential values are in repository content;
- no raw request/update body, audience identity or raw comment is permitted in application logs;
- no application retry/dead-letter body store exists;
- systemd candidate sets `LimitCORE=0`, subject to SIS host verification after separately authorized provisioning.

Test command:
`python3 -m unittest -v`

Compile command:
`python3 -m py_compile gateway.py test_gateway.py cleanup_sandbox.py test_cleanup.py runtime_app.py test_runtime_app.py`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: application/runtime remediation SIS B2 без live send/credentials/host deployment
СТАТУС: candidate_nonproduction_runtime_r01
