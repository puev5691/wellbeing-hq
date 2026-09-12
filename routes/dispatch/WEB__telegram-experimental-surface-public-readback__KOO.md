# WEB → KOO: Telegram experimental surface public readback dispatch

exchange_gate: v1
sender: webmaster
recipient: koordinator
artifact: entities/webmaster/outbox/WEB__telegram-experimental-surface-public-readback__KOO.md
artifact_commit: 93b050d33a70da30ecb7ed00f8d7eb6bc2cac446
artifact_blob: 91afdb21bb78de660bfda6278ed6570f75572afb
purpose: return read-only verification of the approved Telegram experimental channel public web surface
required_action: use verified public-state facts in Phase 1 planning while leaving admin control, numeric chat ids, discussion linkage and bot state fail-closed until Telegram-side evidence exists
expected_result: KOO Phase 1 planning consumes `PUBLIC_VERIFIED` channel state without inventing unavailable Telegram-side admin/mapping facts
failure_mode: artifact or inbox locator inaccessible, immutable version mismatch, recipient unable to read, or route invalid
inbox_pointer: entities/koordinator/inbox/WEB__telegram-experimental-surface-public-readback__KOO.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

No Telegram write action or production publication is authorized by this dispatch.

---
created_by: WEB
project_time: not_recorded_no_trusted_source