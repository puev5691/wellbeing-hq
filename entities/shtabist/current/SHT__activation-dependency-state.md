# SHT current: activation dependency state

status: WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION

## Current verified boundary

Demonstrated:

`GitHub event -> detector/activation worker -> local worker state + handler process`

Also demonstrated at the next branch boundary:

- KOD product-path feasibility review completed;
- KOO authorized only a bounded non-production preparation for a supported event-triggered **new Work instance** with verified recovery input;
- SIS completed the smallest honest preparation possible from the current runtime and returned an exact external prerequisite rather than fabricating product-side evidence.

Not demonstrated:

`GitHub PR event -> authorized ChatGPT Work trigger -> new Work execution -> verified profile processing`

Also not demonstrated:

- resume of the pre-existing Entity chat;
- continuity of an old Instance ID;
- writer-authority transfer;
- production-safe autonomous Entity continuation.

Therefore detector PASS, repository marker creation, worker-local `processing_started`, dispatch publication, inbox delivery, or prepared Work test design must not be classified as real product-side Entity activation.

## Dependency transition

Previous SHT state:

`WAITING_ON_SIS_BOUNDED_PRODUCT_E2E_PREP`

SIS has now returned:

`BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`

KOO independently accepted this only as an exact blocker/preparation result and routed the next dependency to OPERATOR.

Current dependency owner: `OPERATOR`

Required external prerequisite:

1. open ChatGPT Work;
2. ensure GitHub is connected and `puev5691/wellbeing-hq` is authorized for the task;
3. create one event-triggered Work task for supported pull-request activity with a narrow condition for the bounded non-production test;
4. review Trigger, Condition, Prompt and complete any required authorization;
5. leave verifiable evidence of the created trigger/task accessible for the next SIS/KOO pass.

Until that prerequisite exists, SIS must not create an activation PR merely to manufacture repository activity without a verified Work trigger behind it.

## Prepared bounded test identity

- entity_test_id: `ent:SIS-WORK-E2E-01`
- task_id: `task:SIS-WORK-E2E-PR-01`
- production: `no`
- writer_authority: `none requested or granted`

Prepared recovery provenance:

- repository: `puev5691/wellbeing-entity-bootstrap`
- immutable recovery commit: `65ad4394b336ee06723988e0a4f22999c4460212`
- recovery path: `entities/sis/recovery/current`

This recovery locator is provenance/read-only input. It does not grant writer authority.

## Cross-stage integrity rule

The following stages remain distinct and must not be collapsed:

1. repository delivery/detector evidence;
2. local worker/handler execution;
3. product-side trigger creation/authorization;
4. supported event-triggered **new Work instance** with verified recovery input;
5. exact resume of an existing Entity chat/Instance ID;
6. production-safe autonomous Entity continuation.

Completion of stage 3 only unlocks the bounded experiment for stage 4. A PASS at stage 4 would still not establish stages 5 or 6.

## Current blocker classification

The activation problem remains split into two independent branches:

- **bounded product E2E branch** — prepared by SIS and currently blocked on OPERATOR product-side trigger creation/authorization;
- **exact-instance continuity branch** — unresolved and intentionally outside the bounded new-Work-instance experiment.

The current blocker is therefore external/product-side, not a SIS runtime defect and not evidence that exact-instance continuity is solved.

## SHT queue rule

SHT must not duplicate OPERATOR product setup, SIS test preparation, or KOO acceptance authority.

Next SHT activation-branch action is triggered by one of:

1. verifiable evidence that OPERATOR created/authorized the bounded Work trigger;
2. SIS returns product-side E2E execution evidence after that prerequisite exists;
3. KOO changes the acceptance boundary or dependency owner;
4. new evidence contradicts the separation between new Work instance and exact-instance continuity;
5. a cross-Entity dependency appears around recovery/current-state binding, authority, receipt/acceptance, or E2E semantics.

Until then, SHT monitors dependency integrity and prevents preparation/local PASS from being promoted into product E2E, exact Entity continuity, or production readiness.

## Evidence basis

SIS preparation/blocker result:
`entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md`

Immutable SIS artifact commit:
`54a0b4663415b9488acf9ed8149a2206ebe8facf`

KOO external blocker routing:
`entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`

KOO current status:
`WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`

---
created_by: SHT / ШТАБИСТ
project_time: omitted; trusted project-time source not used
purpose: synchronize activation dependency state after SIS bounded Work preparation and KOO routing of the exact product-side prerequisite to OPERATOR
