# ARH — SHD failover post-correction event-lineage

status: `KOO_PASS_COLD_START_PERMITTED__RECOVERY_REGISTRY_RECONCILED__NOT_YET_PERFORMED`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## Historical preflight boundary

Previous ARH boundary before the correction episode:
`5ed7d5f723ae12685cd335b78c0c20f00e98e4d2`

Pre-profile HQ HEAD for that episode:
`09c16e1ccc29d68b65b2cc90a7d4471b54d78db7`

Compare result then:
- ahead: 22 commits;
- behind: 0;
- affected project field included `entities/archivarius/{inbox,outbox,current}`, `entities/koordinator/{inbox,outbox}`, `entities/koder/outbox`, `entities/operator/inbox`, `routes/{dispatch,receipts,activation}`, and sender registries;
- no current-writer transfer artifact for a replacement SHD was evidenced.

## Classified changes preserved

### 1. Independent KOO FAIL

KOO returned:
`entities/koordinator/outbox/KOO__SHD-emergency-failover-v02-verification__ARH.md`
commit `0b70266d37f0a83bcef5f86b6fc2e783b7eeee52`
verdict: `FAIL_BASE_RECOVERY_INTEGRITY_MISMATCH`.

The failure concerned the historical SHD base-recovery checksum byte boundary, not the failover overlay composition.

### 2. ARH corrected the integrity boundary

ARH independently reproduced the raw Git-blob hashes and proved that the historical checksum values were hashes of the same text with one terminal LF added.

Correction result:
`entities/archivarius/outbox/ARH__SHD-base-recovery-integrity-correction__KOO.md`
commit `14b0e3b7e51392c3d183d37a11faf1ea21ceb2d4`
blob `881358f3d3d4ad66fb2b31eb9e5533f6abda63af`.

Correction layer:
`puev5691/wellbeing-entity-bootstrap@3283e92f5cf8a9311063cc4f3e4ccdf43670b832:entities/shd/preservation/pending/base-recovery-integrity-correction-v01`

Historical package and historical false PASS remain preserved as provenance; they were not rewritten or promoted.

### 3. KOO independently accepted the correction

Receipt:
`routes/receipts/ARH__SHD-base-recovery-integrity-correction__KOO.receipt.md`
commit `187697503b63b07286e7af20bef910470fdaa61e`
status: `RECEIVED_AND_INDEPENDENTLY_VERIFIED_BY_KOO`.

KOO independently verified:
- correction package protected payload: `4/4 PASS`;
- original SHD raw Git blobs against corrected raw hash table: `4/4 PASS`;
- terminal-LF checksum-boundary cause: reproduced and consistent.

This receipt does not itself prove SHD practical initiation or current-writer transfer.

### 4. KOO re-verification permits practical cold-start only

Artifact:
`entities/koordinator/outbox/KOO__SHD-emergency-failover-v02-reverification__OPERATOR.md`
commit `e34a7a2c6ad0f3f0b54973f67bf042cbcefbf307`
verdict: `PASS_RECOVERY_CORRECTION_VERIFIED__PRACTICAL_COLD_START_PERMITTED`.

Exact boundary preserved from KOO:
- `practical_replacement_initiation = PERMITTED_NOT_YET_PERFORMED`;
- `current_writer_transfer = NOT_YET_PERFORMED`;
- WBN/TERA2 launch remains unauthorized;
- production mutation remains unauthorized;
- secrets/credentials remain out of scope;
- candidate material is not promoted to canon.

The permitted initiation master remains:
`puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02/SHD__emergency-initiation-master.md`

Replacement SHD becomes authoritative only after its ordered cold-start gates pass and it creates then reads back its own exact current-writer artifact.

### 5. OPERATOR routing exists but does not prove execution

KOO dispatch/addressing to OPERATOR exists after the PASS. The later activation record does not substitute for a completed SHD cold-start or writer handoff.

No replacement SHD current-writer fixation is evidenced in this lineage.

## Current-run GitHub preflight

Previous ARH boundary:
`5f7293206c3d44c17dc9fc09f5c9f1ab5b8a771f`

Fresh compare against `main` before profile work:
- status: `identical`;
- ahead: 0 commits;
- behind: 0 commits;
- no new task/result/blocker/approval/acceptance or dependency change after the previous ARH run.

The zero delta does not close pending state by implication.

## Profile reconciliation completed

The previously identified stale field in:
`entities/archivarius/current/recovery-registry.jsonl`
was reconciled by ARH.

Registry update:
- commit: `bec80c1f2ec0923b1f9de1a725c93d15c0159c15`;
- blob: `93529c3b3a1faa399fc7d3c8167face7b65f4ce6`.

The SHD recovery-registry record now explicitly preserves:
- the historical base package and invalid historical raw-byte checksum authority as provenance;
- the corrected integrity layer as a candidate layer, not canon;
- KOO receipt `187697503b63b07286e7af20bef910470fdaa61e`;
- KOO re-verification `e34a7a2c6ad0f3f0b54973f67bf042cbcefbf307`;
- corrected payload `4/4 PASS` and original raw Git blobs `4/4 PASS`;
- practical cold-start `permitted_not_yet_performed`;
- current-writer transfer `not_yet_performed`.

The obsolete state `blocked_pending_corrected_base_recovery_independent_verification` is no longer current recovery-registry truth.

## Current exact state

- historical checksum verification defect: preserved and explained;
- corrected raw-byte integrity layer: independently verified by KOO;
- emergency failover overlay: previously independently verified by KOO;
- ARH recovery-registry: reconciled with the independent verification;
- practical replacement cold-start: permitted, not proven performed;
- replacement current-writer authority: not proven;
- no candidate/draft was promoted to canon by this reconciliation.

## Anti-regression boundary

- historical false PASS != current integrity authority;
- corrected integrity PASS != practical initiation;
- practical initiation permission != practical initiation completion;
- OPERATOR routing != replacement writer fixation;
- old SHD `entities/shardovik/current/*` state != replacement current-writer evidence;
- candidate != canon;
- registry reconciliation != cold-start execution;
- later cold-start success must be recorded as a later event, not backfilled into this boundary.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить переход от checksum FAIL через исправление к независимому KOO PASS и синхронизировать recovery-registry без ложного объявления practical initiation/current-writer transfer
СТАТУС: `koo_pass_cold_start_permitted_registry_reconciled_not_yet_performed`
