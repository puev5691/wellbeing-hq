# Dispatch SIS → KOD: shard gateway adapter r0.1 independent verify

exchange_gate: v1
sender: `sisadmin`
recipient: `koder`
artifact: `entities/sisadmin/outbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO-KOD.md`
artifact_commit: `294564fe0d25d6c8e33d51975c62a00823fe2cd7`
artifact_blob: `33c7ccb07ec599507df5c7f8faae1ddd59ed3543`
inbox_pointer: `entities/koder/inbox/SIS__shard-gateway-adapter-r01-independent-verify__KOD.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return exact required edits for immutable shard gateway adapter candidate r0.1`
required_action: `correct the four verified deviations and publish a new immutable candidate`
expected_result: `corrected immutable candidate with deterministic tests`
failure_mode: `do not mutate or rewrite the r0.1 candidate; publish successor bytes`
status: `dispatched`
project_time: omitted
