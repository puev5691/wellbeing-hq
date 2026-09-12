# EVENT-CONTRACT для модели организационной динамики — v0.1

## Назначение

Этот документ фиксирует минимальный контракт события, достаточный для того, чтобы будущая модель могла собирать причинные цепочки без склеивания тематически похожих, но фактически разных процессов.

Основание для контракта — проверка реальной activation-lineage проекта. В ней обнаружились как минимум две связанные по теме, но разные экспериментальные ветви. Поэтому идентичность объекта и эксперимента становится обязательной частью события, а не декоративным metadata.

Это кандидатный исследовательский контракт. Он не является Project Source, схемой production-data и техническим заданием КОДЕРУ.

## 1. Инвариант причинной связи

Событие может считаться продолжением другого события только при наличии явной evidence-связи.

Запрещено выводить parent/child relation только из:

- близости времени;
- сходства названий файлов;
- общего каталога;
- участия тех же Сущностей;
- общей темы;
- человечески правдоподобной последовательности.

Минимум нужен один проверяемый link:

`source_event_id` или `source_artifact + immutable version identity` с явной ссылкой внутри downstream artifact.

Если такого link нет, отношение получает статус `UNPROVEN_LINK`, даже если аналитически выглядит очевидным.

## 2. Минимальная структура EVENT-CONTRACT-v0.1

### Обязательные identity-поля

`event_id`

Уникальный идентификатор события в пределах dataset/model.

`event_type`

Нормализованный тип события. Примеры: `blocker_observed`, `blocker_classified`, `decision_made`, `implementation_artifact_prepared`, `external_prerequisite_declared`, `external_prerequisite_routed`, `receipt_recorded`, `result_verified`.

`object_id`

Стабильный идентификатор объекта изменения. Например, `activation_exact_entity_start_resume`.

`experiment_id`

Идентификатор конкретного эксперимента/ветви. Обязателен, когда один объект исследуется несколькими параллельными ветвями.

`task_id`

Логический идентификатор задачи, если он существует в источнике. Если отсутствует, значение не придумывается.

`actor_id`

Сущность/участник, создавший или исполнивший наблюдаемое событие.

### Обязательные causal/provenance-поля

`source_event_id`

Прямой parent-event, если он доказан. Может быть `null`, если событие является root observation или если parent не доказан.

`source_artifact`

Путь к артефакту, из которого извлечено событие.

`source_commit`

Immutable commit identity. Если для события пока не извлечён, оно не считается пригодным для machine causal dataset.

`source_blob`

Blob identity конкретного содержимого, когда доступна. Для mutable paths blob предпочтителен.

`evidence_level`

Минимальные значения:

- `DIRECT` — событие прямо заявлено источником;
- `LINKED` — событие/связь подтверждена downstream-артефактом, который явно ссылается на upstream;
- `DERIVED` — значение вычислено из прямых событий по явному правилу;
- `UNPROVEN` — аналитическая гипотеза, не включаемая в causal calculation.

### Обязательные state-поля

`status_before`

Состояние объекта перед событием, если оно явно известно.

`status_after`

Состояние объекта после события, если оно явно известно.

`decision_scope`

Что именно изменяет событие. Нужен для запрета подмены одного уровня другим. Например, решение о `bounded new Work experiment` не меняет статус `exact-instance resume blocker`.

`result_class`

Примеры: `PASS`, `FAIL`, `BLOCKED`, `AUTHORIZED`, `PREPARED`, `ROUTED`, `UNKNOWN`.

### Временные поля

`event_time`

Время самого события, только если оно содержательно известно из разрешённого источника.

`publication_time`

Время публикации/коммита артефакта, если извлечено из GitHub metadata.

`time_semantics`

Обязательное пояснение: `event_time`, `artifact_publication_time`, `unknown`.

GitHub commit time нельзя автоматически трактовать как время возникновения underlying event.

### Поля границ и качества

`claim_boundary`

Короткая формулировка того, чего событие НЕ доказывает.

`branch_status`

`ROOT`, `CONTINUATION`, `FORK`, `MERGE_PROVEN`, `BRANCH_BOUNDARY`, `UNKNOWN`.

`normalization_notes`

Нужны только для спорных случаев, не как обязательная свалка человеческих комментариев.

## 3. Какие поля можно извлекать автоматически из GitHub

При наличии стандартной структуры репозитория потенциально автоматически извлекаются:

- `source_artifact`;
- `source_commit`;
- `source_blob`;
- `publication_time` из commit metadata;
- `actor_id` только если однозначно задан внутри файла или маршрута;
- часть `event_type` по стандартизованному document_type/status, но не по имени файла как единственному источнику;
- `recipient/sender` для dispatch-like объектов;
- immutable parent artifact, если downstream явно содержит path + commit/blob.

Автоматическое извлечение допустимо только при валидации структуры. Filename heuristics сами по себе недостаточны.

## 4. Какие поля должна задавать создающая Сущность или управляющий контур

Почти всегда вручную/явно должны задаваться:

- `object_id`;
- `experiment_id`;
- `task_id`, если task identity существует;
- `event_type`, если документ может содержать несколько разных событий;
- `source_event_id`;
- `decision_scope`;
- `status_before`;
- `status_after`;
- `claim_boundary`;
- смысл `event_time`.

Именно эти поля защищают от ложной причинности. GitHub не способен угадать их надёжно по одному расположению файла, потому что репозиторий, к счастью или несчастью, ещё не телепатический.

## 5. Прогон ветки A через контракт

Ветка A:

`SIS exact-instance blocker → SHT classification → KOO bounded alternative → KOD package`

### A-EVT-01

`event_id: A-EVT-01`
`event_type: blocker_observed`
`object_id: activation_exact_entity_start_resume`
`experiment_id: exact-instance-boundary-line`
`task_id: unknown`
`actor_id: SIS`
`source_event_id: null`
`source_artifact: entities/sisadmin/outbox/SIS__real-entity-activation-boundary__KOO.md`
`evidence_level: DIRECT`
`status_after: BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY`
`decision_scope: exact ChatGPT Entity start/resume interface`
`result_class: BLOCKED`
`branch_status: ROOT`
`claim_boundary: не доказывает отсутствие всех возможных product-side путей; фиксирует границу проверенного текущего runtime stack`

### A-EVT-02

`event_id: A-EVT-02`
`event_type: blocker_classified`
`object_id: activation_exact_entity_start_resume`
`experiment_id: exact-instance-boundary-line`
`actor_id: SHT`
`source_event_id: A-EVT-01`
`source_artifact: entities/shtabist/outbox/SHT__real-entity-activation-org-gate__KOO.md`
`evidence_level: LINKED`
`status_before: BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY`
`status_after: BLOCKED_ON_ENTITY_START_RESUME_INTERFACE`
`decision_scope: organizational classification and responsibility boundary`
`result_class: BLOCKED`
`branch_status: CONTINUATION`
`claim_boundary: classification is not acceptance of technical solution and not assignment by SHT of implementation authority`

### A-EVT-03

`event_id: A-EVT-03`
`event_type: decision_made`
`object_id: bounded_new_work_e2e`
`experiment_id: ent:KOD-E2E-WORK-01`
`task_id: task:activation-work-e2e-01`
`actor_id: KOO`
`source_event_id: null`
`source_artifact: entities/koordinator/outbox/KOO__activation-product-e2e-decision__KOD.md`
`evidence_level: DIRECT`
`status_after: BOUNDED_E2E_AUTHORIZED_FOR_PREPARATION`
`decision_scope: new Work processing context with verified recovery input`
`result_class: AUTHORIZED`
`branch_status: FORK`
`claim_boundary: exact-instance blocker remains; old Instance ID/resume/current-writer transfer not proven`

Почему `source_event_id: null`: artifact подтверждает decision и ссылается на feasibility-result KOD, а не прямо на A-EVT-02. Поэтому причинный parent A-EVT-02→A-EVT-03 нельзя назначать только по смысловой последовательности.

### A-EVT-04

`event_id: A-EVT-04`
`event_type: implementation_artifact_prepared`
`object_id: bounded_new_work_e2e`
`experiment_id: ent:KOD-E2E-WORK-01`
`task_id: task:activation-work-e2e-01`
`actor_id: KOD`
`source_event_id: A-EVT-03`
`source_artifact: entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md`
`evidence_level: LINKED`
`status_before: BOUNDED_E2E_AUTHORIZED_FOR_PREPARATION`
`status_after: READY_FOR_PRODUCT_SIDE_PR_TRIGGER_SETUP`
`decision_scope: repository-side package preparation`
`result_class: PREPARED`
`branch_status: CONTINUATION`
`claim_boundary: package readiness does not prove Work run, processing_started, delivery, receipt, acceptance or exact-instance resume`

### Результат ветки A

Контракт проходит. Главная неожиданность: A-EVT-03 является fork по объекту/эксперименту, а не простым продолжением exact-instance blocker. Это сохраняет сразу два истинных состояния:

- exact-instance линия остаётся blocked;
- bounded new-Work experiment одновременно может быть authorized/prepared.

Без `object_id + experiment_id + decision_scope` эти состояния конфликтовали бы или одно затёрло бы другое.

## 6. Прогон ветки B через контракт

Ветка B подтверждена лишь частично проверенным набором:

`SIS product-side preparation → KOO product blocker → OPERATOR prerequisite`.

Проверенный KOO artifact:

`entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`

содержит:

- `entity_test_id: ent:SIS-WORK-E2E-01`;
- `task_id: task:SIS-WORK-E2E-PR-01`;
- ссылку на `entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md`;
- статус `WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`.

### B-EVT-01

`event_id: B-EVT-01`
`event_type: external_prerequisite_routed`
`object_id: bounded_new_work_e2e`
`experiment_id: ent:SIS-WORK-E2E-01`
`task_id: task:SIS-WORK-E2E-PR-01`
`actor_id: KOO`
`source_event_id: unknown`
`source_artifact: entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`
`evidence_level: DIRECT`
`status_after: WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`
`decision_scope: creation/authorization of event-triggered Work task`
`result_class: ROUTED`
`branch_status: ROOT_FOR_VERIFIED_SUBSET`
`claim_boundary: не доказывает создание trigger/task и не доказывает связь с KOD experiment`

### Результат ветки B

Контракт не позволяет присвоить parent-event без отдельного чтения SIS preparation artifact и его immutable identity. Это правильный FAIL-CLOSED результат.

Ветка B не объединяется с веткой A, потому что:

`experiment_id(A) = ent:KOD-E2E-WORK-01`

`experiment_id(B) = ent:SIS-WORK-E2E-01`

Совпадение `object_id = bounded_new_work_e2e` означает общую область проблемы, но не общую lineage.

## 7. Машинно-полезные правила валидации

Для будущей модели кандидатные правила:

1. `event_id` уникален.
2. `source_event_id`, если задан, обязан существовать в dataset или быть явно external/unresolved.
3. Parent/child должны иметь совместимые `object_id`, либо downstream должен явно фиксировать `decision_scope` как fork/translation между объектами.
4. Разные `experiment_id` запрещено автоматически объединять в одну lineage.
5. `source_artifact` без immutable `source_commit/blob` достаточен для research draft, но недостаточен для metric-grade event.
6. `publication_time` нельзя использовать как `event_time` без `time_semantics`.
7. `UNPROVEN` события исключаются из causal metrics.
8. Одновременное существование статусов разных объектов допустимо: blocker одного объекта не отменяется PASS/PREPARED другого.
9. Любая `MERGE_PROVEN` должна иметь ссылки на обе/все входящие ветви.
10. Metric query должна указывать конкретные `object_id + event_type + time_semantics`, иначе результат считается неопределённым.

## 8. Что контракт меняет в будущей модели

До этого модель могла выглядеть как единый event log. Теперь точнее говорить о графе событий и состояний:

`objects + experiments + events + explicit causal links + state transitions`.

То есть базовая структура будущего движка должна быть ближе к provenance-aware event graph, чем к линейному журналу.

Это поддерживает более честную реконструкцию:

- fork;
- параллельные эксперименты;
- unresolved dependencies;
- разные уровни состояния;
- доказанный merge;
- сохранение одновременно действующих blocker и альтернативной ветви.

## 9. Что пока не решено

Контракт v0.1 ещё не определяет:

- глобальный формат ID;
- JSON Schema;
- словарь всех `event_type`;
- типизацию object/experiment/task relationship;
- правила version supersession event;
- precise time-source policy для metric datasets;
- access/privacy layer;
- автоматический extractor;
- validator implementation.

Эти пункты не надо отдавать КОДЕРУ до завершения исследовательского минимума.

## 10. Следующий исследовательский цикл

Следующий шаг должен проверить контракт на другом типе процесса, не activation. Наиболее полезный кандидат — file exchange / dispatch / receipt / acceptance, потому что там уже существуют формальные состояния `prepared → dispatched → received → accepted/rejected`.

Если тот же contract без насилия описывает transport lifecycle, можно будет отделить универсальное ядро event graph от domain-specific полей.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: зафиксировать минимальный EVENT-CONTRACT-v0.1 и проверить его на двух activation-ветвях без ложного склеивания причинных цепочек.
Статус: `candidate_research_artifact`; не Project Source; не production schema; не ТЗ КОДЕРУ.
Метка времени: не ставилась; разрешённый проектный источник времени не использован.
