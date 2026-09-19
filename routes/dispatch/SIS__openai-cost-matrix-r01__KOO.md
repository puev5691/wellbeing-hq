# Dispatch SIS → KOO: OpenAI comparative cost matrix r0.1 blocker

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__openai-cost-matrix-r01__KOO-KOD.md`
artifact_commit: `8139700f5f31523073d7bbe3ee93e393308d0775`
artifact_blob: `b267752067b32f355345892992f4f163ccd6cc9e`
inbox_pointer: `entities/koordinator/inbox/SIS__openai-cost-matrix-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return precall blocker: Astra absent from verified runtime allowlist`
required_action: `review BLOCKED_OPENAI_COST_MATRIX_ASTRA_NOT_IN_VERIFIED_RUNTIME_ALLOWLIST and provide exact unblock if authorized`
expected_result: `receipt/acceptance or immutable four-model runtime task/package`
failure_mode: `if artifact identity or inbox pointer mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
