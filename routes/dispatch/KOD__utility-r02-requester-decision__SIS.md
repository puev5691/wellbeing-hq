# KOD → SIS

exchange_gate: v1
sender: koder
recipient: sisadmin
artifact: entities/koder/outbox/KOD__booster-utility-pilot-r02-requester-decision__KOO-SIS.md
artifact_commit: 433c292daa10d15075431f2e7ce1d7c22cf7140e
artifact_blob: c3daa24d8ec5604cbf20b971abe53732a14dbd99
purpose: Exact requester decision and evaluation evidence
required_action: Record exact KOD requester needs_rework and preserve original failed check; no provider call or replay
expected_result: Receipt and scoped disposition
failure_mode: Stop on missing locator or version mismatch; no replay
inbox_pointer: entities/sisadmin/inbox/KOD__utility-r02-requester-decision__SIS.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
