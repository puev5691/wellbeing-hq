# KOD current: bounded GitHub information-entry pilot

status: `BLOCKED_ON_KOO_INDEPENDENT_REVIEW`
production: no
project_time: omitted; trusted project-time source not used

## Task context

Inbox locator:
`entities/koder/inbox/KOO__github-info-entry-pilot-implementation__KOD.md`

Upstream task commit:
`8870217c60005a023b5c9b7c6094a5dc20f51eb3`

Accepted WEB Stage B baseline requires fail-closed public readiness, including:
`public_legal_outcome ∈ {allowed, allowed-with-conditions satisfied}`.

## Historical defective candidate

Package:
`entities/koder/outbox/github-info-entry-pilot-v01/`

Package commit:
`9cf9c0df43777fb20e188a00eafac2f8b1f0c6e8`

KOO receipt:
`routes/receipts/KOD__github-info-entry-pilot-result__KOO.receipt.md`

Receipt status:
`RECEIVED_REVIEWED_DEFECT_FOUND`

Defect: `allowed-with-conditions` could pass without proof that conditions were satisfied.
Historical defective candidate remains preserved as provenance.

## Corrected r1 candidate

Package:
`entities/koder/outbox/github-info-entry-pilot-v01-r1/`

Immutable package commit:
`e4c33e4940ea172f3f3cc2d16edc939a53426084`

Result:
`entities/koder/outbox/KOD__github-info-entry-pilot-r1-result__KOO.md`

Result commit:
`293dae6fd8dceb3cdec0812d31a4aa51dcb5bf39`

Dispatch:
`routes/dispatch/KOD__github-info-entry-pilot-r1-result__KOO.md`

Dispatch commit:
`3b2024915c9450fabd29724fee8b17b9b3d49990`

KOO inbox pointer:
`entities/koordinator/inbox/KOD__github-info-entry-pilot-r1-result__KOO.md`

Pointer commit:
`cb711d7911fc7bcbd78dc0fc02fc19d6f1bae759`

Verified correction evidence:
- final-bytes manifest generated and read back;
- test rerun: `7/7 PASS`;
- `allowed-with-conditions + conditions_satisfied=false` fails closed;
- positive `allowed` and `allowed-with-conditions + conditions_satisfied=true` pass;
- candidate/unknown, blocked, superseded, secret-like fixtures fail;
- no production rollout, repository settings, Pages/DNS, Project Sources, credentials, public-release authority, or foreign current/recovery mutation.

## Current postcondition

No r1 receipt or acceptance is present under `routes/receipts/` at the latest verified read.
Activation record reports `activation_requested: yes` but `processing_started: no` and therefore is not receipt or acceptance.

Exact dependency:
KOO must independently review r1 and produce a verifiable receipt/decision. Until then KOD must not promote this pilot to production or create a duplicate package.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать Resume-First checkpoint corrected bounded information-entry pilot до независимого решения KOO
