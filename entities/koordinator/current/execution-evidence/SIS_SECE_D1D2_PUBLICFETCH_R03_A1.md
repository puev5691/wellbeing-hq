# Execution evidence — SIS_SECE_D1D2_PUBLICFETCH_R03_A1

profile_id: CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01
profile_version_semantic_blob: db146a594659e48fa0ce51fd9cd81602cf50058e
profile_effectivity_record: puev5691/wellbeing-hq@259f4c8dbddc42b4b446ef57fec46f44db1b4e3e:entities/koordinator/current/CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01.active.md

execution_attempt_id: SIS_SECE_D1D2_PUBLICFETCH_R03_A1
task_id: SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R03
task_locator: entities/koordinator/outbox/SIS_SECE_D1D2_publicfetch_exec_r03_prompt.md

authority_ref:
AUTHORIZE_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R03 = YES

authority_scope:
one NEW SIS anonymous-public exact-commit acquisition + offline execution-proof attempt only

profile_applicability_reason:
EXACT_TASK_REQUIRES_DURABLE_PROGRESS_EVIDENCE

task_uses_interchat_prompt_conveyor: YES
task_is_new_attempt: YES

actor_entity: SIS
actor_writer_ref: entities/sisadmin/current/SIS__emergency-replacement-current-writer-r08.md
actor_writer_blob: 2b79f89729cf0fd6c1a3d25e273e86f0c1c01b78
writer_requirement: REQUIRED

target_device_hostname: p552203.kvmvps
target_device_id: 830038a0-232b-4d83-b52d-0e9973126165

public_repository:
puev5691/wellbeing-hq

permitted_remote:
https://github.com/puev5691/wellbeing-hq.git

fixed_disposable_workspace:
/data/wellbeing-lab/tmp/sece-d1d2-publicfetch-r03-a1

input_package_commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

input_package_tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

input_package_identity:
f2ff196fa8463834b08fc44d636de1aa2527db873fa38f490858a9be5688e4a1

predecessor_attempt:
SIS_SECE_D1D2_P552203_LOCALGIT_R02_A1

predecessor_disposition:
TERMINAL_BLOCKED_DO_NOT_REPLAY

task_currentness:
CURRENT_AT_MATERIALIZATION

supersession_conflict:
NONE_FOUND_AT_MATERIALIZATION

device_availability_at_koo_preflight:
ONLINE

terminal_criterion:
one immutable SIS PASS/BLOCKED/FAIL result for exact anonymous-public candidate acquisition, exact materialization and offline runtime proof

initial_state:
INITIAL_NOT_STARTED

processing_started:
NOT_PROVEN

processing_started_event:
NONE

expected_current_version:
INITIAL

accepted_current_version:
INITIAL_V1

successor_acceptance_rule:
exact-attempt conditional current-version acceptance; no last-write-wins

next_causal_disposition:
AWAIT_OPERATOR_MANUAL_TRANSFER_TO_SIS

next_disposition_creates_task_authority:
NO

full_clone_authority:
NONE

branch_sync_authority:
NONE

authenticated_git_authority:
NONE

candidate_activation:
NONE

production_authority:
NONE

historical_replay:
NONE

Project Source/canon mutation:
NONE

project_time: omitted
