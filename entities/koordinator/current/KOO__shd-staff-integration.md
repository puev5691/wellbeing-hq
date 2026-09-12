# KOO: интеграция SHD / ШАРДОВИКА в штат ШТАБА

status: SELF_REPORT_RECEIVED_REVIEW_IN_PROGRESS

## Решение ОПЕРАТОРА

ОПЕРАТОР принял решение:
- сохранить существующую Сущность ШАРДОВИКА;
- переместить её в организационный контур ШТАБА;
- оформить ШАРДОВИКА как сотрудника ШТАБА;
- после профильного доклада ШАРДОВИКА внести его в необходимые реестры и действующие источники;
- детально определить обязанности, возможности и границы роли на основании подтверждённого доклада и действующих approved Project Sources.

Это решение не создаёт вторую Сущность и не меняет существующую identity/path.

## Уже проверено

GitHub repository: `puev5691/wellbeing-hq`.

Существующая identity:
- рабочий код: `SHD` уже используется в commits, dispatch и artifact names;
- имя: `ШАРДОВИК`;
- entity path: `entities/shardovik/`;
- sender registry: `registry/by-sender/shardovik.jsonl`;
- текущая карта `ENTITY-MAP.md` содержит `ШАРДОВИК → entities/shardovik/`, но ещё не фиксирует код `SHD`;
- существуют реальные outbox/dispatch/inbox обмены SHD с SIS и ARH.

## Self-report получен

artifact: `entities/shardovik/outbox/SHD__staff-functions-repo-focus__KOO.md`
artifact_commit: `1999e0b45b9e05b6aaf1fb99cab349509c53bc56`
artifact_blob: `cca580d35d475402ee7ec4f12df18cd15a7bb3d9`
inbox_pointer_commit: `0c66bc845d16de07163c1140675a618ddb26f6ea`
receipt_commit: `3c1a65cd5d0fa33451dc2ab66f4f08e171ab5a76`

Self-report содержит:
- фактически выполняемые функции;
- предметные области;
- capabilities и ограничения;
- файловую/GitHub/маршрутную дисциплину;
- secret boundary;
- типовые задачи и взаимодействия;
- разграничение capability и authority;
- заявленный repo focus;
- предложения по registry/experience/recovery.

Registration profile принят как достаточный вход для следующей стадии проверки, но НЕ как approved role source и НЕ как автоматическое расширение полномочий.

## Текущий exact dependency

Перед нормативным изменением роли KOO должен независимо сверить self-report с действующими approved Project Sources, прежде всего базовым role source, и отделить:
1. уже существующие обязанности;
2. фактически доказанные routine capabilities;
3. допустимый standing delegation без high-impact authority;
4. предложения, требующие отдельного решения ОПЕРАТОРА;
5. пункты, которые должны остаться только experience/operational guidance.

До этой сверки:
- `ENTITY-MAP.md` не изменяется;
- approved role source не изменяется;
- отдельный `registry/staff/` не создаётся;
- новые standing delegation / writer grants не выдаются;
- high-impact authority не расширяется.

## Следующий допустимый шаг KOO

Найти и independently readback действующий approved role source для SHD, сопоставить его с immutable self-report и подготовить bounded role-delta decision. Только после этого допустимы изменения ENTITY-MAP/current role source/recovery и preservation review ARH.

## Anti-regression

- receipt != approval;
- capability != authority;
- existing entity revision != new entity creation;
- factual GitHub activity != standing delegation;
- self-report candidate != Project Source;
- historical SHD results не переписываются новой ролью.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать снятие blocker `waiting_for_shd_self_report` и перейти к независимой нормативной сверке без преждевременного расширения полномочий
СТАТУС: self_report_received_review_in_progress
