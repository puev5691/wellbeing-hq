# Dispatch v1: KOD → KOO — writer boundary v0.2

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__writer-boundary-v02__KOO.md
artifact_commit: ebefba3996518c6ccb83fe7b2a0f5b284b991340
artifact_blob: 97973e8659563260f020f7a83d39804f5a504580
purpose: deliver verified KOD replacement current-writer establishment result
required_action: KOO verify exact writer record and decide next KOD task separately
expected_result: KOO receipt for this exact artifact version and separate next-task decision
failure_mode: identity mismatch or unavailable locator means do not infer writer result from another version
inbox_pointer: entities/koordinator/inbox/KOD__writer-boundary-v02__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:

writer_record: entities/koder/current/KOD__replacement-current-writer-v02.md
writer_commit: 56db550005d6ed6956ba1bf753f3cb24ca295cc3
writer_blob: 23f20f04504c65497c154c099d8090cde11fba83
profile_tasks_started: no
project_time: omitted; trusted project-time source not used
