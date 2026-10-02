# Offline RUNBOOK

Runtime:
CPython 3.12+ standard library only.

External packages:
NONE.

From the package directory run:

python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py schema_minimum_tests.py correction_tests.py architecture_tests.py anti_cheat_regression_tests.py

python3 -I -B run_offline_tests.py

python3 -I -B fixture_runner.py

Expected:
- run_offline_tests.py exits 0 and prints status PASS;
- fixture_runner.py exits 0 and emits 54 ORACLE_PASS records.

No network, model/API, Telegram, credentials, service or production storage is required.
