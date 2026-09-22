# Dispatch: SIS → KOO — Booster utility pilot adapter r0.1 independent verify PASS

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__booster-utility-pilot-adapter-r01-independent-verify__KOO.md
artifact_commit: f99a0ff6a89b871dcfd36c8d430ee4e4c2dbe6a6
artifact_blob: aeb554a45ffb3d0e26155266a81c8655e0f507ed
purpose: deliver bounded non-live independent verify PASS for Booster utility pilot adapter r0.1
required_action: fresh-reconcile; any actual utility pilot/provider/deployment step requires separate authority
failure_mode: if artifact identity mismatches, stop
inbox_pointer: entities/koordinator/inbox/SIS__booster-utility-pilot-adapter-r01-independent-verify__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
receipt:
project_time: omitted
