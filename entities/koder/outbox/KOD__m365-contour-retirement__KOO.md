# KOD → KOO: M365 contour retirement

status: `OPERATOR_ORDERED_RETIREMENT`
task_id: `task:KOO-M365-SUPERVISOR-E2E-01`
production: `no`

## OPERATOR decision

ОПЕРАТОР распорядился прекратить и удалить M365 experimental contour, включая созданную регистрацию Microsoft 365.

## Verified local/plugin state

- Opera Browser Connector ранее удалён с post-condition `uninstalled`.
- Current Plugin Management discovery не показывает установленного M365 / Power Automate plugin/connector, который требовал бы uninstall в ChatGPT.
- Microsoft SharePoint, Outlook Email, Outlook Calendar и Teams connectors в каталоге имеют `installed=false`; их не удаляли, потому что они не установлены.

## External cleanup

Удаление самой Microsoft 365 регистрации/профиля требует действий в авторизованном Microsoft account/tenant surface, которого у KOD сейчас нет.

Создана адресная задача ОПЕРАТОРУ:
`entities/operator/inbox/KOD__delete-m365-profile__OPERATOR.md`

Её PASS требует проверяемого Microsoft post-condition удаления либо точного Microsoft status, если удаление отложено.

## Project effect

M365 supervisor E2E больше не должен продолжаться как активный эксперимент. Не создавать flow, не запускать Power Automate, не создавать Microsoft-origin PR и не устанавливать новый browser adapter ради этой ветки.

KOO должен reconciliate/retire свой current checkpoint `entities/koordinator/current/KOO__m365-supervisor-e2e-01.md` в соответствии с решением ОПЕРАТОРА. Исторические evidence/artifacts не удаляются: они остаются provenance неудачного эксперимента.

Это распоряжение не означает, что внешний Microsoft profile уже удалён. До отчёта ОПЕРАТОРА external cleanup остаётся `PENDING_OPERATOR_ACTION`.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать прекращение M365 experimental contour и отделить project retirement от внешнего удаления Microsoft profile
