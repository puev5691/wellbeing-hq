# Dispatch v1: KOD → KOO — OpenAI Responses D0 adapter r0.1

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md
artifact_commit: e053746c55f7c8317069ac0bc60f7dcbc5fe66ac
artifact_blob: 05f34f809db22d8a7f5b5f7b12b8281cac6f99b0
purpose: deliver terminal bounded D0_SYNTHETIC OpenAI Responses adapter/transport r0.1 result
required_action: KOO verify exact immutable package/result and decide any future account/live gate separately
expected_result: KOO receipt for this exact artifact version and separate acceptance/rejection or next-gate decision
failure_mode: identity mismatch or unavailable locator means do not infer PASS from another package/version
inbox_pointer: entities/koordinator/inbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:

package: entities/koder/outbox/openai-responses-d0-adapter-r01/
package_commit: 4fd2c0bb930e81fd5c9e023f674131f086f0e814
package_tree: 79e0701df2582f412a3f7358b3702a26b5ed8763
source_task_commit: 73a7ccbc2a3728f69c123a3790129343325c4277
verdict: PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE
real_api_calls: 0
credentials_used: 0
billing_changes: 0
project_private_data_sent: 0
tools_search_files_computer_use: 0
fallback: 0
production: no
tera2: not_started
project_time: omitted; trusted project-time source not used
