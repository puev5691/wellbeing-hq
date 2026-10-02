# Continuity materialization invariants r0.1
status: CANDIDATE_NOT_ACTIVE

I1 NO_PROCESSING_BEFORE_DURABLE_TASK_BOUNDARY
VERDICT: REVISE.

Reason: intent is correct, but “durable task boundary” must be a closed predicate, not mere task-file existence.

Revised invariant:
PROCESSING_STARTED_MAY_BECOME_YES only if DURABLE_TASK_BOUNDARY_READY=YES.

DURABLE_TASK_BOUNDARY_READY =
task_id present
AND exact task locator/version/blob verified
AND authority_ref/identity verified and scope covers task
AND writer/instance identity verified where writer is required
AND task_currentness=CURRENT
AND no applicable supersession/conflict
AND required input identities verified
AND stop_conditions + expected_terminal recorded
AND processing_instance_identity recorded
AND durable execution-state object successfully materialized/read back.

Inbox/publication/dispatch/activation_requested never satisfy this predicate.

I2 NO_TERMINAL_STOP_WITHOUT_NEXT_CAUSAL_ACTION
VERDICT: REJECT.

Reason: valid terminal may end in waiting, blocked, no further action, or reconciliation. Requiring an action can manufacture authority.

Replacement:
TERMINAL_REQUIRES_DURABLE_NEXT_CAUSAL_DISPOSITION
VERDICT: ACCEPT.

Predicate:
TERMINAL_COMPLETE_FOR_CONTINUITY =
terminal evidence durable
AND next_causal_disposition in {
 NEXT_AUTHORIZED_TASK,
 WAITING_EXACT_TASK,
 WAITING_OPERATOR_DECISION,
 BLOCKED,
 NO_FURTHER_ACTION,
 UNKNOWN_REQUIRES_RECONCILIATION
}
AND disposition provenance/materialization verified.

NEXT_AUTHORIZED_TASK additionally requires its own exact task+authority identity. Disposition record itself creates no task authority.
