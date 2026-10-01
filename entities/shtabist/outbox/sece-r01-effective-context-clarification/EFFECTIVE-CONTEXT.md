# SECE r0.1 EFFECTIVE_CONTEXT
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

EFFECTIVE_CONTEXT is the immutable-versioned coherent derived context after L1-L5 composition and before L6 projection. It is not authority, Recovery, memory, Task Conveyor, or a winner-takes-all state.

Fields:
context_id; context_version; entity; instance; role;
active_source_set[];
semantic_invariants[];
current_state_evidence[];
selected_current_basis_by_scope[];
current_tasks[] {task_ref, scope, currentness};
authority_bindings[];
profile;
experience_set[];
capability_set[];
causal_events[];
human_input_facts[];
unknown_facts[];
conflict_set[];
context_corrections[];
derived_bindings[];
provenance[];
scope_index[];
dependency_graph[] {dependency_id, source_atom_ids[], derived_binding_ids[], scopes[]};
prior_context_ref;
context_delta_ref.

Every fact/binding preserves exact scope, semantic type, provenance, applicability, epistemic state, lifecycle state, authority/effect state. These axes are never flattened.

Independent scopes coexist. EFFECTIVE_CONTEXT may simultaneously contain allowed possibilities, prohibitions, UNKNOWN and evidence requirements.

No field inclusion creates authority or source effectivity.
