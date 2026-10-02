# Anti-cheat report

status: PASS

## Oracle separation

Simulator.run_fixture computes:
raw input,
context,
binding derivation,
effective context,
projection,
predicates,
aggregation,
synthetic step/result,
delta/successor context,
next gate,
actual assertion state

before calling FixtureOracle.compare.

Automated AST inspection confirms no expected access in the pre-oracle computation segment.

ORACLE_SEPARATION_TEST_PASS=YES

## Fixture ID branching

No conditional expression in Simulator.run_fixture branches on fixture_id.

Fixture family is used only as schema/pipeline family decoding.

NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES

## Hidden binding mapping

All exact affected-fixture binding IDs come from reviewed BindingDerivationInput.

The automated test collects every fixture binding ID from:
initial_derived_bindings
and recomputation_rules

and confirms none is hard-coded in sece_simulator.py.

The generic dependency algorithm parses no binding name.

NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES

## Prose execution

description is not read by the computation pipeline.

## Expected mutation

Expected fixture values are never modified.

## Binding derivation

15/15 affected fixtures:
changed_source_ids
-> typed dependency edges
-> fixed-point invalidation
-> typed recomputation rules
-> recomputed bindings
-> remaining initial bindings
-> preserved bindings.

Expected sets are compared only afterward.

INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15
