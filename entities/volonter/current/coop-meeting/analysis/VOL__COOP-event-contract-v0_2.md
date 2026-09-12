# EVENT-CONTRACT для модели организационной динамики — v0.2

## Назначение

Этот документ уточняет кандидатный `EVENT-CONTRACT-v0.1` после двух доменных проверок: activation lineage и file-exchange lifecycle.

Цель: получить общий контракт события, который способен описывать разные организационные процессы без ложного склеивания причинности, без подмены транспорта содержательным результатом и без перезаписи одного состояния объекта другим.

Статус: `candidate_research_contract`. Это не Project Source, не production-схема и не техническое задание КОДЕРУ.

## 1. Основная модель v0.2

Базовая структура:

`object → process → events → state_dimension-specific transitions`

Опционально процесс может содержать экспериментальную ветвь:

`object → process → optional experiment → events`

Состояние объекта не является одним scalar status. Оно задаётся набором независимых размерностей:

`state(object,t) = {transport, acceptance, work, authority, membership, knowledge, ...}`

Каждое событие изменяет только ту `state_dimension`, изменение которой подтверждено source evidence и `decision_scope`.

## 2. Инвариант причинной связи

Parent/child relation допустим только при проверяемой evidence-связи.

Недостаточно:

- близости времени;
- похожих имён файлов;
- общего каталога;
- участия тех же Сущностей;
- общей темы;
- логически правдоподобной последовательности.

Нужен минимум один явный link:

`source_event_id`

или

`source_artifact + immutable version identity`, на который downstream source прямо ссылается.

Если link не доказан, отношение получает `UNPROVEN_LINK` и не участвует в causal metrics.

## 3. Identity-поля

### `event_id`

Уникальный идентификатор события в dataset/model.

### `event_type`

Нормализованный тип события. Кандидатные типы:

- `observation_recorded`;
- `blocker_observed`;
- `blocker_classified`;
- `decision_made`;
- `artifact_prepared`;
- `dispatch_recorded`;
- `addressed_pointer_created`;
- `receipt_recorded`;
- `acceptance_decision_made`;
- `result_verified`;
- `handover_started`;
- `handover_verified`;
- `recovery_package_prepared`;
- `recovery_readback_verified`;
- `recovery_attempted`;
- `recovery_result_verified`.

Список не считается закрытым taxonomy.

### `object_id`

Стабильный идентификатор объекта, состояние которого меняется или наблюдается.

Пример:

`exchange_object:KOD__activation-product-e2e-blocker__KOO`

или

`entity_recoverability:ent:VOL`.

### `process_id`

Обязательный универсальный идентификатор процесса.

Именно `process_id`, а не `experiment_id`, связывает события обычного delivery, review, recovery, handover, approval или другого процесса.

Примеры:

`file_exchange:KOD->KOO:activation-product-e2e-blocker`

`recovery:ent:VOL:current`

### `experiment_id`

Опциональное поле. Используется только когда процесс действительно является экспериментом или содержит отдельную экспериментальную ветвь.

Разные `experiment_id` нельзя автоматически объединять в одну lineage.

### `task_id`

Логический идентификатор задачи, если он явно существует в источнике. Если отсутствует, не придумывается.

### `actor_id`

Сущность или участник, создавший, исполнивший или подтвердивший событие.

## 4. Causal и provenance-поля

### `source_event_id`

Прямой parent-event, если доказан. Допустимые состояния:

- конкретный `event_id`;
- `null` для root observation;
- `unresolved` для известного downstream event с неразрешённым parent.

### `source_artifact`

Путь к источнику события.

### `source_commit`

Immutable commit identity источника. Без неё событие остаётся research-grade, если иная immutable identity не установлена.

### `source_blob`

Blob identity конкретного содержимого, когда доступна.

### `evidence_level`

Минимальный набор:

- `DIRECT` — событие прямо заявлено immutable source;
- `LINKED` — связь подтверждена downstream source, явно ссылающимся на upstream;
- `DERIVED` — значение получено из прямых событий по явному правилу;
- `DIRECT_CURRENT_NOT_METRIC_GRADE` — содержание прямо наблюдается на mutable/current source, но self immutable identity ещё не разрешена;
- `UNPROVEN` — аналитическая гипотеза; исключается из causal calculation.

## 5. State-поля

### `state_dimension`

Обязательная размерность состояния, к которой относится transition.

Кандидатные значения:

- `transport_state`;
- `acceptance_state`;
- `content_work_state`;
- `authority_state`;
- `membership_state`;
- `knowledge_state`;
- `recovery_structural_state`;
- `recovery_practical_state`;
- `verification_state`.

Это открытый controlled vocabulary. Новое значение требует определения смысла, а не свободной фантазии по ситуации.

### `status_before`

Состояние данной `state_dimension` до события, если доказано.

### `status_after`

Состояние данной `state_dimension` после события, если доказано.

### `decision_scope`

Явная граница изменения. Событие не должно менять состояние вне своего `decision_scope`.

### `result_class`

Грубая классификация результата. Кандидатный набор:

`PASS`, `FAIL`, `BLOCKED`, `AUTHORIZED`, `PREPARED`, `ROUTED`, `RECEIVED`, `ACCEPTED_BOUNDED`, `REJECTED`, `VERIFIED`, `UNKNOWN`.

`result_class` не заменяет `state_dimension + status_after`.

## 6. Branch и process topology

### `branch_status`

Кандидатные значения:

- `ROOT`;
- `CONTINUATION`;
- `FORK`;
- `MERGE_PROVEN`;
- `BRANCH_BOUNDARY`;
- `ROOT_FOR_VERIFIED_SUBSET`;
- `UNKNOWN`.

Fork считается доказанным, если новый process/experiment явно возникает из upstream decision или source relation.

Merge запрещено выводить только из сходства outcomes или общей темы. Нужна явная merge evidence.

## 7. Время

### `event_time`

Время underlying event, только если оно содержательно известно из разрешённого источника.

### `publication_time`

Время публикации/коммита source artifact, если доступно из GitHub metadata.

### `time_semantics`

Обязательная классификация:

- `event_time`;
- `artifact_publication_time`;
- `unknown`.

GitHub commit time нельзя автоматически использовать как время фактического действия, решения, получения или выполнения.

Для latency metric нужен event-specific start/end pair с одинаковой time semantics либо заранее определённым правилом преобразования.

## 8. Claim boundary

### `claim_boundary`

Обязательная краткая формулировка того, чего событие НЕ доказывает.

Примеры:

- dispatch не доказывает receipt;
- receipt не доказывает acceptance;
- acceptance документа не доказывает success underlying work;
- recovery package readiness не доказывает practical recoverability;
- наличие инструкции не доказывает autonomous capability нового исполнителя.

`claim_boundary` является частью anti-overclaim механизма, а не пояснительным украшением.

## 9. Metric-grade boundary

Событие допускается в metric-grade dataset только если:

1. `event_id` стабилен и уникален;
2. известны `object_id` и `process_id`;
3. задана `state_dimension`;
4. source имеет immutable self identity (`source_commit`, предпочтительно также `source_blob` для mutable path);
5. causal parent доказан либо явно `null/unresolved`;
6. `evidence_level != UNPROVEN`;
7. time semantics не смешаны;
8. задан `decision_scope` для решений/изменений;
9. зафиксирован `claim_boundary`.

Research-grade events могут быть полезны для исследования, но не должны незаметно попадать в вычисляемые показатели.

## 10. Правила валидации v0.2

1. `event_id` уникален.
2. `process_id` обязателен для каждого non-root dataset event.
3. `experiment_id` optional и не заменяет `process_id`.
4. `source_event_id`, если конкретен, должен существовать или быть явно external/unresolved.
5. Parent/child должны иметь совместимые `object_id`, либо downstream обязан явно описать translation/fork в `decision_scope`.
6. Разные `experiment_id` не сливаются автоматически.
7. Одно событие может содержать несколько state observations только как отдельные `state_dimension` transitions. Они не должны записываться одним scalar status.
8. Transport, acceptance и underlying work states считаются независимыми до доказанной связи.
9. `publication_time != event_time` по умолчанию.
10. `UNPROVEN` links и events исключаются из causal metrics.
11. Current mutable content без self immutable identity имеет максимум `DIRECT_CURRENT_NOT_METRIC_GRADE`.
12. `result_class=ACCEPTED*` не закрывает `content_work_state=BLOCKED/WAITING`, если отдельное evidence этого не доказывает.
13. Structural readiness и practical success должны жить в разных `state_dimension`, если проверяются разными событиями.

## 11. Что изменилось относительно v0.1

### Изменение 1: `process_id` стал обязательным универсальным уровнем

v0.1 использовал `experiment_id` как основной идентификатор ветви. File-exchange test показал, что это искусственно для неэкспериментальных процессов.

Теперь:

`object_id → process_id → optional experiment_id → event_id`.

### Изменение 2: введён `state_dimension`

v0.1 имел `status_before/status_after`, но не формально разделял независимые состояния.

Теперь каждый transition относится к конкретной размерности. Это предотвращает типовую ошибку:

`received/accepted artifact` → ошибочно трактуется как `underlying task solved`.

### Изменение 3: усилена research-grade / metric-grade граница

Current mutable evidence может использоваться в исследовании, но не должна участвовать в расчётах, пока не разрешена собственная immutable identity.

### Изменение 4: structural readiness отделена от practical recoverability

Это подготовка к третьему доменному тесту на recovery/preservation lifecycle.

## 12. Пример одного процесса в v0.2

Для file exchange:

`object_id = exchange_object:KOD__activation-product-e2e-blocker__KOO`

`process_id = file_exchange:KOD->KOO:activation-product-e2e-blocker`

События изменяют разные state dimensions:

- artifact prepared → `content_work_state`;
- dispatch → `transport_state`;
- receipt → `transport_state` + отдельное observation `acceptance_state=separate_decision_required`;
- bounded acceptance → `acceptance_state`;
- underlying blocker remains → `content_work_state=WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`.

Никакое из этих состояний не обязано перезаписывать остальные.

## 13. Следующая проверка

Третий доменный тест должен использовать recovery/preservation lifecycle и проверить минимум четыре независимые стадии:

`package prepared → structural/readback verification → addressed acceptance/preservation → practical recovery attempt/result`.

Проверяемый вопрос:

достаточно ли `process_id + state_dimension + provenance` для того, чтобы одновременно хранить истинные состояния `structurally ready` и `practical recoverability unknown/failed/passed` без противоречия.

Только после этого имеет смысл объявлять ядро контракта достаточно общим для первых process metrics.

---

Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: обобщить EVENT-CONTRACT после activation и file-exchange проверок и подготовить третий recovery/preservation test.
Статус: `candidate_research_contract`; не Project Source; не production schema; не ТЗ КОДЕРУ.
Метка времени: не ставилась; разрешённый проектный источник времени не использован.
