# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Resume-First current-state для восстановления ARH. Snapshot не является approval, не заменяет fresh GitHub-preflight и не доказывает practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Последний завершённый ARH-owned state/event-lineage commit перед этим refresh: `82d450eb934eced1b603b2358d7e85228ff72ba5`
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
- lifecycle origin commit: `a59ef213629502ecb3b9f480cba78f0bc57bc4f4`;
- active queue origin commit: `4a77f3964c881440ec8853a5b38c2c010736c57e`;
- raw KOO inbox remained unchanged in the pilot-creation commits;
- authority boundaries remain KOO-only, classification-only, no destructive cleanup and no production automation.

ARH preservation audit originally found a bounded completeness gap in immutable provenance and bounded intake cursor. KOO corrected that gap:
- lifecycle append-only correction commit: `e4be520c6a0dd3bc7abd66dda69a32e8265d6b53`;
- active queue reconciliation commit: `184203b19b961d1a233420c9077a7410ec36617a`;
- restored source commit/blob: `1b6aab5e50c759a7027b3c5b370475fe35417eec` / `1f8217d29fcc294178734b303df756113066662a`;
- bounded scan cursor: `d0a8af4e8615eaf5bc93bc6b08c707656fbb813a`;
- reconciliation: `PASS_AFTER_BOUNDED_PRESERVATION_CORRECTION`.

Incoming KOO correction:
- artifact commit: `f5cf774ec90465ae6fb7212db1a03f45e4452582`;
- dispatch commit: `8de433da1abb27b2c8402f2ff70cfe040ec89cf2`;
- ARH inbox locator commit: `8a9694bf030c81628e6ec7bd4518b5cc7a684531`;
- ARH processing receipt: `routes/receipts/KOO__inbox-lifecycle-preservation-correction__ARH.receipt.md`, commit `9007f346a4aefe721f188f39baa4b7c8f24b195c`.

ARH independent re-check result:
- verdict: `PASS_BOUNDED_PRESERVATION_RECHECK`;
- artifact: `entities/archivarius/outbox/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md`;
- artifact commit: `04037d8db16d81c5b84c348273e87558952f270b`;
- artifact blob: `3f55a871361064228254683bad7ea646a34c933a`;
- dispatch commit: `e2976c3ecfc1ba80aa5852b659ee7a1b75dd7a7b`;
- KOO inbox locator commit: `0b65a6e1419e0742bc99e2e0d5d6a6d4f1a97b71`;
- event-lineage commit: `38650d809bdc5f7894bade4f636d4d8ae0eecd7b`.

The original provenance/cursor preservation gap is closed in the bounded KOO-only pilot. Returned ARH verdict remains `dispatched` until exact KOO receipt/processing evidence appears. No canon promotion, production automation, destructive inbox cleanup or authority expansion is inferred.

## KOO parallel-queue supplemental recovery checkpoint

Processed task:
`entities/archivarius/inbox/KOO__parallel-queue-transition-preservation__ARH.md`
source task commit `a188ce174a1af2c5d85a0e39d91486a2ee5afcd8`.

Audit found canonical KOO recovery `6f857ba10e9976a9ca1c2c88df0c8b8a7995b74a` predates the new KOO/KOD/SIS transition identities.

Minimal supplemental preservation checkpoint:
`puev5691/wellbeing-entity-bootstrap@9b2a37c80f99495249a21d3b8e6390a5abd85e85:entities/koo/preservation/parallel-queue-transition-v01`

Fresh immutable readback: `2/2 SHA-256 PASS`.

Preserved status distinctions:
- `WAITING_SHD`: information-entry r2 awaits SHD re-verification;
- `WAITING_OPERATOR`: Telegram Phase1B awaits authorized privilege/execution-path decision;
- `READY / parallel`: recompute from fresh HQ evidence; do not freeze historical ordering;
- `CLOSED`: only terminal subchains; inbox-lifecycle preservation correction is closed, SIS host-gate r3 attempt is closed-with-blocker while parent Telegram remains WAITING_OPERATOR.

Recovery registry update: `82a3222bfef4edb1856e5bda079e3a8eb19c9c74`.

Result:
`entities/archivarius/outbox/ARH__parallel-queue-transition-preservation__KOO.md`
commit `3048012bc667e91c7e220dad206f4973a9507d49`.

Exchange Gate:
- dispatch commit `a97d0aa7bc95cc1abc0919bab4c445c1052089f2`;
- KOO inbox commit `4bbe67e3b323127fcfea8dae6bbaf10d75675da2`;
- exact result receipt: `routes/receipts/ARH__parallel-queue-transition-preservation__KOO.receipt.md`, commit `2a0010303e7fc61d1f4cdd5cdf9f74350a3095d2`;
- KOO processing result: `PASS_SUPPLEMENTAL_RECOVERY_CHECKPOINT_ACCEPTED`;
- sender registry reconciled by ARH commit `fd933596dc3bd3df6cd0b1c76d832a3138028760`;
- event-lineage receipt closure commit `82d450eb934eced1b603b2358d7e85228ff72ba5`.

This checkpoint remains supplemental: canonical KOO recovery was not replaced, current-writer state was not transferred, secrets/credentials were not preserved, and process/candidate artifacts were not promoted to Project Sources.

## ARH anti-regression boundaries

- Raw inbox presence does not prove unprocessed work.
- Receipt does not equal broader approval beyond its exact recorded result.
- Semantic response does not equal route receipt.
- Detector/activation request does not equal Entity processing.
- Candidate/draft/research does not become canon without authority.
- Historical failure is not rewritten by later success.
- Sender registry becomes `received` or `received_and_processed` only from exact matching receipt evidence.
- Canonical recovery preservation PASS does not equal practical replacement initiation.
- ARH does not silently resolve authority/canon conflicts or perform unrelated destructive cleanup.
- Materialized active queue does not become semantic authority over artifacts, receipts, decisions or raw inbox evidence.

## Current open work

1. Start every run with fresh GitHub-preflight and delta classification.
2. Watch returned `ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md` for exact KOO receipt/processing evidence; do not invent receipt or acceptance.
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
ДЛЯ ЧЕГО: синхронизировать current recovery/state после exact KOO receipt closure для parallel-queue preservation результата
СТАТУС: emergency-self-preservation-current
