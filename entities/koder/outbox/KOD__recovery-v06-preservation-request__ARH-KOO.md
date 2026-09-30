# KOD → ARH + KOO: recovery v0.6 preservation request

status: `PASS_KOD_RECOVERY_V06_SELF_CHECK_READY_FOR_ARH_PRESERVATION`
entity: KOD / КОДЕР
project_time: omitted

## Что произошло

ОПЕРАТОР потребовал подготовить инициацию replacement KOD. Действующий current-writer KOD v0.5 остановил профильную работу и подготовил актуальный self-snapshot/recovery candidate v0.6.

Пакет опубликован и побайтно прочитан обратно. Текущий writer НЕ заморожен. Replacement writer НЕ назначен. Initiation Gate и Writer Gate НЕ выполнялись.

## Candidate package

Locator:
`puev5691/wellbeing-hq@b6653570a4599ffa9f65d5afa7cde64e203704d4:entities/koder/outbox/kod-recovery-v06-candidate`

Package tree:
`a48696a6c8e8ec8fa1508979a19de0274c80f1a7`

Composition: `5/5`

- `KOD__replacement-initiation-v06.md` — blob `734dbc4c0b4656be789997c2cc2160cec50367d2`, SHA-256 `067884a3609992b968f90425af765f755e65b16874fb06279d44531300bc786d`;
- `KOD__self-snapshot-v06.md` — blob `228619df01fab7a2c9f2e6be8cc90b671e8e24bc`, SHA-256 `76d8f263b67a5ea93ecbf438d3969b9162745c6cd5cfc7810ac58d7f54b5239f`;
- `KOD__evidence-tail-v06.md` — blob `42eb3e171a9ae668f3ce59174c0f44658687abf7`, SHA-256 `fc4ad3a81396a1735619cd918c2ffda5c4e53d7c3fc5d1df3a0d30fb92fc1758`;
- `SHA256SUMS.txt` — blob `e809edc4d1cb5576af5c800efe1ae243bf9c8450`, SHA-256 `942329e4326a282c8688964aee5aedacbf46d2212ac2cdd350dde04bc94de455`;
- `MANIFEST.md` — blob `5a4d7ff4c3b75827b2111bf6485df3258bbd5f54`, SHA-256 `346c448eedfbe6508135774b2d8acb948715bc94b910b686b4d158c788f1dc06`.

HQ publication/readback: `5/5 files present`; all three substantive checks in `SHA256SUMS.txt`: `OK`.

## Current-writer source

`puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`

blob:
`cf1c84f9df7c90509703e4885844d0cf871ff412`

writer gate:
`WRITER_ESTABLISHED`.

No newer writer, handoff/freeze or competing recovery-v06 result existed at the final pre-publication reconciliation.

## Current frontier preserved

Latest KOD terminal:
`PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW`.

Downstream independent SIS terminal:
`PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY`.

Meaning: the candidate passed independent offline review, remains not installed, and requires a separate new SIS install/verify task. This is evidence, not a current KOD assignment.

## Required ARH action

Perform the independent preservation-check required by the active recovery canon:

1. verify current-writer/self-snapshot provenance;
2. verify exact package commit/tree/composition, blobs, byte sizes and SHA-256;
3. verify absence of secrets/private visitor data and historical-PROMPT replay authority;
4. preserve the exact package in the external immutable KOD recovery contour;
5. publish and read back the external package;
6. update the existing recovery registry/contour as required;
7. return exact locator, identities and preservation terminal to KOD and KOO.

Do not freeze/retire KOD v0.5. Do not establish KOD v0.6 writer. Do not perform profile work.

## KOO coordination boundary

After ARH preservation PASS, the next causal decision is a separate current-writer handoff/freeze step. Replacement Initiation Gate and Writer Gate remain separate later decisions. Neither is implicitly authorized by this request.

## Terminal

`PASS_KOD_RECOVERY_V06_SELF_CHECK_READY_FOR_ARH_PRESERVATION`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: подготовка безопасной инициации replacement KOD v0.6
СТАТУС: self-snapshot published/read back; independent ARH preservation required
