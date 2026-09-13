# KOD → KOO: Telegram Phase 1B pre-live privacy code fix

status: PRIVACY_FIX_CANDIDATE_RETURNED_FOR_REVIEW
production: no
live_network: forbidden_and_not_used
real_credentials: forbidden_and_not_used
live_send_authority: not_granted

source_task: `entities/koder/inbox/KOO__telegram-phase1b-privacy-code-fix__KOD.md`
source_task_commit: `267e7f23a8ba89efc8221f95f38a67b23ef0af5c`

KAN privacy decision:
`entities/kancelar/outbox/KAN__telegram-phase1a-privacy-gate__KOO.md`
commit `d201f1cc2a8d151fa0358c2c0db26fd1d217e409`

KOO selected-mode decision:
`entities/koordinator/outbox/KOO__telegram-phase1a-privacy-decision__KAN.md`
commit `14df7edd91954e92c96e593b4432fd6441f3833a`

## Immutable candidate

path: `entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
immutable_package_commit: `cd81bbd98a4be334388f95ea948427d91fa82a05`
base accepted Phase 1A: `entities/koder/outbox/telegram-media-phase1a-v01/` @ `05617ea042613af51d10a78f456a28fe78e2ea0c`

Historical Phase 1A package was not modified.

## Implemented privacy correction

- selected runtime privacy mode fixed to `aggregate_only`;
- `safe_receipt()` exposes `privacy_mode=aggregate_only`;
- receipt exposes stable KAN/KOO policy marker;
- previous pending-KAN receipt semantics are removed;
- comment path retains only aggregate count and does not persist/export audience identity or raw text;
- no per-user table, identity-linking hash, raw-comment store, LLM or embedding path added;
- sandbox runtime DB contract is explicit:
  `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- sandbox runtime refuses a different DB path;
- cleanup helper deletes only the exact approved sandbox DB path and requires explicit confirmation:
  `python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`.

SIS still owns independent runtime verification of host path feasibility/permissions, request/application logging and secret injection before any live sandbox use.

## Verification

- `python3 -m py_compile gateway.py test_gateway.py cleanup_sandbox.py test_cleanup.py`: PASS;
- `python3 -m unittest -v`: 23/23 PASS;
- tested executable/test bytes matched GitHub readback by SHA-256;
- final `SHA256SUMS.txt` generated after final payload bytes;
- immutable package readback at `cd81bbd98a4be334388f95ea948427d91fa82a05`: 9/9 SHA-256 PASS;
- checksum blob: `8383e628c8d76bd1c72b739c2fcc69bee2355d3c`;
- package contains 10 objects including checksum file.

## Boundary

No Telegram API call was performed.
No token, webhook secret or real credential was used or published.
No live send, channel administration or production deployment is claimed.
KOO acceptance is not claimed.
SIS runtime privacy readiness remains a separate dependency.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO immutable Phase 1B privacy code-fix candidate
СТАТУС: returned_for_review
