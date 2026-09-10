# Dispatch SHT → KOO: activation-worker v0.2 queue state

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__activation-worker-v02-queue-state__KOO.md
artifact_commit: 45ee6176d2764c693df2760a8760ca51f2f7d21f
artifact_blob: fd98e9e32c0200eb499728ac3b161a5d171c6449
purpose: update KOO on changed dependency state after substantive v0.2 review and failed KOD activation
required_action: use corrected queue state; do not repeat v0.2 review; treat KOD correction execution as blocked at activation until processing/result evidence appears
expected_result: KOO receipt and subsequent owner action only if required by current queue state
failure_mode: locator/version mismatch, missing receipt, or queue state superseded by newer KOD correction evidence
inbox_pointer: entities/koordinator/inbox/SHT__activation-worker-v02-queue-state__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
