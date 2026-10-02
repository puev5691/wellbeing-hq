# SECE r0.1 simulator fixture input-completeness derivation specification

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
correction_scope: INPUT_COMPLETENESS_ONLY
project_time: omitted

## Chosen mechanism

Chosen bounded mechanism:
A — explicit typed synthetic initial state embedded in affected fixture input.

No base_context_ref and no external lookup are required.

Binding IDs are fixture data only.
They are not a Project naming convention and are not derived from their textual spelling.

## New typed input object

Affected fixtures receive:

binding_derivation_input:
- changed_source_ids[]
- initial_state

initial_state:
- state_id
- schema_version = SECE_SYNTHETIC_BINDING_STATE_R01
- initial_derived_bindings[]
- dependency_edges[]
- scope_index[]
- recomputation_rules[]
- provenance_ref

### InitialDerivedBinding

- binding_id
- binding_type
- exact_scope
- dependencies[]
- current_state
- provenance_ref
- semantic_role:
  INVALIDATABLE_DEPENDENT | PRESERVED_UNAFFECTED
- recomputation_rule_ref | null

### DependencyEdge

- edge_id
- source_atom_or_evidence_id
- dependent_binding_id
- exact_scope
- relation_type = DEPENDS_ON
- provenance_ref

### ScopeIndexEntry

- scope_id
- atom_ids[]
- evidence_ids[]
- binding_ids[]
- child_scopes[]

### RecomputationRule

- rule_id
- input_binding_ids[]
- output_binding_id
- exact_scope
- output_binding_type
- output_state
- provenance_ref

All semantic nested structures are closed with additionalProperties:false.

## Generic derivation algorithm

The same algorithm applies to all affected fixtures.

Input:
binding_derivation_input only.

1. changed = set(changed_source_ids).
2. invalidated = empty set.
3. Traverse dependency_edges.
4. If an edge source is in changed or is itself an invalidated binding, add its dependent_binding_id to invalidated.
5. Repeat traversal until fixed point.
6. For every invalidated InitialDerivedBinding with recomputation_rule_ref:
   - resolve that rule from initial_state.recomputation_rules;
   - require all rule.input_binding_ids to be invalidated;
   - add rule.output_binding_id to recomputed.
7. preserved =
   all initial_derived_bindings.binding_id not in invalidated.
8. Canonically sort the three output sets.
9. Return:
   invalidated_bindings[],
   recomputed_bindings[],
   preserved_bindings[].

Only after this actual computation may FixtureOracle compare actual sets with expected sets.

## Explicit anti-cheat boundary

The derivation algorithm does NOT read:
- expected.invalidated_bindings
- expected.recomputed_bindings
- expected.preserved_bindings
- fixture_id
- description
- architecture prose

It contains no:
- fixture-specific switch/case;
- scope/change -> binding-ID lookup table;
- binding-ID naming parser;
- hidden external state.

Exact binding IDs enter computation only because they are explicitly present in typed fixture initial state, dependency edges and recomputation rules.

## M6/M8

M6 and M8 now contain non-null binding_derivation_input.initial_state.

Computation is therefore:

typed BASE_STATE
+ typed transformation source/change
-> changed_source_ids
-> dependency traversal
-> invalidated
-> typed recomputation rule
-> recomputed
-> remaining initial bindings
-> preserved.

No M6/M8-specific implementation branch is required.

## Preservation

D2 contract identity:
unchanged, exact reviewed blob 7339655c132459f87a1943f4f825d45b497108e3.

D3 trace semantics:
unchanged, exact reviewed TRACE-SCHEMA blob 0876cff31d1e4b54b065933aa74129e591c78e94.

No L0-L9 / Effective Context / CONTEXT_DELTA / C1-C3 / MULTI_OUTCOME_AGGREGATION semantic change is introduced.

INPUT_COMPLETENESS_CORRECTION_CLOSED=YES
ORACLE_NOT_USED_AS_COMPUTATIONAL_INPUT=YES
NO_FIXTURE_ID_BRANCHING_REQUIRED=YES
NO_HIDDEN_BINDING_ID_MAPPING_REQUIRED=YES
