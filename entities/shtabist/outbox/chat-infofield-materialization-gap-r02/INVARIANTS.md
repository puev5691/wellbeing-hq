# CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP r0.2 invariants
status: CANDIDATE_NOT_ACTIVE

I1 NO_PROCESSING_BEFORE_DURABLE_TASK_BOUNDARY — REVISED.
Boundary PASS means processing is ELIGIBLE only; it is not start evidence.

DURABLE_TASK_BOUNDARY_READY requires exact task-attempt identity, verified task locator/version/blob, authority established for proposed transition, exact actor/processing instance, task currentness/supersession check, required input identities, stop/terminal criteria, initial execution-state identity/version, and accepted/read-back current state frontier.

PROCESSING_STARTED requires a separate causal event for the exact execution_attempt and actor/instance. Scheduling, publication, dispatch, inbox, activation_requested, boundary readback do not prove it.

Missing start evidence => PROCESSING_NOT_PROVEN / UNKNOWN.
NOT_STARTED requires explicit accepted initial NOT_STARTED state for exact attempt plus verified current event/state frontier.
Missing/unverifiable authority => AUTHORITY_NOT_ESTABLISHED for proposed transition; no historical negative assertion, no reconstruction, no execution.

WRITER_NOT_REQUIRED_FOR_TASK remains valid where active Recovery permits independently authorized worker/read-only work. Writing authoritative execution state still requires applicable write authority.

I2 NO_TERMINAL_STOP_WITHOUT_NEXT_CAUSAL_ACTION — REJECTED.
Replacement retained:
TERMINAL_REQUIRES_DURABLE_NEXT_CAUSAL_DISPOSITION as continuity property, not task terminal criterion.

Task terminal evidence is recorded immediately when actual terminal criterion is met.
TERMINAL_COMPLETE_FOR_CONTINUITY = terminal_evidence_verified AND next_disposition_verified.
Missing disposition => NEXT_DISPOSITION_MISSING only; terminal remains terminal and profile replay is forbidden.

Disposition never creates task authority.
