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
- grant production publication authority;
- grant universal writer, migration or destructive-cleanup authority;
- select a centralized registry architecture;
- create a universal candidate-to-approved authority matrix;
- replace RED editorial readiness or SIS infrastructure/security review;
- promote WEB metadata candidates to canon.

## KAN Stage A public/legal branch: accepted bounded working result

KAN source artifact:
`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`

artifact_commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
artifact_blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`

KOO decision:
`entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md`

decision_commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
status: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`
receipt: `routes/receipts/KAN__github-info-entry-public-legal-boundary__KOO.receipt.md`
receipt_commit: `300c5fc8933feda071fb63a71e82f8e744b79a53`

Accepted boundary includes preservation of literal status/provenance; public visibility alone does not authorize publication/reuse; candidate/draft/research must not be represented as approved/current truth; secrets and sensitive personal data are blocked for Stage A public navigation; third-party material without verified rights basis is not to be mirrored as public content. This acceptance does not create a Project Source or authorize production publication/settings changes.

## Current dependency: SIS Stage A infrastructure/security boundary

After KAN bounded acceptance, KOO created the next Stage A task:
`entities/koordinator/outbox/KOO__github-info-entry-stageA-sis__SIS.md`

task_commit: `83dcfa7e1e7c6f651ad12c43f996aa324f7a920a`

KOO dispatched it:
`routes/dispatch/KOO__github-info-entry-stageA-sis__SIS.md`
dispatch_commit: `1df75da93f7f0a976ca1308e1cf7154637edd4f2`

Canonical SIS inbox pointer:
`entities/sisadmin/inbox/KOO__github-info-entry-stageA-sis__SIS.md`
pointer_commit: `ca61728db9bc33c6bf466638ef4d88ea8a387fb9`
pointer_status: `dispatched_pointer`
receipt: separate
acceptance: separate

The correct entity directory is `entities/sisadmin/`. A lookup under `entities/sysadmin/` is not evidence of missing delivery and must not be used as a canonical locator.

Current Stage A dependency state is therefore:
`KAN_bounded_result_accepted -> SIS_task_dispatched_pointer_present -> SIS_receipt/processing/result/acceptance_not_inferred_here`.

Stage A must not be treated as complete until the required SIS infrastructure/security boundary is evidenced and competently handled. WEB/RED/KOD downstream work must preserve this dependency boundary.

## Cleanup boundary

Deletion or destructive legacy cleanup requires separately verified authority plus preservation-value review. In particular, `entities/arhivarius/` may be treated as legacy/error evidence under current `ENTITY-MAP.md`, but this Stage A acceptance alone does not authorize destructive cleanup of historical evidence.

## ARH handling rule

Use this file as the current ARH operational baseline for Stage A source/status/provenance and archive-lifecycle work until superseded by a later competent decision. Preserve original candidate proposals, decisions, receipts, dispatches and bounded results as immutable provenance rather than rewriting their historical statuses.

---
WHO: ARH / АРХИВАРИУС
PURPOSE: synchronize the accepted ARH preservation baseline with KOO's bounded KAN acceptance and the verified transition of the remaining Stage A dependency to SIS, without promoting dispatched work to receipt, processing, result or acceptance.