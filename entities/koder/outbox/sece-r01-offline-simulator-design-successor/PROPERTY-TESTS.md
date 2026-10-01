# SECE r0.1 simulator mutation/property tests

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

Canonical machine records M1-M12 are in FIXTURE-CATALOG.json.

| ID | Mutation | Required property |
|---|---|---|
| M1 | remove authority_ref from P1 | authority-sensitive action emits REJECT_ACTION_AUTHORIZATION_BINDING/BLOCKED_AUTHORITY; no effect |
| M2 | ACTIVE source -> CANDIDATE | normative use rejected; candidate does not become active |
| M3 | CURRENT task -> SUPERSEDED | dependent action rejected; currentness reason preserved |
| M4 | processing_started YES -> UNKNOWN | no RUNNING inference; UNKNOWN_REQUIRED_EVIDENCE retained |
| M5 | add CURRENT_STATE_EVIDENCE unresolved conflict | CURRENT_STATE_CONFLICT_STOP; AGG-R1; no effect |
| M6 | add source conflict only S1 | S1 dependents invalidated; S2 preserved |
| M7 | change experience ranking/content | authority outcome unchanged |
| M8 | change one dependency atom | only dependency closure recomputes |
| M9 | remove projection_basis fact from EFFECTIVE_CONTEXT | projection invalid; L7 not reached |
| M10 | contract introduces context fact absent from EFFECTIVE_CONTEXT | projection rejected; no invented context |
| M11 | required other-Entity handoff -> KOO->KOO with NOT_REQUIRED causal need | REJECT_REDUNDANT_SELF_HANDOFF |
| M12 | combine authority+writer+currentness blockers | AGG-R3; all three reasons remain in secondary_reasons |

## General property invariants

1. Adding advisory experience cannot add authority.
2. Removing evidence cannot make a dependent predicate more certain.
3. Reordering set-like fixture arrays cannot change canonical context/contract/trace identities.
4. Independent scope mutations cannot change unrelated binding identities.
5. A context correction never edits prior immutable context.
6. A delta with unverified trigger cannot become applicable successor state.
7. Aggregation never erases true predicates.
8. ADMIT is impossible while any conflict/reject/blocker/required-UNKNOWN/fail predicate remains.
9. RuntimeStepGuardSimulator cannot create real side effect under any fixture.
10. Neural injected proposal and deterministic handwritten ACTION_INTENT with identical canonical fields produce identical validation output.
