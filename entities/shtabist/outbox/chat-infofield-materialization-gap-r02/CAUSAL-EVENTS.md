# r0.2 continuity causal events
status: CANDIDATE_NOT_ACTIVE

TASK_MATERIALIZED: exact durable task boundary/attempt identity.
TASK_ACTIVATION_REQUESTED: request only.
PROCESSING_STARTED: separately evidenced entry of exact actor/instance into exact execution_attempt; not proof of external operation completion.
CHECKPOINT_DURABLE: task-progress evidence after PROCESSING_STARTED, with exact covered prefix/evidence scope.
PRE_EFFECT_INTENT_MATERIALIZED: exact operation identity/intent before consequential effect; intent != execution/authority.
EFFECT_OUTCOME_EVIDENCED: separately evidenced external effect outcome.
EFFECT_OUTCOME_UNRESOLVED: explicit unresolved status when outcome cannot be proved.
RESULT_PENDING: exact pending result exists.
TERMINAL_PUBLISHED: actual task terminal criterion met and terminal evidence durable.
NEXT_DISPOSITION_MATERIALIZED: separate continuity disposition.
INSTANCE_UNAVAILABLE.
REPLACEMENT_WRITER_ESTABLISHED: writer fact only.

Publication/dispatch/inbox/receipt/activation_requested/readback do not prove PROCESSING_STARTED.
Receipt does not prove acceptance.
Terminal does not prove parent completion, receipt, acceptance, next-task authority or next disposition.
