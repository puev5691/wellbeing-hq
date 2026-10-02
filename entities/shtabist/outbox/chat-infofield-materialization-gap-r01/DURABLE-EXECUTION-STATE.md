# DURABLE_EXECUTION_STATE_R01 candidate
status: CANDIDATE_NOT_ACTIVE

Recommendation: YES, distinct durable execution-state layer is required as candidate architecture.

Fields:
state_id; state_version;
task_id; task_locator; task_version_blob;
authority_ref; authority_identity;
writer_ref; writer_identity; instance_identity;
task_currentness;
processing_state: NOT_STARTED|STARTED|CHECKPOINTED|RESULT_PENDING|TERMINAL|BLOCKED|UNKNOWN;
processing_started_checkpoint;
current_execution_step;
last_durable_checkpoint;
pending_result_locator;
input_identities[];
supersession_evidence[];
crash_replacement_disposition;
chat_only_unmaterialized_work: NONE|UNKNOWN;
next_causal_disposition;
provenance[];
prior_state_ref.

Owner:
the authoritative task-processing Entity/current-writer writes its own execution state only when separately authorized by the future active rule. A replacement cannot assume predecessor state-writing authority merely from replacement status; it must reconcile under Recovery/Task Conveyor/current-writer rules.

Update/CAS:
successor state must reference exact prior state/version. Concurrent/stale write => conflict/STOP. No last-write-wins.

Relationship:
Task Conveyor remains owner of task/PROMPT/activation lifecycle.
Recovery remains owner of instance/recovery/initiation.
DURABLE_EXECUTION_STATE records materialized execution progress for exact task; creates neither task nor writer authority.
SECE EFFECTIVE_CONTEXT may bind/read it as current evidence; execution contract may project needed fields.
Chat may cache/display it but chat state is never authoritative.

Checkpoint trigger candidate classes:
before PROCESSING_STARTED transition;
after any consequential/irreversible external effect;
after completion of a bounded execution step whose loss would cause unsafe replay;
before/when RESULT_PENDING is established;
at TERMINAL before stop, together with durable next disposition.
Exact frequency beyond these safety triggers remains future implementation policy, not established here.
