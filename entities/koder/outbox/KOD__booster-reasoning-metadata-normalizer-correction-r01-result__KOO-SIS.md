# КОДЕР: коррекция обработки reasoning готова к независимой проверке

Утверждённая узкая коррекция выполнена. Служебный output-контейнер reasoning теперь игнорируется при построении review-result v2; пользовательский результат извлекается только из разрешённого assistant/output_text. Tools/actions, неизвестные output-типы, неправильные роли и content-типы остаются заблокированными.

Пакет прошёл 24 локальных теста и опубликован как отдельный неизменяемый successor. Все 18 файлов прочитаны обратно с совпадением exact Git blob и содержимого. Установка и реальные вызовы не выполнялись. Следующий этап — независимая проверка СИСАДМИНА; до неё host mutation запрещена.

## Точное поручение и Resume-First

Task:
puev5691/wellbeing-hq@c751b3e22c4df45ec74aed995096516ecee8a689:entities/koordinator/outbox/KOO__booster-reasoning-metadata-normalizer-correction-r01__KOD.md
blob: ce56ff61413af96494b3332b35684008eac2684e
status: OPERATOR_POLICY_APPROVED__READY_FOR_NON_LIVE_CORRECTION
decision: APPROVE_BOOSTER_REASONING_AS_IGNORED_METADATA_R01

Текущее поручение ОПЕРАТОРА явно адресует этот task; исторические PROMPT не использованы.
Initial preflight: c751b3e22c4df45ec74aed995096516ecee8a689.
KOD writer v0.5: cf1c84f9df7c90509703e4885844d0cf871ff412; competing writer не обнаружен в полном дереве.
Перед публикацией HEAD изменился до e3d7fb96848798863becc6e4c2c219b20f62ef11. Проверенный delta содержит только два изменения литературного журнала RED, не task/writer/inputs. Основания задачи остаются действительными.
Публикация выполнена fast-forward без force.

## Immutable successor

puev5691/wellbeing-hq@628b915faa45908786040265c35b791fc18096bf:entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01

Composition: 18/18.
Publication/readback: 18/18 PASS_EXACT_CONTENT_AND_BLOB.
Manifest: MANIFEST.json, blob 5e88c806534eb3f69dc4a7674a0caf28a882f944.
Checksums: SHA256SUMS.txt, blob 095d4b7cfaccaa84918db31de19b2aaa74f568ca.
SHA256SUMS покрывает 17 остальных файлов, включая manifest; сам checksum file закреплён immutable commit/blob.
TEST-RESULTS.json: blob b1eb12acd02d4bff6cd18d386932f8e76ed0d881.
TEST-LOG.txt: blob d1cc081044fb143e60c113398d0b26786d1908e2.

Baseline:
puev5691/wellbeing-hq@f09ae9cd5be37269582deac05435f5ed5a06ca10:entities/koder/outbox/openai-booster-shape-diag-successor-wiring-r01
tree 6f536f10d99d08dcf5e1e671c5217650261a1548.

## Изменения и сохранённые границы

review_result_store.py содержит единственную поведенческую дельту: пропуск exact type=reasoning в _normalize_evidence. _extract_review_text и validate_record не расширены; reasoning нельзя добавить в сохранённое result evidence. Reasoning-only без допустимого текста не создаёт результат.

Обновлены transitive SHA-256 pins в review-result integration, diagnostic integration и outer runner. Runner и sentinel example привязаны к новому task и действующему writer. Изменение provenance не даёт live authority.

Final live-worker byte-identical:
blob d276de1050fd54e836ed4fc879eb384dba3aa1f1;
SHA-256 175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3.
При локальной материализации обнаружен лишний конечный newline; локальная копия приведена к исходным Git bytes и точному SHA до сборки и тестов. Source worker не модифицирован.

response_shape_store.py и systemd candidate byte-identical. Схема review-result v2 и strict readback сохранены.
В package CORRECTION.patch показывает дельту относительно baseline.
Unit candidate сохраняет прежние host paths как контракт; установка, запуск и systemd mutation не выполнялись.

## Детерминированные проверки

24 test methods, failures 0, errors 0, skipped 0, exit_code 0.

Проверены:
- reasoning до/после/вместе с разрешённым текстом;
- assistant-only regression;
- отсутствие summary/encrypted_content и любого reasoning payload в review-result;
- отсутствие значений reasoning payload в structure-only diagnostic;
- reasoning-only не даёт результат;
- function_call, tool/computer/web/file actions, output actions, неизвестные типы и aliases metadata/reasoning_summary блокируются;
- non-assistant roles и недопустимые content items блокируются;
- поздний запрещённый элемент не позволяет принять разрешённый префикс;
- прежняя семантика объединения нескольких допустимых текстовых сообщений сохранена;
- подмена review payload и добавление reasoning в stored evidence отвергаются strict validation;
- claim → synthetic resolver/transport → shape persist → shape readback → normalize → review persist → review readback;
- отказ shape readback запрещает normalization;
- отказ review readback запрещает terminal PASS;
- tool action сохраняет диагностическую структуру, но не review-result;
- повтор того же synthetic attempt не вызывает второй transport;
- sentinel, exact scope и четыре статические проверки systemd contract.

Тесты запускают точный final live-worker только с synthetic Resolver/Client в scratch. Socket connections принудительно запрещены. Настоящий SystemdCredentialResolver не вызывается.
Фикстуры, где результирующий record содержит provider_calls=1, моделируют один synthetic transport; фактических provider calls нет. Production e2e этим не доказывается.

## Учёт ограничений

provider_calls: 0
credential_value_reads: 0
host_systemd_mutation: 0
deployment: 0
retries: 0
fallback: none
tools: none
project_acceptance: NOT_GRANTED
production_acceptance: NOT_GRANTED
historical_prompt_or_authority_replay: 0
project_time: omitted

Consumed one-shot authority не использовалась. Старые Exchange Gate defects не исправлялись.
Текущая задача завершается KOD PASS и передачей KOO/SIS; substantive acceptance и SIS verification не подменяются readback отправителя.

## Источник для РЕДАКТОРА

После первого реального ответа Booster проект встретил границу собственных правил: модель вернула и текст ответа, и служебный контейнер reasoning, который строгая проверка не принимала. ОПЕРАТОР разрешил узкое изменение: служебный контейнер можно пропускать, но не превращать его содержимое в результат или действие.

КОДЕР реализовал это правило и проверил его без ещё одного реального вызова. Текст проходит, команды инструментам и неизвестные формы по-прежнему блокируются. Коррекция передана на независимую проверку; до неё ничего не устанавливается. Это продолжает историю перехода от найденной причины к проверенному исправлению, сохраняя отдельность человеческого решения, реализации и приёмки.

## Следующий шаг

SIS: independently verify exact immutable successor, manifest/checksums, test suite, lineage pins и сохранение fail-closed границ; provider calls=0, credentials=0, host/deployment=0. После результата вернуть KOO terminal и остановиться. Это запрос предусмотренной текущим task независимой проверки, не live/deployment authority.
KOD после публикации/readback и маршрутизации останавливается.

---
КТО: КОДЕР / KOD v0.5
ДЛЯ ЧЕГО: точный возврат non-live коррекции KOO/SIS и редакционный источник RED
СТАТУС: PASS_KOD_BOOSTER_REASONING_METADATA_NORMALIZER_CORRECTION_R01_READY_FOR_SIS_VERIFY
