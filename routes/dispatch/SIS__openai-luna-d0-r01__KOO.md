# Dispatch SIS → KOO: OpenAI Luna one-shot D0 r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__openai-luna-d0-r01__KOO.md`
artifact_commit: `28f92b1a72b96fefcb991d1ecccfd57752330301`
artifact_blob: `a0c4ba47c522bfb8c43b669f280de6a5be7b17a7`
inbox_pointer: `entities/koordinator/inbox/SIS__openai-luna-d0-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return verified exact-one-call OpenAI Luna D0 PASS`
required_action: `review PASS_SIS_OPENAI_LUNA_D0_R01; one-call authority is consumed`
expected_result: `receipt/acceptance or separate comparative probe task`
failure_mode: `if artifact identity or inbox pointer mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
