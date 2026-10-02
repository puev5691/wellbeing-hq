# SECE r0.1 affected fixture binding-derivation report

status: PASS
project_time: omitted

Generic derivation:
changed_source_ids
-> dependency_edges fixed-point traversal
-> invalidated set
-> recomputation_rules
-> recomputed set
-> initial bindings minus invalidated
-> preserved set.

The actual sets below were produced from typed input only.
Expected sets were read only after actual derivation for FixtureOracle comparison.

| Fixture | changed_source_ids | invalidated actual | recomputed actual | preserved actual | Match |
|---|---|---|---|---|---|
| CXT1 | CXT1-TARGET | [] | [] | BINDING_EVIDENCE_REQUIREMENT, BINDING_MAY_INSPECT, BINDING_MUST_NOT_MUTATE, BINDING_UNKNOWN_CONSUMER | PASS |
| CXT2 | CXT2-TARGET | BINDING_EXECUTABLE_MUTATE_FROM_EXPERIENCE | BINDING_MUTATE_FORBIDDEN | BINDING_EXPERIENCE_ADVISORY, BINDING_UNRELATED_CONTEXT | PASS |
| CXT3 | CXT3-TARGET | BINDING_RECOVERY_CURRENT_S | BINDING_CURRENT_S_SELECTED_DELTA | BINDING_RECOVERY_HISTORY, BINDING_RECOVERY_U | PASS |
| CXT4 | CXT4-TARGET | BINDING_TASK_T_CURRENT, BINDING_TASK_T_EXECUTABLE | BINDING_TASK_T_SUPERSEDED | BINDING_SCOPE_U | PASS |
| CXT5 | CXT5-TARGET | BINDING_ACTION_A_PENDING | BINDING_ACTION_A_AUTHORITY_CURRENT | BINDING_ACTION_B, BINDING_UNRELATED_SCOPE | PASS |
| CXT6 | CXT6-TARGET | BINDING_S1_SOURCE_DEPENDENT | BINDING_S1_CONFLICT_BLOCKED | BINDING_S2 | PASS |
| CXT7 | CXT7-TARGET | BINDING_E_BLOCKED | BINDING_E_RESOLVED | BINDING_INDEPENDENT | PASS |
| CXT8 | CXT8-TARGET | [] | [] | BINDING_VERIFIED_G | PASS |
| CXT9 | CXT9-TARGET | BINDING_DECISION_PENDING_S | BINDING_AUTHORITY_CURRENT_S | BINDING_UNRELATED_SCOPE | PASS |
| CXT10 | CXT10-TARGET | BINDING_NEXT_GATE_G1 | BINDING_NEXT_GATE_G2 | BINDING_INDEPENDENT_EXPERIENCE, BINDING_PROFILE, BINDING_ROLE | PASS |
| P3 | D | BINDING_RECOVERY_CURRENT_S | BINDING_CURRENT_S_SELECTED_DELTA | BINDING_RECOVERY_U | PASS |
| P4 | [] | [] | [] | BINDING_RECOVERY_U | PASS |
| P6 | F-DEP | BINDING_S1_DEPENDENT_OLD | BINDING_S1_DEPENDENT_NEW | BINDING_S2 | PASS |
| M6 | S1 | BINDING_S1_SOURCE_DEPENDENT | BINDING_S1_CONFLICT_BLOCKED | BINDING_S2 | PASS |
| M8 | A1 | BINDING_DEPENDENT_A1 | BINDING_DEPENDENT_A1_RECOMPUTED | BINDING_INDEPENDENT | PASS |

## Representative paths

### CXT3

Typed initial state contains:
- BINDING_RECOVERY_CURRENT_S dependent on CXT3-TARGET;
- BINDING_RECOVERY_U independent;
- BINDING_RECOVERY_HISTORY independent;
- recomputation rule maps invalidated BINDING_RECOVERY_CURRENT_S to BINDING_CURRENT_S_SELECTED_DELTA.

Trigger/change marks CXT3-TARGET changed.

Generic traversal:
CXT3-TARGET
-> BINDING_RECOVERY_CURRENT_S invalidated
-> recomputation rule
-> BINDING_CURRENT_S_SELECTED_DELTA recomputed.

Unrelated recovery U/history remain preserved.

### CXT6

Typed initial state contains:
- BINDING_S1_SOURCE_DEPENDENT dependent on CXT6-TARGET;
- BINDING_S2 independent;
- recomputation rule emits BINDING_S1_CONFLICT_BLOCKED.

Generic traversal derives the exact three sets with no scope lookup table.

### P6

Typed initial state contains:
- source F-DEP;
- BINDING_S1_DEPENDENT_OLD dependent on F-DEP;
- BINDING_S2 independent;
- recomputation rule emits BINDING_S1_DEPENDENT_NEW.

Generic traversal derives expected sets.

### M8

Typed base state is non-null and contains:
- source A1;
- BINDING_DEPENDENT_A1 dependent on A1;
- BINDING_INDEPENDENT independent;
- recomputation rule emits BINDING_DEPENDENT_A1_RECOMPUTED.

The typed transformation changes dependency atom A1.
Generic traversal derives exact sets.

## Closure

INPUT_COMPLETE_FOR_BINDING_DERIVATION=YES for:
CXT1,CXT2,CXT3,CXT4,CXT5,CXT6,CXT7,CXT8,CXT9,CXT10,P3,P4,P6,M6,M8.

AFFECTED_FIXTURES_INPUT_COMPLETE=15/15
BINDING_SET_OUTPUTS_DERIVABLE_FROM_TYPED_INPUT=15/15
MUTATION_BASE_STATE_COMPLETE_M6_M8=YES
