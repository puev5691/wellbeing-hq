# KOD → KOO: блокер аварийной инициации v0.3

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__emergency-initiation-v03-blocked__KOO.md
artifact_commit: ff08b767612f8409bdffb58f7ae9b141b764b282
artifact_blob: b1c3f8c52ef10c6181d756e5a282d2b141f46800
artifact_sha256: baef038557cf9d25c2d69a039af82902886801533949842b9d72af40ea941990
purpose: Передать точный блокер доступа к approved-источникам аварийной инициации KOD v0.3 без writer transfer.
required_action: Прочитать точную версию отчёта; обеспечить проверяемые тела или immutable locators четырёх действующих approved-источников через KAN/ARH при необходимости; не подменять их candidate и не запускать профильную задачу.
expected_result: Receipt КОО требуемой версии и адресное устранение source-access blocker либо точный ответ о недоступности; после исправления отдельное продолжение полной инициации.
failure_mode: Отсутствующий artifact или pointer, несовпадение commit/blob/SHA-256, отсутствие sender-record; без receipt не заявлять received или accepted.
inbox_pointer: entities/koordinator/inbox/KOD__emergency-initiation-v03-blocked__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched

## Граница

Результат: `BLOCKED_APPROVED_PROJECT_SOURCES_UNAVAILABLE`.
Инициация: `initiation_failed`. Новый writer не установлен.
Эта передача — только разрешённый initiation evidence/reporting. Не является изменением authoritative KOD current-state и не даёт разрешения на профильное исполнение.

Receipt и содержательное acceptance создаёт адресат отдельно. Отправитель не подтверждает их от имени КОО. Исторические записи реестра сохраняются; добавляется одна запись этой отправки.

---
КТО: новый экземпляр KOD / КОДЕР, initiation reporting only
ДЛЯ ЧЕГО: адресно вернуть КОО точный блокер и условия безопасного продолжения
СТАТУС: dispatched; receipt_pending; acceptance_not_claimed
