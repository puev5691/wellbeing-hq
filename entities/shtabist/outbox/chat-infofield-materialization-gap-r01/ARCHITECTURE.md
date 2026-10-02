# CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP architecture candidate
status: CANDIDATE_NOT_ACTIVE

Defect:
profile work can otherwise exist only inside a chat after conversational instruction and before durable terminal/checkpoint, making replacement unable to distinguish not-started, started, partially effected, result-pending and unknown work.

Candidate correction:
TASK durable boundary
-> DURABLE_EXECUTION_STATE NOT_STARTED
-> explicit PROCESSING_STARTED
-> bounded CHECKPOINT_DURABLE events
-> RESULT_PENDING when applicable
-> TERMINAL_PUBLISHED
-> NEXT_DISPOSITION_MATERIALIZED.

Chat is working surface/cache, never authoritative execution state.

This candidate complements but does not amend active Task Conveyor/Recovery/SECE. Effectivity would require separate normative review/approval/amendment decision.
