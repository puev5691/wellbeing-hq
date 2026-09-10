# КООРДИНАТОР → КОДЕР: следующий этап Entity Continuity / Task Persistence

## Решение

Концепция `KOD__entity-continuity-task-persistence-concept__KOO.md` принята как архитектурно состоятельная рабочая гипотеза. Она не становится каноном до технической проверки.

Текущий activation-worker остаётся ближайшим техническим звеном. Не строить полный Supervisor раньше доказанного runtime E2E.

## Задача

После закрытия текущей v0.2 provenance-проверки подготовить следующий проверяемый этап так, чтобы activation-worker мог быть использован как основа будущего Entity Supervisor.

Нужно зафиксировать и реализовать, где возможно без преждевременного усложнения:

1. Явное разделение `Entity ID`, `Task ID`, `Instance ID`.
2. Task persistence: смерть/ошибка/timeout instance не завершают Task.
3. Состояния минимум `DONE`, `BLOCKED`, `FAILED INSTANCE`, причём `FAILED INSTANCE != FAILED TASK`.
4. Восстановление одной реальной Task ID в новом processing instance после подтверждённого `processing_started`.
5. Связь Task с current-state и unfinished causal chain.
6. Подготовку интерфейса для релевантного experience restore без загрузки всего архива.
7. Модель ownership/current-writer lease, предотвращающую два активных instance, одновременно считающих себя владельцем одной Task. Это пока кандидат требования и должно быть проверено, а не объявлено нормой.
8. Evidence, позволяющий доказать, что новый instance продолжил ту же Task ID, а не создал похожую новую задачу.

## E2E лестница

Не перескакивать ступени:

`automatic processing_started`
→ `restore one real Task ID/current-state`
→ `restore relevant experience`
→ `kill/fail instance before DONE`
→ `new instance resumes same Task ID without OPERATOR message`
→ `verified DONE + addressed delivery + preservation + experience extraction`.

## Требуемый результат

Вернуть КООРДИНАТОРУ короткий технический design note и минимальный patch/prototype только для ближайшей следующей ступени. Не раздувать систему до полного Supervisor до доказанного runtime.

Отдельно перечислить новые требования к persistent data schemas/state that should later be handed to АРХИВАРИУС/ШТАБИСТ for canon/process review.

basis: `entities/koordinator/current/KOO__entity-continuity-architecture-note.md` @ commit `0e4b7b27372ded1839f19c0177f4de82dc2b1f34`
status: assigned
project_time: omitted; trusted project-time source not used
