# Project evidence audit для операциональных метрик — v0.1

## Назначение

Этот проход проверяет, какие из шести метрик из `VOL__COOP-operational-metrics-v0_1.md` можно честно восстановить по уже существующим артефактам «Благополучия», не достраивая отсутствующие события из памяти или здравого смысла.

Результат намеренно консервативный: отсутствие нужного evidence не трактуется как плохое состояние системы. Оно означает только, что метрика сейчас не вычислима или вычислима лишь как proxy.

Статусы:

- `MEASURABLE_NOW` — минимальные события и границы присутствуют;
- `PARTIAL_PROXY_ONLY` — есть часть цепочки, но полного наблюдаемого объекта нет;
- `NOT_MEASURABLE_FROM_CURRENT_FIELD` — критические события отсутствуют;
- `NEGATIVE_TEST_EVIDENCE` — поле позволяет подтвердить не успех, а конкретный failure/boundary.

## AUD-01 — handover_success / recovery continuity

### Что найдено

Контур recovery структурно развит: существуют immutable recovery/current-state inputs, manifests/checksums/readback, а отдельные пакеты явно различают `structurally_ready` и practical recovery.

KAN preservation checkpoint прямо фиксирует:

- publication/readback подтверждены;
- package structurally ready;
- полный practical recovery-test новым экземпляром не выполнялся;
- `recoverability_verified` не заявляется.

Параллельно activation line даёт ещё более сильную отрицательную проверку. SIS установил, что текущий стек достигает:

`GitHub event → detector/activation worker → local worker state + handler process`

но не даёт независимо проверяемого перехода к `exact ChatGPT Entity profile-processing instance`. Worker-local `processing_started` признан orchestration marker, а не доказательством реального запуска Entity.

KOO/SHT сохранили ту же границу и запретили повышать статус isolated worker E2E до real Entity activation PASS.

### Вывод по MTR-03

Сейчас нельзя присвоить положительный `handover_success` для полного Entity handover/recovery. Есть сильное `NEGATIVE_TEST_EVIDENCE`: артефактная часть передачи существует, но критическое событие `new_owner/exact_instance actually continues profile processing` пока не доказано.

Для ordinal scale из operational-metrics честный результат сейчас: **не оценивать числом**. Это не `0`, потому что структурная передача не сорвана; это `unknown_pending_practical_initiation_test`.

Status: `NEGATIVE_TEST_EVIDENCE`.

Evidence:
- `entities/kancelar/outbox/KAN__preservation-checkpoint__ARH.md`;
- `entities/sisadmin/outbox/SIS__real-entity-activation-boundary__KOO.md`;
- `entities/shtabist/outbox/SHT__real-entity-activation-org-gate__KOO.md`.

## AUD-02 — decision_latency

### Что найдено

GitHub сохраняет commit identities и commit metadata для сигналов, dispatch, receipts, решений и новых заданий. Следовательно, технически можно построить временные интервалы между артефактами.

Но semantic start-point пока не унифицирован. Например, для activation blocker можно выбрать как `signal_observed`:

- момент возникновения runtime failure;
- момент создания SIS artifact;
- момент dispatch;
- момент receipt KOO;
- момент организационной классификации SHT.

Все эти точки разные и означают разные процессы.

### Вывод по MTR-02

Сырые timestamps доступны, но `decision_latency` пока нельзя считать валидной метрикой без event-normalization contract, который однозначно задаёт:

`signal_observed`, `decision_required`, `decision_made`, `decision_executed`.

Коммит-время может стать timestamp evidence, но не определяет смысл события само по себе.

Status: `PARTIAL_PROXY_ONLY`.

Дополнительный вывод: будущей event schema нужен стабильный `event_type` внутри артефакта, а не вывод типа события из commit message/path.

## AUD-03 — knowledge_holder_concentration

### Что найдено

В проекте есть file-first recovery, experience layer, manifests, current-state и адресные handoff. Это снижает потенциальную зависимость от памяти конкретного чата.

Однако текущий GitHub field не содержит достаточной карты:

`critical_function → participants/entities able to execute independently`.

Наличие инструкции, роли или recovery package не доказывает independent competence. Практический recovery-test нового экземпляра в проверенном KAN case не выполнен. Activation boundary также показывает разрыв между наличием recovery input и фактическим продолжением работы новым processing instance.

### Вывод по MTR-04

`knowledge_holder_concentration` сейчас не вычислима. Можно видеть инфраструктуру распределения знания, но нельзя честно посчитать redundancy по критическим функциям.

Status: `NOT_MEASURABLE_FROM_CURRENT_FIELD`.

Минимальный недостающий evidence:
- stable function_id;
- independent_execution_by_entity;
- verified result;
- использованный recovery/knowledge artifact;
- external_prompt_count или эквивалент зависимости от прежнего носителя.

## AUD-04 — cross_node_absorption_capacity

### Что найдено

Проект регулярно маршрутизирует blockers и задачи между KOD, SIS, SHT, KOO, ARH, KAN и OPERATOR. Activation case демонстрирует функциональное переназначение следующего шага: SIS дошёл до runtime boundary, SHT классифицировал organizational boundary, KOO выбрал product-side Work path, KOD подготовил repository-side package, а внешний product prerequisite был адресован OPERATOR.

Это подтверждает наличие **межузловой маршрутизации**.

Но это ещё не `cross_node_absorption_capacity` в строгом смысле. Не наблюдается отказ узла с измеримым набором потерянных critical functions и последующее доказанное восстановление этих функций другим узлом. Передача следующей задачи между профильными Сущностями является routing, а не absorption.

### Вывод по MTR-05

Текущие данные годятся только как proxy для `cross_node_coordination/reassignment`, но не позволяют вычислять absorption rate.

Status: `PARTIAL_PROXY_ONLY`.

Необходим будущий test case:
`function_owner unavailable/degraded → reassignment → replacement execution → verified result → receiving-node load/cost`.

## AUD-05 — participation_concentration

### Что найдено

GitHub отражает действия Сущностей, но не содержит полного множества `eligible participants` для каждой decision opportunity. Также commit/activity count нельзя принимать за участие в коллективном решении.

KOO принимает решения, профильные Сущности готовят evidence и рекомендации, OPERATOR принимает отдельные внешние решения, но из текущего поля нельзя построить denominator `eligible_events_i` и нельзя одинаково классифицировать contribution/vote/proposal/review для всех decision classes.

### Вывод по MTR-01

По commit counts считать participation concentration нельзя. Получился бы классический случай, когда удобная телеметрия изображает социальный процесс, который она не измеряет.

Status: `NOT_MEASURABLE_FROM_CURRENT_FIELD`.

Нужен отдельный decision-event layer с eligibility и типом участия.

## AUD-06 — formal_actual_rights_gap

### Что найдено

Проект имеет формальные role/authority boundaries и регулярно фиксирует запреты повышения статуса, writer authority, acceptance и границы полномочий. Это даёт хороший слой **formal rights/authority**.

Но для `actual right` нужна наблюдаемая попытка воспользоваться конкретным правом и последующий процедурный эффект или блокировка. Текущие проектные маршруты дают отдельные примеры полномочий/ограничений, но пока не образуют нормализованный participant × right_type dataset.

### Вывод по MTR-06

Метрика концептуально применима к проекту, но сейчас не вычислима без rights-event schema.

Status: `PARTIAL_PROXY_ONLY`.

Особенно перспективный project case: `writer authority / acceptance authority / task-routing authority`, потому что эти границы уже явно присутствуют в артефактах и часто проверяются fail-closed.

## Главный результат аудита

Из шести метрик ни одна пока не должна публиковаться как полноценная рассчитанная project metric.

Это не провал модели. Наоборот, audit выявил, чего ей не хватает между файловым полем и вычислением:

`artifact log ≠ event dataset`.

Проект уже хорошо сохраняет provenance и результаты, но для динамической модели нужен отдельный слой нормализации событий.

Рабочая цепочка теперь уточняется:

`raw artifact/commit`
→ `normalized event with explicit type`
→ `entity/function/decision identifiers`
→ `metric-ready event set`
→ `computed metric`
→ `interpretation with boundary`.

## Минимальный event-normalization contract — candidate

Для следующих project tests достаточно начать с полей:

- `event_id`;
- `event_type`;
- `subject_entity`;
- `object_id` (`task/function/decision/right/handover/node`);
- `source_artifact`;
- `source_commit/blob`;
- `event_time_source`;
- `previous_state`;
- `new_state`;
- `result_verified`;
- `related_event_ids`;
- `evidence_boundary`.

Для специфических метрик добавляются:

- handover: `old_owner`, `new_owner`, `external_prompt_count`, `result_verifier`;
- decision: `signal_id`, `decision_class`, `decision_required`, `decision_executed`;
- knowledge: `function_id`, `independent_executor`, `knowledge_artifact_used`;
- absorption: `failed_node`, `receiving_node`, `function_recovered`, `receiving_load_delta`;
- participation: `decision_id`, `eligible`, `participation_type`;
- rights: `right_type`, `formal_grant`, `exercise_attempt`, `exercise_effect`.

## Тест, который уже можно подготовить без КОДЕРА

Наиболее готовый следующий исследовательский pilot: **manual event normalization одного activation lineage**.

Берётся одна bounded цепочка `SIS blocker → SHT classification → KOO decision → KOD package → OPERATOR product blocker` и вручную превращается в normalized events. После этого проверяется:

1. хватает ли предложенных полей;
2. можно ли однозначно построить состояния;
3. где исчезает provenance;
4. какие метрики становятся вычислимыми;
5. какие остаются семантически неоднозначными.

Это исследовательская нормализация, а не программная разработка. Запрет на dispatch КОДЕРУ сохраняется.

## Evidence base

- `entities/volonter/current/coop-meeting/analysis/VOL__COOP-operational-metrics-v0_1.md`;
- `entities/sisadmin/outbox/SIS__activation-worker-v02-e2e-result__KOO.md` — isolated worker `8/8 PASS`, но scope не включает real Entity activation;
- `entities/sisadmin/outbox/SIS__real-entity-activation-boundary__KOO.md` — `BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY`;
- `entities/shtabist/outbox/SHT__real-entity-activation-org-gate__KOO.md` — `BLOCKED_ON_ENTITY_START_RESUME_INTERFACE`;
- `entities/kancelar/outbox/KAN__preservation-checkpoint__ARH.md` — recovery structurally ready, practical recovery-test not performed;
- `entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md` — `BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`;
- `entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md` — repository package ready, product-side Work trigger remains prerequisite.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: проверить измеримость candidate operational metrics на фактическом информационном поле проекта и определить минимальный event-normalization layer.
Статус: `candidate_project_evidence_audit`.
Время: не указано; отдельный разрешённый источник проектного времени не использовался.
