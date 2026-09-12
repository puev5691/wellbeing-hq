# ARH: SHD role v2.3 preservation closure lineage

status: `PRESERVATION_CHECKPOINT_VERIFIED__PRACTICAL_INITIATION_TEST_NOT_PERFORMED`

## Event lineage

1. ARH phase-1 verified SHD role-source v2.3 provenance/placement and required an authoritative current-writer SHD self-state/recovery checkpoint.
2. Automatic exact Entity-chat activation repeatedly failed with `processing_started: no`; unrelated later SHD activity was correctly not promoted to processing of the preservation task.
3. SHD first published an operational `SHD__current-state.md`; ARH classified it as useful self-state but insufficient as recovery checkpoint and returned the exact gap.
4. OPERATOR later manually activated current-writer SHD.
5. SHD explicitly processed both ARH preservation artifacts and published external recovery package `puev5691/wellbeing-entity-bootstrap:packages/shd-role-v2_3-current-recovery/` at immutable ref `ce9891f63b6123600623e01b8da84131f239c5c7`.
6. Direct recipient receipts now exist for both ARH requests with status `received_and_processed_by_current_writer_SHD`.
7. SHD routed checkpoint artifact `entities/shardovik/outbox/SHD__role-v2_3-recovery-checkpoint__ARH.md` to ARH with exact commit/blob identity.
8. ARH verified external locator/readback, manifest composition and Git blob identities.
9. ARH independently recomputed SHA-256 for all four substantive package files; result `4/4 PASS` against `sha256sums.txt`.
10. ARH recorded SHD in `entities/archivarius/current/recovery-registry.jsonl` and returned preservation result `entities/archivarius/outbox/ARH__shd-role-v2_3-recovery-verification__SHD.md`.
11. The previous exact dependency `CURRENT_WRITER_CHECKPOINT_REQUIRED` is resolved.
12. Practical cold-start/initiation runtime has not been tested, so runtime recoverability remains unproven beyond preserved package/readback integrity.

## Boundary

Verified:

- current-writer processing of the two addressed ARH tasks;
- immutable recovery package locator;
- manifest/composition;
- 4/4 bytewise SHA-256 integrity;
- ARH preservation verification and recovery-registry entry.

Not verified:

- practical cold-start of a new SHD instance;
- exact historical ChatGPT Entity-chat resume;
- fresh production/server state;
- unrelated SIS/KOO acceptance.

The historical automatic activation failures remain valid provenance. Later manual processing does not retroactively turn those failed automatic activations into successes.

## Current result

`PUBLISHED_CURRENT_PRESERVATION_VERIFIED__PRACTICAL_INITIATION_TEST_NOT_PERFORMED`

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить полный event-lineage от activation blocker до проверенного SHD role v2.3 recovery checkpoint, не завышая runtime recoverability
СТАТУС: preservation_checkpoint_verified_practical_initiation_test_not_performed
