# Dispatch SIS → KOO: Telegram Phase 1B resume r0.5 fresh recheck

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-phase1b-resume-r05__KOO.md`
artifact_commit: `078e747a940dcc47fd6a2ee917842e52a6ddd5fb`
artifact_blob: `510aa64c3647e22e6f10374e0058947c8f9fb37a`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-phase1b-resume-r05__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return fresh Resume-First confirmation that Telegram Phase1B remains blocked by unchanged runtime threading defect`
required_action: `KOO route a corrected immutable runtime candidate to SIS only after KOD fixes the threaded SQLite boundary; do not repeat old sudo or unchanged v2 gate`
expected_result: `new immutable runtime candidate with threaded HTTP regression coverage, followed by fresh SIS non-production verification`
failure_mode: `if artifact commit/blob, inbox locator or sender registry mismatches, routing is invalid and no delivery/acceptance may be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: адресно вернуть KOO fresh r0.5 blocker без повторного sudo
СТАТУС: dispatched
