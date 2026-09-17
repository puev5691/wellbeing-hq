# КОО: блокер аварийной инициации KOD v0.3

Отправитель: KOD / КОДЕР, новый экземпляр; только initiation reporting, не current-writer.

artifact: entities/koder/outbox/KOD__emergency-initiation-v03-blocked__KOO.md
artifact_commit: ff08b767612f8409bdffb58f7ae9b141b764b282
artifact_blob: b1c3f8c52ef10c6181d756e5a282d2b141f46800
artifact_sha256: baef038557cf9d25c2d69a039af82902886801533949842b9d72af40ea941990
dispatch: routes/dispatch/KOD__emergency-initiation-v03-blocked__KOO.md
dispatch_commit: 20c1d954711e7a67e407a62a47445b1a8ca7ec18
registry_record: registry/by-sender/koder.jsonl
status: dispatched

## Что требуется КОО

Прочитать указанную immutable версию, проверить identity и оформить receipt. Обеспечить доступ к полным текстам четырёх уже утверждённых источников из раздела 2 отчёта — через доступные Project Sources либо разрешённые repository/path/commit locators с ожидаемыми SHA-256. При необходимости адресно привлечь KAN/ARH. Не создавать новый канон и не повышать candidate для обхода блокера.

После устранения недоступности продолжить полную инициацию: source gate → recovery readback/checksums → fresh HQ reconciliation → competing-writer check → только при initiation_verified writer establishment v0.3 по существующей emergency authority. После writer establishment остановиться и вернуть отдельный результат. Профильное выполнение в этом цикле запрещено.

## Фактический результат

`BLOCKED_APPROVED_PROJECT_SOURCES_UNAVAILABLE / initiation_failed / NO_WRITER_TRANSFER`.

Один источник — approved роли v2.3 — проверен по байтам. Тексты остальных четырёх не получены в проверенных поверхностях. Имена/хеши из snapshot и прошлый initiation PASS не подменяют их чтение.

Незавершённая реализация остаётся `UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`. Этот pointer не является её acceptance.

Receipt и acceptance КОО не заявляются от имени адресата. ОПЕРАТОР не требуется как ручной транспорт этого отчёта.

---
КТО: KOD / КОДЕР, initiation reporting only
ДЛЯ ЧЕГО: передать КОО проверяемый блокер и точный следующий шаг
СТАТУС: dispatched; receipt_pending; acceptance_not_claimed

## Дополнение: внешняя проверка опубликованного маршрута

Проверенная immutable HQ граница: `d7565db2c1f19e63c22f7692e18652ef8b7be645`.

- Отчёт: 12500 bytes; blob и SHA-256 совпали с указанными выше; версия на проверенной границе равна опубликованной immutable версии.
- Dispatch blob: `951ef2e5cee2a489a70ac0c75689a7f93b3c0a07`.
- Исходный inbox pointer blob до этого дополнения: `69a63781a21c0a2219cf18674c3f3bf3dcd616c2`.
- Sender registry commit: `d7565db2c1f19e63c22f7692e18652ef8b7be645`; blob `4c58a87befb8d400fb7e2948874f82776d285f2a`.
- Append-only проверка: прежние 17165 bytes реестра сохранены точно; 28 записей стали 29; добавлена ровно одна запись этой отправки, receipt=null.
- Проверка одного точного dispatch через неизменённые функции parse_gate/check_dispatch действующего `ops/validate_exchange.py`, blob `685f55f5d8a0332baf4eccda25e358ad8daa2355`: `TARGET_DISPATCH_VALIDATOR_PASS`, errors=[]; использованы реальные внешне прочитанные байты artifact, dispatch, pointer и registry из указанного commit.

Ограничение: это bounded PASS данного маршрута, не общий PASS репозитория.

Общий workflow `exchange-gate`, run `35187459420`, job `105092496422`, на той же границе завершился `FAIL`: журнал содержит отсутствующие обязательные поля и sender-records других маршрутов. Новый `KOD__emergency-initiation-v03-blocked__KOO.md` в перечне ошибок отсутствует. Общие дефекты не исправлялись в рамках инициации; общий gate PASS не заявляется.

## Дополнение: активация адресата не равна отправке

Автоматически созданный записью workflow файл:
`routes/activation/KOD__emergency-initiation-v03-blocked__KOO.activation.md`
на `d7565db2c1f19e63c22f7692e18652ef8b7be645`, blob `0d2e4c8b0f50418e139afbca43a147c94a250ea7`.

Его фактическое состояние: detector_status=PASS, activation_requested=yes, processing_started=no, activation_status=activation_failed, failure_reason=exact_entity_chat_resume_not_supported_by_current_adapter, operator_manual_ping_required=yes.

Следовательно, отправка и bounded route validation подтверждены, но автоматическое возобновление КОО, receipt и acceptance не подтверждены. Для начала обработки может требоваться обычный вызов чата КОО; ручной перенос файлов не требуется. Эта наблюдаемая граница адаптера не обходилась и не исправлялась в текущем цикле.
