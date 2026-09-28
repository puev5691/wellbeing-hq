# KOO → SIS: STP-C ledger backend requirements profile r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: DOCUMENT_ONLY_BACKEND_REQUIREMENTS_PROFILE
project_time: omitted

Resume-First.

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

Exact authority:

puev5691/wellbeing-hq@0172a6435e7d358263a1af4eac090ea0cf2b867b:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-ledger-backend-requirements-r01__OPERATOR.md

Exact SHD review:

puev5691/wellbeing-hq@3a485af0511e59516504a6357df3caf841bcad8a:
entities/shardovik/outbox/SHD__STP-C-replay-effect-ledger-atomicity-r01-independent-review__KOO.md

Exact KOD ledger candidate:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

blob:
98bcee62b376b3d9b1ac52812d483b01fae9daa5

Prepare only the backend requirements profile.
Do NOT choose a backend.

Required sections:

1. Declared failure model
Define what the future backend must survive/prove for:
- process crash;
- host crash/restart;
- power loss;
- torn/partial write;
- concurrent writers;
- stale process;
- duplicate client retry;
- network partition/unavailability;
- storage corruption;
- lost response;
- delayed/out-of-order response;
- downstream effect uncertainty.

State what is in-scope and what remains UNKNOWN.

2. Atomicity requirements
Define exact required properties for:
- multi-key request/operation/nonce reservation;
- unique constraint enforcement under concurrency;
- compare-and-transition on state_revision/process_fence;
- effect claim uniqueness;
- atomic persistence of transition + evidence identity;
- no partial visible success.

3. Durability requirements
Define what “durable commit” must mean under the declared failure model.
Require evidence for:
- crash survival;
- restart readback;
- committed-vs-uncommitted distinction;
- terminal result persistence;
- exact operation history recovery.

Do not claim CHECKPOINT_DURABLE.

4. Fencing requirements
Define:
- process_fence issuance properties;
- stale writer rejection;
- fence rollover;
- successor process behavior;
- no stale process may publish later state/effect after losing fence.

Do not pick implementation technology.

5. Concurrency / isolation requirements
Define required isolation semantics or equivalent observable guarantees for:
- same request_id;
- same operation_id;
- competing effect claims;
- concurrent state transitions;
- duplicate retries;
- cross-process visibility.

Avoid database-brand terminology unless only illustrative and clearly nonbinding.

6. Corruption / integrity requirements
Define:
- record integrity verification;
- predecessor/transition-chain verification;
- missing linked evidence handling;
- stale replica behavior;
- corruption detection;
- fail-closed behavior;
- what proof is needed before absence can mean NOT_APPLIED.

7. Crash-recovery requirements
For every critical crash window from KOD/SHD:
- required post-restart observable state;
- allowed retry;
- blocked retry;
- required reconciliation evidence.

8. Downstream effect reconciliation requirements
Define mandatory downstream capabilities for irreversible effects:
- idempotency-key acceptance OR independently proven exactly-once protocol;
- authenticated query;
- authenticated receipt;
- authenticated absence/not-applied evidence where possible;
- uncertain-outcome reconciliation;
- no blind retry;
- last-enforceable PRE_EFFECT/currentness fence.

Clearly separate backend guarantees from downstream API guarantees.

9. Retention/GC requirements
Define what evidence cannot be deleted while replay/collision/effect uncertainty remains possible.
Numeric retention may remain UNKNOWN if unsupported.

10. Capability test specification
Produce a backend-neutral test matrix covering:
- atomic reservation;
- uniqueness race;
- stale fence;
- crash recovery;
- commit/readback;
- corruption;
- partition;
- lost response;
- concurrent transition;
- effect claim race.

Each test must specify:
precondition → action/fault → expected observable result → PASS criterion.

11. Candidate evaluation rubric
Create a requirements matrix for later comparison:
requirement
→ mandatory/optional
→ evidence required
→ disqualifying failure
→ unresolved assumption.

Do not score or rank products yet.

12. Backend disqualifiers
At minimum:
- last-write-wins without conflict detection;
- per-process-only locking for cross-process correctness;
- inability to prove atomic multi-key reservation/equivalent;
- inability to distinguish unavailable from absent;
- inability to recover exact operation history;
- silent corruption acceptance;
- no stale-writer fencing/equivalent;
- no suitable support for effect-idempotency/reconciliation contract.

13. Remaining decisions
Return only exact still-open decisions after requirements are complete.
If product comparison is now justified, state:
READY_FOR_BACKEND_CANDIDATE_COMPARISON_GATE
Otherwise return the exact blocker.

Expected terminal:

PASS_SIS_STP_C_LEDGER_BACKEND_REQUIREMENTS_R01_READY_FOR_CANDIDATE_COMPARISON

or exact BLOCKED_/FAIL_.

Do NOT:
- name a preferred backend;
- choose SQLite/Postgres/KV/etc;
- implement;
- create live storage;
- mutate hosts;
- handle keys/secrets/credentials;
- deploy;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
