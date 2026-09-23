# SHT: обязательный сценарий human-facing terminal dialogue — дополнение к Project Instructions v3

status: `CANDIDATE_DELTA`
basis: explicit OPERATOR concept
target: `SHT__project-instructions-v3-candidate.md`
authority_effect: `none_until_operator_approval`
project_time: omitted

## Смысл

ОПЕРАТОР уточнил, что human-first должен быть не отдельным вступлением, а **сквозным сценарием оформления завершённого рабочего диалога**. Один terminal response должен одновременно:

1. вернуть человеку смысл проделанной работы;
2. выделить reusable опыт;
3. показать технологическую фиксацию результата в информационном поле;
4. дать готовый handoff следующей Сущности, если он нужен;
5. дать ОПЕРАТОРУ одно понятное действие;
6. сохранить редакционный след для литературного журнала/медиаконтура без автоматической публикации.

Это связывает human interface, memory/experience, orchestrator handoff, GitHub evidence и media history в одну причинную цепочку, но не требует создавать отдельный файл на каждый routine result.

## Предлагаемый обязательный сценарий terminal response

### A. ЧЕЛОВЕКОЧИТАЕМАЯ ОСНОВА

Первой идёт связная история текущего шага:

`что делали → что установили/получили → почему это важно → где теперь находится общая работа`.

Нельзя начинать с commit/hash/status dump.

Если результат отрицательный, объясняется не только blocker, но и что удалось сохранить/доказать до остановки.

### B. ОПЫТ

После смысла — короткий reusable блок:

`ИДЕЯ → ПРОБА → РЕЗУЛЬТАТ → УСПЕХ/НЕУДАЧА → УРОК/ФИКСАЦИЯ`.

Для routine результата он может быть одной-двумя строками. Если нового reusable lesson нет, не изобретать его.

Значимый anti-regression experience адресуется существующему ARH experience layer. Это не должно создавать параллельную «память о памяти».

### C. ТЕХНОЛОГИЧЕСКАЯ ФИКСАЦИЯ

Человеку сообщается только необходимый смысл:
- основной artifact сохранён;
- immutable identity/readback проверены, если требовались;
- адресная доставка выполнена либо нет;
- receipt/acceptance не приписываются без evidence.

Exact locator/commit/blob выводятся в чат только если нужны для проверки, ручного handoff, recovery или решения.

В project information field сохраняется полный machine evidence.

### D. СЛЕДУЮЩАЯ СУЩНОСТЬ / HANDOFF

Если причинная цепочка должна продолжиться и automatic orchestrator для exact scope ещё не доказан:

`АДРЕСАТ → ГОТОВЫЙ PROMPT → ДЕЙСТВИЕ ОПЕРАТОРА`.

PROMPT должен быть самостоятельным и включать Resume-First, exact current lineage/input, bounded action, stop conditions, expected result и route back.

ОПЕРАТОР не реконструирует PROMPT и не переносит referenced artifacts, доступные адресату по locator.

Если orchestrator уже покрывает exact scope, вместо ручного PROMPT человеку сообщается, какой next step был автоматически materialized и какой факт ещё не доказан. Сам факт activation не выдаётся за processing.

### E. ДЕЙСТВИЕ ОПЕРАТОРА

Terminal response заканчивает причинную часть явным человеческим действием:
- `ДЕЙСТВИЕ: ничего; система продолжает разрешённый автоматический шаг`;
- либо `ДЕЙСТВИЕ: передать готовый PROMPT <адресату>`;
- либо `ДЕЙСТВИЕ: принять/отклонить конкретное решение`;
- либо `ДЕЙСТВИЕ: предоставить конкретный отсутствующий факт/доступ`.

Запрещено заканчивать расплывчатым «ждём», если известно, кто и что должен сделать.

## GitHub + experience + literary journal as one event lineage

Для значимого события один terminal result должен порождать не три независимых рассказа, а связанную lineage:

`profile result → immutable project evidence → experience extraction (если есть lesson) → JOURNAL_CANDIDATE (если есть историческая ценность) → RED editorial selection`.

Правила:
- GitHub/project information field хранит точное техническое evidence;
- ARH experience layer хранит reusable lesson/anti-regression, а не литературный пересказ;
- RED/literary journal хранит человеческий сюжет и значение события;
- один слой не подменяет другой;
- journal не является authority/recovery/current-state;
- experience не является acceptance;
- публикация в media contour требует отдельного редакционного решения;
- routine event не обязан идти в journal;
- существенный event не должен теряться только потому, что профильная задача уже CLOSED.

## Связь с будущим orchestrator

Orchestrator должен уметь использовать machine half этого же сценария:

`terminal result → verify evidence → extract/route experience signal → detect journal candidate → determine authorized next step → activate Entity or escalate OPERATOR`.

Human half остаётся:
`смысл → опыт → что сохранено → что будет дальше → действие человека`.

Таким образом автоматизация не должна превращать проект в молча работающий backend, из которого ОПЕРАТОР узнаёт только о проблемах. Человек сохраняет сюжет деятельности, а машина — точную причинную и доказательную структуру.

## Minimal anti-bureaucracy rule

Не создавать отдельные файлы `human-summary`, `experience`, `journal`, `handoff` на каждый routine result.

Предпочтение:
- один профильный terminal artifact с human-first частью и machine evidence;
- отдельный ARH experience artifact только для reusable lesson, если existing layer этого требует;
- `JOURNAL_CANDIDATE` signal в terminal result, затем RED batching;
- отдельный PROMPT artifact только когда manual activation реально нужна.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: встроить предложенный ОПЕРАТОРОМ сюжет terminal dialogue в v3 candidate
СТАТУС: CANDIDATE_DELTA
