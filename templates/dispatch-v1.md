# Dispatch v1 template

exchange_gate: v1
sender: <sender>
recipient: <recipient>
artifact: entities/<sender>/outbox/<file>
artifact_commit: <immutable-commit-sha>
artifact_blob: <blob-sha-or-null>
purpose: <why>
required_action: <what-recipient-must-do>
expected_result: <what-must-be-returned>
failure_mode: <what-counts-as-undelivered-or-version-mismatch>
inbox_pointer: entities/<recipient>/inbox/<pointer>.md
registry_record: registry/by-sender/<sender>.jsonl
status: dispatched
receipt: <routes/receipts/...md-or-empty-until-received>

Не объявлять `received` без receipt требуемой версии. Не объявлять `accepted` только по receipt.