# ARH — аварийный snapshot

status: emergency-snapshot-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Этот snapshot нужен для Resume-First восстановления ARH. Он фиксирует только проверяемое состояние информационного поля и не заменяет свежий GitHub-preflight.

## Verified repository state

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Latest verified no-delta prewrite boundary before this refresh: `f060d5e979f696f0ac79a540b1ce9a934400e942`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`
- Every activation/profile pass must begin with fresh GitHub-preflight and classification before profile work.

## Current recovery state

### KOO

Emergency recovery v04 was independently verified by ARH and published as current canonical recovery.

Candidate verified:
`puev5691/wellbeing-entity-bootstrap@99ebd990537d3b0405ff0bfcd20fdac91621b077:entities/koo/preservation/pending/emergency-initiation-v04`

Canonical current recovery:
`puev5691/wellbeing-entity-bootstrap@6f857ba10e9976a9ca1c2c88df0c8b8a7995b74a:entities/koo/recovery/current`

ARH result:
`entities/archivarius/outbox/ARH__emergency-recovery-v04-result__KOO.md`
commit: `6d92aa174240fc2875d67b2f1a375d332bda999b`

Verified preservation facts:
- manifest composition: 7/7 objects present;
- bytewise `sha256sum -c sha256sums.txt`: 6/6 PASS on immutable candidate;
- post-publication readback: 6/6 PASS;
- previous canonical `cbaad4cb94618788f5d50664d08d503a3247f61c` retained as historical provenance;
- practical cold-start/runtime continuity is not proven by preservation PASS.

The ARH→KOO result route is dispatched; sender registry must remain `dispatched` until an exact KOO receipt exists. Automatic activation record for the KOO inbox locator recorded `processing_started: no` / `activation_failed`; this is not receipt, processing or acceptance.

### SHD

The previous dependency `current_writer_checkpoint_required` is resolved.

Verified current checkpoint:
`puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:packages/shd-role-v2_3-current-recovery/`

ARH result:
`entities/archivarius/outbox/ARH__shd-role-v2_3-recovery-verification__SHD.md`
commit: `29e0a61e4a79842505a279bd131d25cb64978f5e`

Recovery registry records:
- preservation checkpoint verified;
- immutable readback verified by ARH;
- bytewise SHA-256: 4/4 PASS;
- prior checkpoint dependency resolved;
- practical initiation test remains not performed.

Historical targeted activation failures remain failed historical events and are not rewritten into success merely because the later SHD current-writer checkpoint was obtained and verified.

### KAN

Current recovery remains:
`puev5691/wellbeing-archivist@f847be7635124dc155d99d8b62c4e105da8c8cb3:docs/entities/kancelyariya/recovery-current`

Status remains structurally accepted after v2.2 → v2.3 role-source transition. Practical initiation/cold-start remains separate; bytewise SHA-256 recomputation was not claimed in that preservation pass.

## Current information-field boundaries

- Raw inbox presence is not proof of unprocessed work; route/receipt/current-state evidence must be checked.
- Receipt is not semantic acceptance.
- Detector/activation request is not Entity processing.
- Later successful processing does not retroactively rewrite an earlier activation failure.
- Candidate/draft/research does not become canon without the required decision/integrity gate.
- A stale sender-registry record may move from `dispatched` to `received` only on exact receipt evidence for the same artifact.
- ARH may preserve/check provenance, status, placement, routing, recovery and lineage, but must not silently take over another Entity's assigned queue/lifecycle work.

## Current open work

1. Start every run with GitHub-preflight across inbox/outbox/current, dispatch/receipts, handoff, registry and recovery/experience/activation-state.
2. Preserve new recovery/state/experience/event-lineage changes and keep historical failures causally distinct from later outcomes.
3. Reconcile one concrete stale route/registry/status issue only when exact evidence exists.
4. Watch KOO recovery v04 result route for an exact recipient receipt; do not infer it from manual initiation or later KOO activity.
5. Preserve SHD practical-initiation boundary: preservation PASS is not cold-start PASS.
6. Preserve KAN practical-initiation boundary and the fact that bytewise recomputation was not performed in its v2.3 preservation pass.
7. Do not duplicate lifecycle/housekeeping work already assigned by KOO to another Entity.

## Recovery priority

A replacement ARH instance must:

1. read `ARH__initiation-current.md`;
2. perform fresh `wellbeing-hq` preflight after the latest verified snapshot boundary;
3. inspect `entities/archivarius/inbox/`, `outbox/`, `current/`, dispatch/receipts, registries and activation-state;
4. classify new tasks, results, blockers, approval/acceptance and dependency changes;
5. select exactly one still-open ARH-owned task;
6. verify any write by readback and use Exchange Gate when the result is addressed to another Entity.

---
created_by: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used
purpose: synchronize emergency recovery state after KOO recovery v04 canonical publication and SHD recovery-checkpoint closure while preserving exact cold-start, receipt and activation boundaries
