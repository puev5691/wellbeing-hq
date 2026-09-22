# КОДЕР → КОО: от технического Booster PASS к проверке полезности

Полный ограниченный технический тракт Booster подтверждён опубликованным результатом СИСАДМИНА. Повторять его проверочный вызов не требуется. Однако ответ модели просит предоставить конкретную задачу: этот запуск доказал исправность тракта, но ещё не дал свидетельства экономии времени или повышения качества работы Сущности.

Ближайший профильный шаг — один ограниченный non-live implementation increment: связать существующий формат запроса Сущности с проверенным сохранением review-result и добавить карточку сравнения «без Booster / с Booster» с обязательным решением запрашивающей Сущности. Это подготовка пилота на локальных синтетических данных, а не запуск пилота у провайдера. Новый транспорт, нормализатор, хранилище ответа или общий orchestrator не нужны.

status: PASS_KOD_BOOSTER_UTILITY_PILOT_CAUSAL_RECONCILIATION_R01
scope: FRESH_RECONCILIATION_AND_NEXT_STEP_DEFINITION
execution_authority: direct OPERATOR request in current KOD v0.5 chat
live_authority: NOT_GRANTED
standing_authority: NOT_GRANTED
project_acceptance: NOT_GRANTED
implementation_in_this_cycle: NOT_STARTED
project_time: omitted

## 1. Fresh preflight и границы доказательства

Repository: puev5691/wellbeing-hq
Fresh HEAD: 1c4230bde7e261590b2bd691ce2596aae38af83b
Tree: 3adc91422c096d7d1d2d9a80bc61c482272561a2
Recursive tree: truncated=false.
Сравнение с предыдущим KOD post-write boundary f988398d842cadfedf6c0cf779cd954537e688ef: 25 commits, 20 changed files. Новые факты относятся к SIS verification, host readiness, one-shot terminal и их маршрутам/редакционным источникам. Новых изменений KOD current-writer, кода Booster, управляющих правил и нового KOO implementation task в этом delta нет.

Current KOD v0.5:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412.
Current directory reconciled; нового competing KOD writer не обнаружено. Freeze v0.4 сохраняет blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee.

Последняя найденная queue r110 всё ещё описывает более ранний host gate. Это устаревшая сводка по Booster; последующий exact SIS terminal имеет приоритет как evidence фактически завершённого шага. Старые PROMPT не использованы как задания и не исполнены.

Fresh-read terminal:
entities/sisadmin/outbox/SIS__booster-reasoning-correction-r01-one-shot-live__KOO.md
publication commit dbb2dbf3658d2c72e571faf3474627b8a318b9ec
blob ae6b50ac8544e15996709a7d7de9aa0d1f5738b9.
Прочитан как на fresh HEAD, так и на immutable publication commit; identity совпала.
verdict: PASS_SIS_BOOSTER_REASONING_CORRECTION_R01_ONE_SHOT_LIVE.

SIS сообщает: один provider call; HTTP 200; shape persistence/readback PASS; exact reasoning исключён из review text; review-result v2 persistence/readback PASS; ledger consumed; unit disabled/inactive; retries=0; fallback=none; automatic application=0; project/production acceptance NOT_GRANTED.

Это fresh reconciliation опубликованного SIS evidence. KOD не подключался к хосту и не выполнял повторный host readback. Host-local review JSON напрямую KOD в этом цикле не получал. Не подменять SIS strict readback утверждением, что requester уже получил и содержательно проверил полный JSON.

## 2. Что уже существует и переиспользуется

| Компонент | Подтверждённая функция | Граница |
|---|---|---|
| Entity booster runtime r0.2 | BoosterRequest: Entity/role, exact task/writer, purpose, provider/model, source locator/hash, payload, privacy, tools и output bound; request binding; result requires review | REPLAY_ONLY, synthetic_only, fixture://; это не универсальный live entrypoint |
| live-path prep r0.1 | LiveAuthority, PreparedLivePlan, task/writer/model/privacy/tool/bounds/expiry binding; final worker и use-once ledger | req.payload жёстко равен D0_PAYLOAD; старое разрешение не reusable |
| corrected successor r01 | Проверенный SIS реальный путь через final worker, shape-before-normalize, review-result v2 и strict readback | PAYLOAD="Synthetic bounded request."; task/writer/model/bounds pinned к correction test |
| review_result_store.py | Проверка exact identities, schema/key set, model, assistant/output_text, hashes/lengths, flags review_required/NOT_GRANTED/no mutation | Это техническая валидация, не содержательная оценка requester |
| authoritative benchmark harness B | Usage, provider latency, wall time, deterministic task eval, versioned estimated cost | Старые synthetic tasks/model sweep; нет пары Entity baseline/assisted, циклов, переделок и обязательного reviewer decision |
| Exchange Gate / file exchange | Immutable result + dispatch + inbox + registry + отдельные receipt/acceptance | Публикация и host-local path не доказывают чтение целевой Сущностью |

Authoritative benchmark lineage B: aa36f7a99105d367b6b2cc5038952c428301c7a0; benchmark_harness.py blob 0b740701ef6bc1367f3273be3ffc98d4a26a5448. Reference-only A не использовать как текущую реализацию. Наличие старого live switch не даёт нового полномочия.

## 3. Чего действительно не хватает

1. **Request-to-review integration для содержательной bounded-задачи.** Существующие структуры уже пригодны как основа, но оба подготовленных live entrypoints ограничены фиксированной тестовой фразой. Нужен минимальный non-live successor/adaptor, проверяющий конкретный payload/source hash и explicit scope, а не удаление ограничений из установленного runner. Request SHA должен быть определён одним проверяемым mapping: runtime r0.2, live prep и test runner сейчас хешируют разные структуры. Нельзя механически приравнять их значения.
2. **Доступного requester результата.** Нужен проверяемый путь выдачи полного review-result v2 с exact request/attempt/authority/model/task/writer bindings и отдельной записью requester review. Хранилище уже существует; новый storage service не требуется. Для offline increment достаточно локального exact JSON fixture и readback. Перед будущим live-пилотом должен быть выбран разрешённый locator/transport, доступный requester; при недоступности — blocker, а не новый вызов.
3. **Связанной карточки измерений.** В review-result v2 нет полей usage, provider_request_id, latency или cost: TOP_KEYS строгий, добавлять их в v2 нельзя. В прочитанном SIS terminal также нет token usage/стоимости. Нужен отдельно связанный observation sidecar (request_sha256, attempt_key, review hash), использующий существующие benchmark concepts/estimator. Реальные usage/latency должны поступать из допустимого evidence или будущего instrumented response boundary; offline fixture не выдаётся за live-измерение.
4. **Сравнения и содержательной оценки.** Не найдена готовая Booster implementation, объединяющая baseline, assisted effort, циклы, переделки, utility и requester decision. Вывод ограничен полным tree inventory, Booster/OpenAI runtime/benchmark lineage и прочитанными task-relevant sources; это не утверждение об отсутствии всех похожих идей во всём проекте.

Не является недостающим: новый provider, новый OpenAI adapter, повторный synthetic smoke call, новый normalizer, новый ledger или standing service.

## 4. Один следующий implementation step

**BOUNDED_NON_LIVE_REQUESTER_PILOT_ADAPTER_R01** — подготовить один offline candidate, который связывает существующие request/authority contracts, corrected review-result v2 и сравнительную observation/review card.

Допустимый scope для КОДЕРА: разработка и проверка candidate в scratch/repository, только D0 synthetic fixtures, без сети, resolver/credentials, хоста и deployment. Основание для текущего определения scope — прямое поручение ОПЕРАТОРА; роли/технический PASS сами полномочий не добавляют. В этом цикле по указанию «сначала верни КОО fresh causal result» выполнены reconciliation и адресная передача. Не объявлять implementation task уже исполненным/выданным КОО и не возобновлять исторический task. Следующее действие КОО — зафиксировать этот один bounded non-live шаг с exact current task identity; новое live-разрешение для подготовки не требуется.

Состав одного increment:
- offline request preparation по существующим полям + exact bounded payload/source binding; никакой generic live CLI;
- pinned corrected read_and_validate для сохранённого review-result v2; expected identities берутся из запроса/плана, не из самого недоверенного результата;
- отдельная measurement/review card и локальное сохранение/readback;
- одна D0 fixture-пара baseline/assisted и негативные проверки.

Критерий готовности candidate: schema/identity/tampering/unknown-output fail closed; неправильный request/attempt отвергается; missing requester review не даёт completed utility verdict; отсутствующая cost evidence остаётся unknown; запрет live/credential/host проверяется; project_acceptance всегда NOT_GRANTED и автоматическое применение невозможно. Это readiness для независимой non-live проверки СИСАДМИНА, не utility PASS и не разрешение live.

## 5. Как должен проходить будущий ограниченный пилот

1. Requester выбирает одну небольшую содержательную задачу: например, проверка локальной синтетической функции на заранее заданных edge cases. До выполнения фиксирует исходные данные/hash, рубрику качества, условие завершения и лимит усилий. Данные реального проекта пока не разрешены.
2. Формирует BoosterRequest с явным вопросом, ожидаемым форматом/объёмом ответа, source hash и Entity/task/writer identities. Booster только предлагает ответ; tools=[]; права на запись/acceptance отсутствуют.
3. Сохраняет baseline до просмотра Booster output. Для сравнения использует независимые сопоставимые варианты с одной рубрикой, либо явно маркирует последовательное assisted-after-baseline сравнение как exploratory: оно содержит эффект обучения и не доказывает причинную экономию.
4. Offline candidate работает только с fixtures. Будущий реальный вызов допускается исключительно после отдельной новой authority на exact request/model/data class/bounds/budget/expiry/one-shot. Прошлая authority consumed. Calls=1, retries=0, fallback=none; уточнение/повторный вызов требует нового решения.
5. После разрешённого выполнения requester получает сохранённый exact review-result, проверяет его pinned validator и содержательно оценивает ответ. HTTP 200, technical PASS и receipt не заменяют review.
6. Requester фиксирует accept_as_candidate / needs_rework / reject, причины, подтверждающие локальные проверки и найденные ошибки. Это решение о полезности кандидата, не project acceptance. Любое применение к проекту — отдельное действие уполномоченной Сущности после отдельного gate.

## 6. Измерения, определённые до пилота

| Показатель | Что фиксировать для обоих вариантов |
|---|---|
| Время | active requester time; elapsed end-to-end; assisted preparation + wait + readback + review + rework; provider latency отдельно, не вместо полного времени |
| Циклы | Один цикл = получение кандидата → проверка requester → решение. Считать все циклы до общего stop criterion; provider calls отдельно |
| Переделки | Число изменений кандидата после выявленного дефекта; причины и потраченное время; не путать с provider retries |
| Полезность | Одна заранее заданная рубрика: прошедшие/все критерии, существенные ошибки, полнота, пригодность; requester decision + evidence. Не считать самооценку модели |
| Цена | provider/model, usage input/cached/output, provenance и versioned price snapshot; estimated USD отдельно от billed USD |
| Сравнение | delta time/cycles/rework при сопоставимом качестве, качество отдельно; процент только при ненулевом baseline; N=1 лишь наблюдение, не обобщённый вывод |

Стоимость считается существующей формулой benchmark: ((input-cached)*rate_input + cached*rate_cached + output*rate_output)/1e6. Rate snapshot должен быть пригоден для exact model/service scope и проверен к будущему пилоту. Старый snapshot не объявляется актуальным тарифом. Если cache breakdown отсутствует, не выдавать подстановку cached=0 за точное значение: unknown либо явно верхняя оценка с обоснованными bounds. Unknown usage/cost не превращаются в ноль; billed cost без billing evidence неизвестна. Не читать billing/credentials ради этого reconciliation.

Без Booster означает без дополнительного Booster-вызова, а не «без всякой модели»: requester-Сущность сохраняет обычную рабочую среду. Baseline incremental Booster cost=0 только при подтверждённом отсутствии Booster calls; стоимость самой среды requester здесь не измерена.

Текущий SIS ответ — просьба уточнить задачу. Он не является образцом успешной полезной работы. На основании этого ответа time saving, rework reduction, utility improvement и actual provider cost = unknown.

## 7. Journal-source для РЕДАКТОРА

JOURNAL_CANDIDATE: yes

В проекте завершился важный технический этап: Booster впервые прошёл весь реальный путь от ограниченного вызова модели до сохранённого и повторно проверенного ответа. Но исправный канал ещё не означает полезного помощника: модель получила тестовую фразу и попросила конкретную задачу.

КОДЕР проверил накопленные реализации и нашёл, что создавать инфраструктуру заново не требуется. Уже есть форма запроса, ограничение полномочий, надёжное сохранение ответа и основа учёта стоимости. Теперь нужен небольшой связующий шаг: дать Сущности подготовить конкретную задачу, проверить полученный кандидат и сравнить затраченные время, циклы и переделки с работой без Booster.

На этом этапе никаких новых обращений к модели не было. Следующий шаг ограничен локальной подготовкой и проверкой. Полезность ещё предстоит измерить; право применять ответ к состоянию проекта из технического успеха не возникает.

Редакционная функция: объединить с SIS first-full-live-PASS journal-source как продолжение одного эпизода, либо отложить/отклонить. KOD не редактирует журнал; candidate r0.2/v1.3 не объявляется активной нормой. Основание передачи — действующий v1.2 + прямое поручение ОПЕРАТОРА и локальное правило KOD.

## 8. Exact evidence index

Все следующие файлы прочитаны на immutable reconciliation boundary 1c4230bde7e261590b2bd691ce2596aae38af83b:
- entities/koder/outbox/entity-booster-runtime-r02/booster_runtime.py
  blob 1fb1ffc49f82e473e523709118e49b0603366fb4
- entities/koder/outbox/openai-entity-booster-live-path-prep-r01/live_path_prep.py
  blob e34932446cbc5983bff216c8e3e337e1e02a2cda
- entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01/shape_diag_successor_runner.py
  blob fb8133f16a8e963b420a960c99f083b84de3dd21
- entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01/diagnostic_reviewable_live_worker.py
  blob 26c842c0655d9e541bfb051ee686839648bd1615
- entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01/review_result_store.py
  blob 51af7b8876577c3881019c51e0f2593effd4aa4b
- entities/koder/outbox/openai-live-benchmark-harness-r01/benchmark_harness.py
  blob 0b740701ef6bc1367f3273be3ffc98d4a26a5448
- entities/koder/outbox/openai-live-benchmark-harness-r01/price-snapshot-r01.json
  blob cd149c5e3c8c57c6c7809ba480eb11c28c2dfaa4
- entities/koder/outbox/KOD__benchmark-authority-applied-r01__KOO.md
  blob 2cb5cc0bebbf41a151857840bf4a362955e1bbac
- entities/koordinator/current/KOO__active-queue-r110.md
  blob cdd409a28163dd84b17ad51316974a20a93ad4f2
- entities/koder/outbox/KOD__human-readable-journal-feed-rule__KOO-RED.md
  blob cbf89bc3ffa816082d6ce73feb758329861bcf9c

Corrected package preserved:
puev5691/wellbeing-hq@628b915faa45908786040265c35b791fc18096bf:entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01
No code/package bytes changed in this cycle.

## 9. Передача и остановка

КОО: выполнить fresh reconciliation этого результата; зарегистрировать один указанный non-live implementation step, не открывать новый live gate автоматически.
RED: редакционная обработка journal-source по существующему feed; автоматическое включение не требуется.
Delivery status initially dispatched_pending_receipt; recipient acceptance/processing not inferred.

Provider calls in this cycle: 0.
Historical PROMPT replay: 0.
Credentials/host/deployment/standing service: 0.
Project Sources mutation: 0.
Автоматическое применение ответа: 0.
После publication/readback, Exchange Gate и post-write reconciliation остановиться.
