# KOO -> KOD: SECE r0.1 OFFLINE simulator implementation correction successor

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

## Exact SHD independent review result

puev5691/wellbeing-hq@d9b4f0395e284cc1098fa5d0ac615ecf4446546d:
entities/shardovik/outbox/SHD__SECE-r01-offline-simulator-implementation-candidate-successor-review__KOO.md

blob:
ddbb81956d5164582d0768ec8e04cc3580670b21

terminal:
BLOCKED_REVIEW_EXECUTION_ENVIRONMENT

Important:
this result contains TWO distinct facts:

A. independent exact command execution was unavailable in SHD review environment;

B. static source review found implementation defects that independently prevent PASS.

This task addresses ONLY B.

Do NOT try to solve the SHD review-environment limitation by mutating hosts, deployment environment, or external infrastructure.

## Exact predecessor implementation candidate

puev5691/wellbeing-hq@ab5b41145c08cc9639ffc96617c7612af76dc994:
entities/koder/outbox/sece-r01-offline-simulator-implementation-candidate-successor/

package tree:
eb2743a5dea5da3431a09e97b4e4d3485f7788a2

status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Exact result:

puev5691/wellbeing-hq@29063d168e5ac078fd694b69cb023f1333ba8a2e:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-implementation-candidate-successor-result__KOO.md

blob:
d9458b16c03fa7d9a0ab52e102ea516d3d93e927

## Reviewed design/input basis remains authoritative for this correction

Input-completeness PASS:

puev5691/wellbeing-hq@a22779b65015e5160c5cf98a4c64058345fb0688:
entities/shardovik/outbox/SHD__SECE-r01-simulator-design-input-completeness-review__KOO.md

blob:
c6ef3e94231f61d5ca945cd461848880b99faa65

terminal:
PASS_SHD_SECE_R01_SIMULATOR_DESIGN_INPUT_COMPLETENESS_REVIEW

Reviewed Effective Context PASS:

puev5691/wellbeing-hq@7b77579c81f10b006417f8e6ee450ec396a20b04:
entities/shardovik/outbox/SHD__SECE-r01-effective-context-clarification-review__KOO.md

blob:
325dd7d9a6c5d0edd4270177703a7d257be2f56d

Reviewed MULTI_OUTCOME_AGGREGATION PASS:

puev5691/wellbeing-hq@49cd4669539068277f70886c41a2b65c024905f1:
entities/shardovik/outbox/SHD__SECE-r01-multi-outcome-aggregation-review__KOO.md

blob:
9d583178ebd5c58fd6c692bcfdef482d180ef18e

Reviewed D2 identity blob:
7339655c132459f87a1943f4f825d45b497108e3

Reviewed D3 trace blob:
0876cff31d1e4b54b065933aa74129e591c78e94

## Scope

Perform ONLY a NEW bounded implementation correction successor addressing the exact static defects identified by SHD.

Do NOT:
- resume/replay historical implementation tasks;
- alter reviewed fixture meanings;
- alter reviewed D2/D3 identity semantics;
- alter L0-L9;
- redesign Effective Context semantics;
- redesign CONTEXT_DELTA semantics;
- redesign C1/C2/C3;
- redesign MULTI_OUTCOME_AGGREGATION;
- activate/deploy runtime;
- call provider/model/API/Telegram;
- mutate host/services/production storage;
- access/create credentials;
- activate Sources/canons;
- mutate roles/recovery/current-writer;
- create production/live authority.

## Defect C1 — JSON Schema minimum support

SHD finding:
ClosedSchemaValidator does not implement keyword "minimum" although reviewed FIXTURE-SCHEMA uses it.

Correction:
implement exact JSON-Schema minimum semantics required by the reviewed schemas.

Required:
- numeric minimum enforced;
- non-numeric behavior remains governed by type validation;
- add negative test where a value below reviewed minimum is rejected;
- add positive boundary test equal to minimum;
- no claim of full generic JSON Schema support.

Return marker:
REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED=YES

## Defect C2 — ContextCorrectionEngine reviewed scoped correction

SHD finding:
ContextCorrectionEngine.correct currently returns copied context/collisions with corrections=[] and does not perform reviewed exact-scope correction.

Correction must implement reviewed behavior sufficiently for exact design scope:

- consume typed collisions and applicable reviewed correction rules/state;
- create explicit correction objects;
- correct only affected exact scope;
- preserve unaffected semantic lines;
- retain unresolved conflicts/UNKNOWN where unresolved;
- emit invalidation seeds/changed-state information required for successor context;
- never rewrite prior immutable context;
- no winner-takes-all global composition.

Add direct tests proving:
1. correction in S1 leaves independent S2 unchanged;
2. verified refinement changes only affected scope;
3. unresolved conflict remains explicit blocker, not silently erased;
4. correction output is actually consumed downstream.

Return marker:
CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED=YES

## Defect C3 — EffectiveContextBuilder full reviewed structure

SHD finding:
EffectiveContextBuilder emits a reduced payload and omits major reviewed EFFECTIVE_CONTEXT fields.

Correction must implement the reviewed schema/semantic structure sufficient for simulator scope, including at minimum:

- context_id
- context_version
- entity
- instance
- role
- active_source_set[]
- semantic_invariants[]
- current_state_evidence[]
- selected_current_basis_by_scope[]
- current_tasks[]
- authority_bindings[]
- profile
- experience_set[]
- capability_set[]
- causal_events[]
- human_input_facts[]
- unknown_facts[]
- conflict_set[]
- context_corrections[]
- derived_bindings[]
- provenance[]
- scope_index[]
- dependency_graph[]
- prior_context_ref
- context_delta_ref

Preserve orthogonal semantic/epistemic/lifecycle/authority-effect distinctions where represented.

Field presence MUST NOT create authority.

Context identity must remain deterministic and bind complete canonical semantic context payload per reviewed design.

Add direct schema/semantic tests.

Return marker:
EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED=YES

## Defect C4 — C1 projection boundary

SHD finding:
ExecutionContractProjector always emits ACTION_AUTHORIZATION_BINDINGS=[] and validators read raw fixture facts directly.

Correction:

- project C1 ACTION_AUTHORIZATION_BINDINGS[] from EFFECTIVE_CONTEXT into the bounded L6 contract;
- preserve exact action/rule/source/authority/task/currentness provenance needed by reviewed C1;
- ActionAuthorizationValidator must consume projected contract C1 binding state, not bypass L6 via raw fixture authority facts for the final authorization decision;
- raw context may be used only upstream to build EFFECTIVE_CONTEXT.

Add tests showing:
1. valid projected C1 binding admits when all other predicates clear;
2. missing/stale/conflicted binding rejects/blocks as reviewed;
3. changing raw fixture authority fact without corresponding EFFECTIVE_CONTEXT/L6 binding cannot bypass projector/validator boundary.

Return marker:
C1_L6_PROJECTION_BOUNDARY_FIXED=YES

## Defect C5 — actual L6 projection firewall enforcement

SHD finding:
projection_valid is currently a fixture/assertion proxy, not projector enforcement.

Correction:
ExecutionContractProjector itself must enforce:

- every projected context fact/binding exists in EFFECTIVE_CONTEXT;
- only ACTION_INTENT may be added as the extra semantic input;
- projection_basis[] references actual EFFECTIVE_CONTEXT items;
- context_dependency_refs[] are valid referenced dependencies;
- missing projection basis => projection invalid before L7;
- invented contract-only context fact/binding => projection invalid before L7.

Represent an explicit projection validation result/error object that StaticValidator/L7 path consumes.

Add negative tests by mutating projection source data, not fixture expected output.

Return marker:
L6_PROJECTION_FIREWALL_ENFORCED=YES

## Defect C6 — ResultClassifier fidelity

SHD finding:
ResultClassifier currently maps synthetic action event or VERIFIED trigger to PASS without comparing actual observation to EXPECTED_RESULT / EXPECTED_TERMINAL.

Correction:
implement reviewed classification:

Input:
- injected synthetic observation/result;
- contract EXPECTED_RESULT;
- contract EXPECTED_TERMINAL.

Output:
- PASS only when observed synthetic result matches reviewed expected result/terminal semantics;
- FAIL on verified mismatch;
- UNKNOWN when required observation is absent/unknown;
- NOT_APPLICABLE only where exact reviewed flow permits.

No oracle expected fixture object may be used here.
Use only execution contract expectation fields + synthetic observation.

Add direct PASS/FAIL/UNKNOWN tests.

Return marker:
RESULT_CLASSIFIER_FIDELITY_FIXED=YES

## Defect C7 — NextGateResolver grounding

SHD finding:
NextGateResolver currently echoes aggregation.next_gate_class and AGGREGATION_RULE ref only.

Correction:
NextGateResolver must consume:

- aggregation next_gate_class;
- verified RESULT/EVENT;
- active NEXT_GATE_RULE[];
- current verified state/Task Conveyor evidence carried by EFFECTIVE_CONTEXT/L6 contract as reviewed.

It may return an exact next-gate candidate ONLY when grounded by those inputs.

Must NOT:
- derive exact routing from terminal alone;
- derive from list order;
- infer from historical queue;
- invent recipient/task;
- convert aggregation class into authority.

Add tests:
1. class + exact active rule + verified state => grounded candidate;
2. class without exact active rule => NONE/UNKNOWN/STOP as reviewed;
3. historical/superseded rule cannot route;
4. terminal alone cannot route.

Return marker:
NEXT_GATE_RESOLVER_GROUNDING_FIXED=YES

## Defect C8 — strengthen architecture assertions

SHD identified weak proxy tests.

Replace/augment assertions so each stated property is directly tested, not inferred from class existence or a single proxy flag.

Required strengthened assertions:

A1 compatible semantic lines coexist.
A2 scope-local conflict preserves unrelated scope.
A3 dependency changes recompute complete dependency closure only.
A4 stale dependent binding cannot survive:
   construct transitive dependency case and prove all transitively dependent bindings invalidated and none preserved.
A5 L6 projection cannot invent context facts:
   directly attempt projection with absent fact/binding and prove projector rejection before L7.
A6 ACTION_INTENT remains proposal only:
   vary ACTION_INTENT without authority and prove no authority/effect is created.
A7 profile/experience/capability do not create authority:
   mutate each independently and prove authority outcome invariant absent authority binding change.
A8 C1/C2/C3 explicit:
   inspect actual projected contract structures and prove validators consume them.
A9 L7 aggregation local:
   prove aggregation does not mutate EFFECTIVE_CONTEXT.
A10 simultaneous reasons preserved:
   multiple predicates remain in secondary reasons/provenance.
A11 no ADMIT with conflict/reject/blocker/required UNKNOWN/FAIL.
A12 unverified/UNKNOWN/conflicted event cannot mutate successor context.
A13 Task Conveyor/Recovery/current-writer remain external evidence/boundaries:
   vary those evidence states and prove simulator does not synthesize authority from them.

Each test must fail if the actual stated property is broken.

Return marker:
ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13

## Integration requirements

After correcting C1-C8:

- retain all 54 reviewed fixture meanings unchanged;
- retain reviewed input blobs or exact semantic successors only if correction requires internal generated structures;
- preserve D2/D3 identity semantics exactly;
- preserve generic binding derivation;
- preserve anti-cheat boundaries;
- preserve deterministic/no-side-effect boundaries.

## Required execution tests in KOD environment

Run exact package-local commands for corrected candidate:

python3 -m py_compile <all corrected .py modules>
python3 -I -B run_offline_tests.py
python3 -I -B fixture_runner.py

Add dedicated negative/architecture tests for C1-C8.

Required:

SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
TOTAL_FIXTURES_PASS=54/54
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15

and new:

REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED=YES
CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED=YES
EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED=YES
C1_L6_PROJECTION_BOUNDARY_FIXED=YES
L6_PROJECTION_FIREWALL_ENFORCED=YES
RESULT_CLASSIFIER_FIDELITY_FIXED=YES
NEXT_GATE_RESOLVER_GROUNDING_FIXED=YES
ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13

## Anti-cheat regression tests

Still required:

ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES

Add:
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES

Meaning:
core architectural invariants such as projection firewall/correction cannot be satisfied merely because fixture transformation enum says they should be.

## Side-effect boundary

Retain and re-test:
- no network;
- no provider/model/API/Telegram;
- no host/service effect;
- no credential access;
- no production storage mutation;
- no runtime activation.

## Output

Create one NEW immutable corrected implementation-candidate successor package, e.g.:

entities/koder/outbox/sece-r01-offline-simulator-implementation-candidate-correction-successor/

Include at minimum:

- corrected source;
- corrected offline tests;
- strengthened architecture tests;
- schema validator tests including minimum negative/boundary cases;
- anti-cheat regression tests;
- README/RUNBOOK;
- TEST-RESULTS.md;
- CORRECTION-MAP.md mapping SHD defects C1-C8 -> code/tests/evidence;
- COVERAGE-MAP.md;
- SECURITY-BOUNDARY.md;
- MANIFEST.md;
- package identity/SHA256SUMS.

Status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

## STOP conditions

STOP if:
- fixing a defect requires changing reviewed SECE semantics;
- fixture meaning must change;
- D2/D3 identity semantics must change;
- external/live dependency is required;
- KOD writer conflict appears;
- side-effect boundary cannot be preserved.

## Expected terminal

PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CORRECTION_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/tree/blobs;
- exact correction map C1-C8;
- exact test command;
- all old required markers;
- all new correction markers;
- 54/54 fixture counts;
- strengthened 13/13 assertion results;
- anti-cheat regression result;
- determinism/side-effect evidence;
- status OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED;
- exact next gate:
  NEW independent bounded corrected-implementation review only.

Do not attempt to solve SHD review-environment execution limitation in this task.

Then STOP.
