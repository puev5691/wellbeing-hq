# KOO -> SHT: Entity Semantic Bootstrap Profile r0.1 D1-D3 correction-only

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SHT writer:
puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da

Exact original SHT candidate/result:
puev5691/wellbeing-hq@46f04e4f2d89fae93cedcaee0b21b3529d5c68e9:
entities/shtabist/outbox/SHT__entity-operational-semantics-bootstrap-gap-r01__KOO.md
blob 9849752526f971c0730ae2222e227f5c8149438a

terminal:
PASS_SHT_ENTITY_SEMANTIC_BOOTSTRAP_GAP_CONFIRMED_MINIMAL_PROFILE_CANDIDATE_READY_FOR_REVIEW

Exact KAN normative review:
puev5691/wellbeing-hq@381256e7d5041914ea29481c759c65322256ed7c:
entities/kancelar/outbox/KAN__entity-semantic-bootstrap-profile-r01-normative-review__KOO.md
blob 5a954568ccea73719ba421e88fd4fe63198ef015

terminal:
NEEDS_REWORK_KAN_ENTITY_SEMANTIC_BOOTSTRAP_PROFILE_R01

Scope:
CORRECTION_ONLY_D1_D2_D3

Do not redesign the profile.
Do not activate it.
Do not start ARH review.
Do not touch PKTB D1-D2 lineage.

## D1 — semantic evaluation != admission / initiation / work authority

Correct the candidate so that SEMANTIC_BOOTSTRAP_PASS means only:
successful completion of the exact semantic evaluation in its declared scope.

It MUST NOT:
- create task;
- create writer;
- create authority;
- create approval;
- activate/effectuate a source;
- imply processing_started;
- create production authority;
- independently admit profile work.

Use the KAN-prescribed boundary:

- semantic bootstrap becomes a prerequisite only where a future separately approved effectivity decision explicitly makes it applicable;
- until such effectivity decision, candidate introduces no new gate;
- minimum active Sources, initiation/recovery evidence, role/profile and exact task/evidence may be read before semantic PASS when already permitted by existing authority and Source Loading Policy;
- reading for verification/diagnosis/correction != task execution and != source activation;
- bootstrap does not replace Recovery Canon checks or alter their outcomes;
- semantic FAIL/UNKNOWN/SOURCE_CONFLICT do not invalidate already established identity, writer appointment, integrity/readback or factual terminal result;
- they only block the dependent transition in the exact applicable scope;
- emergency recovery and separately permitted read-only/recovery diagnostics remain governed by Recovery Canon.

Clarify effectivity:
if future integration changes the meaning of a mandatory Recovery Canon procedure, that requires a separate explicit canon amendment/activation. "Complements" is not enough.

Do NOT amend Recovery Canon here.

## D2 — split normative seed from instance binding

Do not expand the seed vocabulary beyond what is necessary.

Classify existing seed slots into two explicit classes:

NORMATIVE_INVARIANT
- representation of an already active applicable norm;
- each mandatory slot has exact source locator/version, normative status and exact semantic basis;
- seed gives no normative force by itself;
- candidate norm cannot populate active normative truth.

INSTANCE_BINDING
- exact verified role/profile/instance/current-state dependency with its own status, scope and provenance;
- not a global norm;
- task/profile/current evidence does not become global Project Source;
- may be loaded before PASS when needed under Source Loading Policy;
- missing binding remains UNKNOWN;
- do not synthesize from memory/general role.

Explicitly classify:
- role identity/ref and exact current-state dependencies -> INSTANCE_BINDING;
- Entity/instance, role/task, authority/capability distinctions -> NORMATIVE_INVARIANT.

For applicability-dependent optional binding:
record reason/applicability; do not invent universal requirement.

Add a compact slot -> source-section mapping for mandatory normative slots.
Do not copy canons.
For mandatory normative slot:
semantic basis must be exact and verifiable.
If basis cannot be established -> slot UNKNOWN and evaluation cannot PASS.

Preserve:
- construction order != precedence;
- active source conflict not resolved by timestamp/order;
- fresh current evidence applies only in exact proven scope;
- no synthetic recovery/current-state reconstruction.

## D3 — deterministic outcome semantics

For every applicable S1-S12 scenario, evaluation must preserve:
- exact scenario/input;
- checkable answer/result;
- source basis;
- scenario outcome;
within one evaluation artifact or referenced evidence.

No separate file per scenario is required.

Overall result rules:
- PASS only if all applicable mandatory scenarios are checked and successful against exact seed/source versions;
- skipped test, missing mandatory input, or insufficient evaluation evidence -> UNKNOWN, not PASS;
- proven wrong transition/answer violating invariant -> FAIL;
- proven contradiction between applicable active approved Sources -> SOURCE_CONFLICT;
- if multiple problems coexist, preserve all scenario outcomes and aggregate:
  SOURCE_CONFLICT > FAIL > UNKNOWN > PASS.
This is only outcome aggregation, not source precedence.

Remove ambiguous "persistent" from human-interface failure criterion.
Use one exact checkable S9 criterion.

For source/seed mismatch distinguish:
- insufficient evidence to compare -> UNKNOWN;
- proven incorrect composition vs verified source -> FAIL;
- conflict between active norms themselves -> SOURCE_CONFLICT.

S9 boundary:
- connected Russian meaning first;
- required exact evidence remains preserved/checkable;
- good prose without required evidence != PASS;
- a human-interface failure triggers correction/retest only of affected scenario/evaluation;
- it does not invalidate factual result, recovery or writer;
- PASS proves only demonstrated application of listed invariants in this exact evaluation, not universal infallibility.

Do not add runtime tester, retry policy or new journal.

## Successor requirements

Create one immutable correction successor artifact/package.

Must include:
- predecessor exact identity;
- KAN review exact identity;
- exact D1-D3 diff;
- corrected candidate text;
- statement that all other candidate distinctions remain unchanged;
- CANDIDATE_NOT_ACTIVE;
- no effectivity claim.

Do NOT:
- activate/create Project Source;
- modify Recovery Canon;
- implement loader/runtime;
- modify semantic engine code;
- change writer/recovery;
- create Entity;
- start ARH review;
- touch PKTB D1-D2 lineage;
- replay historical prompts.

Expected terminal:

PASS_SHT_ENTITY_SEMANTIC_BOOTSTRAP_PROFILE_R01_D1D3_CORRECTION_READY_FOR_KAN_RECHECK

or exact BLOCKED_/FAIL_.

Mandatory RETURN KOO.
Then STOP.
