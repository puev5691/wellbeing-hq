# Test results
execution_attempt_id: KOD_SECE_IMPLCORR_STATIC_D1D2_R02_A1
candidate_status: OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Package-local commands required:
python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py schema_minimum_tests.py correction_tests.py architecture_tests.py anti_cheat_regression_tests.py d1d2_tests.py
python3 -I -B run_offline_tests.py
python3 -I -B fixture_runner.py

Current KOD execution result:
BLOCKED_KOD_LOCAL_MATERIALIZATION_BRIDGE

The container cannot resolve GitHub; the GitHub connector can read exact immutable bytes but cannot place them into that Python filesystem. No external host/runtime was mutated to bypass this boundary.

Therefore 54/54 and all old/new runtime PASS markers are NOT claimed by this result.
Static source construction did verify exact patch anchors and absence of transformation_type in generated StaticValidator and Simulator scopes.
SHD independent execution environment blocker remains UNCHANGED_EXTERNAL_BLOCKER.