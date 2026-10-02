# SHT → KOO: CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP r0.1 result

status: CANDIDATE_NOT_ACTIVE
terminal: PASS_SHT_CHAT_INFOFIELD_MATERIALIZATION_GAP_R01_CANDIDATE_READY_FOR_REVIEW

Package:
entities/shtabist/outbox/chat-infofield-materialization-gap-r01/

Blobs:
ARCHITECTURE.md 40af4b9ab1988bde479de67b7c50087849fe6128
DURABLE-EXECUTION-STATE.md e7942ae00ddbbcc07df9b576e68b54d11c0dd267
STATE-TRANSITIONS.md 812aa29b1570b7212cf8e9d4e010a8ca559f2411
CRASH-REPLACEMENT-MATRIX.md 8d1cc3d4800f676cb6bc069db6e64386d67a5e80
CAUSAL-EVENTS.md f452f16bc1e60674a05b4e02720bcd305ede11d3
INVARIANTS.md b2a31e3b54a8626a6fa83cbf787ff2af1b5a6af1
FIXTURES.md dcbbb6b7bee3a2e6512af60bc544148145ca35fb
SOURCE-IMPACT.md 9c03230a9820c0383978ce685c1a46eaf72c394e
NEXT-GATES.md 9d6e4804b3e41cd299d9aa77e0d38f0efbc16a53
MANIFEST.md 198b5d341f4c773a4c52ec4f57cd26ea4c3b25e8

Invariant verdicts:

NO_PROCESSING_BEFORE_DURABLE_TASK_BOUNDARY:
REVISE.
Adopt revised machine predicate DURABLE_TASK_BOUNDARY_READY requiring exact durable task+authority+writer/instance where required+currentness+inputs+stop/terminal+processing instance+durable execution-state readback before PROCESSING_STARTED=YES.

NO_TERMINAL_STOP_WITHOUT_NEXT_CAUSAL_ACTION:
REJECT.

Replacement:
TERMINAL_REQUIRES_DURABLE_NEXT_CAUSAL_DISPOSITION:
ACCEPT.

Disposition classes:
NEXT_AUTHORIZED_TASK
WAITING_EXACT_TASK
WAITING_OPERATOR_DECISION
BLOCKED
NO_FURTHER_ACTION
UNKNOWN_REQUIRES_RECONCILIATION.
Disposition creates no task authority.

Durable execution state:
DURABLE_EXECUTION_STATE_R01 recommended as distinct candidate layer between durable task authority and mutable chat working context.
Chat may cache/display it but cannot be authoritative.

Crash/replacement:
no automatic replay.
STARTED without checkpoint => UNKNOWN_REQUIRES_RECONCILIATION.
CHECKPOINTED => bounded resume candidate only from exact checkpoint after fresh authority/currentness/writer validation.
RESULT_PENDING => continue result validation/fixation only, no profile replay by default.
TERMINAL => no resume; consume durable next disposition.
chat-only/unmaterialized => UNKNOWN, DO_NOT_RECONSTRUCT, DO_NOT_REPLAY.
replacement writer alone => no predecessor resume.
superseded => no resume.

Causal events explicitly separate TASK_MATERIALIZED, TASK_ACTIVATION_REQUESTED, PROCESSING_STARTED, CHECKPOINT_DURABLE, RESULT_PENDING, TERMINAL_PUBLISHED, NEXT_DISPOSITION_MATERIALIZED, INSTANCE_UNAVAILABLE, REPLACEMENT_WRITER_ESTABLISHED.

GAP1-GAP10: PASS machine-decidable under candidate.

Source impact:
no active source changed.
Likely future review surfaces: Task Conveyor v1.2 first, Recovery v1.6 integration boundary second; Project Core only if global elevation is chosen. File Work mechanics appear reusable. Reviewed SECE unchanged.

Historical KOD v0.6 chat-only work:
NOT RECONSTRUCTED.
NOT REPLAYED.
UNKNOWN remains UNKNOWN.

Exact next gate:
KAN independent normative/source-impact review of this candidate only.

## EXPERIENCE
Idea → continuity requires durable execution evidence between task creation and terminal, not faith in chat history.
Probe → crash/replacement matrix across not-started, started, checkpointed, result-pending, terminal and unmaterialized states.
Result → a distinct execution-state layer closes the observability gap without inventing replay.
Success → GAP1-GAP10 become machine-decidable candidate behavior.
Lesson → “the task existed” and “the task was being executed” are different durable facts; if the second is not recorded, replacement must not guess it.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
