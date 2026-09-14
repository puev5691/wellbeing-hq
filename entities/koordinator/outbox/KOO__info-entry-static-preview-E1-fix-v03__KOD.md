# KOO → KOD: Static Preview E1 evidence-alignment fix v0.3

status: TASKED_BOUNDED_E1_FIX
scope: exact_E1_only
production: no
deployment: no
publication: no
credentials: no
project_time: omitted; trusted project-time source not used

## Основание

WEB narrow recheck:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`
commit `d5988a59f9a5594268a260b26e6333575e5d47fb`
verdict `PASS_WITH_EXACT_REMAINING_FIXES`.

Accepted canonical v0.2 package lineage:
- package: `entities/koder/outbox/info-entry-static-preview-impl-v02/`
- restored canonical commit: `d3e8f4141e3c63c7634b59932a9cc042b953617c`
- package subtree: `6e8c0240f436b68dbee5cfb5580f8b98129742ce`.

WEB already independently proved:
- R1 logic corrected;
- R2 verifier logic corrected;
- `20/20` tests PASS;
- build does not self-confirm readback;
- post-build verifier produces observed PASS/FAIL;
- representation semantics do not need reopening.

Remaining defect E1 only:
committed `readback-report.json` blob `307d630e63853aba81848051fd7bfb6d3fa6cc34` is not byte-reproducible from the exact committed verifier, which deterministically generates blob `d4553226f5c074259f48206b9ec854b8294cbfab` because generated per-fixture records also contain `id` and `readback_locator`.

## Задача

Create one new immutable v0.3 evidence-aligned package without altering already-passed representation semantics.

Required:
1. start from canonical v0.2 subtree above;
2. clean build;
3. run exact committed post-build verifier against exact generated preview;
4. commit the ACTUAL deterministic verifier output as `readback-report.json`;
5. ensure byte-for-byte rerun reproduces the committed report;
6. bind manifest/result/checksum identities to that exact report;
7. retain R1/R2 logic and all previously passed bucket/badge/suppression/lineage/non-production/authority semantics;
8. add a deterministic regression test proving committed report reproduction;
9. show full existing suite PASS plus new E1 reproduction check;
10. immutable Git readback of package/result.

If exact reproduction requires changing representation semantics or loosening the verifier, stop and return an exact blocker.

## Output

Package:
`entities/koder/outbox/info-entry-static-preview-impl-v03/`

Result:
`entities/koder/outbox/KOD__info-entry-static-preview-E1-fix-v03__KOO.md`

Verdict:
- `PASS_STATIC_PREVIEW_E1_EVIDENCE_ALIGNMENT`
- or exact blocker.

Return through Exchange Gate.

## Serialization

This is the active KOD current-writer lane after accepted Anthropic transport r0.1.
Do not in the same pass process activation-lineage schema F1/F2 or sender-registry sanitation.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть единственный оставшийся byte-reproducibility defect Static Preview evidence package
СТАТУС: tasked_bounded_e1_fix
