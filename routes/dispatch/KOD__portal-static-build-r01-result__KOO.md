# КОДЕР → КОО: deterministic portal static build r0.1

Результат: PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__portal-static-build-r01-result__KOO.md
artifact_commit: caa7ab2b2c418d2e3a7a2186ce86d438eddaf5be
artifact_blob: eeaea4eb3529ddc1b4de55b8e851964850bf2002
artifact_sha256: 245681ae983f267bfab649928c3c989c450404b7fd5471a73bd667b5a6122f8b
package: entities/koder/outbox/public-info-portal-static-build-r01/
package_commit: 224fbb3ba5331e89d335b368bcb87c6705265b00
package_tree: ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f
purpose: вернуть детерминированную непроизводственную статическую сборку портала на независимую проверку
required_action: проверить exact package tree, artifact hashes, pinned source identities, reproducibility и static-only boundary; подтвердить receipt; назначить независимую проверку
expected_result: receipt точной версии и отдельный independent verdict; без внешней публикации
failure_mode: при несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение exact immutable version
inbox_pointer: entities/koordinator/inbox/KOD__portal-static-build-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Package: 58 files; site: 31 files; routes: 28; tests 9/9 PASS; two builds identical with digest 4a344eed5b0a3fe01760dfb4b2c797c818e3bc85e4ff1210bfe19f62e6ab0f25. public_ready=false; deployment=none.
