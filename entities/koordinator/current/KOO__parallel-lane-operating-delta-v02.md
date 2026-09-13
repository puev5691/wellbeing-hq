# KOO — parallel-lane operating delta v0.2

status: ACTIVE_WORKING_DIRECTIVE
canon: no
supersedes_for_current_scheduling: `entities/koordinator/current/KOO__parallel-lane-operating-delta-v01.md`
production_mutation: no
automation_change: no
project_time: omitted; trusted project-time source not used

## Базовая модель

Сохраняется принятая рабочая схема:

`BUILD CONFLICT GRAPH → SELECT SAFE READY_PARALLEL SET → PRIORITIZE/AGE → DISPATCH EXACT LANES → RECONCILE RETURNS`.

Inbox placement или activation request не доказывают `RUNNING`.

Operational states:
`READY_PARALLEL`, `RUNNING`, `WAITING_EXTERNAL`, `WAITING_ENTITY`, `WAITING_OPERATOR`, `CONFLICT`, `CLOSED`.

## Изменение относительно v0.1: SHD

Специальное состояние
`excluded_operator_direct_control`
больше не является текущим для SHD.

Основание: новое явное решение ОПЕРАТОРА вернуть ШАРДОВИКА под управление KOO.

Текущий SHD state задаётся отдельной карточкой:
`entities/koordinator/current/KOO__shd-control-return-v01.md`.

На текущей границе:
- `control_owner: KOO`;
- `queue_participation: adaptive`;
- `scheduler_eligible: false`;
- `state: WAITING_OPERATOR` только потому, что ОПЕРАТОР завершает настройку и формирует exact направление по запуску криптоплатформы.

После получения этого exact handoff SHD участвует в обычном conflict-checked adaptive scheduling наравне с другими профильными Сущностями.

## Anti-regression

- возврат управления не равен немедленному запуску старой SHD задачи;
- не активировать старые WBN/WBNP/TERA2 хвосты без reconciliation;
- не считать старый `lab-01` план доказательством текущей готовности МАЖОРА;
- не дублировать настройку, пока ОПЕРАТОР явно не сообщил о её завершении;
- после exact handoff выполнить fresh preflight и выбрать один проверяемый SHD next action.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: убрать устаревшее special exclusion SHD после решения ОПЕРАТОРА
СТАТУС: active_working_directive
