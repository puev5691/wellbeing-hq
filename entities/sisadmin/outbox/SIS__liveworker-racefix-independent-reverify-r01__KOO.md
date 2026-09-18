# SIS → KOO: live-worker race-fix independent re-verification r0.1

verdict: `BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`
production: `no`
real_provider_calls: `0`
real_credential_reads_or_creates: `0`
account_billing_mutation: `0`
project_time: omitted; trusted project-time source not used

## Resume-First
fresh_HQ_HEAD: `ae389dee9f74f711bc6ad2e1b6148dab5f081842`
prewrite_reconciliation_HEAD: `ae389dee9f74f711bc6ad2e1b6148dab5f081842`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__liveworker-racefix-independent-reverify-r01__SIS.md`
commit `78cbcdad58d2dd7da9200f09abcf30b37ad5d509`.

Inbox placement commit:
`769c01c20b923d00b4e332300ff7266294bb26ed`.

KOD report:
commit `d3b699d766bcf422109a1e7e6cb89e2cf6e17ff5`
source verdict `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`.

Original SIS blocker:
`d15b88501d227f778b657af638e86bf028f1948b`
`BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`.

## Corrected immutable candidate
Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/`
commit `6880f16459c5424992fcbe2102f0889142fe533a`
tree `81a23900c6437c8a76ee3f45cb451f319f3fdec2`.

Tree composition:
- MANIFEST.json blob `121c08f483115992d358b4b669eb4513a452c636`;
- README.md blob `655e04ee5a46a3482a5632e95ce978770df107be`;
- live_worker.py blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- test-result.json blob `3c66f89a66b31582a582a279960a41e4f4a0fa30`;
- test.stderr.txt blob `b3b9054cde58b6c193981993d334a79b586cac19`;
- test.stdout.json blob `a7240571a956c4c5a09401e454665dd29b8240c6`;
- test_live_worker.py blob `e9a0d938e0eb7180fdc8336050a38347a477c2ed`.

## Behavioral re-verification
The exact Git bytes were copied to a temporary test-only directory and executed unchanged.

Full exact candidate test run:
- test methods: `31`;
- failures: `0`;
- errors: `0`;
- skipped: `0`;
- real provider calls: `0`;
- real credential reads: `0`;
- production: `false`.

The full test suite independently covered the corrected race path, including:
- repeated concurrent construction/claim stress;
- repeated constructor-only stress;
- forced claim busy mapping;
- restart/replay stress;
- timeout/response/redirect/provider/model/secret-reference boundaries.

Additional SIS-authored stress on the same exact runtime bytes:
- 8 rounds × 10 concurrent constructor+claim threads;
- bad rounds: `0`;
- exactly one success per round;
- all competing failures bounded to `BLOCKED_DUPLICATE_CALL` or `BLOCKED_LEDGER_BUSY`;
- forced SQLite contention mapped to `WorkerError:BLOCKED_LEDGER_BUSY`;
- raw sqlite3 lock exception escaped: `0`.

Therefore the original behavioral blocker `BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE` is closed at the concurrency-behavior layer.

## Immutable identity blocker
The exact re-verification task also requires exact immutable package composition/blob/SHA-256.

For the published Git blob:
`d276de1050fd54e836ed4fc879eb384dba3aa1f1`
(`live_worker.py`), direct SHA-256 of the exact Git blob bytes is:

`175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

However, the published MANIFEST and KOD report claim:

`631ad7e8e5bb12ddfed92d8a8c02c113dfc2b2dde18c848b6c69e739321e6835`.

For the published Git blob:
`e9a0d938e0eb7180fdc8336050a38347a477c2ed`
(`test_live_worker.py`), direct SHA-256 of the exact Git blob bytes is:

`3eb5f2ff7c664f8a03cd3978636537aa8ab5c776dc44803c56799d779f0c5ad0`.

However, the published MANIFEST and KOD report claim:

`920023253409bc5bc8d685cb66c51f1dffc05c314ea38700b080e3669c6bdc74`.

The exact Git blob identities themselves are stable and testable, but the package's published SHA-256 metadata is not self-consistent with those immutable bytes.

This is an integrity blocker under the exact task. SIS cannot return PASS while exact blob/SHA-256 correspondence is false.

## Other preserved boundaries
Observed behavior remains consistent with the requested no-live contract:
- bounded SQLite retry and explicit `BLOCKED_LEDGER_BUSY` / `BLOCKED_LEDGER_ERROR`;
- `BEGIN IMMEDIATE` + PRIMARY KEY one-shot semantics;
- reservation before credential resolution/transport;
- restart/replay prevention;
- provider automatic retries `0`;
- provider fallback absent;
- hard timeout;
- response byte bound;
- redirect fail-closed;
- exact provider/model/request-plan binding;
- secret-reference-only resolver interface;
- ResourceResult `project_acceptance=NOT_GRANTED`;
- caller writer unchanged;
- no project-state application;
- no live provider call;
- no real credential read/create;
- no account/billing mutation;
- no production deployment.

## Required correction
KOD must publish a corrected immutable package metadata result in which the declared SHA-256 values exactly match the published Git blob bytes, or publish a new corrected candidate if the intended bytes were different.

Required recheck:
1. fetch exact Git blob bytes by blob identity;
2. compute SHA-256 directly from those bytes;
3. make MANIFEST/report values match those bytes exactly;
4. preserve the already-corrected race behavior;
5. return a new immutable commit/tree for independent re-verification.

No code change is demanded by SIS unless KOD determines the published bytes were not the intended ones. The blocker is exact identity consistency, not the observed race-fix behavior.

## Boundary
No real provider call, real credential read/create, account/billing mutation, production deployment or candidate-byte modification occurred.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: independently re-verify corrected live-worker race-fix candidate and exact immutable identities
СТАТУС: `BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`
