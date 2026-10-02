# Crash / replacement matrix
status: CANDIDATE_NOT_ACTIVE

1 durable task, NOT_STARTED:
resume=no (nothing started); replay=no; new attempt=start candidate only after fresh authority/currentness/writer validation; reconciliation required before start if any state changed; UNKNOWN preserved; mandatory exact task+authority+currentness+writer/input evidence.

2 STARTED durable, crash before durable checkpoint:
resume=no; replay=no; new attempt=no by default; reconciliation=yes; execution extent after STARTED is UNKNOWN; require task/authority/currentness + evidence whether side effects occurred. Disposition UNKNOWN_REQUIRES_RECONCILIATION.

3 CHECKPOINTED durable:
bounded resume candidate=yes from exact checkpoint only after fresh authority/currentness/writer/input validation; replay completed prefix=no; new attempt=no by default; reconciliation=yes on replacement; UNKNOWN preserved for post-checkpoint unmaterialized work.

4 RESULT_PENDING durable, terminal absent:
resume profile execution=no by default; continue result-validation/fixation candidate only if exact pending result identity/readback and authority/currentness valid; no replay; reconciliation on replacement; terminal remains absent.

5 TERMINAL durable:
resume/replay=no; use durable next causal disposition. Missing disposition = continuity process defect requiring disposition materialization/reconciliation, not implicit next task.

6 chat-only/unmaterialized work:
resume=no; replay=no; new attempt only from a NEW separately authorized durable task; reconciliation=yes if operationally relevant; state UNKNOWN/NOT_MATERIALIZED; do not reconstruct.

7 replacement writer with task currentness UNKNOWN:
resume=no; replay=no; new attempt=no; reconciliation=yes; UNKNOWN preserved; writer establishment is insufficient.

8 task superseded during execution:
resume=no; replay=no; new attempt only under successor task authority; reconcile/preserve last checkpoint/result evidence; supersession mandatory.

No automatic replay.
