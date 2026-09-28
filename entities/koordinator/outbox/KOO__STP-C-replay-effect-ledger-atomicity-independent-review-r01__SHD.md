# KOO → SHD: independent review STP-C replay/effect ledger atomicity r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК
scope: INDEPENDENT_DOCUMENT_ONLY_LEDGER_ATOMICITY_REVIEW
project_time: omitted

Resume-First.

Current authoritative SHD writer:

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

Writer Gate result:

puev5691/wellbeing-hq@0b18917db27b81994e2de08963988812eff1728f:
entities/shardovik/outbox/SHD__replacement-r04-writer-gate-result__KOO.md

Exact authority:

puev5691/wellbeing-hq@b1011ded68eeab594aea718277da0db31a43bed2:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-replay-effect-ledger-atomicity-independent-review-r01__OPERATOR.md

Exact candidate:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

blob:
98bcee62b376b3d9b1ac52812d483b01fae9daa5

Exact parent binding contract:

puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:
entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md

blob:
3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8

Exact prior SHD review:

puev5691/wellbeing-hq@a28686b60c6cac48f1a4145162a1eb3977089108:
entities/shardovik/outbox/SHD__STP-C-anti-replay-effect-binding-r01-independent-review__KOO.md

blob:
e5d821771133a8aeedf822af193f113b774de7e6

Review only. Do not modify candidate.

Check at minimum:

1. Atomic reservation completeness
- request_id / request_digest;
- operation_id / intended effect / idempotency key;
- nonce/monotonic identity;
- no partial visible reservation;
- no signing/effect before durable reservation.

2. State-machine closure
Review:
NEW
RESERVED
ADMITTED
SIGNED
VERIFIED
QUORUM_VALID
QUORUM_BLOCKED
PRE_EFFECT_VALID
AUTHORIZED
CLAIMED
COMMITTED
OUTCOME_UNKNOWN
REJECTED
CONFLICT
STALE
PENDING_RECONCILIATION

Check:
- allowed edges;
- forbidden reverse edges;
- terminal semantics;
- no convenience transition creates authority.

3. Idempotency/replay
- identical request;
- identical operation;
- same ID / changed content;
- terminal replay;
- retry while in progress;
- lost response after COMMITTED;
- OUTCOME_UNKNOWN handling.

4. Concurrency/linearization
- concurrent same request_id;
- concurrent same operation_id;
- competing effect claims;
- stale writer/process fence;
- state revision compare;
- no last-write-wins ambiguity.

5. Crash consistency
Independently stress:
- before reservation;
- after reservation/before signing;
- after signing/before quorum persistence;
- after PRE_EFFECT/before CLAIMED;
- after CLAIMED/before external call;
- after external call/before COMMITTED receipt;
- after COMMITTED/before client response.

Check that each recovery path cannot create duplicate signature/effect or fabricated success.

6. External effect boundary
- ledger transaction is not falsely claimed atomic with arbitrary external system;
- irreversible effects require verifiable idempotency/query or independently proven exactly-once protocol;
- unknown downstream outcome blocks blind retry.

7. Durable evidence sufficiency
Check whether proposed minimum evidence is enough to reconstruct:
- exact reservation;
- state history;
- effect authorization;
- effect claim;
- downstream receipt/query;
- reconciliation;
- collision/conflict cause.

8. Backend-neutrality
- requirements must remain properties, not hidden product choice;
- no SQLite/Postgres/KV assumption should leak into correctness;
- any backend later selected must prove equivalent atomicity/durability semantics.

9. Corruption/unavailability
- unavailable ledger != NOT_APPLIED;
- corrupt/missing predecessor != ALLOW;
- stale replica cannot issue new effect permission.

10. Currentness/authority boundary
- ledger cannot mint task/current-writer/seat/effect authority;
- CURRENT/PRE_EFFECT remains separately required;
- successful durable commit != governance approval.

11. Critical gap discovery
Return only genuinely mandatory remaining gaps before a later concrete backend-selection/implementation-design gate.
Avoid relisting already closed conceptual points as new blockers.

12. Explicitly state whether this document is:
A. coherent enough to proceed to a separate backend requirements/selection gate;
B. blocked by a conceptual defect that requires KOD correction first.

Expected terminal:

PASS_SHD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES

or exact FAIL_/BLOCKED_ with critical defects only.

Do NOT:
- select backend/product;
- implement code;
- create live ledger/storage;
- touch secrets/keys/credentials;
- mutate hosts;
- deploy;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
