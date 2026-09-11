# Нормализация activation-lineage в события — v0.1

## Назначение

Этот проход проверяет, можно ли превратить реальную цепочку проектных артефактов в нормализованный event set без додумывания отсутствующих переходов.

Проверяемая гипотеза была простой:

`SIS blocker → SHT classification → KOO decision → KOD package → OPERATOR product blocker`

Проверка показала, что эта последовательность **не является одной линейной lineage**. После KOO решения фактически существуют как минимум две связанные, но различающиеся ветви bounded Work E2E. Это критический результат: построение модели по близости тематики или времени коммитов создало бы ложную причинную цепь.

Статусы событий ниже:

- `OBSERVED` — прямо подтверждено содержанием артефакта;
- `DERIVED_LINK` — связь подтверждается явной ссылкой на предыдущий артефакт/статус;
- `NOT_PROVEN` — логичная, но документально не подтвержденная связь;
- `BRANCH_BOUNDARY` — место, где нельзя склеивать события в одну цепь.

## Объекты

### Общая проблема

`object_id_candidate: activation_exact_entity_start_resume`

Смысл: переход от проверенного GitHub activation event / worker orchestration к независимо проверяемому запуску exact ChatGPT Entity processing instance.

### Ветка A — exact-instance boundary → KOD bounded new-Work experiment

`experiment_id_candidate: ent:KOD-E2E-WORK-01 / task:activation-work-e2e-01`

Acceptance target:

`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`

Эта ветка **не** доказывает resume существующей Entity instance.

### Ветка B — SIS product-trigger prerequisite

`experiment_id_candidate: ent:SIS-WORK-E2E-01 / task:SIS-WORK-E2E-PR-01`

Статус у KOO:

`WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`

Эта ветка использует отдельный SIS preparation artifact и отдельный recovery input.

## Нормализованные события

### EVT-01 — runtime boundary observed

`event_type: blocker_observed`
`actor: SIS`
`object: activation_exact_entity_start_resume`
`status: OBSERVED`

Evidence:
`entities/sisadmin/outbox/SIS__real-entity-activation-boundary__KOO.md`

Observed state:

`GitHub event → detector/activation worker → local worker state + handler process`

не доказал переход к:

`exact ChatGPT Entity profile-processing instance`.

Ключевой blocker:

`BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY`.

Это событие допустимо использовать как `signal_observed` для отдельного класса решений **только если** event contract заранее определит именно publication/verification этого blocker как начало отсчета. Сам момент фактического возникновения технической невозможности из этого артефакта не восстанавливается.

### EVT-02 — organizational boundary classified

`event_type: blocker_classified`
`actor: SHT`
`object: activation_exact_entity_start_resume`
`status: DERIVED_LINK`
`source_event: EVT-01`

Evidence:
`entities/shtabist/outbox/SHT__real-entity-activation-org-gate__KOO.md`

SHT прямо ссылается на SIS result и классифицирует его как:

`BLOCKED_ON_ENTITY_START_RESUME_INTERFACE`.

Дополнительно разделены полномочия:
KOO выбирает путь/acceptance boundary; implementation Entity готовит adapter/interface; SIS возвращается только после появления принятого runtime interface/package; SHT контролирует сквозную целостность.

### EVT-03 — bounded alternative path authorized

`event_type: decision_made`
`actor: KOO`
`object: bounded_new_work_e2e`
`status: OBSERVED`

Evidence:
`entities/koordinator/outbox/KOO__activation-product-e2e-decision__KOD.md`

KOO не снимает exact-instance blocker. Вместо этого разрешает ограниченный эксперимент с новым Work processing context:

`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`.

Статус решения:

`BOUNDED_E2E_AUTHORIZED_FOR_PREPARATION`.

Это важное изменение типа объекта. EVT-03 не является решением `exact resume achieved`; это решение **обойти недоказанный exact-instance transition через новый ограниченный эксперимент**, сохранив blocker исходной линии.

### EVT-04 — KOD package prepared

`event_type: implementation_artifact_prepared`
`actor: KOD`
`object: ent:KOD-E2E-WORK-01 / task:activation-work-e2e-01`
`status: DERIVED_LINK`
`source_event: EVT-03`

Evidence:
`entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md`

Status:
`READY_FOR_PRODUCT_SIDE_PR_TRIGGER_SETUP`.

Package fixes:
- fresh new Instance ID required;
- immutable artifact/recovery/current-state locators;
- fail-closed provenance verification;
- no exact-instance resume claim;
- no writer-authority expansion;
- no E2E PASS before actual product-side run.

Следующее внешнее prerequisite в этом артефакте: создать/включить GitHub PR-triggered Work task и провести controlled PR event.

### EVT-05A — product prerequisite routed to OPERATOR for SIS experiment

`event_type: external_prerequisite_routed`
`actor: KOO`
`object: ent:SIS-WORK-E2E-01 / task:SIS-WORK-E2E-PR-01`
`status: BRANCH_BOUNDARY`

Evidence:
`entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`

Status:
`WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`.

Но этот artifact **не ссылается на KOD package EVT-04 как immutable basis**. Он ссылается на другой SIS artifact:

`entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md`

и использует другой test identity:

- `ent:SIS-WORK-E2E-01`;
- `task:SIS-WORK-E2E-PR-01`.

Следовательно, склеивать EVT-04 и EVT-05A в одну строгую lineage нельзя.

### EVT-05B — внешний prerequisite из KOD package

`event_type: external_prerequisite_declared`
`actor: KOD`
`object: ent:KOD-E2E-WORK-01 / task:activation-work-e2e-01`
`status: OBSERVED`

Evidence находится внутри EVT-04 artifact.

Required product-side prerequisite: capable actor creates/enables GitHub PR-triggered Work task for `puev5691/wellbeing-hq`, затем выполняет controlled PR event и возвращает Work-run evidence.

В проверенном наборе артефактов отдельный KOO→OPERATOR routing artifact именно для `ent:KOD-E2E-WORK-01` не подтвержден.

## Что удалось восстановить

Для ветки A честно восстанавливается:

`runtime blocker observed → organizational blocker classified → bounded alternative authorized → repository-side package prepared → product prerequisite declared`.

Для ветки B честно восстанавливается отдельная цепь:

`SIS product-side preparation → KOO blocker accepted → product-trigger prerequisite routed to OPERATOR`.

Связь между A и B на уровне общей архитектурной проблемы очевидна, но exact parent/child relation между KOD package и SIS/OPERATOR blocker **не подтверждена**.

## Проверка event contract

Минимальный event contract должен иметь не только `event_type`, `actor`, `timestamp`, но и обязательные identity-поля:

`event_id`
`object_id`
`experiment_id`
`task_id`
`source_event_id`
`source_artifact`
`source_commit/blob`
`decision_scope`
`status_before`
`status_after`
`evidence_level`

Без `object_id/experiment_id/source_event_id` тематически похожие ветви легко склеиваются в ложную lineage.

## Первая реально вычислимая метрика

### artifact_decision_to_package_latency — только proxy

Для ветки A потенциально вычислим интервал:

`KOO bounded authorization artifact publication → KOD package publication`.

Но на текущем этапе я **не вычисляю число**, потому что метрика `decision_latency` была определена как:

`t(decision_made) - t(signal_observed)`.

EVT-03→EVT-04 измеряет уже другое: `decision_to_prepared_artifact_latency`.

Это может стать отдельной операционной метрикой после утверждения event semantics, но подменять ею `decision_latency` нельзя.

### Что уже можно утверждать

- `blocker_classification_exists = true` для EVT-01→EVT-02;
- `bounded_alternative_decision_exists = true` для EVT-03;
- `repository_package_prepared = true` для EVT-04;
- `product_side_prerequisite_unresolved = true` по проверенным artifacts;
- `exact_instance_resume_verified = false/not proven`;
- `full_event_lineage_single_chain = false`.

## Главный результат цикла

Первый реальный normalization pass выявил не отсутствие данных, а **проблему идентичности процесса**.

GitHub уже хорошо хранит immutable artifacts. Но без стабильных `object_id`, `experiment_id` и явных parent-event links можно построить очень убедительную и совершенно ложную историю просто потому, что несколько Сущностей одновременно работают над похожей activation-проблемой.

Для будущего движка это anti-regression requirement:

> Никакое событие не включается в causal lineage только по совпадению темы, пути каталога, близости времени или человечески понятной последовательности. Нужна явная identity/link evidence.

## Следующий цикл

1. определить минимальный `EVENT-CONTRACT-v0.1` с обязательными identity/provenance полями;
2. прогнать через него обе activation-ветви;
3. проверить, какие поля можно заполнять автоматически из GitHub, а какие должны быть заданы создающей Сущностью;
4. только после этого считать временные и routing metrics.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: нормализовать реальную activation-lineage проекта в события и проверить пригодность event contract будущей модели организационной динамики.
Статус: `candidate_research_artifact`; не Project Source; не ТЗ КОДЕРУ.
Метка времени: не ставилась; разрешённый проектный источник времени не использован.
