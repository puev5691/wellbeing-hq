# KOO → KOD: Power Automate supervisor setup via ChatGPT Work

## Задача

Продолжить ту же активную Task, а не создавать новую:

- entity_id: `ent:KOO-M365-E2E-01`
- task_id: `task:KOO-M365-SUPERVISOR-E2E-01`

Использовать ChatGPT Work / Cloud Browser для настройки Microsoft Power Automate вместо ручного пошагового кликанья ОПЕРАТОРОМ.

## Resume-First input

Current checkpoint:
`entities/koordinator/current/KOO__m365-supervisor-e2e-01.md`

Resume-First Gate:
`entities/koordinator/current/KOO__continuity-resume-first-gate.md`

Prepared GitHub branch:
`m365/activation-e2e-koo-01`

Marker commit:
`ea0ebdae5125a9bd9321827f549f1f5c85e9d80e`

Do not create a replacement Task ID.

## Required browser action

Open:
`https://make.powerautomate.com`

If authentication or MFA is required:
- pause;
- request OPERATOR takeover/login;
- never ask OPERATOR to paste password or MFA secret into chat;
- after authenticated session is available, continue.

Create one bounded Scheduled cloud flow:

Trigger:
- Recurrence
- one-hour test cadence

Action:
- GitHub connector
- CreatePullRequest

Repository:
- owner: `puev5691`
- repo: `wellbeing-hq`

PR:
- title: `[E2E] M365 activation KOO 01`
- head: `m365/activation-e2e-koo-01`
- base: `main`
- draft: false
- body must contain:
  - `ent:KOO-M365-E2E-01`
  - `task:KOO-M365-SUPERVISOR-E2E-01`
  - marker commit `ea0ebdae5125a9bd9321827f549f1f5c85e9d80e`

## Verification

Do not claim success from UI clicks.

PASS Stage A requires:
1. flow exists and can be read back;
2. run history shows a real run;
3. GitHub readback shows PR created by the Microsoft-side path;
4. PR head/base match expected values;
5. marker commit is reachable from PR head.

If Microsoft blocks browser automation, authentication, GitHub connector authorization, licensing, or CreatePullRequest, return exact blocker and current screen/state. Do not change architecture silently.

## Safety boundary

- Do not disable existing ChatGPT alarms.
- Do not create a new Microsoft tenant/trial.
- Do not purchase or accept paid subscription.
- Do not expand repository scope beyond `puev5691/wellbeing-hq`.
- Do not claim exact old-chat resume.
- This is a non-production bounded E2E.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: передать KOD продолжение активной M365 supervisor Task через Work/Cloud Browser
СТАТУС: assigned_for_work_browser_execution
source: current KOO checkpoint + Resume-First Gate
approval_status: operational_task
responsibility_boundary: KOD configures and verifies bounded E2E; OPERATOR only handles login/MFA/required confirmations
