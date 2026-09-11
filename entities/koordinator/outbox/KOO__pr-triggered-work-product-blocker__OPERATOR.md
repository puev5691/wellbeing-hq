# KOO → OPERATOR: product-side prerequisite for bounded PR-triggered Work E2E

## Decision

SIS result is accepted only as an exact blocker/preparation result. No E2E PASS, no `processing_started`, no exact Entity/chat resume, and no writer-authority transfer are claimed.

Verified blocker:

`BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`

The next bounded experiment cannot begin until one event-triggered ChatGPT Work task for supported GitHub pull-request activity is created/authorized for repository `puev5691/wellbeing-hq`.

Independent KOO verification against current OpenAI product documentation confirms:
- eligible users can create event-triggered Work tasks for supported GitHub pull-request activity in an authorized github.com repository;
- creation is performed in ChatGPT Work and requires review of Trigger, Condition, Prompt and any required authorization;
- connected-app permissions and approval requirements remain in force.

## Exact immutable evidence

SIS artifact:
- path: `entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md`
- commit: `54a0b4663415b9488acf9ed8149a2206ebe8facf`
- blob: `995a3085bca31445e206ec5cbcb44b1b443ea91c`

Prepared recovery input:
- repository: `puev5691/wellbeing-entity-bootstrap`
- commit: `65ad4394b336ee06723988e0a4f22999c4460212`
- path: `entities/sis/recovery/current`

Bounded test IDs:
- entity_test_id: `ent:SIS-WORK-E2E-01`
- task_id: `task:SIS-WORK-E2E-PR-01`

## One required external step

OPERATOR creates and authorizes one event-triggered Work task for supported pull-request activity in `puev5691/wellbeing-hq`, with a narrow condition for the bounded non-production test, then leaves evidence of the created trigger/task accessible for the next SIS/KOO pass.

Until this prerequisite exists:
- do not create the activation PR merely to manufacture activity;
- do not mutate production/current-state;
- do not grant writer authority;
- do not claim resume of an existing Entity/chat instance.

status: `WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`
from_entity: `KOO`
to_entity: `OPERATOR`
document_type: `external-product-blocker-routing`
project_time: omitted; trusted project-time source not used
