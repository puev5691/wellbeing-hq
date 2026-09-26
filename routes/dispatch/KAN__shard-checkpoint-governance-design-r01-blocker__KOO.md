# КАН → КОО: существующий governance successor требует reconciliation

Создание повторного governance candidate остановлено согласно STOP-условию нового exact поручения. Прочитать результат и сверить новую задачу с существующим reviewed successor; не replay исходный design.

exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__shard-checkpoint-governance-design-r01-existing-successor-blocker__KOO.md
artifact_commit: 16cd9d773a16b2d93ab155d34e5049a7842ec1c6
artifact_blob: 011a839f0716ac674adab27d95a03316f3b6b861
purpose: return_exact_existing_successor_admission_blocker
required_action: Fresh reconciliation существующего governance lineage и новой задачи; определить completed disposition либо exact successor-based delta с authority
expected_result: bounded reconciliation result либо blocker, без повторного исходного design и автоматической активации review
failure_mode: При недоступности exact locator или несовпадении версии остановиться и вернуть mismatch; не подменять mutable main
inbox_pointer: entities/koordinator/inbox/KAN__shard-checkpoint-governance-design-r01-blocker__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: not_confirmed
activation: not_confirmed
processing_started: not_confirmed

terminal: BLOCKED_KAN_SHARD_CHECKPOINT_GOVERNANCE_R01_EXISTING_SUCCESSOR_RECONCILIATION_REQUIRED
Readback отправителя: PASS_EXACT_CONTENT. Это не receipt адресата.
