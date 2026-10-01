# SECE r0.1 architecture local correction
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

L0-L9 topology unchanged. C1/C2/C3 unchanged.

L7 Static Validator emits the full simultaneous predicate set rather than first-match return, then applies MULTI_OUTCOME_AGGREGATION to derive effect decision, aggregate outcome and terminal class while retaining all causal reasons.

L9 derives NEXT_GATE only after aggregation and only from active NEXT_GATE rules, current verified state and Task Conveyor where applicable. Aggregation rule order is not source/rule precedence.

Human causal view renders the aggregate result plus material causal reasons from the same contract/result.

No runtime or simulator implementation is authorized.
