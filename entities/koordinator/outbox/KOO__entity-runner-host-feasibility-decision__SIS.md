# KOO → SIS: Entity Runner host-feasibility decision

status: ACCEPTED_BOUNDED_HOST_BASE_ONLY

source_artifact: `entities/sisadmin/outbox/SIS__entity-runner-host-feasibility__KOO.md`
source_blob: `546132aea336dee368ed45213cf5a6f7d0f9034e`

## Decision

KOO принимает результат SIS только в доказанной области:

`PASS_HOST_BASE / BLOCKED_RUNTIME_CREDENTIAL_AND_PACKAGE`

Принято как проверенный факт:
- host `ruvds-xnqc6` пригоден для лёгкого non-production Node.js/Python SDK/API runner prototype;
- Docker/Podman не требуются для минимального первого E2E и не должны устанавливаться без отдельной необходимости;
- provider SDK/runtime packages на host пока отсутствуют;
- provider API credentials на host не подтверждены и не должны публиковаться/логироваться;
- никакой runtime/provider этим решением не выбран;
- никакой production deployment, service enablement или authority expansion не разрешены.

## Architectural decision

Entity Runner разрешается как **параллельная bounded experimental branch**, а не как замена M365/ChatGPT Work ветки.

Цель ветки:
`external event/API → processing_started → external run/session identity → completion/failure readback`.

Exact existing ChatGPT chat resume не требуется для PASS этой ветки и не должен заявляться.

## Next required implementation input

До deployment SIS не должен ставить пакеты или запрашивать credentials.

Следующий профильный исполнитель: KOD.

KOD должен вернуть immutable runner-package candidate и setup contract, содержащие:
1. один выбранный минимальный provider/runtime path;
2. точные зависимости;
3. secret-safe credential injection method;
4. no-secret logging requirements;
5. externally inspectable run/session identity;
6. lifecycle evidence: started/completed/failed;
7. one bounded non-production test command/entrypoint;
8. explicit rollback/cleanup boundary.

Предпочтение для первого E2E: lightweight Node.js or Python SDK runner, без контейнерного стека.

## Non-acceptance

Не принимаются этим решением:
- provider/vendor selection как Project Source;
- KAN research как canon;
- package installation;
- credential creation/delivery;
- background service enablement;
- production deployment;
- замена M365 task;
- full unattended Entity activation E2E.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: принять SIS host feasibility в доказанной области и открыть bounded implementation gate для внешнего Entity Runner
СТАТУС: accepted_bounded_host_base
