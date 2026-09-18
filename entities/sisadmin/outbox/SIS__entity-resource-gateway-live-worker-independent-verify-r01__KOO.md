# SIS → KOO: Entity Resource Gateway live-worker independent verify r0.1

verdict: `BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`
production: `no`
real_provider_calls: `0`
real_credential_reads_or_creates: `0`
account_billing_mutation: `0`
project_time: omitted; trusted project-time source not used

## Resume-First
fresh_HQ_HEAD: `b5fd441efd8f5763039b206da9ff5f85bf9a1637`
prewrite_reconciliation_HEAD: `b5fd441efd8f5763039b206da9ff5f85bf9a1637`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-independent-verify-r01__SIS.md`
commit `d09d942f43f7cab08feab1de60849819007bb4e6`.

Inbox placement commit:
`a6ab0d5bcd8927ab19d44ea14cb4d0dd7f646376`.

KOD report:
commit `b56d5159bcf7951efcb21de6dd684d4f74907844`
source verdict `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY`.

## Exact immutable candidate
Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-r01/`
commit `cd9f0c7327613ee29f9de54574ca141b557e5d18`
tree `222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`.

Exact composition:
- MANIFEST.json blob `3e60b0b0f90a2d13ceec82c45f7a4d08ff9d4db1`;
- README.md blob `5ea72ad9ed8e79b4aea8b84d98e415ec5bb19875`;
- live_worker.py blob `2e9ddfac78e8a38a413c9e6ee9a938208de2eb89`;
- test-result.json blob `4d5b43f501ae5872de3b016a6706dcca36649150`;
- test_live_worker.py blob `97f37dd62fee5ef4f3ff5360902e086e72cd9add`.

Independent SHA-256:
- MANIFEST.json `7e40a9db4ba0a429af8f67098a595fad14e0997de0e549fbfa7f90f847356296`;
- README.md `e7802f79f5a5882a3cc9069447206397f2dbdb28fb1a6f0a4e7a4b9456866652`;
- live_worker.py `4dcf53cacd0ba20c734fff218fd7b555a86af5244f8359e2c3eda6a0c76fd093`;
- test-result.json `f00d811b34c0381f049bfa02f2e2de1a8b2391164ccab9d6cb920dad9afa786c`;
- test_live_worker.py `dc5fb1e12d5b19534b5e967db95559e82de589f719e9a2dfedbc2552a92122ba`.

The implementation and test hashes remained unchanged across the independent runs.

## Independent execution result
The exact package was copied from the immutable commit into a temporary test-only directory and executed with:
`python3 -I -B test_live_worker.py`.

### Independent run 1
27 tests started. One required concurrency case failed:

`test_atomic_competing_claim`

Observed exception in one competing thread:

`sqlite3.OperationalError: database is locked`

The exception occurred while constructing `DurableOneShotLedger`, inside:
`_connect() -> PRAGMA journal_mode=WAL`.

The test therefore observed only:
`['ok']`

instead of the required deterministic result:
`['BLOCKED_DUPLICATE_CALL', 'ok']`.

Run result:
- tests: 27;
- failures: 1;
- real provider calls: 0;
- real credential reads: 0.

### Independent run 2
The exact same unchanged bytes were rerun once.
All 27 tests passed.

This second PASS does not erase the first observed race. The task explicitly requires concurrent duplicate/replay prevention; a concurrency invariant that sometimes emits an uncontrolled SQLite lock exception is not independently verified.

## Exact defect
`DurableOneShotLedger.__init__()` calls `_init()`.
`_init()` calls `_connect()`.
`_connect()` executes:
- `PRAGMA journal_mode=WAL`;
- `PRAGMA synchronous=FULL`;
- `PRAGMA busy_timeout=5000`.

Two competing constructors can therefore race on `PRAGMA journal_mode=WAL` before the intended `BEGIN IMMEDIATE` claim path is reached.

The current implementation only converts duplicate INSERT `sqlite3.IntegrityError` to `BLOCKED_DUPLICATE_CALL`. It does not provide a deterministic fail-closed mapping for an initialization-time SQLite lock.

Therefore the claimed invariant:
`restart-safe durable/atomic one-shot ledger + concurrent duplicate prevention`
is not established for the exact candidate.

## Other boundaries observed
The source still shows the intended properties:
- attempts table has `PRIMARY KEY`;
- claim uses `BEGIN IMMEDIATE`;
- `synchronous=FULL`;
- reservation/claim occurs before credential resolution and transport;
- hard timeout uses POSIX setitimer and fails closed outside supported main-thread environment;
- response byte limit is bounded;
- redirect handler is fail-closed;
- OpenAI endpoint is exactly `https://api.openai.com/v1/responses`;
- Anthropic endpoint is exactly `https://api.anthropic.com/v1/messages`;
- CredentialResolver receives a typed secret reference;
- automatic retries are zero;
- ResourceResult boundary retains `project_acceptance=NOT_GRANTED`, caller writer unchanged, no project-state application and no external dispatch authority.

These observations do not override the concurrency blocker.

## Required correction
KOD must correct only the durable-ledger initialization/claim concurrency boundary and provide a new immutable candidate.

The corrected candidate must independently demonstrate, on repeated concurrent construction/claim attempts:
1. no raw `sqlite3.OperationalError: database is locked` escapes;
2. exactly one claimant succeeds;
3. every competing duplicate is deterministically classified fail-closed as `BLOCKED_DUPLICATE_CALL` or another explicitly approved bounded ledger-busy classification;
4. reservation remains committed before credential resolution or transport;
5. restart/replay prevention remains intact;
6. no automatic provider retry/fallback is introduced.

Possible implementation strategy is not prescribed by SIS: initialization may be serialized/pre-created or lock handling may be bounded and explicit. KOD must choose and test the exact mechanism.

## Boundary
No real provider call, real credential read/create, account/billing mutation, production deployment or candidate-byte modification occurred.

The exact candidate is not accepted for the live-worker boundary until the concurrency defect is corrected and independently reverified.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: independently verify exact Entity Resource Gateway live-worker candidate
СТАТУС: `BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`
