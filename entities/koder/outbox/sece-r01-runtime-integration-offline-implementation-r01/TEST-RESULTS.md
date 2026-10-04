# Test results

KOD local offline checks on new runtime layer:
- python3 -m py_compile runtime_integration.py runtime_integration_tests.py package_gate_tests.py run_runtime_integration_tests.py run_all_offline_tests.py => PASS
- python3 -I -B run_runtime_integration_tests.py => PASS
- RUNTIME_INTEGRATION_TESTS_PASS=16/16
- NO_LIVE_EFFECT_TEST_BOUNDARY=YES

Covered:
- transport adapter cannot manufacture positive facts;
- explicit trust policy required;
- unverified/untrusted evidence remains UNKNOWN;
- conflict has no order winner;
- worker/writer/Recovery eligibility;
- resolution + actor binding propagation;
- intent requires RESOLVED + core ADMIT;
- intent carries authority/input/actor identity refs;
- evidence-frontier change invalidates admission;
- actor-binding change invalidates admission;
- unresolved prior effect blocks overlap;
- non-live adapter performs no effect;
- mock observation cannot fabricate outcome;
- separate trusted outcome evidence required;
- result and human explanation share one truth path;
- deterministic identities;
- forbidden I/O imports absent from runtime layer.

Exact baseline core was independently proven by SIS R06:
all three baseline workloads exit 0, 54/54 fixtures PASS, D1/D2/C7 and anti-cheat/determinism/no-side-effect gates PASS.

Combined package runner is included:
python3 -I -B run_all_offline_tests.py

It runs package baseline identity/interface gate, reviewed baseline tests, 54 fixture runner, and new runtime integration tests.
Combined runner was not executed in the KOD local container because the exact reviewed baseline bytes are available through the GitHub connector but not materialized into that container. This does not claim independent combined-package execution.
