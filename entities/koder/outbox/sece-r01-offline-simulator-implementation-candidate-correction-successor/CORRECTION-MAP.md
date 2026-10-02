# SHD static defects C1-C8 correction map

status: PASS

## C1 JSON Schema minimum

Code:
ClosedSchemaValidator.validate

Correction:
implements numeric minimum.

Direct test:
schema_minimum_tests.py

Evidence:
below reviewed minimum rejected;
exact minimum accepted.

REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED=YES

## C2 ContextCorrectionEngine fidelity

Code:
ContextCorrectionEngine.correct

Correction:
- consumes typed collisions;
- emits explicit correction objects;
- exact-scope verified refinement;
- preserves unrelated scope;
- preserves unresolved conflict/UNKNOWN explicitly;
- emits changed_scopes/invalidation_seeds;
- prior input remains immutable;
- EffectiveContextBuilder consumes corrections.

Direct tests:
correction_tests.py c2_*

CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED=YES

## C3 EffectiveContextBuilder fidelity

Code:
EffectiveContextBuilder

Implemented reviewed structure includes:
context_id/version,
entity/instance/role,
active_source_set,
semantic_invariants,
current_state_evidence,
selected_current_basis_by_scope,
current_tasks,
authority_bindings,
profile,
experience_set,
capability_set,
causal_events,
human_input_facts,
unknown_facts,
conflict_set,
context_corrections,
derived_bindings,
provenance,
scope_index,
dependency_graph,
prior_context_ref,
context_delta_ref.

Identity binds complete canonical emitted context without context_id.

Field presence does not create authority.

EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED=YES

## C4 C1 L6 projection boundary

Code:
EffectiveContextBuilder._authority_bindings
ExecutionContractProjector.project
ActionAuthorizationValidator.evaluate

Final C1 decision consumes projected ACTION_AUTHORIZATION_BINDINGS only.

Direct tests:
valid, missing, stale, conflicted and raw-fact-bypass cases.

C1_L6_PROJECTION_BOUNDARY_FIXED=YES

## C5 L6 projection firewall

Code:
ExecutionContractProjector._item_index
ExecutionContractProjector.project

Enforced:
- basis IDs must exist in EFFECTIVE_CONTEXT;
- dependency IDs must exist in dependency graph;
- invented context item rejected;
- ACTION_INTENT is only extra semantic input;
- invalid projection marked before L7.

Direct tests mutate projection source data directly.

L6_PROJECTION_FIREWALL_ENFORCED=YES

## C6 ResultClassifier fidelity

Code:
ResultClassifier.classify

Inputs:
synthetic observation,
contract EXPECTED_RESULT,
contract EXPECTED_TERMINAL.

Direct tests:
PASS, verified mismatch FAIL, missing UNKNOWN, unverified UNKNOWN.

RESULT_CLASSIFIER_FIDELITY_FIXED=YES

## C7 NextGateResolver grounding

Code:
NextGateResolver.resolve

Requires:
aggregation class,
verified event/result,
ACTIVE CURRENT exact NEXT_GATE_RULE,
matching current verified evidence when required.

No exact rule:
no route candidate.

Historical/superseded rule:
no route.

Terminal alone:
no route.

NEXT_GATE_RESOLVER_GROUNDING_FIXED=YES

## C8 strengthened architecture assertions

architecture_tests.py directly proves A1-A13.

ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13

## Regression containment

Reviewed fixture meanings:
unchanged.

D2 contract identity semantics:
unchanged.

D3 trace identity semantics:
unchanged.

Generic binding derivation:
unchanged.

Anti-cheat/determinism/no-side-effect boundaries:
preserved.
