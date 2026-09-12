# WEB → OPERATOR: Telegram Phase 0 KOD activation dependency dispatch

exchange_gate: v1
sender: webmaster
recipient: operator
artifact: entities/webmaster/outbox/WEB__telegram-phase0-kod-manual-activation__OPERATOR.md
artifact_commit: a580416f2a2a8608c8d632d50b994ca40e707456
artifact_blob: 8ea6c0628c26a55022d3e8f643af4a709f21c3e9
purpose: remove the exact-entity-chat activation blocker for already assigned Telegram Media Gateway Phase 0 KOD task
required_action: manually activate the existing KOD chat and instruct it to process `KOO__telegram-media-phase0__KOD.md`; no file transfer required
expected_result: KOD starts Phase 0 and returns immutable credential-free package or exact blocker to KOO
failure_mode: OPERATOR cannot access KOD chat, KOD cannot read existing inbox locator, or activation boundary changes
inbox_pointer: entities/operator/inbox/WEB__telegram-phase0-kod-manual-activation__OPERATOR.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

---
created_by: WEB
project_time: not_recorded_no_trusted_source