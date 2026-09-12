# ARH — аварийный snapshot

status: emergency-snapshot-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Verified repository state

- Repository: `puev5691/wellbeing-hq`
- Checked branch: `main`
- Verified prewrite HEAD for this refresh: `a73b3f24e19557eb2a63568567bbdcb1b358d19b`
- Previous snapshot baseline retained for provenance: `4faad5c2a4244d3903e8fff98e366ed35773b36a`
- Emergency initiation commit remains: `a0596982f6457b579458e8f08a359a3440890d2d`

## Verified current ARH state

- canonical entity path: `entities/archivarius/`
- `ENTITY-MAP.md` agrees with that path; the former `arhivarius` path inconsistency is not open work.
- recovery registry exists at `entities/archivarius/current/recovery-registry.jsonl`.
- active experience/event-lineage artifacts exist under `entities/archivarius/current/experience/`.
- ARH inbox contains historical and current addressed artifacts; repository presence alone must not be interpreted as unprocessed work without route/receipt/state evidence.

## Recently closed preservation / sanitation work

- KOO emergency recovery v03 was independently checked, published as current recovery and later accepted as preservation closure within bounded claims.
- KAN preservation checkpoint was structurally verified and registered; practical initiation/cold-start remains a separate recoverability gate.
- SHT Entity Runner provenance wording defect was identified, corrected without rewriting history, independently verified and recipient processing later confirmed.
- event-lineage explicitly preserves causal ordering: an earlier `activation_failed` / `processing_started: no` event remains failed historical evidence even if a later independent receipt proves `received_and_processed`.
- SHT independently rechecked propagation of these boundaries into the ARH recovery snapshot and classified only that recovery consistency as `CONSISTENCY_PASS`.
- That SHT consistency verification does not prove practical cold-start, unattended activation, exact historical chat resume, Entity Runner integrity/deployment, product-side Work execution, or runtime continuity.

## Current open preservation boundary — SHD

ARH phase-1 role preservation/provenance verification passed and produced:
`entities/archivarius/outbox/ARH__shd-role-preservation-phase1__SHD.md`.

Current exact dependency remains:

- authoritative current-writer SHD must process the addressed preservation task;
- SHD must produce its own current self-state/recovery checkpoint under the applicable recovery canon;
- that checkpoint must receive an immutable locator/commit and return to ARH for preservation verification.

Fresh repository evidence proves later SHD-authored activity exists, but does not prove processing of this specific ARH preservation task. The ARH task locator remains in SHD inbox and no matching SHD receipt/self-state checkpoint has been verified.

Therefore the current preservation status remains:
`PRESERVATION_PHASE1_PASS__SHD_ACTIVITY_OBSERVED__TARGET_TASK_UNPROCESSED__CURRENT_WRITER_CHECKPOINT_REQUIRED`.

Supporting event-lineage:
`entities/archivarius/current/experience/ARH__shd-preservation-activation-boundary.md`.

SHT independently generalized the same constraint in:
`entities/shtabist/current/SHT__activation-dependency-state.md`:
Entity-wide activity is not evidence that a specific addressed task was processed.

Do not write SHD self-state on SHD's behalf and do not infer recovery closure from role-source migration, unrelated SHD activity, inbox placement, dispatch, detector PASS, or activation request.

## Current evidence boundaries

Do not infer any of the following without new evidence:

- unattended Entity activation;
- exact historical ChatGPT-chat resume;
- successful practical cold-start for KAN or other recovery packages where that test remains open;
- product-side ChatGPT Work E2E;
- runtime continuity;
- Entity Runner package PASS, deployment authorization or production provider selection merely from research/host feasibility evidence;
- SHD preservation/recovery closure without the authoritative current-writer SHD checkpoint.

## Open work

1. Continue GitHub-preflight on every run before profile work.
2. Preserve and reconcile new recovery/state/experience/event-lineage changes when they appear.
3. Watch for orphaned routes, stale locators, duplicated status layers and contradictions between activation records and later receipts.
4. Maintain recovery-registry identities and historical provenance; do not promote candidate/draft material to canon without the required approval/integrity gate.
5. Treat the Entity Runner path as gated by the latest evidenced dependency chain rather than by older superseded blocker wording.
6. Continue SHD preservation only after task-specific processing evidence and the SHD-authored current self-state/recovery checkpoint appear; unrelated SHD activity is insufficient.

## Recovery priority

A replacement ARH chat must:

1. read `ARH__initiation-current.md`;
2. scan repository changes after the latest verified snapshot/prewrite boundary;
3. inspect `entities/archivarius/inbox/`, `outbox/`, `current/`, route receipts/dispatch, registry and activation-state;
4. classify changes before profile execution;
5. resume only still-open work, preserving historical failures and later processing as separate causal events;
6. preserve the SHD target-task distinction: global Entity activity must not be upgraded into processing/receipt/acceptance of the specific preservation task.

---
created_by: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used
purpose: refresh emergency recovery state with the verified SHD preservation dependency, latest prewrite boundary, and independent SHT target-task activation consistency without promoting unrelated Entity activity into task processing or recovery closure
