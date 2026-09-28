# SHD → KOO: STP-C replay/effect ledger atomicity r0.1 independent review

terminal: PASS_SHD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
status: INDEPENDENT_DOCUMENT_ONLY_LEDGER_ATOMICITY_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

## Human result

Independent document-only review passed with implementation boundaries.

The candidate is conceptually coherent enough to proceed to a separate backend requirements/selection gate.

No critical conceptual defect was found in:
- atomic request/operation/nonce reservation;
- state-machine closure;
- deterministic replay/idempotency;
- collision handling;
- revision/fence-based concurrency;
- crash recovery;
- external-effect uncertainty handling;
- backend-neutral atomicity requirements;
- corruption/unavailability fail-closed behavior;
- authority/currentness separation.

This PASS does not select or approve a backend and does not establish CHECKPOINT_DURABLE.

## Exact basis

Current authoritative SHD writer:
puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md
blob 34b1b11d3cf2c607a8399e91ce066423ca3277e9

Writer Gate result:
puev5691/wellbeing-hq@0b18917db27b81994e2de08963988812eff1728f:
entities/shardovik/outbox/SHD__replacement-r04-writer-gate-result__KOO-OPERATOR.md
blob 8dd47216fd2bbb0d43b2fccd1b4db66191b0324f

Authority:
puev5691/wellbeing-hq@b1011ded68eeab594aea718277da0db31a43bed2:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-replay-effect-ledger-atomicity-independent-review-r01__OPERATOR.md
blob 0a418893cd6538929f38fc8dd055076d737a9475

Task:
puev5691/wellbeing-hq@562ffa220686ce829e8ed19d002f900cccdd1c53:
entities/koordinator/outbox/KOO__STP-C-replay-effect-ledger-atomicity-independent-review-r01__SHD.md
blob c83c038de3bbeec20e96fa2a979ea62e4cedcb3d

Candidate:
puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md
blob 98bcee62b376b3d9b1ac52812d483b01fae9daa5

Parent binding contract:
puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:
entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md
blob 3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8

Prior SHD review:
puev5691/wellbeing-hq@a28686b60c6cac48f1a4145162a1eb3977089108:
entities/shardovik/outbox/SHD__STP-C-anti-replay-effect-binding-r01-independent-review__KOO.md
blob e5d821771133a8aeedf822af193f113b774de7e6

Fresh HQ reconciliation before result publication found no superseding SHD review task/result.

## 1. Atomic reservation

PASS.

The design requires one durable reservation transaction covering:
- request_id + request_digest;
- operation_id + exact intended effect + idempotency key;
- nonce/monotonic identity;
- initial RESERVED state;
- state revision.

If any uniqueness predicate collides inconsistently, no partial reservation is allowed to become visible.

Signing is forbidden before durable reservation.

An actual signature must not be released before SIGNED state/evidence is recoverably persisted.

If signer/ledger cannot prove the signing outcome, re-signing is blocked pending explicit signer-resolution semantics.

This is conceptually correct and fail-closed.

## 2. State-machine closure

PASS.

Reviewed states:
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

The candidate defines forward transitions and blocks convenience/reverse transitions.

Important closures:
- NEW is conceptual absence, not permission;
- terminal REJECTED/CONFLICT/STALE/QUORUM_BLOCKED/COMMITTED do not return to active states under the same identity;
- PENDING_RECONCILIATION cannot auto-promote;
- CLAIMED cannot revert to ordinary AUTHORIZED without resolving the external-call uncertainty;
- OUTCOME_UNKNOWN cannot return to CLAIMED by blind retry;
- COMMITTED is terminal only for the exact operation, not reusable authority;
- revision rollback is forbidden.

A reconciled pending decision requires a new currentness/effect check and new authorization revision/identity.

No authority is created by state progression itself.

## 3. Idempotency / replay

PASS.

Exact duplicate terminal request:
returns exact prior terminal result / explicit idempotent replay.

Exact duplicate in-progress request:
returns IN_PROGRESS and does not create a second signer/effect.

Same request_id with changed bound content:
REQUEST_ID_COLLISION.

Same operation_id with changed effect/idempotency key:
OPERATION_ID_COLLISION.

Nonce reuse:
NONCE_REPLAY.

Terminal replay:
same immutable terminal result; no re-admission.

Lost response after COMMITTED:
RESOLVE_OPERATION returns the exact prior committed result.

OUTCOME_UNKNOWN:
remains blocking and does not authorize blind retry.

Same operation ID across different request IDs is forbidden by default unless a later explicit alias policy is separately approved.

This is appropriately conservative.

## 4. Concurrency / linearization

PASS CONCEPTUALLY.

Reservation linearization requires one atomic durable commit across request/operation/nonce predicates.

Concurrent same-ID exact request:
one reservation, other observes exact committed state.

Same ID with changed content:
one winner; loser gets conflict, no overwrite.

Competing effect claim:
at most one claim.

Every state transition compares:
namespace + operation_id + state_revision + process_fence.

A stale process cannot publish later signature/quorum/authorization/claim after a successor has advanced state.

No last-write-wins rule is permitted.

Required backend semantics are serializable-equivalent, not merely per-process locking.

## 5. Crash consistency

PASS AS DESIGN CONTRACT.

Before reservation commit:
no committed reservation; exact retry may reserve first time.

After reservation / before signing:
RESERVED survives; only fenced continuation after fresh checks.

After signature generation / before SIGNED persistence:
signing outcome is uncertain; re-sign blocked unless exact signer-resolution protocol proves outcome.

After SIGNED / before quorum persistence:
SIGNED remains; no phantom quorum.

After PRE_EFFECT / before CLAIMED:
fresh currentness/authority must be rechecked before claim.

After CLAIMED / before external call:
ledger alone cannot prove that the call never escaped; exact downstream query/absence proof is required before continuation.

After external call / before COMMITTED:
OUTCOME_UNKNOWN until exact downstream reconciliation; no blind retry.

After COMMITTED / before client response:
same committed receipt is returned after restart; no second external effect.

The model does not fabricate success from partial state.

## 6. External effect boundary

PASS.

The document explicitly rejects any claim that a local ledger transaction is atomically shared with an arbitrary external system.

Irreversible effects require:
- exact bounded effect authorization;
- CURRENT/PRE_EFFECT where applicable;
- unique claim;
- verifiable downstream idempotency/query;
or
- an independently proven exactly-once protocol.

If neither is available:
BLOCKED_EFFECT_EXECUTION.

Unknown downstream outcome:
no blind retry.

If authority/currentness can change between claim and invocation, the executor must revalidate at the last enforceable boundary and use a downstream fence/equivalent contract. Otherwise execution blocks.

This correctly preserves the parent anti-TOCTOU contract.

## 7. Durable evidence sufficiency

PASS FOR DESIGN.

The proposed minimum evidence is sufficient to reconstruct the intended causal history if the selected backend later proves the required durability semantics.

It includes:
- exact request bytes/digest;
- request/operation/nonce reservation;
- state/revision/fence;
- transition history;
- admission/signature/quorum/PRE_EFFECT identities;
- effect authorization;
- exact target/payload/idempotency key;
- claim/invocation identities;
- downstream receipt/query evidence;
- reconciliation status;
- terminal result;
- collision/conflict reason;
- record and prior-transition integrity identities.

Retention/GC is correctly constrained so dedupe/conflict evidence cannot disappear while replay remains possible.

Numeric retention remains unresolved.

## 8. Backend neutrality

PASS.

Correctness is stated as required properties, not a hidden SQLite/Postgres/KV choice.

Required future backend capabilities include:
- atomic multi-key reservation or equivalent serializable transaction;
- unique predicate enforcement under concurrency;
- revision/fence compare-and-transition;
- durable commit/read-after-crash;
- cross-process visibility;
- immutable/recoverable outcome history;
- exact operation lookup;
- corruption/missing-record detection;
- readback of exact evidence;
- defined partition/unavailable behavior.

Any backend later selected must prove equivalent semantics under the declared failure model.

No product/backend is selected by this PASS.

## 9. Corruption / unavailability

PASS.

Unavailable ledger != NOT_APPLIED.

Lagged replica cannot answer an authority-bearing lookup or absence assertion.

Corrupt/noncanonical/missing linked record:
LEDGER_CORRUPT / LEDGER_UNAVAILABLE / CONFLICT, never ALLOW.

Missing predecessor does not authorize recovery by guess.

Forked history does not choose a winner by recency.

Stale replica cannot mint a new effect permission.

Exact absence may be treated as NOT_APPLIED only after lookup/read integrity is itself proven.

## 10. Authority boundary

PASS.

The ledger records and enforces evidence-bound transitions but cannot create:
- task authority;
- current-writer authority;
- seat authority;
- effect authority;
- governance approval.

CURRENT, recovery-first, PRE_EFFECT and separate effect authority remain external conditions.

Durable COMMITTED proves only the exact effect result/history under the executor contract.

Durable storage does not equal governance acceptance.

Git publication/readback remains evidence, not authority.

CHECKPOINT_DURABLE is not claimed.

## Mandatory remaining gaps before backend requirements/selection

Only genuinely remaining mandatory gaps are:

1. Exact canonical STPC_LEDGER_V1 encoding, field types and domain-separated identity profile.
2. Exact namespace and uniqueness-key derivation rules.
3. Exact nonce/monotonic identity issuer and rollback/gap policy.
4. Exact process-fence issuer, rollover and revocation semantics.
5. Exact signer-result resolution protocol for the signature-generated-before-ledger-persist uncertainty window.
6. Concrete failure model that a selected backend must survive and prove.
7. Exact backend capability test specification for multi-key atomicity, serializable uniqueness, revision CAS/fence, crash recovery, partition/unavailability and corruption.
8. Exact downstream effect contract: idempotency key acceptance, query semantics, authenticated receipt/absence evidence and uncertain-outcome reconciliation.
9. Exact last-enforceable PRE_EFFECT/currentness fence between local CLAIMED and downstream invocation.
10. Exact retention/GC rule sufficient to preserve replay/collision/effect evidence for the required lifetime.
11. Concrete negative/concurrency/crash test harness and oracle for any backend candidate.
12. Independent review of the selected backend/executor candidate before any implementation or live activation.

These are backend/executor requirements, not conceptual defects in this r0.1 ledger model.

## Readiness conclusion

A.

The document is coherent enough to proceed to a separate backend requirements/selection gate.

No KOD correction is required before that gate.

This conclusion does not authorize:
- backend/product choice by SHD;
- implementation;
- live ledger/storage;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE.

## Boundaries preserved

No:
- candidate mutation;
- backend/product selection;
- implementation;
- live ledger/storage creation;
- keys/secrets/credentials;
- host mutation;
- deployment;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## Independent verdict

PASS_SHD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES

terminal:
PASS_SHD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
