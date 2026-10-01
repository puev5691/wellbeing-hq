# KOO -> KOD: SECE r0.1 offline synthetic simulator/harness design

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Exact authority

OPERATOR decision in current KOO chat:

AUTHORIZE_SECE_R01_OFFLINE_SYNTHETIC_SIMULATOR_DESIGN = YES

This authority permits DESIGN ONLY for a bounded OFFLINE synthetic SECE simulator/harness.

It does NOT authorize:
- runtime implementation;
- production simulator;
- source/canon activation;
- Entity role mutation;
- recovery/current-writer mutation;
- historical task replay;
- provider/Telegram calls;
- host/storage mutation;
- credential work;
- production/live authority.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact architecture readiness PASS

puev5691/wellbeing-hq@5fc0f41e7603edaa1fa6acb7671b5344099ff36f:
entities/shardovik/outbox/SHD__semantic-entity-control-engine-r01-C1C2C3-rereview__KOO.md

blob:
a934bde88e9ebcc4098d284314d26d401a4fde96

terminal:
PASS_SHD_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_C1C2C3_REREVIEW

Verified:
C1_ACTION_BINDING_CLOSED=YES
C2_CAUSAL_HANDOFF_STATE_CLOSED=YES
C3_CURRENT_STATE_EVIDENCE_CLOSED=YES
CORRECTION_CONTAINED=YES
SIMULATOR_DESIGN_READINESS=YES

## Exact corrected architecture package

puev5691/wellbeing-hq@b768ed1c85fcca8cc79e375613961119b873b81f:
entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-correction-r01/

Key blobs:
ARCHITECTURE.md a536445c3807981ef890e6915a8b7d68c32c43b1
EXECUTION-CONTRACT-SCHEMA.md be67d382778c5ca096f2f1e6f05713516f977cfd
SOURCE-RULE-MAPPING.md 2f218b32eafb01ed39d67396832c600f598b7eff
SEMANTIC-ATOMS.md 80109fc973b2584d2b9de56b7f49de2600f142a2
ADVERSARIAL-FIXTURES.md b6bf41061beca9b3d5101dfab44eb495ae7669b8

## Goal

Produce one immutable DESIGN candidate for an OFFLINE synthetic simulator/harness that can deterministically exercise SECE r0.1 contract/validator semantics.

No production/runtime code.

## Required design

Define interfaces/modules for:

1. FixtureLoader
2. ContractAssembler
3. ActionAuthorizationValidator
4. CausalEventValidator
5. CurrentStateEvidenceResolver
6. StaticValidator
7. RuntimeStepGuardSimulator
8. ResultClassifier
9. NextGateResolver
10. HumanCausalRenderer
11. TraceRecorder
12. FixtureOracle

For each specify:
- inputs;
- outputs;
- deterministic behavior;
- UNKNOWN/conflict behavior;
- provenance;
- side-effect boundary.

## Preserve corrected contract structures

Simulator design must explicitly model:

ACTION_AUTHORIZATION_BINDINGS[]
CAUSAL_EVENTS[]
CURRENT_STATE_EVIDENCE[]

and existing SECE_EXECUTION_CONTRACT_R01 fields.

Do not simplify away C1/C2/C3.

## Closed outcomes

Define a closed machine outcome set including at least:

ADMIT
REJECT_ACTION_AUTHORIZATION_BINDING
REJECT_FORBIDDEN
REJECT_PRECONDITION
REJECT_REDUNDANT_SELF_HANDOFF
SOURCE_CONFLICT_STOP
CURRENT_STATE_CONFLICT_STOP
UNKNOWN_REQUIRED_EVIDENCE
BLOCKED_AUTHORITY
BLOCKED_WRITER
BLOCKED_CURRENTNESS
PASS
FAIL
UNKNOWN

If precedence among simultaneous outcomes is not already established by architecture, mark DESIGN_BLOCKER instead of inventing a norm.

## One-safe-step simulation

Represent:

PRE_STATE
-> ACTION_INTENT
-> exact action/rule/source/authority/task binding
-> preconditions
-> validator decision
-> simulated ACTION_EVENT only after ADMIT
-> result classification
-> next-gate candidate

No real effect occurs.

## Trace requirements

Each deterministic trace must include:

fixture_id
contract_version
action_id
compiled_rule_id
source_provenance
authority_ref
task_binding
current_state_evidence_ids
causal_event_ids
evaluated_predicates
outcome
rejected_predicate if any
expected_vs_actual

Canonical trace output must support regression comparison.

## T1-T15

Design machine-executable synthetic fixture definitions for all accepted T1-T15:

T1 writer yes / task authority absent
T2 task yes / required writer absent
T3 historical UNKNOWN after replacement
T4 dispatch without processing_started
T5 stale task + newer terminal/supersession
T6 recovery older than verified delta exact scope
T7 experience recommends forbidden action
T8 profile capability outside task
T9 useful extra action outside ALLOWED
T10 required UNKNOWN
T11 active-source conflict
T12 automation capability without authority
T13 replacement writer established, old task still UNKNOWN
T14 candidate source not active
T15 current OPERATOR decision already at KOO; redundant KOO->KOO handoff rejected

For each specify:
- synthetic inputs;
- expected contract state;
- proposed bad transition;
- exact validator predicate;
- expected outcome/terminal/next-gate class;
- architecture rule mapping.

## Positive controls

Design at least:

P1 valid current task + writer + authority + active source + matching action => ADMIT

P2 causally required handoff to another Entity => admitted handoff

P3 verified delta refines recovery exact scope, no conflict => delta selected

P4 recovery remains applicable outside refined scope

P5 experience recommends an allowed action, but admission still requires authority binding

## Mutation/property tests

Design tests proving:

- remove authority_ref from valid fixture => reject;
- ACTIVE source -> CANDIDATE => reject authority-sensitive action;
- CURRENT task -> SUPERSEDED => reject effect;
- processing_started YES -> UNKNOWN => no RUNNING inference;
- add CURRENT_STATE_EVIDENCE conflict => STOP;
- change causally required other-Entity handoff to redundant KOO->KOO => reject;
- add useful unbound action => does not expand ALLOWED;
- modify experience => does not change authority result.

## Determinism

Require:

- canonical fixture serialization;
- stable ordering;
- no wall-clock dependency;
- no randomness;
- no network;
- no model call for deterministic validator core.

Any later neural proposal simulation must be injected input only.

## Output package

Create one immutable DESIGN package under:

entities/koder/outbox/sece-r01-offline-simulator-design/

Include at minimum:

SIMULATOR-ARCHITECTURE.md
FIXTURE-SCHEMA.md or JSON
TRACE-SCHEMA.md or JSON
VALIDATOR-OUTCOMES.md
FIXTURES-T1-T15.md
POSITIVE-CONTROLS.md
PROPERTY-TESTS.md
IMPLEMENTATION-BOUNDARY.md
NEXT-GATES.md
MANIFEST.md

status:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Stop conditions

STOP and return exact blocker if:
- architecture/package identity mismatch;
- newer superseding SECE design/review appears;
- KOD writer conflict;
- required simulator semantics are under-specified such that design would invent project norms.

## Expected terminal

PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/blobs;
- module/interface summary;
- outcome model;
- T1-T15 summary;
- P1-P5 summary;
- property-test summary;
- determinism strategy;
- DESIGN_BLOCKER items if any;
- status SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- exact next gate:
  independent bounded simulator-design review only.

Then STOP.
