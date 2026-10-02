# SECE r0.1 simulator design input-completeness correction diff

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED
correction_scope: INPUT_COMPLETENESS_ONLY
project_time: omitted

## Exact predecessor

puev5691/wellbeing-hq@9e1d66efc798041d2217c5e9a195fc795d84aad9:
entities/koder/outbox/sece-r01-offline-simulator-design-successor-d1d2d3-correction/

tree:
66686bac2a742a4673ec7da9eb2b7b57a74c7721

Predecessor:
FIXTURE-SCHEMA.json blob 7d221176ebd694d67321261c5466f6df1090bf8f
FIXTURE-CATALOG.json blob 4ce7939519ecdfa24e4102742be519fa5d5f2259

## Corrected D1 input completeness only

FIXTURE-SCHEMA:
adds closed definitions:
- InitialDerivedBinding
- DependencyEdge
- ScopeIndexEntry
- RecomputationRule
- SyntheticInitialState
- BindingDerivationInput

CXTInput:
binding_derivation_input is required because all CXT1-CXT10 are affected.

PInput / MutationInput:
binding_derivation_input is optional and is present only in affected P3/P4/P6/M6/M8.

FIXTURE-CATALOG:
adds binding_derivation_input only to the 15 affected fixtures.

The 39 unaffected fixtures are logically byte-identical records to predecessor.

No expected field is changed.

No fixture ID/family/description/architecture_rule_refs/provenance/predecessor_meaning_ref is changed.

## Exact intended effect

Before:
exact invalidated/recomputed/preserved binding sets could not be computed for 15 fixtures without oracle/hidden mapping.

After:
the exact binding inventory, dependency edges and recomputation outputs are explicit typed fixture data.

The reviewed generic rule:
changed dependency -> traverse dependents -> invalidate -> recompute affected -> preserve unaffected
can now execute without hidden information.

## Unchanged

D2 contract identity semantics:
UNCHANGED.

D3 trace identity/schema:
UNCHANGED.

L0-L9:
UNCHANGED.

Effective Context:
UNCHANGED.

CONTEXT_DELTA:
UNCHANGED.

C1/C2/C3:
UNCHANGED.

MULTI_OUTCOME_AGGREGATION:
UNCHANGED.

Task Conveyor:
UNCHANGED.

Recovery/current-writer:
UNCHANGED.

Fixture expected meanings:
UNCHANGED.
