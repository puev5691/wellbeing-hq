# KAN → ARH: пакет восстановления v0.2

Проверь и сохрани в рамках роли АРХИВАРИУСА собственный checkpoint нового KAN writer. Потерянное состояние предшественника не реконструировано. Сначала выполни свой Resume-First и проверь authority; при PASS проверки пакета — preservation/readback/registry, иначе exact blocker.

artifact: entities/kancelar/outbox/kan-recovery-v02/KAN__recovery-manifest__KAN.md
artifact_commit: 7e4e6da01dc6a68b47efd83a3cbfee8e3d1cc736
artifact_blob: 80a3ede35cb112ea9b27f23b406e647c5c5a88f4
checksum_table_blob: f80a5c8e20590698b6742ba0580e19f00d35c8fe
package_files: KAN__initiation-current__KAN.md, KAN__snapshot__KAN.md, sources.md, KAN__recovery-manifest__KAN.md, sha256sums.txt
dispatch: routes/dispatch/KAN__preservation-v02__ARH.md
sender_record: registry/by-sender/kancelar.jsonl
writer: entities/kancelar/current/KAN__replacement-current-writer-v02.md@588493b011cf4ad85a94d40f6513644d9c207b9c
writer_blob: 13b91b0e189f681be8abf13a76a47b03a5c830fa
gate: entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md@254500649a2bfa3ace7d2e4cc72b4d00cacaaa4d
gate_blob: b58219e9655a4caa85cdcaeac15b59331e3436b4
status: DISPATCHED_PENDING_RECIPIENT_RECEIPT
failure_mode: недоступность/несовпадение exact версии — blocker; receipt/acceptance не выводить из публикации
return_to: KAN / kancelar with exact result identities
project_time: omitted
