# SECE r0.1 simulator positive controls P1-P7

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

Canonical machine records are in FIXTURE-CATALOG.json.

## P1 — clean valid context/action
Input:
current task + required writer + exact authority binding + ACTIVE verified source + satisfied preconditions + no conflict/UNKNOWN/fail.

Expected:
ADMIT candidate -> AGG-R6 -> effect_decision ADMIT -> validator terminal PASS -> CAUSAL_NEXT_GATE to RuntimeStepGuardSimulator.

PASS is validator admission only.

## P2 — required handoff to another Entity
Input:
CAUSAL_EVENT handoff recipient != current decision recipient;
causal_requirement_status=REQUIRED;
valid action binding/preconditions.

Expected:
redundant_self_handoff=NO;
ADMIT under AGG-R6;
synthetic handoff ACTION_EVENT may be emitted by RuntimeStepGuardSimulator.
No delivery/receipt/processing inference.

## P3 — verified delta refines recovery exact scope
Input:
recovery R for scopes S/U;
verified delta D relation=REFINES R for S;
selected_current_basis S=D.

Expected:
D selected for S;
R invalidated only for current bindings depending on R:S;
R preserved for U/history;
no global reset.

## P4 — recovery remains applicable outside refined scope
Input:
same R/D context.

Expected:
R remains applicable evidence outside refined scope;
no automatic recovery precedence inside S.

## P5 — experience suggests allowed action; authority still required
Input:
experience recommends action A;
A is not forbidden;
exact current authority binding exists.

Expected:
experience remains advisory;
A admission depends on authority binding and all normal gates;
with binding present and clean context -> ADMIT.
Mutation removing authority_ref must reject.

## P6 — one scope changes; unrelated scope preserved
Input:
verified event changes dependency in S1; S2 independent.

Expected:
only S1 dependency closure invalidated/recomputed;
S2 binding identity/reference preserved;
resulting context immutable successor.

## P7 — bounded L6 projection firewall
Input:
EFFECTIVE_CONTEXT contains facts F1,F2 and binding B1 for selected scope; ACTION_INTENT A.

Expected:
projection_basis is subset of {F1,F2,B1};
only additional semantic object is ACTION_INTENT A;
attempt to add F3 absent from EFFECTIVE_CONTEXT => projection invalid before L7.
