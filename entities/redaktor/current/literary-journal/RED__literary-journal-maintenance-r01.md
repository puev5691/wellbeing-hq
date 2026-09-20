# RED literary journal maintenance r0.1

status: `ACTIVE_RED_INTERNAL_EDITORIAL_GUIDELINE`
project_source: `no`
authority_expansion: `none`
automation: `none`
project_time: omitted; trusted project-time source not used

## Назначение

Сделать уже активированный литературный журнал реально живым без превращения его в per-task log.

Основной журнал:
`entities/redaktor/current/literary-journal/RED__project-literary-journal.md`.

## Правило RED Resume-First

При каждом новом Resume-First цикле RED, **после выполнения основной профильной задачи или при отсутствии другой более приоритетной RED-задачи**, делает лёгкую journal-delta проверку:

1. смотрит, появились ли после последней journal-check точки очевидно значимые события;
2. не пересматривает весь архив;
3. если значимых событий нет — журнал не меняется;
4. если есть — добавляет обычно 1–3 записи одним bounded update;
5. exact evidence проверяется до записи фактического утверждения;
6. литературный смысл не подменяет technical truth.

Journal maintenance не должен задерживать основную задачу и не является отдельным обязательным отчётом после каждого terminal result.

## Что считать значимым

Событие является journal-worthy, если оно:
- изменило архитектуру, правило или направление;
- выявило серьёзный дефект/ложное предположение и породило урок;
- завершило первый реальный/публичный/production-like рубеж;
- открыло новый крупный контур;
- создало новую устойчивую практику взаимодействия человека и Сущностей;
- содержит человеческий контекст, который невозможно восстановить из machine evidence;
- имеет очевидную ценность для будущей истории, Telegram, портала или книги.

Обычный PASS, routine task, refactor, route/receipt и повторяющееся действие сами по себе недостаточны.

## Последняя проверенная точка

Initial journal activation:
- journal commit `f8029d9a7847244a7fb6190331a8541fcea26398`;
- journal blob `100fe794309b82d485f48bd786b623516e9cbff3`.

Последний завершённый journal-delta review:
`4d86f2b20db6d19f63ebf0ca737b3611031f2249`.

В этом review журнал получил post-seed update commit `5f0cb60ae8202ef0293f2cc10936e39b7e1a3720`.

Следующая journal-delta проверка должна начинаться после `4d86f2b20db6d19f63ebf0ca737b3611031f2249`, а не перечитывать всю историю.

## Входящие сигналы

Если KOO или другая Сущность адресно передаёт RED отметку `JOURNAL_CANDIDATE` с exact evidence, RED рассматривает её как вход для редакторского отбора, но не обязан автоматически включать запись.

Signal ≠ journal entry.
RED сохраняет право:
- объединить несколько сигналов в один сюжет;
- отложить недостаточно значимое;
- отклонить дубль;
- запросить evidence, если фактическая основа не доказана.

## Continuity

Следующий RED preservation/recovery snapshot должен сохранять:
- locator основного журнала;
- locator этой guideline;
- last journal-check point;
- незавершённые JOURNAL_CANDIDATE refs, если они есть.

---
WHO: RED / РЕДАКТОР
PURPOSE: lightweight maintenance mechanism for active literary journal
