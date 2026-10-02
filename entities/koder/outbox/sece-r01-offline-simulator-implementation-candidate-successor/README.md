# SECE r0.1 OFFLINE simulator implementation candidate successor

status: OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

This package is a deterministic synthetic-only implementation candidate. It performs no real project effect.

## Reviewed inputs

Vendored under reviewed-inputs/ as exact immutable copies:

- FIXTURE-SCHEMA.json
  Git blob 2647d0f11719b143cef5543a13218cc28376e2bc
- FIXTURE-CATALOG.json
  Git blob cdaed663de7027d700278322341260c5974cb01d
- TRACE-SCHEMA.json
  Git blob 0876cff31d1e4b54b065933aa74129e591c78e94
- IDENTITY-SPEC.md
  Git blob 7339655c132459f87a1943f4f825d45b497108e3
- CONTRACT-ID-TEST-VECTORS.json
  Git blob 8758546a2a1bf62defd4e7b32d5ab3357abba8e2
- TRACE-ID-TEST-VECTORS.json
  Git blob 00eb5487c611ae9e3e1db6c4a00100c419c9a650
- INPUT-DERIVATION-SPEC.md
  Git blob 0f9d11946b6f271ef03c99c8757e1ed9f032e466

## Implementation

Core:
sece_simulator.py

Offline test runner:
run_offline_tests.py

Fixture execution runner:
fixture_runner.py

Schema/canonicalization facade:
schema_tools.py

## Exact offline commands

From this package directory:

python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py

python3 -I -B run_offline_tests.py

python3 -I -B fixture_runner.py

No network or external package install is needed.

## Pipeline

RAW synthetic context
-> semantic atoms/bindings
-> context composition
-> collision detection
-> exact-scope correction
-> EFFECTIVE_CONTEXT(n)
-> bounded L6 projection
-> C1/C2/C3 validation
-> simultaneous predicate set
-> local L7 aggregation
-> synthetic one-safe-step only after ADMIT
-> synthetic RESULT/EVENT classification
-> CONTEXT_DELTA
-> EFFECTIVE_CONTEXT(n+1)
-> next-gate classification
-> trace
-> FixtureOracle.

The final trace envelope is serialized after FixtureOracle only to append expected_vs_actual. All causal computation is complete before oracle comparison; expected values never feed actual computation.

## Non-authority

This candidate is not production, not live runtime, not a Source/canon activation, not an Entity authority engine, and not approval for live use.
