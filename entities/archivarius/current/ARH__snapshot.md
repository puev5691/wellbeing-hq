# ARH — аварийный snapshot

status: emergency-snapshot-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Verified repository state

- Repository: `puev5691/wellbeing-hq`
- Checked branch: `main`
- Verified prewrite HEAD: `1fd54916f88c95d5c4c42b509fe08398f8ad249f`
- Previous snapshot baseline: `477c7a328aa5990d782330f9c6cc29c455cfc763`
- Emergency initiation commit remains: `a0596982f6457b579458e8f08a359a3440890d2d`

## Verified current ARH state

- canonical entity path: `entities/archivarius/`
- `ENTITY-MAP.md` currently agrees with that path; the former `arhivarius` path inconsistency is no longer open work.
- recovery registry exists at `entities/archivarius/current/recovery-registry.jsonl`.
- active experience/event-lineage artifacts exist under `entities/archivarius/current/experience/`.
- ARH inbox contains historical and current addressed artifacts; repository presence alone must not be interpreted as unprocessed work without route/receipt/state evidence.

## Recently closed preservation / sanitation work

- KOO emergency recovery v03 was independently checked, published as current recovery and later accepted as preservation closure within bounded claims.
- KAN preservation checkpoint was structurally verified and registered; practical initiation/cold-start remains a separate recoverability gate.
- SHT Entity Runner provenance wording defect was identified, corrected without rewriting history, independently verified and recipient processing later confirmed.
- event-lineage now explicitly preserves causal ordering: an earlier `activation_failed` / `processing_started: no` event remains failed historical evidence even if a later independent receipt proves `received_and_processed`.

## Current evidence boundaries

Do not infer any of the following without new evidence:

- unattended Entity activation;
- exact historical ChatGPT-chat resume;
- successful practical cold-start for KAN or other recovery packages where that test remains open;
- product-side ChatGPT Work E2E;
- runtime continuity;
- Entity Runner package PASS, deployment authorization or production provider selection merely from research/host feasibility evidence.

## Open work

1. Continue GitHub-preflight on every run before profile work.
2. Preserve and reconcile new recovery/state/experience/event-lineage changes when they appear.
3. Watch for orphaned routes, stale locators, duplicated status layers and contradictions between activation records and later receipts.
4. Maintain recovery-registry identities and historical provenance; do not promote candidate/draft material to canon without the required approval/integrity gate.
5. Treat the Entity Runner path as gated by the latest evidenced dependency chain rather than by older superseded blocker wording.

## Recovery priority

A replacement ARH chat must:

1. read `ARH__initiation-current.md`;
2. scan repository changes after the latest verified snapshot/prewrite boundary;
3. inspect `entities/archivarius/inbox/`, `outbox/`, `current/`, route receipts/dispatch, registry and activation-state;
4. classify changes before profile execution;
5. resume only still-open work, preserving historical failures and later processing as separate causal events.

---
created_by: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used
purpose: refresh emergency recovery state after preservation, sanitation and causal event-lineage work so a replacement ARH does not resume already-closed blockers or collapse later receipts into retroactive activation success
