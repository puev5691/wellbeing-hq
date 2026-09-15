# KOO → KOD: replacement initiation v0.2

status: `TASKED_INITIATION_ONLY`
profile_execution_before_initiation_verified: `forbidden`
writer_transfer_by_this_task: `forbidden`
project_time: omitted; trusted project-time source not used

## Canonical recovery

`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Exact initiation file:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`

Independent ARH verification:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`.

Known historical current-writer artifact:
`entities/koder/current/KOD__initiation-verified-current-writer-v01.md`
commit `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`.

More recent KOD result that must be reconciled after loading recovery:
`entities/koder/outbox/KOD__info-entry-static-preview-E1-fix-v03__KOO.md`
commit `1f31bc2b640a456f2f99655620e809ce8eaeaada`.

## Exact task

1. Загрузить active approved Project Sources.
2. Independently verify canonical recovery exact immutable commit, composition, Git blob identities and bytewise checksums exactly as required by its manifest.
3. Сделать fresh GitHub-preflight `puev5691/wellbeing-hq`.
4. Reconcile всё более свежее KOD evidence после canonical recovery, включая E1 v0.3 result/dispatch/receipt and current KOD inbox/current state.
5. Проверить instance continuity, competing/current-writer boundary и отсутствие более свежего replacement writer evidence.
6. До `initiation_verified` работать read-only.
7. Вернуть exact initiation report.

## Writer boundary

Этот task **не передаёт current-writer** новому экземпляру автоматически.

Если прежний KOD writer не имеет отдельной retirement/replacement boundary, после успешной initiation остановиться в:
`WAKE_WAITING_OPERATOR_DECISION / WAITING_OPERATOR_WRITER_DECISION`.

Нельзя объявлять winner по новизне чата, commit time, availability или факту успешной recovery verification.

## Required result

Вернуть:
`entities/koder/outbox/KOD__replacement-initiation-v02-result__KOO.md`

Указать:
- initiation status;
- recovery verification;
- fresh HQ HEAD;
- newer KOD evidence reconciled;
- previous writer state;
- competing writer state;
- writer transfer performed: `no`;
- exact next gate.

Не брать следующую KOD профильную задачу до отдельного writer/task решения.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: инициировать новый экземпляр КОДЕРА без самовольного writer transfer и без потери свежего KOD evidence
СТАТУС: tasked_initiation_only
