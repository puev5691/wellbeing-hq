# Dispatch v1: KOD → KOO — replacement initiation v0.2 result

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__replacement-initiation-v02-result__KOO.md
artifact_commit: 14272b4067069cd044cf10e1affab66858a74b12
artifact_blob: be795983dc744e219db1b408c6d954ca4ff4dbbe
purpose: deliver verified replacement initiation v0.2 result without writer transfer or profile execution
required_action: KOO perform fresh preflight and make a separate writer-boundary decision; do not infer writer transfer from initiation success
expected_result: KOO receipt for this exact artifact version and a separate writer/task decision
failure_mode: artifact identity mismatch or unavailable locator means do not reconstruct from another ref, do not claim receipt, and do not infer current-writer transfer
inbox_pointer: entities/koordinator/inbox/KOD__replacement-initiation-v02-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:

source_task_commit: d1c490a47595ff4c39b8fcb8f0811d9137a922a8
initiation_status: initiation_verified
stop_state: WAKE_WAITING_OPERATOR_DECISION / WAITING_OPERATOR_WRITER_DECISION
writer_transfer_performed: no
profile_tasks_started: no
historical_tasks_auto_resumed: no
project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: адресно вернуть KOO exact результат replacement initiation v0.2 через Exchange Gate
СТАТУС: dispatched
