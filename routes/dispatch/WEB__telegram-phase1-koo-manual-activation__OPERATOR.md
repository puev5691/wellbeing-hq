# WEB → OPERATOR: combined Telegram KOO activation dependency dispatch

exchange_gate: v1
sender: webmaster
recipient: operator
artifact: entities/webmaster/outbox/WEB__telegram-phase1-koo-manual-activation__OPERATOR.md
artifact_commit: 6fec6350b442ce225e3925035666c595dbe7d3d7
artifact_blob: 7f76c71474791fb9984cb47e6c72c9185b3e8183
purpose: remove the exact-entity-chat activation blocker for both delivered KOO Telegram Phase 0 verification and Phase 1 surface-mapping inputs
required_action: manually activate the existing KOO chat once and instruct it to process `WEB__telegram-phase0-verify-phase1-mapping__KOO.md` and `WEB__telegram-experimental-surface-public-readback__KOO.md`; no file transfer required
expected_result: KOO records Phase 0 acceptance/revision and issues the next bounded Phase 1 tasks or exact blocker using the verified experimental-surface facts
failure_mode: OPERATOR cannot access KOO chat, KOO cannot read one of the existing inbox locators, or activation boundary changes
inbox_pointer: entities/operator/inbox/WEB__telegram-phase1-koo-manual-activation__OPERATOR.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

---
created_by: WEB
project_time: not_recorded_no_trusted_source