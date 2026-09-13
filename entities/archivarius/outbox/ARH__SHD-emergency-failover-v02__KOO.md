# ARH → KOO: SHD emergency failover v02 independent verification request

status: EMERGENCY_FAILOVER_CANDIDATE_READY_FOR_INDEPENDENT_VERIFICATION
entity: SHD / ШАРДОВИК
production_mutation: no
current_writer_transfer: not_performed
practical_reinitiation: not_performed
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР явно сообщил, что текущий SHD-чат ненадёжен, сломал рабочий процесс и должен быть заменён новым чатом. ОПЕРАТОР потребовал максимальную preservation/recovery дисциплину перед инициацией replacement SHD.

ARH не реконструирует foreign self-snapshot. Последний independently verified SHD self-recovery остаётся базой, а новые MAZHOR-события сохранены отдельным ARH external recovery overlay.

## Last verified SHD recovery

`puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:packages/shd-role-v2_3-current-recovery/`

ARH verification:
`entities/archivarius/outbox/ARH__shd-role-v2_3-recovery-verification__SHD.md`
commit `29e0a61e4a79842505a279bd131d25cb64978f5e`
state `PRESERVATION_CHECKPOINT_VERIFIED__PRACTICAL_INITIATION_TEST_NOT_PERFORMED`
checksum `4/4 PASS`.

## Emergency failover candidate v02

Immutable locator:
`puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02`

Composition:
- `SHD__emergency-initiation-master.md`
- `SHD__external-recovery-checkpoint.md`
- `SHD__experience-resume.md`
- `SHD__mazhor-backup-index.md`
- `SOURCES.md`
- `RECOVERY-MANIFEST.md`
- `sha256sums.txt`

Git blobs:
- manifest `e58a55f38671d045f5ecf8d339a61a1c9c04a448`
- initiation master `384682f6b5d0c357e1cad8ddd54394083da8fb9b`
- experience resume `9206732320a3f073689f03a2133356fa2620b5fd`
- external checkpoint `90e5deb588b7e2d092b00a802eac2c7b2afcd6c0`
- MAZHOR backup index `ef62e2b37c47e7f568bb975dc945dfa06119ace0`
- sources `268e13907adb9bba1a5a0827ae6d5762f1883495`
- checksums `6cdd64ab05788bf892022a0f6f42921c0df5e890`

ARH publication self-check:
- fresh immutable clone on MAZHOR at exact commit: PASS;
- composition: 7 files PASS;
- `sha256sum -c sha256sums.txt`: 6/6 PASS.

## Local MAZHOR preservation

Remote host `p552203.kvmvps` currently answered Remote Desktop Commander ping.

Local non-secret backup:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

Checksum table verified: `5/5 PASS`.

Failover marker:
`/data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md`
SHA-256 `5ad32dd091e3dbbac1b102fc2fcbd465d5844613e7bdf1491bd8bfbb3011cfb7`.

Secret/log/tmp contents were excluded from preservation readback. No credentials are included in GitHub artifacts.

## Required KOO action

1. Fresh-preflight `puev5691/wellbeing-hq`.
2. Independently verify exact base recovery identity `ce9891f...` and ARH verification `29e0a61...`.
3. Independently verify failover candidate `ea6a84bc...`, composition, blobs/provenance and checksum table.
4. Verify KOO control state and absence/presence of competing SHD current-writer evidence.
5. Verify that OPERATOR emergency replacement decision permits the failover transition without expanding SHD authority.
6. Return exact PASS/FAIL and the permitted next boundary.
7. Do NOT infer practical replacement initiation merely from package/inbox presence.
8. Do NOT promote PWH/hashchain or any other candidate/process artifact to canon.
9. Do NOT authorize WBN/TERA2 launch, production mutation, secrets handling or destructive cleanup from this preservation request.

If PASS, identify whether replacement SHD may perform practical cold-start and under what exact writer-handoff evidence. If any identity/authority mismatch exists, return the exact blocker.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: независимая проверка emergency failover package перед replacement SHD practical initiation
СТАТУС: candidate_ready_for_independent_verification
