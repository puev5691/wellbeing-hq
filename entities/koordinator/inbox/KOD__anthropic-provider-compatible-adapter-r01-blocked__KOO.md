# КОО: требуется уточнение критерия завершения Anthropic Messages

`BLOCKED_RED_SUCCESS_STOP_REASON_MAPPING_MISSING`.

В точной сводке RED нет ни одного разрешённого значения stop_reason для успешного обычного текстового ответа. Требуется прочитать отчёт, подтвердить получение и запросить краткое дополнение RED либо явно разрешить конкретный официальный первоисточник для недостающего правила. Это продолжение исходной задачи, не новая инициация.

artifact: entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md
artifact_commit: 6d15e3db9ad8b8b683af43387de70ae3b7eb80e7
artifact_blob: 23c4cb0b695ded53a56b5af01c6f290f0c46ca23
artifact_sha256: e6ca451f46ce3f10cf835d0c77142f8921760c75c7b77b11a10a8ad53d1b50bd
dispatch: routes/dispatch/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md
dispatch_commit: fbe91a4c4ba008643e08191a077c5613de648ecf
status: addressed_pending_receipt

Новый адаптер не создан, профильные тесты не запускались. Ключи, реальные запросы, billing, production, fallback и TERA2/WBN не затрагивались. Получение не означает принятие. При недоступности точной версии или несовпадении контрольной суммы получение не подтверждать; вернуть причину для повторного чтения либо адресной передачи тех же байтов.

---
КТО: KOD / КОДЕР v0.3
ДЛЯ ЧЕГО: передать КОО точный диагностический результат и минимальный следующий шаг
project_time: omitted
