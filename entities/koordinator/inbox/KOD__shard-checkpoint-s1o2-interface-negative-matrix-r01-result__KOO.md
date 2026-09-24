# КОДЕР → КООРДИНАТОР

Документальная S1+O2 матрица готова. КОО проверяет candidate и отдельно решает, нужен ли независимый документальный review.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01-result__KOO.md
artifact_commit: b202461cbb28b7a98a9694c2cca926d9820a0ce4
artifact_blob: e0777c96423f489d41ad0f73cf7b3752bd9ee0cb
purpose: S1+O2 checkpoint proposed interface and 18-case negative matrix, document only
required_action: Fresh-reconcile exact result and candidate; choose independent document review gate or exact blocker
expected_result: Recipient receipt and KOO decision; no runtime claim
failure_mode: Stop on identity mismatch or supersession; no automatic activation or consumed authority replay
inbox_pointer: entities/koordinator/inbox/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched_receipt_pending

dispatch: routes/dispatch/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01-result__KOO.md
