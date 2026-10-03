# r0.2 crash/replacement matrix
status: CANDIDATE_NOT_ACTIVE

Initial accepted NOT_STARTED, no start event:
processing not proven. Start candidate only after fresh eligibility/currentness/authority. Absence of later event alone does not prove historical non-execution outside recorded frontier.

STARTED, crash before checkpoint:
post-start execution/effect extent UNKNOWN. No automatic replay/resume. Reconcile effect evidence/currentness.

CHECKPOINTED:
checkpoint proves only exact covered prefix. Any possible post-checkpoint tail remains UNKNOWN. Resume/retry overlapping affected tail blocked until tail/external-effect outcome reconciled. Completed prefix not replayed.

Consequential effect:
require PRE_EFFECT_INTENT_MATERIALIZED plus later EFFECT_OUTCOME_EVIDENCED or EFFECT_OUTCOME_UNRESOLVED. Crash between effect and post-effect checkpoint => unresolved; no replay. Intent is not execution or authority.

RESULT_PENDING:
continue result validation/fixation only when exact pending artifact exists/current. Do not invent pending artifact.

TERMINAL:
terminal fact preserved immediately. Missing next disposition => NEXT_DISPOSITION_MISSING; reconciliation only for disposition dependency; no profile replay.

Chat-only/unmaterialized:
UNKNOWN / NOT_MATERIALIZED; no reconstruction/replay.

Replacement writer + unknown currentness:
no resume/replay; reconcile.

Superseded task:
no resume; preserve evidence; successor needs separate authority.

No exactly-once, RECOVERY_READY, admitted shard/storage durability or production durability is claimed.
