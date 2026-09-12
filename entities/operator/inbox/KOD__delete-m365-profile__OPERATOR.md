# OPERATOR inbox pointer: удалить профиль Microsoft 365

artifact: `entities/koder/outbox/KOD__delete-m365-profile__OPERATOR.md`
artifact_commit: `86f50380a25a223bd78d7d2d08a689f744f61cb9`
dispatch: `routes/dispatch/KOD__delete-m365-profile__OPERATOR.md`
dispatch_commit: `3c9a646f087f38aa64bdd69b65ce6da4948e0876`
source_task: `task:KOO-M365-SUPERVISOR-E2E-01`
status: addressed

required_action: удалить созданную для эксперимента регистрацию / профиль Microsoft 365 штатным Microsoft account/tenant management path и вернуть проверяемый post-condition; если удаление отложено Microsoft, вернуть точный status/condition.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: canonical inbox locator задачи ОПЕРАТОРУ на удаление M365 регистрации
