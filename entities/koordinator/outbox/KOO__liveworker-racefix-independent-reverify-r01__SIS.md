# KOO → SIS: live-worker race-fix independent re-verification r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Corrected candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/`

commit:
`6880f16459c5424992fcbe2102f0889142fe533a`

tree:
`81a23900c6437c8a76ee3f45cb451f319f3fdec2`

KOD report:
`d3b699d766bcf422109a1e7e6cb89e2cf6e17ff5`

source verdict:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`

Original SIS blocker:
`d15b88501d227f778b657af638e86bf028f1948b`
`BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`

## Independently re-verify

Verify the exact corrected immutable candidate and specifically the old failure mode:

- no raw sqlite3.OperationalError/database locked escapes under concurrent construction/claim;
- exactly one claimant succeeds;
- competitors fail closed as BLOCKED_DUPLICATE_CALL or documented bounded BLOCKED_LEDGER_BUSY;
- initialization/claim bounded retry behavior is deterministic;
- BEGIN IMMEDIATE + PRIMARY KEY one-shot semantics remain;
- reservation commits before credential resolution/transport;
- restart/replay prevention remains;
- no provider retry/fallback introduced;
- hard timeout, response bound, redirect fail-closed remain;
- provider/model/request-plan binding unchanged;
- secret-reference-only boundary remains;
- ResourceResult stays project_acceptance=NOT_GRANTED;
- caller writer unchanged;
- no project-state application;
- no real provider call;
- no real credential read/create;
- no account/billing mutation;
- no production deployment.

Reproduce concurrency stress independently, including repeated constructor+claim races and forced SQLite contention.

Do not modify candidate bytes.

Expected:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01`
or exact blocker/fail.

Return terminal result to KOO through Exchange Gate and stop.
