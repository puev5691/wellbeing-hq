# КОДЕР → КОО: мост агрегатной квитанции в событие ядра

Требуется проверить точные версии отчёта и пакета, подтвердить получение отдельным receipt и назначить независимую проверку. Результат ограничен преобразованием существующей агрегатной квитанции; смысловое содержание обсуждения не выдумывается, реальное подключение не разрешается.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__telegram-facilitator-normalized-event-bridge-r01-result__KOO.md
artifact_commit: c03a6b22d6917381f75cc87da7a87520c9c8df8c
artifact_blob: 281be02b9fc3b7fd332df3ffcaba2dfd2b5f3ff3
artifact_sha256: e0b69cab942ec3b932f473b339ea9a098385ade08cfee9327ef2730306288f5f
package: entities/koder/outbox/telegram-facilitator-normalized-event-bridge-r01/
package_commit: e01a62216be791fc13b581581e777a1c6113eedc
package_tree: b5885c483212eefad145b983dac6af37bd5ba7b5
purpose: вернуть изолированный мост агрегатной квитанции Phase 1B в NormalizedEvent на независимую проверку
required_action: проверить состав и версии; подтвердить получение отдельным receipt; назначить независимую проверку схемы, происхождения, приватности, сроков и полномочий; отдельно зафиксировать acceptance или замечания
expected_result: receipt точных версий и отдельное заключение независимой проверки без Telegram, provider API и runtime deployment
failure_mode: при недоступности locator или несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же проверенные байты; без receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__telegram-facilitator-normalized-event-bridge-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Результат КОДЕРа: PASS_TELEGRAM_FACILITATOR_NORMALIZED_EVENT_BRIDGE_R01_READY_FOR_INDEPENDENT_VERIFY. Прошли 33 тестовых метода без сети, процессов, записи и открытия БД. Принятые Phase 1B и facilitator-core не менялись. Контекст допуска поставляется отдельно; модуль не вызывает dispatch и не создаёт исполняемых задач. Receipt не означает содержательную приёмку.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: адресно вернуть КОО результат исходной задачи
СТАТУС: dispatched_pending_recipient_receipt
project_time: omitted
