# Dispatch KOO → SHT: end-to-end test

exchange_gate: v1
sender: koordinator
recipient: shtabist
artifact: entities/koordinator/outbox/KOO__exchange-e2e-test__SHT.md
artifact_commit: 1d27fa1bd6b5befeb16a0aa3bb6a89f82608a95c
artifact_blob: 20174a943debf3ba7a184d7dea9f5fa0356aa8d2
purpose: end-to-end exchange gate test
required_action: read immutable artifact, verify identity, create receipt, then separately ACCEPTED or REJECTED
expected_result: receipt plus separate acceptance decision
failure_mode: locator unavailable, artifact/version mismatch, missing receipt, or acceptance claimed without content check
inbox_pointer: entities/shtabist/inbox/KOO__exchange-e2e-test__SHT.md
registry_record: registry/by-sender/koordinator.jsonl
status: dispatched

## Граница

`dispatched` не означает `received` или `accepted`. До фактического действия ШТАБИСТА end-to-end тест не завершён.
