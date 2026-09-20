# KAN → KOO + RED: кандидат нормы человекочитаемых результатов

status: `candidate / not approved / not active`
approved_source_mutations: `0`
writer_gate: `WRITER_NOT_REQUIRED_FOR_TASK`
project_time: omitted; trusted project-time source not used

## Смысл

Для результата, который предназначен человеку, сначала должен быть понятен человеческий смысл: что произошло, что это означает и что теперь можно, нужно или нельзя делать. Точные технические данные сохраняются и следуют после этого там, где они нужны для проверки или исполнения.

Норма не должна порождать отдельные summary-файлы, cover notes или «человеческие копии» тех же артефактов.

## Рекомендуемое нормативное место

Минимальное место закрепления:

`project-instructions-core-v2_2-approved.md`

Вставка отдельного короткого раздела:

`## Человекочитаемые результаты`

сразу после раздела:

`## Минимальный документооборот`

и перед:

`## Доставка артефактов`.

Причина: правило относится ко всем human-facing результатам, а не только к формальным документам. Поэтому project core является более точным местом, чем file-work canon или role-specific source.

Отдельный новый canon не нужен.

## Точный предлагаемый текст вставки

### Человекочитаемые результаты

Если результат предназначен ОПЕРАТОРУ или иному человеку, он сначала кратко и понятным русским языком объясняет:

`что произошло → что это означает → что теперь возможно, разрешено или требуется`.

После этого, если они нужны для проверки или исполнения, приводятся точные технические данные: machine status, version, commit/blob/tree, locator, path, protocol fields и другие literal identifiers.

Техническая точность имеет приоритет над литературностью. Source code, commands, config, logs, protocol literals, identifiers и machine-readable fields сохраняются буквально там, где изменение формы может снизить корректность.

Это правило не требует создавать дополнительные документы, summary-файлы, cover notes или отдельные «человекочитаемые версии». Если один artifact может одновременно содержать понятное объяснение и точные machine fields, используется один artifact.

Pure machine-consumed code, config, logs и protocol data не обязаны дополняться русской прозой.

Один machine status без человеческого объяснения недостаточен как результат, адресованный ОПЕРАТОРУ или иному человеку.

## Проверка недублирования

### Project core: minimal document flow

Действующая норма уже запрещает лишний документооборот и требует один проверяемый результат с короткой фиксацией.

Предлагаемая вставка не создаёт новый artifact type и не требует второго документа. Она определяет только порядок изложения внутри уже существующего human-facing результата.

### File-work canon §4.1

§4.1 запрещает автоматически плодить route-note, manifest, request, acceptance, status-report и другие документы без практической функции.

Новая норма эту границу усиливает: человекочитаемое объяснение помещается в тот же artifact, а не оформляется отдельной обязательной «человеческой версией».

### File-work canon §23

§23 уже требует начинать документ с краткого смысла, назначения, требуемого действия и статуса, а служебные данные переносить ниже.

Предлагаемая норма шире по области: она относится не только к формальным документам, но к любому результату, адресованному человеку, и задаёт единый смысловой порядок:

`событие → значение → возможность/требование → exact technical evidence`.

Поэтому она дополняет §23, а не повторяет его.

### RED role

РЕДАКТОР уже отвечает за readable-first, естественный текст и сохранение фактического статуса.

Новая норма не переносит на RED контроль фактов и не делает RED обязательным участником каждого результата. Она устанавливает общий minimum для всех Сущностей; RED остаётся профильным владельцем качества текста, когда отдельная редакторская работа действительно нужна.

## Scope boundaries

Этот candidate НЕ:

- меняет machine status vocabulary;
- требует перевода или переформулировки source code, commands, config, logs, protocol literals, identifiers или machine-readable fields;
- меняет routing, recovery, task-conveyor или Exchange Gate;
- создаёт обязательный новый artifact, summary, cover note или duplicate version;
- утверждает human-readable event journal;
- требует prose wrapping для pure machine-consumed data;
- активирует или утверждает сам себя;
- изменяет любой approved Project Source в этой задаче.

## Почему другие approved sources одновременно менять не требуется

Одновременная правка `file-work-canon` не требуется, потому что его §4.1 и §23 уже совместимы с предлагаемой нормой и не конфликтуют с ней.

Одновременная правка `entity-roles-short` не требуется, потому что роли KAN и RED уже задают свои профильные функции, а новая норма является общепроектной формой human-facing результата, а не изменением роли.

`source-loading-policy`, `recovery canon` и `task-conveyor canon` не затрагиваются по смыслу вообще.

Минимальная корректная дельта поэтому одна: короткая вставка только в project core после отдельного решения ОПЕРАТОРА.

## Handoff для RED

RED должен проверить только:

- естественность русского текста вставки;
- ясность смысловой последовательности;
- сохранение technical fidelity;
- отсутствие стилистического разрастания;
- отсутствие скрытого требования создавать дополнительные документы.

RED не должен:
- расширять scope нормы;
- добавлять event journal;
- менять routing/recovery/task-conveyor;
- превращать machine literals в литературный пересказ;
- менять статус candidate.

## Terminal result

`PASS_KAN_HUMAN_READABLE_RESULTS_RULE_CANDIDATE_READY_FOR_RED_REVIEW`

candidate_locator:
`entities/kancelar/outbox/KAN__human-readable-results-rule-candidate__KOO-RED.md`

recommended_normative_location:
`project-instructions-core-v2_2-approved.md → after ## Минимальный документооборот`

approved_source_mutations:
`0`

next_owner:
`RED / bounded readability review`

---

sender: KAN
recipients: KOO, RED
document_type: human-readable-results-rule-candidate
status: candidate / not approved / not active
approval_authority: OPERATOR only
project_time: omitted; trusted project-time source not used
