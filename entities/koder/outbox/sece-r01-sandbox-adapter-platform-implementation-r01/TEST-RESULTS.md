# Verification results

STATIC_PY_COMPILE:
PASS

PURE_MOCK_TESTS:
22/22 PASS

Command:
python3 -I -B run_sandbox_adapter_tests.py

Observed:
SANDBOX_ADAPTER_TESTS_PASS=22/22
REAL_SANDBOX_EFFECT_EXECUTION=NOT_EXECUTED

Coverage:
- accepted/rejected leaf grammar
- platform capability PASS/BLOCKED
- root identity/binding
- binding version/root/evidence drift
- pre-effect fail closed
- prior UNRESOLVED blocks
- openat2 primitive plan
- EVIDENCED_SUCCESS vs UNRESOLVED outcome
- cleanup eligible/BLOCKED/UNRESOLVED
- exclusive namespace mutation control requirement
- anchored post-cleanup readback

R04 baseline:
independently proven earlier by SIS R07, runtime integration 22/22 PASS.

Combined new-candidate runner:
NOT_EXECUTED_BY_THIS_KOD_ATTEMPT because exact R04 package could not be materialized into the local container through GitHub DNS/connector-to-filesystem bridge.

No combined-runtime PASS is claimed for this new candidate.
