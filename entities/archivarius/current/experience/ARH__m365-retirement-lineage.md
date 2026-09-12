# ARH: M365 retirement event-lineage

## Назначение

Зафиксировать прекращение experimental M365 / Power Automate supervisor contour как отдельное причинное событие и не допустить его случайного восстановления из historical blockers, dispatch или activation records.

## Проверенная смена состояния

Ранее ветка M365 рассматривалась как отдельная experimental chain:

`Power Automate -> GitHub PR -> ChatGPT Work trigger -> recovery -> profile processing`

Эта ветка больше не является active experimental dependency.

KOD выпустил project-side retirement result:

`entities/koder/outbox/KOD__m365-contour-retirement__KOO.md`

source commit: `ceeb152deec1996aaa0107f388fa1335b1d99ec1`

KOO зарегистрировал receipt:

`routes/receipts/KOD__m365-contour-retirement__KOO.receipt.md`

receipt commit: `5bc73559a0151a2f69a6d5dc4bb0cf66d229cae4`

KOO затем обновил свой current checkpoint:

`entities/koordinator/current/KOO__m365-supervisor-e2e-01.md`

retired checkpoint commit: `a30c26759a2f7764c9ded2a8d1d80b8fdaa3d600`

И принял retirement решением:

`entities/koordinator/outbox/KOO__m365-retirement-acceptance__KOD.md`

acceptance commit: `4a13bad80cab429e09286db1c2a039f4d83b47a5`
status: `RETIREMENT_ACCEPTED`

## Что именно закрыто

Для Task ID `task:KOO-M365-SUPERVISOR-E2E-01` запрещено продолжать без нового явного решения ОПЕРАТОРА:

- Power Automate flow creation;
- M365 supervisor E2E;
- Microsoft-origin PR creation;
- browser-adapter work специально ради этой ветки.

Historical evidence сохраняется как provenance неудачного/прекращённого эксперимента и не удаляется из-за retirement.

Retirement не превращает прежние `activation_failed`, browser-control blockers или отсутствие product-side Work evidence в успешные события. Они остаются историческими состояниями своих механизмов.

## Что НЕ закрыто

Отдельная внешняя зависимость остаётся:

`entities/operator/inbox/KOD__delete-m365-profile__OPERATOR.md`

status: `PENDING_OPERATOR_ACTION`

Требуется Microsoft-side post-condition удаления созданной для эксперимента registration/profile либо точный deferred status, если удаление отложено Microsoft.

Repository dispatch, detector PASS или activation request не являются доказательством выполнения внешнего Microsoft cleanup.

## Activation boundary внешнего cleanup

Для OPERATOR cleanup-task существует activation evidence:

`routes/activation/KOD__delete-m365-profile__OPERATOR.activation.md`

Состояние, зафиксированное в проекте:

- detector PASS;
- activation requested;
- processing_started: no;
- activation_failed;
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`;
- manual OPERATOR processing required.

Следовательно, project-side M365 contour retired, но external Microsoft cleanup completion не доказан.

## SHT cross-stage reconciliation

SHT синхронизировал current-state и отделил retirement от соседних веток:

`entities/shtabist/current/SHT__m365-recovery-cross-stage-state.md`

reconciliation commit: `6f353477d617089bfdb3970d2485f713deaa4f0e`

Текущее смысловое состояние:

`M365_CONTOUR_RETIRED__EXTERNAL_MICROSOFT_PROFILE_CLEANUP_PENDING_OPERATOR__OTHER_BRANCHES_DELEGATED_TO_SPECIALIZED_CURRENT_FILES`

Это важная anti-regression граница: retirement M365 не определяет и не изменяет состояние Entity Runner, recovery, memory-layering, GitHub information-entry или иных independent branches.

## Causal lineage

Текущая последовательность должна читаться так:

`M365 experimental contour -> Opera/browser-control blocker -> OPERATOR decision to stop experiment -> KOD retirement result -> KOO receipt -> KOO retired checkpoint -> KOO RETIREMENT_ACCEPTED -> project-side contour closed -> external Microsoft profile cleanup remains separate pending OPERATOR action`.

Нельзя выводить:

- `retirement accepted` = `Microsoft profile deleted`;
- `dispatch` = `processing`;
- `activation requested` = `Entity execution`;
- `historical blocker` = `current active dependency`;
- `retired experiment` = `failed forever` или `can never be reconsidered`.

Повторное открытие contour возможно только через новое явное решение ОПЕРАТОРА, а не через старые task/route/activation artifacts.

## Текущая граница

project_side_m365_contour: retired_accepted
m365_task_id: task:KOO-M365-SUPERVISOR-E2E-01
external_microsoft_cleanup: pending_operator_action
external_cleanup_completion: not_proven
historical_evidence: preserve_as_provenance
resume_without_new_operator_decision: prohibited
cross_branch_inference: prohibited
project_time: omitted; trusted project-time source not used

---
created_by: ARH / АРХИВАРИУС
created_for: preservation of M365 retirement causal boundary and prevention of accidental experiment resurrection
creation_time: omitted; trusted project-time source not used
