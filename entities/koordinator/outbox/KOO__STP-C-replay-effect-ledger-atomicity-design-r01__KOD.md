# KOO → KOD: STP-C replay/effect ledger atomicity design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DOCUMENT_ONLY_PROTOCOL_STORAGE_CONTRACT_DESIGN
project_time: omitted

Resume-First.

Current authoritative KOD writer:

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

Exact authority:

puev5691/wellbeing-hq@c0e761ed684fa1d05f93b29542b342a5d31b7e6f:
entities/koordinator/outbox/KOO__authorize-KOD-STP-C-replay-effect-ledger-atomicity-design-r01__OPERATOR.md

Exact SHD review:

puev5691/wellbeing-hq@a28686b60c6cac48f1a4145162a1eb3977089108:
entities/shardovik/outbox/SHD__STP-C-anti-replay-effect-binding-r01-independent-review__KOO.md

Exact reviewed candidate:

puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:
entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md

blob:
3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8

Design only the backend-agnostic durable replay/effect ledger contract.

Required coverage:

1. Atomic reservation
- (scope_namespace, request_id) + exact request_digest;
- (scope_namespace, operation_id) + exact intended effect/idempotency key;
- define what must be persisted atomically before signing/effect progression.

2. State transitions
At minimum:
NEW
RESERVED
ADMITTED
SIGNED
VERIFIED
QUORUM_VALID / QUORUM_BLOCKED
PRE_EFFECT_VALID
AUTHORIZED
CLAIMED
COMMITTED
OUTCOME_UNKNOWN
REJECTED
CONFLICT
STALE
PENDING_RECONCILIATION

Define allowed source→destination transitions and forbidden reverse/convenience transitions.

3. Idempotency
- duplicate exact request;
- duplicate exact operation;
- lost response after commit;
- retry while in-progress;
- same ID with changed digest/effect;
- effect replay after terminal result.

4. Concurrency / linearization
- two concurrent requests for same request_id;
- two concurrent operations for same operation_id;
- concurrent state advance;
- competing effect claims;
- stale writer/process observing old ledger state.

Define one linearization point for each critical class without selecting a backend.

5. Crash consistency
Analyze crashes:
- before reservation commit;
- after reservation but before signing;
- after signing before quorum persistence;
- after PRE_EFFECT before CLAIMED;
- after CLAIMED before external call;
- after external call before COMMITTED receipt persistence;
- after COMMITTED before client response.

For each state define recovery outcome and whether retry is allowed.

6. External effect boundary
Distinguish:
- ledger authorization;
- effect claim;
- external effect invocation;
- externally confirmed effect;
- unknown effect outcome.

Do not pretend a database transaction can atomically commit with an arbitrary external system unless a real protocol proves it.

7. Durable evidence minimum
Define exact minimum persistent evidence for:
- request reservation;
- digest binding;
- nonce/operation identity;
- current state;
- prior terminal result;
- effect auth identity;
- effect payload/target;
- external receipt/query evidence;
- reconciliation status.

8. Backend-neutral storage requirements
State required properties only:
- atomic compare-and-set / serializable equivalent;
- durable commit;
- crash recovery;
- conflict detection;
- recoverable operation ledger;
- corruption detection/readback where applicable.

Do NOT pick SQLite/Postgres/KV/etc yet.

9. Failure semantics
Define exact terminal/blocking outcomes:
REQUEST_ID_COLLISION
OPERATION_ID_COLLISION
NONCE_REPLAY
IN_PROGRESS
IDEMPOTENT_REPLAY
EFFECT_OUTCOME_UNKNOWN
BLOCKED_EFFECT_EXECUTION
LEDGER_UNAVAILABLE
LEDGER_CONFLICT
LEDGER_CORRUPT
and any strictly necessary additions.

10. Required future tests
Produce a negative/crash/concurrency test matrix that a later concrete backend implementation must pass.

11. Boundary with currentness/effect authority
Preserve:
- valid ledger state != task authority;
- valid signature/quorum != effect authority;
- CURRENT/PRE_EFFECT rules from SIS r0.2 and KOD r0.1 remain external admission conditions;
- ledger cannot mint authority.

Required output:
one standalone candidate contract, no code.

Expected terminal:

PASS_KOD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

or exact FAIL_/BLOCKED_.

Do NOT:
- select backend/product;
- implement code;
- generate keys;
- handle secrets;
- mutate hosts;
- deploy;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
