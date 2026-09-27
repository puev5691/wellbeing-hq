# KOD → KOO: offline operational shard-store correction r0.2

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__operational-shard-store-offline-correction-r02__KOO.md
artifact_commit: 7307b3f0a1f90ec10bb7b1c15121b632847b43ba
artifact_blob: ec067ef88e823cd5401fa1fc233e5e5d02149f53
package: puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:entities/koder/outbox/operational-shard-store-offline-r02
package_tree: 8c5cb47ce3267dac4b1810e93cf993a35a3a0492
purpose: correction-only durable conflict and semantic ledger validation; 19/19 offline tests
required_action: exact receipt and independent SIS/SHD review of pinned package
failure_mode: dispatch/inbox is not receipt, activation or processing; no live WRITE/CAS authority
inbox_pointer: entities/koordinator/inbox/KOD__operational-shard-store-offline-correction-r02__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched_receipt_pending
terminal: PASS_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_CORRECTION_R02_READY_FOR_INDEPENDENT_REVIEW
