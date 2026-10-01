# SECE r0.1 validator predicates and reviewed L7 aggregation

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Predicate/outcome vocabulary

Closed validator predicate set used by fixtures includes at minimum:

ADMIT
REJECT_ACTION_AUTHORIZATION_BINDING
REJECT_FORBIDDEN
REJECT_PRECONDITION
REJECT_REDUNDANT_SELF_HANDOFF
SOURCE_CONFLICT_STOP
CURRENT_STATE_CONFLICT_STOP
UNKNOWN_REQUIRED_EVIDENCE
BLOCKED_AUTHORITY
BLOCKED_WRITER
BLOCKED_CURRENTNESS
FAIL
UNKNOWN

PASS is a scoped result/terminal class, not a permission source.

## Aggregate object

VALIDATOR_OUTCOME_AGGREGATION:
- observed_predicates[]
- blocking_predicates[]
- conflict_predicates[]
- unknown_predicates[]
- rejected_action_predicates[]
- effect_decision: ADMIT|REJECT|STOP|NO_EFFECT
- primary_outcome:
  AGGREGATE_CLEAR|AGGREGATE_CONFLICT_STOP|AGGREGATE_REJECTED|
  AGGREGATE_BLOCKED|AGGREGATE_UNKNOWN|AGGREGATE_FAIL
- secondary_reasons[]
- terminal_class: PASS|BLOCKED|FAIL|UNKNOWN
- next_gate_class:
  NONE|STOP|REQUEST_EVIDENCE|REQUEST_AUTHORITY|WRITER_GATE|
  CURRENTNESS_RECONCILIATION|CAUSAL_NEXT_GATE
- aggregation_rule_id
- provenance[]

Each secondary reason:
reason_id, predicate_id, evidence_ref, scope, provenance.

## Reviewed local L7 mapping

AGG-R1 CONFLICT:
If SOURCE_CONFLICT_STOP or CURRENT_STATE_CONFLICT_STOP is true:
effect_decision=STOP
primary_outcome=AGGREGATE_CONFLICT_STOP
terminal_class=BLOCKED
next_gate_class=STOP unless an exact active conflict-resolution gate is separately established.
All other true reasons remain secondary.

AGG-R2 REJECT:
Else if any of:
REJECT_FORBIDDEN,
REJECT_ACTION_AUTHORIZATION_BINDING,
REJECT_PRECONDITION,
REJECT_REDUNDANT_SELF_HANDOFF:
effect_decision=REJECT
primary_outcome=AGGREGATE_REJECTED
terminal_class=BLOCKED
next gate only from exact active rules/current verified state.

AGG-R3 BLOCKED:
Else if BLOCKED_AUTHORITY/BLOCKED_WRITER/BLOCKED_CURRENTNESS:
effect_decision=NO_EFFECT
primary_outcome=AGGREGATE_BLOCKED
terminal_class=BLOCKED.
All blockers remain reasons.
Gate is causally derived, never selected by list order.

AGG-R4 UNKNOWN:
Else if UNKNOWN_REQUIRED_EVIDENCE or required UNKNOWN:
effect_decision=NO_EFFECT
primary_outcome=AGGREGATE_UNKNOWN
terminal_class=UNKNOWN.
REQUEST_EVIDENCE only when exact evidence is identifiable and request permitted.

AGG-R5 FAIL:
Else if observed FAIL:
effect_decision=NO_EFFECT
primary_outcome=AGGREGATE_FAIL
terminal_class=FAIL.

AGG-R6 ADMIT:
Only if no conflict/reject/blocker/unknown/fail:
effect_decision=ADMIT
primary_outcome=AGGREGATE_CLEAR
terminal_class=PASS for validator admission criterion only.

AGG-R7 boundary:
PASS never overrides conflict/reject/blocker/unknown/fail.

## Boundary

This ordering is architecture-local classification for one proposed transition only.
It is not:
- source precedence;
- Project Source/canon precedence;
- global context composition;
- authority;
- task currentness;
- writer;
- approval;
- acceptance;
- production authority.

All true causal reasons remain in trace/secondary_reasons.
