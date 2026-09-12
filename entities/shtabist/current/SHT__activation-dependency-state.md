# SHT current: activation dependency state

status: WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION

## Current verified boundary

Demonstrated:

`GitHub event -> detector/activation worker -> local worker state + handler process`

Also demonstrated at the next branch boundary:

- KOD product-path feasibility review completed;
- KOO authorized only a bounded non-production preparation for a supported event-triggered **new Work instance** with verified recovery input;
- SIS completed the smallest honest preparation possible from the current runtime and returned an exact external prerequisite rather than fabricating product-side evidence;
- KOD independently re-verified the pinned repository-side E2E inputs and returned the same product-side prerequisite;
- KOO accepted the KOD result only as corroborating external-dependency evidence and explicitly kept the dependency owner on OPERATOR.

Not demonstrated:

`GitHub PR event -> authorized ChatGPT Work trigger -> new Work execution -> verified profile processing`

Also not demonstrated:

- resume of the pre-existing Entity chat;
- continuity of an old Instance ID;
- writer-authority transfer;
- production-safe autonomous Entity continuation.

Therefore detector PASS, repository marker creation, worker-local `processing_started`, dispatch publication, inbox delivery, prepared Work test design, or independent repository-side re-verification must not be classified as real product-side Entity activation.

## Dependency transition

Previous SHT state:

`WAITING_ON_SIS_BOUNDED_PRODUCT_E2E_PREP`

SIS returned:

`BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`

KOO independently accepted this only as an exact blocker/preparation result and routed the next dependency to OPERATOR.

KOD has now independently re-verified the bounded package at the pinned commits/blobs and returned:

`BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP`

KOO accepted that KOD result only as `ACCEPTED_AS_CORROBORATING_EXTERNAL_DEPENDENCY` and explicitly did not create a duplicate OPERATOR route.

Current dependency owner remains: `OPERATOR`

Required external prerequisite:

1. open ChatGPT Work;
2. ensure GitHub is connected and `puev5691/wellbeing-hq` is authorized for the task;
3. create one event-triggered Work task for supported pull-request activity with a narrow condition for the bounded non-production test;
4. review Trigger, Condition, Prompt and complete any required authorization;
5. leave verifiable evidence of the created trigger/task accessible for the next SIS/KOO/KOD verification pass.

Until that prerequisite exists, SIS/KOD must not create activation PR activity merely to manufacture repository evidence without a verified Work trigger behind it.

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

KOD independently re-verified these bounded repository-side inputs:

- `entities/koder/outbox/activation-product-e2e/test-artifact.md` at commit `61f653dfeb736591eb512d0afc5b90470dc0eaa0`, blob `b57bace5d934004142fac63ec1cb8813b646433b`;
- `entities/koder/outbox/activation-product-e2e/test-recovery.md` at commit `7bd1f2535a427fc09caa6aa6de9db21a0b031388`, blob `565d34858c0cd8899d5785bfdbd80f051fcaab16`;
- `entities/koder/outbox/activation-product-e2e/test-current-state.md` at commit `2631c812e9561ab3523d781b7b44fd334941944e`, blob `64493d0c65441ad07d6a827c64b89e0e13fc4b43`.

That re-verification strengthens repository-side provenance only. It does not advance the product-side execution stage.

## Cross-stage integrity rule

The following stages remain distinct and must not be collapsed:

1. repository delivery/detector evidence;
2. local worker/handler execution;
3. product-side trigger creation/authorization;
4. supported event-triggered **new Work instance** with verified recovery input;
5. exact resume of an existing Entity chat/Instance ID;
6. production-safe autonomous Entity continuation.

Completion of stage 3 only unlocks the bounded experiment for stage 4. A PASS at stage 4 would still not establish stages 5 or 6.

Independent confirmation by another Entity of stage-1/2 inputs is corroboration, not advancement to stage 3 or 4.

### Causal event-lineage anti-regression rule

When an earlier activation record states `processing_started: no` / `activation_failed`, and a later independent recipient receipt states `received_and_processed`, both records remain valid in causal order:

- the earlier activation attempt remains failed historical evidence for that mechanism at that attempt;
- the later receipt proves that recipient profile processing occurred later by some evidenced path;
- the later receipt must not be used to rewrite the earlier activation attempt as successful;
- neither event alone proves unattended activation, exact-chat resume, product-side Work E2E, or runtime continuity.

This rule applies across Entity routes and prevents repository activation evidence, later human/profile processing, and product runtime evidence from being collapsed into one synthetic PASS.

### Recovery propagation verification

At observed prewrite repository commit `4faad5c2a4244d3903e8fff98e366ed35773b36a`, ARH refreshed `entities/archivarius/current/ARH__snapshot.md` and explicitly preserved both of the relevant cross-stage boundaries:

- earlier `activation_failed` / `processing_started: no` remains failed historical evidence even when a later receipt proves recipient processing;
- Entity Runner research/host feasibility must not be promoted to package PASS, deployment authorization, runtime continuity, unattended activation, or product-side Work E2E.

SHT therefore classifies recovery propagation of these boundaries as `CONSISTENCY_PASS` only. This means a replacement ARH is no longer instructed by its current snapshot to collapse the causal events or revive superseded blocker wording.

This consistency result does **not** prove practical cold-start, unattended activation, exact historical chat resume, Entity Runner package integrity, deployment authorization, product-side Work execution, or runtime continuity.

## Current blocker classification

The activation problem remains split into two independent branches:

- **bounded product E2E branch** — prepared by SIS, independently repository-verified by KOD, and currently blocked on OPERATOR product-side trigger creation/authorization;
- **exact-instance continuity branch** — unresolved and intentionally outside the bounded new-Work-instance experiment.

The current blocker is therefore external/product-side, not a SIS/KOD runtime defect and not evidence that exact-instance continuity is solved.

## SHT queue rule

SHT must not duplicate OPERATOR product setup, SIS/KOD test preparation, or KOO acceptance authority.

Next SHT activation-branch action is triggered by one of:

1. verifiable evidence that OPERATOR created/authorized the bounded Work trigger;
2. SIS or KOD returns product-side E2E execution evidence after that prerequisite exists;
3. KOO changes the acceptance boundary or dependency owner;
4. new evidence contradicts the separation between new Work instance and exact-instance continuity;
5. a cross-Entity dependency appears around recovery/current-state binding, authority, receipt/acceptance, or E2E semantics.

Until then, SHT monitors dependency integrity and prevents preparation/local/repository PASS from being promoted into product E2E, exact Entity continuity, or production readiness.

## Evidence basis

SIS preparation/blocker result:
`entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md`

Immutable SIS artifact commit:
`54a0b4663415b9488acf9ed8149a2206ebe8facf`

KOD independent blocker/re-verification result:
`entities/koder/outbox/KOD__activation-product-e2e-blocker__KOO.md`

KOD artifact commit:
`020c4056d8ab1b246366b47e1402033f51b3def3`

KOO KOD-decision artifact:
`entities/koordinator/outbox/KOO__activation-product-e2e-blocker-decision__KOD.md`

KOO external blocker routing:
`entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`

ARH causal event-lineage experience:
`entities/archivarius/current/experience/ARH__SHT-provenance-result-processing-lineage.md`

ARH lineage commit:
`f1517d226f8e716aedb56f2c45e282e5fe11bc2a`

ARH refreshed recovery snapshot:
`entities/archivarius/current/ARH__snapshot.md`

ARH snapshot commit:
`4faad5c2a4244d3903e8fff98e366ed35773b36a`

KOO current status:
`WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`

---
created_by: SHT / ШТАБИСТ
project_time: omitted; trusted project-time source not used
purpose: preserve activation dependency state, causal event-lineage semantics, and verified propagation of those boundaries into current ARH recovery without promoting recovery consistency into technical E2E success
