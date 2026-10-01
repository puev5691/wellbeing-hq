# SECE r0.1 Outcome Aggregation

status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
model: MULTI_OUTCOME_AGGREGATION

Preserve all simultaneous validator reasons and deterministically derive one effect decision, terminal class, and next-gate class. Construction order is not precedence.

Conflict predicates stop effect. Explicit rejected-action predicates reject the proposed action. Missing authority/writer/currentness blocks dependent effect. Required unknown evidence remains UNKNOWN. Observed FAIL remains FAIL. Only a clean valid action may be admitted.

All causal reasons remain recorded even when one aggregate class is selected.
