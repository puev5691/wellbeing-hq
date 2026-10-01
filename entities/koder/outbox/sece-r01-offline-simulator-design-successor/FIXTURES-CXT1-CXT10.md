# SECE r0.1 simulator Effective Context fixtures CXT1-CXT10

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

Canonical machine records are in FIXTURE-CATALOG.json.

| ID | Synthetic input/trigger | Affected scopes | Invalidated bindings | Preserved bindings/context | Expected successor |
|---|---|---|---|---|---|
| CXT1 | MAY inspect + MUST_NOT mutate + consumer UNKNOWN | gateway | none | all three semantic lines + evidence requirement | compatible lines coexist; no winner |
| CXT2 | experience suggests mutate; active rule forbids | action/mutate | experience-derived executable mutate proposal | experience advisory + unrelated context | mutate remains forbidden |
| CXT3 | recovery R covers S/U; verified delta D refines S | S | R-derived current bindings in S | R for U + historical provenance | D selected for S; R retained outside S |
| CXT4 | verified terminal supersedes current task T | T | all T-dependent executable/current bindings | unrelated U | T terminal/superseded; U unchanged |
| CXT5 | new exact authority grant A/S | A/S | pending/non-authorized A bindings | B + unrelated scopes | A binding current subject to other gates |
| CXT6 | active source conflict only S1 | S1 | S1 source-dependent bindings | S2 | S1 conflict/STOP dependent effects; S2 unchanged |
| CXT7 | verified event resolves required UNKNOWN E | dependency closure of E | E-blocked bindings | independent bindings | UNKNOWN removed exact scope; dependents recomputed |
| CXT8 | unauthorized human claim H contradicts verified G | claim comparison scope | none from G solely due H | verified G | H retained unverified/conflicting; G unchanged |
| CXT9 | authorized OPERATOR decision event in S | decision/authority S | pending decision-dependent bindings | unrelated scopes | bounded authority binding updated |
| CXT10 | verified result changes next-gate condition | result/next-gate | G1 derivation | role/profile/independent experience | G2 derived; unrelated context stable |

## Recompute oracle

Every CXT fixture checks:
changed facts/evidence
-> changed_scopes
-> dependency traversal
-> invalidated_bindings
-> recomputed_bindings
-> preserved_unaffected_bindings
-> immutable resulting_context_id.

The oracle fails if:
- a stale dependent binding survives;
- an unrelated binding is recomputed without dependency;
- a full reset occurs without all-scope dependency;
- authority is created by context/delta/profile/experience/capability/human input.
