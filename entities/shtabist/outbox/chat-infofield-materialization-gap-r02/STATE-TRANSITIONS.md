# r0.2 documentary state transitions
status: CANDIDATE_NOT_ACTIVE

TASK_MATERIALIZED + accepted initial state => INITIAL_NOT_STARTED.
INITIAL_NOT_STARTED + fresh eligibility + separate PROCESSING_STARTED evidence => STARTED.
STARTED + CHECKPOINT_DURABLE covering exact prefix => CHECKPOINTED.
STARTED/CHECKPOINTED may produce RESULT_PENDING only when an actual pending-result artifact/locator exists.
Any state may record TERMINAL when its declared task terminal criterion is actually met; RESULT_PENDING is not mandatory.
Terminal PASS/FAIL/BLOCKED are allowed according to actual criterion.

TERMINAL and NEXT_DISPOSITION are independent facts.
TERMINAL_COMPLETE_FOR_CONTINUITY is derived after both are verified.
NEXT_DISPOSITION_MISSING does not undo TERMINAL.

Any required evidence/currentness ambiguity => UNKNOWN/BLOCK dependent transition.
Superseded task => no resume of superseded execution.
Replacement writer alone => no resume.

Pre-start materialization is INITIAL_NOT_STARTED, never CHECKPOINT_DURABLE.
