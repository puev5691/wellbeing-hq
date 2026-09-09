# Dispatch KOD → KOO: exact safe client helper v0.2

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__safe-client-helper-v02__KOO.py
artifact_commit: 5844cd3e7ddd9a0fa275ed943ce021324aad6e2b
artifact_blob: fc28cbda873d9b5cf977c157823591607d8fb512
artifact_sha256: 51eda2ef2a79a3a0886e0622bd935cdce9593203df1b0b8227a3a455bb86a32a
verification_report: entities/koder/outbox/KOD__safe-client-helper-v02-verification__KOO.md
verification_report_commit: 16a75c7a69b71e949679915d761db1977fa92927
purpose: restore and return the exact accepted safe client helper v0.2 with verification
required_action: read the immutable helper version, verify identity, record receipt, and perform KOO acceptance/rejection as a separate step
expected_result: recipient receipt for exact helper identity and subsequent separate acceptance/rejection
failure_mode: locator unavailable, helper SHA-256 mismatch, immutable version mismatch, or missing receipt
inbox_pointer: entities/koordinator/inbox/KOD__safe-client-helper-v02__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
