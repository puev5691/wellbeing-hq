# TERMINAL EVIDENCE — SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1

status:
TERMINAL_EVIDENCE_CAPTURED

terminal_classification:
FAIL

project_time:
omitted

attempt:
SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1

task_blob:
c08ca216c0eb67253927520d1b6c1e4708a095d3

authority_blob:
257e9a0f56063b31aba8c9ba0f69e48a71bae03b

writer_blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

## Durable progress evidence

PROCESSING_STARTED:
puev5691/wellbeing-hq@8b2cf1017881c30f60c40b65865b0ed7b8c7b53f:
entities/sisadmin/outbox/execution-evidence/SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1__PROCESSING_STARTED_E1.md

processing_started_blob:
03fb97c1901dcf8034b6434fdd7e74981b2ad9f5

CHECKPOINT_DURABLE:
puev5691/wellbeing-hq@9714d8037a8f38539dc92b396e84fcab0a9e8921:
entities/sisadmin/outbox/execution-evidence/SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1__CHECKPOINT_DURABLE_C1.md

checkpoint_blob:
a5dbcd99e80c0319d093170e089be8dc41218932

checkpoint_readback:
PASS

## Exact materialization state before Python

target:
burzh / ruvds-xnqc6

device_id:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

workspace:
/tmp/wellbeing-sece-d1d2-publicfetch-r05-a1

source:
https://github.com/puev5691/wellbeing-hq.git

candidate_commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

package_tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

exact_commit_acquisition:
PASS

package_materialization:
PASS

file_composition:
24/24 PASS

key_blobs:
9/9 PASS

SHA256SUMS_blob:
e948075bbb08a2d78654c2e3446d94001b59f64f PASS

SHA256SUMS_SHA256:
86c7691d0ddc31dc15898df2015512fc5b349fa0d51b168ce3444a735eb74d2d PASS

SHA256SUMS_payload:
21/21 PASS

MANIFEST_package_identity:
PASS

PACKAGE_IDENTITY_file:
PASS

## Python workloads

Python:
3.12.3

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

## Bounded failure evidence

run_offline_tests reported:
- status = FAIL
- NEXT_GATE_RESOLVER_GROUNDING_FIXED = false
- correction_tests.c7_grounded_candidate = false

The required workload therefore failed explicitly after exact-byte materialization.

## Required runtime-gate matrix observed in run_offline_tests output

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

## Failure classification

FAIL_reason:
REQUIRED_PYTHON_WORKLOAD_RUN_OFFLINE_TESTS_EXIT_1

secondary_failure_markers:
NEXT_GATE_RESOLVER_GROUNDING_FIXED=false
c7_grounded_candidate=false

PASS_requirements_met:
NO

BLOCKED_condition_established:
NO

FAIL_condition_established:
YES

candidate_activation:
NOT_ACTIVATED

R03_R04_p552203_access:
NONE

cleanup:
PENDING_POST_TERMINAL_EVIDENCE_SAFE_CLEANUP

STOP_ON_REQUIRED_WORKLOAD_FAILURE:
APPLIED
