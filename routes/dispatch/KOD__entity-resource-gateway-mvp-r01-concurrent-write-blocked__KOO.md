# КОДЕР → КОО: конфликт параллельных изменений шлюза ресурсов

Нужно определить единственную основную реализацию и исполнителя исходной задачи. Наш код сохранён локально, но не опубликован поверх уже появившегося gateway.py. В этом цикле выполнена только фиксация конфликта после успешных локальных тестов.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__entity-resource-gateway-mvp-r01-concurrent-write-blocked__KOO.md
artifact_commit: e4d0729bccd0045bc0db55eaa89817ec46f21a44
artifact_blob: 9fad982b3625520c7ed70fddfde342cb850b8f81
artifact_sha256: 7f162aa81ff75c15aeb679f2634643a7b30c8575c36f505d4c8c9ab91cb9f9e2
purpose: вернуть наблюдаемый конфликт параллельных изменений одной задачи без перезаписи реализации
required_action: прочитать точный отчёт; подтвердить получение отдельным receipt; установить источник записей и определить единственную основную реализацию и исполнителя
expected_result: receipt точной версии и отдельное решение КОО о версии и границах продолжения исходной задачи
failure_mode: при недоступности locator или несовпадении commit/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же байты; без receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__entity-resource-gateway-mvp-r01-concurrent-write-blocked__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Наблюдаемая другая реализация: entities/koder/outbox/entity-resource-gateway-mvp-r01/gateway.py, commit 597d45cc47ef6d443ce9a0936bdca6bd95e4e760, blob e93ac320468dfeed84a7342b4e9dc5c597f48fc2. Её авторский экземпляр не установлен; writer-маркер v0.3 не менялся. Этот маршрут не принимает ни одну реализацию и не разрешает новые профильные изменения.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: BLOCKED_CONCURRENT_GATEWAY_IMPLEMENTATION
project_time: omitted
