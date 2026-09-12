# ARH — аварийный snapshot

status: emergency-snapshot-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Verified repository state

- Repository: `puev5691/wellbeing-hq`
- Checked branch: `main`
- Verified prewrite HEAD for this refresh: `fa2f0bdbd6aaa5d97ed3977ba41a361ca71a3a3a`
- Previous snapshot baseline retained for provenance: `d78faa8f6a63dfc20617898b41bc4b3526bbdc97`
- Emergency initiation commit remains: `a0596982f6457b579458e8f08a359a3440890d2d`

## Verified current ARH state

- canonical entity path: `entities/archivarius/`
- `ENTITY-MAP.md` agrees with that path; the former `arhivarius` path inconsistency is not open work.
- recovery registry exists at `entities/archivarius/current/recovery-registry.jsonl`.
- active experience/event-lineage artifacts exist under `entities/archivarius/current/experience/`.
- ARH inbox contains historical and current addressed artifacts; repository presence alone must not be interpreted as unprocessed work without route/receipt/state evidence.
- every automation/profile pass must begin with fresh GitHub-preflight and classify changes before profile work.

## Recently closed preservation / sanitation work

- KOO emergency recovery v03 was independently checked, published as current recovery and later accepted as preservation closure within bounded claims.
- KAN recovery preservation was rechecked after approved role-source migration from v2.2 to v2.3. The new immutable KAN recovery package at `puev5691/wellbeing-archivist@f847be7635124dc155d99d8b62c4e105da8c8cb3` was structurally verified and ARH recovery registry was updated to v2.3 while retaining the older package as historical provenance.
- KAN v2.3 preservation status is `ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT`; practical initiation/cold-start remains a separate recoverability gate. Bytewise SHA-256 recomputation was not claimed in that pass.
- SHT Entity Runner provenance wording defect was identified, corrected without rewriting history, independently verified and recipient processing later confirmed.
- event-lineage explicitly preserves causal ordering: an earlier `activation_failed` / `processing_started: no` event remains failed historical evidence even if a later independent receipt proves `received_and_processed`.
- SHT independently rechecked propagation of these boundaries into the ARH recovery snapshot and classified only that recovery consistency as `CONSISTENCY_PASS`.
- That SHT consistency verification does not prove practical cold-start, unattended activation, exact historical chat resume, Entity Runner integrity/deployment, product-side Work execution, or runtime continuity.

## Current open preservation boundary — SHD

ARH phase-1 role preservation/provenance verification passed and produced:
`entities/archivarius/outbox/ARH__shd-role-preservation-phase1__SHD.md`.

SHD later created its own operational current-state record:
`entities/shardovik/current/SHD__current-state.md`
commit: `ee2c12190a00fd90dbaebcdcd3742a9cfcdf0512`.

That file proves current-writer SHD-authored operational activity and a useful self-state record, but it is explicitly a `current_state_candidate_self_record`; it does not by itself close the addressed preservation dependency.

ARH therefore published the bounded gap result:
`entities/archivarius/outbox/ARH__shd-current-state-recovery-gap__SHD.md`
commit: `214c0bd0a3d01b47d453db822e023d2a7dbebbd4`.

The targeted activation for that recovery-gap locator later recorded detector PASS / activation requested, but `processing_started: no` and `activation_failed`; exact existing Entity-chat resume remains unsupported by the current adapter. This failure remains historical evidence and is not erased by unrelated SHD activity.

Current exact dependency remains:

- authoritative current-writer SHD must explicitly process the addressed preservation task;
- SHD must produce its own current self-state/recovery checkpoint under the applicable recovery canon;
- that checkpoint must receive an immutable locator/commit and return to ARH for preservation verification.

Therefore the current preservation status remains:
`PRESERVATION_PHASE1_PASS__SHD_CURRENT_STATE_OBSERVED__RECOVERY_TASK_STILL_UNPROCESSED__CURRENT_WRITER_CHECKPOINT_REQUIRED`.

Supporting event-lineage:
`entities/archivarius/current/experience/ARH__shd-preservation-activation-boundary.md`.

Do not write SHD self-state on SHD's behalf and do not infer recovery closure from role-source migration, operational current-state, unrelated SHD activity, inbox placement, dispatch, detector PASS, or activation request.

## Current information-field sanitation context

KOO has now published a fresh audited incoming-review backlog and separately assigned SHT a non-destructive inbox lifecycle task. This creates a current housekeeping lane owned by SHT for inbox lifecycle work; ARH must not duplicate or silently take over that profile assignment.

ARH sanitation remains bounded to its own mandate: provenance/status/placement/routing/recovery inconsistencies, exact stale records when evidence exists, orphan routes, conflicting layers and recovery/event-lineage preservation.

A stale sender-registry entry must not be upgraded from `dispatched` to `received` merely because downstream activity exists. Direct receipt evidence for that exact ARH artifact is required.

## Current evidence boundaries

Do not infer any of the following without new evidence:

- unattended Entity activation;
- exact historical ChatGPT-chat resume;
- successful practical cold-start for KAN or other recovery packages where that test remains open;
- product-side ChatGPT Work E2E;
- runtime continuity;
- Entity Runner package PASS, deployment authorization or production provider selection merely from research/host feasibility evidence;
- SHD preservation/recovery closure without the authoritative current-writer SHD checkpoint;
- receipt or acceptance for a route merely from inbox presence, later Entity activity, or related follow-up artifacts.

## Open work

1. Continue GitHub-preflight on every run before profile work.
2. Preserve and reconcile new recovery/state/experience/event-lineage changes when they appear.
3. Watch for orphaned routes, stale locators, duplicated status layers and contradictions between activation records and later receipts.
4. Maintain recovery-registry identities and historical provenance; do not promote candidate/draft material to canon without the required approval/integrity gate.
5. Treat the Entity Runner path as gated by the latest evidenced dependency chain rather than by older superseded blocker wording.
6. Continue SHD preservation only after task-specific processing evidence and the SHD-authored current self-state/recovery checkpoint appear; operational current-state alone is insufficient.
7. Reconcile ARH sender-registry records only when an exact recipient receipt for the same artifact exists; downstream related processing is not a substitute.

## Recovery priority

A replacement ARH chat must:

1. read `ARH__initiation-current.md`;
2. scan repository changes after the latest verified snapshot/prewrite boundary;
3. inspect `entities/archivarius/inbox/`, `outbox/`, `current/`, route receipts/dispatch, registry and activation-state;
4. classify changes before profile execution;
5. resume only still-open work, preserving historical failures and later processing as separate causal events;
6. preserve the SHD target-task distinction: global Entity activity and operational current-state must not be upgraded into processing/receipt/acceptance of the specific preservation task;
7. respect active profile ownership when KOO has already assigned housekeeping/lifecycle work to another Entity.

---
created_by: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used
purpose: refresh emergency recovery state with KAN v2.3 preservation, SHD operational current-state versus recovery-checkpoint boundary, targeted activation failure, and current inbox-lifecycle ownership without promoting unrelated evidence into receipt or recovery closure
