# KOO → SIS: STP-C ledger backend candidate comparison r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: DOCUMENT_ONLY_BACKEND_CANDIDATE_DISCOVERY_AND_COMPARISON
project_time: omitted

Resume-First.

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

Exact authority:

puev5691/wellbeing-hq@23858faf814e6c3254c16045212bb3e6c47087bd:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-ledger-backend-candidate-comparison-r01__OPERATOR.md

Exact requirements profile:

puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md

blob:
73ede64f24208419ca339d8d2c2d40b2e3d9670a

Exact SHD ledger review:

puev5691/wellbeing-hq@3a485af0511e59516504a6357df3caf841bcad8a:
entities/shardovik/outbox/SHD__STP-C-replay-effect-ledger-atomicity-r01-independent-review__KOO.md

Exact KOD ledger contract:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

blob:
98bcee62b376b3d9b1ac52812d483b01fae9daa5

Perform only a document-only backend candidate discovery/comparison.

## 1. Candidate discovery

Identify a bounded set of technically plausible concrete backend candidates/classes.

Do not select candidates because they are familiar or convenient.

For inclusion, require a plausible path to satisfy at least:
- atomic multi-key reservation or equivalent;
- concurrent uniqueness enforcement;
- compare-and-transition / fencing equivalent;
- crash durability;
- exact operation-history recovery;
- authoritative absence semantics;
- corruption handling;
- cross-process correctness.

Exclude obvious disqualifiers early.

Use current primary/official technical documentation for factual product claims where available.
Record exact source/version/documentation locator where practical.

Do not infer capability from marketing language.

## 2. Requirements comparison

Compare every admitted candidate against the exact mandatory matrix from:

SIS__STP-C-ledger-backend-requirements-r01__KOO.md

For each mandatory requirement return one of:

SUPPORTED_BY_DOCUMENTED_PRIMITIVE
SUPPORTED_WITH_DESIGN_CONSTRAINT
NEEDS_EMPIRICAL_PROOF
UNKNOWN
DISQUALIFIED

Do not collapse UNKNOWN into PASS.

## 3. Mandatory dimensions

At minimum compare:

- multi-key atomic reservation;
- uniqueness under concurrency;
- revision/state CAS or equivalent;
- process fencing support/equivalent design;
- durable commit semantics;
- process/host crash recovery;
- power-loss boundary;
- torn/partial-write handling;
- cross-process visibility;
- network partition/unavailability semantics;
- authoritative absence;
- corruption/integrity detection;
- exact operation-history recovery;
- retention/GC feasibility;
- backup/restore implications for replay history;
- observability/readback;
- suitability for deterministic test harness;
- operational complexity;
- single-host vs replicated deployment implications.

## 4. Downstream effect boundary

Do not treat backend capability as proof of downstream exactly-once execution.

For each candidate state explicitly:
backend can/cannot help with:
- idempotency ledger;
- effect claim;
- reconciliation evidence storage.

Backend does NOT by itself prove:
- downstream idempotency-key behavior;
- authenticated downstream query;
- authenticated receipt;
- authenticated NOT_APPLIED;
- external exactly-once.

Keep that boundary explicit.

## 5. Failure-model evidence

For each candidate identify:
- what is documented;
- what must be empirically tested;
- what depends on deployment configuration;
- what remains UNKNOWN.

Especially distinguish:
product capability
from
configured deployment guarantee.

## 6. Disqualification

Apply exact requirements profile disqualifiers.

If a candidate fails a mandatory property with no equivalent design path:
DISQUALIFIED.

Do not compensate a mandatory failure with convenience, popularity or performance.

## 7. No ranking by taste

Do not produce a subjective score.

Instead produce:
candidate
→ mandatory requirements satisfied
→ constraints
→ empirical proofs still needed
→ disqualifiers
→ operational consequences.

If more than one candidate remains viable, preserve multiple viable candidates.

## 8. Decision gate

Conclude one of:

A.
READY_FOR_OPERATOR_BACKEND_CANDIDATE_DECISION
with the exact surviving candidates and the factual differences the OPERATOR must choose between;

B.
READY_FOR_BOUNDED_EMPIRICAL_BACKEND_PROOF
if documented evidence is insufficient and a narrow non-production test is required before decision;

C.
BLOCKED_BACKEND_CANDIDATE_COMPARISON
with exact missing evidence.

Do NOT silently select a winner.

## 9. Boundaries

No:
- backend installation;
- live storage;
- host mutation;
- deployment;
- credentials/secrets;
- production test;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

Expected terminal:

PASS_SIS_STP_C_LEDGER_BACKEND_CANDIDATE_COMPARISON_R01_READY_FOR_DECISION_OR_PROOF

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
