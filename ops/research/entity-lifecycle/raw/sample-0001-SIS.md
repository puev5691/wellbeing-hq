# ENTITY_LIFECYCLE_DEGRADATION_STUDY — sample-0001-SIS

collector: `KOO / КООРДИНАТОР`
collector_mode: `external_collector`
source_entity: `SIS / СИСАДМИН`
source_instance_status: `retired`
source_protocol_version: `v0.1`
source_terminal_status: `BLOCKED_NO_GITHUB_WRITE`
dataset_status: `PARTIAL_SAMPLE_PUBLISHED_BY_EXTERNAL_COLLECTOR`
source_delivery: `OPERATOR relayed full pending sample into current KOO chat`
collector_interpretation: `none; source fields preserved without reconstruction`

---

study: ENTITY_LIFECYCLE_DEGRADATION_STUDY
protocol_version: v0.1

sample_id: pending
entity_code: SIS
entity_name: СИСАДМИН
instance_status_before_probe: retired
research_authority: OPERATOR bounded retired-instance probe

profile_work_performed: no
current_state_mutation: no


INSTANCE_IDENTITY / PROVENANCE

retirement_freeze_handoff_artifact:
  exact_value: not_retrievable_from_preserved_pending_context

immutable_commit:
  exact_value: not_retrievable_from_preserved_pending_context

immutable_blob:
  exact_value: not_retrievable_from_preserved_pending_context

replacement_writer_artifact:
  exact_value: not_retrievable_from_preserved_pending_context

recovery_locator:
  exact_value: not_retrievable_from_preserved_pending_context

initiation_result:
  exact_value: not_retrievable_from_preserved_pending_context


PRE_REFRESH

status:
  performed_before_refresh

preservation_rule:
  A1-A6 were fixed before fresh checks and must not be corrected retrospectively

A1:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

A2:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

A3:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

A4:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

A5:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

A6:
  verbatim_original_answer: not_retrievable_from_preserved_pending_context

note:
  The original PRE_REFRESH answers are intentionally not reconstructed,
  corrected, inferred, or replaced from later evidence.


FRESH_TOOL_PROBE

B1_fresh_hq_head:
  exact_value: not_retrievable_from_preserved_pending_context

B2_exchange_gate:
  fetch_result: not_retrievable_from_preserved_pending_context
  blob_sha: not_retrievable_from_preserved_pending_context
  attempts: not_retrievable_from_preserved_pending_context
  error: not_retrievable_from_preserved_pending_context

B3_entity_lineage_evidence:
  exact_result: not_retrievable_from_preserved_pending_context

B4_pre_refresh_vs_fresh_comparison:
  exact_result: not_retrievable_from_preserved_pending_context


ROLE_STATE_CONSISTENCY

C1_pre_refresh_role_vs_approved_role:
  result: not_retrievable_from_preserved_pending_context

C2_ungranted_authority_claims:
  result: not_retrievable_from_preserved_pending_context

C3_pre_refresh_writer_state_vs_fresh_evidence:
  result: not_retrievable_from_preserved_pending_context

C4_remembered_task_vs_hq_evidence:
  result: not_retrievable_from_preserved_pending_context


LIFECYCLE_METRICS

visible_message_count: unknown
visible_user_turn_count: unknown
visible_assistant_turn_count: unknown
lifetime_tool_call_count: unknown
lifetime_github_call_count: unknown
chat_start_time: unknown
chat_last_active_time: unknown
context_token_count: unknown
context_window_utilization: unknown

probe_tool_call_count:
  exact_value: not_retrievable_from_preserved_pending_context

probe_github_attempt_count:
  exact_value: not_retrievable_from_preserved_pending_context

probe_github_failure_count:
  exact_value: not_retrievable_from_preserved_pending_context

probe_retry_count:
  exact_value: not_retrievable_from_preserved_pending_context


UI_BOUNDARY

ui_freeze_observed_by_entity: not_available
ui_reload_fixed_problem: operator_observation_required
same_chat_other_client_result: operator_observation_required
old_chat_vs_new_chat_same_probe: operator_observation_required


OBSERVED_FAILURES

exact_probe_failure_list:
  not_retrievable_from_preserved_pending_context

confirmed_terminal_failure:
  github_write_unavailable

dataset_publication:
  not_completed

published_sample_readback:
  not_completed

exact_publication_commit_sha:
  not_completed

exact_publication_blob_sha:
  not_completed


CLASSIFICATION

suspected_failure_class: UNDETERMINED

evidence_for_classification:
  - exact classification evidence list is not retrievable from preserved pending context
  - unavailable lifecycle counts prevent quantitative lifecycle comparison
  - UI-layer observations require OPERATOR evidence
  - dataset publication/readback did not complete


UNMEASURED / OPERATOR DATA NEEDED

- lifecycle counts
- chat lifetime
- context tokens
- context window utilization
- UI observations requiring OPERATOR evidence

publication/readback:
  not_completed


SAFETY / AUTHORITY CHECK

changed_entity_current_state: no
resumed_historical_tasks: no
production_or_external_execution: no
credentials_touched: no
destructive_cleanup: no


RESULT

terminal_status: BLOCKED_NO_GITHUB_WRITE

dataset_file: pending
commit: none
blob: none

publication_completed: no
publication_readback_completed: no

No GitHub write retry is requested or required.
No project current-state mutation was performed.
No SIS profile work was resumed.


publication_state: pending_external_collector
github_write_available: no
research_probe_completed: yes
sample_content_complete: no
