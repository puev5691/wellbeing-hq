# Dispatch KOO → RED: GitHub information-entry editorial gate

sender: koordinator
recipient: redaktor
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__github-info-entry-stageB-red__RED.md`
artifact_commit: `6025db6b3bae54da5b99b29190e7cad5ff6b153c`
artifact_blob: `98b3eab7de38eca90d7b9c712f0a371383df5a3f`

inbox_locator: `entities/redaktor/inbox/KOO__github-info-entry-stageB-red__RED.md`
inbox_commit: `ac1277087e0f7344203f1eb5c2dc327b44c47a52`
inbox_blob: `93d3fd2bb4ab3ad988d6fcc01d0087c58b947ad5`

required_result: bounded RED editorial lifecycle/readiness result or exact blocker
next_stage_if_accepted: KOO review → bounded WEB Stage B synthesis authorization
failure_mode: no WEB Stage B production or repository-setting action without RED result + KOO next-stage decision
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: Exchange Gate dispatch RED Stage B prerequisite
СТАТУС: dispatched
