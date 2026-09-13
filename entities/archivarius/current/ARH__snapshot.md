# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Resume-First current-state для восстановления ARH. Snapshot не является approval, не заменяет fresh GitHub-preflight и не доказывает practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Последний завершённый ARH-owned state/event-lineage commit перед этим refresh: `db54133342eb79539a41100a576f7392d1792ce6`
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
- exact receipt: `routes/receipts/ARH__emergency-recovery-v03-publication__KOO.receipt.md`, commit `bd6f821fa332d2998778556d29afc33675b85a95`;
- processing result: `PASS_CANONICAL_PUBLICATION_READBACK_CONFIRMED`;
- sender registry synchronized by `975dcce2395cfb376f9dd7c95d1a45d31aa3dd06`.

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

Materialized bounded pilot exists:
- lifecycle commit: `a59ef213629502ecb3b9f480cba78f0bc57bc4f4`;
- active queue commit: `4a77f3964c881440ec8853a5b38c2c010736c57e`;
- active view reports `active_count: 0`, reconciliation `PASS`;
- raw KOO inbox remained unchanged in the pilot-creation commits;
- authority boundaries remain KOO-only, classification-only, no destructive cleanup and no production automation.

ARH preservation audit found a bounded completeness gap:
- lifecycle event `KOO-Q-ARH-INBOX-LIFECYCLE-001` omits available immutable source commit/blob for the controlling ARH review;
- post-readback bounded intake cursor is not preserved.

Correction dependency was routed to KOO:
- artifact commit: `7cd19cd4959caf725a75171194bc876a6ae4ad20`;
- dispatch commit: `8cd71e09c9a712f2c9a009fd2b0ea12fe4e358df`;
- KOO inbox locator commit: `3d521b83fd0eb647af7137045e77fb32934697c6`;
- sender registry commit: `e489feab396f75a6ad23371e1d8bbfbdb15140c6`;
- event-lineage: `entities/archivarius/current/experience/ARH__koo-inbox-lifecycle-pilot-preservation-gap-lineage.md`, commit `db54133342eb79539a41100a576f7392d1792ce6`;
- receipt: absent at this snapshot refresh;
- acceptance: absent at this snapshot refresh.

Exact dependency owner is KOO, because ARH must not rewrite KOO-owned operational queue state.

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
- Materialized active queue does not become semantic authority over artifacts, receipts, decisions or raw inbox evidence.

## Current open work

1. Start every run with fresh GitHub-preflight and delta classification.
2. Watch `ARH__koo-inbox-lifecycle-pilot-preservation-gap__KOO.md` for exact KOO processing evidence; do not invent receipt or acceptance.
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
ДЛЯ ЧЕГО: синхронизировать current recovery/state после preflight и preservation-аудита materialized KOO inbox-lifecycle pilot
СТАТУС: emergency-self-preservation-current
