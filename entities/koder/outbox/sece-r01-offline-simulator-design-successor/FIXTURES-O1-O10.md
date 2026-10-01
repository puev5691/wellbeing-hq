# SECE r0.1 simulator simultaneous outcome fixtures O1-O10

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

These fixtures are exact projections of the independently reviewed L7 MULTI_OUTCOME_AGGREGATION family. Canonical records are in FIXTURE-CATALOG.json.

| ID | Simultaneous predicates | Rule | effect_decision | primary_outcome | terminal | next gate | Required secondary reasons |
|---|---|---|---|---|---|---|---|
| O1 | SOURCE_CONFLICT_STOP + BLOCKED_AUTHORITY | AGG-R1 | STOP | AGGREGATE_CONFLICT_STOP | BLOCKED | STOP | both |
| O2 | CURRENT_STATE_CONFLICT_STOP + REJECT_REDUNDANT_SELF_HANDOFF | AGG-R1 | STOP | AGGREGATE_CONFLICT_STOP | BLOCKED | STOP | both |
| O3 | UNKNOWN_REQUIRED_EVIDENCE + REJECT_FORBIDDEN | AGG-R2 | REJECT | AGGREGATE_REJECTED | BLOCKED | NONE | forbidden + UNKNOWN preserved |
| O4 | BLOCKED_WRITER + BLOCKED_CURRENTNESS | AGG-R3 | NO_EFFECT | AGGREGATE_BLOCKED | BLOCKED | CURRENTNESS_RECONCILIATION | both |
| O5 | BLOCKED_AUTHORITY + REJECT_PRECONDITION | AGG-R2 | REJECT | AGGREGATE_REJECTED | BLOCKED | NONE | both |
| O6 | REJECT_FORBIDDEN + valid authority evidence | AGG-R2 | REJECT | AGGREGATE_REJECTED | BLOCKED | NONE | forbidden + valid authority |
| O7 | UNKNOWN_REQUIRED_EVIDENCE + valid authority evidence | AGG-R4 | NO_EFFECT | AGGREGATE_UNKNOWN | UNKNOWN | REQUEST_EVIDENCE | UNKNOWN + valid authority |
| O8 | BLOCKED_AUTHORITY + BLOCKED_WRITER + BLOCKED_CURRENTNESS | AGG-R3 | NO_EFFECT | AGGREGATE_BLOCKED | BLOCKED | CURRENTNESS_RECONCILIATION | all three |
| O9 | clean valid action/all gates valid | AGG-R6 | ADMIT | AGGREGATE_CLEAR | PASS | CAUSAL_NEXT_GATE | valid bindings/preconditions/currentness |
| O10 | REJECT_REDUNDANT_SELF_HANDOFF + otherwise valid context | AGG-R2 | REJECT | AGGREGATE_REJECTED | BLOCKED | CAUSAL_NEXT_GATE | rejection + otherwise-valid evidence |

## Boundary

AGG-R ordering is used only to classify the predicate set for one transition.
It must never:
- select an active source;
- overwrite EFFECTIVE_CONTEXT;
- resolve unrelated context collisions;
- create authority/currentness/writer;
- erase any simultaneous causal reason.
