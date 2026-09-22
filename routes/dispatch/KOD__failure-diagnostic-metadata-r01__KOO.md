# KOD → KOO

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__booster-failure-diagnostic-metadata-r01-result__KOO-SIS.md
artifact_commit: 7ac942e9aa1e70d9531e8d5c92c96ff192dd6afd
artifact_blob: 98f0906c6fe46958e97d113083e887e59222a61a
purpose: Failure metadata implementation result and independent verification
required_action: Reconcile exact completed non-live implementation; retain no-live boundary; coordinate independent SIS verify
expected_result: Receipt and exact scoped PASS FAIL or BLOCKER
failure_mode: Stop on missing locator or version mismatch; no replay
inbox_pointer: entities/koordinator/inbox/KOD__failure-diagnostic-metadata-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
