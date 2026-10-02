# Durable execution-state transitions
status: CANDIDATE_NOT_ACTIVE

TASK_MATERIALIZED creates NOT_STARTED only after durable boundary fields verify.
NOT_STARTED -> STARTED only via durable PROCESSING_STARTED event and fresh task/authority/currentness/writer checks.
STARTED -> CHECKPOINTED via CHECKPOINT_DURABLE with exact step/resulting state identity.
STARTED/CHECKPOINTED -> RESULT_PENDING when result artifact/locator is durable but terminal not yet established.
RESULT_PENDING -> TERMINAL only with durable terminal evidence and durable next causal disposition.
Any active state -> BLOCKED on exact blocker while preserving prior checkpoint.
Any required currentness/evidence ambiguity -> UNKNOWN; no replay.
Superseded task -> BLOCKED/SUPERSEDED disposition; no resume.
Replacement writer establishment alone causes no START/RESUME transition.

No automatic replay by default.
