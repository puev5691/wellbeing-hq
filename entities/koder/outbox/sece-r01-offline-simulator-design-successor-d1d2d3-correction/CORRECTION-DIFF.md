# SECE r0.1 simulator design successor — D1/D2/D3 exact correction diff

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
correction_scope: D1_D2_D3_ONLY
project_time: omitted

## Exact task

puev5691/wellbeing-hq@565771897bc51bcc406eb192fb0c979aa9f0ba7c:
entities/koordinator/outbox/KOO__SECE-r01-simulator-design-D1D2D3-correction__KOD.md

blob:
b54e5883a7fe8ac0ea88209a26f496e754326bce

## Exact SHD NEEDS_REWORK

puev5691/wellbeing-hq@1029c15789e546270c77cf8c33ac9a92bd377071:
entities/shardovik/outbox/SHD__SECE-r01-offline-simulator-design-successor-review__KOO.md

blob:
1114d4ab99ccdd1d948cd940da6c36bb503e7654

terminal:
NEEDS_REWORK_SHD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_SUCCESSOR_REVIEW

## Exact predecessor package

puev5691/wellbeing-hq@5b9642fe5915386518ea0d3a7d9f2b9ee6376469:
entities/koder/outbox/sece-r01-offline-simulator-design-successor/

tree:
6f3056ac669377c4dc0211d34da7d321ea75836c

Relevant predecessor blobs:
- FIXTURE-SCHEMA.json — 8a414eece84c924670e1d14431e85692d1c4381f
- FIXTURE-CATALOG.json — 7e39b90736c6d84f75a4581c46de7bd9baa34c99
- TRACE-SCHEMA.json — 07002d5cf5ffdd15aa9947d620ded69bc0384719
- SIMULATOR-ARCHITECTURE.md — d5cb5dc2be66db94af3c46be769d5261b5d08927
- MANIFEST.md — 01961a2ba2d8577430e00c5b327c283c07dcd708

Unchanged predecessor architecture artifacts remain referenced by those immutable identities and are not silently reconstructed.

## D1 — fixture schema closure

OLD:
- one generic fixture schema;
- nested input/expected objects open;
- executable meaning depended on ad-hoc free-form keys/strings.

NEW:
- family discriminator is mandatory: T | CXT | O | P | MUTATION;
- each family has a closed semantic_input and expected schema;
- semantic nested objects use additionalProperties:false;
- machine vocabulary is closed through enums for:
  facts/states,
  validator predicates,
  current-state evidence states,
  causal-event lifecycle states,
  trigger/change types,
  aggregation rules/outcomes,
  mutation transformations,
  assertion types,
  UNKNOWN/conflict states;
- affected_scopes, invalidated_bindings, recomputed_bindings, preserved_bindings are explicit;
- successor-context assertions are explicit;
- mutation transformations are typed enums, not free-form commands;
- descriptions/provenance remain non-executable human/evidence metadata only.

A corrected typed FIXTURE-CATALOG is included because the predecessor catalog representation could not validate against the closed schema without hidden conventions.

All 54 fixture IDs/families/descriptions/rule refs/provenance are preserved.
Each corrected record references predecessor catalog commit/blob/fixture ID and predecessor expected-semantic digest.

Marker:
D1_FIXTURE_SCHEMA_CLOSED=YES

## D2 — contract identity closure

OLD:
contract_id bound only effective_context_id + selected_scope + action_id + projection_basis.

NEW:
contract_id =
SHA-256(
  "sece-execution-contract-r01\0"
  + canonical_complete_SECE_EXECUTION_CONTRACT_R01_payload_without_contract_id
)

Only contract_id is removed before hashing.
No other field is excluded.

The identity therefore binds the full ACTION_INTENT and the complete contract payload, including all C1/C2/C3, ALLOWED/FORBIDDEN, preconditions, STOP_IF, result/terminal/next-gate, provenance/validation and predecessor top-level fields.

Canonicalization defines stable object-key ordering and stable ordering for schema-declared set-like arrays.
No circular identity.

Marker:
D2_CONTRACT_ID_FULL_PAYLOAD_BOUND=YES

## D3 — trace schema closure

OLD:
trace schema omitted recomputed bindings, context delta identity, full L6 projection identity/basis, classified result identity/state, synthetic event/result verification identity and next-gate derivation refs.

NEW:
trace_id is REQUIRED.

Trace requires, at minimum:
- input_context_id/version;
- triggering event/result;
- affected_scopes;
- invalidated_bindings;
- recomputed_bindings;
- preserved_bindings;
- context_delta_id;
- resulting_context_id;
- contract_id;
- projected_effective_context_id/version;
- projection_scope;
- projection_basis[];
- context_dependency_refs[];
- validator predicate set;
- aggregation_id/rule/outcome/reasons;
- classified_result_id/state;
- synthetic event/result id/type/verification_state;
- next_gate_class;
- next_gate_derivation_refs[];
- expected_vs_actual.

trace_id =
SHA-256(
  "sece-simulator-trace-r01\0"
  + canonical_complete_trace_payload_without_trace_id
)

Only trace_id is removed.
Trace remains returned data only; no storage/network sink is implied.

Marker:
D3_TRACE_SCHEMA_CLOSED=YES

## Explicitly unchanged

Not reopened:
- L0-L9;
- Effective Context semantics;
- CONTEXT_DELTA semantics;
- C1/C2/C3;
- MULTI_OUTCOME_AGGREGATION;
- T/CXT/O/P/M fixture meanings;
- Task Conveyor;
- Recovery;
- current-writer boundaries;
- authority semantics;
- no-side-effect simulator boundary.

No runtime implementation is present in this correction.
