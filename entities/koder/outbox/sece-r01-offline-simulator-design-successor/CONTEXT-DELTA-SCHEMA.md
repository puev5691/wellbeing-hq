# CONTEXT_DELTA schema for SECE r0.1 simulator design

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
schema_id: SECE_CONTEXT_DELTA_R01

## Required fields

- delta_id
- parent_context_id
- triggering_event_or_result_ref
- added_facts[]
- removed_or_superseded_facts[]
- refined_facts[]
- new_unknowns[]
- resolved_unknowns[]
- new_conflicts[]
- resolved_conflicts[]
- changed_scopes[]
- invalidated_bindings[]
- recomputed_bindings[]
- preserved_unaffected_bindings[]
- provenance[]
- resulting_context_id

## Deterministic construction

1. Accept only a fixture-declared verified RESULT/EVENT as trigger.
2. Resolve changed atoms/evidence.
3. Determine exact touched scopes.
4. Traverse dependency_graph from changed IDs.
5. invalidated_bindings = complete dependency closure affected by change.
6. recomputed_bindings = deterministic re-evaluation of invalidated bindings only.
7. preserved_unaffected_bindings = prior bindings outside dependency closure, preserving identity/reference.
8. New/resolved UNKNOWN/conflict entries are exact-scope changes only.
9. Build successor context.
10. resulting_context_id must equal deterministic identity of successor context.
11. Compute delta_id from canonical delta content excluding delta_id and resulting_context_id circular fields according to the identity rule in SIMULATOR-ARCHITECTURE.

## Invariants

- No stale binding depending on a changed dependency may appear in preserved_unaffected_bindings.
- No unaffected binding may be recomputed solely because another independent scope changed.
- No full reset unless dependency traversal explicitly reaches every scope/binding.
- Recovery/delta refinement is exact-scope only.
- Prior context remains immutable.
- Delta is derived representation, not authority.
- Delta cannot activate a source/canon or create writer/task/production authority.

## Event verification boundary

If triggering event/result is UNVERIFIED, UNKNOWN or CONFLICT:
- no applicable successor delta is emitted;
- trace records reason;
- parent context remains current input context for the simulation branch.

## Provenance

Every added/removed/refined/unknown/conflict/binding entry references:
- triggering event/result;
- changed atom/evidence IDs;
- dependency edges used;
- source/evidence provenance.
