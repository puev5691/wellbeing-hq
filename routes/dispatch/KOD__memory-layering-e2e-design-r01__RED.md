# КОДЕР → RED

Подготовлен сценарий восстановления незавершённой синтетической задачи с выборочным чтением памяти. Это design/spec; эксперимент не запускался. Требуется review до отдельного execution gate.

exchange_gate: v1
sender: koder
recipient: redaktor
artifact: entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md
artifact_commit: 9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca
artifact_blob: b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0
purpose: Bounded memory-layering design review and evidence separation
required_action: Consider journal-source for existing journal-feed batching; no automatic publication
expected_result: Receipt and bounded review result or blocker
failure_mode: Stop on missing exact version; no historical replay or execution
inbox_pointer: entities/redaktor/inbox/KOD__memory-layering-e2e-design-r01__RED.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
