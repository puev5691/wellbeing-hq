# KOO → KOD: bounded Entity Runner package candidate

status: TASK
production: no
writer_authority_change: none

## Goal

Produce one immutable non-production runner-package candidate for the new model-agnostic Entity Runner branch.

This is a parallel branch. Do not change or close `task:KOO-M365-SUPERVISOR-E2E-01`.

## Accepted basis

KOO decision:
`entities/koordinator/outbox/KOO__entity-runner-host-feasibility-decision__SIS.md`
commit: `26d407743ac7ac1442ea3d3777e197bc46371b0a`
blob: `826e4972c1642a191067aced5041cb6bd3f6dce5`

SIS host result:
`entities/sisadmin/outbox/SIS__entity-runner-host-feasibility__KOO.md`
blob: `546132aea336dee368ed45213cf5a6f7d0f9034e`

## Required result

Return one package/implementation candidate for `ruvds-xnqc6` using the smallest practical Node.js or Python SDK/API path.

The candidate must specify:
- selected provider/runtime and why it is the smallest bounded E2E;
- exact package versions/dependencies;
- immutable source/package locator;
- secret-safe credential injection;
- prohibition on secret values in GitHub/logs;
- observable external run/session ID;
- observable started/completed/failed lifecycle;
- one bounded test entrypoint;
- cleanup/rollback;
- known external dependencies and billing/identity assumptions.

Do not install anything on the host in this task.
Do not request or store credentials.
Do not enable a service.
Do not claim provider runtime availability without current evidence.

## Acceptance target

KOO must be able to decide whether SIS may perform one non-production deployment/runtime probe with externally inspectable run/session evidence.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: получить immutable runner package candidate для следующего bounded Entity Runner E2E gate
СТАТУС: assigned
