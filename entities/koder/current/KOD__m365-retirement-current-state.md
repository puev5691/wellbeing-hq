# KOD: текущее состояние M365 retirement

status: `RETIRED_EXTERNAL_CLEANUP_PENDING_OPERATOR`
task_id: `task:KOO-M365-SUPERVISOR-E2E-01`
production: `no`

## Проверенный project-side result

M365 supervisor E2E прекращён по решению ОПЕРАТОРА и принят KOO.

- KOD retirement result: `entities/koder/outbox/KOD__m365-contour-retirement__KOO.md`
- result commit: `ceeb152deec1996aaa0107f388fa1335b1d99ec1`
- KOO receipt: `routes/receipts/KOD__m365-contour-retirement__KOO.receipt.md`
- receipt commit: `5bc73559a0151a2f69a6d5dc4bb0cf66d229cae4`
- KOO acceptance: `entities/koordinator/outbox/KOO__m365-retirement-acceptance__KOD.md`
- KOO status: `RETIREMENT_ACCEPTED`
- KOO current checkpoint: `entities/koordinator/current/KOO__m365-supervisor-e2e-01.md`
- current task status: `RETIRED_BY_OPERATOR_DECISION`
- experiment status: `STOPPED`

## Запрещённое продолжение

Для этой Task ID KOD не возобновляет:
- Power Automate flow creation;
- M365 supervisor E2E;
- Microsoft-origin PR creation;
- browser-adapter work;
- попытки трактовать старые plugin/browser checkpoints как активный план.

Historical evidence сохраняется как provenance.

## Единственная незакрытая зависимость

External Microsoft 365 profile deletion остаётся `PENDING_OPERATOR_ACTION`.
Canonical задача ОПЕРАТОРУ:
`entities/koder/outbox/KOD__delete-m365-profile__OPERATOR.md`
→ `routes/dispatch/KOD__delete-m365-profile__OPERATOR.md`
→ `entities/operator/inbox/KOD__delete-m365-profile__OPERATOR.md`.

До Microsoft-side post-condition либо точного deferred-deletion status нельзя заявлять, что внешний M365 profile удалён.

## Resume-First

При следующем проходе:
1. GitHub preflight;
2. не считать эту Task ID ACTIVE/BLOCKED project work: она RETIRED;
3. проверить только наличие нового OPERATOR post-condition по external cleanup;
4. если его нет — не плодить новые M365 artifacts и не возобновлять experiment;
5. перейти к другим актуальным KOD task/checkpoint по Resume-First.

## ОПЫТ / KOD

Идея: retirement проекта и удаление внешнего аккаунта — разные post-condition.

Проба: M365 experiment был прекращён и маршрутизирован KOO, а external profile cleanup вынесен в отдельную OPERATOR-задачу.

Результат: KOO независимо прочитал retirement result, создал receipt и перевёл исходную Task ID в `RETIRED_BY_OPERATOR_DECISION`.

Итог: project-side retirement закрыт успешно; external cleanup ещё не доказан.

Фиксация: в Resume-First не возвращать retired experiment в ACTIVE только потому, что внешняя cleanup-задача ещё не завершена.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: reconciliate KOD Resume-First checkpoint после подтверждённого KOO retirement и отделить его от внешней OPERATOR cleanup-задачи
