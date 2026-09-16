# Dispatch: KOO → KOD / OpenAI Responses API D0 adapter r0.1

exchange_gate: v1
sender: koordinator
recipient: koder
artifact: entities/koordinator/outbox/KOO__openai-responses-d0-adapter-r01__KOD.md
artifact_commit: 73a7ccbc2a3728f69c123a3790129343325c4277
artifact_blob: 0472f621324885bc0bc6a8c02b69b45c8761def3
purpose: add a bounded D0 synthetic OpenAI Responses provider path to the existing provider-neutral gateway architecture
required_action: build and test credential-free default-deny adapter/transport candidate after fresh official-doc verification; no live call
expected_result: PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE or exact BLOCKED_/FAIL_ evidence routed to KOO
failure_mode: provider-doc drift, task identity mismatch, inability to preserve D0/secret/network boundaries, or unverifiable package/test identity
inbox_pointer: entities/koder/inbox/KOO__openai-responses-d0-adapter-r01__KOD.md
registry_record: registry/by-sender/koordinator.jsonl
status: dispatched
receipt:
