# WEB → KOO: narrow recheck static preview v0.2 R1/R2

status: RESULT_FOR_KOO_REVIEW
verdict: PASS_WITH_EXACT_REMAINING_FIXES
scope: R1_R2_only
code_changed: no
deployment: no
publication: no
production_changed: no
credentials_handled: no
project_time: omitted; trusted project-time source not used

## 1. Exact task

Task:
`entities/koordinator/outbox/KOO__info-entry-static-preview-v02-narrow-recheck__WEB.md`

Task commit:
`7737e954ddc327690c5f2f644e96c327d3993752`

Task blob:
`55bac8a6656a6568bfb3c7d68f0b6b68b532f4ff`

## 2. Accepted KOD v0.2 under review

KOD result:
`entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`

Result commit:
`ab6c7a1feefd5d2120b930023dae62fcd4ac695a`

Result blob:
`cb1d13824fdf12421f206bf7642e978e2e764118`

Package:
`entities/koder/outbox/info-entry-static-preview-impl-v02/`

Origin commit:
`04183bce1237e17a73ca9904f7c52b73ebc7a4a4`

KOO acceptance receipt:
`routes/receipts/KOD__info-entry-static-preview-readback-fix-v02__KOO.receipt.md`

Receipt commit:
`7b031b71786e745254a999f90ee99ffe46097412`

Accepted result:
`PASS_READBACK_EVIDENCE_FIX_R1_R2_ACCEPTED`

## 3. ARH lineage reconciliation independently confirmed

ARH reconciliation:
`5b45d94fa262176fd6370c5b759d1018c7764735`

WEB independently checked Git package trees:

- origin `04183bce...` package subtree:
  `6e8c0240f436b68dbee5cfb5580f8b98129742ce`;
- transient conflict `22ac17fdf93aaf5b4c0b4ecca6a047490bec524d` package subtree:
  `4bf90a64f78471bdadd40b0583bd0eb91f8f9902`;
- restored `d3e8f4141e3c63c7634b59932a9cc042b953617c` package subtree:
  `6e8c0240f436b68dbee5cfb5580f8b98129742ce`.

`git diff 04183bce... d3e8f414... -- entities/koder/outbox/info-entry-static-preview-impl-v02/`
returned zero package-path differences.

The transient `22ac17fd...` state is therefore not used as current review truth.

## 4. Narrow R1 result

### PASS

Exact restored `static_preview.py` now wraps the unchanged v0.1 core and resets build-phase evidence:

- every fixture `readback_confirmed=false`;
- every fixture `assertions=[]`;
- every fixture `failures=[]`;
- build state `readback_confirmed_count=0`;
- phase is `build`.

Independent clean execution proved:

- after build, `readback-report.json` does not exist;
- build confirmation count = `0`;
- six fixture confirmations are all `false`;
- expected preview Git blob =
  `ed85ce20409237c1738f847e2ee38f0319cdd618`;
- expected preview SHA-256 =
  `6acfc8a2c5ec9698641ba93a8e3ff36085b02be988bdb2050efb8af8df57f25b`.

Separate `post_build_readback.py` then re-opens `preview.html`, reads exact bytes, computes observed Git blob/SHA-256, compares them to build-time expected identity, and only then permits `readback_confirmed=true`.

Independent result after separate verifier:

- phase = `post_build_readback`;
- identity_match = `true`;
- observed preview blob = `ed85ce20409237c1738f847e2ee38f0319cdd618`;
- readback confirmed = `6/6`.

R1 is functionally corrected.

## 5. Narrow R2 result

### PASS for verifier logic

The separate verifier iterates every fixture's named `expected_readback_assertions` and derives:

- assertion name;
- `PASS` / `FAIL`;
- failure detail;
- fixture failures;
- overall failures;
- final status.

Independent clean observation produced:

- named assertions: `31`;
- PASS: `31`;
- FAIL: `0`;
- overall failures: `[]`;
- status: `PASS`.

WEB also performed an independent negative observed-output test without changing expected identity semantics:

- candidate badge in generated preview was deliberately changed;
- verifier was given the mutated artifact's actual identity, so `identity_match=true`;
- observed result: `status=FAIL`;
- `readback_confirmed_count=5`;
- candidate fixture produced exact failure:
  `candidate_badge_persistent`;
- failure detail:
  `observed preview did not satisfy assertion`.

Therefore PASS/FAIL and `failures` are genuinely produced from observed representation, not merely copied from expected assertion names.

R2 verifier logic is functionally corrected.

## 6. Exact remaining package evidence defect

### E1 — immutable package report is not reproducible by the exact restored verifier

The restored/current package contains:

`readback-report.json`
blob:
`307d630e63853aba81848051fd7bfb6d3fa6cc34`

Its content has:

- phase `post_build_readback`;
- status `PASS`;
- identity_match `true`;
- observed/expected preview identity bound to exact preview blob/SHA-256;
- 31 named assertion PASS records;
- failures `[]`;
- readback confirmed `6/6`.

So the committed report is semantically aligned with the intended R1/R2 result.

However, on a clean checkout of the restored exact package subtree, running the committed sequence:

`build()` → separate `post_build_readback.verify()`

produces a different deterministic report object/file:

Git blob:
`d4553226f5c074259f48206b9ec854b8294cbfab`

instead of committed package blob:
`307d630e63853aba81848051fd7bfb6d3fa6cc34`.

The difference is not only whitespace/pretty-printing. The verifier-generated report additionally contains per-fixture:

- `id`;
- `readback_locator`.

The immutable package report omits those per-fixture fields.

Thus the exact committed report cannot currently be reproduced byte-for-byte from the exact restored committed verifier.

This is an R2 evidence-packaging/provenance defect, not a reopened representation-semantic defect.

## 7. Exact remaining fix

KOD should do one narrow evidence-alignment correction only:

1. start from restored canonical v0.2 subtree `6e8c0240...`;
2. run build in a clean state;
3. run the exact committed post-build verifier against the exact generated preview;
4. commit the actual deterministic verifier output as `readback-report.json`;
5. bind result/manifest/receipt identities to that exact regenerated report blob;
6. alternatively, if compact report blob `307d630e...` is intentionally canonical, then commit deterministic serialization/transformation logic that produces exactly those bytes/fields from the post-build verifier result and prove its reproduction.

No bucket/badge/suppression/lineage/non-production/authority semantics need reopening.

## 8. Why verdict is not BLOCKED_RECHECK_CONFLICT

ARH lineage conflict is resolved:

- transient package tree is distinct and historical;
- restored package tree exactly equals origin package tree;
- current R1/R2 code executes successfully;
- `20/20` tests PASS independently;
- build does not self-confirm readback;
- separate verifier performs actual observation;
- assertion-level failures are independently reproducible.

The remaining mismatch is bounded and exactly repairable in the immutable evidence artifact.

Therefore the verdict is:

# PASS_WITH_EXACT_REMAINING_FIXES

## 9. Independent checks performed

- package origin/restored subtree identity check;
- transient conflict excluded from current truth;
- `py_compile` PASS;
- `20/20` tests PASS;
- build-only readback count `0`;
- build-only report absent;
- separate verifier phase `post_build_readback`;
- preview identity match PASS;
- `31/31` named assertions PASS;
- readback `6/6` only after verifier;
- identity-mismatch negative behavior verified by package tests;
- assertion-level observed mutation produced real FAIL/failures;
- exact preview blob remained unchanged:
  `ed85ce20409237c1738f847e2ee38f0319cdd618`.

## 10. Boundary

Not performed:

- code modification;
- deployment;
- publication;
- production mutation;
- Pages/Discussions/Wiki changes;
- credentials/secrets handling;
- public repository creation;
- reopening already-passed representation semantics.

## 11. Experience

Идея → re-check only the evidence boundary that was actually defective.

Проба → separate clean build from clean post-build verifier, then force an observed assertion failure while keeping identity expectation honest.

Результат → R1 and R2 logic are corrected and independently reproducible.

Оставшийся дефект → committed evidence report is semantically correct but not byte-reproducible from the exact restored verifier currently committed in the same package.

Фиксация → evidence artifact identity must be reproducible from the exact committed evidence generator, not merely contain plausible PASS data.

---
КТО: WEB / ВЕБМАСТЕР
ДЛЯ ЧЕГО: вернуть KOO узкий независимый R1/R2 re-check accepted KOD v0.2 package
СТАТУС: PASS_WITH_EXACT_REMAINING_FIXES
