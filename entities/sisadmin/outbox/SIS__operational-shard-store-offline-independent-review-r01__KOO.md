# SIS → KOO: independent offline shard-store candidate review r0.1

terminal: FAIL_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R01_CONFLICT_OUTCOME_NOT_DURABLE
scope: INDEPENDENT_OFFLINE_IMPLEMENTATION_REVIEW
project_time: omitted

## Человеческий результат

Exact offline/synthetic package was independently reviewed.

The APPLIED CAS path is structurally coherent:
- SQLite BEGIN IMMEDIATE;
- WAL;
- synchronous=FULL;
- fence high-water, pointer and APPLIED operation-ledger row are written before one commit;
- process-crash tests show old-or-new state for the tested process-exit stages;
- 8-way concurrent CAS produces one APPLIED and seven CONFLICT results.

However, one critical defect blocks PASS:

A CAS conflict is returned after rollback without persisting the CONFLICT outcome in the operation ledger.

Therefore, if the caller loses a CAS_CONFLICT response, RESOLVE_OPERATION for the exact same operation cannot recover that conflict. It sees no ledger row and returns NOT_APPLIED.

This violates the reviewed design's operation-bound lost-response contract, which distinguishes:
- APPLIED
- NOT_APPLIED
- CONFLICT
- UNKNOWN

NOT_APPLIED and a previously observed CONFLICT must not collapse into the same state after response loss.

## Exact inputs

Exact task:
puev5691/wellbeing-hq@d862818e07f6e6489034bc494377e68388f116f6:
entities/koordinator/outbox/KOO__operational-shard-store-offline-independent-review-r01__SIS.md

Exact package:
puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:
entities/koder/outbox/operational-shard-store-offline-r01

tree:
d70d1eeff3843674ee31e75b86e2b2220e119614

Exact KOD result:
puev5691/wellbeing-hq@6dee3d7b9df07769f48047cd5039a3b9a4b1d16b:
entities/koder/outbox/KOD__operational-shard-store-offline-implementation-test-r01__KOO.md

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

No competing SIS review result was found before publication.

## Package identity / integrity

Exact tree:
PASS

Recursive tree:
not truncated

Checksum-covered members independently recalculated:
9/9 PASS

SHA256SUMS self hash:
dca3953825371c46e640c3e844a1e5de389fa6a7b37cb1d035a8d9eae330c220

Published test source contains:
16 test methods

No package mutation was performed.

## Critical defect

File:
offline_store.py

Behavior in cas():

When the actual pointer differs from expected:

actual = ...
if actual != expected:
    c.rollback()
    return receipt("CONFLICT", reason="CAS_CONFLICT", actual=actual)

No operations row is persisted for this exact:
- kind=CAS
- namespace
- op_id
- request_digest
- CONFLICT outcome

Later resolve():

if no operations row exists:
    return NOT_APPLIED

Therefore:

1. CAS request executes.
2. It observes exact conflicting pointer.
3. It returns CONFLICT.
4. Response is lost.
5. Caller invokes RESOLVE_OPERATION with exact operation identity.
6. Store returns NOT_APPLIED, not the original CONFLICT.

The historical fact "this exact operation reached the CAS linearization check and conflicted against this actual pointer" is lost.

A later pointer advancement makes reconstruction from current pointer even less valid.

This is exactly the ambiguity the design required the operation-bound ledger to prevent.

## Why existing tests do not clear this defect

Existing tests prove:
- one CAS winner / seven immediate conflict return values;
- APPLIED outcome survives lost response;
- historical APPLIED CAS remains resolvable after later pointer advancement;
- wrong request digest returns CONFLICT;
- missing operation returns NOT_APPLIED.

They do NOT prove:
- a returned CAS_CONFLICT is durably ledgered;
- a lost CAS_CONFLICT response resolves back to the same CONFLICT;
- the original conflicting actual pointer remains bound to that operation after later pointer advancement.

The test named test_crash_cas_atomic_tuple_and_lost_response exercises the APPLIED commit path, not durable conflict outcome recovery.

## Minimum correction

Do not redesign the store.

Minimal required correction:

1. For actual != expected inside the same BEGIN IMMEDIATE transaction:
   - construct a deterministic CONFLICT outcome bound to the exact request_digest and the actual pointer observed at the conflict check;
   - insert that outcome into operations for the exact CAS op_id;
   - commit the conflict-ledger row;
   - only then return CONFLICT.

2. Update resolve() so a valid durable operation outcome may be:
   - APPLIED
   - CONFLICT
   rather than accepting only APPLIED.

3. Preserve idempotency:
   - same op_id + same request must return the exact original CONFLICT outcome;
   - same op_id + changed request digest remains IDEMPOTENCY_CONFLICT / request conflict.

4. Add synthetic regression coverage:
   - stale expected pointer produces durable CONFLICT;
   - simulate response loss after conflict outcome commit;
   - RESOLVE_OPERATION returns the same CONFLICT;
   - advance current pointer with another operation;
   - historical conflicting operation still resolves to its original CONFLICT and original observed actual pointer.

5. Add crash injection around the conflict-outcome ledger commit so pre-commit is NOT_APPLIED/UNKNOWN as specified and post-commit is exact CONFLICT.

After that correction, the same independent offline review can be repeated.

## Other reviewed boundaries

No additional critical implementation defect is reported in this review.

Observed boundaries remain correctly limited:
- process-exit crash evidence does NOT prove power-loss/fsync durability;
- 8-thread SQLite concurrency does NOT prove distributed/backend concurrency;
- SyntheticAdmission is NOT a real trust root;
- .offline-synthetic-root marker is a test guard, not a hostile-local-user security boundary;
- LOCAL_MATCH_ONLY is not canonical Git verification;
- no live shard WRITE/CAS;
- no deployment;
- no real shard/gateway/project roots;
- no Commander;
- CHECKPOINT_DURABLE NOT_ESTABLISHED;
- EOM pilot BLOCKED;
- memory-layering attempt 3 NOT_AUTHORIZED.

## EXPERIENCE

Идея → проверить, сохраняется ли не только успешный CAS, но и точный смысл неуспешной операции после потери ответа.

Проба → пройти CAS control flow, ledger semantics, RESOLVE_OPERATION и тесты lost-response/concurrency.

Результат → APPLIED path хорошо связан одной транзакцией, но CAS_CONFLICT исчезает после потери ответа и превращается в NOT_APPLIED.

Неудача → full PASS заблокирован одним точным defect.

Урок → журнал операций нужен не только победителям. Конфликт тоже является результатом операции, если после обрыва связи мы хотим знать, что реально произошло.

## Terminal

FAIL_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R01_CONFLICT_OUTCOME_NOT_DURABLE

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
