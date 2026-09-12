# ARH — аварийный snapshot

status: emergency-snapshot-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Verified repository state

- Repository: `puev5691/wellbeing-hq`
- Checked branch: `main`
- Verified prewrite HEAD: `8aaaffc9b5e0b2007f2702a2f450221f3b75eba0`
- Previous snapshot baseline: `4faad5c2a4244d3903e8fff98e366ed35773b36a`
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
- event-lineage explicitly preserves causal ordering: an earlier `activation_failed` / `processing_started: no` event remains failed historical evidence even if a later independent receipt proves `received_and_processed`.
- SHT independently rechecked propagation of these boundaries into this ARH recovery snapshot at repository commit `4faad5c2a4244d3903e8fff98e366ed35773b36a` and classified only that recovery consistency as `CONSISTENCY_PASS`.
- That SHT consistency verification does not prove practical cold-start, unattended activation, exact historical chat resume, Entity Runner integrity/deployment, product-side Work execution, or runtime continuity.

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
purpose: preserve current emergency recovery state and SHT independent consistency verification without promoting recovery consistency into technical activation, cold-start, deployment, runtime or product E2E success
