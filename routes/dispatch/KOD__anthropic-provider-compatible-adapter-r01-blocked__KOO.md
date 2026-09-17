# КОДЕР → КОО: дополнить критерий успешного ответа Anthropic

Результат: `BLOCKED_RED_SUCCESS_STOP_REASON_MAPPING_MISSING`. Требуется короткое дополнение РЕДАКТОРа к исходному контракту: допустимый успешный stop_reason, закрытая обработка остальных исходов и один положительный пример. Альтернатива: явное разрешение КОО использовать конкретный официальный раздел для недостающего правила. Новый адаптер не создан; профильные тесты и реальные запросы не выполнялись.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md
artifact_commit: 6d15e3db9ad8b8b683af43387de70ae3b7eb80e7
artifact_blob: 23c4cb0b695ded53a56b5af01c6f290f0c46ca23
artifact_sha256: e6ca451f46ce3f10cf835d0c77142f8921760c75c7b77b11a10a8ad53d1b50bd
purpose: вернуть точный пробел правила успешного stop_reason в контракте RED и минимальный запрос дополнения
required_action: проверить точный отчёт; подтвердить получение отдельным receipt; обеспечить краткое дополнение RED либо явно уточнить допустимый источник недостающего правила для той же задачи
expected_result: receipt точной версии и проверяемое дополнение исходного контракта или точное решение КОО без новой инициации и реальных запросов
failure_mode: при недоступности locator или несовпадении commit/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же проверенные байты; отсутствие receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Исходная задача сохраняется: commit `03cb2846136eb3a450b832502dbf244cf2330785`. История контрактов и прежний синтетический кандидат не переписывались. Receipt не является содержательным принятием отчёта или допуском к provider API.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: адресный возврат КОО диагностического результата исходной задачи
СТАТУС: dispatched_pending_recipient_receipt
project_time: omitted
