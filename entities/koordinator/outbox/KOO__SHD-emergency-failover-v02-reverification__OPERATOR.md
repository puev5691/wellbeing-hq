# KOO → OPERATOR: SHD emergency failover v02 re-verification

status: `PASS_RECOVERY_CORRECTION_VERIFIED__PRACTICAL_COLD_START_PERMITTED`
entity: `SHD / ШАРДОВИК`
current_writer_transfer: `NOT_YET_PERFORMED`
practical_replacement_initiation: `PERMITTED_NOT_YET_PERFORMED`
production_mutation: no
secrets_credentials: out_of_scope
project_time: omitted; trusted project-time source not used

## Fresh HQ boundary

Fresh preflight basis for this decision:
`puev5691/wellbeing-hq@53d4c6703a0b2424a17a1fe717068e7636a2b314`.

## Base recovery and correction

Original SHD self-recovery content source remains immutable:
`puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:packages/shd-role-v2_3-current-recovery/`

The old checksum contract in that package is invalid for raw Git blob bytes and must remain only as provenance of the defect.

Corrected integrity layer:
`puev5691/wellbeing-entity-bootstrap@3283e92f5cf8a9311063cc4f3e4ccdf43670b832:entities/shd/preservation/pending/base-recovery-integrity-correction-v01`

KOO independent checks:
- correction directory composition: 5 files PASS;
- correction protected payload SHA-256: `4/4 PASS`;
- original SHD raw Git blobs against `raw-blob-sha256.txt`: `4/4 PASS`;
- terminal-LF cause of the historical false PASS: independently reproduced.

Accepted ARH correction result:
`entities/archivarius/outbox/ARH__SHD-base-recovery-integrity-correction__KOO.md`
commit `14b0e3b7e51392c3d183d37a11faf1ea21ceb2d4`
blob `881358f3d3d4ad66fb2b31eb9e5533f6abda63af`.

KOO receipt:
`routes/receipts/ARH__SHD-base-recovery-integrity-correction__KOO.receipt.md`
commit `187697503b63b07286e7af20bef910470fdaa61e`.

## Emergency overlay

Failover overlay remains:
`puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02`

Previous independent KOO check:
- composition: 7 files PASS;
- protected payload raw SHA-256: `6/6 PASS`;
- overlay is ARH external recovery evidence only and does not replace SHD self-state or expand authority.

## Role, control and writer boundary

Active SHD role remains approved role-source v2.3. PWH/hashchain and other research/process candidates remain candidates, not canon.

KOO control state remains restored for SHD. The OPERATOR explicitly decided to replace the degraded old SHD chat and requested emergency failover verification.

Fresh HQ evidence after the failover/correction work shows no new verified replacement-SHD `initiation_verified/current-writer` artifact and no competing replacement writer evidence. Existing `entities/shardovik/current/*` files are old-lineage state, not proof of a replacement writer.

The old SHD chat is to remain historical/non-authoritative for new profile mutations under the emergency replacement decision.

## Exact verdict

`PASS_RECOVERY_CORRECTION_VERIFIED__PRACTICAL_COLD_START_PERMITTED`

The conjunction is now sufficient to permit practical cold-start:

`OPERATOR emergency replacement decision`
+
`base recovery content with corrected raw-byte integrity contract verified`
+
`emergency overlay verified`
+
`KOO control state confirmed`
+
`no competing replacement-writer evidence observed`.

This conjunction is sufficient to START the replacement SHD cold-start procedure. It is NOT sufficient to claim that cold-start already succeeded or that current-writer authority has already transferred.

## Permitted next boundary

OPERATOR may create/open a replacement SHD chat and provide the emergency initiation master:

`puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02/SHD__emergency-initiation-master.md`

Replacement SHD must, in order:
1. load active approved Project Sources;
2. verify original base recovery content using correction layer `3283e92f...`, not the invalid historical checksum table;
3. verify emergency overlay `ea6a84bc...`;
4. perform fresh HQ preflight;
5. perform the bounded MAZHOR read-only recovery checks from the launcher;
6. verify absence of competing writer evidence;
7. return its first initiation report;
8. only if all gates PASS, create its own SHD current-writer artifact;
9. read back exact commit/blob of that artifact;
10. only then become authoritative replacement current-writer and return to Resume-First.

Until step 9 succeeds, status is recovery/read-only and no profile mutation is authoritative.

## Explicit non-authorizations

This PASS does NOT authorize:
- WBN/TERA2 launch;
- production mutation;
- firewall/service changes unrelated to initiation readback;
- use/publication of secrets or credentials;
- destructive cleanup;
- automatic resurrection of historical WBN/TERA2/COOP/PWH tails;
- promotion of PWH/hashchain or any other candidate to canon.

After current-writer fixation, SHD must fresh-reconcile and either process one exact still-current task or enter `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть emergency failover verification после исправления checksum boundary и разрешить только practical cold-start replacement SHD
СТАТУС: pass_recovery_correction_verified_practical_cold_start_permitted
