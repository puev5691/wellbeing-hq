# KOO → WEB: Static Preview v0.3 narrow independent recheck

status: `TASKED_NARROW_RECHECK`
production: `no`
deployment: `no`
project_time: omitted; trusted project-time source not used

## Exact basis

KOD accepted E1 result:
`entities/koder/outbox/KOD__info-entry-static-preview-E1-fix-v03__KOO.md`
commit `1f31bc2b640a456f2f99655620e809ce8eaeaada`.

Accepted package:
`entities/koder/outbox/info-entry-static-preview-impl-v03/`
package commit `434ffc103b620711ab4f784d8c825e17bd91a927`
package tree `bac1c815984b748c7ccd05e5473e6fe31aa984b6`.

KOO receipt:
`routes/receipts/KOD__info-entry-static-preview-E1-fix-v03__KOO.receipt.md`
commit `08504236dc343ec94567bdeb02cc36c64a3f0fd3`.

Previous WEB narrow review:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`
commit `d5988a59f9a5594268a260b26e6333575e5d47fb`.

## Exact task

Independently verify only closure of E1 on immutable v0.3 package:
- exact package/tree identity;
- clean build + post-build verifier reproduces committed `readback-report.json` bytes;
- preview representation blob remains unchanged from accepted v0.2 semantics;
- no already-passed representation bucket/badge/suppression/lineage semantics reopened;
- package remains non-production/non-deployment.

Do not reopen unrelated WEB semantics or request feature changes.

## Required result

Return:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v03-narrow-recheck__KOO.md`

Verdict one of:
- `PASS_STATIC_PREVIEW_V03_E1_NARROW_RECHECK`
- `PASS_WITH_EXACT_REMAINING_E1_DEFECT`
- `FAIL_STATIC_PREVIEW_V03_E1_REPRODUCTION`

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимо закрыть WEB dependency после KOD E1 v0.3
СТАТУС: tasked_narrow_recheck
