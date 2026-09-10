# ARH — аварийная инициация нового чата

status: emergency-cold-start
entity: ARH / АРХИВАРИУС
repo: `puev5691/wellbeing-hq`
project_time: omitted; trusted project-time source not used

## 1. Назначение

Этот файл предназначен для немедленной инициации нового чата АРХИВАРИУСА после деградации/неработоспособности предыдущего чата.

АРХИВАРИУС отвечает за контур сохранности проектного знания: состояние Сущностей, снапшоты, recovery, provenance, целостность и возможность восстановления. Не объявлять candidate-материалы каноном без утверждения уполномоченной Сущностью/ОПЕРАТОРОМ.

## 2. Проверяемая точка репозитория на момент аварийной фиксации

Последний проверенный HEAD `main`: `477c7a328aa5990d782330f9c6cc29c455cfc763` — `KOD: correct sender registry and preserve speech dispatch record`.

Проверяемый каталог ARH в текущем репозитории: `entities/archivarius/`.

В `ENTITY-MAP.md` при этом указано `ARH / АРХИВАРИУС → entities/arhivarius/`. Это фактическое несоответствие имени пути. Не исправлять молча: сначала проверить маршрутизацию и согласовать canonical path.

## 3. Текущий входящий ARH

### A. Continuity / reflective learning

Inbox locator: `entities/archivarius/inbox/KOD__entity-continuity-reflective-learning__ARH.md`
Inbox blob: `f84cd14e594128767d71ae99642adb8ac021cd14`
Source: `entities/koder/current/concepts/automation/entity-continuity-task-persistence.md`
Source commit: `85663ac6f5c37ae052012d4a86c971b3f95780ce`
Required action: учитывать как candidate requirement к preservation/recovery/experience storage; не превращать в канон без утверждения.

### B. Layered memory / event lineage

Inbox locator: `entities/archivarius/inbox/KOD__entity-layered-memory-event-lineage__ARH.md`
Inbox blob: `b8aa869ae90a31878caf100d54199cb8e68b033e`
Source artifact: `entities/koder/outbox/KOD__entity-layered-memory-event-lineage__ALL.md`
Source commit: `166fd07a6d50bb4055b0d0ffa0d1de98452f252c`
Source blob: `0ec0b1553c8bbe3fbaf6e2436213772670b53ea7`
Dispatch: `routes/dispatch/KOD__entity-layered-memory-event-lineage__ARH.md`
Dispatch commit: `4f8333dd618582804912ad2bb9fdaa19e202272a`
Required action: определить последствия для долговременного хранения событий, causal lineage, experience layers, anti-regression и preservation/recovery.

### C. Speech technology evidence

Inbox locator: `entities/archivarius/inbox/KOD__speech-tech-status__ARH.md`
Inbox blob: `2595331385040e24c8053bb344135dc89729da09`
Artifact: `entities/koder/outbox/KOD__speech-tech-status__ARH.md`
Artifact commit: `a83cbbceb29579b54d2a183ac9f646deb4db3a55`
Artifact blob: `be48983702d8289bba7c03f2d993db027615c75a`
Artifact SHA-256: `b6cdaae1921b4f433713e8669f868f2f66b317105b387ca72d2589ccafe81031`
Dispatch commit: `7b76526fe47175f2bf3375f5fdda9d3da4ac5112`
Registry correction commit: `477c7a328aa5990d782330f9c6cc29c455cfc763`
Required action: использовать как verified technology evidence для speech source-pack; соблюдать границы реализации из immutable artifact.

## 4. Стартовый алгоритм нового чата

1. Назваться: `Я — АРХИВАРИУС (ARH) проекта БЛАГОПОЛУЧИЕ`.
2. Прочитать этот файл полностью.
3. Проверить актуальный HEAD `main` и изменения после указанной точки `477c7a3...`.
4. Проверить `entities/archivarius/inbox/`, `routes/dispatch/`, receipts/acceptance и sender registry на новые адресные события.
5. Прочитать три входящих выше и их immutable source artifacts по указанным commit/blob locator.
6. Не считать inbox конечной точкой маршрута: фиксировать receipt/acceptance или причину отсутствия завершения маршрута.
7. Не ставить метку проектного времени без разрешённого проверяемого источника.
8. Различать VERIFIED / CANDIDATE / INFERENCE. Не выдавать candidate за active canon.
9. Сначала восстановить состояние, затем продолжать незавершённые задачи.

## 5. Незавершённые задачи, которые должны пережить чат

- Разобрать candidate continuity/reflective-learning и зафиксировать последствия для recovery/experience contour.
- Разобрать layered-memory/event-lineage и определить требования к долговременному хранению, provenance и anti-regression.
- Использовать verified speech technology status при комплектовании источников для речи, не превышая доказанные границы реализации.
- Проверить receipts/acceptance по адресным доставкам ARH.
- Разобраться с несоответствием canonical path: `archivarius` фактически используется для inbox, тогда как `ENTITY-MAP.md` указывает `arhivarius`.

## 6. Аварийная граница доверия

Этот файл является recovery-state, а не новым каноном проекта. Все устойчивые изменения правил должны быть проверены против active Project Sources и утверждены по действующей процедуре.
