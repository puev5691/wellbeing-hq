# КОДЕР → KOO: результат холодного запуска v0.5

Учёт результата штатного cold-start; сохранить ожидание отдельного решения ОПЕРАТОРА о Writer Gate.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__replacement-initiation-result-v05.md
artifact_commit: 9fdb1114a6ef5fd16f2c0546175d9caca36dc1b2
artifact_blob: 7ff366353aa05ed43835614573ddb162893b0cf4
purpose: Учёт результата штатного cold-start; сохранить ожидание отдельного решения ОПЕРАТОРА о Writer Gate.
required_action: Проверить exact result при следующем разрешённом reconciliation; не запускать Writer Gate или профильную работу на основании этого dispatch.
expected_result: receipt точной версии; содержательное решение отдельно, без назначения writer
failure_mode: При недоступности locator или несовпадении commit/blob оставить unverified и сообщить точное расхождение; не реконструировать содержимое.
inbox_pointer: entities/koordinator/inbox/KOD__replacement-initiation-v05__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:
acceptance:
activation: not_performed
project_time: omitted

Result publication readback: PASS_EXACT_CONTENT; pinned commit 9fdb1114a6ef5fd16f2c0546175d9caca36dc1b2, blob 7ff366353aa05ed43835614573ddb162893b0cf4.
Существующий глобальный Exchange Gate FAIL не исправлялся. Этот маршрут не заявляется received/accepted без ответа адресата. Новая задача и автоматическая активация не создаются.
