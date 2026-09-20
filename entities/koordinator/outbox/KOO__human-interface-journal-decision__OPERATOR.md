# KOO → OPERATOR: human interface + literary journal decision packet

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Что произошло

KAN подготовил два кандидата:

1. human-interface norm для successor `project-instructions-core-v2_4`;
2. отдельное предложение литературного журнала проекта.

RED проверил оба:
`PASS_RED_HUMAN_INTERFACE_AND_JOURNAL_REVIEW_R01`.

Critical edits:
none.

Project Sources mutations:
0.

## Что это означает

Содержательная разработка завершена.
Новые KAN/RED циклы не требуются.

Нужно одно решение ОПЕРАТОРА, после которого KOO сможет:
- материализовать exact `project-instructions-core-v2_4-approved.md`;
- подготовить готовый Markdown-файл для одной Project Sources замены;
- отдельно открыть bounded RED implementation task на литературный журнал как профильный редакторский рабочий источник, не как baseline Project Source.

## Exact human-interface norm to approve

В current core v2.3 после раздела `## Минимальный документооборот` и перед `## Доставка артефактов` добавить:

### Человекочитаемый интерфейс проекта

Материал, предназначенный ОПЕРАТОРУ или иному человеку, сначала кратко и нормальным русским языком сообщает:

`что произошло → что это означает → что теперь возможно, разрешено или требуется`.

В основном human-facing тексте используется общеупотребительная лексика; инженерные и иные профильные термины применяются там, где они нужны по смыслу.

Paths, hashes, commits, blobs, locators, machine statuses, route history и подробный provenance по умолчанию остаются в информационном поле и не повторяются в human-facing ответе без практической необходимости.

Если точные технические данные нужны человеку для понимания, решения, действия, диагностики, безопасности, recovery или handoff, они приводятся полностью и без смыслового упрощения. Source code, commands, config, logs, protocol fields, identifiers и exact values сохраняются буквально там, где literal form нужна для корректности.

Machine-readable evidence сохраняется в информационном поле и остаётся доступным Сущностям, программам и последующей проверке, даже если оно не показано в текущем human-facing ответе.

Это правило не требует отдельной «человекочитаемой копии» артефакта. Если один результат может одновременно содержать понятное объяснение и необходимые exact machine fields, используется один результат. Pure machine-consumed code, config, logs и protocol data не требуют русского пояснения.

## Exact journal proposal to approve for implementation design

Литературный журнал проекта:

- не является техническим логом;
- не является full transcript;
- не является authoritative current-state;
- не является Project Source;
- не создаётся по каждой задаче;
- пополняется эпизодически/периодически по значимым событиям;
- сохраняет события, решения, причины, поворотные моменты, ошибки, открытия, характерные реплики, смешные эпизоды и человеческий контекст;
- machine evidence связывается locator-ом только при необходимости;
- будущий основной владелец: RED в рамках уже существующей роли;
- отдельное изменение entity roles не требуется;
- публикация в Telegram/портал/книгу остаётся отдельной редакторской/publication задачей.

Это решение НЕ активирует журнал.
Оно только разрешает KOO после core-materialization дать RED одну bounded implementation-design задачу:
- предложить минимальный storage/layout;
- предложить формат одной записи;
- предложить простой режим пополнения;
- не вводить automation/cron/per-task bureaucracy;
- вернуть candidate implementation package для отдельного OPERATOR activation decision.

## Единственное решение

Decision text:

`APPROVE_HUMAN_INTERFACE_CORE_V24_AND_JOURNAL_IMPLEMENTATION_PREP`

## Последствия решения

Если ОПЕРАТОР выбирает этот текст:

1. human-interface norm считается содержательно утверждённой;
2. KOO materializes exact `project-instructions-core-v2_4-approved.md`;
3. остальные пять active Project Sources не меняются;
4. KOO отдаёт ОПЕРАТОРУ готовый Markdown-файл напрямую;
5. после UI replacement + readback core v2.3 → v2.4 supersession вступает в силу;
6. только после этого KOO маршрутизирует RED bounded implementation-design task для литературного журнала;
7. journal сам по себе ещё не становится active mechanism;
8. journal activation потребует отдельного решения ОПЕРАТОРА после готового RED implementation candidate.

## Если решение не принято

Ничего не активируется и active Project Sources остаются без изменений.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: final human-interface + literary-journal preparation decision
СТАТУС: OPERATOR_DECISION_REQUIRED
