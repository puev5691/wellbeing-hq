# SECE_EXECUTION_CONTRACT_R01 outcome aggregation successor
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
basis_schema_blob: be67d382778c5ca096f2f1e6f05713516f977cfd

All predecessor fields and C1/C2/C3 structures remain unchanged.

Add VALIDATOR_OUTCOME_AGGREGATION:
- observed_predicates[]
- blocking_predicates[]
- conflict_predicates[]
- unknown_predicates[]
- rejected_action_predicates[]
- effect_decision
- primary_outcome
- secondary_reasons[] with reason_id, predicate_id, evidence_ref, scope, provenance
- terminal_class
- next_gate_class
- aggregation_rule_id
- provenance[]

Allowed effect_decision: ADMIT, REJECT, STOP, NO_EFFECT.
Allowed terminal_class: PASS, BLOCKED, FAIL, UNKNOWN.
Allowed next_gate_class: NONE, STOP, REQUEST_EVIDENCE, REQUEST_AUTHORITY, WRITER_GATE, CURRENTNESS_RECONCILIATION, CAUSAL_NEXT_GATE.

Invariants:
all true causal predicates retained;
aggregate primary outcome does not erase secondary reasons;
next gate requires exact active next-gate rule plus current verified state and Task Conveyor where applicable;
terminal/pass never creates approval, acceptance, task, writer or production authority.
