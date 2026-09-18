# Entity Resource Gateway live-worker ledger race fix r0.1

This package is a minimal correction of the previously blocked live-worker candidate.

## Blocker addressed

Independent SIS verification at commit `d15b88501d227f778b657af638e86bf028f1948b` found a race during concurrent `DurableOneShotLedger` construction:

`_connect() -> PRAGMA journal_mode=WAL -> sqlite3.OperationalError: database is locked`.

The correction changes only the SQLite initialization/claim concurrency boundary. Accepted gateway, executor-preparation and provider bindings are unchanged.

## Correction

`DurableOneShotLedger` now:
- separates connection opening from WAL/schema initialization;
- maps SQLite busy/locked OperationalError to bounded `BLOCKED_LEDGER_BUSY`;
- maps other SQLite operational failures to `BLOCKED_LEDGER_ERROR`;
- retries only SQLite lock acquisition/initialization locally, never provider execution;
- keeps `BEGIN IMMEDIATE` + PRIMARY KEY claim semantics;
- commits the reservation before credential resolution or transport;
- preserves restart/replay prevention;
- preserves automatic_retries=0 and max_calls=1.

No provider fallback or retry path was added.

## Stress evidence

The full test suite contains 31 methods.

New stress tests include:
- 40 rounds × 12 concurrent constructor+claim threads against one key;
- 30 rounds × 16 concurrent constructors;
- explicit forced lock contention mapped to `BLOCKED_LEDGER_BUSY`;
- 50 restart/replay duplicate attempts against a committed key.

Observed final run:
- tests: 31;
- failures: 0;
- errors: 0;
- skipped: 0;
- real provider calls: 0;
- real credential reads: 0;
- production: false;
- UID: 1000.

No raw `sqlite3.OperationalError` escaped in the stress tests.

## Unchanged boundaries

The following remain exactly as in the previous candidate:
- exact OpenAI and Anthropic endpoint/model/request-plan binding;
- hard timeout;
- response-size bound;
- fail-closed redirect policy;
- secret-reference credential resolver interface;
- no secret in logs/results/files;
- one-call semantics;
- zero automatic provider retries;
- ResourceResult remains NOT_GRANTED;
- caller writer unchanged;
- no project-state application;
- no external dispatch authority.

## Immutable lineage

Blocked source candidate:
- package commit `cd9f0c7327613ee29f9de54574ca141b557e5d18`;
- tree `222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`.

Exact corrective task:
- `388d3b67d0d2e0de008ca1dd8cef872da46a4338:entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-ledger-race-fix-r01__KOD.md`.

Expected verdict:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`.

Independent reverification is required before live attachment or deployment.
