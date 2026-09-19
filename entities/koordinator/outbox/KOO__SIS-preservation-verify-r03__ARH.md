# KOO → ARH: verify SIS self-preservation v0.3

status: TASK
execution_mode: RECOVERY_PRESERVATION_VERIFY
priority: RECOVERY

## Basis

SIS self-preservation result:
`318032c4185c46cabce288cf6abe86ec051de819`

Verdict:
`PASS_SIS_SELF_PRESERVATION_V03_PUBLISHED_AND_READBACK_VERIFIED`

Current SIS writer artifact:
`entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
blob `6590555d95275d18f4eee4478dad0f80ec9b260f`

External candidate locator:
`puev5691/wellbeing-entity-bootstrap@c195f023a5ad955105995de9f1c772e8cd85833d:entities/sis/preservation/pending/self-preservation-current-writer-v03`

Candidate status:
`candidate_not_canonical`

Expected composition: exactly 8 files.

## Required independent verification

1. verify exact source/current-writer identity;
2. verify exact immutable locator and commit;
3. verify 8-file composition and absence of undeclared directories;
4. verify listed Git blob identities;
5. independently verify published raw-byte SHA-256 identities from the recovery report;
6. verify manifest consistency and recovery package internal references;
7. verify secret boundary: no passwords/tokens/API keys/private keys/webhook secrets/usable access URIs;
8. inspect preserved open task state and classify stale/current dependencies;
9. confirm recoverability limitations, including that KOD Astra clean package is an active dependency, not accepted SIS runtime;
10. record Telegram temporary credential fact only as non-secret operational tail, without reading contents;
11. update ARH recovery registry according to current canon;
12. return exact preservation verdict.

Do not:
- rewrite SIS self-state;
- appoint replacement writer;
- promote candidate beyond what recovery canon permits without exact evidence;
- resume SIS profile work;
- read secret contents.

Expected:
`PASS_ARH_SIS_PRESERVATION_R03_READY_FOR_REPLACEMENT_INITIATION`
or exact blocker/fail.

Return result to KOO and stop.
