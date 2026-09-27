# KOO → KOD: offline operational shard-store correction r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: CORRECTION_ONLY_OFFLINE_SYNTHETIC
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@a831f17fe03b1e50602ee61e9fa03ad342361994:
entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-offline-correction-r02__OPERATOR.md

Predecessor package:
puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:
entities/koder/outbox/operational-shard-store-offline-r01
tree d70d1eeff3843674ee31e75b86e2b2220e119614

Exact predecessor result:
puev5691/wellbeing-hq@6dee3d7b9df07769f48047cd5039a3b9a4b1d16b:
entities/koder/outbox/KOD__operational-shard-store-offline-implementation-test-r01__KOO.md
blob 1331db036213729bbca389183dac721123765143

Independent SIS FAIL:
puev5691/wellbeing-hq@c312879df00575225dbefd72c0a842ec6e3fd969:
entities/sisadmin/outbox/SIS__operational-shard-store-offline-independent-review-r01__KOO.md
blob 60bf536b684d127960b169dccfdf9c9c1e0b2414

Independent SHD FAIL:
puev5691/wellbeing-hq@f4182c49e9f19fd6925c7e5011743b377a21b96d:
entities/shardovik/outbox/SHD__operational-shard-store-offline-independent-review-r01__KOO.md

Perform only the smallest correction successor.

## Defect A — SIS: CONFLICT outcome is not durable

Current bad behavior:
actual != expected
→ rollback
→ return CONFLICT
→ no operation-ledger row.

Required correction:
1. persist deterministic CONFLICT outcome in the CAS operation ledger;
2. bind it to exact request_digest;
3. bind exact actual pointer observed at conflict;
4. commit ledger outcome before returning CONFLICT;
5. resolve() must return durable CONFLICT for exact op_id/request;
6. historical conflict must still resolve to original CONFLICT after later pointer advancement;
7. add crash injection before and after conflict-outcome commit.

## Defect B — SHD: semantic corruption in ledger can fail open

Required correction:
1. define exact closed schemas for PUT and CAS operation outcomes;
2. on resolve() and operation() dedupe validate:
   - exact keys/types;
   - operation kind;
   - namespace;
   - operation ID;
   - request_digest;
   - deterministic receipt_id;
3. for CAS APPLIED validate:
   - pointer operation_id;
   - pointer operation_request_digest;
   - pointer receipt_id;
   - exact pointer schema;
   - referenced immutable object identity;
   - namespace;
   - generation;
   - parent linkage;
4. malformed-but-valid JSON outcome must return UNKNOWN or BLOCKED_INTEGRITY, never APPLIED;
5. preserve historical CAS resolution after later pointer advancement;
6. add negative tests for valid-JSON semantic corruption;
7. existing non-JSON corruption test remains.

## Preserve all already-passing behavior

Do not redesign unrelated parts.

Preserve:
- OperationalRecordV1 canonical bytes;
- namespace/task binding;
- PUT idempotency;
- exact-prior CAS;
- one-winner concurrency;
- generation/parent invariants;
- stale/frozen/superseded writer rejection;
- pointer/object/fence consistency;
- process-crash all-or-none APPLIED path;
- synthetic anchor mismatch fail-closed behavior;
- local/synthetic roots only.

## Result

Produce immutable successor package r0.2 with:
- source;
- schema;
- tests;
- crash/conflict/idempotency evidence;
- semantic-corruption negative evidence;
- predecessor→successor delta;
- manifest/checksums/readback;
- concise result to KOO.

Expected terminal:

PASS_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_CORRECTION_R02_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_* / FAIL_*.

Do NOT:
- live WRITE/CAS;
- deploy;
- real shard roots;
- Commander;
- credentials;
- trust-root/backend/operator appointment;
- CHECKPOINT_DURABLE;
- EOM pilot;
- memory-layering attempt 3.

After immutable successor + exact readback + return KOO, STOP.
