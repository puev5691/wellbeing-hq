# KOO → KOD: operational shard store offline implementation/test r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: OFFLINE_IMPLEMENTATION_TEST_ONLY
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@ab40541b968937720452e4d8114bf2213ac90902:
entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-offline-implementation-test-r01__OPERATOR.md

Exact design:
puev5691/wellbeing-hq@dc0e458fd8950fc5cc7fbb08034e7695630f7a77:
entities/koder/outbox/KOD__operational-shard-store-cas-fence-trust-design-r01__KOO.md
blob d57cb65e9a18100939bbfcab1c6cdf8b25b992db

SIS design review:
puev5691/wellbeing-hq@1ba484e9cc819f3514afdefe7476b6403b17a494:
entities/sisadmin/outbox/SIS__operational-shard-store-design-independent-review-r01__KOO.md

SHD design review:
puev5691/wellbeing-hq@4515391b10b0f59af2052fb8171f5a86adea43ce:
entities/shardovik/outbox/SHD__operational-shard-store-design-independent-review-r01__KOO.md

Implement only an offline/synthetic candidate.

## Required implementation scope

1. OperationalRecordV1 canonical byte serialization.
2. Immutable object identity/digest validation.
3. Namespace binding:
   entity_id / task_id / task_version / stream_id.
4. PUT_IMMUTABLE idempotency behavior.
5. COMMIT_CURRENT_CAS state machine.
6. Exact expected-prior-pointer comparison.
7. generation/parent consistency.
8. operation-specific ledger.
9. RESOLVE_OPERATION:
   APPLIED / NOT_APPLIED / CONFLICT / UNKNOWN.
10. writer fence high-water state machine.
11. stale/frozen/superseded writer rejection.
12. object without pointer / pointer without object behavior.
13. Git/shard mismatch representation only as synthetic input/state.
14. deterministic synthetic vectors.
15. concurrency tests.
16. crash-injection tests around:
   - object write;
   - operation ledger;
   - fence update;
   - pointer commit;
   - lost response.
17. negative path/namespace/identity tests.

## Critical SIS boundary

For any CAS resolved as APPLIED, prove one recoverable linearization protocol covering:
- exact prior pointer comparison;
- new pointer;
- fence high-water transition;
- operation request digest;
- operation outcome/receipt identity.

Do not claim this property unless tests actually demonstrate it.

## Environment boundary

Use only local/synthetic test roots.

Do NOT:
- use existing shard/gateway roots;
- touch production/project runtime storage;
- deploy to host;
- enable live WRITE/CAS;
- invoke Commander;
- access credentials;
- appoint trust root/backend/operator;
- claim CHECKPOINT_DURABLE;
- execute EOM pilot;
- execute memory-layering attempt 3.

## Result package

Produce one immutable implementation/test package including:
- source;
- schema;
- deterministic vectors;
- test suite;
- crash/idempotency/concurrency evidence;
- README/boundary statement;
- exact manifest/checksums/readback;
- concise result to KOO.

Expected terminal:

PASS_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_IMPLEMENTATION_TEST_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_* / FAIL_*.

After immutable package + readback + result to KOO, STOP.
