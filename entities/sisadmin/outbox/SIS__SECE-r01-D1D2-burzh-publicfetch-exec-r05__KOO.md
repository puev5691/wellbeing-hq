# SIS — SECE D1+D2 alternative-host execution proof R05 result

status:
FAIL

terminal:
FAIL_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05

project_time:
omitted

entity:
SIS / СИСАДМИН r0.9

attempt:
SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1

## Human outcome

R05 successfully established a clean independent execution environment on burzh, acquired and materialized the exact immutable D1+D2 candidate, and passed all required package-integrity checks.

The Python compilation workload passed with exit 0.

The required offline test workload executed against the exact package and returned exit 1 with its own status FAIL. The observed failing evidence was NEXT_GATE_RESOLVER_GROUNDING_FIXED=false and correction_tests.c7_grounded_candidate=false.

Per the exact STOP condition, fixture_runner was not run after the required workload failure.

The attempt is therefore FAIL, not BLOCKED and not PASS.

## Exact task

puev5691/wellbeing-hq:
entities/koordinator/outbox/SIS_SECE_D1D2_burzh_exec_r05_prompt.md

task_blob:
c08ca216c0eb67253927520d1b6c1e4708a095d3

## Exact authority

puev5691/wellbeing-hq@9ae4cd2d597dc723efc7c77f5820fa5a4900f05c:
entities/koordinator/outbox/KOO__authorize-SIS-SECE-D1D2-burzh-R05__OPERATOR.md

authority_blob:
257e9a0f56063b31aba8c9ba0f69e48a71bae03b

decision:
AUTHORIZE_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05 = YES

## Current SIS writer

puev5691/wellbeing-hq@1de10d5d61430fae49f8e27bccbd655c3ed2c972:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r09.md

writer_blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

writer_status:
CURRENT_WRITER_ESTABLISHED

## Durable evidence

PROCESSING_STARTED:

puev5691/wellbeing-hq@8b2cf1017881c30f60c40b65865b0ed7b8c7b53f:
entities/sisadmin/outbox/execution-evidence/SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1__PROCESSING_STARTED_E1.md

blob:
03fb97c1901dcf8034b6434fdd7e74981b2ad9f5

readback:
PASS

CHECKPOINT_DURABLE:

puev5691/wellbeing-hq@9714d8037a8f38539dc92b396e84fcab0a9e8921:
entities/sisadmin/outbox/execution-evidence/SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1__CHECKPOINT_DURABLE_C1.md

blob:
a5dbcd99e80c0319d093170e089be8dc41218932

readback:
PASS

TERMINAL_EVIDENCE:

puev5691/wellbeing-hq@0021869004f6fbd295dba113bd7f22a2ca2c7aa5:
entities/sisadmin/outbox/execution-evidence/SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1__TERMINAL_FAIL_E2.md

blob:
6eb193d99aa8c7d0a9209235890a4afd240c3cd1

readback:
PASS

## Target and preflight

target:
burzh / ruvds-xnqc6

device_id:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

inventory:
ONLINE

Commander_ping:
PASS

minimal_terminal_process:
PASS

minimal_terminal_evidence:
/bin/true reached process_exit

environment_note:
Commander shell startup reported getcwd errors because its inherited starting directory no longer existed. Commands after explicit cd to /tmp executed normally. This did not prevent the required preflight or R05 execution.

Python:
3.12.3

Python_requirement:
PASS >= 3.12

workspace:
/tmp/wellbeing-sece-d1d2-publicfetch-r05-a1

workspace_initial_state:
ABSENT

anonymous_exact_source_reachability:
PASS

interactive_credentials:
DISABLED

## Exact immutable candidate

source:
https://github.com/puev5691/wellbeing-hq.git

candidate_commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

package_path:
entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-r02/

package_tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

declared_package_identity:
f2ff196fa8463834b08fc44d636de1aa2527db873fa38f490858a9be5688e4a1

candidate_status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

candidate_activation:
NOT_ACTIVATED

## Acquisition and materialization

workspace_created:
YES

disposable_bare_repo:
CREATED_IN_R05_WORKSPACE_ONLY

exact_commit_acquisition:
PASS

fetched_commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

resolved_package_tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

package_materialization:
PASS

file_composition:
24/24 PASS

key_blobs:
9/9 PASS

SHA256SUMS:
e948075bbb08a2d78654c2e3446d94001b59f64f PASS

MANIFEST.md:
da896e89dc5a6961a4d5ffd77bdc485857ae3fe6 PASS

PACKAGE-IDENTITY.txt:
805c38795db17adb4a09f50fb2823021b71b9102 PASS

sece_simulator.py:
e7b89c948c4e672c5b682408ce790670dfcdad5c PASS

run_offline_tests.py:
37b6f9e655e55d9f4be59a87052cc354ff38a328 PASS

d1d2_tests.py:
e4858197c67b4a2f8aaa275642610e5005605b92 PASS

anti_cheat_regression_tests.py:
29ab8609955d22c8785004332df4a0a9c5d3856d PASS

architecture_tests.py:
6e24ba6424e99659e36c8385df34c30b608558ca PASS

correction_tests.py:
af58242a1d988856016cdf8556dbf14faba51663 PASS

SHA256SUMS_SHA256:
86c7691d0ddc31dc15898df2015512fc5b349fa0d51b168ce3444a735eb74d2d PASS

SHA256SUMS_entries:
21

SHA256SUMS_payload:
21/21 PASS

MANIFEST_package_identity:
PASS

PACKAGE_IDENTITY_file:
PASS

## Python workloads

py_compile_command:
python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py schema_minimum_tests.py correction_tests.py architecture_tests.py anti_cheat_regression_tests.py d1d2_tests.py

py_compile_exit:
0

run_offline_tests_command:
python3 -I -B run_offline_tests.py

run_offline_tests_exit:
1

run_offline_tests_status:
FAIL

fixture_runner_command:
python3 -I -B fixture_runner.py

fixture_runner_execution:
NOT_RUN_DUE_STOP_ON_REQUIRED_WORKLOAD_FAILURE

fixture_runner_exit:
NOT_AVAILABLE

## Required runtime-gate matrix observed before STOP

SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
TOTAL_FIXTURES_PASS=54/54
INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
TRACE_SCHEMA_PASS=YES
ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13
ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES
DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES
NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED=YES
STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED=YES
ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION=YES
DESIGN_INTERFACE_MAPPING_COMPLETE=22/22

required_runtime_gate_matrix:
PASS_AS_REPORTED_BY_RUN_OFFLINE_TESTS

## Failing workload evidence

run_offline_tests overall status:
FAIL

NEXT_GATE_RESOLVER_GROUNDING_FIXED:
false

correction_tests.c7_grounded_candidate:
false

failure_classification:
REQUIRED_PYTHON_WORKLOAD_RUN_OFFLINE_TESTS_EXIT_1

The failure occurred after exact-byte acquisition and integrity verification and is therefore an execution result of the immutable candidate, not an acquisition or transport blocker.

## Predecessor boundaries

R03_access:
NONE

R03_resume_replay_cleanup:
NONE

R04_access:
NONE

R04_resume_replay_cleanup:
NONE

p552203_access:
NONE

## Existing burzh state

existing_burzh_project_repository_access:
NONE

existing_burzh_project_repository_mutation:
NONE

existing_burzh_worktree_object_database_mutation:
NONE

## Side-effect accounting

R05_workspace_creation:
PERFORMED

anonymous_public_exact_object_acquisition:
PERFORMED

exact_package_materialization:
PERFORMED

offline_python_execution:
PERFORMED_UNTIL_REQUIRED_WORKLOAD_FAILURE

candidate_modification:
NONE

authenticated_Git_credentials:
NONE

package_installation:
NONE

existing_service_network_provider_API_Telegram_mutation:
NONE

Project_Source_canon_mutation:
NONE

role_recovery_current_writer_mutation:
NONE

simulator_activation_deploy:
NONE

automatic_SHD_rereview:
NONE

forbidden_effects:
NONE

## Cleanup

terminal_evidence_captured_before_cleanup:
YES

R05_workspace_ownership:
PROVEN_BY_INITIAL_ABSENCE_AND_THIS_ATTEMPT_CREATION

cleanup:
PASS

cleanup_action:
removed only /tmp/wellbeing-sece-d1d2-publicfetch-r05-a1

post_cleanup_readback:
WORKSPACE_ABSENT

## Final classification

PASS_requirements_met:
NO

BLOCKED_condition_established:
NO

FAIL_condition_established:
YES

status:
FAIL

terminal:
FAIL_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05

next_gate_classification:
RETURN_TO_KOO_FOR_FRESH_FAILED_CANDIDATE_EXECUTION_RECONCILIATION

No automatic SHD rereview.

STOP
