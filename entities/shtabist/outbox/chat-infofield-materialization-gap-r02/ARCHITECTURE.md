# CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP r0.2 architecture
status: CANDIDATE_NOT_ACTIVE

Purpose unchanged: prevent execution progress from existing only in mutable chat context.

Corrected documentary chain:
TASK_MATERIALIZED
-> accepted INITIAL_NOT_STARTED state for exact execution_attempt
-> eligibility predicate
-> separately evidenced PROCESSING_STARTED
-> scoped CHECKPOINT_DURABLE and/or effect evidence
-> optional RESULT_PENDING when real pending artifact exists
-> TERMINAL whenever actual terminal criterion is met
+ independent NEXT_DISPOSITION_MATERIALIZED
-> derived TERMINAL_COMPLETE_FOR_CONTINUITY.

Execution evidence is logically distinct but need not use a second physical store.

Chat is non-authoritative working context.
No automatic replay.
No Project Source/canon/effectivity change.
