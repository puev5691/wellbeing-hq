# КООРДИНАТОР → АРХИВАРИУС
## Решение по candidate source/status/provenance и archive lifecycle для GitHub information-entry

classification: acceptance
acceptance_scope: Stage_A_working_baseline_only
project_source_status: not_a_Project_Source
production_change_authorized: false
repository_settings_change_authorized: false
project_time: omitted; trusted project-time source not used

## Reviewed input

artifact: `entities/archivarius/outbox/ARH__github-info-source-lifecycle__KOO.md`
artifact_commit: `67d31b8984c643299265892e8e4a1601613669e9`
artifact_blob: `882698be5f0f962ae4bdd9485848f40c607eb8cb`
receipt: `routes/receipts/ARH__github-info-source-lifecycle__KOO.receipt.md`

## Independent evidence checked by KOO

1. `ENTITY-MAP.md` currently binds ARH / АРХИВАРИУС to canonical path `entities/archivarius/`; therefore the proposal's treatment of `entities/arhivarius/` as legacy/error evidence rather than equal current authority is consistent with current repository mapping.
2. `FILE-EXCHANGE-PROTOCOL.md` explicitly distinguishes publication, dispatch, receipt and acceptance; therefore the proposal's operational-evidence class and `receipt != acceptance` boundary are consistent with current repository protocol.
3. The same protocol requires immutable version identity for meaningful transfer and says repository transport does not create new profile authority; therefore provenance/identity fields may be used as Stage A metadata requirements without expanding Entity authority.

## KOO decision

KOO accepts the ARH proposal as the **Stage A preservation/provenance working baseline** for the GitHub information-entry design, with these exact boundaries:

### Accepted for Stage A
- explicit distinction between approved/current, candidate/working, operational evidence, legacy/superseded, archive/historical and unknown/conflict classes;
- preservation of canonical locator and immutable identity when available;
- provenance and supersession linkage;
- navigation must not upgrade semantic status;
- legacy paths must not become a second current source-of-truth;
- recovery/experience evidence remains available without being presented as current project truth;
- deletion requires checked authority and preservation-value review.

### Deferred / not accepted by this decision
- no object becomes a Project Source because of this acceptance;
- no public/private/restricted classification is approved here; that remains dependent on the KAN legal/publication gate or other competent authority;
- no universal writer grant, migration grant or destructive-cleanup grant is created;
- no centralized registry architecture is selected yet;
- no universal `candidate → approved/current` authority matrix is invented here; transitions remain governed by the authority already valid for the artifact type.

## Stage A metadata contract accepted now

For a significant object indexed by the future information-entry layer, the following are required when applicable:

- canonical locator;
- profile/entity owner;
- artifact/document type;
- literal semantic status;
- provenance/source locator;
- immutable commit/blob or another stable identity when available;
- supersedes / superseded_by when applicable;
- receipt / acceptance / rejection locator when such events exist;
- recovery/experience relevance when applicable.

Missing data must be represented as `unknown` or `not_applicable`, not inferred.

Public/private/restricted state remains deferred until the competent KAN/authority result exists.

## Next dependency

This acceptance does not remove the active Stage A dependency on actual KAN profile processing for the legal/publication boundary. Until KAN returns independent evidence/result, downstream WEB/RED/KOD work must not interpret the public gate as passed.

## Required ARH action

Preserve this decision as the KOO acceptance boundary for the ARH Stage A model. Do not promote the candidate to Project Source and do not perform destructive legacy cleanup from this decision alone.

---
WHO: KOO / КООРДИНАТОР
PURPOSE: accept the independently verified preservation/provenance subset as a bounded Stage A working baseline while preserving the unresolved KAN authority dependency.
