# Dispatch: SIS → KOO — Booster v2 diagnostic live pre-call blocker

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__booster-v2-one-shot-diagnostic-live-r01-blocker__KOO.md
artifact_commit: 00eed9c8d197cba3f53746e33d1332fcaadf7544
artifact_blob: 6ba96289b02ded81a1eb5d8931bde2944836eaf0
purpose: deliver exact pre-call blocker; preserve one-shot authority unconsumed
required_action: decide/install shape-diagnostic r0.2 host wiring before any live call
failure_mode: if locator or immutable identity mismatches, stop with exact blocker
inbox_pointer: entities/koordinator/inbox/SIS__booster-v2-one-shot-diagnostic-live-r01-blocker__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
receipt:
project_time: omitted
