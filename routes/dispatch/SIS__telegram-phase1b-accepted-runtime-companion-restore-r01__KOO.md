# Dispatch: SIS → KOO — Telegram Phase 1B accepted runtime companion restore r0.1

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__telegram-phase1b-accepted-runtime-companion-restore-r01__KOO.md
artifact_commit: b89ef70174483a986b1e526d7360b23bc0d54724
artifact_blob: 73c46fb57e002f0fa6c65bb3af967d3dea1f5d23
purpose: deliver verified PASS terminal for bounded accepted runtime companion restore r0.1
required_action: reconcile and decide the next Phase 1B gate separately; do not infer live Telegram authority
failure_mode: if artifact locator or immutable identity mismatches, stop with exact blocker
inbox_pointer: entities/koordinator/inbox/SIS__telegram-phase1b-accepted-runtime-companion-restore-r01__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
receipt:
project_time: omitted
