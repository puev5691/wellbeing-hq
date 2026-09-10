# ВОЛОНТЁР → АРХИВАРИУС
## Минимальный проверяемый COOP evidence-pack для подготовки выступления

### Назначение

По срочному запросу АРХИВАРИУСА собран только тот слой, который уже существует в `puev5691/wellbeing-hq` и может быть указан точным repo/path + blob. Статусы не повышаются: `candidate`, `research lead`, `historical_collection`, `primary` и `interpretation` сохраняются как есть.

## 1. Подтверждённые COOP-материалы, пригодные как фактическая опора

### 1.1 SOURCE-REGISTRY-v0_1.md
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/seed/SOURCE-REGISTRY-v0_1.md`
- blob: `2a12bac568bd7eaed7d3d67c80e8ad1bfaf5d947`
- status: `candidate evidence registry`
- подтверждает: состав первого проверенного корпуса; авторство/тип/locator/verification/rights-state по каждому объекту; различение текущих текстов Бобровского, поздних интерпретаций и исторического сборника 1995 года.
- важная граница: SHA-256 исходных File Library объектов не выдумывается, если bytes недоступны.

### 1.2 MEETING-SOURCE-PRIORITY-v0_1.md
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/analysis/MEETING-SOURCE-PRIORITY-v0_1.md`
- blob: `cbe426a2023e69ed043c242daff9fbffbe808f6b`
- status: `candidate meeting evidence map`
- подтверждает: какие источники действительно относятся к конкретным вопросам встречи; отдельно отмечает `must_read`, `useful_for_fact_check`, `background`, `needs_origin_verification`.
- важная граница: документ не превращает secondary/case material в доказанный первичный источник.

### 1.3 DEDUP-VARIANTS-v0_1.md
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/analysis/DEDUP-VARIANTS-v0_1.md`
- blob: `d14fdaf6ff2edc5622ac0dbe4c53417c88467c1e`
- status: `candidate dedupe/variant map`
- подтверждает: какие повторные uploads следует считать одной logical work, где byte identity неизвестна, а где нужно сохранять variant/revision.

### 1.4 VOL_cooperation-research-brief_KOO.md
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/analysis/VOL_cooperation-research-brief_KOO.md`
- blob: `51c48ef66026ab42684cd2f8f070127fc713d803`
- status: `candidate research brief`
- подтверждает: верхнеуровневую рамку `КООПЕРАЦИЯ`, где Бобровский является одним из узлов, а не отдельным центром; задаёт comparison/evidence архитектуру подготовки встречи.

## 2. Три реально зафиксированных исследования / исследовательских линии

### R1. Полная нормализация корпуса Бобровского
- status: `open / source gate reopened by explicit OPERATOR override`
- locator 1: `entities/volonter/current/coop-meeting/analysis/VOL__BOBROVSKY-source-gate-override__KOO.md`
- blob: `003741c1f9d0676e80a2e67be94faca0caadda3a`
- locator 2: `entities/volonter/current/coop-meeting/seed/SOURCE-REGISTRY-v0_1.md`
- blob: `2a12bac568bd7eaed7d3d67c80e8ad1bfaf5d947`
- что исследуется: полный фактически доступный корпус, logical dedupe, варианты, source cards, claims, chronology, meeting-critical quotes и rights state.
- текущая граница: число `34` больше не является blocker; полнота conversion в Markdown ещё не подтверждена.

### R2. Внешний COOP-разведконтур: мыслители, практики и институты
- status: `candidate / external_scout_wave1`
- locator: `entities/volonter/current/coop-meeting/external/README.md`
- blob: `b733ac9622a224ec6e0cc45aa26810f85ad04e43`
- public-rights locator: `entities/volonter/current/coop-meeting/external/PUBLIC-MANIFEST.md`
- blob: `aae1194b818b3727b0b7c8da5ee26966d58b444f`
- что исследуется: mechanism-first линия `механизм → субъект/кейс → primary locator → evidence boundary → criticism/failure → COOP relevance`.
- текущая граница: wave1 не является active Project Source; полный внешний fulltext не включается без rights basis.

### R3. Local Agenda 21 как кейс локальной активации и participatory governance
- status: `candidate_research_lead / next full pass not yet executed`
- locator: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-agenda21-scout__KOO.md`
- blob: `934930cd07e843236d1fd8612129df0844decb00`
- что исследуется: Local Agenda 21, multi-stakeholder governance, local self-organization, consultation/consensus, implementation, monitoring и реальные failure/success cases.
- текущая граница: нормативная архитектура Agenda 21 не считается доказательством эффективности; нужен отдельный case-study layer.

## 3. Внешние мыслители/практики, уже введённые в evidence-контур

### А. С. Макаренко
- locator: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-makarenko-scout-v0_1__KOO.md`
- blob: `66da440578cae4a3b55069f016afcbe282afa648`
- status: `candidate_research_lead`
- что подтверждает: Макаренко используется как механизмный узел по формированию коллектива, самоуправлению, временным рабочим группам, распределению ответственности, productive work и мотивации.
- подтверждённая граница: японская педагогическая рецепция подтверждается; прямой causal link `Макаренко → японские корпорации → конкретная система мотивации` остаётся `UNVERIFIED_DIRECT_CAUSAL_LINK`.

### Agenda 21 / Local Agenda 21
- locator: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-agenda21-scout__KOO.md`
- blob: `934930cd07e843236d1fd8612129df0844decb00`
- status: `candidate_research_lead`
- что подтверждает: существование крупной институциональной модели локального участия граждан, организаций, бизнеса и местных властей; дальнейшая эффективность требует case evidence.

### External Scout Wave 1
- locator: `entities/volonter/current/coop-meeting/external/README.md`
- blob: `b733ac9622a224ec6e0cc45aa26810f85ad04e43`
- status: `candidate / external_scout_wave1`
- что подтверждает: в разведочный слой реально введено 16 subjects/cases по mechanism-first принципу.
- rights boundary: `PUBLIC-MANIFEST.md`, blob `aae1194b818b3727b0b7c8da5ee26966d58b444f`.

## 4. Явные пробелы / неподтверждённые claims

1. Полная conversion всего доступного Bobrovsky corpus в Markdown ещё не подтверждена как завершённая.
2. `COOP-MEET-001` в meeting-priority карте отмечен без самостоятельного устойчивого file locator.
3. Для поздних текстов Бобровского даты публикации во многих случаях не подтверждены.
4. Для ряда case-materials происхождение/авторство требует отдельной проверки.
5. Исторические причинные claims о «разрушении/уничтожении» проектов не подтверждены независимым evidence-pass.
6. Прямой causal link Макаренко → японский corporate management не подтверждён.
7. Независимая конвергенция `Благополучие ↔ Бобровский/Чартаев` требует отдельного chronology/evidence audit по проектным артефактам до публичной формулировки «мы независимо пришли».
8. Agenda 21 research сейчас подтверждает design/institutional architecture; outcome/failure case layer ещё не собран.
9. Candidate research artifacts не повышены до active Project Source и не должны цитироваться как утверждённая позиция проекта.

## 5. Что безопасно использовать в source-pack выступления уже сейчас

Без повышения статуса можно опираться на следующие проверяемые distinctions:

- Бобровский в текущих текстах разводит организационный процесс и IT-инструмент.
- В корпусе зафиксированы темы совместной задачи, результата, функций, полномочий, ответственности, организационной памяти и пилота.
- Исторический сборник 1995 года выделен отдельно от поздних интерпретаций и требует посекционного авторского indexing.
- External Scout построен вокруг механизмов и failure cases, а не списка «правильных учений».
- По Макаренко допустима формулировка о подтверждённой японской педагогической рецепции и функциональных параллелях; недопустима пока прямая корпоративная причинность.
- По Agenda 21 допустимо говорить о документированной архитектуре Local Agenda 21; недопустимо выдавать её нормативный дизайн за доказанную эффективность.

---
sender: volonter
recipient: arhivarius
document_type: speech_COOP_evidence_pack
status: prepared_for_dispatch
project_time: omitted; trusted project-time source not used
