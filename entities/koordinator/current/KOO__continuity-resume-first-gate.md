# KOO: Resume-First Gate для непрерывности рабочего процесса

## Смысл

Существующая концепция Entity Continuity / Task Persistence правильно разделяет Entity ID, Task ID и Instance ID и фиксирует инвариант `FAILED INSTANCE != FAILED TASK`. Однако текущий опыт аварийной замены KOO выявил дополнительный operational gap: после успешного recovery новый instance способен восстановить роль и общие приоритеты, но ошибочно выбрать новую работу вместо продолжения незавершённой активной Task.

Нужен обязательный Resume-First Gate: после initiation/recovery Сущность не выбирает новую профильную задачу, пока не установлено состояние ранее активной Task и незавершённых внешних действий.

Статус документа: architectural_candidate. Это не новая approved норма.

## Требуемый порядок старта

После recovery/initiation:

`restore Entity identity → restore active Task register → restore last verified checkpoint → reconcile in-flight external effects → restore unfinished causal chain → validate writer/lease → resume same Task OR explicitly close/supersede it → only then select another Task`.

Ключевой принцип:

> Наличие успешно восстановленной Entity не означает, что восстановлена её незавершённая работа.

## Минимальный Task Continuity Checkpoint

Для каждой активной Task должен существовать компактный проверяемый checkpoint, достаточный новому instance для продолжения без догадки.

Минимальный состав:

- `entity_id`;
- `task_id`;
- `task_status`: минимум `ACTIVE | BLOCKED | DONE`;
- `current_goal`: что именно должно быть получено;
- `current_step`: последний незавершённый шаг;
- `last_verified_result`: последнее подтверждённое состояние;
- `in_flight_action`: действие, которое могло начаться, но post-condition ещё не подтверждён;
- `external_side_effects`: процессы, публикации, регистрации, оплаты, запущенные сервисы, незавершённые изменения и другие внешние последствия;
- `unknown_postconditions`: что после сбоя стало `unknown` и требует reconciliation;
- `next_admissible_action`: один следующий допустимый шаг при сохранении текущего evidence;
- `blocker` и адресат, если Task BLOCKED;
- `artifact_refs` / immutable locators;
- `predecessor_instance_id`;
- `writer_lease` / ownership evidence;
- `checkpoint_reason`: normal_step | blocker | credible_degradation | instance_handoff | pre-external-side-effect | post-external-side-effect.

Поля являются кандидатом минимальной схемы и не объявляются каноном.

## In-flight side-effect rule

Перед действием, которое меняет внешний мир, должен быть зафиксирован pre-action checkpoint с ожидаемым post-condition.

После действия должен быть зафиксирован один из результатов:

- `CONFIRMED`: post-condition независимо проверен;
- `FAILED`: действие доказанно не произошло;
- `UNKNOWN`: действие могло произойти, но подтверждения нет.

После crash/recovery состояние `UNKNOWN` запрещает слепой повтор. Сначала выполняется reconciliation внешнего состояния.

Это покрывает, например:

- signup/tenant creation;
- оплату или заказ;
- GitHub write;
- deployment/start/stop сервиса;
- изменение automation;
- выдачу/смену credentials или access;
- запуск долгого процесса;
- физически опасный или ресурсный контур, если он интегрирован с цифровым управлением.

## Resume decision

После восстановления checkpoint новый instance обязан принять одно из четырёх проверяемых решений:

1. `RESUME`: продолжить ту же Task ID с зафиксированного шага.
2. `RECONCILE`: сначала проверить внешнее состояние из-за unknown post-condition.
3. `BLOCKED`: сохранить Task активной и адресовать точный blocker.
4. `CLOSE/SUPERSEDE`: только при проверяемом DONE либо явном уполномоченном решении прекратить/заменить Task.

Переход к новой несвязанной Task при существующей ACTIVE/BLOCKED Task запрещён без отдельного решения о приоритете.

## Связь с текущими линиями проекта

### Entity Continuity

Документ расширяет существующую рабочую гипотезу:
`entities/koordinator/current/KOO__entity-continuity-architecture-note.md`.

Он не заменяет требование доказать real `processing_started`, но уточняет, что после запуска instance необходимо восстанавливать не только current-state вообще, а конкретный Task Continuity Checkpoint и unknown external side effects.

### Microsoft 365 / замена будильников

Внешний supervisor должен уметь не только инициировать instance, но и хранить/получать активный Task ID и checkpoint. Иначе внешний будильник лишь надёжнее разбудит Сущность, которая после пробуждения всё равно может начать не ту работу.

Поэтому E2E замены будильников следует проверять не как `event → wake`, а как:

`event → Entity identified → active Task found → checkpoint restored → unknown effects reconciled → same Task resumed → result verified → checkpoint advanced`.

## Практический пример текущего сбоя KOO

Перед аварийной заменой KOO активной линией была разработка внешнего supervisor и Microsoft 365 tenant/connector E2E. После recovery новый instance восстановил роль, emergency priorities и preservation state, но первоначально не восстановил семантическую связь Microsoft tenant diagnostic с задачей замены будильников.

Resume-First Gate должен был выявить незавершённую Task и вернуть новый instance к состоянию:
`M365 tenant/work-account state = unknown → reconcile tenant existence → connector E2E → evaluate supervisor candidate`,
а не позволить считать Microsoft отдельным второстепенным хвостом.

## Ближайший технический смысл

До появления real processing adapter схему можно использовать как формат checkpoint/handoff и anti-regression requirement.

После доказанного automatic `processing_started` ближайший E2E должен проверять не просто восстановление Task ID, а:

`kill instance with ACTIVE Task + unresolved in-flight checkpoint → new instance → same Task ID → checkpoint restore → reconciliation/resume → verified continuation`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать Resume-First Gate и Task Continuity Checkpoint как архитектурное дополнение к Entity Continuity
СТАТУС: architectural_candidate
source: verified current Entity Continuity artifacts + observed emergency KOO recovery failure mode
related_files: KOO__entity-continuity-architecture-note.md; entities/koder/current/concepts/automation/entity-continuity-task-persistence.md
approval_status: not_project_source
responsibility_boundary: не меняет approved canon; требует отдельного технического E2E и последующей профильной проверки
