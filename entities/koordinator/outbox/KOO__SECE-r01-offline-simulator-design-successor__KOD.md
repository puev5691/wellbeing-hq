# KOO -> KOD: SECE r0.1 offline synthetic simulator/harness design successor

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Exact OPERATOR authority

AUTHORIZE_SECE_R01_OFFLINE_SYNTHETIC_SIMULATOR_DESIGN_SUCCESSOR = YES

Authority scope:
ONE NEW bounded OFFLINE synthetic simulator/harness DESIGN task only.

This is NOT authority for:
- replay/resume of the historical blocked simulator task;
- runtime implementation;
- live/provider/network work;
- Project Source/canon activation;
- role/recovery/current-writer mutation;
- host/storage mutation;
- credentials;
- production authority.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Historical blocked task — evidence only / DO NOT REPLAY

puev5691/wellbeing-hq@7745bcb6b36f30b631d2a6a4d6137eb91a2a7890:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-design-blocker__KOO.md

blob:
04bd88026a6155f299119457146d89802cd481cc

terminal:
BLOCKED_KOD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_OUTCOME_PRECEDENCE_UNSPECIFIED

classification:
HISTORICAL_COMPLETED_BLOCKER_RESULT
TASK_REPLAY=FORBIDDEN

The old task is not resumed.
This successor is a NEW task under NEW OPERATOR authority.

## Independently reviewed Effective Context PASS

puev5691/wellbeing-hq@7b77579c81f10b006417f8e6ee450ec396a20b04:
entities/shardovik/outbox/SHD__SECE-r01-effective-context-clarification-review__KOO.md

blob:
325dd7d9a6c5d0edd4270177703a7d257be2f56d

terminal:
PASS_SHD_SECE_R01_EFFECTIVE_CONTEXT_CLARIFICATION_REVIEW

Verified:
EFFECTIVE_CONTEXT_FORMALIZED=YES
CONTEXT_COMPOSITION_MACHINE_SPECIFIED=YES
COLLISION_CORRECTION_SCOPE_BOUNDED=YES
AFFECTED_SCOPE_RECOMPUTATION_DEFINED=YES
CONTEXT_DELTA_DEFINED=YES
CONTEXT_COMPOSITION_DISTINCT_FROM_L7_AGGREGATION=YES
MULTI_OUTCOME_AGGREGATION_PRESERVED_LOCAL_TO_L7=YES
EXECUTION_CONTRACT_DEFINED_AS_BOUNDED_CONTEXT_PROJECTION=YES
CLARIFICATION_CONTAINED=YES

Exact package:

puev5691/wellbeing-hq@8c3c22ff1bce80083030af2f7f160b1797800f45:
entities/shtabist/outbox/sece-r01-effective-context-clarification/

Key blobs:
EFFECTIVE-CONTEXT.md
90615ad4a7c78ef501530e9173814b6b2959f09f

CONTEXT-COMPOSITION.md
16f7c319b86a503512a94e3d0e60d6495a4020a9

COLLISION-CORRECTION.md
07429379c6d678551749ff5f1802cea0c45916ac

CONTEXT-DELTA.md
6807a61007a74f05edc5670bf129f4c02b4a9eb2

ARCHITECTURE.md
b0c9721d14d6261883d69998185e0e34a22402f7

EXECUTION-CONTRACT-SCHEMA.md
75a248ce0db2c3b821a13f8534ce6989f8d90285

CONTEXT-FIXTURES.md
320ed77112b831b373516c65fcf6c6d49c08b998

## Independently reviewed MULTI_OUTCOME_AGGREGATION PASS

puev5691/wellbeing-hq@49cd4669539068277f70886c41a2b65c024905f1:
entities/shardovik/outbox/SHD__SECE-r01-multi-outcome-aggregation-review__KOO.md

blob:
9d583178ebd5c58fd6c692bcfdef482d180ef18e

terminal:
PASS_SHD_SECE_R01_MULTI_OUTCOME_AGGREGATION_REVIEW

Verified:
OUTCOME_AGGREGATION_MODEL=MULTI_OUTCOME_AGGREGATION
SIMULTANEOUS_OUTCOMES_MACHINE_DECIDABLE=YES
TERMINAL_MAPPING_MACHINE_DECIDABLE=YES
NEXT_GATE_MAPPING_MACHINE_DECIDABLE=YES
CAUSAL_REASON_PRESERVATION=YES
AGGREGATION_CORRECTION_CONTAINED=YES

Exact package:

puev5691/wellbeing-hq@4a5dc3c7939967a4a2ee6c3af73abf815b1b06c5:
entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

Key blobs:
OUTCOME-AGGREGATION.md
7f8710eafd618a185159b79a8ceff0d55eaef635

AGGREGATION-RULES.md
3e53de74b3106f2f3b7fbe0061cf6592945ffb6d

EXECUTION-CONTRACT-SCHEMA.md
cb8bea18e6fc132f789eabcd933719a8a8a98da4

OUTCOME-FIXTURES.md
0ead740f96a014f25fdf3f3b811ba633c618bbc8

## Preserved SECE architecture

L1-L5 context composition
-> EFFECTIVE_CONTEXT
-> L6 bounded SEMANTIC_EXECUTION_CONTRACT projection for ONE next-step candidate
-> L7 validator + local MULTI_OUTCOME_AGGREGATION for ONE proposed transition
-> L8 ONE SAFE STEP
-> L9 RESULT/EVENT
-> CONTEXT_DELTA
-> successor EFFECTIVE_CONTEXT.

Context composition != validator outcome aggregation.

SECE_EXECUTION_CONTRACT_R01 is derived and not authority.

Profile / experience / capability may affect proposal/action-space but cannot create authority.

Task Conveyor / Recovery / current-writer remain authoritative external boundaries.

UNKNOWN remains non-promotable.

## Goal

Produce one immutable DESIGN candidate for an OFFLINE synthetic simulator/harness that models the reviewed SECE architecture without performing any real effect.

The design must cover BOTH:

A. dynamic context evolution;
B. one-transition validator/aggregation behavior.

No production/runtime implementation.

## Required simulator layers

Design interfaces/modules for at least:

1. FixtureLoader
2. RawContextLoader
3. SemanticAtomLoader
4. ContextComposer
5. CollisionDetector
6. ContextCorrectionEngine
7. DependencyScopeResolver
8. EffectiveContextBuilder
9. ExecutionContractProjector
10. ActionAuthorizationValidator
11. CausalEventValidator
12. CurrentStateEvidenceResolver
13. StaticValidator
14. MultiOutcomeAggregator
15. RuntimeStepGuardSimulator
16. ResultClassifier
17. ContextDeltaBuilder
18. SuccessorContextBuilder
19. NextGateResolver
20. HumanCausalRenderer
21. TraceRecorder
22. FixtureOracle

For each specify:
- input schema;
- output schema;
- deterministic behavior;
- UNKNOWN/conflict behavior;
- provenance propagation;
- side-effect boundary.

## Dynamic context model

Simulator design must represent:

RAW CONTEXT
-> semantic atoms
-> applicable rules/bindings
-> collision detection
-> scoped context corrections
-> EFFECTIVE_CONTEXT(n)
-> bounded L6 projection
-> validator
-> local L7 MULTI_OUTCOME_AGGREGATION
-> simulated one safe step only after ADMIT
-> RESULT/EVENT
-> CONTEXT_DELTA
-> EFFECTIVE_CONTEXT(n+1).

The simulator must not use winner-takes-all global context semantics.

Compatible parallel semantic lines must coexist.

## Required EFFECTIVE_CONTEXT support

Represent at minimum:
- context_id/version;
- entity/instance/role;
- active source set;
- semantic invariants;
- current-state evidence;
- selected current basis by exact scope;
- tasks/currentness;
- authority bindings;
- profile;
- experience;
- capabilities;
- causal events;
- human input;
- UNKNOWN facts;
- conflicts;
- corrections;
- derived bindings;
- provenance;
- scope index;
- dependency graph;
- prior context ref;
- context delta ref.

## Context recomputation

Design exact affected-scope recomputation:

verified Event/Result
-> changed atoms/evidence
-> affected scopes
-> dependency traversal
-> invalidated bindings
-> recomputed bindings
-> preserved unaffected bindings
-> new immutable context version.

No full reset unless an explicit fixture proves all scopes affected.

No stale dependent binding may survive changed dependency.

## CONTEXT_DELTA

Represent at minimum:
- delta_id;
- parent_context_id;
- triggering_event_or_result_ref;
- added_facts[];
- removed_or_superseded_facts[];
- refined_facts[];
- new_unknowns[];
- resolved_unknowns[];
- new_conflicts[];
- resolved_conflicts[];
- changed_scopes[];
- invalidated_bindings[];
- recomputed_bindings[];
- preserved_unaffected_bindings[];
- provenance[];
- resulting_context_id.

## Bounded L6 projection

Execution contract must reference:
- effective_context_id;
- effective_context_version;
- selected_scope;
- projection_basis[];
- context_dependency_refs[];
- projection_created_for_action_id.

Contract may not introduce context facts/bindings absent from EFFECTIVE_CONTEXT except ACTION_INTENT itself.

## C1/C2/C3 preserved

Design must retain:
- ACTION_AUTHORIZATION_BINDINGS[];
- CAUSAL_EVENTS[];
- CURRENT_STATE_EVIDENCE[].

Do not simplify them.

## L7 reviewed aggregation

Model MULTI_OUTCOME_AGGREGATION only for one proposed transition.

Represent:
- observed_predicates[];
- blocking_predicates[];
- conflict_predicates[];
- unknown_predicates[];
- rejected_action_predicates[];
- effect_decision;
- primary_outcome;
- secondary_reasons[];
- terminal_class;
- next_gate_class;
- aggregation_rule_id;
- provenance[].

All true causal reasons remain traceable.

Do not reuse L7 aggregation as global context composition.

## Closed machine outcomes

Use the reviewed architecture mapping for:
- conflict STOP;
- rejected/forbidden action;
- blocked authority/writer/currentness;
- required UNKNOWN;
- FAIL;
- clean ADMIT.

Do not invent new Project Source/canon precedence.

## Required fixture families

### T1-T15
Design machine-executable fixtures for all previously accepted validator/boundary cases.

### CXT1-CXT10
Design machine-executable dynamic context fixtures:

CXT1 MAY inspect + MUST_NOT mutate + UNKNOWN consumer coexist.
CXT2 experience suggests forbidden mutate.
CXT3 verified delta refines recovery scope S.
CXT4 terminal supersedes task T, unrelated U survives.
CXT5 new exact authority A recomputes only dependent bindings.
CXT6 source conflict S1 leaves S2 intact.
CXT7 verified evidence resolves UNKNOWN only in dependency closure.
CXT8 unauthorized human claim does not overwrite verified state.
CXT9 authorized OPERATOR decision creates bounded context delta.
CXT10 result changes next gate while role/profile/independent experience persist.

### O1-O10
Design machine-executable simultaneous outcome fixtures for reviewed L7 aggregation.

## Positive controls

At minimum:

P1 clean valid context/action => ADMIT.
P2 required handoff to another Entity => admitted handoff.
P3 verified delta refines recovery exact scope.
P4 recovery remains applicable outside refined scope.
P5 experience suggests allowed action but authority binding still required.
P6 new event changes one scope while byte/logically preserving unrelated scope.
P7 context projection uses only EFFECTIVE_CONTEXT facts plus ACTION_INTENT.

## Mutation/property tests

At minimum:

- remove authority_ref => authority-sensitive action rejects;
- ACTIVE source -> CANDIDATE => reject normative use;
- CURRENT task -> SUPERSEDED => dependent action rejects;
- processing_started YES -> UNKNOWN => no RUNNING inference;
- add current-state conflict => STOP;
- add source conflict only S1 => S2 preserved;
- change experience => no authority outcome change;
- change one dependency => only dependent bindings recompute;
- remove projection_basis fact => contract projection invalid;
- attempt to add context fact only in contract => reject projection;
- redundant KOO->KOO self-handoff => reject;
- simultaneous blockers retain all causal reasons.

## Trace requirements

Each run must trace at minimum:

fixture_id
input_context_id
input_context_version
changed_event/result if any
affected_scopes
invalidated_bindings
preserved_bindings
resulting_context_id
projection_scope
action_id
compiled_rule_id
source_provenance
authority_ref
task_binding
current_state_evidence_ids
causal_event_ids
validator predicates
aggregation_rule_id
primary_outcome
secondary_reasons
effect_decision
terminal_class
next_gate_class
expected_vs_actual.

## Determinism

Require:
- canonical fixture serialization;
- stable ordering;
- immutable context IDs derived deterministically from canonical content or equivalent deterministic identity strategy;
- no wall-clock dependency;
- no randomness;
- no network;
- no provider/model call required for deterministic core.

Any neural proposal must be optional injected input only.

## Implementation-neutral design

Do not implement runtime.

Specify:
- schemas;
- state transitions;
- module contracts;
- fixture format;
- oracle behavior;
- canonical trace format;
- deterministic identity strategy;
- no-side-effect sandbox boundary.

## Required output package

Create one immutable DESIGN package under:

entities/koder/outbox/sece-r01-offline-simulator-design-successor/

Include at minimum:

SIMULATOR-ARCHITECTURE.md
EFFECTIVE-CONTEXT-SCHEMA.md
CONTEXT-DELTA-SCHEMA.md
FIXTURE-SCHEMA.md or JSON schema
TRACE-SCHEMA.md or JSON schema
VALIDATOR-OUTCOMES.md
FIXTURES-T1-T15.md
FIXTURES-CXT1-CXT10.md
FIXTURES-O1-O10.md
POSITIVE-CONTROLS.md
PROPERTY-TESTS.md
IMPLEMENTATION-BOUNDARY.md
NEXT-GATES.md
MANIFEST.md

Status:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Stop conditions

STOP and return exact blocker if:
- either independent SHD PASS identity mismatches;
- newer superseding SECE architecture/review appears;
- KOD writer conflict appears;
- design requires inventing a Project Source/canon norm;
- any required fixture cannot be made machine-decidable from reviewed architecture.

## Expected terminal

PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/blobs;
- module/interface summary;
- context evolution design;
- L6 projection design;
- L7 aggregation design;
- T1-T15 summary;
- CXT1-CXT10 summary;
- O1-O10 summary;
- positive controls;
- property tests;
- determinism strategy;
- DESIGN_BLOCKER items if any;
- status SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- exact next gate:
  independent bounded simulator-design review only.

Then STOP.
