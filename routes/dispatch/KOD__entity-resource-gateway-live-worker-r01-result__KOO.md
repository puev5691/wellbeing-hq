# КОДЕР → КОО: live-worker r0.1

Результат: PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__entity-resource-gateway-live-worker-r01-result__KOO.md
artifact_commit: b56d5159bcf7951efcb21de6dd684d4f74907844
artifact_blob: bbf29f1a6e64ce7a8975062bd06018d725f52442
artifact_sha256: c5f5e4b479b7f795f103b8cc0b2372e91530d35344786bb4092ee821d7d09853
package: entities/koder/outbox/entity-resource-gateway-live-worker-r01/
package_commit: cd9f0c7327613ee29f9de54574ca141b557e5d18
package_tree: 222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4
purpose: вернуть restart-safe live-worker candidate на независимую проверку без реального provider call
required_action: проверить точные байты пакета; подтвердить получение отдельным receipt; назначить независимую проверку durable ledger, timeout/redirect/response bounds, provider binding и credential-ref boundary
expected_result: receipt точной версии и отдельное заключение независимой проверки; никаких live provider calls до нового допуска
failure_mode: при недоступности locator или несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же байты
inbox_pointer: entities/koordinator/inbox/KOD__entity-resource-gateway-live-worker-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

27/27 тестов прошли. Реальные provider calls и credential reads: 0. LIVE authority этим результатом не выдаётся. Receipt не является acceptance.
