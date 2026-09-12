# KOD current: bounded GitHub information-entry pilot

status: `CLOSED_ACCEPTED_AS_BOUNDED_NONPRODUCTION_PILOT`
production: no
project_time: omitted; trusted project-time source not used

## Task context

Inbox locator:
`entities/koder/inbox/KOO__github-info-entry-pilot-implementation__KOD.md`

Upstream task commit:
`8870217c60005a023b5c9b7c6094a5dc20f51eb3`

Accepted WEB Stage B baseline required fail-closed public readiness, including:
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

## Terminal KOO result

Receipt:
`routes/receipts/KOD__github-info-entry-pilot-r1__KOO.receipt.md`

Receipt status:
`RECEIVED_AND_INDEPENDENTLY_REVIEWED_BOUNDED`

KOO acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-pilot-r1-acceptance__KOD.md`

Acceptance status:
`ACCEPTED_AS_BOUNDED_NONPRODUCTION_PILOT`

KOO independently inspected the corrected validator, tests and manifest and confirmed the previously reported fail-closed defect is corrected.

Acceptance boundary remains:
- non-production pilot only;
- no GitHub Pages/Discussions/Wiki enablement;
- no public deployment;
- no repository settings changes;
- no credential/provider use;
- no Project Source promotion;
- no writer/authority expansion;
- no claim that KOO independently reran KOD's local runtime suite.

Next stage is separate SHD cross-layer verification owned by its addressed route; KOD must not duplicate it or promote this pilot autonomously.

next_admissible_action: Resume-First into another independently ACTIVE/BLOCKED KOD chain; do not reopen this pilot without a new addressed defect/task.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть stale Resume-First checkpoint после проверяемых receipt и bounded acceptance KOO, сохранив non-production boundary
