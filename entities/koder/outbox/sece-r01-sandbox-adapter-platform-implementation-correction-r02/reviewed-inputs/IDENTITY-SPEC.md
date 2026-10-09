# SECE r0.1 simulator D2/D3 deterministic identity specification

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Canonicalization

Canonical serialization is UTF-8 JSON with:
- object keys sorted lexicographically recursively;
- no whitespace dependence;
- schema-declared set-like arrays sorted by stable semantic key;
- arrays not declared set-like preserve schema order;
- no wall-clock/random/process fields are injected.

Set-like contract arrays normalized before hashing:
projection_basis, context_dependency_refs,
ACTION_AUTHORIZATION_BINDINGS, CAUSAL_EVENTS, CURRENT_STATE_EVIDENCE,
AUTHORITY_BASIS, SOURCE_SET, INPUTS, EXPERIENCE_SET,
ALLOWED_ACTIONS, FORBIDDEN_ACTIONS, REQUIRED_PRECONDITIONS,
STOP_IF, EXPECTED_TERMINAL, NEXT_GATE_RULE, PROVENANCE, CAPABILITIES.

## D2 — contract_id

Domain separator:
`sece-execution-contract-r01\0`

Rule:

`contract_id = SHA-256(domain_separator + canonical_complete_contract_payload_without_contract_id)`

The payload is the complete SECE_EXECUTION_CONTRACT_R01 object after removing ONLY `contract_id`.
No other field is excluded.

Therefore the identity binds, at minimum:
- effective_context_id/version;
- selected_scope;
- projection_basis[];
- context_dependency_refs[];
- full ACTION_INTENT including parameters/content beyond action_id;
- ACTION_AUTHORIZATION_BINDINGS[];
- CAUSAL_EVENTS[];
- CURRENT_STATE_EVIDENCE[];
- ALLOWED_ACTIONS[];
- FORBIDDEN_ACTIONS[];
- REQUIRED_PRECONDITIONS[];
- STOP_IF[];
- EXPECTED_RESULT;
- EXPECTED_TERMINAL[];
- NEXT_GATE_RULE[];
- provenance and VALIDATION_STATE;
- predecessor top-level semantic fields such as CURRENT_STATE, TASK_IDENTITY, AUTHORITY_BASIS, SOURCE_SET, INPUTS, PROFILE, EXPERIENCE_SET, CAPABILITIES;
- every other field present in the contract object.

There is no circular identity because contract_id is removed before canonicalization/hash.

D2_CONTRACT_ID_FULL_PAYLOAD_BOUND=YES

## Contract identity validation

Base vector contract_id:
7b819fb3ac464c226b83fbc4fe9fddb1a40b90a6b3f5c35c11d5078347e4ab6f

Identical canonical copy:
7b819fb3ac464c226b83fbc4fe9fddb1a40b90a6b3f5c35c11d5078347e4ab6f

Identical IDs:
YES

Mutation matrix field classes:
- effective_context_version: DIFFERENT_ID
- selected_scope: DIFFERENT_ID
- projection_basis: DIFFERENT_ID
- context_dependency_refs: DIFFERENT_ID
- full_ACTION_INTENT: DIFFERENT_ID
- ACTION_AUTHORIZATION_BINDINGS: DIFFERENT_ID
- CAUSAL_EVENTS: DIFFERENT_ID
- CURRENT_STATE_EVIDENCE: DIFFERENT_ID
- ALLOWED_ACTIONS: DIFFERENT_ID
- FORBIDDEN_ACTIONS: DIFFERENT_ID
- REQUIRED_PRECONDITIONS: DIFFERENT_ID
- STOP_IF: DIFFERENT_ID
- EXPECTED_RESULT: DIFFERENT_ID
- EXPECTED_TERMINAL: DIFFERENT_ID
- NEXT_GATE_RULE: DIFFERENT_ID
- PROVENANCE: DIFFERENT_ID
- VALIDATION_STATE: DIFFERENT_ID
- TASK_IDENTITY: DIFFERENT_ID
- AUTHORITY_BASIS: DIFFERENT_ID
- SOURCE_SET: DIFFERENT_ID
- INPUTS: DIFFERENT_ID
- PROFILE: DIFFERENT_ID
- EXPERIENCE_SET: DIFFERENT_ID
- CAPABILITIES: DIFFERENT_ID
- CURRENT_STATE: DIFFERENT_ID

CONTRACT_ID_COLLISION_BY_OMITTED_SEMANTIC_FIELD_PREVENTED=YES

## D3 — trace_id

Domain separator:
`sece-simulator-trace-r01\0`

Rule:

`trace_id = SHA-256(domain_separator + canonical_complete_trace_payload_without_trace_id)`

Only trace_id is removed. All causal/recomputation/delta/projection/validator/aggregation/result/next-gate/oracle fields remain bound.

Trace is returned data only. Identity does not imply persistence/storage/network sink.

D3_TRACE_SCHEMA_CLOSED=YES
