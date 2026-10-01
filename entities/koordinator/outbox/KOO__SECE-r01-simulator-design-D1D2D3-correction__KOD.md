# KOO -> KOD: SECE r0.1 simulator-design D1/D2/D3 correction-only

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

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact SHD NEEDS_REWORK

puev5691/wellbeing-hq@1029c15789e546270c77cf8c33ac9a92bd377071:
entities/shardovik/outbox/SHD__SECE-r01-offline-simulator-design-successor-review__KOO.md

blob:
1114d4ab99ccdd1d948cd940da6c36bb503e7654

terminal:
NEEDS_REWORK_SHD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_SUCCESSOR_REVIEW

DESIGN_STATUS:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

OFFLINE_IMPLEMENTATION_DESIGN_READINESS=NO

Blocking defects:
D1 fixture schema closure.
D2 contract_id full semantic payload binding.
D3 trace schema causal reconstruction closure.

No other architecture/design blocker is authorized to be reopened by this task.

## Exact predecessor design package

puev5691/wellbeing-hq@5b9642fe5915386518ea0d3a7d9f2b9ee6376469:
entities/koder/outbox/sece-r01-offline-simulator-design-successor/

tree:
6f3056ac669377c4dc0211d34da7d321ea75836c

Relevant exact blobs:

FIXTURE-SCHEMA.json
8a414eece84c924670e1d14431e85692d1c4381f

FIXTURE-CATALOG.json
7e39b90736c6d84f75a4581c46de7bd9baa34c99

SIMULATOR-ARCHITECTURE.md
d5cb5dc2be66db94af3c46be769d5261b5d08927

TRACE-SCHEMA.json
07002d5cf5ffdd15aa9947d620ded69bc0384719

MANIFEST.md
01961a2ba2d8577430e00c5b327c283c07dcd708

Fixture catalog meanings remain fixed:
T1-T15
CXT1-CXT10
O1-O10
P1-P7
M1-M12
total 54.

## Scope

Perform ONLY bounded simulator-DESIGN correction of D1, D2, D3.

Do NOT:
- alter fixture meanings;
- redesign L0-L9;
- reopen Effective Context;
- alter CONTEXT_DELTA semantics;
- reopen C1/C2/C3;
- alter MULTI_OUTCOME_AGGREGATION semantics;
- change Task Conveyor / Recovery / current-writer boundaries;
- implement runtime;
- call network/providers/Telegram;
- mutate host/storage;
- create credentials;
- activate Sources/canons;
- create production/live authority.

## D1 — close machine-semantic fixture schema

Problem:
predecessor FIXTURE-SCHEMA permits arbitrary nested input/expected objects, so implementation would need hidden conventions.

Correction must make fixture semantics machine-closed while preserving all 54 existing meanings.

Use one of these bounded forms:

A. discriminated closed schema per family:
T
CXT
O
P
MUTATION

or

B. one common closed typed operation/assertion vocabulary with family discriminators.

Required:

- family discriminator;
- exact typed input operation/state objects;
- exact typed expected assertion/outcome objects;
- exact enums for UNKNOWN/conflict/lifecycle/outcome where applicable;
- explicit schema for affected scopes;
- explicit schema for invalidated/recomputed/preserved bindings;
- explicit schema for validator predicates;
- explicit schema for aggregation expectations;
- explicit schema for context successor assertions;
- explicit schema for mutation/property transformation and expected invariant;
- additionalProperties:false on semantic nested objects;
- no free-form string command interpreted as machine behavior;
- no hidden family-specific implementation convention.

The 54 fixture IDs and meanings must remain unchanged.

Return marker:
D1_FIXTURE_SCHEMA_CLOSED=YES

## D2 — bind contract_id to complete semantic contract payload

Problem:
predecessor contract_id hashes only:
effective_context_id + selected_scope + action_id + projection_basis.

That does not prove identity of all semantically significant contract fields.

Correction:

contract_id MUST be a domain-separated deterministic digest of the complete canonical semantically meaningful SECE_EXECUTION_CONTRACT_R01 payload, excluding only contract_id itself and any explicitly proved non-semantic presentation fields.

ACTION_INTENT content must be included, not merely action_id.

At minimum identity binding must cover:
- effective_context_id/version;
- selected_scope;
- projection_basis[];
- context_dependency_refs[];
- full ACTION_INTENT;
- C1 ACTION_AUTHORIZATION_BINDINGS[];
- C2 CAUSAL_EVENTS[];
- C3 CURRENT_STATE_EVIDENCE[];
- ALLOWED_ACTIONS[];
- FORBIDDEN_ACTIONS[];
- REQUIRED_PRECONDITIONS[];
- STOP_IF[];
- EXPECTED_RESULT;
- EXPECTED_TERMINAL[];
- NEXT_GATE_RULE[];
- relevant provenance/validation state;
- every other field whose change can alter validator/result/next-gate semantics.

Preferred rule:

contract_id =
SHA-256(
  domain_separator
  + canonical_complete_semantic_contract_payload_without_contract_id
)

Define canonicalization and exclude nothing semantically relevant.

No circular identity.

Return marker:
D2_CONTRACT_ID_FULL_PAYLOAD_BOUND=YES

## D3 — close trace schema

Problem:
predecessor TRACE-SCHEMA cannot reconstruct the full declared causal path without hidden lookups.

Add required machine fields for at least:

- trace_id REQUIRED;
- recomputed_bindings[];
- context_delta_id;
- contract_id;
- projected_effective_context_id;
- projected_effective_context_version;
- projection_scope;
- projection_basis[];
- context_dependency_refs[];
- classified_result_id or equivalent;
- classified_result_state;
- synthetic_event_or_result_id;
- synthetic_event_or_result_type;
- synthetic_event_or_result_verification_state;
- resulting_context_id;
- exact aggregation object identity/rule;
- next-gate derivation refs where applicable.

Trace must reconstruct:

Context(n)
-> triggering event/result
-> affected scopes
-> invalidated bindings
-> recomputed bindings
-> preserved bindings
-> CONTEXT_DELTA
-> Context(n+1)
-> L6 contract/projection
-> validator predicate set
-> aggregation
-> classified synthetic result/event
-> next-gate class
-> expected_vs_actual

without narrative or external hidden lookup.

Trace remains returned data only.
No implicit storage/network sink.

trace_id must be deterministic domain-separated digest of complete canonical trace payload excluding only trace_id itself.

Return marker:
D3_TRACE_SCHEMA_CLOSED=YES

## Required consistency checks

Revalidate only what D1/D2/D3 directly affect:

1. all 54 catalog records validate against corrected fixture schema;
2. no fixture meaning changed;
3. two semantically different execution contracts cannot share contract_id under declared identity rule;
4. identical canonical semantic contract yields identical contract_id;
5. trace schema can fully reference context delta, contract projection, recomputation and classified result/event;
6. identical canonical trace yields identical trace_id;
7. trace contains no hidden authority semantics;
8. deterministic/no-side-effect boundary unchanged.

Required markers:

FIXTURE_CATALOG_VALIDATES_54_OF_54=YES
FIXTURE_MEANINGS_UNCHANGED=YES
CONTRACT_ID_COLLISION_BY_OMITTED_SEMANTIC_FIELD_PREVENTED=YES
TRACE_CAUSAL_PATH_RECONSTRUCTABLE=YES
DETERMINISM_BOUNDARY_PRESERVED=YES
NO_SIDE_EFFECT_BOUNDARY_PRESERVED=YES

## Output

Create one immutable correction successor package, for example:

entities/koder/outbox/sece-r01-offline-simulator-design-successor-d1d2d3-correction/

Include at minimum:

- corrected FIXTURE-SCHEMA.json
- corrected TRACE-SCHEMA.json
- corrected SIMULATOR-ARCHITECTURE.md or IDENTITY-SPEC.md for D2
- exact CORRECTION-DIFF.md
- validation/readback report for 54 fixtures
- MANIFEST.md
- any unchanged predecessor artifacts by exact immutable reference, not silent reconstruction.

Status:
SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Expected terminal

PASS_KOD_SECE_R01_SIMULATOR_DESIGN_D1D2D3_CORRECTION_READY_FOR_SHD_REREVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/tree/blobs;
- D1/D2/D3 closure markers;
- 54/54 schema validation result;
- contract identity rule;
- trace identity and reconstruction result;
- confirmation fixture meanings unchanged;
- confirmation architecture boundaries unchanged;
- DESIGN_STATUS=SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- OFFLINE_IMPLEMENTATION_DESIGN_READINESS remains NOT_ESTABLISHED until SHD rereview;
- exact next gate:
  SHD narrow rereview D1/D2/D3 only.

Then STOP.
