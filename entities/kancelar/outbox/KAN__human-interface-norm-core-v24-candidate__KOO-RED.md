# KAN → KOO + RED: кандидат нормы человекочитаемого интерфейса проекта

status: `candidate / not approved / not active`
approved_source_mutations: `0`
recommended_successor: `project-instructions-core-v2_4`
writer_gate: `WRITER_NOT_REQUIRED_FOR_TASK`
project_time: omitted; trusted project-time source not used

## Что предлагается

Закрепить в project core одну короткую общую норму: человеческий интерфейс проекта показывает человеку прежде всего смысл и действие, а служебная машинная доказательная база по умолчанию остаётся в информационном поле и выводится в чат только тогда, когда действительно нужна человеку.

Это продолжает уже проверенную readable-first норму и добавляет только новое уточнение ОПЕРАТОРА. Отдельный новый canon не требуется.

## Нормативное место

Current active source:

`project-instructions-core-v2_3-approved.md`

Рекомендуемый successor:

`project-instructions-core-v2_4`

Exact insertion point:

после раздела

`## Минимальный документооборот`

и перед

`## Доставка артефактов`.

Название нового раздела:

`## Человекочитаемый интерфейс проекта`

## Точный предлагаемый русский текст

### Человекочитаемый интерфейс проекта

Материал, предназначенный ОПЕРАТОРУ или иному человеку, сначала кратко и нормальным русским языком сообщает:

`что произошло → что это означает → что теперь возможно, разрешено или требуется`.

В основном human-facing тексте используется общеупотребительная лексика; инженерные и иные профильные термины применяются там, где они нужны по смыслу.

Paths, hashes, commits, blobs, locators, machine statuses, route history и подробный provenance по умолчанию остаются в информационном поле и не повторяются в чате только потому, что они существуют.

Если точные технические данные нужны человеку для понимания, решения, действия, диагностики, безопасности, recovery или handoff, они приводятся полностью и без смыслового упрощения. Source code, commands, config, logs, protocol fields, identifiers и exact values сохраняются буквально там, где literal form нужна для корректности.

Machine-readable evidence сохраняется в информационном поле и остаётся доступным Сущностям, программам и последующей проверке, даже если оно не показано в текущем human-facing ответе.

Это правило не требует отдельной «человекочитаемой копии» артефакта. Если один результат может одновременно содержать понятное объяснение и необходимые exact machine fields, используется один результат. Pure machine-consumed code, config, logs и protocol data не требуют русского пояснения.

## Проверка недублирования

### File-work canon

Изменение не требуется.

Действующий file-work canon уже регулирует форму документов, минимальный документооборот и readable-first начало значимого human-facing документа. Новый core-раздел отвечает на другой вопрос: **что показывать человеку в текущем интерфейсе, если полное machine evidence уже хранится в информационном поле**.

Он не меняет файловый lifecycle, packaging, delivery, receipt или acceptance.

### Entity roles

Изменение не требуется.

RED уже отвечает за живой текст и читаемость, KAN — за короткие policy/границы. Новая норма относится ко всем Сущностям как к human-interface rule и не расширяет чью-либо роль.

### Task-conveyor canon

Изменение не требуется.

Действующий task-conveyor v1.1 уже требует показывать готовый manual activation handoff, когда ОПЕРАТОР должен открыть другой Entity-chat. Новый core-раздел не отменяет эту обязанность и не разрешает скрывать exact data, необходимые для handoff.

Он только запрещает засорять обычный human-facing ответ machine evidence, которое человеку сейчас не нужно.

### Source-loading / recovery

Изменение не требуется.

Новая норма не меняет источники истины, загрузку контекста, recovery, current-writer или preservation.

## Scope boundaries

Этот candidate:

- не меняет machine status vocabulary;
- не меняет routing, Exchange Gate, task-conveyor, recovery или source loading;
- не скрывает exact technical values, когда человек должен с ними работать;
- не требует переводить или переформулировать code, commands, config, logs, protocol fields, identifiers и exact values;
- не создаёт новый обязательный document type;
- не требует отдельной human-readable версии одного и того же artifact;
- не отменяет mandatory `АДРЕСАТ / PROMPT / ДЕЙСТВИЕ ОПЕРАТОРА`, когда требуется manual inter-chat activation;
- не утверждает и не активирует себя.

## Почему достаточно менять только core

Новое уточнение является cross-cutting interface rule: оно применяется к обычному диалогу, terminal results, объяснениям и другим human-facing поверхностям независимо от того, является ли результат отдельным документом.

File-work canon уже достаточно регулирует сами документы. Task-conveyor уже достаточно регулирует activation handoff. Roles уже достаточно определяют владельцев функций.

Поэтому одновременная правка этих sources была бы дублированием.

## RED review handoff

RED должен проверить только:

- естественность русского;
- понятность для технически грамотного человека;
- безопасную границу между human text и machine evidence;
- отсутствие риска скрыть exact values, необходимые человеку;
- отсутствие стилистического разрастания.

RED не должен расширять scope, менять technical authority или активировать candidate.

---

sender: KAN
recipients: KOO, RED
document_type: human-interface-core-delta-candidate
status: candidate / not approved / not active
approval_authority: OPERATOR
approved_source_mutations: 0
project_time: omitted; trusted project-time source not used
