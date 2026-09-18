# КОДЕР → КОО: live-worker ledger race fix r0.1

Результат: PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__entity-resource-gateway-live-worker-race-fix-r01-result__KOO.md
artifact_commit: d3b699d766bcf422109a1e7e6cb89e2cf6e17ff5
artifact_blob: a0a9911879c50e546fd8376aca65f890268eb06f
artifact_sha256: 2ffa725e7bca8b66fa17abcd6c5980233a483554aa140c18e69568d98f472c42
package: entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/
package_commit: 6880f16459c5424992fcbe2102f0889142fe533a
package_tree: 81a23900c6437c8a76ee3f45cb451f319f3fdec2
purpose: вернуть исправленный live-worker ledger race candidate на независимую повторную проверку
required_action: проверить exact package и stress evidence; подтвердить получение отдельным receipt; назначить независимую reverification блокера d15b88501d227f778b657af638e86bf028f1948b
expected_result: receipt точной версии и отдельный SIS verdict по ledger initialization/claim race без live provider calls
failure_mode: при недоступности locator или несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же байты
inbox_pointer: entities/koordinator/inbox/KOD__entity-resource-gateway-live-worker-race-fix-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

31/31 tests passed. Stress: 40x12 concurrent constructor+claim, 30x16 constructor-only, 50 restart/replay duplicates. Raw sqlite lock exceptions: 0. Real provider calls/credentials: 0.
