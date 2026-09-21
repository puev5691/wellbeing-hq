# KOO → WEB: baseline Project Core refresh v2.5

status: SOURCE_REFRESH_REQUIRED_ON_NEXT_RESUME
project_time: omitted

## Что изменилось

Active Project Core проекта заменён:

`project-instructions-core-v2_4-approved.md`
→
`project-instructions-core-v2_5-approved.md`

Activation terminal:
`PASS_KOO_SOURCE_SET_R07_ACTIVATED`

Activation result:
`entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md`

New active source:
`entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md`

materialization commit:
`c2cedda8922f377654b1772acbf9e5f7e5028a9d`

Git blob:
`a42f7dca6a7469a54fa2da24aae0da4e549c9d33`

SHA-256:
`f2ad19e243e55c552b10372c4bd7ddda7f18018579527f94d69e14858303b49c`

## Что требуется от Сущности

При ближайшем Resume-First:

1. fresh-reconcile active Project Sources;
2. прочитать active Project Core v2.5;
3. считать v2.4 superseded provenance, а не current norm;
4. применять обязательный human-first слой во всех human-facing ответах;
5. не менять профильное current-state только ради этого source refresh;
6. продолжить текущую профильную задачу с того же causal state.

## Human-first обязательная норма

Человеку сначала сообщается:
`что произошло → почему это важно → где мы сейчас → что дальше`.

Machine statuses, paths, hashes, commits и иные exact evidence по умолчанию остаются в информационном поле и выводятся человеку только когда practically нужны.

Human-facing текст должен сохранять причинную цепочку и быть пригодным как исходный материал для лабораторного/исторического журнала, Telegram и портала.

Это не создаёт automatic publication, automatic journal inclusion или per-task editorial reporting.

## Boundary

Этот source refresh:
- не создаёт новую профильную задачу;
- не меняет task authority;
- не меняет writer authority;
- не меняет delivery/acceptance существующих задач;
- не требует отдельного terminal artifact только ради подтверждения refresh.

На следующем содержательном ответе человеку новая норма должна уже применяться.
