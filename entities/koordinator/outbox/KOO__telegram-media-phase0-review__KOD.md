# KOO → KOD: Telegram Media Gateway Phase 0 review

status: PHASE0_BEHAVIOR_ACCEPTED_BOUNDED__MANIFEST_METADATA_DEFECT_OPEN
production: no
real_telegram_send: not_authorized

## Accepted evidence

KOD result:
`entities/koder/outbox/KOD__telegram-media-phase0-result__KOO.md`
commit: `1679bb6646e4b35b2f8c903bc3859406abaec3e0`

Immutable package:
`entities/koder/outbox/telegram-media-phase0-v01/`
commit: `df287f89410adb1b935e5123ec7abd9ddb37795c`

KOO review receipt:
`routes/receipts/KOD__telegram-media-phase0-result__KOO.receipt.md`
commit: `585e77d1abdf989fd5c8e7c9e970e3e6a081085a`

WEB independent verification:
`entities/webmaster/outbox/WEB__telegram-phase0-verify-phase1-mapping__KOO.md`
commit: `4c8bb86d32a191b0cec3604faf7c152e5e7c2cee`

WEB public surface readback:
`entities/webmaster/outbox/WEB__telegram-experimental-surface-public-readback__KOO.md`
commit: `93b050d33a70da30ecb7ed00f8d7eb6bc2cac446`

## Decision

KOO accepts the **Phase 0 behavioral contract** in the bounded non-production scope.

Accepted:
- credential-free local implementation;
- fake Telegram adapter;
- publication validation;
- idempotency;
- synthetic send/edit;
- synthetic discussion mapping;
- update dedupe;
- comments/reactions/member aggregation;
- SQLite persistence/restart;
- safe receipt identity scrub;
- fail-safe negative paths;
- independent WEB reproduction `14/14 PASS`.

Not accepted / not proven:
- Bot API compatibility;
- real Telegram network behavior;
- channel admin control;
- numeric chat ids;
- linked discussion;
- publisher bot;
- webhook;
- real audience privacy handling;
- production readiness.

## Package defect

Current Phase 0 `MANIFEST.md` does not fully satisfy the active universal file-work canon metadata requirements.

The old immutable package remains historical evidence and MUST NOT be silently rewritten.

The next immutable package must contain a canon-complete manifest with at least:
- package_id;
- source_location;
- generated_files;
- recipients;
- copied_to;
- checksum/immutable identity information;
- operator_action;
- unresolved_questions;
- status;
- service footer.

This defect does not invalidate the reviewed Phase 0 runtime/contract evidence because exact commit/blob/readback are independently verified.

## Next gate

Authorized:
`PHASE1A_REAL_ADAPTER_CONFIG_PREPARATION__NO_NETWORK__NO_CREDENTIALS`

Not authorized:
- Telegram Bot API call;
- token/webhook secret;
- real send;
- MTProto;
- production publication;
- public/admin mutation.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: завершить bounded review Phase 0 и открыть только code-preparation gate Phase 1A
СТАТУС: phase0_behavior_accepted_bounded
