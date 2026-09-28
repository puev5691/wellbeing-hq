# KOO → KOD: STP-C bounded backend empirical proof harness design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DOCUMENT_ONLY_BOUNDED_EMPIRICAL_PROOF_HARNESS_DESIGN
project_time: omitted

Resume-First.

Current authoritative KOD writer:

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

Exact authority:

puev5691/wellbeing-hq@96129f347ed68553adfb12a833728c27455d35c8:
entities/koordinator/outbox/KOO__authorize-KOD-STP-C-backend-bounded-empirical-proof-design-r01__OPERATOR.md

Exact SIS candidate comparison:

puev5691/wellbeing-hq@9f401ffef3b3d90ec28a2786ec076d87d36f7e74:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-candidate-comparison-r01__KOO.md

blob:
da9dedea095bc245f03d19b0e595c27740aa3464

Exact backend requirements profile:

puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md

blob:
73ede64f24208419ca339d8d2c2d40b2e3d9670a

Exact ledger atomicity contract:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

Design only the bounded non-production empirical proof harness.

Candidates in scope:

- PostgreSQL 18
- FoundationDB 7.4.8
- etcd 3.7
- CockroachDB v26.1/current stable line

No ranking and no backend selection.

## 1. Common proof model

Define one common logical STPC_LEDGER test model so every candidate is tested against the same semantics:

- request_id
- request_digest
- operation_id
- nonce_identity
- state_revision
- process_fence
- effect_claim
- idempotency_key
- transition/evidence identity
- terminal result
- OUTCOME_UNKNOWN/reconciliation evidence

Candidate adapters may map primitives differently, but PASS oracle must remain semantically identical.

## 2. Exact tests

At minimum design tests for:

T01 atomic reservation
T02 uniqueness race
T03 state_revision CAS
T04 stale process_fence
T05 acknowledged commit + process crash/restart
T06 acknowledged commit + host crash/restart
T07 power-loss boundary where safely testable
T08 torn/partial-write or nearest safe corruption injection
T09 partition/unavailability != absence
T10 authoritative absence
T11 lost response after commit
T12 concurrent transition race
T13 effect-claim race
T14 OUTCOME_UNKNOWN no-blind-retry
T15 backup/restore + successor fence/currentness
T16 exact operation-history recovery
T17 retention of replay/collision/uncertain-effect evidence
T18 stale/delayed response after newer revision
T19 corruption/integrity detection
T20 missing linked evidence / transition-chain break

CockroachDB:
explicitly include a proof path for the documentary UNKNOWN on exact corruption/integrity requirement.
If safely proving this is not feasible, return that as candidate-specific unresolved blocker, not PASS.

## 3. For every test define

- exact precondition;
- initial ledger rows/keys/state;
- actors/processes;
- deterministic barrier/synchronization point;
- fault injection point;
- expected authoritative state;
- expected client-visible classification;
- forbidden outcome;
- evidence to capture;
- PASS criterion;
- FAIL criterion;
- cleanup/reset procedure;
- whether test is common or candidate-specific.

## 4. Evidence contract

Define a uniform machine-readable evidence bundle candidate containing at minimum:

- candidate identity/version;
- deployment topology identity;
- configuration identity;
- test_id;
- run_id;
- exact initial-state identity;
- exact fault point;
- actor/process identities;
- observed responses;
- post-fault authoritative readback;
- operation-history identity;
- integrity/corruption check output identity;
- PASS/FAIL/UNKNOWN classification;
- reason code.

No secret values in evidence.

## 5. Reproducibility

Specify:
- deterministic seed/input where applicable;
- exact test ordering constraints;
- reset requirements;
- no result reuse across candidate/version/config changes;
- configuration change => new proof identity;
- deployment topology change => new proof identity.

## 6. Safety boundary

The proof must be:
- non-production;
- isolated;
- destructive only inside disposable test storage;
- no real external irreversible effects.

For downstream-effect tests, use a deterministic fake/mock effect service capable of:
- idempotency-key acceptance;
- authenticated-style test receipt;
- query by exact operation identity;
- controlled lost response;
- controlled delayed response;
- controlled UNKNOWN state.

Do not call any real external effecting system.

## 7. Candidate adapter requirements

For each backend define only the adapter obligations needed to instantiate the common tests:

PostgreSQL 18
FoundationDB 7.4.8
etcd 3.7
CockroachDB v26.1/current stable

Do not choose production topology.

Where a test depends on topology/config, mark exact required test configuration variants.

## 8. Fault injection design

Prefer safe, deterministic non-production mechanisms.

Do not require dangerous physical power interruption if an equivalent test cannot be safely controlled.
For true power-loss semantics that cannot be proven safely in this environment, mark:
NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF
and keep it separate from ordinary crash tests.

Do not fake power-loss PASS from process kill.

## 9. Oracle rules

No candidate may PASS a test because:
- command exited 0;
- service restarted;
- log says success;
- request timed out.

PASS must come from exact observable ledger/evidence semantics.

UNKNOWN stays UNKNOWN.

Unavailable != absent.
Lost response != failed effect.
Recovered process != recovered authority.

## 10. Test execution gate

End by specifying exactly what would be needed to authorize a later bounded execution:
- disposable environment;
- candidate/version/config pin;
- allowed commands/actions;
- resource limits;
- fault methods;
- evidence output path;
- cleanup;
- stop conditions.

Do not execute them now.

## 11. Result gate

Conclude one of:

READY_FOR_INDEPENDENT_PROOF_HARNESS_REVIEW

or exact BLOCKED_ if a conceptual harness gap prevents fair comparison.

Expected terminal:

PASS_KOD_STP_C_BACKEND_BOUNDED_EMPIRICAL_PROOF_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

Do NOT:
- install/run backends;
- choose winner;
- create live storage;
- mutate production hosts;
- handle secrets;
- deploy;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
