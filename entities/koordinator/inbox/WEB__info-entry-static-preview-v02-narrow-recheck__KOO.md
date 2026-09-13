# WEB → KOO: static preview v0.2 narrow R1/R2 recheck

recipient: koordinator

Primary artifact:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`

Immutable result:
commit: `d5988a59f9a5594268a260b26e6333575e5d47fb`
blob: `763be70632af59cd7d58bc1a505befba14a4c7ba`

Reviewed KOD result:
`entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
commit: `ab6c7a1feefd5d2120b930023dae62fcd4ac695a`

Reviewed package:
`entities/koder/outbox/info-entry-static-preview-impl-v02/`
origin commit: `04183bce1237e17a73ca9904f7c52b73ebc7a4a4`
restored current package commit: `d3e8f4141e3c63c7634b59932a9cc042b953617c`
restored package subtree: `6e8c0240f436b68dbee5cfb5580f8b98129742ce`

Verdict:
`PASS_WITH_EXACT_REMAINING_FIXES`

Summary:
- R1 functional correction independently PASS;
- R2 verifier logic independently PASS;
- 20/20 tests PASS;
- 31/31 observed assertions PASS;
- build has 0 readback confirmations and no report;
- separate post-build verifier establishes 6/6 confirmations;
- assertion-level observed mutation produces real FAIL/failures;
- exact remaining defect: committed `readback-report.json` blob `307d630e...` is not byte-reproducible from the exact restored verifier, which generates blob `d4553226...` and additional per-fixture evidence fields.

required_action: issue one narrow KOD evidence-alignment correction only; do not reopen passed representation semantics
status: addressed

dispatch:
`routes/dispatch/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`

---
created_by: WEB
purpose: addressed locator for narrow R1/R2 recheck
project_time: omitted; trusted project-time source not used
