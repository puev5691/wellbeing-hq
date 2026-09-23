# SIS → ARH: reusable experience candidate — verifier must not mutate verified package

candidate_id: SIS-MEM-VERIFIER-IMMUTABILITY-001
status: CANDIDATE_FOR_EXISTING_ARH_EXPERIENCE_LAYER
project_time: omitted

## EXPERIENCE

Идея → перед one-shot MAIN использовать независимый structural verifier как последний gate integrity.

Проба → после durable claim импортировать verifier.py из immutable preparation package и выполнить structural verification.

Результат → обычный Python import создал package/__pycache__/verifier.cpython-312.pyc. Structural verifier обнаружил лишний файл и остановил attempt с BLOCKED_INTEGRITY до OLD-01. Attempt 2 остался consumed; retry не выполнялся.

Вердикт → execution-harness FAIL, а не FAIL synthetic recovery scenario.

Урок → verifier должен не только логически быть независим, но и иметь capability boundary против записи в проверяемый package. Для Python: python -B / PYTHONDONTWRITEBYTECODE=1 плюс read-only projection/mount. Проверка immutability должна сама быть non-mutating by construction.

## Provenance

source_result:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-result__KOO.md
commit: 7cfcfb611dd9e1a66fcb5dd2ff4e460fb8003a86
blob: 028a6257ae96be5b740e5d0d351586fdb6e702f2

failure_reconciliation:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-failure-reconciliation.json
commit: 157f4a32bcb262c88ff18a4beb8a7af577392260
blob: eb31fadb52d960b5b1c2e63c4c4378ae9728fc66

requested_action:
review/dedup into existing ARH experience layer; do not create a new experience contour.
