# SECE r0.1 Context Delta
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

Transition:
Context(n) + VERIFIED Event/Result -> CONTEXT_DELTA -> Context(n+1).

CONTEXT_DELTA fields:
delta_id
parent_context_id
triggering_event_or_result_ref
added_facts[]
removed_or_superseded_facts[]
refined_facts[]
new_unknowns[]
resolved_unknowns[]
new_conflicts[]
resolved_conflicts[]
changed_scopes[]
invalidated_bindings[]
recomputed_bindings[]
preserved_unaffected_bindings[]
provenance[]
resulting_context_id

Affected-scope recomputation:
1 identify changed atoms/evidence;
2 determine exact touched scopes;
3 traverse dependency_graph to dependent derived bindings;
4 invalidate all bindings depending on changed dependency;
5 recompute only invalidated bindings from current inputs/rules;
6 retain unaffected bindings byte/logically unchanged by reference;
7 emit new immutable context version and delta.

No stale dependent binding may survive dependency change.
No full-context reset merely because one fact changed.
Prior context remains immutable evidence.
Memory cannot reconstruct missing current basis.
