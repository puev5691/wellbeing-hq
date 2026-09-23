# КОДЕР → RED

Synthetic MAIN остановлен до запуска: эта среда не предоставляет проверяемую сетевую и файловую изоляцию нового worker. Разрешение осталось неиспользованным, OLD-01 и NEW-01 не стартовали.

exchange_gate: v1
sender: koder
recipient: redaktor
artifact: entities/koder/outbox/KOD__memory-layering-e2e-r01-main-runtime-admission-blocker__KOO-SHT-ARH.md
artifact_commit: c2123504f068b1d5b5f069b228745149d40fe776
artifact_blob: 54304f71ff26e253ee0760fb26420ec5c2f4db33
purpose: Pre-main runtime isolation blocker and evidence
required_action: Review human-readable journal-source for existing journal-feed; no automatic publication
expected_result: Receipt and scoped reconciliation or blocker
failure_mode: Stop if exact version inaccessible; no MAIN retry or authority replay
inbox_pointer: entities/redaktor/inbox/KOD__memory-r01-main-isolation-blocker__RED.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched

dispatch: routes/dispatch/KOD__memory-r01-main-isolation-blocker__RED.md
