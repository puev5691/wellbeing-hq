# KOO -> KOD: SECE r0.1 OFFLINE simulator implementation candidate

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Exact OPERATOR authority

AUTHORIZE_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE = YES

Authority scope:
ONE NEW bounded OFFLINE simulator implementation-candidate task only.

This authority does NOT authorize:
- production/runtime activation;
- live SECE deployment;
- provider/model/API calls;
- Telegram;
- network dependence;
- host/service mutation;
- credentials;
- Project Source/canon activation;
- Entity role/recovery/current-writer mutation;
- historical task replay;
- production/live authority.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact independent implementation-design readiness PASS

puev5691/wellbeing-hq@89f5c103de4526771e6dd71674ade0f3aeae5151:
entities/shardovik/outbox/SHD__SECE-r01-simulator-design-D1D2D3-rereview__KOO.md

blob:
68c7eed500bb00fae8c25b5c153de390687ed7f0

terminal:
PASS_SHD_SECE_R01_SIMULATOR_DESIGN_D1D2D3_REREVIEW

Verified:

D1_FIXTURE_SCHEMA_CLOSED=YES
FIXTURE_CATALOG_VALIDATES_54_OF_54=YES
FIXTURE_MEANINGS_UNCHANGED=YES

D2_CONTRACT_ID_FULL_PAYLOAD_BOUND=YES
CONTRACT_ID_COLLISION_BY_OMITTED_SEMANTIC_FIELD_PREVENTED=YES

D3_TRACE_SCHEMA_CLOSED=YES
TRACE_CAUSAL_PATH_RECONSTRUCTABLE=YES

DETERMINISM_BOUNDARY_PRESERVED=YES
NO_SIDE_EFFECT_BOUNDARY_PRESERVED=YES
D1D2D3_CORRECTION_CONTAINED=YES

OFFLINE_IMPLEMENTATION_DESIGN_READINESS=YES

DESIGN_STATUS:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Exact reviewed design basis

Base simulator design package:

puev5691/wellbeing-hq@5b9642fe5915386518ea0d3a7d9f2b9ee6376469:
entities/koder/outbox/sece-r01-offline-simulator-design-successor/

tree:
6f3056ac669377c4dc0211d34da7d321ea75836c

Correction package:

puev5691/wellbeing-hq@9e1d66efc798041d2217c5e9a195fc795d84aad9:
entities/koder/outbox/sece-r01-offline-simulator-design-successor-d1d2d3-correction/

tree:
66686bac2a742a4673ec7da9eb2b7b57a74c7721

Corrected key blobs:

FIXTURE-SCHEMA.json
7d221176ebd694d67321261c5466f6df1090bf8f

FIXTURE-CATALOG.json
4ce7939519ecdfa24e4102742be519fa5d5f2259

TRACE-SCHEMA.json
0876cff31d1e4b54b065933aa74129e591c78e94

IDENTITY-SPEC.md
7339655c132459f87a1943f4f825d45b497108e3

CONTRACT-ID-TEST-VECTORS.json
8758546a2a1bf62defd4e7b32d5ab3357abba8e2

TRACE-ID-TEST-VECTORS.json
00eb5487c611ae9e3e1db6c4a00100c419c9a650

## Independently reviewed architecture basis

Effective Context PASS:

puev5691/wellbeing-hq@7b77579c81f10b006417f8e6ee450ec396a20b04:
entities/shardovik/outbox/SHD__SECE-r01-effective-context-clarification-review__KOO.md

blob:
325dd7d9a6c5d0edd4270177703a7d257be2f56d

terminal:
PASS_SHD_SECE_R01_EFFECTIVE_CONTEXT_CLARIFICATION_REVIEW

MULTI_OUTCOME_AGGREGATION PASS:

puev5691/wellbeing-hq@49cd4669539068277f70886c41a2b65c024905f1:
entities/shardovik/outbox/SHD__SECE-r01-multi-outcome-aggregation-review__KOO.md

blob:
9d583178ebd5c58fd6c692bcfdef482d180ef18e

terminal:
PASS_SHD_SECE_R01_MULTI_OUTCOME_AGGREGATION_REVIEW

## Goal

Implement one bounded OFFLINE deterministic simulator/harness implementation candidate that faithfully implements the reviewed simulator DESIGN and architecture.

The implementation candidate exists only to execute synthetic fixtures locally/offline.

It must not perform real project effects.

## Implementation scope

Implement the reviewed module behavior needed to execute the canonical fixture catalog.

Required functional pipeline:

RAW synthetic context
-> semantic atoms/bindings
-> context composition
-> collision detection
-> exact-scope correction
-> EFFECTIVE_CONTEXT(n)
-> bounded L6 execution-contract projection
-> C1/C2/C3 validation
-> complete validator predicate set
-> local L7 MULTI_OUTCOME_AGGREGATION
-> synthetic one-safe-step only after ADMIT
-> synthetic RESULT/EVENT classification
-> CONTEXT_DELTA
-> EFFECTIVE_CONTEXT(n+1)
-> next-gate classification
-> canonical trace
-> fixture oracle.

No real effect.

## Implementation modules

Implement the reviewed behavior corresponding to all 22 interfaces:

1 FixtureLoader
2 RawContextLoader
3 SemanticAtomLoader
4 ContextComposer
5 CollisionDetector
6 ContextCorrectionEngine
7 DependencyScopeResolver
8 EffectiveContextBuilder
9 ExecutionContractProjector
10 ActionAuthorizationValidator
11 CausalEventValidator
12 CurrentStateEvidenceResolver
13 StaticValidator
14 MultiOutcomeAggregator
15 RuntimeStepGuardSimulator
16 ResultClassifier
17 ContextDeltaBuilder
18 SuccessorContextBuilder
19 NextGateResolver
20 HumanCausalRenderer
21 TraceRecorder
22 FixtureOracle

Internal code organization may combine modules only if:
- external semantics remain separable/testable;
- no reviewed boundary is collapsed;
- mapping from reviewed interface -> implementation component is documented.

## Language/toolchain

Choose the smallest appropriate offline implementation language/toolchain already suitable for the repository/environment.

Requirements:
- deterministic;
- dependency-minimal;
- preferably standard-library only where practical;
- no network at test/runtime;
- no model/API dependency.

Record exact interpreter/runtime requirements.

Do not install or mutate production host services.

## Canonicalization and identities

Implement reviewed deterministic canonicalization exactly.

contract_id:

SHA-256(
  "sece-execution-contract-r01\0"
  + canonical complete SECE_EXECUTION_CONTRACT_R01 payload without contract_id
)

Only contract_id excluded.

trace_id:

SHA-256(
  "sece-simulator-trace-r01\0"
  + canonical complete trace payload without trace_id
)

Only trace_id excluded.

Implement context/delta identities according to reviewed design without adding time/random/process-dependent values.

## Fixture/schema requirements

The implementation must validate the corrected closed FIXTURE-SCHEMA before fixture execution.

Canonical fixture source:

FIXTURE-CATALOG.json
blob 4ce7939519ecdfa24e4102742be519fa5d5f2259

Required inventory:
54 total:
T1-T15 = 15
CXT1-CXT10 = 10
O1-O10 = 10
P1-P7 = 7
M1-M12 = 12

Unknown/unrecognized semantic fields must fail closed.
No arbitrary free-form field may become executable behavior.

## Required test gates

### G1 Schema/catalog

- corrected schema loads;
- corrected catalog loads;
- 54/54 fixtures validate;
- 54 unique IDs;
- family counts exact.

### G2 Contract identity

Independently execute the published contract test vectors.

Required:
- published base SHA-256 reproduced exactly;
- canonical-identical copy same ID;
- 25/25 semantic field mutations change ID.

### G3 Trace identity

Independently execute trace test vectors.

Required:
- published base SHA-256 reproduced exactly;
- canonical-identical trace same ID;
- recomputed_bindings mutation changes ID;
- corrected trace validates against schema.

### G4 Fixture execution

Execute all 54 canonical fixtures.

Required:
- T = 15/15
- CXT = 10/10
- O = 10/10
- P = 7/7
- MUTATION = 12/12
- total = 54/54

Each fixture must produce:
- canonical machine result;
- oracle PASS/FAIL;
- trace_id;
- exact mismatch report if FAIL.

No fixture may pass through hard-coded fixture ID branching.

## Anti-cheat / semantic fidelity rules

Forbidden:
- switch/case keyed by fixture_id to return expected result;
- using expected oracle output as actual computation input;
- bypassing validators for positive controls;
- special-case code for T/CXT/O/P/M labels except schema/family decoding;
- mutating fixture expected values at runtime;
- ignoring unknown fields silently;
- treating prose description as executable semantics.

The harness must compute behavior from typed fixture input + reviewed rules.

## Required architecture assertions

Automated tests must prove at least:

1. context composition preserves compatible parallel lines;
2. scope-local conflict does not erase independent scope;
3. dependency change recomputes dependent bindings only;
4. stale dependent binding cannot survive;
5. L6 projection cannot invent context facts;
6. ACTION_INTENT is proposal only;
7. capability/profile/experience do not create authority;
8. C1/C2/C3 validators remain explicit;
9. L7 aggregation remains local to one transition;
10. all simultaneous reasons remain traceable;
11. no ADMIT when conflict/reject/blocker/required UNKNOWN/FAIL exists under reviewed mapping;
12. unverified/UNKNOWN/conflicted synthetic event cannot mutate successor context;
13. Task Conveyor/Recovery/current-writer are represented only as external evidence/boundaries, not reimplemented as authority generators.

## Deterministic trace

Every executed fixture must generate a trace satisfying corrected TRACE-SCHEMA and containing the full causal path:

Context(n)
-> trigger
-> scope changes
-> invalidated/recomputed/preserved bindings
-> delta
-> Context(n+1)
-> L6 contract/projection
-> predicates
-> aggregation
-> classified synthetic result/event
-> next-gate classification
-> expected_vs_actual.

Trace is returned/test data only.

No external sink required.

## Side-effect firewall

Implementation MUST fail if an attempted code path tries to use:
- network;
- provider/model API;
- Telegram;
- subprocess intended for external effect;
- host/service control;
- credential access;
- production storage mutation.

Repository fixture/code reads and local ephemeral test-memory/temp artifacts required for offline tests are allowed only within bounded implementation/test environment.

No production/live service.

## Output package

Create one immutable implementation-candidate package, e.g.:

entities/koder/outbox/sece-r01-offline-simulator-implementation-candidate/

Include at minimum:

- source code;
- offline test runner;
- schema validator/canonicalizer;
- fixture runner;
- trace/oracle implementation;
- README/RUNBOOK for offline execution;
- exact dependency/runtime declaration;
- TEST-RESULTS.md
- COVERAGE-MAP.md mapping 22 design interfaces to code;
- SECURITY-BOUNDARY.md
- MANIFEST.md

Preserve exact reviewed schema/catalog/test vectors by immutable reference or exact vendored copy with verified blob/hash identity.

## Required result evidence

Return exact machine-verifiable evidence for:

IMPLEMENTATION_CANDIDATE_CREATED=YES
SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
T_FIXTURES_PASS=15/15
CXT_FIXTURES_PASS=10/10
O_FIXTURES_PASS=10/10
POSITIVE_CONTROLS_PASS=7/7
PROPERTY_FIXTURES_PASS=12/12
TOTAL_FIXTURES_PASS=54/54
TRACE_SCHEMA_PASS=YES
DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES
DESIGN_INTERFACE_MAPPING_COMPLETE=22/22

If any is not established:
do not claim PASS.

## Status

OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

This candidate is NOT:
- production;
- runtime-activated;
- source/canon activation;
- an Entity authority engine;
- approval for live use.

## Stop conditions

STOP with exact blocker if:
- any reviewed input identity mismatches;
- KOD writer conflict/supersession appears;
- implementation requires inventing a semantic rule not in reviewed design;
- any fixture meaning must be changed to make tests pass;
- network/live dependency becomes necessary;
- deterministic identity cannot be reproduced;
- side-effect firewall cannot be demonstrated.

## Expected terminal

PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/tree/blobs;
- runtime/language choice;
- 22/22 design-interface mapping;
- exact test command;
- all required result markers;
- fixture-family pass counts;
- identity-vector results;
- determinism evidence;
- side-effect evidence;
- any blocker/known limitation;
- status OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED;
- exact next gate:
  independent bounded implementation-candidate review only.

Then STOP.
