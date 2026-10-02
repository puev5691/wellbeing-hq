# KOO -> KOD: SECE r0.1 simulator-design input-completeness correction

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

## Exact implementation blocker

puev5691/wellbeing-hq@989a124944afb35bb0ced6227b1a7037b353c3d4:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-implementation-candidate-blocker__KOO.md

blob:
31c8c0e79ffa1f6b01509b2b80f4e6bd07202b87

terminal:
BLOCKED_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_FIXTURE_INPUT_INSUFFICIENT

IMPLEMENTATION_BLOCKER:
TYPED_FIXTURE_INPUT_DOES_NOT_DETERMINE_REQUIRED_BINDING_SET_OUTPUTS

Affected fixtures:
CXT1-CXT10
P3
P4
P6
M6
M8

count:
15/54

## Exact reviewed design basis

Reviewed D1/D2/D3 PASS:

puev5691/wellbeing-hq@89f5c103de4526771e6dd71674ade0f3aeae5151:
entities/shardovik/outbox/SHD__SECE-r01-simulator-design-D1D2D3-rereview__KOO.md

blob:
68c7eed500bb00fae8c25b5c153de390687ed7f0

terminal:
PASS_SHD_SECE_R01_SIMULATOR_DESIGN_D1D2D3_REREVIEW

Correction package:

puev5691/wellbeing-hq@9e1d66efc798041d2217c5e9a195fc795d84aad9:
entities/koder/outbox/sece-r01-offline-simulator-design-successor-d1d2d3-correction/

tree:
66686bac2a742a4673ec7da9eb2b7b57a74c7721

Relevant exact blobs:

FIXTURE-SCHEMA.json
7d221176ebd694d67321261c5466f6df1090bf8f

FIXTURE-CATALOG.json
4ce7939519ecdfa24e4102742be519fa5d5f2259

TRACE-SCHEMA.json
0876cff31d1e4b54b065933aa74129e591c78e94

IDENTITY-SPEC.md
7339655c132459f87a1943f4f825d45b497108e3

## Scope

Perform ONLY a bounded simulator-DESIGN input-completeness correction.

Do NOT resume the blocked implementation task.
Do NOT create an implementation candidate.

Do NOT reopen:
- L0-L9;
- Effective Context semantics;
- CONTEXT_DELTA semantics;
- C1/C2/C3;
- MULTI_OUTCOME_AGGREGATION;
- D2 contract identity;
- D3 trace identity;
- Task Conveyor;
- Recovery;
- current-writer boundaries;
- fixture meanings.

Goal:
make every affected fixture's exact binding-set outputs derivable solely from typed machine input + reviewed rules, with no oracle feedback, fixture_id branching, hidden mapping, or invented semantic naming convention.

## Acceptable bounded evidence forms

Choose ONE or a minimal combination, without changing fixture meaning:

A. Embed typed initial execution state in fixture input:
- initial_effective_context
- initial_derived_bindings[]
- dependency_graph[]
- scope_index[]
- selected current basis as required

B. Provide exact immutable base_context_ref to a machine-readable synthetic base context containing those structures.

C. Define and independently test a deterministic generic binding-construction/dependency rule that is already justified by reviewed architecture and is sufficient to derive exact binding IDs.

Do NOT invent an arbitrary naming rule merely to satisfy fixtures.

Preferred approach:
explicit typed synthetic state/reference, because binding IDs are fixture data, not project semantics.

## Required machine input closure

For every affected fixture, actual computation must be able to derive:

invalidated_bindings[]
recomputed_bindings[]
preserved_bindings[]

from INPUT ONLY.

The implementation must not read expected/oracle fields to construct actual output.

Required typed structures should cover as needed:

### InitialDerivedBinding
- binding_id
- binding_type
- exact_scope
- dependencies[]
- current_state
- provenance_ref
- semantic_role
- recomputation_rule_ref if applicable

### DependencyEdge
- edge_id
- source_atom_or_evidence_id
- dependent_binding_id
- exact_scope
- relation_type
- provenance_ref

### ScopeIndexEntry
- scope_id
- atom_ids[]
- evidence_ids[]
- binding_ids[]
- child_scopes[] if applicable

### Base synthetic context reference
If using base_context_ref:
- exact immutable synthetic-context identity
- exact schema/version
- exact content/hash/blob identity
- no external hidden lookup beyond declared package fixture asset

Equivalent closed structures are acceptable.

## MUTATION fixtures

For M6 and M8 where base_fixture_ref is null:

provide exact typed base state sufficient for the transformation.

The mutation must be computable as:

BASE_STATE
+ typed transformation
-> actual changed dependency/state
-> dependency traversal
-> invalidated/recomputed/preserved bindings

No fixture_id-specific lookup.

## Affected fixture requirements

Re-close only these:

CXT1
CXT2
CXT3
CXT4
CXT5
CXT6
CXT7
CXT8
CXT9
CXT10
P3
P4
P6
M6
M8

For each return proof:

INPUT_COMPLETE_FOR_BINDING_DERIVATION=YES

and machine derivation path:

typed initial state
-> trigger/change
-> dependency traversal
-> invalidated set
-> recomputed set
-> preserved set

## Meaning containment

The following MUST remain unchanged for all 54 fixtures:

- fixture_id;
- family;
- description;
- architecture_rule_refs;
- provenance;
- semantic intent;
- expected semantic outcome.

You may add typed input state needed to compute already-existing expected outputs.

Do not change expected outputs merely to match new input.

## Schema correction

Update FIXTURE-SCHEMA only as needed to admit the new typed input structures.

Semantic nested objects remain closed:
additionalProperties:false or equivalent.

No arbitrary executable strings.

UNKNOWN/conflict remain exact states.

## Catalog correction

Update FIXTURE-CATALOG only to add required machine input completeness.

Required:
- 54 total records;
- same 54 IDs;
- same family counts;
- all 54 validate;
- unaffected 39 fixtures semantically unchanged and ideally byte/logically unchanged except schema-version references if unavoidable.

## Required anti-cheat proof

Provide explicit evidence that implementation can compute affected outputs without:

- reading expected.invalidated_bindings;
- reading expected.recomputed_bindings;
- reading expected.preserved_bindings;
- branching on fixture_id;
- hidden scope/change -> binding ID tables;
- prose description;
- invented binding-ID naming rules.

Design a generic derivation demonstration over at least representative:
CXT3
CXT6
P6
M8

and preferably all 15 affected fixtures.

## Validation gates

V1:
corrected schema validates catalog 54/54.

V2:
all 15 affected fixtures have complete typed binding/dependency input.

V3:
derive exact invalidated/recomputed/preserved sets for all 15 solely from input structures.

V4:
expected values are used only by FixtureOracle after actual computation.

V5:
39 unaffected fixtures retain meanings.

V6:
M6/M8 have non-null computable base state in corrected semantics.

## Required closure markers

INPUT_COMPLETENESS_CORRECTION_CLOSED=YES
AFFECTED_FIXTURES_INPUT_COMPLETE=15/15
BINDING_SET_OUTPUTS_DERIVABLE_FROM_TYPED_INPUT=15/15
FIXTURE_CATALOG_VALIDATES_54_OF_54=YES
FIXTURE_MEANINGS_UNCHANGED=YES
ORACLE_NOT_USED_AS_COMPUTATIONAL_INPUT=YES
NO_FIXTURE_ID_BRANCHING_REQUIRED=YES
NO_HIDDEN_BINDING_ID_MAPPING_REQUIRED=YES
MUTATION_BASE_STATE_COMPLETE_M6_M8=YES
D2_IDENTITY_SEMANTICS_UNCHANGED=YES
D3_TRACE_SEMANTICS_UNCHANGED=YES
DETERMINISM_BOUNDARY_PRESERVED=YES
NO_SIDE_EFFECT_BOUNDARY_PRESERVED=YES

## Output package

Create one immutable simulator-DESIGN correction package, e.g.:

entities/koder/outbox/sece-r01-simulator-design-input-completeness-correction/

Include at minimum:

- corrected FIXTURE-SCHEMA.json
- corrected FIXTURE-CATALOG.json
- BASE-CONTEXT-SCHEMA.json if used
- synthetic base-context assets if used
- INPUT-DERIVATION-SPEC.md
- AFFECTED-FIXTURE-DERIVATION-REPORT.md
- CORRECTION-DIFF.md
- VALIDATION-REPORT.md
- MANIFEST.md

Status:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Boundaries

Do NOT:
- implement simulator/runtime;
- resume historical blocked implementation task;
- create a new implementation candidate;
- activate Sources/canons;
- mutate roles/recovery/current-writer;
- call providers/Telegram;
- mutate host/runtime/storage;
- access/create credentials;
- create production/live authority.

## Expected terminal

PASS_KOD_SECE_R01_SIMULATOR_DESIGN_INPUT_COMPLETENESS_CORRECTION_READY_FOR_SHD_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/tree/blobs;
- chosen completeness mechanism;
- 15/15 affected fixture derivation evidence;
- 54/54 schema validation;
- anti-cheat proof;
- meaning-containment proof;
- closure markers;
- confirmation D2/D3 unchanged;
- status SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- OFFLINE_IMPLEMENTATION_DESIGN_READINESS=NOT_ESTABLISHED pending SHD review;
- exact next gate:
  SHD narrow independent input-completeness correction review only.

Then STOP.
