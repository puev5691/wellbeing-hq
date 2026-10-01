# SECE r0.1 OFFLINE synthetic simulator/harness — successor design

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
design_scope: OFFLINE_DETERMINISTIC_DESIGN_ONLY
project_time: omitted

## 1. Purpose

Design one deterministic, side-effect-free synthetic harness for the independently reviewed SECE r0.1 architecture.

The harness models two distinct machines:

A. **Dynamic context evolution**
RAW CONTEXT -> semantic atoms/bindings -> collision detection -> scoped correction -> EFFECTIVE_CONTEXT(n) -> verified RESULT/EVENT -> CONTEXT_DELTA -> EFFECTIVE_CONTEXT(n+1).

B. **One-transition execution decision**
EFFECTIVE_CONTEXT(n) -> bounded L6 projection for one ACTION_INTENT -> L7 predicate collection -> local MULTI_OUTCOME_AGGREGATION -> simulated ONE SAFE STEP only after ADMIT -> synthetic RESULT/EVENT.

These machines are connected through:
- L6 projection from EFFECTIVE_CONTEXT into one execution contract;
- verified L9 RESULT/EVENT into CONTEXT_DELTA.

They are not merged. L7 aggregation is never a global context-composition rule.

## 2. Exact reviewed architecture basis

Effective Context independent PASS:
puev5691/wellbeing-hq@7b77579c81f10b006417f8e6ee450ec396a20b04:
entities/shardovik/outbox/SHD__SECE-r01-effective-context-clarification-review__KOO.md
blob 325dd7d9a6c5d0edd4270177703a7d257be2f56d

Effective Context package:
puev5691/wellbeing-hq@8c3c22ff1bce80083030af2f7f160b1797800f45:
entities/shtabist/outbox/sece-r01-effective-context-clarification/

MULTI_OUTCOME_AGGREGATION independent PASS:
puev5691/wellbeing-hq@49cd4669539068277f70886c41a2b65c024905f1:
entities/shardovik/outbox/SHD__SECE-r01-multi-outcome-aggregation-review__KOO.md
blob 9d583178ebd5c58fd6c692bcfdef482d180ef18e

Aggregation package:
puev5691/wellbeing-hq@4a5dc3c7939967a4a2ee6c3af73abf815b1b06c5:
entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

C1/C2/C3 remain preserved from the corrected SECE architecture.

## 3. Global deterministic flow

1. FixtureLoader loads and canonicalizes one fixture.
2. RawContextLoader materializes fixture-declared raw context only.
3. SemanticAtomLoader converts declared raw facts/evidence into typed atoms while preserving provenance.
4. ContextComposer retains compatible semantic lines in parallel.
5. CollisionDetector detects typed collisions only for overlapping scopes/conditions.
6. ContextCorrectionEngine applies reviewed exact-scope corrections; it never rewrites prior immutable context.
7. EffectiveContextBuilder emits immutable EFFECTIVE_CONTEXT(n).
8. ExecutionContractProjector selects one exact scope and one ACTION_INTENT and projects only facts/bindings already present in EFFECTIVE_CONTEXT.
9. C1/C2/C3 validators plus StaticValidator emit the complete simultaneous predicate set.
10. MultiOutcomeAggregator applies reviewed AGG-R1..AGG-R6 locally to that one predicate set.
11. RuntimeStepGuardSimulator revalidates the same bounded dependencies. Only effect_decision=ADMIT permits a synthetic ACTION_EVENT record.
12. ResultClassifier classifies injected synthetic observed result as PASS/FAIL/UNKNOWN without any real effect.
13. ContextDeltaBuilder accepts only fixture-declared verified RESULT/EVENT and computes exact changed scopes/dependencies.
14. SuccessorContextBuilder recomputes invalidated bindings only, preserves unaffected bindings by identity/reference, and emits EFFECTIVE_CONTEXT(n+1).
15. NextGateResolver resolves only reviewed next_gate_class and exact active next-gate evidence when supplied.
16. HumanCausalRenderer renders prose from machine state.
17. TraceRecorder emits canonical trace.
18. FixtureOracle compares expected and actual canonical machine outputs.

## 4. Deterministic identity strategy

Canonical serialization:
- UTF-8 JSON;
- object keys lexicographically sorted;
- set-like arrays sorted by declared stable key;
- ordered semantic sequences preserve schema-defined order only;
- no timestamps, wall-clock values, random IDs, UUID generation or process-dependent values.

Identity domains:
- fixture_id is fixture-declared immutable identifier;
- context_id = SHA-256("sece-effective-context-r01\0" + canonical context payload excluding context_id);
- delta_id = SHA-256("sece-context-delta-r01\0" + canonical delta payload excluding delta_id/resulting_context_id);
- contract_id = SHA-256("sece-execution-contract-r01\0" + effective_context_id + "\0" + selected_scope + "\0" + action_id + "\0" + canonical projection_basis);
- trace_id = SHA-256("sece-simulator-trace-r01\0" + canonical trace payload excluding trace_id).

The design defines identity construction only. It does not implement hashing/runtime code.

## 5. Module/interface contracts

### 5.1 FixtureLoader
Input:
- fixture document matching FIXTURE-SCHEMA;
- schema identifier/version.

Output:
- CanonicalFixture;
- fixture_id;
- canonical_fixture_digest candidate.

Determinism:
schema validation + canonical ordering only.

UNKNOWN/conflict:
schema omission of required field => fixture invalid, not inferred.
Contradictory expected oracle fields => fixture invalid.

Provenance:
preserves fixture source locator/fixture evidence refs.

Side effects:
none; no network/filesystem discovery.

### 5.2 RawContextLoader
Input:
- CanonicalFixture.raw_context;
- fixture-declared source/evidence objects.

Output:
- RawContext with only declared facts/evidence.

Determinism:
exact copy/projection; no memory or hidden environment.

UNKNOWN/conflict:
missing required raw input remains UNKNOWN_REQUIRED_EVIDENCE where fixture says required; otherwise absent.

Provenance:
every raw item carries source/evidence ref.

Side effects:
none.

### 5.3 SemanticAtomLoader
Input:
- RawContext;
- fixture-declared compiled semantic rule mappings.

Output:
- typed SemanticAtom[] with atom_id, scope, semantic_type, applicability, epistemic_state, lifecycle_state, authority_effect_state, dependencies, provenance.

Determinism:
only declared rule/atom mappings; no neural interpretation in deterministic core.

UNKNOWN/conflict:
unsupported mapping => fixture/design validation error; no guessed atom.

Provenance:
source locator/version/blob and semantic basis retained.

Side effects:
none.

### 5.4 ContextComposer
Input:
- applicable SemanticAtom[];
- existing bindings/profile/experience/capability/human-input lines.

Output:
- ComposedContextCandidate containing all compatible lines.

Determinism:
conjunctive/compositional; independent scopes coexist.

UNKNOWN/conflict:
UNKNOWN remains present; difference across independent scopes is not conflict.

Provenance:
union without loss.

Side effects:
none.

### 5.5 CollisionDetector
Input:
- ComposedContextCandidate;
- normalized scope index.

Output:
- Collision[] using reviewed classes:
DIRECT_NORM_CONFLICT, SCOPE_OVERLAP_CONFLICT, AUTHORITY_CONFLICT,
CURRENT_STATE_CONFLICT, SOURCE_STATUS_CONFLICT, TASK_CURRENTNESS_CONFLICT,
EVIDENCE_CONFLICT, PROFILE_CONSTRAINT_CONFLICT,
EXPERIENCE_CONFLICT_WITH_RULE, HUMAN_INPUT_CONFLICT_WITH_VERIFIED_EVIDENCE,
UNKNOWN_REQUIRED_EVIDENCE, SUPERSESSION_REFINEMENT.

Determinism:
only overlapping exact scopes/conditions are compared.

UNKNOWN/conflict:
insufficient required evidence produces UNKNOWN_REQUIRED_EVIDENCE, not invented resolution.

Provenance:
collision records reference all input atom/binding IDs and evidence refs.

Side effects:
none.

### 5.6 ContextCorrectionEngine
Input:
- ComposedContextCandidate;
- Collision[];
- reviewed correction rules.

Output:
- ContextCorrection[];
- retained facts;
- invalidation seeds;
- unresolved conflicts/unknowns.

Determinism:
applies only reviewed exact-scope transformations.

UNKNOWN/conflict:
unresolved conflict stays conflict and blocks dependent effect only in affected scope;
UNKNOWN remains uncertainty + evidence requirement.

Provenance:
each correction records collision_id, affected scope, affected IDs, transformation, retained facts, provenance.

Side effects:
none; prior context immutable.

### 5.7 DependencyScopeResolver
Input:
- changed atom/evidence IDs;
- scope_index;
- dependency_graph.

Output:
- affected_scopes[];
- invalidated_bindings[];
- preserved_unaffected_bindings[].

Determinism:
graph traversal from exact changed dependencies; stable ID ordering.

UNKNOWN/conflict:
unknown dependency edge for a required binding => binding invalidated/UNKNOWN, never preserved by assumption.

Provenance:
records dependency edge IDs used.

Side effects:
none.

### 5.8 EffectiveContextBuilder
Input:
- corrected facts;
- selected current basis by scope;
- context corrections;
- recomputed bindings;
- preserved unaffected bindings;
- prior_context_ref/context_delta_ref.

Output:
- immutable EFFECTIVE_CONTEXT.

Determinism:
canonical serialization/identity rules.

UNKNOWN/conflict:
unknowns/conflicts retained as first-class fields; field presence creates no authority.

Provenance:
complete per fact/binding plus context-level provenance.

Side effects:
none.

### 5.9 ExecutionContractProjector
Input:
- EFFECTIVE_CONTEXT;
- selected_scope;
- ACTION_INTENT/action_id.

Output:
- bounded SECE_EXECUTION_CONTRACT_R01 projection including:
effective_context_id/version, selected_scope, projection_basis[],
context_dependency_refs[], projection_created_for_action_id,
plus preserved C1/C2/C3 and validator fields applicable to that scope/action.

Determinism:
projection is subset/reference operation plus ACTION_INTENT.

UNKNOWN/conflict:
missing projection basis => projection invalid;
attempt to introduce absent context fact/binding => projection invalid.

Provenance:
every projected fact/binding references context ID and source provenance.

Side effects:
none; contract is not authority.

### 5.10 ActionAuthorizationValidator
Input:
- ACTION_INTENT;
- ACTION_AUTHORIZATION_BINDINGS[];
- compiled-rule/source/task/writer/effect requirements.

Output:
- observed predicate records including ADMIT candidate,
REJECT_ACTION_AUTHORIZATION_BINDING, BLOCKED_AUTHORITY, BLOCKED_WRITER,
BLOCKED_CURRENTNESS as applicable.

Determinism:
exact binding predicate from reviewed C1.

UNKNOWN/conflict:
unknown/stale/conflicted provenance cannot satisfy binding.

Provenance:
binding ID, compiled_rule_id, source locator/blob, authority_ref, task_binding.

Side effects:
none.

### 5.11 CausalEventValidator
Input:
- CAUSAL_EVENTS[];
- proposed causal transition/handoff.

Output:
- lifecycle/causal predicates including REJECT_REDUNDANT_SELF_HANDOFF and processing-start inference rejection.

Determinism:
dispatch/receipt/activation distinctions and reviewed C2 predicate.

UNKNOWN/conflict:
UNKNOWN causal requirement is not promoted to REQUIRED.

Provenance:
event IDs/evidence refs retained.

Side effects:
none.

### 5.12 CurrentStateEvidenceResolver
Input:
- CURRENT_STATE_EVIDENCE[];
- selected_scope.

Output:
- selected basis by scope;
- predicates CURRENT_STATE_CONFLICT_STOP, UNKNOWN_REQUIRED_EVIDENCE, BLOCKED_CURRENTNESS as applicable.

Determinism:
exact-scope evidence relations only; no filename/recency convention.

UNKNOWN/conflict:
applicable unresolved_conflict => STOP predicate;
no selected required basis => UNKNOWN predicate.

Provenance:
all candidate/selected evidence IDs and relation edges retained.

Side effects:
none.

### 5.13 StaticValidator
Input:
- projected contract;
- outputs of C1/C2/C3 validators;
- ALLOWED_ACTIONS/FORBIDDEN_ACTIONS/REQUIRED_PRECONDITIONS/STOP_IF;
- expected input identities.

Output:
- complete simultaneous ValidatorPredicateSet:
observed, blocking, conflict, unknown, rejected-action and fail predicates.

Determinism:
evaluates all applicable predicates; never first-match returns.

UNKNOWN/conflict:
retained as predicates for L7 aggregation.

Provenance:
predicate_id -> rule/evidence/source refs.

Side effects:
none.

### 5.14 MultiOutcomeAggregator
Input:
- complete ValidatorPredicateSet for one proposed transition.

Output:
VALIDATOR_OUTCOME_AGGREGATION with reviewed fields:
observed_predicates[], blocking_predicates[], conflict_predicates[],
unknown_predicates[], rejected_action_predicates[], effect_decision,
primary_outcome, secondary_reasons[], terminal_class, next_gate_class,
aggregation_rule_id, provenance[].

Determinism:
exact reviewed AGG-R1..AGG-R6; AGG-R7 boundary.

UNKNOWN/conflict:
conflict -> AGG-R1; reject -> AGG-R2; blocker -> AGG-R3;
unknown -> AGG-R4; fail -> AGG-R5; otherwise clean admit -> AGG-R6.
All simultaneous reasons retained.

Provenance:
aggregation rule + every predicate/evidence ref.

Side effects:
none. Local L7 only; never global context composition.

### 5.15 RuntimeStepGuardSimulator
Input:
- effect_decision;
- projected contract;
- exact dependencies/bindings selected at L7.

Output:
- if ADMIT: SyntheticActionEventIntent;
- otherwise: NoEffect record.

Determinism:
revalidates fixture-supplied same bounded predicates/dependencies before synthetic step.

UNKNOWN/conflict:
any newly injected blocker/conflict/unknown causes no synthetic action event and requires re-aggregation trace.

Provenance:
contract_id + revalidated refs.

Side effects:
strictly no real effect; no host/network/storage/provider/credential call.

### 5.16 ResultClassifier
Input:
- injected synthetic observation/result;
- EXPECTED_RESULT/EXPECTED_TERMINAL from contract.

Output:
- result_class: PASS|FAIL|UNKNOWN;
- observed result facts;
- causal event/result record candidate.

Determinism:
exact fixture comparison only.

UNKNOWN/conflict:
missing required observation => UNKNOWN, never guessed PASS/FAIL.

Provenance:
synthetic observation ref and contract expectation refs.

Side effects:
none.

### 5.17 ContextDeltaBuilder
Input:
- EFFECTIVE_CONTEXT(n);
- verified synthetic RESULT/EVENT;
- dependency graph/scope index.

Output:
- CONTEXT_DELTA exact schema.

Determinism:
changed facts -> exact scopes -> dependency closure -> invalidated/recomputed/preserved lists.

UNKNOWN/conflict:
unverified synthetic result cannot mutate successor context; it may be traced but delta is not applicable.

Provenance:
triggering result/event + affected facts/dependencies.

Side effects:
none.

### 5.18 SuccessorContextBuilder
Input:
- parent EFFECTIVE_CONTEXT;
- verified CONTEXT_DELTA;
- recomputed affected bindings;
- preserved unaffected bindings.

Output:
- immutable EFFECTIVE_CONTEXT(n+1).

Determinism:
no full reset unless dependency closure explicitly spans all scopes.

UNKNOWN/conflict:
no stale dependent binding may survive;
unaffected bindings preserved byte/logically by identity/reference.

Provenance:
prior_context_ref + context_delta_ref + per-field provenance.

Side effects:
none.

### 5.19 NextGateResolver
Input:
- aggregation next_gate_class;
- verified RESULT/EVENT;
- active NEXT_GATE_RULE[];
- current verified Task Conveyor/state evidence supplied by fixture.

Output:
- next_gate_class;
- exact next-gate candidate only if grounded.

Determinism:
no routing from terminal alone/list order/historical queue.

UNKNOWN/conflict:
absent exact gate evidence => NONE/STOP/UNKNOWN as reviewed fixture requires; never invent recipient/task.

Provenance:
active rule IDs + state/evidence refs.

Side effects:
none.

### 5.20 HumanCausalRenderer
Input:
- effective context;
- contract;
- aggregation;
- result;
- delta/next gate.

Output:
- human causal narrative:
checked -> known/UNKNOWN -> authority -> allowed/forbidden -> observed -> significance -> next action.

Determinism:
template projection from machine state.

UNKNOWN/conflict:
renders them explicitly; does not resolve them.

Provenance:
optional visible source/evidence refs.

Side effects:
none; prose never feeds validator state.

### 5.21 TraceRecorder
Input:
- all stage outputs and IDs.

Output:
- canonical TRACE-SCHEMA object.

Determinism:
stable ordering and canonical serialization.

UNKNOWN/conflict:
records, never resolves.

Provenance:
retains all causal/evidence references.

Side effects:
in design, trace is returned data only; no filesystem/network sink implied.

### 5.22 FixtureOracle
Input:
- CanonicalFixture.expected;
- canonical actual context/contract/predicate/aggregation/result/delta/trace.

Output:
- ORACLE_PASS|ORACLE_FAIL;
- exact field/path mismatches.

Determinism:
strict canonical comparison with schema-declared ignored fields = none unless fixture explicitly marks non-applicable.

UNKNOWN/conflict:
expected UNKNOWN/conflict must match exactly; it is not treated as wildcard.

Provenance:
fixture_id + expected architecture rule refs.

Side effects:
none.

## 6. One-safe-step state machine

PRE_STATE
-> ACTION_INTENT
-> exact ACTION_AUTHORIZATION_BINDING / rule / source / authority / task binding
-> REQUIRED_PRECONDITIONS
-> complete validator predicate set
-> MULTI_OUTCOME_AGGREGATION
-> if effect_decision != ADMIT: no synthetic ACTION_EVENT
-> if ADMIT: RuntimeStepGuardSimulator revalidates
-> Synthetic ACTION_EVENT only
-> injected synthetic RESULT
-> ResultClassifier
-> verified RESULT/EVENT candidate
-> ContextDeltaBuilder
-> SuccessorContextBuilder
-> next-gate candidate.

No real effect exists anywhere in this design.

## 7. Determinism / neural boundary

Deterministic core requires no model.

A future neural proposal may only be fixture-injected data such as:
neural_proposal = {action_id, proposed_atoms[], provenance:"INJECTED_SYNTHETIC"}

It receives no authority status from being neural. The deterministic core validates it identically to any other ACTION_INTENT.

## 8. Design blocker result

DESIGN_BLOCKER items:
NONE

All required T1-T15, CXT1-CXT10 and O1-O10 are machine-decidable from reviewed architecture evidence.

terminal:
PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW
