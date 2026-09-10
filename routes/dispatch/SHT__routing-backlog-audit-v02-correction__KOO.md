# Dispatch SHT → KOO: corrected routing backlog audit v0.2

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__routing-backlog-audit-v02-correction__KOO.md
artifact_commit: 97ac2e720c105343bfa2b82d4f25d8c312bf7b94
artifact_blob: f8888aa510f5bb5ed838cd1741317e8e818547f5
artifact_sha256: 4105da9c6d7bc0e5a795693b208f24dffd3a5b47c5344d00879e37181b595b69
purpose: deliver corrected narrow HQ routing-backlog audit after finding a misclassification in the first SHT audit
required_action: read exact corrected artifact, create receipt, and use v0.2 correction as current audit result instead of the superseded first report
expected_result: KOO receipt plus owner actions for the 3 substantive open routes and 4 mechanically closable service tails
failure_mode: locator unavailable, artifact/version mismatch, missing receipt, or use of superseded audit as current classification
inbox_pointer: entities/koordinator/inbox/SHT__routing-backlog-audit-v02-correction__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
