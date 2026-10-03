# DURABLE_EXECUTION_STATE_R01 r0.2 candidate
status: CANDIDATE_NOT_ACTIVE

Logical execution evidence is recommended; a new physical store is NOT required by this candidate.

Identity:
state_id; execution_attempt_id; task_id; actor_instance_id; causal_event_id;
task_locator/version/blob; authority_ref/identity; writer_ref/identity when applicable;
expected_current_state_version; accepted_state_version; predecessor_state_identity;
task_currentness; processing_state;
processing_started_evidence_ref;
current_execution_step;
last_durable_checkpoint {checkpoint_id, covered_prefix_scope, evidence_refs};
pending_result_locator;
input_identities[];
supersession_evidence[];
crash_replacement_disposition;
chat_only_unmaterialized_work: NONE|UNKNOWN;
next_causal_disposition;
provenance[].

processing_state:
INITIAL_NOT_STARTED | STARTED | CHECKPOINTED | RESULT_PENDING | TERMINAL | BLOCKED | UNKNOWN.

Documentary conditional-acceptance model:
1 declare exact task-attempt scope;
2 propose successor against exact expected current version;
3 revalidate current-writer/write authority where required and task currentness at acceptance;
4 conditionally accept exactly one successor for expected current version;
5 record accepted successor acknowledgement/readback;
6 stale branch is rejected but preserved as evidence;
7 missing acceptance/currentness predicate => UNKNOWN/BLOCK.
No last-write-wins.
An old writer holding an old reference cannot authoritatively commit after replacement.

This does not choose a backend/CAS engine and does not claim production atomicity.

Relationship:
Task Conveyor owns task/PROMPT/activation lifecycle.
Recovery owns instance/recovery/initiation/writer outcomes.
Execution-state is evidence dependency, not recovery package/self-snapshot/writer grant.
SECE may consume exact evidence by profile/addendum; EFFECTIVE_CONTEXT is not authoritative execution storage.
Chat may cache/display, never establish authoritative execution fact.
