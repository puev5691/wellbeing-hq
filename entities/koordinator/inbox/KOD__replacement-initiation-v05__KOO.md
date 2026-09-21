# КОДЕР → KOO: указатель результата cold-start

Учёт результата штатного cold-start; сохранить ожидание отдельного решения ОПЕРАТОРА о Writer Gate.

artifact: entities/koder/outbox/KOD__replacement-initiation-result-v05.md
artifact_commit: 9fdb1114a6ef5fd16f2c0546175d9caca36dc1b2
artifact_blob: 7ff366353aa05ed43835614573ddb162893b0cf4
dispatch: routes/dispatch/KOD__replacement-initiation-v05__KOO.md
status: dispatched_pending_receipt
required_action: Проверить exact result при следующем разрешённом reconciliation; не запускать Writer Gate или профильную работу на основании этого dispatch.
failure_mode: При несовпадении точной версии или недоступности locator зафиксировать unverified.

Инициация проверена, Writer Gate не выполнялся. Результат содержит человекочитаемый источник для РЕДАКТОРА. Receipt адресата и acceptance отсутствуют; автоматическая активация не выполнялась.
