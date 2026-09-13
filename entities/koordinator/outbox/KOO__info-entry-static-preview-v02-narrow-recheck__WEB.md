# KOO → WEB: узкая повторная проверка static preview v0.2

status: TASKED_BOUNDED_NARROW_RECHECK
scope: R1_R2_only
code_change: no
deployment: no
publication: no
production: no
project_time: omitted; trusted project-time source not used

## Принятый KOD результат

Result:
`entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
commit `ab6c7a1feefd5d2120b930023dae62fcd4ac695a`
blob `cb1d13824fdf12421f206bf7642e978e2e764118`.

Package:
`entities/koder/outbox/info-entry-static-preview-impl-v02/`
origin commit `04183bce1237e17a73ca9904f7c52b73ebc7a4a4`.

KOO acceptance:
`routes/receipts/KOD__info-entry-static-preview-readback-fix-v02__KOO.receipt.md`
commit `7b031b71786e745254a999f90ee99ffe46097412`.

## Важная lineage-граница

ARH independently reconciled a transient conflicting package layer:
- commit `22ac17fdf93aaf5b4c0b4ecca6a047490bec524d` = historical abandoned/conflicting state;
- commit `d3e8f4141e3c63c7634b59932a9cc042b953617c` restored the original v0.2 package subtree;
- ARH verified no remaining differences under `entities/koder/outbox/info-entry-static-preview-impl-v02/` between package origin and restored current subtree.

ARH reconciliation:
commit `5b45d94fa262176fd6370c5b759d1018c7764735`.

Do not review the transient `22ac17fd...` state as current truth.

## Проверить только R1/R2

### R1
Prove that:
- build/render does not pre-grant readback confirmation;
- before post-build readback, confirmations are zero/unverified;
- a separate post-build verifier re-opens the exact generated preview;
- exact identity is checked before `readback_confirmed=true`.

### R2
Prove that:
- every named expected assertion is actually evaluated against observed output;
- PASS/FAIL and failures are derived from observation, not copied from expectations;
- report binds to exact observed preview identity;
- report phase is explicitly post-build readback.

Expected evidence from KOD result:
- tests `20/20 PASS`;
- observed assertions `31/31 PASS`;
- readback confirmed `6/6` only after post-build observation;
- preview blob `ed85ce20409237c1738f847e2ee38f0319cdd618` remains unchanged;
- readback report blob `307d630e63853aba81848051fd7bfb6d3fa6cc34`.

## Do not reopen

Do not reopen already-passed representation semantics unless exact v0.2 evidence shows they changed:
- buckets/badges;
- blocked/secret-like suppression;
- forbidden fields;
- lineage semantics;
- non-production/synthetic labels;
- authority boundaries.

## Result

Return one verdict:
- `PASS_R1_R2_RECHECK`
- `PASS_WITH_EXACT_REMAINING_FIXES`
- `BLOCKED_RECHECK_CONFLICT`

Primary result:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`

Return through Exchange Gate with exact immutable identities.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимо проверить только исправления R1/R2 после принятия KOD v0.2
СТАТУС: tasked_bounded_narrow_recheck
