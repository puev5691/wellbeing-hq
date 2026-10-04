# SHT -> KOO: SECE runtime-integration architecture C1-C3 correction R02

status: ARCHITECTURE_CORRECTION_COMPLETE_NOT_ACTIVE
terminal: PASS_SHT_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_C1C3_CORRECTION_R02_READY_FOR_NARROW_REREVIEW
execution_attempt_id: SHT_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_C1C3_CORRECTION_R02_A1
project_time: omitted

## Human result
R01 overall runtime-integration architecture is preserved. Only SHD C1-C3 interface defects are corrected.

C1 closes the evidence/trust interface: positive task/authority/currentness/writer facts cannot originate from adapter/model/profile/memory inference.
C2 closes the TOCTOU/bypass interface: EffectAdapter cannot execute from EffectIntent alone; it requires a matching current machine-bound PRE_EFFECT_ADMISSION for that exact intent and evidence frontier.
C3 closes worker/writer ambiguity: actor execution mode, current writer, exact writer requirement, mutation class and Recovery/freeze/handoff basis travel end-to-end and are revalidated at effect boundary.

No runtime implementation or activation is created.

## Exact basis
Authority:
puev5691/wellbeing-hq@7a8e22b752e338486f794e8256743ee11b145751:
entities/koordinator/outbox/KOO__authorize-SHT-SECE-runtime-integration-C1C3-correction-R02__OPERATOR.md
blob a06c63c523f55fa6b839eba5b4885bd6529e549f.

Correction specification:
puev5691/wellbeing-hq@0d806d9a28d724e8e107f0f59a8bd6d105385fb1:
entities/koordinator/outbox/KOO__SECE-runtime-integration-C1C3-correction-decision__OPERATOR.md
blob dcbcbe451d02b84ab1f86fd44023622998815417.

SHD review:
puev5691/wellbeing-hq@0c0a3c3fd1391fb2cfecea19ba62a20850e6d78f:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-architecture-review-r01__KOO.md
blob 64f4d8db1da39a001d9ded75d61b0a4d8896b448
terminal NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_REVIEW_R01.

Predecessor architecture:
puev5691/wellbeing-hq@6d25ba2487d8b48de2365091801bcc3d070bcdcc:
entities/shtabist/outbox/SHT__SECE-r01-runtime-integration-architecture-r01__KOO.md
blob 032304ba729e55eb05a7a27577df85374b92e7f1.

Fresh pre-start HEAD 228deb4f1f97f00870be2b64a4efc5e7cb04c0aa.
Current SHT writer blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.
Initial execution state blob 6b37062427199fc4aa278a63c2a25ba20e4b233e, INITIAL_NOT_STARTED_V1.

PROCESSING_STARTED:
puev5691/wellbeing-hq@40fc3ca6c307d8a67e75bab294f05d43ec0cebeb:
entities/shtabist/outbox/execution-evidence/SHT_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_C1C3_CORRECTION_R02_A1__PROCESSING_STARTED_E1.md
blob 4377de43e8bcd37dc50fe00c4af8e75a07b181ed.

# C1 — closed RuntimeEvidenceResolver provenance/trust contract

Add machine object RUNTIME_EVIDENCE_RESOLUTION.

Each evidence item:
- evidence_id
- evidence_kind
- exact_immutable_locator
- exact_version_or_blob
- exact_scope
- source_class: ACTIVE_PROJECT_SOURCE | OPERATOR_DECISION | TASK_CONVEYOR | RECOVERY | CURRENT_WRITER | VERIFIED_EVENT | VERIFIED_RESULT | OTHER_EXPLICIT
- trust_basis_ref
- verified_state: VERIFIED | UNVERIFIED | INVALID
- currentness_state: CURRENT | STALE | SUPERSEDED | UNKNOWN
- semantic_fact_class
- authority_class when applicable
- authority_action_classes[]
- authority_scope when applicable
- task_ref/currentness when applicable
- actor/writer binding when applicable
- conflict_state: NONE | CONFLICT | UNKNOWN
- selected_basis_relation: SELECTED | REFINES | SUPERSEDES | HISTORICAL | INDEPENDENT | CONFLICTS | NOT_SELECTED
- provenance_chain[]
- derived_positive_fact_ids[]
- unknown_fields[].

Resolution result:
resolution_id
input_evidence_ids[]
selected_fact_bindings[]
unknown_fact_bindings[]
conflict_sets[]
rejected_inference_attempts[]
resolution_verdict: RESOLVED | PARTIAL_UNKNOWN | CONFLICT | INVALID
provenance_digest.

Closed invariants:
1 RuntimeInputAdapter may transport/normalize only; it cannot mark authority/currentness/writer/task as positive.
2 RuntimeEvidenceResolver may emit a positive authority/currentness/writer/task fact only when at least one exact authoritative evidence item supports that exact semantic fact/scope and is VERIFIED + CURRENT where currentness is required + non-conflicted.
3 capability/profile/experience/memory/model output/human assertion without independently valid decision/evidence status cannot become authority/currentness.
4 missing support => ABSENT or UNKNOWN, never inferred PASS.
5 conflicting applicable support => CONFLICT, never winner-by-order.
6 every positive fact in RuntimeInputEnvelope/EFFECTIVE_CONTEXT/contract carries evidence_id + trust_basis_ref + provenance chain.
7 unresolved provenance for any effect-sensitive fact => dependent EffectIntent cannot be admitted.
8 outcome evidence uses the same provenance contract: PRE_EFFECT_INTENT cannot become EVIDENCED_SUCCESS/FAILURE without separate outcome evidence.

Machine predicate:
POSITIVE_RUNTIME_FACT_ADMISSIBLE(f) =
supporting_evidence_exact(f)
AND trust_class_allowed(f)
AND verified_state=VERIFIED
AND required_currentness=CURRENT
AND conflict_state=NONE
AND scope_matches(f)
AND provenance_chain_complete.

Else fact state = ABSENT | UNKNOWN | CONFLICT | INVALID.

This closes authority/currentness manufacture at architecture level.

# C2 — machine-bound PRE_EFFECT_ADMISSION

EffectIntentCandidate receives immutable intent_id computed/bound from:
contract_id
effective_context_id/version
action_id/class
selected_scope
action parameters/target identity where applicable
required authority/task/writer/Recovery/input evidence IDs
effect_adapter_class
required outcome evidence mode.

PreEffectRevalidator produces PRE_EFFECT_ADMISSION object:

admission_id
intent_id
contract_id
effective_context_id/version
action_id/class
selected_scope
action_target_identity
intent_payload_digest
authority_evidence_refs[]
task_evidence_refs[]
writer_worker_evidence_refs[]
recovery_freeze_handoff_evidence_refs[]
input_version_refs[]
current_state_evidence_refs[]
source_provenance_refs[]
prior_effect_state_refs[]
adapter_class
adapter_authority_ref
adapter_effect_class_scope
expected_current_evidence_versions[]
revalidation_verdict: ADMIT_EFFECT_NOW | NO_EFFECT_UNKNOWN | NO_EFFECT_BLOCKED | NO_EFFECT_STOP | NO_EFFECT_REJECT
revalidation_reason_ids[]
admission_basis_digest
predecessor/current evidence identities
provenance[].

Freshness is evidence/version/state freshness, never wall-clock authority.

EffectAdapter interface MUST accept:
EffectIntent + PRE_EFFECT_ADMISSION.

Adapter MUST reject/no-effect unless:
- admission intent_id exact match;
- contract/context/action/scope/target/payload digest exact match;
- adapter class exact match;
- adapter authority current and covers effect class/scope;
- all evidence refs/current versions still match at invocation boundary;
- actor/writer/Recovery binding remains eligible;
- no unresolved overlapping prior effect;
- verdict = ADMIT_EFFECT_NOW.

Any stale/mismatch/UNKNOWN/conflict/missing admission => NO_EFFECT.

Admission is single-current-evidence-frontier bound: if any listed expected current evidence version changes before adapter invocation, admission is invalid and a NEW revalidation is required. Do not infer exactly-once; repeated invocation safety remains effect-class specific and unresolved prior effect blocks overlap.

PRE_EFFECT_INTENT remains intent, not effect.
PRE_EFFECT_ADMISSION remains admission evidence, not outcome.
EffectOutcome still requires separate observed evidence.

Machine predicate:
EFFECT_ADAPTER_CALL_ELIGIBLE =
intent_identity_match
AND admission_identity_match
AND admission_verdict=ADMIT_EFFECT_NOW
AND evidence_frontier_unchanged
AND adapter_authority_valid
AND actor_effect_eligibility_valid
AND unresolved_prior_effect=NO.

This closes TOCTOU/bypass at architecture level.

# C3 — explicit actor / writer / worker / Recovery binding

Add ACTOR_EXECUTION_BINDING carried unchanged by identity through:
RuntimeInputEnvelope
-> RUNTIME_EVIDENCE_RESOLUTION
-> EFFECTIVE_CONTEXT dependency
-> ExecutionContract
-> EffectIntent
-> PRE_EFFECT_ADMISSION.

Fields:
actor_instance_ref
actor_role
actor_execution_mode: CURRENT_WRITER | WORKER_READ_ONLY | OTHER_EXPLICIT_CLASS | UNKNOWN
current_writer_ref
current_writer_state: CURRENT | ABSENT | CONFLICT | UNKNOWN
writer_requirement: REQUIRED | NOT_REQUIRED_FOR_TASK | UNKNOWN
authoritative_state_mutation_required: YES | NO | UNKNOWN
effect_mutation_class: READ_ONLY_ANALYSIS | CANDIDATE_ARTIFACT_WRITE | AUTHORITATIVE_CURRENT_STATE_WRITE | EXTERNAL_EFFECT | OTHER_EXPLICIT
worker_effect_authority_ref
writer_authority_ref
recovery_state_ref
freeze_state: CLEAR | FROZEN | UNKNOWN
handoff_state: NONE | ACTIVE | CONFLICT | UNKNOWN
replacement_state: NONE | REPLACED | UNKNOWN
recovery_evidence_refs[]
binding_provenance[].

Invariants:
1 WRITER_NOT_REQUIRED_FOR_TASK means only that this task/effect does not require current-writer authority under applicable active Recovery/task rules. It never changes actor_execution_mode to CURRENT_WRITER and never creates current_writer_ref.
2 CURRENT_WRITER eligibility requires exact current-writer evidence plus compatible Recovery/freeze/handoff state.
3 WORKER_READ_ONLY may perform only independently authorized effect/mutation classes that do not require current-writer. It cannot perform AUTHORITATIVE_CURRENT_STATE_WRITE.
4 CANDIDATE_ARTIFACT_WRITE is distinct from AUTHORITATIVE_CURRENT_STATE_WRITE and requires its own task/file authority.
5 EXTERNAL_EFFECT eligibility is independent of writer status unless exact governing rule requires writer; it always requires separate effect-class authority and PRE_EFFECT_ADMISSION.
6 writer_requirement=UNKNOWN or authoritative_state_mutation_required=UNKNOWN => NO_EFFECT for any dependent mutation.
7 freeze/handoff/replacement conflict/UNKNOWN blocks dependent authoritative mutation/effect until reconciled.
8 actor binding used by contract must equal actor binding used by PRE_EFFECT_ADMISSION; any change invalidates admission.

Actor effect eligibility table:
- CURRENT_WRITER + writer REQUIRED + exact writer evidence + clear Recovery + exact effect authority => potentially eligible subject to all other gates.
- WORKER_READ_ONLY + writer REQUIRED => NO_EFFECT.
- WORKER_READ_ONLY + NOT_REQUIRED_FOR_TASK + READ_ONLY_ANALYSIS + exact task/effect authority => potentially eligible.
- WORKER_READ_ONLY + NOT_REQUIRED_FOR_TASK + AUTHORITATIVE_CURRENT_STATE_WRITE => NO_EFFECT.
- any mode + UNKNOWN writer requirement where mutation depends on it => NO_EFFECT.
- WRITER_NOT_REQUIRED_FOR_TASK alone => no positive writer inference.

# Minimal dependent adjustment to R01 flow

R1 RuntimeEvidenceResolver now outputs closed RUNTIME_EVIDENCE_RESOLUTION plus ACTOR_EXECUTION_BINDING.

R2-R4 unchanged except Effective Context/contract preserve exact evidence and actor-binding references.

R5 PreEffectRevalidator consumes exact EffectIntent + current evidence frontier and emits PRE_EFFECT_ADMISSION.

R6 durable PRE_EFFECT_INTENT remains separate. Architecture does not require admission itself to mean effect occurred.

R7 EffectAdapter signature becomes:
execute(EffectIntent, PRE_EFFECT_ADMISSION)
and MUST fail closed if EFFECT_ADAPTER_CALL_ELIGIBLE is false.

R8 outcome provenance is resolved through C1 evidence contract.

R9-R10 unchanged.

# Preservation of unrelated R01 review PASS boundaries

Unchanged:
- simulator core does not silently become runtime;
- EffectAdapter remains outside semantic core and separately authorized;
- unresolved prior effect blocks unsafe replay;
- intent cannot fabricate outcome;
- NextGate cannot bypass Task Conveyor;
- human explanation uses same causal trace;
- future gates create no implementation/deployment authority;
- accepted offline baseline unchanged;
- Semantic Bootstrap / Dialogue Engine / PROJECT_OPERATIONS division unchanged;
- no exactly-once claim;
- no automatic replay.

# Correction closure

C1_RUNTIME_EVIDENCE_PROVENANCE_TRUST_CLOSED=YES
C2_MACHINE_BOUND_PRE_EFFECT_ADMISSION_CLOSED=YES
C3_WORKER_WRITER_RECOVERY_BINDING_CLOSED=YES

runtime implementation: NONE
simulator activation/use: NONE
host/service/storage mutation: NONE
provider/model/API/Telegram: NONE
credentials: NONE
Project Source/canon mutation: NONE
role/recovery/current-writer mutation: NONE
deployment/sandbox/live effects: NONE
production authority: NONE
automatic SHD rereview: NONE

# Exact next causal gate classification

NARROW_INDEPENDENT_C1C3_ARCHITECTURE_REREVIEW_REQUIRED_AFTER_KOO_RECONCILIATION_AND_SEPARATE_TASK_AUTHORITY.

Review only:
C1 closed provenance/trust contract;
C2 machine-bound admission/TOCTOU closure;
C3 actor/writer/worker/Recovery binding;
and verify no unrelated R01 PASS boundary was changed.

This result creates no SHD rereview authority.

## EXPERIENCE
Idea -> convert three prose safeguards into typed objects that must survive every interface boundary.
Probe -> ask what exact machine evidence an adapter would need if every convenient English sentence disappeared.
Result -> evidence provenance, pre-effect admission and actor/writer/Recovery state are explicit and fail-closed.
Success -> C1-C3 can now be rereviewed independently without redesigning runtime flow.
Lesson -> a safety check that is not carried as data to the component that performs the effect is merely advice with better typography.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
