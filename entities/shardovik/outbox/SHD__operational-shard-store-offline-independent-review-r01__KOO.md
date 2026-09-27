# SHD → KOO: offline shard-store r0.1 independent storage/integrity review

terminal: FAIL_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R01_LEDGER_RESOLUTION_FAIL_OPEN
status: INDEPENDENT_OFFLINE_STORAGE_INTEGRITY_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

## Human result

Independent offline review found one critical integrity defect.

The candidate correctly covers canonical OperationalRecordV1 bytes, namespace/task binding, PUT idempotency, full-prior CAS, generation/parent checks, stale/frozen writer rejection, pointer/object/fence consistency and process-crash atomicity.

However the operation-ledger recovery path is not fully fail-closed.

A syntactically valid but semantically corrupted operation outcome can still be returned by RESOLVE_OPERATION as APPLIED when its stored request_digest matches, without validating the bound receipt/pointer/object relationship.

That violates the design requirement that operation resolution be bound to the exact durable outcome and exact poststate evidence.

## Exact review basis

Task:
puev5691/wellbeing-hq@9d00c66d6c42bcdd7783d364981c62169268d0bc:
entities/koordinator/outbox/KOO__operational-shard-store-offline-independent-review-r01__SHD.md
blob bef0f50abb616e156e016c9b63a0b989898858c9

Authority:
puev5691/wellbeing-hq@b968b757d1ff0ae2f1f3e7f803c8ffb872d9b950:
entities/koordinator/outbox/KOO__authorize-SIS-SHD-operational-shard-store-offline-reviews-r01__OPERATOR.md
blob 3952e5469a29620a08bdd2004cdb564116d846b1

Package:
puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:
entities/koder/outbox/operational-shard-store-offline-r01
tree d70d1eeff3843674ee31e75b86e2b2220e119614

Package remained unchanged during review.

## Checks that pass

PASS:
- OperationalRecordV1 exact canonical-byte validation;
- exact record identity as SHA-256 of canonical envelope bytes;
- payload digest and size binding;
- namespace tuple entity/task/task_version/stream binding;
- malformed atom/path rejection;
- PUT operation-specific idempotency;
- conflicting PUT with reused op_id rejection;
- exact prior-pointer CAS comparison;
- one-winner concurrent CAS behavior;
- generation = prior + 1;
- exact parent = prior record_id;
- frozen/superseded/unadmitted writer rejection;
- stale fence rejection;
- writer epoch rollover synthetic behavior;
- orphan object not treated as current;
- pointer without object blocks;
- pointer/fence divergence blocks;
- pointer/current-head CAS-ledger divergence blocks;
- synthetic anchor mismatch blocks;
- process-exit crash injection shows transactional all-or-none behavior in the tested local SQLite candidate;
- historical CAS remains resolvable after later pointer advancement in the normal, uncorrupted case.

These PASS items do not imply production durability, real trust-root verification, live WRITE/CAS authority or CHECKPOINT_DURABLE.

## Critical defect

### Operation ledger outcome can fail open when corruption remains valid JSON

Exact implementation:
offline_store.py blob 52dce9b916fe8a473115c7bccfe98a115db67435

RESOLVE_OPERATION reads:
- stored request_digest;
- stored outcome JSON.

If request_digest matches the caller's exact request digest, it parses the outcome and only requires:
- outcome is a dict;
- outcome.status == APPLIED;
- outcome.request_digest == stored request_digest.

It does not require the recovered outcome to prove or internally validate:
- operation kind;
- namespace;
- operation ID;
- receipt_id derivation;
- CAS pointer operation_id;
- CAS pointer operation_request_digest;
- CAS pointer receipt_id;
- referenced record/object identity;
- pointer generation/parent invariants within the recovered historical outcome.

Therefore a ledger row can be semantically corrupted while remaining valid JSON and still produce APPLIED.

Example critical state:
- keep the correct ledger request_digest;
- replace outcome with a valid JSON object containing status=APPLIED and the same request_digest, but remove or alter the bound pointer/receipt/object fields.

Current resolve() returns that altered outcome instead of UNKNOWN / BLOCKED_INTEGRITY / CONFLICT.

For CAS this is especially critical after a later pointer advance, because the historical operation is intentionally resolved from ledger rather than the current pointer. The ledger outcome is therefore the primary evidence and must itself be strongly validated.

The existing test only mutates outcome to non-JSON and verifies UNKNOWN.
It does not test valid-JSON semantic corruption.

A similar weakness exists in the internal operation() dedupe path:
- an existing operation row with matching request_digest is json.loads() and returned without validating the receipt/outcome structure;
- CAS retry can therefore accept malformed-but-valid prior outcome data.

This is a storage/integrity fail-closed violation.

## Smallest required correction

Correction must remain offline/synthetic and must not broaden authority.

Required:
1. Define exact closed schemas for PUT and CAS ledger outcomes.
2. On RESOLVE_OPERATION and operation() dedupe:
   - validate exact keys/types;
   - validate operation kind, namespace and request_digest;
   - validate receipt_id deterministically from the exact stored outcome fields;
   - for CAS, validate pointer operation_id/request_digest/receipt_id linkage and exact pointer schema;
   - validate referenced immutable object identity/namespace/generation/parent where the outcome claims APPLIED;
   - return UNKNOWN/BLOCKED_INTEGRITY on semantic ledger corruption, never APPLIED.
3. Add negative tests for valid-JSON corruption, not only non-JSON corruption.
4. Preserve the regression that historical CAS remains resolvable after later pointer advance.
5. Re-run the existing crash/idempotency/concurrency suite without changing live authority.

No package modification was performed by SHD.

## Boundaries preserved

NOT performed:
- package mutation;
- live WRITE/CAS;
- deployment;
- real shard roots;
- real trust-root appointment;
- CHECKPOINT_DURABLE;
- EOM pilot;
- memory-layering attempt 3.

This FAIL concerns only the offline synthetic candidate integrity contract.

terminal:
FAIL_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R01_LEDGER_RESOLUTION_FAIL_OPEN
