# SHT -> KOO: SECE r0.1 runtime-integration architecture R01

status: ARCHITECTURE_DESIGN_COMPLETE_NOT_ACTIVE
terminal: PASS_SHT_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_R01_READY_FOR_INDEPENDENT_REVIEW
execution_attempt_id: SHT_SECE_R01_RUNTIME_INTEGRATION_ARCHITECTURE_R01_A1
project_time: omitted

## Human result
Accepted R03 is a reviewed offline development baseline, not an activated runtime.

Target flow:
authoritative project evidence -> semantic atoms -> EFFECTIVE_CONTEXT -> one bounded execution contract -> static validation -> fresh pre-effect revalidation -> one admitted EffectIntent -> separately authorized Effect Adapter -> evidenced EffectOutcome -> result/fixation/context delta/next-gate candidate.

SECE may admit/reject one proposed transition. It does not create the authority for that transition and does not perform the external effect.

## Exact basis
Authority commit 101f419f6b8538c401f7f30862da3c6aa8ba6206, blob daaa7bec250c42fee053d971462cf0fa14a2b8c7.
Fresh pre-start HEAD 65f700ea86065c515514d2cf48231106861356cb.
Task at that HEAD: entities/koordinator/outbox/SHT_SECE_runtime_integration_architecture_r01_prompt.md, blob 6857cd409df25a39f7956a8b1c5872d196b47fb9.
SHT writer blob a019c21cffeb99bb7c387b8fa95a4629137dc6da, CURRENT_WRITER.
Initial execution-state blob 4e05b714bcc187865c0a59e1f35cbda31bb8e0cd, INITIAL_NOT_STARTED_V1.

Accepted baseline commit 51b3654b1f5b802009b0e61d6c52df841420d306, tree 4080fb9195fac4ebdfcb144fe3bdab83323485b4, package identity 957824fb2e652893932e41cc7cdf1d07921587be013f96b417c57101ae92d9d3, MATCH.
Core blob e7b89c948c4e672c5b682408ce790670dfcdad5c.
SHD final review commit 5975738596712ba694fe565bc02d25feb6b02713, blob f1c11ee611010c8bd5aabdf95dc098a181e5213f, PASS.

PROCESSING_STARTED commit 50421aa74ecb328f50f52ef7b794d085adc3f728, blob 1994c3d64c96f28fdf8d92178c38fbe5d4a10347.
CHECKPOINT_DURABLE commit 9a22f500f3502f2fcb28de222a6222885efbed89, blob 07ea2e83f7dc63e24baf9d5f0d1a4f6bf770d125.

## Interfaces

### RuntimeInputEnvelope
Exact verified Entity/instance/role; active source refs; task/currentness/supersession; authority refs/scope/action classes; writer requirement/evidence; Recovery dependencies; immutable inputs; profile/capability/advisory experience; causal events/human input; UNKNOWN/conflicts; proposed action.

Semantic Bootstrap contributes semantic prerequisites/provenance only. Bootstrap PASS is not action authority.

### Reviewed deterministic core
SemanticAtomLoader -> ContextComposer/collision/correction -> EffectiveContextBuilder -> ExecutionContractProjector -> StaticValidator -> MultiOutcomeAggregator.

Output: one bounded contract and validator state for one proposed next step.

### EffectIntentCandidate
Contains action/contract/context IDs, scope, C1 binding, compiled-rule/source provenance, authority/task/currentness/writer/Recovery-sensitive dependencies, inputs, preconditions/STOP_IF, validation/aggregation and required evidence mode.

It is not an effect and not authority.

### EffectAdapter
Future separately authorized world-facing component only. It accepts an EffectIntent only after fresh pre-effect revalidation.

Output:
EVIDENCED_SUCCESS | EVIDENCED_FAILURE | UNRESOLVED | NOT_EXECUTED plus exact evidence refs.

### Downstream
ResultClassifier -> ContextDeltaBuilder -> SuccessorContextBuilder -> NextGateResolver -> HumanCausalRenderer/TraceRecorder -> fixation/handoff candidate.
NextGate candidate remains subject to Task Conveyor/coordination authority.

## Reusable reviewed baseline
Reusable as deterministic semantics/reference implementation:
canonicalization/digests/contract/trace identity; schema validation; SemanticAtomLoader; typed mutation semantics; ContextComposer; CollisionDetector; ContextCorrectionEngine; DependencyScopeResolver; EffectiveContextBuilder; ExecutionContractProjector; ActionAuthorizationValidator; CausalEventValidator; CurrentStateEvidenceResolver; StaticValidator; MultiOutcomeAggregator; ResultClassifier; ContextDeltaBuilder; SuccessorContextBuilder; NextGateResolver; HumanCausalRenderer; TraceRecorder concept.

Reuse does not mean activation.

Simulation-only:
FixtureLoader; FixtureOracle; fixture expected outcomes; Simulator orchestration; RuntimeStepGuardSimulator as effect simulator; synthetic fixture transformations as external-event source; test/anti-cheat harness; offline oracle state.

Future implementation requires new:
RuntimeInputAdapter; RuntimeEvidenceResolver; ContractCompilerFacade; PreEffectRevalidator; EffectIntentEmitter; EffectAdapter interface; EffectOutcomeRecorder; RuntimeResultFixator; RuntimeHumanExplanationAdapter.

## Runtime flow
R0 verified evidence + proposed action.
R1 verify source/task/currentness/authority/writer/Recovery/input identities.
R2 build EFFECTIVE_CONTEXT.
R3 project one contract.
R4 static validate and aggregate.
STOP/REJECT/BLOCKED/required UNKNOWN => no executable intent.
R5 fresh pre-effect revalidation.
R6 durable PRE_EFFECT_INTENT.
R7 separately authorized adapter only; otherwise NO_EFFECT.
R8 durable evidenced/unresolved outcome.
R9 result/context-delta/successor/next-gate.
R10 durable result/trace + human explanation.

## Effect-boundary revalidation
Before intent emission and again immediately before any external effect verify:
authority current/scope/action class; task CURRENT and not superseded; writer when required or explicit WRITER_NOT_REQUIRED_FOR_TASK; instance/Recovery/freeze/handoff consistency; active source provenance; immutable inputs; selected current-state basis; absence of unresolved overlapping prior effect; contract/context identity.

Any mismatch => NO_EFFECT.

UNKNOWN: NO_EFFECT, preserve missing evidence/scope.
BLOCKED: NO_EFFECT, preserve blockers.
STOP: NO_EFFECT in affected scope; independent scope only if proven independent and separately authorized.
REJECT: no effect for invalid proposal.
FAIL: only observed failure criterion, never missing evidence.
No prose/model layer may promote UNKNOWN/BLOCKED/STOP/REJECT to ADMIT.

## Durable evidence boundary
Applicable chain:
TASK/ATTEMPT -> accepted INITIAL_NOT_STARTED -> separate PROCESSING_STARTED -> scoped CHECKPOINT_DURABLE -> PRE_EFFECT_INTENT -> EFFECT_OUTCOME_EVIDENCED or EFFECT_OUTCOME_UNRESOLVED -> optional real RESULT_PENDING -> TERMINAL + independent NEXT_DISPOSITION.

Checkpoint proves exact prefix only. Crash tail UNKNOWN. Intent is not effect. UNRESOLVED blocks overlapping replay. No exactly-once or automatic replay. EFFECTIVE_CONTEXT may reference evidence but is not authoritative execution storage.

## Human explanation
One truth path:
RuntimeInputEnvelope -> EffectiveContext -> Contract -> predicates/aggregation -> revalidation/outcome -> Result/Delta/NextGate -> HumanCausalRenderer.

Explanation states what was checked, known/UNKNOWN, authority/currentness, allowed/forbidden action, whether effect was actually attempted, observed outcome evidence, significance and exact next gate. Renderer cannot add status absent from trace.

## System reconciliation
Semantic Bootstrap = upstream semantic seed/prerequisite, no action authority.
Semantic Dialogue Engine = representation/explanation/proposal, not effect authority.
PROJECT_OPERATIONS = orchestration surface binding verified project evidence to SECE and future authorized adapters.
SECE = deterministic membrane between proposal and effect.
Task Conveyor = external task/activation/next-task lifecycle owner.
Recovery/current-writer = external instance/state-write boundaries consumed as evidence, never replaced.

## Future gates
G1 independent review of this design.
G2 separate offline implementation authority for adapters/core packaging, no live effect.
G3 independent static/offline integration review.
G4 separate sandbox authority for exact adapter/effect class.
G5 independent sandbox evidence/review.
G6 separate OPERATOR live/production effect-class decision or exact bounded reusable authority.
G7 deployment/effectivity only after exact version/scope/rollback/monitoring evidence.

These are candidate gates, not successor authority.

## STOP before future effect
authority stale/missing/scope mismatch; task UNKNOWN/superseded/incompatible terminal; required writer mismatch/freeze/handoff conflict; Recovery/instance conflict; source/current-state conflict; immutable input mismatch; required evidence UNKNOWN; unresolved overlapping prior effect; adapter not separately authorized; external boundary undefined; contract/context mismatch; validator not ADMIT; pre-effect revalidation changed; required evidence carrier unavailable; action outside exact allowed set.

## Boundaries
runtime implementation NONE.
simulator activation/use NONE.
external system mutation NONE.
provider/model/API/Telegram calls NONE.
Project Source/canon mutation NONE.
role/recovery/current-writer mutation NONE.
production deployment/effects NONE.
historical replay NONE.
successor implementation authority NONE.

## Exact next causal gate
INDEPENDENT_BOUNDED_RUNTIME_INTEGRATION_ARCHITECTURE_REVIEW_REQUIRED_AFTER_KOO_RECONCILIATION_AND_SEPARATE_TASK_AUTHORITY.

Suitable reviewer class: independent technical/architecture reviewer; SHD may be selected only by separate KOO/OPERATOR authority.

## EXPERIENCE
Idea -> reuse the simulator as deterministic semantic evidence, not as a service.
Probe -> place an evidence adapter before the core and an authority-gated effect adapter after it, with fresh revalidation at the membrane.
Result -> semantic reasoning, authority/currentness and external effects have separate interfaces.
Success -> bounded runtime architecture is reviewable without runtime activation.
Lesson -> validator PASS is not permission to touch the world; the world-facing adapter must re-prove that this exact intent is still authorized now.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
