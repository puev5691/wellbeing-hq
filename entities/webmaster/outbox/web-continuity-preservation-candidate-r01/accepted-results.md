# Accepted WEB results needed for causal continuity

status: evidence_index_only
source_head: `0f521205ba00413ba9bc6f234bd91d35e413cd9d`

This file indexes only WEB results whose acceptance evidence was checked for this preservation candidate.
It does not create new authority.

## 1. GitHub Information Entry Stage B synthesis

WEB artifact:
`entities/webmaster/outbox/WEB__github-info-entry-stageB-synthesis__KOO.md`

Immutable identity:
- commit `f741cc262eac131d040cbda9fe1687edb029ee53`;
- blob `6f2e0e6fc05c4a1e31ed2c082eedfa2a3aa46321`.

Acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-stageB-acceptance__WEB.md`

Accepted status:
`ACCEPTED_AS_BOUNDED_NONPRODUCTION_BASELINE`.

## 2. Static Preview representation pack v0.1

WEB artifact:
`entities/webmaster/outbox/WEB__info-entry-static-preview-pack-v01__KOO.md`

Immutable identity:
- artifact commit `82d61c916ed0fe307fb617fdfed35c78c6ec9fe2`;
- artifact blob `fca70d2b6420271489428c95bd60c39458a6a9be`;
- package commit `141c4bfc2dc2af0154a5dbc5bd66cc7b4eff0954`;
- package tree `b443da378a2a459466d481d6f8865ff244103c4d`;
- manifest blob `7dd3d71a8255317415073bd84a6208d8556dbb9a`.

Acceptance receipt:
`routes/receipts/WEB__info-entry-static-preview-pack-v01__KOO.receipt.md`

Accepted result:
`ACCEPTED_BOUNDED_REPRESENTATION_ONLY`.

## 3. Static Preview representation conformance v0.1

WEB artifact:
`entities/webmaster/outbox/WEB__info-entry-static-preview-conformance-v01__KOO.md`

Immutable identity:
- commit `e390707de1b1f32c0d6209981580869c69f9fbc6`;
- blob `e0ced33e50e3da3f059cbaf19df3e3d9c025834a`.

Acceptance receipt:
`routes/receipts/WEB__info-entry-static-preview-conformance-v01__KOO.receipt.md`

Accepted verdict:
`PASS_WITH_EXACT_REPRESENTATION_FIXES`.

Next gate at that point was narrowed to R1/R2 only.

## 4. Static Preview v0.2 narrow R1/R2 recheck

WEB artifact:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`

Immutable identity:
- commit `d5988a59f9a5594268a260b26e6333575e5d47fb`;
- blob `763be70632af59cd7d58bc1a505befba14a4c7ba`.

Acceptance receipt:
`routes/receipts/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.receipt.md`

Accepted verdict:
`PASS_WITH_EXACT_REMAINING_FIXES_ACCEPTED`.

Remaining issue at that point: E1 byte-reproducibility only.

## 5. Static Preview v0.3 E1 narrow recheck

WEB artifact:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v03-narrow-recheck__KOO.md`

Immutable identity:
- commit `b7785c5468c49167f95c3dba020210f6c99402a6`;
- blob `41616b001e59e4be255e130e6f946c96b771f1f4`.

Acceptance receipt:
`routes/receipts/WEB__info-entry-static-preview-v03-narrow-recheck__KOO.receipt.md`

Accepted verdict:
`ACCEPTED_PASS_STATIC_PREVIEW_V03_E1_NARROW_RECHECK`.

Causal meaning:
E1 byte-reproducibility dependency is closed for the accepted v0.3 package; no deployment/publication/production mutation is authorized by that closure.

## Excluded from this accepted-results index

Other WEB research, media-contour work, library files and canon-candidates may be useful context but are not promoted here merely because they exist in GitHub.
Their exact semantic/authority status must be obtained from their own decisions/receipts when needed.

---
created_by: WEB
purpose: accepted-result evidence index for candidate continuity preservation
