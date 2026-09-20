# KOO → OPERATOR: human-readable results norm approval gate

status: OPERATOR_DECISION_REQUIRED
approved_source_mutation_before_decision: no
project_time: omitted; trusted project-time source not used

## Что уже сделано

KAN candidate:
`entities/kancelar/outbox/KAN__human-readable-results-rule-candidate__KOO-RED.md`
commit `4753d2c1903bec2501b7a79c6031068d7b0e2f5a`
blob `7651189ec49dd7ee68d4525fdebe92f628e15465`
verdict `PASS_KAN_HUMAN_READABLE_RESULTS_RULE_CANDIDATE_READY_FOR_RED_REVIEW`.

RED review:
commit `fbb2e9d428221dac9f4ab75f1bac7c1ce0f8e2c2`
verdict `PASS_RED_HUMAN_READABLE_RESULTS_RULE_CANDIDATE_R01`
status `CANDIDATE_READY_FOR_OPERATOR_DECISION`.

Current active project core:
`project-instructions-core-v2_3-approved.md`.

## Минимальное место изменения

Только:
`project-instructions-core-v2_3-approved.md`
→ successor `project-instructions-core-v2_4-approved.md`.

Вставка:
после раздела `## Минимальный документооборот`
и перед `## Доставка артефактов`.

Другие active sources менять не требуется.

## Exact proposed delta

### Человекочитаемые результаты

Если результат предназначен ОПЕРАТОРУ или иному человеку, сначала кратко и понятным русским языком указывается:

`что произошло → что это означает → что теперь возможно, разрешено или требуется`.

После этого, если они нужны для проверки или исполнения, приводятся точные технические данные: machine status, version, commit/blob/tree, locator, path, protocol fields и другие literal identifiers.

Техническая точность имеет приоритет над литературностью. Source code, commands, config, logs, protocol literals, identifiers и machine-readable fields сохраняются буквально там, где изменение формы может снизить корректность.

Это правило не требует дополнительных документов, summary-файлов, cover notes или отдельных «человекочитаемых версий». Если один artifact может одновременно содержать понятное объяснение и точные machine fields, используется один artifact.

Pure machine-consumed code, config, logs и protocol data не требуют дополнительного русского пояснения.

Один machine status без человеческого объяснения недостаточен как результат, адресованный ОПЕРАТОРУ или иному человеку.

## Что эта норма НЕ делает

- не меняет machine status vocabulary;
- не требует переводить source code, commands, config, logs или protocol literals;
- не создаёт новых обязательных документов;
- не меняет routing/recovery/task-conveyor;
- не делает RED обязательным участником каждого результата;
- не активирует event journal;
- не ухудшает automation/parsing.

## OPTION A — approve

Decision text:

`APPROVE_HUMAN_READABLE_RESULTS_NORM_CORE_V24`

Effect:
- KOO materializes exact `project-instructions-core-v2_4-approved.md`;
- no other source changes;
- KOO prepares one-file source replacement package;
- OPERATOR receives the ready Markdown file directly, not a GitHub scavenger hunt;
- after Project Sources replacement/readback, v2.3 → v2.4 supersession becomes effective.

## OPTION B — reject/edit

Decision text:

`REVISE_HUMAN_READABLE_RESULTS_NORM: <exact change>`

Effect:
- no source mutation;
- KOO applies only the exact requested correction using already reviewed basis;
- no new KAN/RED cycle unless the change materially expands scope.

## Separate follow-up

Human-readable significant-event journal remains separate and parked until this general norm is resolved.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: final OPERATOR decision on general human-readable-results norm
СТАТУС: OPERATOR_DECISION_REQUIRED
