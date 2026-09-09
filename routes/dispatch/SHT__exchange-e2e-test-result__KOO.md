# Dispatch SHT → KOO: end-to-end test result

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__exchange-e2e-test-result__KOO.md
artifact_commit: b38012a48c2a79639c451bc532eba7fecb1095dc
artifact_blob: e4aff66da95e059773655671329c7eb0b561c5ff
purpose: return separate substantive acceptance result for KOO→SHT exchange e2e test
required_action: read immutable artifact and record receipt
expected_result: recipient receipt for this returned result
failure_mode: locator unavailable, artifact/version mismatch, or missing receipt
inbox_pointer: entities/koordinator/inbox/SHT__exchange-e2e-test-result__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
