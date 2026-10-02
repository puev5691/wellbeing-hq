# Durable continuity causal events
status: CANDIDATE_NOT_ACTIVE

TASK_MATERIALIZED: exact task/authority/input/currentness boundary durable.
TASK_ACTIVATION_REQUESTED: request only; not processing.
PROCESSING_STARTED: separate durable event after boundary predicate PASS.
CHECKPOINT_DURABLE: exact execution step/state persisted/read back.
RESULT_PENDING: exact result locator durable; terminal absent.
TERMINAL_PUBLISHED: terminal result durable; does not imply receipt/acceptance/next task.
NEXT_DISPOSITION_MATERIALIZED: one durable disposition class + provenance.
INSTANCE_UNAVAILABLE: processing instance unavailable; does not infer crash extent.
REPLACEMENT_WRITER_ESTABLISHED: writer authority established; does not resume task.

Ordering:
TASK_MATERIALIZED precedes PROCESSING_STARTED.
ACTIVATION_REQUESTED may precede PROCESSING_STARTED but never implies it.
CHECKPOINT_DURABLE requires PROCESSING_STARTED.
RESULT_PENDING requires STARTED/CHECKPOINTED causal basis.
TERMINAL_PUBLISHED requires result/terminal criterion, not merely dispatch.
NEXT_DISPOSITION_MATERIALIZED is required for continuity-complete terminal under candidate invariant.

Publication, dispatch, inbox, receipt, activation request and processing start remain distinct events.
