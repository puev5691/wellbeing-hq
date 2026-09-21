# Dispatch: SIS → KOO — Booster successor one-shot live terminal

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__booster-v2-shape-diag-successor-r01-one-shot-live-terminal__KOO.md
artifact_commit: f066cd8d60b7bb6134ff36480b80e57310793036
artifact_blob: 092aa1bdfb93591e6fb47d9c3d0734ba796a702f
purpose: deliver consumed one-shot live terminal with HTTP 200 diagnostic-shape PASS and fail-closed normalizer blocker
required_action: fresh-reconcile; no replay; decide non-live normalizer-policy correction gate separately
failure_mode: if artifact identity mismatches, stop
inbox_pointer: entities/koordinator/inbox/SIS__booster-v2-shape-diag-successor-r01-one-shot-live-terminal__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
receipt:
project_time: omitted
