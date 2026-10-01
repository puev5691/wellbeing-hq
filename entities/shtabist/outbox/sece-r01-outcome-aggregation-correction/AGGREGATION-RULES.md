# SECE r0.1 Outcome Aggregation Rules
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

VALIDATOR_OUTCOME_AGGREGATION fields:
observed_predicates[]
blocking_predicates[]
conflict_predicates[]
unknown_predicates[]
rejected_action_predicates[]
effect_decision: ADMIT|REJECT|STOP|NO_EFFECT
primary_outcome: AGGREGATE_CLEAR|AGGREGATE_CONFLICT_STOP|AGGREGATE_REJECTED|AGGREGATE_BLOCKED|AGGREGATE_UNKNOWN|AGGREGATE_FAIL
secondary_reasons[]
terminal_class: PASS|BLOCKED|FAIL|UNKNOWN
next_gate_class: NONE|STOP|REQUEST_EVIDENCE|REQUEST_AUTHORITY|WRITER_GATE|CURRENTNESS_RECONCILIATION|CAUSAL_NEXT_GATE
aggregation_rule_id
provenance[]

AGG-R1 CONFLICT:
SOURCE_CONFLICT_STOP or CURRENT_STATE_CONFLICT_STOP => effect STOP; outcome AGGREGATE_CONFLICT_STOP; terminal BLOCKED. Other reasons preserved. Next STOP unless exact active conflict-resolution gate exists.

AGG-R2 REJECT:
Else REJECT_FORBIDDEN or REJECT_ACTION_AUTHORIZATION_BINDING or REJECT_PRECONDITION or REJECT_REDUNDANT_SELF_HANDOFF => effect REJECT; outcome AGGREGATE_REJECTED; terminal BLOCKED. Next gate only from active rules/current verified state.

AGG-R3 BLOCKED:
Else BLOCKED_AUTHORITY or BLOCKED_WRITER or BLOCKED_CURRENTNESS => NO_EFFECT; AGGREGATE_BLOCKED; BLOCKED. All blockers preserved. Gate must be causally derived, never selected by list order.

AGG-R4 UNKNOWN:
Else UNKNOWN_REQUIRED_EVIDENCE or required UNKNOWN => NO_EFFECT; AGGREGATE_UNKNOWN; UNKNOWN. REQUEST_EVIDENCE only if exact missing evidence is identifiable and request is permitted.

AGG-R5 FAIL:
Else observed FAIL => NO_EFFECT; AGGREGATE_FAIL; FAIL. Next gate only from active rules/current state.

AGG-R6 ADMIT:
Else clean ADMIT with no conflict/reject/blocker/unknown/fail => ADMIT; AGGREGATE_CLEAR; PASS for validator-admission criterion only. It does not imply task completion, approval, acceptance or production authority.

AGG-R7:
PASS never overrides conflict/reject/blocker/unknown/fail.

These rules are architecture-local aggregation semantics, not Project Source precedence. Every true causal predicate remains in the reason set.
