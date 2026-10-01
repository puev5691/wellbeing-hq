# SECE_EXECUTION_CONTRACT_R01 projection clarification
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
basis: outcome aggregation schema blob cb8bea18e6fc132f789eabcd933719a8a8a98da4

All existing C1/C2/C3 and outcome aggregation fields remain unchanged.

Add mandatory projection identity:
effective_context_id
effective_context_version
selected_scope
projection_basis[] {context_atom_or_binding_id, exact_scope, provenance_ref, reason_used}
context_dependency_refs[]
projection_created_for_action_id

Contract = bounded derived projection of EFFECTIVE_CONTEXT for ONE next-step candidate.

Contract is NOT:
entire Entity memory;
entire semantic context;
authority source;
permanent state;
Recovery replacement;
Task Conveyor replacement;
current-writer replacement;
source-set replacement.

Projection cannot introduce a fact/binding absent from effective context except the proposed action itself, which remains proposal until validation.
