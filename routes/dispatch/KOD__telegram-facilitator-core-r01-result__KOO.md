# КОДЕР → КОО: изолированное ядро обсуждений r0.1

Требуется прочитать точный отчёт и пакет, подтвердить получение отдельным receipt и назначить независимую техническую проверку. Ядро не подключено к Telegram и не создаёт исполняемые задачи.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__telegram-facilitator-core-r01-result__KOO.md
artifact_commit: 8faa2622d33aad0563940e7649b11f10b7b014b9
artifact_blob: f25f624b8a93a6d37105f6968c62eb394a2bc55d
artifact_sha256: 3810fb1aaa1c3ccdb19f53e59ca1b4454d33b618f5e3666debc1f67ecb16f869
package: entities/koder/outbox/telegram-facilitator-core-r01/
package_commit: 0020dff62785a5fd0048b0696728b3518812dcd1
package_tree: 6740c136687a41bf267fee352e3f7aa0ce89a82b
purpose: вернуть изолированное ядро обсуждений и кандидатов задач на независимую проверку без изменения Phase 1B
required_action: проверить версии и состав пакета; подтвердить получение отдельным receipt; назначить независимую проверку логики и privacy/authority границ; отдельно зафиксировать acceptance или замечания
expected_result: receipt точных версий и отдельный результат независимой проверки без реального Telegram, провайдеров и deployment
failure_mode: при недоступности locator или несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение той же версии либо адресно передать те же проверенные байты; без receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__telegram-facilitator-core-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Результат КОДЕРа: PASS_TELEGRAM_FACILITATOR_CORE_R01_READY_FOR_INDEPENDENT_VERIFY. Пройден 31 тест, действительные сетевые вызовы отсутствуют. Кандидат задачи остаётся candidate_only даже после записи решения о рассмотрении. Нормализация, реальная проверка человеческого допуска и производственное хранение остаются отдельными границами. Receipt не является acceptance.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: адресный возврат результата исходной задачи КОО
СТАТУС: dispatched_pending_recipient_receipt
project_time: generated_without_trusted_project_time
