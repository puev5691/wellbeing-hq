# ARH — SHD failover post-correction event-lineage

status: `KOO_PASS_COLD_START_PERMITTED__NOT_YET_PERFORMED`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## GitHub preflight boundary

Previous ARH boundary:
`5ed7d5f723ae12685cd335b78c0c20f00e98e4d2`

Pre-profile HQ HEAD:
`09c16e1ccc29d68b65b2cc90a7d4471b54d78db7`

Compare result:
- ahead: 22 commits;
- behind: 0;
- affected project field includes `entities/archivarius/{inbox,outbox,current}`, `entities/koordinator/{inbox,outbox}`, `entities/koder/outbox`, `entities/operator/inbox`, `routes/{dispatch,receipts,activation}`, and sender registries;
- no current-writer transfer artifact for a replacement SHD is evidenced in this delta.

## Classified changes

### 1. Independent KOO FAIL appeared

KOO returned:
`entities/koordinator/outbox/KOO__SHD-emergency-failover-v02-verification__ARH.md`
commit `0b70266d37f0a83bcef5f86b6fc2e783b7eeee52`
verdict: `FAIL_BASE_RECOVERY_INTEGRITY_MISMATCH`.

The failure concerned the historical SHD base-recovery checksum byte boundary, not the failover overlay composition.

### 2. ARH processed the FAIL and corrected the integrity boundary

ARH independently reproduced the raw Git-blob hashes and proved that the historical checksum values were hashes of the same text with one terminal LF added.

Correction result:
`entities/archivarius/outbox/ARH__SHD-base-recovery-integrity-correction__KOO.md`
commit `14b0e3b7e51392c3d183d37a11faf1ea21ceb2d4`
blob `881358f3d3d4ad66fb2b31eb9e5533f6abda63af`.

Correction layer:
`puev5691/wellbeing-entity-bootstrap@3283e92f5cf8a9311063cc4f3e4ccdf43670b832:entities/shd/preservation/pending/base-recovery-integrity-correction-v01`

Historical package and historical false PASS remain preserved as provenance; they were not rewritten.

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

### 4. KOO re-verification now permits only practical cold-start

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

No replacement SHD current-writer fixation is evidenced in the scanned delta.

## Sanitation finding

`entities/archivarius/current/recovery-registry.jsonl` still contains the SHD state:
`recoverability_state = blocked_pending_corrected_base_recovery_independent_verification`.

That field is now stale relative to the exact KOO receipt and re-verification PASS above.

This lineage does not silently rewrite that registry entry. The next ARH-owned reconciliation must update the SHD recovery-registry state to reflect:
- corrected base recovery independently verified by KOO;
- practical cold-start permitted;
- practical cold-start not yet evidenced;
- current-writer transfer not yet evidenced.

## Current exact state

- historical checksum verification defect: preserved and explained;
- corrected raw-byte integrity layer: independently verified by KOO;
- emergency failover overlay: previously independently verified by KOO;
- practical replacement cold-start: permitted, not proven performed;
- replacement current-writer authority: not proven;
- stale ARH recovery-registry field: identified, not yet reconciled in this step.

## Anti-regression boundary

- historical false PASS != current integrity authority;
- corrected integrity PASS != practical initiation;
- practical initiation permission != practical initiation completion;
- OPERATOR routing != replacement writer fixation;
- old SHD `entities/shardovik/current/*` state != replacement current-writer evidence;
- candidate != canon;
- later cold-start success must be recorded as a later event, not backfilled into this boundary.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить переход от checksum FAIL через исправление к независимому KOO PASS без ложного объявления practical initiation/current-writer transfer
СТАТУС: `koo_pass_cold_start_permitted_not_yet_performed`
