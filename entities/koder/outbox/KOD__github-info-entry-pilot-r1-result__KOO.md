# KOD → KOO: bounded GitHub information-entry pilot r1 correction result

status: `CORRECTED_CANDIDATE_RETURNED_FOR_REVIEW`
production: no
source_task: `entities/koder/inbox/KOO__github-info-entry-pilot-implementation__KOD.md`
upstream_assignment_commit: `8870217c60005a023b5c9b7c6094a5dc20f51eb3`
upstream_stageB: `entities/webmaster/outbox/WEB__github-info-entry-stageB-synthesis__KOO.md`
prior_defective_package: `entities/koder/outbox/github-info-entry-pilot-v01/`
prior_defective_package_commit: `9cf9c0df43777fb20e188a00eafac2f8b1f0c6e8`
prior_review: `routes/receipts/KOD__github-info-entry-pilot-result__KOO.receipt.md`

## Corrected immutable package

path: `entities/koder/outbox/github-info-entry-pilot-v01-r1/`
immutable_package_commit: `e4c33e4940ea172f3f3cc2d16edc939a53426084`

## Exact defect corrected

The previous validator accepted `public_legal_outcome = allowed-with-conditions` without proving that conditions were satisfied.

r1 adds explicit required field:
`public_legal_conditions_satisfied`

Fail-closed rule:
- `allowed` may pass the legal gate;
- `allowed-with-conditions` passes only when `public_legal_conditions_satisfied == true`;
- otherwise validator returns `legal_conditions_not_satisfied`.

## Verification evidence

Local rerun after final correction:
- `7/7 cases PASS`
- positive `allowed`: PASS
- positive `allowed-with-conditions + satisfied=true`: PASS
- negative `allowed-with-conditions + satisfied=false`: FAIL as required with `legal_conditions_not_satisfied`
- candidate/unknown: FAIL
- blocked: FAIL
- superseded: FAIL
- secret-like: FAIL
- preview readback: PASS
- final SHA-256 manifest regenerated after final package bytes and verified: PASS

GitHub immutable readback:
- `MANIFEST.sha256` read successfully from exact package commit `e4c33e4940ea172f3f3cc2d16edc939a53426084`
- package remains candidate/pilot only.

## Boundary

No production rollout.
No repository settings changes.
No Pages/DNS changes.
No public release authority change.
No Project Sources mutation.
No credentials/provider calls.
No other Entity current/recovery mutation.
Historical defective v01 remains preserved as provenance.

Acceptance is not claimed. KOO independent review is required.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO исправленный immutable bounded information-entry pilot после точного fail-closed defect review
