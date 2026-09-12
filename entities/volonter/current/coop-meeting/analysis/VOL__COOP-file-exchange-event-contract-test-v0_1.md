# Проверка EVENT-CONTRACT на file-exchange lifecycle — v0.1

## Назначение

Этот проход проверяет, выдерживает ли `VOL__COOP-event-contract-v0_1.md` другой тип проектного процесса, не связанный напрямую с activation logic: адресный файловый обмен.

Тестовый lifecycle:

`artifact prepared → dispatched/addressed → received → accepted/rejected`

Цель проверки не в повторном аудите Exchange Gate. Цель — выяснить, достаточно ли общего event contract для точного описания транспорта, receipt и содержательного acceptance без подмены одного состояния другим.

Результат: `PARTIAL_PASS_WITH_GENERIC_SCHEMA_EXTENSIONS`.

Контракт в целом удерживает causal/provenance chain, но file-exchange case выявил две общие недостающие сущности: универсальный `process_id` и явный `state_dimension`.

## 1. Проверяемый case

Взят реальный обмен:

`KOD__activation-product-e2e-blocker__KOO`

### Исходный артефакт

`entities/koder/outbox/KOD__activation-product-e2e-blocker__KOO.md`

Immutable identity:

- commit: `020c4056d8ab1b246366b47e1402033f51b3def3`;
- blob: `e360e277990955929a78b9543b4d6ba0de56e027`.

Artifact status:

`BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP`.

Его смысл: repository-side inputs повторно проверены, но KOD не имеет интерфейса для создания/авторизации product-side ChatGPT Work PR trigger. Artifact просит KOO маршрутизировать prerequisite способному actor.

### Dispatch

`routes/dispatch/KOD__activation-product-e2e-blocker__KOO.md`

Immutable dispatch commit:

`bcb6f1056d12db9f8ccec1c0927146a993e95072`.

Dispatch прямо связывает:

- sender `koder`;
- recipient `koordinator`;
- exact artifact path;
- artifact commit/blob;
- inbox pointer;
- `status: dispatched`;
- `receipt: null`;
- `acceptance: null`.

### Addressed inbox pointer

`entities/koordinator/inbox/KOD__activation-product-e2e-blocker__KOO.md`

Pointer содержит exact artifact identity и dispatch commit, статус `addressed`, а receipt/acceptance в момент создания ещё `null`.

Собственная immutable identity этого pointer в данном проходе отдельно не нормализована, поэтому он используется как transport evidence, но не как обязательная metric-grade стадия.

### Receipt

`routes/receipts/KOD__activation-product-e2e-blocker__KOO.receipt.md`

Immutable receipt commit:

`fc08093403e4b76cbd95c8bcb0a3e287306fe3a2`.

Receipt фиксирует:

- exact source artifact commit/blob;
- exact source dispatch commit;
- recipient `koordinator`;
- `receipt_status: read_and_verified`;
- `acceptance: separate_decision_required`.

То есть получение и проверка транспорта прямо отделены от содержательного acceptance.

### Отдельное acceptance decision

`entities/koordinator/outbox/KOO__activation-product-e2e-blocker-decision__KOD.md`

Current content фиксирует:

`ACCEPTED_AS_CORROBORATING_EXTERNAL_DEPENDENCY`.

Decision прямо ссылается на source artifact commit `020c...` и receipt commit `fc080...`.

Однако собственный immutable commit этого decision artifact в текущем проходе не установлен. Поэтому событие acceptance допустимо как исследовательское `DIRECT_CURRENT`, но не как metric-grade event до фиксации его собственной immutable identity.

## 2. Нормализованные события

### FX-EVT-01 — artifact prepared

`event_id: FX-EVT-01`
`event_type: artifact_prepared`
`object_id: exchange_object:KOD__activation-product-e2e-blocker__KOO`
`process_id: file_exchange:KOD->KOO:activation-product-e2e-blocker`
`actor_id: KOD`
`source_event_id: null`
`source_artifact: entities/koder/outbox/KOD__activation-product-e2e-blocker__KOO.md`
`source_commit: 020c4056d8ab1b246366b47e1402033f51b3def3`
`source_blob: e360e277990955929a78b9543b4d6ba0de56e027`
`evidence_level: DIRECT`
`state_dimension: content_work_state`
`status_after: BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP`
`result_class: BLOCKED`
`branch_status: ROOT`

Claim boundary: подготовленный blocker artifact не означает dispatch, receipt, acceptance или разрешение underlying product dependency.

### FX-EVT-02 — dispatch recorded

`event_id: FX-EVT-02`
`event_type: dispatch_recorded`
`object_id: exchange_object:KOD__activation-product-e2e-blocker__KOO`
`process_id: file_exchange:KOD->KOO:activation-product-e2e-blocker`
`actor_id: KOD`
`source_event_id: FX-EVT-01`
`source_artifact: routes/dispatch/KOD__activation-product-e2e-blocker__KOO.md`
`source_commit: bcb6f1056d12db9f8ccec1c0927146a993e95072`
`evidence_level: LINKED`
`state_dimension: transport_state`
`status_before: prepared`
`status_after: dispatched`
`result_class: ROUTED`
`branch_status: CONTINUATION`

Claim boundary: dispatch не доказывает receipt и не доказывает acceptance.

### FX-EVT-03 — addressed pointer observed

`event_id: FX-EVT-03`
`event_type: addressed_pointer_created`
`object_id: exchange_object:KOD__activation-product-e2e-blocker__KOO`
`process_id: file_exchange:KOD->KOO:activation-product-e2e-blocker`
`actor_id: KOD`
`source_event_id: FX-EVT-02`
`source_artifact: entities/koordinator/inbox/KOD__activation-product-e2e-blocker__KOO.md`
`source_commit: unresolved_in_this_pass`
`evidence_level: DIRECT_CURRENT_NOT_METRIC_GRADE`
`state_dimension: transport_state`
`status_after: addressed`
`result_class: ROUTED`
`branch_status: CONTINUATION`

Claim boundary: наличие inbox pointer само по себе не является receipt.

Поскольку self-commit pointer не разрешён, FX-EVT-03 исключается из metric-grade calculation. Это не ломает lifecycle: receipt напрямую ссылается на artifact и dispatch.

### FX-EVT-04 — receipt recorded

`event_id: FX-EVT-04`
`event_type: receipt_recorded`
`object_id: exchange_object:KOD__activation-product-e2e-blocker__KOO`
`process_id: file_exchange:KOD->KOO:activation-product-e2e-blocker`
`actor_id: KOO`
`source_event_id: FX-EVT-02`
`source_artifact: routes/receipts/KOD__activation-product-e2e-blocker__KOO.receipt.md`
`source_commit: fc08093403e4b76cbd95c8bcb0a3e287306fe3a2`
`evidence_level: LINKED`
`state_dimension: transport_state`
`status_before: dispatched`
`status_after: received_and_verified`
`result_class: RECEIVED`
`branch_status: CONTINUATION`

Дополнительное state observation в том же source:

`state_dimension: acceptance_state`
`status_after: separate_decision_required`

Claim boundary: receipt подтверждает чтение/verification exact exchange object, но не содержательное acceptance результата и не Work-run success.

### FX-EVT-05 — acceptance decision observed

`event_id: FX-EVT-05`
`event_type: acceptance_decision_made`
`object_id: exchange_object:KOD__activation-product-e2e-blocker__KOO`
`process_id: file_exchange:KOD->KOO:activation-product-e2e-blocker`
`actor_id: KOO`
`source_event_id: FX-EVT-04`
`source_artifact: entities/koordinator/outbox/KOO__activation-product-e2e-blocker-decision__KOD.md`
`source_commit: unresolved_self_identity_in_this_pass`
`evidence_level: DIRECT_CURRENT_NOT_METRIC_GRADE`
`state_dimension: acceptance_state`
`status_before: separate_decision_required`
`status_after: ACCEPTED_AS_CORROBORATING_EXTERNAL_DEPENDENCY`
`result_class: ACCEPTED_BOUNDED`
`branch_status: CONTINUATION`

Decision explicitly links the source artifact and receipt commit, so semantic parentage is strong. Но до получения собственного immutable commit decision event не должен входить в metric-grade time series.

Отдельное underlying work-state observation после acceptance:

`state_dimension: content_work_state`
`status_after: WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`

Это ключевой факт: **acceptance exchange object не означает разрешение технического blocker**.

## 3. Что выдержал EVENT-CONTRACT-v0.1

Контракт без специальных исключений сохранил:

- explicit parent links;
- immutable provenance;
- разделение DIRECT/LINKED/неполной evidence;
- claim boundaries;
- отсутствие автоматического повышения статуса;
- запрет считать receipt содержательным acceptance;
- запрет считать acceptance решением underlying technical problem.

Поэтому базовая идея event graph подтверждается на втором типе процесса.

## 4. Что контракту не хватило

### 4.1 `experiment_id` слишком узок

Для activation experiment поле естественно. Для обычного file exchange оно искусственно.

Нужен более общий:

`process_id`

Он связывает события одного процесса независимо от того, является ли процесс экспериментом, delivery, recovery, review или task handover.

`experiment_id` следует оставить как optional domain field, когда процесс действительно является экспериментом.

Рабочая иерархия:

`object_id → process_id → optional experiment_id → event_id`.

### 4.2 Одного `status_before/status_after` недостаточно

В одном и том же lifecycle одновременно существуют разные состояния:

- transport: `prepared → dispatched → received`;
- acceptance: `pending → separate_decision_required → accepted/rejected`;
- underlying work: `BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP → WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`.

Если хранить один scalar status, acceptance легко затрёт transport state или, ещё хуже, будет ошибочно воспринят как разрешение blocker.

Поэтому нужен обязательный:

`state_dimension`

Кандидатные значения в этом case:

- `transport_state`;
- `acceptance_state`;
- `content_work_state`.

Общий смысл: status всегда принадлежит конкретной размерности состояния.

## 5. Обобщённая схема после второго теста

Вместо:

`experiment → events → status`

рабочая модель становится:

`object → process → events → state_dimension-specific transitions`.

То есть состояние объекта в момент времени является не одним словом, а вектором:

`state(object,t) = {transport, acceptance, work, authority, ...}`

Конкретный event изменяет только заявленную `state_dimension`, если source/decision_scope не доказывает большее.

Это резко уменьшает риск статусной подмены.

## 6. Metric-grade boundary

Для metric-grade event должны быть выполнены минимум:

1. event имеет stable `event_id`;
2. известны `object_id` и `process_id`;
3. задана `state_dimension`;
4. source artifact имеет immutable self identity;
5. causal parent доказан либо явно unresolved;
6. event_time/publication_time semantics разделены;
7. claim boundary зафиксирована.

В этом case metric-grade готовы FX-EVT-01, FX-EVT-02 и FX-EVT-04.

FX-EVT-03 и FX-EVT-05 остаются research-grade до разрешения их self immutable commits.

## 7. Anti-regression правила

1. `dispatch != receipt`.
2. `receipt != acceptance`.
3. `acceptance(exchange object) != success(underlying work object)`.
4. Технический blocker нельзя закрыть только потому, что документ о blocker принят.
5. Транспортный status не должен перезаписывать substantive/work status.
6. Acceptance без собственного immutable source identity не включается в metric-grade time series.

## 8. Итог проверки

`EVENT-CONTRACT-v0.1` прошёл второй доменный тест частично успешно.

Базовая causal/provenance модель оказалась переносимой с activation на file exchange. Но выявлены две действительно общие schema extensions:

- `process_id` как универсальный process identity;
- `state_dimension` как обязательная размерность перехода состояния.

Их следует внести в следующий кандидат `EVENT-CONTRACT-v0.2` до расчёта routing/latency metrics.

## Следующий цикл

1. собрать `EVENT-CONTRACT-v0.2` с `process_id` и `state_dimension`;
2. не удалять `experiment_id`, а сделать его optional specialization;
3. проверить v0.2 на третьем процессе, не activation и не file exchange;
4. предпочтительный третий test: recovery/preservation lifecycle, потому что там хорошо различаются structural readiness, readback, archive acceptance и practical recoverability;
5. только после третьего доменного теста переходить к первым вычисляемым process metrics.

---

Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: проверить переносимость EVENT-CONTRACT на реальном file-exchange lifecycle и выявить общие schema extensions.
Статус: `candidate_research_artifact`; не Project Source; не production schema; не ТЗ КОДЕРУ.
Метка времени: не ставилась; разрешённый проектный источник времени не использован.
