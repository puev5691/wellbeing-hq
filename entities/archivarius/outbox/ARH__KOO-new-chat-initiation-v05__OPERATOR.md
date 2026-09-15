# ARH → OPERATOR: инструкция аварийной инициации replacement KOO v05

status: `READY_FOR_OPERATOR_COLD_START`
entity: `KOO / КООРДИНАТОР`
old_writer_state: `CURRENT_WRITER_HANDOFF_FREEZE`
replacement_writer_state: `not_established`
project_time: omitted; trusted project-time source not used

## Назначение

Открыть новый чат КООРДИНАТОРА и восстановить его только из independently verified canonical recovery v05, после чего отдельно установить replacement current-writer при отсутствии competing writer evidence.

Старый KOO после freeze `87cf8bd2f14786f7cdc4fa1e10ef59f18ec8b1cd` не должен выполнять нормальную authoritative profile/current-state работу.

## Canonical recovery

Использовать:
`puev5691/wellbeing-entity-bootstrap@47eea7599619c98a2d590f38b6a7a608d4af97c8:entities/koo/recovery/current`

ARH preservation result:
`entities/archivarius/outbox/ARH__emergency-recovery-v05-result__KOO.md`
commit `82619b22e25e52b06d92df2c6b7a98f0bb5c58db`
blob `1d4722b4d9935ae86fe452e9141f06091ec96160`
verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.

Verified canonical composition: 7 files.
Verified checksum table: 6/6 PASS.

## Mandatory cold-start order

1. Load only the five active approved Project Sources listed in canonical `SOURCES.md`.
2. Read canonical `MANIFEST.md`.
3. Verify exact immutable commit `47eea759...` and exact 7-file composition.
4. Verify `sha256sums.txt` against externally read published bytes, without LF/CRLF normalization.
5. Read `KOO__initiation-current__KOO.md` and `KOO__snapshot__KOO.md`.
6. Read `KOO__emergency-initiation-master-v05.md`.
7. Fresh-preflight `puev5691/wellbeing-hq`.
8. Read `entities/koordinator/current/KOO__emergency-handoff-v05.md` and confirm old writer freeze.
9. Check for any newer competing/replacement KOO writer evidence after the freeze.
10. Reconcile all HQ evidence newer than snapshot boundary `457865df475b5296c5ce087eb69c9e06826936ba`.
11. Read `entities/koordinator/current/KOO__work-queue-current.md`, but do not execute queue v09 automatically.
12. Return one initiation status: `initiation_verified`, `initiation_loaded_external_unverified`, or `initiation_failed`.

## Writer gate

OPERATOR has explicitly ordered emergency replacement of the degraded KOO chat. That is the human authority basis for replacement, but it does not bypass recovery or competing-writer checks.

Only if:
- recovery verification is PASS;
- fresh HQ reconciliation is PASS;
- old writer freeze is confirmed;
- no unresolved competing replacement writer exists;

then the new KOO may create a KOO-owned replacement current-writer artifact.

Writer establishment becomes effective only after immutable publication/readback of that exact writer artifact and a fresh post-publication competing-writer reconciliation.

`initiation_verified != current_writer_established`.

## First report required from replacement KOO

Return a standalone KOO-owned result containing:
- `initiation_status`;
- exact canonical recovery locator;
- composition result;
- raw-byte checksum result;
- active Project Sources verification result;
- ARH preservation result identity;
- fresh HQ HEAD;
- old writer freeze identity;
- competing writer state;
- replacement current-writer state;
- writer artifact commit/blob/readback if established;
- current queue pointer identity;
- unresolved OPERATOR gates and blocked dependencies;
- confirmation that no historical queue/task was automatically replayed.

## Do not auto-execute during initiation

Do not automatically:
- approve or activate recovery canon v1.5 candidate r0.4;
- resolve the KOD replacement writer gate;
- launch Telegram threading-fix work;
- launch TERA2 root-profile work;
- execute Work-mode migration/pilot tasks;
- re-enable old Entity GitHub Work automations;
- perform production/external execution;
- create/reconstruct/publish credentials;
- perform destructive cleanup.

After writer establishment, do another fresh HQ preflight and recompute priorities from current evidence. Do not replay `KOO__work-queue-v09-ru.md` blindly.

## Stop conditions

If canonical recovery fails identity/composition/checksum verification: `initiation_failed` and stop normal profile work.

If competing writer evidence appears: do not choose winner by time or availability; stop at writer conflict and return exact evidence.

If recovery verifies but writer establishment cannot be authorized/proven: remain read-only and return the exact blocked state.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: операторский cold-start replacement KOO после verified emergency recovery v05
СТАТУС: ready_for_operator_cold_start
