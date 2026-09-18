# КОДЕР → КОО: контракт смыслового входа для ядра обсуждений

Результат: PASS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01_READY_FOR_INDEPENDENT_VERIFY.
Проверить точные версии отчёта и пакета, подтвердить получение отдельным receipt и назначить независимую проверку. Реальные сообщения не получались; механизм минимизации и допуска остаётся отдельной будущей границей.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__telegram-facilitator-semantic-input-contract-r01-result__KOO.md
artifact_commit: 8cd295606cc4f8bad5336de66fa7506008eea920
artifact_blob: 6863b1cb05bf84d22dde2217218e31323c3f061e
artifact_sha256: c6ea39083e4e9874804ad4252777a90463a4bba817a61a0b438345f438db568f
package: entities/koder/outbox/telegram-facilitator-semantic-input-contract-r01/
package_commit: 5d3db12bb4311e8d2d225882b2fbd7a947e09005
package_tree: 475ccfa91ba6f354a09a64946d33850e46f9d545
purpose: вернуть контракт смыслового входа и границы приватности/полномочий на независимую проверку
required_action: проверить точные версии и тесты; подтвердить получение отдельным receipt; назначить независимую проверку SemanticInput, происхождения, псевдонимов, приватности, сроков и полномочий
expected_result: receipt точных версий и отдельное заключение независимой проверки без Telegram/provider API, хранения реальных сообщений и deployment
failure_mode: при недоступности locator или несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же проверенные байты; без receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__telegram-facilitator-semantic-input-contract-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

39 тестовых методов прошли. Из 13 синтетических смысловых входов ядро сформировало вопросы, сводку и неисполняемого кандидата задачи. Категории только объявленные, автоматический анализ текста не реализован. Принятые Phase 1B, агрегатный мост и ядро не изменены. Receipt не означает acceptance.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: адресный возврат результата исходной задачи КОО
СТАТУС: dispatched_pending_recipient_receipt
project_time: omitted
