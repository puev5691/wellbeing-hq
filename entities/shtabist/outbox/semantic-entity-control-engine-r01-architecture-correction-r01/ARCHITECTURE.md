# SECE r0.1 — Architecture C1/C2/C3 correction
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
predecessor_architecture_blob: 5446206cd2413db76c46d2a5ceff4b3d585f3354

L0-L9 unchanged. Only local precision edits:

L3 CURRENT STATE + EVENT/TASK BINDING now outputs:
CURRENT_STATE_EVIDENCE[] with exact scope/evidence relations and CAUSAL_EVENTS[] for current event/decision/handoff state.
Selection of current state is exact-scope/evidence based. Recovery never automatically outranks verified delta. Missing required basis=UNKNOWN; unresolved conflict=STOP.

L6 SEMANTIC_EXECUTION_CONTRACT now contains ACTION_AUTHORIZATION_BINDINGS[], CAUSAL_EVENTS[], CURRENT_STATE_EVIDENCE[].

L7 STATIC VALIDATOR additionally:
- validates every authority-sensitive proposed action through exact ACTION→RULE→ACTIVE SOURCE→AUTHORITY→TASK/STATE binding;
- rejects absent/stale/conflicted/scope-mismatched/task-mismatched binding;
- evaluates dispatch/delivery/receipt/processing separately;
- rejects redundant self-handoff from explicit decision/handoff fields;
- selects current-state basis only from explicit CURRENT_STATE_EVIDENCE.

L8 RUNTIME GUARD revalidates the selected current-state evidence and per-action authorization binding before each consequential effect.

L9 RESULT/NEXT-GATE uses explicit CAUSAL_EVENTS and causal_requirement_status. Narrative next action is not validator state.

All accepted architecture boundaries remain unchanged.
