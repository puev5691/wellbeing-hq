# SECE r0.1 Effective Context architecture clarification
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

L0-L9 topology unchanged. C1/C2/C3 unchanged. MULTI_OUTCOME_AGGREGATION unchanged.

Local placement:
L1-L5 composition progressively supplies semantic atoms, current bindings, profile and advisory experience.
After L5, Context Composer produces EFFECTIVE_CONTEXT.
L6 projects one bounded SEMANTIC_EXECUTION_CONTRACT from EFFECTIVE_CONTEXT for one proposed next step.
L7 validates that proposed transition and applies local MULTI_OUTCOME_AGGREGATION only to simultaneous validator predicates for that transition.
L8 performs one safe step after revalidation.
L9 emits RESULT/EVENT and, when verified, CONTEXT_DELTA input for successor EFFECTIVE_CONTEXT.

CONTEXT COMPOSITION != L7 OUTCOME AGGREGATION.
Composition maintains evolving Entity context and parallel semantic lines.
Aggregation collapses validator predicates for one proposed transition to one effect decision while preserving causal reasons.

No cross-layer leakage.
