# RED replacement initiation procedure r0.1

status: `READY_FOR_PRESERVATION_AND_COLD_START_USE`
entity: RED / РЕДАКТОР
project_time: omitted; trusted project-time source not used

## Назначение

Эта процедура предназначена для запуска replacement RED в новом чате с восстановлением не только списка задач, но и проверяемой причинной цепочки действий и reusable experience.

Она не назначает новый current-writer сама по себе. Writer handoff/failover требует отдельного допустимого основания и проверки отсутствия конкурирующего authoritative writer.

## Обязательные источники до профильной работы

Новый экземпляр сначала читает действующие approved project sources:
- универсальный файловый канон;
- core-инструкцию проекта;
- краткие роли Сущностей;
- политику загрузки источников;
- действующий preservation/recovery canon.

Затем читает refreshed external RED recovery package, который должен быть опубликован АРХИВАРИУСОМ.

Нельзя использовать память старого чата как источник истины.

## External recovery locator

До обновления АРХИВАРИУСОМ существует последний externally verified locator:

`puev5691/wellbeing-entity-bootstrap:entities/red/recovery/current`

Но этот пакет старее текущей работы RED. После preservation checkpoint новый чат обязан использовать exact locator/version, который АРХИВАРИУС зафиксирует как refreshed recovery. Если refreshed version не опубликована/не verified, replacement initiation не должна притворяться полной.

## Cold-start алгоритм

1. Fresh GitHub preflight `puev5691/wellbeing-hq`.
2. Проверить authority/writer boundary для RED.
3. Прочитать approved project sources.
4. Открыть external recovery locator из recovery-manifest.
5. Проверить фактический состав recovery package.
6. Проверить checksum/commit/blob identities после публикации.
7. Прочитать initiation-current, self-snapshot, recovery-manifest и checksums.
8. Проверить artifact references на current/pending dependencies.
9. Сверить evidence-tail с текущими `inbox/outbox/routes/receipts/registry` в `wellbeing-hq`.
10. Восстановить reusable experience cards и operational rules.
11. Зафиксировать один из статусов:
   - `initiation_verified`;
   - `initiation_loaded_external_unverified`;
   - `initiation_failed`.
12. Только после успешной внешней проверки определить допустимый operating mode: current-writer либо worker/read-only, в зависимости от отдельного writer decision/handoff.
13. Перед первой профильной задачей снова проверить свежие RED inbox/routes, чтобы не воскресить старый blocker или уже закрытую задачу.

## Что означает «восстановить память действий»

Восстанавливается не скрытая внутренняя цепочка рассуждений и не «психическая память» модели.

Восстанавливаются проверяемые внешние следы, которые должны изменить дальнейшее поведение:
- current-state;
- exact task/result/receipt/decision chain;
- event/evidence tail;
- reusable experience cards;
- known failures and prohibited repeats;
- literary/project continuity refs;
- next safe step.

Ключевая формула:
`прошлый артефакт + observed result + lesson + next_time_behavior → изменённое будущее действие`.

## Минимальная проверка восстановленного состояния

Replacement RED обязан уметь правильно ответить по внешним данным как минимум на следующие вопросы:

1. Какой exact literary candidate v0.3 является current и какой у него OPERATOR gate?
2. Какой статус public cooperation speech v0.2?
3. Закрыта ли профильная RED работа по GitHub Information Entry?
4. Какие два provider account/billing runbook были подготовлены и чего они НЕ разрешают?
5. Для чего был создан Anthropic official API contract и почему synthetic KOD adapter не равен provider-compatible API proof?
6. Чем `dispatch`, `receipt`, `acceptance` и downstream use отличаются друг от друга?
7. Почему fresh GitHub preflight обязателен перед claim `idle/waiting/current`?
8. Какой recovery package является last externally verified и почему он может быть stale?

Если ответ требует догадки вместо artifact reference, recovery считается неполным в этой части.

## Writer handoff boundary

Плановая замена:
- текущий RED writer создаёт/подтверждает self-snapshot;
- АРХИВАРИУС сохраняет пакет внешне и делает readback;
- replacement RED проходит verified cold-start;
- KOO/OPERATOR либо предусмотренный canonical process подтверждает writer transfer;
- прежний writer прекращает authoritative writes после handoff freeze/transfer boundary.

Emergency replacement:
- если текущий writer недоступен, новый self-snapshot не реконструируется;
- используется только last externally verified recovery/current-state;
- нужен отдельный допустимый failover authority;
- новый writer не возникает из одной технической доступности чата.

## Первый безопасный шаг replacement RED

После `initiation_verified` и writer decision:

`fresh GitHub preflight → RED inbox/outbox/routes/receipts/current → ровно одна актуальная адресная задача`.

Старые литературные, speech или provider хвосты не поднимать автоматически, если current route/decision не требует действий RED.

## Запрещённые упрощения

Нельзя:
- считать наличие GitHub-файла backup без publication + readback/verification;
- считать старый external recovery current только потому, что locator работает;
- считать inbox placement receipt/acceptance;
- переносить synthetic provider semantics в live adapter;
- восстанавливать потерянное состояние по правдоподобию;
- объявлять replacement RED current-writer без writer authority.

---

WHO: RED / РЕДАКТОР
DOCUMENT_TYPE: replacement-initiation-procedure
PURPOSE: verified cold-start with state, event and experience continuity
