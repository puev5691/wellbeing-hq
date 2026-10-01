# EFFECTIVE_CONTEXT schema for SECE r0.1 simulator design

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
schema_id: SECE_EFFECTIVE_CONTEXT_R01

## Required top-level fields

- context_id: deterministic immutable identity.
- context_version: fixture-local monotonic semantic version, not wall-clock.
- entity: stable Entity identity.
- instance: current replaceable instance identity/evidence ref.
- role: role/profile binding identity.
- active_source_set[].
- semantic_invariants[].
- current_state_evidence[].
- selected_current_basis_by_scope[].
- current_tasks[].
- authority_bindings[].
- profile.
- experience_set[].
- capability_set[].
- causal_events[].
- human_input_facts[].
- unknown_facts[].
- conflict_set[].
- context_corrections[].
- derived_bindings[].
- provenance[].
- scope_index[].
- dependency_graph[].
- prior_context_ref.
- context_delta_ref.

## Common semantic-line envelope

Every fact/binding object must carry:

- id
- exact_scope
- semantic_type
- value/state payload
- provenance[]
- applicability: APPLICABLE|NOT_APPLICABLE|UNKNOWN
- epistemic_state: VERIFIED|UNVERIFIED|UNKNOWN|CONFLICT
- lifecycle_state where applicable
- authority_effect_state where applicable
- dependencies[]

The four axes are never flattened.

## selected_current_basis_by_scope[]

Each:
- scope
- selected_evidence_id
- selection_basis
- unresolved_conflict: YES|NO
- provenance[]

No selected basis may be reconstructed from memory, filename recency or list order.

## active_source_set[]

Each:
- source_id
- locator
- version_blob
- active_status: ACTIVE|CANDIDATE|HISTORICAL|UNKNOWN
- semantic_basis
- conflict_status
- provenance[]

CANDIDATE/HISTORICAL/UNKNOWN does not become normative ACTIVE.

## current_state_evidence[]

Preserves reviewed CURRENT_STATE_EVIDENCE structure:
- evidence_id
- evidence_kind
- exact_immutable_identity
- scope
- provenance_source
- verified_state
- currentness_state
- relation_to_other_evidence
- relation_target_evidence_id
- selected_current_basis
- selection_basis
- unresolved_conflict
- conflict_set[]
- unknown_fields[]

## current_tasks[]

Each:
- task_ref
- task_version
- scope
- task_status/currentness
- supersession_state
- provenance[]

Historical/inbox/recovery/capability never creates CURRENT task.

## authority_bindings[]

Includes both externally grounded authority evidence and derived ACTION_AUTHORIZATION_BINDINGS, with clear type field.

ACTION_AUTHORIZATION_BINDING preserves:
- action_id
- action_class
- disposition
- compiled_rule_id
- source_locator
- source_version_blob
- authority_ref
- authority_scope
- authority_action_classes[]
- task_binding
- task_currentness_requirement
- writer_requirement
- production_or_effect_authority_requirement
- provenance_status
- conflict_status

Derived binding is not authority; it points to exact authority.

## profile / experience / capability

Profile:
- profile_id
- selection_basis
- scope
- provenance

Experience item:
- ref
- provenance
- applicability
- freshness
- reason_loaded
- advisory_only: true

Capability item:
- capability_id
- scope
- availability_state
- provenance

None of these may populate authority by themselves.

## causal_events[]

Preserves reviewed CAUSAL_EVENTS structure, including:
event/lifecycle/dispatch/delivery/receipt/processing_started/handoff/decision fields,
redundant_self_handoff and causal_requirement_status.

## human_input_facts[]

Each:
- input_id
- claimed_fact
- scope
- authority_status
- evidence_status
- provenance

Unauthorized human input may coexist but cannot overwrite verified state.

## unknown_facts[]

Each:
- unknown_id
- required_for[]
- exact_scope
- missing_evidence_description
- request_permitted
- provenance

UNKNOWN is never promoted to YES/NO.

## conflict_set[]

Each:
- collision_id
- collision_type
- exact_scope
- involved_ids[]
- unresolved
- dependent_binding_ids[]
- provenance[]

Difference across independent scopes is not conflict.

## context_corrections[]

Each:
- correction_id
- collision_id/type
- affected_scope
- affected_atom_binding_ids[]
- transformation
- retained_fact_ids[]
- unresolved_state
- provenance[]

Corrections never rewrite prior context.

## derived_bindings[]

Each:
- binding_id
- binding_type
- exact_scope
- source_atom_ids[]
- dependency_ids[]
- computed_state
- provenance[]

A dependency change invalidates all dependent bindings.

## scope_index[]

Canonical mapping:
scope_id -> atom_ids[], evidence_ids[], binding_ids[], task_refs[], authority_binding_ids[], conflict_ids[].

## dependency_graph[]

Each:
- dependency_id
- source_atom_ids[]
- source_evidence_ids[]
- derived_binding_ids[]
- scopes[]

Graph traversal defines affected-scope recomputation.

## Identity

context_id is a deterministic digest of canonical context payload excluding context_id itself.
context_version is semantic fixture sequence (for example 0,1,2), not time.

No field inclusion creates authority.
