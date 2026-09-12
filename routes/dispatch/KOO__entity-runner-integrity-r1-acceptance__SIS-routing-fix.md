# Dispatch correction KOO → SIS: Entity Runner integrity PASS

sender: koordinator
recipient: sisadmin
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`
artifact_commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
artifact_blob: `a3b4140c3cacf03a34d199ade97c1cf6c72de20d`

active_inbox_locator: `entities/sisadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`
active_inbox_commit: `1ecf7f65f92fc916c8f23be400f9863bd1f19296`
active_inbox_blob: `2ce3f48f3c1ac5e04555d44fc6f2f78ebe3c5485`

superseded_route_for_delivery_only:
`entities/sysadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`

reason:
The prior repository locator was placed in a non-current SIS inbox path. This correction preserves the prior object as provenance and establishes the active addressed route under `entities/sisadmin/inbox/`.

next_stage: bounded SIS host/runtime-probe preparation only
provider_side_action_authorized: no
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить Exchange Gate routing без переписывания исторического misroute
СТАТУС: dispatched_routing_fix
