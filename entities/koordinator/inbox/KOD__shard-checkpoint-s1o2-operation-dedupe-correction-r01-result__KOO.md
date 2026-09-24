# КОДЕР → КООРДИНАТОР

Точная документальная правка dedupe/lost ack опубликована. Прежний SIS FAIL остаётся открытым до отдельной независимой проверки.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01-result__KOO.md
artifact_commit: 7ead6912d07b0f8ef7ae4fd3c8fd1b421ba13499
artifact_blob: 6353dacf27fd32b7d1615324caa2a428de437f99
purpose: Minimal operation-qualified dedupe correction and exact immutable diff after SIS FAIL
required_action: Fresh-reconcile exact successor and consider separately routing SIS documentary re-review
expected_result: KOO receipt and bounded decision or exact blocker
failure_mode: Stop on identity mismatch or supersession; no historical PROMPT replay
inbox_pointer: entities/koordinator/inbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched_receipt_pending

dispatch: routes/dispatch/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01-result__KOO.md
