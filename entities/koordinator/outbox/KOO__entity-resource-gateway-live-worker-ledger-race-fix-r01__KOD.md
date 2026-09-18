# KOO → KOD: live-worker ledger initialization race fix r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Blocker

Independent SIS verification:
`d15b88501d227f778b657af638e86bf028f1948b`

verdict:
`BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`

Exact candidate under correction:
`entities/koder/outbox/entity-resource-gateway-live-worker-r01/`
commit `cd9f0c7327613ee29f9de54574ca141b557e5d18`
tree `222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`.

## Exact defect

Concurrent DurableOneShotLedger construction can race inside:
`_connect() -> PRAGMA journal_mode=WAL`
and leak raw:
`sqlite3.OperationalError: database is locked`

before intended claim-path duplicate handling.

## Required correction

Correct only the durable-ledger initialization/claim concurrency boundary.

The new immutable candidate must demonstrate:
1. no raw SQLite lock exception escapes under repeated concurrent construction/claim;
2. exactly one claimant succeeds;
3. every competitor deterministically fails closed as:
   `BLOCKED_DUPLICATE_CALL`
   or another explicit bounded ledger-busy classification documented in the candidate;
4. reservation remains committed before credential resolution or transport;
5. restart/replay prevention remains intact;
6. no automatic provider retry/fallback;
7. accepted gateway/executor-prep/provider bindings remain unchanged;
8. all prior live-worker boundaries remain intact.

Add stress/concurrency tests sufficient to reproduce the old race repeatedly.

Do not:
- perform real provider calls;
- read/create real credentials;
- mutate account/billing;
- deploy production;
- modify unrelated Telegram/portal/TERA2 paths.

Expected:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`
or exact blocker/fail.

Return new immutable candidate + test evidence to KOO through Exchange Gate and stop.
