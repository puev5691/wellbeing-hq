# Dispatch SIS → KOO: OpenAI four-model cost matrix r0.2 terminal result

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__openai-cost-matrix-r02__KOO-KOD.md`
artifact_commit: `4744028f96d6453abaf4a7987a6328ad43b619d8`
artifact_blob: `8eae38796fdccd9f9a7f516c91abfe2044ce6998`
inbox_pointer: `entities/koordinator/inbox/SIS__openai-cost-matrix-r02__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return terminal PASS_SIS_OPENAI_COST_MATRIX_R02 with safe four-model entitlement/usage/cost metadata`
required_action: `review terminal result and reconcile active queue`
expected_result: `receipt and subsequent coordination decision if needed`
failure_mode: `if artifact identity or inbox pointer mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
