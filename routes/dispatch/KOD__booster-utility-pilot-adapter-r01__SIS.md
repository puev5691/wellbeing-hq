# KOD → SIS: offline utility adapter r01

exchange_gate: v1
sender: koder
recipient: sisadmin
artifact: entities/koder/outbox/KOD__booster-utility-pilot-adapter-r01-result__KOO-SIS.md
artifact_commit: a4101452f864ede1d194e5b74c1af9af70244415
artifact_blob: 9a876fe5f3183c284762f6e9e9a5afd10c21c0a1
purpose: Независимая проверка offline utility requester adapter
required_action: Проверить immutable package, pins, tests и границы; только non-live scratch; вернуть KOO exact результат
expected_result: Independent non-live PASS либо exact blocker
failure_mode: Stop on unavailable locator or identity mismatch; no receipt/acceptance/processing inferred
inbox_pointer: entities/sisadmin/inbox/KOD__booster-utility-pilot-adapter-r01__SIS.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
