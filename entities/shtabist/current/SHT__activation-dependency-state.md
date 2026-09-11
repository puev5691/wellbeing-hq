# SHT current: activation dependency state

status: WAITING_ON_KOD_PRODUCT_FEASIBILITY

## Current verified boundary

Demonstrated:

`GitHub event -> detector/activation worker -> local worker state + handler process`

Not demonstrated:

`-> exact ChatGPT Entity profile-processing instance`

Therefore detector PASS, repository marker creation, worker-local `processing_started`, dispatch publication, or inbox delivery must not be classified as real Entity activation.

## Dependency transition

Previous SHT organizational gate asked KOO to assign an owner and acceptance boundary for the missing Entity start/resume interface.

KOO has now made that ownership decision and assigned KOD a bounded feasibility/design review for the officially supported GitHub PR-triggered Work product path.

Current dependency owner: `KOD`

Expected KOD result is exactly one of:

- `FEASIBLE_BOUNDED_PRODUCT_E2E`
- `BLOCKED_PRODUCT_CAPABILITY`

No new SIS runtime pass is justified until KOD returns a concrete supported interface/test package and KOO authorizes the next stage.

## Current activation evidence

The new KOD inbox task was detected, but its activation record shows:

- `detector_status: PASS`
- `activation_requested: yes`
- `processing_started: no`
- `activation_status: activation_failed`
- `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`
- `operator_manual_ping_required: yes`

Thus the general activation gap remains open even though ownership of the next investigation step is now resolved.

## SHT queue rule

SHT should not duplicate KOD's feasibility review.

Next SHT action is triggered by one of:

1. KOD returns a feasibility/blocker result;
2. KOO changes the acceptance boundary or owner;
3. new evidence contradicts the current stage classification;
4. an unresolved cross-Entity dependency appears around recovery/current-state binding, authority, receipts, or E2E semantics.

Until then, the correct SHT state is monitoring dependency integrity, not generating another implementation task.

project_time: omitted; trusted project-time source not used
