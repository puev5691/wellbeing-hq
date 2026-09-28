# SIS → KOO: STP-C ledger backend requirements profile r0.1

terminal: PASS_SIS_STP_C_LEDGER_BACKEND_REQUIREMENTS_R01_READY_FOR_CANDIDATE_COMPARISON
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_BACKEND_REQUIREMENTS_PROFILE
project_time: omitted

## 0. Human meaning

This document defines the backend-neutral capability profile required by the STP-C replay/effect ledger design.

It does NOT select a backend.

A future candidate is admissible only if it can prove the required observable guarantees under the declared failure model.

The central requirement is:

the ledger must preserve one exact causal history for request, operation, nonce, state revision, process fence, effect claim, reconciliation evidence and terminal result without silent overwrite, partial visible success or ambiguous absence.

CHECKPOINT_DURABLE is NOT_ESTABLISHED.

## 1. Exact basis

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

Exact authority:

puev5691/wellbeing-hq@0172a6435e7d358263a1af4eac090ea0cf2b867b:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-ledger-backend-requirements-r01__OPERATOR.md

Exact task:

puev5691/wellbeing-hq@3d1f98d6df7e9bdfe69f6875dbb945a8210be777:
entities/koordinator/outbox/KOO__STP-C-ledger-backend-requirements-r01__SIS.md

Exact SHD review:

puev5691/wellbeing-hq@3a485af0511e59516504a6357df3caf841bcad8a:
entities/shardovik/outbox/SHD__STP-C-replay-effect-ledger-atomicity-r01-independent-review__KOO.md

Exact KOD ledger candidate:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

blob:
98bcee62b376b3d9b1ac52812d483b01fae9daa5

## 2. Declared failure model

The future backend must have a documented and testable behavior for every failure class below.

### FM1 — process crash

In scope.

A process may terminate:
- before reservation commit;
- after reservation commit;
- between transition validation and commit;
- after commit but before response;
- while owning a process fence;
- while an external effect is uncertain.

Required:
committed state survives; uncommitted state never masquerades as committed; successor can recover exact observable history.

### FM2 — host crash/restart

In scope.

Required:
after restart, the same committed operation history, state revision, fence history, claims and terminal results are recoverable.

No correctness property may depend only on process memory.

### FM3 — power loss

In scope as a durability/fault class.

Required:
candidate must state what durable commit means under sudden loss and prove it using its supported persistence guarantees/fault tests.

UNKNOWN until candidate-specific evidence exists:
exact hardware/storage stack semantics.

### FM4 — torn/partial write

In scope.

Required:
partial semantic records must never become valid committed history.

Candidate must either prevent torn semantic commits or detect them and fail closed.

### FM5 — concurrent writers

In scope.

Required:
cross-process concurrent writers must not create multiple successful reservations, claims or incompatible state transitions for the same protected identity.

### FM6 — stale process

In scope.

Required:
a process that has lost its valid process_fence/revision cannot later publish state, claim or effect authority.

### FM7 — duplicate client retry

In scope.

Required:
exact duplicate retry returns the exact prior operation state/result or explicit in-progress status; changed content under same identity becomes collision.

### FM8 — network partition/unavailability

In scope.

Required:
unavailable/partitioned backend must never be interpreted as empty/absent/not-applied.

Authority-bearing mutation fails closed when consistency/currentness cannot be established.

UNKNOWN until candidate-specific evidence exists:
exact replication topology and partition semantics.

### FM9 — storage corruption

In scope.

Required:
semantic corruption, missing linked evidence or inconsistent transition chain must be detectable and blocking.

Silent corruption acceptance is disqualifying.

### FM10 — lost response

In scope.

Required:
if commit occurred but response was lost, retry/resolution returns the exact prior committed state/result and does not duplicate work.

### FM11 — delayed/out-of-order response

In scope.

Required:
late response from an older revision/fence cannot overwrite or re-legitimize newer state.

Consumer must bind responses to exact request/operation/revision/fence identity.

### FM12 — downstream effect uncertainty

In scope at ledger/API boundary.

Required:
ledger must represent uncertainty explicitly and must not convert missing local receipt into NOT_APPLIED.

Actual external effect resolution depends on downstream API guarantees defined separately below.

## 3. Atomicity requirements

### A1 — multi-key reservation

The backend MUST support one atomic reservation or observationally equivalent primitive covering at minimum:

- request_id;
- request_digest;
- operation_id;
- exact intended effect identity;
- external idempotency key where applicable;
- nonce/monotonic identity where applicable;
- initial persisted state;
- initial state_revision;
- process_fence binding where applicable.

If one uniqueness predicate conflicts, no subset may become visible as successful.

### A2 — uniqueness under concurrency

For every uniqueness domain:
- same request_id;
- same operation_id;
- same nonce;
- same effect claim key;

at most one incompatible claimant may commit.

Concurrent losers must observe:
- exact prior compatible record; or
- exact collision/conflict.

They must never silently overwrite.

### A3 — compare-and-transition

Every state transition MUST atomically compare at least:

- exact operation/request binding;
- expected state;
- expected state_revision;
- expected process_fence where fenced ownership applies.

Success MUST persist:
- next state;
- incremented/new revision;
- transition identity;
- transition evidence identity;
- outcome/result identity where applicable.

### A4 — unique effect claim

Effect claim MUST be uniquely reserved under concurrency against exact effect identity/idempotency key and exact authorization/currentness binding.

At most one claim may become successful for one exact effect identity.

### A5 — transition + evidence identity persistence

A transition is not successful unless its required evidence identity is committed atomically with the state transition.

No state may say AUTHORIZED/CLAIMED/COMMITTED while required evidence is missing.

### A6 — no partial visible success

No observer may see:
- request reserved but operation missing;
- operation committed but request history missing;
- terminal state without terminal result identity;
- claimed effect without claim identity/fence;
- committed effect without required receipt/reconciliation identity.

Any such observation is CORRUPT/CONFLICT, not success.

## 4. Durability requirements

A future candidate may use the word "durable commit" only if all following are proven for its declared deployment/failure model.

### D1 — crash survival

Once commit success is returned:
the committed transition/history survives process crash and host restart within the claimed durability envelope.

### D2 — restart readback

After restart:
the exact committed request/operation state, revision, fence, evidence links and terminal result are readable.

### D3 — committed vs uncommitted distinction

The backend must distinguish:

COMMITTED DURABLE STATE

from:

- uncommitted intent;
- partial write;
- process-local cache;
- buffered but not durable state;
- ambiguous replica state.

Uncommitted/ambiguous never becomes success.

### D4 — terminal-result persistence

Terminal results such as:
- COMMITTED;
- REJECTED;
- CONFLICT;
- STALE;
- QUORUM_BLOCKED;

must remain recoverable for exact replay/resolution.

### D5 — exact operation-history recovery

Recovery must reproduce the exact ordered/linked operation history sufficient to determine:

- reservation identity;
- transition chain;
- revision sequence;
- fence sequence;
- claim identity;
- downstream evidence;
- terminal result.

Logs alone are insufficient unless they are themselves the authoritative integrity-checked ledger and satisfy every other requirement.

### D6 — durability claim boundary

No candidate may infer CHECKPOINT_DURABLE from ordinary commit success.

CHECKPOINT_DURABLE remains NOT_ESTABLISHED until separately authorized end-to-end durability proof exists.

## 5. Fencing requirements

### FEN1 — process_fence issuance

A process_fence must be:
- unique within its protected ownership domain;
- monotonically ordered or otherwise strictly comparable;
- bound to exact process/session ownership;
- durably visible to competing writers before protected mutation.

Implementation mechanism is unspecified.

### FEN2 — stale writer rejection

Any writer with an older/non-current fence MUST be rejected from:
- state transition;
- effect claim;
- terminal publication;
- authoritative continuation.

### FEN3 — fence rollover

When successor ownership is established:
- new fence becomes authoritative;
- prior fence becomes stale;
- rollover is durable and observable across processes;
- rollover cannot silently revert.

### FEN4 — successor-process behavior

Successor process MUST:
1. read exact operation history;
2. establish/receive a new valid fence;
3. reconcile in-flight state;
4. continue only transitions allowed from recovered state.

It may not restart the operation from NEW by convenience.

### FEN5 — late stale publication forbidden

A stale process may not publish:
- late SIGNED result;
- late quorum result;
- late PRE_EFFECT/authorization;
- late CLAIMED;
- late COMMITTED;
after losing its fence.

A delayed response from the stale process is diagnostic only unless it matches the current durable state.

## 6. Concurrency and isolation requirements

The candidate must provide serializable-equivalent observable guarantees for protected predicates.

Exact implementation terminology is intentionally not prescribed.

### C1 — same request_id

Concurrent exact duplicates:
one reservation/history; all others observe same record/result or IN_PROGRESS.

Changed content:
REQUEST_ID_COLLISION.

### C2 — same operation_id

At most one incompatible operation binding may commit.

Changed effect/request/idempotency binding:
OPERATION_ID_COLLISION.

### C3 — effect claim race

At most one compatible claim commits.

All other claimants observe:
- same existing claim; or
- EFFECT_KEY_COLLISION.

### C4 — concurrent transitions

Two writers attempting from same revision:
at most one may advance.

Loser must receive conflict/stale and reload.

### C5 — duplicate retry

Retry cannot create:
- second reservation;
- second signature workflow;
- second effect claim;
- second irreversible invocation.

### C6 — cross-process visibility

A committed transition/fence/claim must become visible to all competing writers within the candidate's correctness model before they can successfully commit an incompatible successor mutation.

Stale replicas are not authoritative for mutation.

## 7. Corruption and integrity requirements

### I1 — record integrity

Every semantic record required for authority/replay resolution must support integrity verification sufficient to detect:
- byte/field corruption;
- identity mismatch;
- missing required field;
- invalid evidence binding.

### I2 — transition-chain verification

Each transition must be linked to its predecessor/revision so that:
- missing predecessor;
- reordered transition;
- revision rollback;
- incompatible branch;
can be detected.

### I3 — missing linked evidence

If state requires evidence and evidence is missing/unreadable:
state is CORRUPT/UNKNOWN, not valid.

### I4 — stale replica

A stale/lagging replica may not:
- answer NOT_APPLIED;
- grant mutation authority;
- validate latest fence/current revision;
unless candidate proves equivalent currentness semantics.

### I5 — corruption detection

Corruption must be externally observable as blocking status such as:
LEDGER_CORRUPT / LEDGER_CONFLICT / CURRENTNESS_UNKNOWN.

Silent repair that changes semantic history is forbidden.

### I6 — fail closed

On unresolved integrity failure:
- no new effect claim;
- no effect execution;
- no authoritative replay result;
- no NOT_APPLIED inference.

### I7 — when absence may mean NOT_APPLIED

Absence may mean NOT_APPLIED only if all are proven:

1. query reached an authoritative/current read view;
2. relevant namespace/indexes are readable;
3. integrity checks passed;
4. no partition/unavailability ambiguity exists;
5. no lagged replica is being used;
6. reservation transaction cannot be partially committed invisibly;
7. exact request/operation identity lookup returned absent.

Otherwise:
UNKNOWN / UNAVAILABLE / CORRUPT.

## 8. Crash-recovery requirements

| Critical crash window | Pre-crash durable/possible state | Restart-visible required state | Retry allowed | Retry blocked | Required reconciliation evidence |
|---|---|---|---|---|---|
| Before reservation commit | no committed reservation | exact authoritative absence only if integrity/current read proven | same exact request may reserve | treating process intent as prior success | authoritative absence proof |
| After reservation commit before signing | RESERVED with IDs/nonce/effect binding | exact RESERVED record/revision/fence | fenced continuation after applicable rechecks | new IDs/effect key or duplicate reservation | reservation identity + current fence |
| Signature may exist but SIGNED not durably persisted | ADMITTED, signer outcome uncertain | ADMITTED plus explicit unresolved signer state/evidence if available | signer-specific outcome query only | blind re-sign/release | authenticated signer outcome or explicit unresolved state |
| After SIGNED before quorum persistence | SIGNED + signature evidence | same SIGNED history | recompute/re-evaluate quorum under current policy | assume quorum from memory | exact signature + currentness/quorum evidence |
| After PRE_EFFECT before claim | PRE_EFFECT_VALID/AUTHORIZED may be durable | same state, no claim | revalidate currentness/authority then claim | reuse stale PRE_EFFECT indefinitely | exact currentness/effect-authority evidence |
| After CLAIMED before known external invocation | CLAIMED | CLAIMED/OUTCOME_UNKNOWN as applicable | downstream exact-key query; controlled continuation only if non-invocation is proven and policy still valid | blind invocation/reclaim | claim identity + downstream query/absence evidence |
| After external call before local COMMITTED | CLAIMED/OUTCOME_UNKNOWN, effect may have happened | OUTCOME_UNKNOWN unless exact receipt already durable | reconciliation query only | blind retry | authenticated receipt/query/not-applied proof |
| After COMMITTED before client response | COMMITTED + exact terminal result/receipt | exact same COMMITTED result | return same result | second external effect | terminal result + receipt identity |
| During fence rollover | old or new fence transition | exactly one current fence, predecessor preserved | successor continues from recovered state | stale predecessor mutation | fence-chain evidence |
| During transition write/torn write | prior committed revision or detectably corrupt partial | prior state or CORRUPT, never fabricated successor | depends on exact recovered authoritative state | guessing intended successor | record/transition integrity proof |
| During partition | possibly divergent observation | no mutation success unless candidate's consistency contract proves one authoritative branch | resume only after authoritative state established | LWW merge/guess | partition resolution + exact history |
| After lost response for reservation/transition | commit may have happened | exact existing record if committed | resolve/replay exact identity | create alternate operation | exact authoritative lookup |

## 9. Downstream effect reconciliation requirements

This section separates ledger/backend guarantees from downstream API guarantees.

### 9.1 Backend guarantees

The backend MUST guarantee:

B-E1.
Unique effect claim for exact protected effect identity.

B-E2.
Durable claim state before effect invocation is treated as authorized.

B-E3.
Persistence of:
- exact target/effect identity;
- payload/effect digest;
- external idempotency key;
- claim identity;
- process fence;
- last applicable PRE_EFFECT/currentness evidence identity;
- invocation/result/reconciliation evidence.

B-E4.
Explicit OUTCOME_UNKNOWN state.

B-E5.
No transition from unknown outcome to success/failure without reconciliation evidence.

B-E6.
No blind effect retry from CLAIMED/OUTCOME_UNKNOWN.

B-E7.
Lost client/backend response resolves to exact prior ledger state/result.

### 9.2 Downstream API guarantees

For irreversible effects, downstream integration MUST provide either:

D-E1.
Idempotency-key acceptance with stable semantics for the exact operation;

OR

D-E2.
An independently proven exactly-once effect protocol.

Additionally, where reconciliation is required:

D-E3.
Authenticated query by exact operation/idempotency identity.

D-E4.
Authenticated receipt proving executed effect and exact matching payload/target.

D-E5.
Authenticated absence/not-applied evidence where the downstream system can actually prove non-execution.

D-E6.
If non-execution cannot be proven:
outcome remains UNKNOWN; no blind retry.

D-E7.
Responses/results must be attributable to the exact downstream operation, not merely textual success.

### 9.3 Last-enforceable PRE_EFFECT/currentness fence

Before irreversible invocation:
the executor must verify the last enforceable applicable currentness/effect-authority condition.

If authority/currentness can change between local claim and downstream acceptance, the integration must provide:
- downstream fence/equivalent; or
- another proven mechanism preventing stale claim execution.

If this cannot be proven:
irreversible execution is BLOCKED.

Backend transaction semantics alone cannot make an arbitrary external system atomic.

## 10. Retention / GC requirements

The following evidence MUST NOT be deleted while replay, collision, audit, successor recovery or uncertain downstream outcome remains possible:

- request_id + request_digest;
- operation_id + exact effect binding;
- nonce/replay identity;
- collision records;
- state transition chain;
- state_revision history needed for causality;
- process_fence history;
- signature/quorum evidence identities required for recovery;
- PRE_EFFECT/currentness evidence identities;
- effect claim identity;
- external idempotency key;
- invocation identity;
- authenticated receipt/query evidence;
- OUTCOME_UNKNOWN evidence;
- terminal result identity;
- reconciliation/conflict evidence;
- integrity/corruption evidence needed to explain blocking state.

GC is allowed only after a separately defined policy proves that:
- no admissible replay/collision can refer to the identity;
- no downstream effect can still be uncertain;
- no required historical verification depends on it;
- no successor/recovery path needs it.

Numeric retention:

UNKNOWN

because no supported runtime/business/downstream replay horizon evidence was supplied.

## 11. Backend-neutral capability tests

| Test | Precondition | Action / fault | Expected observable result | PASS criterion |
|---|---|---|---|---|
| T01 Atomic reservation | no request/operation/nonce exists | attempt one reservation; inject failure at each internal write boundary | either all reservation identities/state appear, or none | never partial visible reservation |
| T02 Uniqueness race | empty protected identity | two concurrent incompatible reservations for same request/operation/nonce | one winner max; other exact conflict | no overwrite, no two successes |
| T03 Stale fence | process A owns fence F1; successor gets F2 | A attempts transition after F2 authoritative | A rejected stale/conflict | no state/effect from F1 after rollover |
| T04 Crash recovery | committed state exists | crash process/host immediately after commit before response | exact committed state/result visible after restart | same revision/history/result recovered |
| T05 Commit/readback | candidate reports commit success | immediate independent read then restart read | same exact committed semantic record | success never precedes durable readable record |
| T06 Corruption | valid operation history exists | alter/miss one required semantic record/evidence link | CORRUPT/UNKNOWN/block | no silent success/repair/NOT_APPLIED |
| T07 Partition | authoritative store becomes unreachable or partitioned | perform authority-bearing lookup/mutation | unavailable/unknown/block | absent is never inferred from unavailable |
| T08 Lost response | operation commit succeeds; response dropped | client retries exact same identity | same existing state/result; no duplicate work | invocation/reservation count unchanged |
| T09 Concurrent transition | state revision R; two writers race R→different successors | simultaneous transition attempts | at most one commit | loser sees conflict/current state |
| T10 Effect claim race | AUTHORIZED exact effect, no claim | two processes claim same effect | one claim max | one current claim identity/fence only |
| T11 Duplicate terminal retry | terminal result exists | exact client retry | same terminal result/replay classification | no new transition/effect |
| T12 Changed-content retry | request_id exists | retry same ID with changed digest/binding | durable collision | existing history unchanged |
| T13 Restart after torn write | inject power/write interruption during transition | restart/read | prior commit or corruption indication | never fabricated successor state |
| T14 Delayed stale response | transition R1 superseded by R2 | deliver R1 response after R2 committed | consumer/backend rejects as stale identity | R2 remains authoritative |
| T15 OUTCOME_UNKNOWN | claim exists; downstream result unavailable | retry/recovery | explicit unknown + reconciliation path | no second irreversible call |
| T16 Authoritative absence | no row exists on healthy authoritative view | exact lookup | NOT_APPLIED | only passes if current/read integrity proven |

A candidate fails admission if the test cannot be constructed or its PASS criterion cannot be independently observed for the claimed deployment model.

## 12. Candidate evaluation matrix

| Requirement | Mandatory / optional | Evidence required | Disqualifying failure | Unresolved assumption |
|---|---|---|---|---|
| Atomic multi-key reservation/equivalent | MANDATORY | documented semantics + concurrent/fault test | partial reservation possible | candidate primitive unknown |
| Unique constraints under concurrency | MANDATORY | race test | two incompatible successes | topology unknown |
| Conditional revision transition | MANDATORY | compare-and-transition test | stale overwrite | primitive unknown |
| Process fencing/equivalent | MANDATORY | rollover/stale-writer test | old writer can publish | fence implementation unknown |
| Durable commit crash survival | MANDATORY | crash/power/restart evidence | acknowledged commit disappears | storage stack unknown |
| Exact operation-history recovery | MANDATORY | restart/recovery test | history cannot reconstruct state | history representation unknown |
| Terminal-result persistence | MANDATORY | replay after restart | duplicate work after lost response | retention policy unknown |
| Corruption detection | MANDATORY | injected corruption test | silent acceptance | integrity mechanism unknown |
| Authoritative absence proof | MANDATORY | partition/stale replica tests | unavailable indistinguishable from absent | replication model unknown |
| Cross-process visibility | MANDATORY | competing process tests | incompatible success from stale view | consistency model unknown |
| Unique effect claim | MANDATORY | effect-race test | multiple successful claims | claim primitive unknown |
| OUTCOME_UNKNOWN preservation | MANDATORY | lost downstream result test | blind retry/false success | downstream behavior unknown |
| Authenticated downstream query | MANDATORY for irreversible effects needing reconciliation | API evidence/test | outcome cannot be resolved safely | downstream API unknown |
| Authenticated downstream receipt | MANDATORY for irreversible effect commit | exact receipt verification | success only textual/unbound | downstream API unknown |
| Downstream idempotency or proven exactly-once | MANDATORY for irreversible effects | API contract + fault tests | duplicate irreversible effect possible | downstream API unknown |
| Authenticated not-applied/absence evidence | MANDATORY where retry after uncertainty is expected; otherwise operation must remain blocked | downstream contract/test | missing receipt treated as non-execution | capability may not exist |
| Retention/GC safety | MANDATORY | policy + replay horizon evidence | evidence deleted while replay/uncertainty possible | numeric horizon UNKNOWN |
| Operational observability | MANDATORY | exact status/readback API | cannot distinguish conflict/corrupt/unavailable | candidate API unknown |
| Performance/latency optimization | OPTIONAL at this gate | benchmark after correctness | not disqualifying unless violates operational SLA later | SLA not defined |
| Horizontal scale | OPTIONAL at this gate unless future workload requires | workload evidence | not disqualifying now | workload unknown |

## 13. Backend disqualifiers

A backend/candidate deployment is DISQUALIFIED for this STP-C ledger role if any of the following is true:

DQL1.
Last-write-wins can overwrite conflicting state without conflict detection.

DQL2.
Correctness relies only on per-process locking while multiple processes may write.

DQL3.
Atomic multi-key reservation or an observationally equivalent primitive cannot be proven.

DQL4.
Backend unavailability/partition cannot be distinguished from authoritative absence.

DQL5.
Exact operation history cannot be recovered after crash/restart.

DQL6.
Semantic corruption may be silently accepted as valid state.

DQL7.
No stale-writer fencing or equivalent observable guarantee exists.

DQL8.
Duplicate retries can create duplicate reservation/signing/effect work.

DQL9.
Effect claim uniqueness cannot be proven under concurrency.

DQL10.
Committed terminal result can disappear or become ambiguous under the claimed failure model.

DQL11.
A stale replica can answer authority-bearing NOT_APPLIED/current-state queries without proven currentness.

DQL12.
There is no suitable basis for downstream idempotency/reconciliation for an irreversible effect class.

DQL13.
Unknown downstream outcome is automatically converted to retry/success/failure without authenticated evidence.

DQL14.
Partial visible success is possible across request/operation/nonce reservation or transition/evidence persistence.

## 14. Remaining decisions

Requirements are complete enough to justify a separate candidate-comparison gate.

Still open, but NOT blockers to comparison:

- concrete candidate backends to evaluate;
- exact candidate deployment topology;
- exact persistence/storage hardware semantics;
- exact replication/partition model;
- exact process_fence issuance mechanism;
- exact integrity encoding/check mechanism;
- exact downstream systems/APIs;
- numeric retention/GC horizon;
- performance/SLA requirements;
- workload/throughput envelope.

Numeric retention:
UNKNOWN

Concrete backend:
NOT_SELECTED

Implementation:
NOT_AUTHORIZED

Live storage:
NOT_CREATED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Gate status:

READY_FOR_BACKEND_CANDIDATE_COMPARISON_GATE

## 15. Boundary preservation

No:
- SQLite/Postgres/KV/other backend selection;
- product ranking/scoring;
- implementation;
- live storage;
- host mutation;
- keys/secrets/credentials;
- deployment;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → превратить ledger design из логической схемы в проверяемый профиль требований к будущему хранилищу.

Проба → пройти по отказам, конкуренции, fencing, crash windows и внешнему эффекту так, чтобы каждое обещание backend можно было проверить наблюдаемым тестом.

Результат → сформирован backend-neutral admission profile: обязательные гарантии, capability tests, disqualifiers и граница downstream API.

Успех → можно переходить к отдельному gate сравнения кандидатов без выбора продукта по удобству или привычке.

Урок → слово "transaction" само по себе ничего не доказывает. Нужен наблюдаемый ответ на скучный вопрос: что именно останется после падения питания, двух писателей и потерянного ответа. Скучные вопросы, как обычно, спасают систему от очень дорогих приключений.

## Terminal

PASS_SIS_STP_C_LEDGER_BACKEND_REQUIREMENTS_R01_READY_FOR_CANDIDATE_COMPARISON

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
