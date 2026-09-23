# Exact correction diff: Project Instructions v3 r0.2 → r0.3

status: EXACT_TEXTUAL_CORRECTION_MAP
base: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r02.md@da770ca7dede1a21c415c7fd6b1912f97b5482c4
successor: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03.md
scope: K1-K4 + K6 + K5 evidence-gap metadata only

## K1 — §2 heading and opening

OLD:
`## 2. Resume-First`

`Каждое новое пробуждение, activation или продолжение существенной работы начинается с минимального fresh reconciliation:`

NEW:
`## 2. Wake → Resume / Initiation → Exact Task`

`Каждое пробуждение начинается с проверки continuity экземпляра. При подтверждённой continuity выполняется Resume-First. Новый, заменяющий или недостоверно восстановленный экземпляр проходит Initiation-required по действующему recovery-канону; проверенная инициация и writer authority проверяются раздельно. Независимо авторизованный bounded read-only/diagnostic шаг допускается только в предусмотренных каноном границах и не заменяет initiation или Writer Gate.`

`После выбора Resume/Initiation существенная работа начинается с минимального fresh reconciliation:`

## K6-support — §3 parallel lanes clarification

OLD:
`Это не запрещает независимые parallel lanes. Параллельность допустима только при отсутствии causal, mutable-resource, current-writer и authority conflicts.`

NEW:
`Это не запрещает независимые parallel lanes, если одного профильного owner недостаточно для нескольких действительно независимых causal steps. Параллельность не создаёт task authority и не отменяет минимальную достаточность состава исполнителей, существующие WIP/coordination limits или профильную ответственность за каждый результат. Она допустима только при отсутствии causal, mutable-resource, current-writer и authority conflicts.`

## K3/K4 — §4.4 automatic/manual branch

OLD:
`Если exact scope покрыт проверенным orchestrator/automatic activation, человеку сообщается:`

NEW:
`Если exact scope покрыт отдельно утверждённым standing/explicit automation-authority и фактически проверенным механизмом automatic activation, действуют автоматическая ветвь и обязательные проверки §9. Техническая доступность сама по себе ручную ветвь не отменяет.`

`В таком случае человеку сообщается:`

OLD:
`Если automatic activation для exact scope отсутствует, ответ содержит готовый manual handoff:`

NEW:
`Во всех остальных случаях сохраняется переходный ручной режим: ОПЕРАТОР передаёт готовый PROMPT адресному чату, но не собирает PROMPT и не переносит referenced artifacts, доступные по проверяемому locator.`

`Если следующего разрешённого профильного шага Сущность определить не может, она не придумывает поручение, а даёт готовый handoff КООРДИНАТОРУ для fresh reconciliation. При неподтверждённой continuity/writer КООРДИНАТОРА ему не поручается профильная mutation в обход recovery gate; человеку сообщается конкретная зависимость.`

`Manual handoff:`

## K2 — §10 file-first

OLD:
`Значимый reusable результат должен существовать как самостоятельный проверяемый artifact, когда задача этого требует.`

NEW:
`Значимый рабочий результат должен существовать как самостоятельный проверяемый файл или пакет по действующему файловому канону. Самостоятельный артефакт не требует дополнительных manifest, summary и других документов без практической функции. Исключения применяются только в предусмотренных каноном случаях.`

## K6 — §11 status/provenance boundary

OLD opening:
`## 11. Activation lineage и время`

`Не склеивай разные experiment/task lineage по теме, похожести или времени.`

`Late BRIDGE/relation может связать существующие события, но не переписывает historical parent.`

NEW opening:
`## 11. Activation lineage и время`

`Общие действующие границы delivery/activation/processing применяются по active Project Sources. Специфические event/BRIDGE правила применяются только в пределах подключённого и утверждённого activation-lineage contract; данный общий текст не повышает экспериментальную схему до active contract автоматически.`

`В пределах применимого утверждённого contract не склеивай разные experiment/task lineage по теме, похожести или времени. Late BRIDGE/relation может связать существующие события, но не переписывает historical parent.`

## K4 — §15 transition wording

OLD:
`ОПЕРАТОР не должен быть:`
`- ручным маршрутизатором каждой задачи;`

NEW:
`Целевое состояние автоматизируемого проекта: ОПЕРАТОР не должен оставаться постоянным машинным диспетчером. Пока exact scope не покрыт разрешённой и проверенной автоматизацией, действует переходный manual handoff из §4.4.`

`ОПЕРАТОР не должен самостоятельно реконструировать машинную маршрутизацию и по мере покрытия automation не должен оставаться:`
`- ручным маршрутизатором каждой задачи;`

## K5/K6 — service metadata

OLD:
`version: v3-candidate-r0.2`

NEW:
`version: v3-candidate-r0.3`

ADDED:
`policy_delta_status:`
`- mandatory terminal-dialogue scenario: NEW_PROPOSED_POLICY_REQUIRES_OPERATOR_APPROVAL`
`- orchestrator automatic-activation rules beyond active-source invariants: NEW_PROPOSED_POLICY_REQUIRES_OPERATOR_APPROVAL`
`- specific activation-lineage BRIDGE semantics: PROFILE_CONTRACT_ONLY_IF_SEPARATELY_APPROVED`
`- memory/Booster implementation details: PROFILE_IMPLEMENTATION_NOT_PROMOTED_BY_THIS_DOCUMENT`

`predecessor_ui_baseline:`
`- exact UI Project Instructions v2 immutable export: NOT_AVAILABLE_IN_VERIFIED_PROJECT_EVIDENCE`
`- preservation completeness versus UI predecessor: NOT_VERIFIED`
`- this gap does not block candidate correction/re-review, but blocks complete predecessor diff/activation claim`

Basis updated from r0.1 to r0.2 + exact KAN review commit.

No other intentional policy change was introduced in r0.3.

---
КТО: SHT / ШТАБИСТ
СТАТУС: EXACT_TEXTUAL_CORRECTION_MAP
