# Коррекция нормализатора: reasoning как игнорируемые метаданные

Отдельный non-live successor по решению ОПЕРАТОРА APPROVE_BOOSTER_REASONING_AS_IGNORED_METADATA_R01. Требует независимой проверки СИСАДМИНА. Не установлен на хост; новый вызов OpenAI не разрешён.

## Что изменено

В _normalize_evidence пропускается только output item с точным type=reasoning. Его содержимое не копируется в review-result, не интерпретируется и не исполняется. Результат по-прежнему извлекается только из message с role=assistant и content type=output_text.

function_call, tool/action outputs, неизвестные типы, metadata/reasoning_summary как самостоятельные output-типы, неправильные роли и content-типы остаются заблокированными. Только reasoning без текстового результата не даёт PASS. Существующее последовательное объединение разрешённых текстовых сообщений сохранено; новой семантики выбора результата нет.

Review-result v2 schema, строгий readback и diagnostic shape schema не изменены. Диагностика сохраняется и проверяется до нормализации. Ни результат, ни диагностика не сохраняют значения summary/encrypted_content из reasoning. Диагностика сохраняет только прежнюю структурную информацию.

## Привязки компонентов

live_worker.py включён с exact final lineage SHA-256 175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3; его исходные байты, включая отсутствие конечного перевода строки, сохранены.

reviewable_live_worker.py и diagnostic_reviewable_live_worker.py изменены только в hash pins зависимостей. Outer runner изменён только в transitive pins и provenance TASK_COMMIT/TASK_BLOB/WRITER_BLOB нового поручения и действующего KOD v0.5. Эти идентификаторы не являются live authority.

response_shape_store.py и systemd candidate сохранены byte-identical. Указанный в candidate прежний installation root остаётся лишь контрактом будущего отдельного deployment; копирование туда и запуск unit этой задачей не выполняются.

SENTINEL-INVOCATION.example.json — только non-live пример с новыми provenance identities, не повтор старого consumed invocation. Не превращать его в разрешение LIVE. Режим LIVE в тестах работает исключительно с synthetic Resolver/Client и временными локальными ledger.

## Проверка в scratch checkout

Сначала проверьте SHA256SUMS.txt. Затем выполните `python run_tests.py` внутри локальной копии этого каталога. Скрипт блокирует socket connections, использует синтетические ответы и пишет TEST-LOG.txt / TEST-RESULTS.json. Настоящий credential resolver не вызывается. Тесты запускаются только в scratch, не на production state.

Получено 24/24 PASS, failures=0, errors=0. Подтверждены positive reasoning+text, assistant-only regression, отрицательные tools/unknown/role/content cases, отсутствие reasoning payload в сохранённых artifacts, порядок claim/transport/shape-persist/shape-readback/normalize/review-persist/review-readback, запрет PASS при отказе readback и повторного transport по тому же synthetic attempt.

Это offline доказательство; успешный production или live вызов не заявляется. Старый one-shot authority израсходован и не используется.

## Точное основание

Task: puev5691/wellbeing-hq@c751b3e22c4df45ec74aed995096516ecee8a689:entities/koordinator/outbox/KOO__booster-reasoning-metadata-normalizer-correction-r01__KOD.md
Task blob: ce56ff61413af96494b3332b35684008eac2684e.
Baseline package: puev5691/wellbeing-hq@f09ae9cd5be37269582deac05435f5ed5a06ca10:entities/koder/outbox/openai-booster-shape-diag-successor-wiring-r01; tree 6f536f10d99d08dcf5e1e671c5217650261a1548.
Worker source: puev5691/wellbeing-hq@716637bb0e18319fa8f3151253ed5c71b8c1aad7:entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/live_worker.py; blob d276de1050fd54e836ed4fc879eb384dba3aa1f1.

---
КТО: KOD v0.5
ДЛЯ ЧЕГО: независимая проверка узкой non-live коррекции
СТАТУС: CANDIDATE_NOT_DEPLOYED / READY_FOR_SIS_VERIFY
