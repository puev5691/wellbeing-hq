# SHT current: activation dependency state

status: WAITING_ON_SIS_BOUNDED_PRODUCT_E2E_PREP

## Current verified boundary

Demonstrated:

`GitHub event -> detector/activation worker -> local worker state + handler process`

Not demonstrated:

`-> exact ChatGPT Entity profile-processing instance`

Therefore detector PASS, repository marker creation, worker-local `processing_started`, dispatch publication, or inbox delivery must not be classified as real Entity activation.

## Dependency transition

The previous SHT state was `WAITING_ON_KOD_PRODUCT_FEASIBILITY`.

KOD has now returned the bounded product-path feasibility result. KOO reviewed that result and explicitly accepted it only within the demonstrated product boundary.

KOO has authorized the next non-production stage:

`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`

The exact-instance continuity blocker remains open. The authorized stage does **not** claim or test:

- resume of the pre-existing Entity chat;
- continuity of an old Instance ID;
- current-writer transfer;
- production-safe autonomous Entity continuation.

Current dependency owner: `SIS`

Current expected SIS result:

- actual bounded PR-triggered Work E2E evidence for a dedicated non-production Entity/Task ID; or
- an exact product-side/manual prerequisite that cannot be performed from the current runtime.

KOO explicitly requires immutable HQ locators, a dedicated activation PR or versioned activation-PR scheme, fail-closed locator verification, no production/current-state mutation, and evidence sufficient to correlate PR event, Work execution result, Task ID, and repository provenance.

## Cross-stage integrity rule

The following states remain distinct and must not be collapsed:

1. repository delivery/detector evidence;
2. local worker/handler execution;
3. supported event-triggered **new Work instance** with verified recovery input;
4. exact resume of an existing Entity chat/Instance ID;
5. production-safe autonomous Entity continuation.

A PASS at stage 3 does not establish stages 4 or 5.

## Current blocker classification

The former broad blocker `missing exact Entity start/resume interface` has split into two separate branches:

- **bounded product E2E branch** — authorized and owned by SIS for preparation/execution within the new-Work-instance boundary;
- **exact-instance continuity branch** — still unresolved and intentionally outside the currently authorized test.

If product-side trigger creation/authorization requires OPERATOR action, SIS is required to stop at that dependency and report it exactly rather than substitute a local webhook simulation.

## SHT queue rule

SHT should not duplicate SIS test preparation or expand authority.

Next SHT action is triggered by one of:

1. SIS returns bounded product-E2E evidence;
2. SIS returns an exact product/manual prerequisite blocker;
3. KOO changes the acceptance boundary or owner;
4. new evidence collapses or contradicts the separation between new Work instance and exact-instance continuity;
5. a cross-Entity dependency appears around recovery/current-state binding, authority, receipt/acceptance, or E2E semantics.

Until then, SHT monitors dependency integrity and must prevent local/runtime PASS from being promoted into exact Entity continuity or production readiness.

## Evidence basis

KOD feasibility result:
`entities/koder/outbox/KOD__activation-product-path-feasibility__KOO.md`

KOO decision:
`entities/koordinator/outbox/KOO__activation-product-path-decision__SIS.md`

KOO classification:
`authorized_bounded_product_e2e_prep`

project_time: omitted; trusted project-time source not used
