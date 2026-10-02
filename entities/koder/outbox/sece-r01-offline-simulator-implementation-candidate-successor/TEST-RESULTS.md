# Offline test results

status: PASS

Test command:

python3 -I -B run_offline_tests.py

Interpreter:
CPython 3.12.3

## G1 schema/catalog

SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES

Inventory:
T=15
CXT=10
O=10
P=7
MUTATION=12
TOTAL=54

## G2 input completeness

INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15

## G3 contract identity

Published base contract ID reproduced:
7b819fb3ac464c226b83fbc4fe9fddb1a40b90a6b3f5c35c11d5078347e4ab6f

Canonical-identical:
same ID PASS

Semantic mutation classes:
25/25 different IDs PASS

CONTRACT_ID_TEST_VECTORS_PASS=YES

## G4 trace identity

Published base trace ID reproduced:
efadafaafa8577a36bf11cf965bb2a38fa5dacb8ed8dadccb88d95a611c59e73

Canonical-identical:
same ID PASS

recomputed_bindings mutation:
different ID PASS

Corrected base trace:
TRACE-SCHEMA PASS

TRACE_ID_TEST_VECTORS_PASS=YES
TRACE_SCHEMA_PASS=YES

## G5 all fixtures

T_FIXTURES_PASS=15/15
CXT_FIXTURES_PASS=10/10
O_FIXTURES_PASS=10/10
POSITIVE_CONTROLS_PASS=7/7
PROPERTY_FIXTURES_PASS=12/12
TOTAL_FIXTURES_PASS=54/54

## G6 anti-cheat

ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES

## G7 architecture assertions

13/13 PASS:
- compatible semantic lines coexist;
- scope-local conflict preserves unrelated scope;
- dependency changes recompute dependency closure only;
- stale dependent binding cannot survive;
- L6 projection cannot invent context facts;
- ACTION_INTENT is proposal only;
- profile/experience/capability do not create authority;
- C1/C2/C3 explicit;
- L7 aggregation local;
- simultaneous reasons preserved;
- no ADMIT with conflict/reject/blocker/required UNKNOWN/FAIL;
- unverified/UNKNOWN/conflicted event cannot create successor delta;
- Task Conveyor/Recovery/current-writer evidence does not generate authority.

DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES
DESIGN_INTERFACE_MAPPING_COMPLETE=22/22

## Cross-process determinism

Two independent fixture_runner executions were byte-identical.

SHA-256:
31dcf2dd5f160bc2bea3ad0e95060b61923303d6054a1f4b949a53959479045d

## Required markers

IMPLEMENTATION_CANDIDATE_CREATED=YES
SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15
ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
T_FIXTURES_PASS=15/15
CXT_FIXTURES_PASS=10/10
O_FIXTURES_PASS=10/10
POSITIVE_CONTROLS_PASS=7/7
PROPERTY_FIXTURES_PASS=12/12
TOTAL_FIXTURES_PASS=54/54
TRACE_SCHEMA_PASS=YES
DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES
DESIGN_INTERFACE_MAPPING_COMPLETE=22/22
