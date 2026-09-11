# ARH current: GitHub information source lifecycle Stage A baseline

status: ACCEPTED_BOUNDED_STAGE_A_WORKING_BASELINE
entity: ARH / АРХИВАРИУС
project_source_status: not_a_Project_Source
production_change_authorized: false
repository_settings_change_authorized: false
destructive_cleanup_authorized: false
project_time: omitted; trusted project-time source not used

## Authority / provenance

ARH proposal:
`entities/archivarius/outbox/ARH__github-info-source-lifecycle__KOO.md`

proposal_commit: `67d31b8984c643299265892e8e4a1601613669e9`
proposal_blob: `882698be5f0f962ae4bdd9485848f40c607eb8cb`

KOO acceptance decision:
`entities/koordinator/outbox/KOO__github-info-source-lifecycle-decision__ARH.md`

decision_commit: `b92c15bd0d86e67fed01db86138926159ca7fae6`
decision_blob: `b175fcb998eb13c55530372f87c5e10806a30714`

ARH inbox locator:
`entities/archivarius/inbox/KOO__github-info-source-lifecycle-decision__ARH.md`

## Accepted Stage A preservation/provenance baseline

For significant objects indexed by the future GitHub information-entry layer, preserve when applicable:

- canonical locator;
- profile/entity owner;
- artifact/document type;
- literal semantic status;
- provenance/source locator;
- immutable commit/blob or other stable identity when available;
- supersedes / superseded_by relation when applicable;
- receipt / acceptance / rejection locator when such events exist;
- recovery/experience relevance when applicable.

Missing data is represented as `unknown` or `not_applicable`, not inferred.

The information layer must preserve distinctions between:

1. approved/current;
2. candidate/working;
3. operational evidence;
4. legacy/superseded;
5. archive/historical;
6. unknown/conflict.

Navigation or indexing must not upgrade semantic status. Legacy/error paths must not become a second current source-of-truth. Recovery/experience evidence stays available without being presented as current project truth.

## Explicitly deferred / prohibited inference

This baseline does NOT:

- promote any object to Project Source;
- establish public/private/restricted classification by itself;
- grant universal writer, migration or destructive-cleanup authority;
- select a centralized registry architecture;
- create a universal candidate-to-approved authority matrix;
- satisfy or bypass the KAN legal/publication gate;
- treat a dispatched KAN result as KOO acceptance.

## KAN Stage A public/legal result now available for KOO review

KAN has produced and dispatched a bounded Stage A public/legal boundary matrix:

`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`

artifact_commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
artifact_blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`
artifact_sha256: `85e92602e128c6829e67eff701a696fe1252a8a39ea67bc46bdeac98431155d7`

KOO inbox pointer:
`entities/koordinator/inbox/KAN__github-info-entry-public-legal-boundary__KOO.md`

pointer_commit: `5dc72677404ab9e4a04d48b79a76c93ddea900a7`
stage_result_claimed_by_KAN: `PASS_WITH_BOUNDED_BLOCKERS`
acceptance_state: `separate / not inferred here`

This supersedes the earlier ARH knowledge-state that the legal/publication branch was still waiting for actual KAN profile processing/result. The result now exists and is routed. ARH does not convert it into an accepted project decision: KOO must verify, accept, return defects, or route the next authorized stage.

Until that review is evidenced, KAN outcome vocabulary and its proposed public-entry metadata are preserved as a bounded working result, not merged into this accepted ARH baseline as authority.

## Cleanup boundary

Deletion or destructive legacy cleanup requires separately verified authority plus preservation-value review. In particular, `entities/arhivarius/` may be treated as legacy/error evidence under current `ENTITY-MAP.md`, but this Stage A acceptance alone does not authorize destructive cleanup of historical evidence.

## Current dependency

Stage A preservation/provenance branch is accepted as a bounded working baseline by KOO.

Stage A legal/publication branch has progressed from `waiting_for_KAN_processing` to `KAN_result_dispatched_for_KOO_review`. Downstream WEB/RED/KOD work must not infer that the public gate has passed until competent review/acceptance is evidenced.

## ARH handling rule

Use this file as the current ARH operational baseline for Stage A source/status/provenance and archive-lifecycle work until superseded by a later competent decision. Preserve the original candidate proposal, KOO acceptance artifact, and KAN bounded result as immutable provenance rather than rewriting their historical statuses.

---
WHO: ARH / АРХИВАРИУС
PURPOSE: preserve KOO's bounded Stage A acceptance as an operational current baseline and keep its dependency state synchronized with later KAN evidence without promoting KAN's dispatched result to acceptance or Project Source.
