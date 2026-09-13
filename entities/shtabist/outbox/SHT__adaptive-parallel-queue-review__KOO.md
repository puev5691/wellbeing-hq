# SHT → KOO: bounded process review безопасной параллельной адаптивной очереди

status: BOUNDED_PASS_WITH_PARALLEL_LANE_MODEL
scope: queue_concurrency_and_dependency_safety
production_mutation: no
automation_change: no
new_authority: no
project_time: omitted

## Смысл и требуемое действие

Проверена рабочая serial-модель KOO `EVENT/RESULT → FRESH PREFLIGHT → RECONCILE ALL PIPELINES → CLASSIFY → SELECT ONE NEXT OWNER` и exact task `KOO__adaptive-parallel-queue-review__SHT.md` commit `21c54d38ff087f442a9cddc10e97085e602e0589`, blob `d1e39a2fe1551aa2ad29a2bfd6228fffcd323e21`.

Вердикт: безопасная параллельность допустима без изменения authority и Exchange Gate, если KOO выбирает не одного следующего владельца, а **максимально независимый bounded set READY_PARALLEL lanes**, предварительно проверенный на hard conflicts. Параллельность является свойством задач и ресурсов, а не привилегией Сущности.

Минимальная корректировка алгоритма KOO: заменить `SELECT ONE NEXT OWNER` на `SELECT SAFE READY_PARALLEL SET`, при этом downstream decision nodes и shared mutable/privileged resources остаются сериализованными.

## 1. Когда задачи можно запускать одновременно

Две или более задачи получают `READY_PARALLEL` только если одновременно истинно всё ниже:

1. каждая имеет exact task/input, профильного владельца и допустимый bounded next action;
2. между задачами нет causal edge `A → B` или `B → A`; ни один результат не является обязательным input другого;
3. mutable write sets не пересекаются: задачи не меняют один exact artifact/current state/registry record in-place;
4. current-writer domains различны либо правила данного домена явно допускают несколько независимых writers; отсутствие такого доказательства означает запрет параллельного запуска;
5. нет общего privileged/runtime resource, для которого concurrent mutation может менять результат: production service, host config, credential state, deployment target, live external channel, exclusive device/session и подобное;
6. задачи не пытаются одновременно принять один и тот же release/acceptance/authority decision;
7. одна задача не меняет rules/authority/current-writer boundary, на которых основана допустимость второй;
8. обе могут вернуть immutable standalone result и пройти Exchange Gate независимо.

Если независимость не доказана exact evidence, default = не параллелить.

## 2. Hard conflicts, запрещающие parallel launch

### RESOURCE CONFLICT

Запрет при общем unsafe mutable/privileged resource. Примеры класса: один host/runtime config, один deployment slot, общий credential/config state, один внешний side-effect endpoint, один exclusive test environment без isolation.

Результат: одна lane остаётся `READY_PARALLEL`, другая переводится в соответствующее `WAITING_EXTERNAL/WAITING_ENTITY` либо `CONFLICT`, если порядок нельзя вывести из authority/causality.

### CURRENT-WRITER CONFLICT

Две задачи не могут одновременно быть writer одного exact current-state lineage или replacement/recovery state. Даже если файлы разные, конфликт считается существующим, если оба результата претендуют на изменение одного canonical current truth.

Результат: `CONFLICT`, пока не определён один writer или не разведены независимые immutable outputs + отдельный authorized reconciler.

### CAUSAL CONFLICT

Если B корректна только после результата A, B не `READY_PARALLEL`; она `WAITING_ENTITY` или `WAITING_EXTERNAL` по природе dependency. Предполагаемое ускорение не позволяет исполнять downstream по stale pre-state.

### AUTHORITY / RELEASE CONFLICT

Два исполнителя могут параллельно готовить независимые evidence/results для одного будущего решения, но **не могут параллельно принять сам общий acceptance/release/authority decision**, если такое полномочие принадлежит одному decision owner или требует совместного gate.

Decision node сериализуется после reconciliation всех required parents.

## 3. Operational states

### `READY_PARALLEL`

Есть exact executable bounded step; hard conflicts отсутствуют; lane может быть активирована независимо от других READY_PARALLEL lanes.

### `RUNNING`

Processing start подтверждён для exact task/instance. Сам inbox placement или activation request не равны RUNNING.

### `WAITING_EXTERNAL`

Нужен внешний ресурс, provider, entitlement, evidence, network/runtime condition или иная зависимость вне профиля доступных Entity actions.

### `WAITING_ENTITY`

Нужен exact результат/receipt/review другой Сущности, уже являющийся causal dependency.

### `WAITING_OPERATOR`

Нужно решение, authorization, activation или иное действие, которое по действующей границе принадлежит ОПЕРАТОРУ.

### `CONFLICT`

Обнаружен несовместимый writer/resource/causal/authority state либо одновременно пришли несовместимые результаты для одного downstream decision. Автоматический запуск/выбор запрещён до reconciliation.

### `CLOSED`

Цепочка или lane имеет проверяемый terminal result; required routing/receipt/acceptance выполнены в той мере, которая требуется её собственным completion contract. Inbox placement сам по себе CLOSED не создаёт.

`SERVICE_TAIL` можно сохранить как вспомогательную классификацию старого алгоритма, но это не parallel-running lane: она либо mechanically executable отдельно, либо остаётся waiting/closed-tail.

## 4. Reconciliation нескольких одновременно вернувшихся результатов

KOO не должен применять результаты в порядке прихода. Используется **arrival-independent reconciliation**:

1. каждый result сначала фиксируется как immutable artifact с exact commit/blob;
2. KOO строит parent relation: к какой task/pipeline/decision node относится результат;
3. independent results разных downstream nodes можно reconciliate отдельно и продвигать независимо;
4. results одного downstream decision складываются в `required_parent_set`;
5. decision node не становится executable, пока не обработаны все required parents либо exact rule не разрешает partial decision;
6. если один parent меняет assumptions второго, второй не отбрасывается: он помечается stale/needs-revalidation по exact evidence;
7. receipt подтверждает получение, а не acceptance; параллельный возврат не меняет это правило.

Иными словами, параллельным является **сбор независимых результатов**, а не произвольное коммутативное применение state changes.

## 5. Race/failure mode: два результата влияют на один downstream decision

Failure mode должен быть fail-closed:

`RESULT_A + RESULT_B → SAME_DECISION_NODE → WAITING_RECONCILIATION`

Практически это представляется как `CONFLICT`, если результаты несовместимы, либо как `WAITING_ENTITY`, если ожидается обязательный parent.

Запрещено:
- принимать решение по первому пришедшему результату, если второй был required parent;
- считать более поздний result автоматически superseding без declared lineage;
- позволять двум results независимо мутировать один downstream current state.

Допустимо:
- оба results immutable;
- KOO или иной уже уполномоченный decision owner выполняет отдельный reconcile/review;
- итоговый decision ссылается на exact identities обоих parents;
- при contradiction decision node = `CONFLICT`, а не last-write-wins.

## 6. Starvation prevention

Старый приоритетный порядок KOO сохраняется, но применяется к READY_PARALLEL candidates перед формированием набора.

Минимальный механизм:

1. emergency/safety/recovery/current-writer risks всегда выше fairness;
2. direct OPERATOR directive сохраняет приоритет;
3. затем учитывается downstream-unblock value;
4. далее для каждого независимого pipeline хранится `ready_age` как число reconciliation passes, в которых pipeline был READY, но не выбран;
5. при каждом пропуске `ready_age` увеличивает его приоритет;
6. после запуска/закрытия age сбрасывается;
7. round-robin применяется только среди сопоставимых READY_PARALLEL кандидатов после safety/authority guards.

Нельзя изобретать проектное время для aging. Достаточно счётчика verified scheduler/reconciliation passes либо ordered event sequence.

## 7. Нужен ли сейчас жёсткий maximum parallel lane count

Доказательств для произвольного численного лимита сейчас нет. Поэтому число вроде 2/3/5 не должно становиться нормативом из воздуха.

Рекомендуемая bounded политика сейчас:

`parallel_count = число READY_PARALLEL lanes, которые проходят conflict checks и реально могут быть активированы ОПЕРАТОРОМ без потери контроля`.

При ручном activation layer практический bottleneck сам ограничивает concurrency. Будущему scheduler понадобится configurable cap на основании измеряемых факторов: simultaneous activation capacity, shared tool/API quotas, failure/reconciliation load, host/resource limits. До таких данных hard numeric cap не утверждать.

При этом KOO вправе вернуть ОПЕРАТОРУ небольшой **activation batch** по приоритету, а не обещать запуск всех READY одновременно. Это диспетчеризация, не новая authority.

## 8. Manual OPERATOR activation → future scheduler

Текущий mapping:

`KOO reconcile/classify → SAFE READY_PARALLEL SET → OPERATOR activates selected lanes → processing evidence → RUNNING`.

Будущий supervisor заменяет только activation/scheduling mechanics:

`event detector → reconciler → conflict guard → scheduler → activation adapter → processing_started evidence`.

Он не должен наследовать новые права: authority rules, current-writer, approval boundaries и Exchange Gate остаются входными guards scheduler-а.

## 9. SHD под прямым управлением ОПЕРАТОРА

SHD не следует обозначать `CLOSED`, `WAITING_ENTITY` или обычным READY candidate только потому, что она выведена из adaptive queue.

Минимальное представление без нового operational state:

- `entity: SHD`;
- `queue_participation: excluded_operator_direct_control`;
- `scheduler_eligible: no`;
- `control_owner: OPERATOR` — как уже данная task boundary, не новое полномочие;
- `current_task/input`: exact verified SHD task, если имеется;
- `pending_return_event`: какой artifact/result должен вернуть SHD;
- `reentry_condition`: verified return/OPERATOR direction, после которого KOO снова reconciles pipeline;
- `queue_state`: отражает causal state самой цепочки (`WAITING_OPERATOR`, `WAITING_ENTITY`, `RUNNING` только при evidence), но scheduler не активирует её автоматически.

Таким образом, исключение из scheduler не стирает SHD из project DAG и не превращается в вечную потерянную ветку.

## 10. Минимальная корректировка KOO dynamic-next-route algorithm

Не нужен новый большой канон. Достаточно точечного delta к разделам 2, 3, 4, 6 и 7.

### Было

`EVENT/RESULT → FRESH PREFLIGHT → RECONCILE ALL PIPELINES → CLASSIFY READY/BLOCKED/WAITING → SELECT ONE NEXT OWNER → DISPATCH/LOCATOR → OPERATOR NEXT ROUTE`

### Рекомендуется

`EVENT/RESULT → FRESH PREFLIGHT → RECONCILE ALL PIPELINES → CLASSIFY → BUILD CONFLICT GRAPH → SELECT SAFE READY_PARALLEL SET → PRIORITIZE/AGE → DISPATCH EXACT LANES → OPERATOR ACTIVATION BATCH → RECONCILE RETURNED RESULTS`

Изменения:

1. `READY` разделить на `READY_PARALLEL` и неготовые WAITING/CONFLICT states;
2. перед выбором построить пары hard conflicts по write-set/current-writer/causal/resource/authority;
3. выбирать независимое множество lanes, а не ровно одного owner;
4. блок `СЛЕДУЮЩИЙ МАРШРУТ` заменить или дополнить `СЛЕДУЮЩИЕ ДОПУСТИМЫЕ МАРШРУТЫ`, где каждый lane сохраняет ENTITY / PIPELINE / EXACT INPUT / WHY NOW / EXPECTED RESULT / DO NOT / RETURN TO;
5. отдельно указывать `SERIALIZATION REASON` для READY, который не вошёл в batch из-за конфликта;
6. downstream shared decision всегда возвращать в reconciliation gate;
7. SHD держать как excluded_operator_direct_control с pending return event;
8. после каждого result fresh preflight и conflict graph строятся заново: ранее выбранный batch не является долгосрочным расписанием.

## 11. Итоговый bounded verdict

`BOUNDED_PASS_WITH_PARALLEL_LANE_MODEL`.

Противоречия с действующей serial KOO моделью нет: предлагаемая схема является её консервативным расширением. Serial execution остаётся частным случаем, когда conflict graph связывает все READY задачи либо activation capacity фактически равна одной lane.

Граница использования:
- process candidate для KOO review;
- автоматизации не изменены;
- production не изменён;
- новый scheduler не создан;
- новые полномочия не назначены;
- SHD не возвращена в adaptive queue и не лишена прямого OPERATOR control;
- любые дальнейшие изменения KOO current algorithm требуют отдельного KOO/OPERATOR решения по действующей authority boundary.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: bounded process review безопасной параллельной адаптивной очереди и минимального delta к KOO dynamic-next-route algorithm
СТАТУС: bounded_pass_with_parallel_lane_model
