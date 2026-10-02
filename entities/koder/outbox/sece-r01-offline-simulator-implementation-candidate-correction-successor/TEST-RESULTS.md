# Corrected offline test results

status: PASS

Runtime:
CPython 3.12.3

Exact commands executed from package directory:

python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py schema_minimum_tests.py correction_tests.py architecture_tests.py anti_cheat_regression_tests.py

python3 -I -B run_offline_tests.py

python3 -I -B fixture_runner.py

## Regression gates

SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
TOTAL_FIXTURES_PASS=54/54

T_FIXTURES_PASS=15/15
CXT_FIXTURES_PASS=10/10
O_FIXTURES_PASS=10/10
POSITIVE_CONTROLS_PASS=7/7
PROPERTY_FIXTURES_PASS=12/12

INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15

CONTRACT_ID_TEST_VECTORS_PASS=YES
25/25 semantic contract mutations produced the reviewed different IDs.

TRACE_ID_TEST_VECTORS_PASS=YES
TRACE_SCHEMA_PASS=YES

## C1-C8 correction gates

REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED=YES

Below reviewed minimum:
rejected.

Exactly reviewed minimum:
accepted.

CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED=YES

Direct tests prove:
- S1 correction preserves S2;
- verified refinement changes only exact affected scope;
- unresolved conflict remains explicit;
- UNKNOWN remains explicit;
- prior context remains immutable;
- Effective Context consumes correction objects.

EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED=YES

Direct tests verify full reviewed minimum structure and deterministic complete-context identity.
Profile/experience/capability field presence alone creates no authority.

C1_L6_PROJECTION_BOUNDARY_FIXED=YES

Direct tests:
- valid projected C1 binding + clear predicates => ADMIT and synthetic guarded step;
- missing binding => reject/block;
- stale binding => reject;
- conflicted binding => reject/block;
- raw authority fact changed after Effective Context construction cannot bypass L6.

L6_PROJECTION_FIREWALL_ENFORCED=YES

Projector directly rejects:
- missing basis;
- invented context item;
- invalid context dependency.

RESULT_CLASSIFIER_FIDELITY_FIXED=YES

Direct cases:
PASS
FAIL
UNKNOWN missing
UNKNOWN unverified

NEXT_GATE_RESOLVER_GROUNDING_FIXED=YES

Direct cases:
- class + active current exact rule + verified current evidence => grounded candidate;
- class without rule => no candidate;
- superseded rule => no candidate;
- terminal/result alone => no candidate.

ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13

A1-A13 all directly PASS.

## Anti-cheat

ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES

No fixture expected value feeds actual computation.
No run_fixture branch uses fixture_id.
No exact reviewed fixture binding ID is hard-coded in core source.
Core correction/projector/authority/result/next-gate invariants do not depend on fixture transformation enums.

## Determinism / side effects

DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES

Two independent fixture_runner runs are byte-identical.

See:
DETERMINISM-EVIDENCE.txt

DESIGN_INTERFACE_MAPPING_COMPLETE=22/22

## Final status

OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

The independent SHD review-execution-environment limitation is not addressed or claimed fixed by this package.
