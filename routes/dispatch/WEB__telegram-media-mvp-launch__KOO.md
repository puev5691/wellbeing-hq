# WEB → KOO: Telegram media MVP implementation dispatch

exchange_gate: v1
sender: webmaster
recipient: koordinator
artifact: entities/webmaster/outbox/WEB__telegram-media-mvp-launch__KOO.md
artifact_commit: 741f5ea8e752cb9d62cd232c122f02bafb7cbb2d
artifact_blob: 67a82d7d160f20b0b0cf808245ef9c03d135ac7a
purpose: start bounded implementation cycle for Telegram channel, linked discussion group, automated publishing, comments/reactions/member metrics and safe feedback capture
required_action: review the architecture, open the implementation cycle, issue bounded KOD/SIS/KAN tasks, link RED editorial work, and return exact bootstrap/acceptance decisions
expected_result: working Phase 0 media-gateway package, Phase 1 private Telegram sandbox plan/runtime, profile boundaries, and explicit blockers/acceptance criteria
failure_mode: artifact or inbox locator inaccessible, immutable version mismatch, recipient unable to read, or route invalid
inbox_pointer: entities/koordinator/inbox/WEB__telegram-media-mvp-launch__KOO.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

Implementation boundary:
- Bot API MVP now;
- private/non-production Telegram sandbox before real project publication;
- MTProto user-session views/native stats only after separate SIS+KAN authority;
- no production send or token storage in GitHub authorized by this dispatch.

---
created_by: WEB
purpose_note: addressed technical launch request for Telegram media-gateway MVP
project_time: not_recorded_no_trusted_source