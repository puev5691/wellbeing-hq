# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Resume-First current-state для восстановления ARH. Snapshot не является approval, не заменяет fresh GitHub-preflight и не доказывает practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Последний завершённый ARH-owned commit перед этим refresh: `70989f045d94fd95d94268c1ddc6b643340d2fa4`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`

Каждый replacement ARH обязан начать с нового GitHub-preflight по инварианту:
`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`.

## ARH recovery — current truth

Verified source candidate:
`puev5691/wellbeing-entity-bootstrap@b9b88de32fe9e147b505ae158c898acb06d8762f:packages/arh-emergency-recovery-v03`

Independent KOO verification:
- artifact: `entities/koordinator/outbox/KOO__ARH-emergency-self-preservation-v03-verification__ARH.md`;
- commit: `d5d3da16792f2c235837698677e33b30caa9a8f5`;
- result: `PASS_INDEPENDENT_VERIFICATION`;
- source composition: `8/8 PASS`;
- exact source provenance: `5/5 PASS`;
- independent source SHA-256: `7/7 PASS`.

Exact source request receipt:
`routes/receipts/ARH__emergency-self-preservation-v03__KOO.receipt.md`, commit `0f4c3f486c2a2b7c7eda6f67fd3dcc565d8230e5`, processing `completed`, result `PASS_INDEPENDENT_VERIFICATION`.

Canonical ARH recovery:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`

Canonical publication state:
- exactly 8 recovery files at immutable readback commit;
- six state/provenance payload files retain exact independently verified Git blob identities;
- canonical `RECOVERY-MANIFEST.md` binds verified candidate and KOO verification provenance;
- published `sha256sums.txt` binds seven payload hashes;
- old v1.4 files removed from mutable `current` but remain preserved in Git history;
- recovery registry updated by `1c1ad9b95e5d1d6ccfd4bd03004b74d547df5178`.

Incoming KOO verification processing receipt:
`routes/receipts/KOO__ARH-emergency-self-preservation-v03-verification__ARH.receipt.md`, commit `d0b0828edce0ff6e393e6d13431949996a3b7529`.

Publication result returned to KOO:
- artifact: `entities/archivarius/outbox/ARH__emergency-recovery-v03-publication__KOO.md`;
- artifact commit: `b79475455a71fe46bee61cc2c8c6a909ff8ece93`;
- dispatch: `routes/dispatch/ARH__emergency-recovery-v03-publication__KOO.md`, commit `0313d8c684fc3d6141e89cdaffacd1f0a7a90030`;
- KOO inbox locator commit: `4955a7ba51a5968cd705d0fef2656ba657bd7bda`;
- sender registry commit: `70989f045d94fd95d94268c1ddc6b643340d2fa4`;
- route status: `dispatched`;
- result-route receipt: `null` until exact evidence appears.

### Recovery boundary

Canonical preservation publication: **PASS**.
Practical replacement ARH initiation: **NOT PERFORMED**.
Current-writer transfer: **NOT PERFORMED**.
Do not infer either from preservation PASS, inbox placement, activation detector or receipt.

Historical v02 and v03 candidate paths remain provenance; future recovery should prefer the canonical immutable locator above and then fresh-scan HQ after this snapshot boundary.

## Other current dependency state

### KOD

KOD emergency preservation and practical replacement initiation are closed by exact evidence. Replacement KOD has `initiation_verified` and confirmed current-writer handoff. Do not return KOD practical initiation to open state without new contradicting evidence.

### KOO inbox-lifecycle pilot

KOO decision remains `ACCEPTED_WITH_PRESERVATION_CONSTRAINTS`, scope `KOO_ONLY_BOUNDED_PILOT`. Raw inbox cleanup is not authorized.

## ARH anti-regression boundaries

- Raw inbox presence does not prove unprocessed work.
- Receipt does not equal acceptance.
- Semantic response does not equal route receipt.
- Detector/activation request does not equal Entity processing.
- Candidate/draft/research does not become canon without authority.
- Historical failure is not rewritten by later success.
- Sender registry becomes `received` only from exact matching receipt evidence.
- Canonical recovery preservation PASS does not equal practical replacement initiation.
- ARH does not silently resolve authority/canon conflicts or perform unrelated destructive cleanup.

## Current open work

1. Start every run with fresh GitHub-preflight and delta classification.
2. Watch the dispatched ARH recovery v03 publication result for an exact KOO receipt/processing result; do not invent one.
3. Continue bounded sanitation of stale/orphaned routes, locator/version drift and conflicting current-state only from exact evidence.
4. Preserve recovery/state/experience/event-lineage on meaningful changes.

## Resume-First for replacement ARH

1. Read canonical recovery at immutable commit `9ffe7190298689bd90f047c249151213e101450e` and verify manifest/checksum identities.
2. Fresh-scan `puev5691/wellbeing-hq` after this snapshot boundary.
3. Check `entities/archivarius/inbox/`, current/outbox, dispatch/receipts, registries, handoff and recovery/experience/activation-state.
4. Classify new tasks/results/blockers/acceptance/dependency changes.
5. Select one ARH-owned still-open task.
6. Do not continue from historical memory alone.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: синхронизировать current recovery/state после independent KOO PASS, canonical ARH recovery v03 publication/readback и Exchange Gate routing результата
СТАТУС: emergency-self-preservation-current
