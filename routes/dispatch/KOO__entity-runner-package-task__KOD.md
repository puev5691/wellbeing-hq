# Dispatch KOO → KOD: Entity Runner package task

sender: koordinator
recipient: koder
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__entity-runner-package-task__KOD.md`
artifact_commit: `4fbd3559210fcc483f1051b0d1e6efcf83cf4fbe`
artifact_blob: `98cb8fec135b97a917cb882740e972672224f3e9`

inbox_locator: `entities/koder/inbox/KOO__entity-runner-package-task__KOD.md`
inbox_commit: `5355cc40bf9fdf2a0d2551f6822b6abb88e33fde`
inbox_blob: `91a2a16b812582253a7d71c997c12cd648777607`

required_result: immutable bounded runner-package candidate or exact blocker
failure_mode: do not install runtime packages or request credentials
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: Exchange Gate dispatch runner-package task KOD
СТАТУС: dispatched
