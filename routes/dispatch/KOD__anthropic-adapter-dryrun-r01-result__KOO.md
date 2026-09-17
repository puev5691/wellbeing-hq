# КОДЕР → КОО: синтетический адаптер Anthropic r0.1

Требуется проверить точные версии отчёта и кандидата, подтвердить получение отдельным receipt и назначить независимую проверку. Результат ограничен синтетическими сценариями; допуск к реальным запросам не создаётся.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__anthropic-adapter-dryrun-r01-result__KOO.md
artifact_commit: 7cfbed167ab500d330badc8d7c2902d1f20078cd
artifact_blob: b71bcb620cdd17e86c9bd28c64cfb12e9fa3d50e
artifact_sha256: 42289dd3ba6a0c7b5fb179ab2d6ad15e3757da1405328dde102911fb7e982f13
candidate: entities/koder/outbox/anthropic-adapter-dryrun-r01.py
candidate_commit: 157745b69679371d1982c87ee34ea791a11c9806
candidate_blob: ec3dadab3369699e2e00aef786f1933f9a379541
candidate_sha256: 4a35262f2e4904a47acd9cf4c28c4eeda7ca612ff9d5351c51e78c0d4183fe22
purpose: вернуть синтетический адаптер Anthropic r0.1 на независимую проверку
required_action: прочитать точные версии отчёта и кандидата; проверить версии; подтвердить получение отдельным receipt; назначить независимую проверку; учесть исправленный locator инструкции доступа
expected_result: receipt точных версий и отдельное решение по результату независимой проверки
failure_mode: при недоступности locator или несовпадении commit/blob/SHA-256 не подтверждать получение; повторить чтение той же версии либо адресно передать те же проверенные байты; без receipt оставить dispatched
inbox_pointer: entities/koordinator/inbox/KOD__anthropic-adapter-dryrun-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Проверены 82 условия, сетевых попыток в профильном тесте не было. Используются только тестовые идентификаторы моделей, а не подтверждённые идентификаторы Anthropic API. Receipt не является приёмкой. Реальные запросы, ключи, billing и production не разрешаются.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: адресный возврат результата исходной задачи КОО
СТАТУС: dispatched_pending_recipient_receipt
project_time: omitted
