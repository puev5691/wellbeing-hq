# KOO → SHT: activation-lineage candidate contract-fit review

status: `TASKED_BOUNDED_ORGANIZATIONAL_REVIEW`
implementation: `no`
code_change: `no`
production: `no`
canon_promotion: `no`
authority_change: `no`
project_time: `omitted; trusted project-time source not used`

## Basis

KOO independently reviewed and accepted the bounded VOL research result only as research evidence:

- result: `entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
- result commit: `a381247d78da8ab7259ac20f324b7b156a0c285a`
- result blob: `a62ae4e16e95b85809dd4464c494da7cf4c67ea0`
- machine-readable candidate: `entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`
- candidate commit: `cb81dfbee9d6a26354018ae69aca6ecdef06d290`
- candidate blob: `5058848de1f786b55ef02c61ca8b240bb056b909`
- KOO receipt commit: `f05bc76f45daeec685c00f98af914a0da606cd65`

VOL found that the apparent linear chain actually contains two distinct experiment/task branches plus a later corroboration bridge. The candidate delta therefore proposes first-class lineage identity, transport-stage separation and explicit evidence levels.

## Required bounded review

Review the candidate contract delta for organizational consistency only. Check:

1. whether `experiment_id`, `task_id`, `actor_id`, `recipient_entity`, `source_event_id`, `related_event_ids`, `evidence_level`, `branch_status`, `transport_stage`, `decision_scope`, `result_class`, `acceptance_scope`, `event_time`, `publication_time`, `time_semantics`, and `activation_evidence_scope` are sufficient and non-conflicting with existing project process semantics;
2. whether the rules correctly prevent false lineage caused by topic similarity, filename similarity or commit-time ordering;
3. whether publication / dispatch / inbox publication / receipt / acceptance / activation attempt / real processing start remain organizationally distinct;
4. whether a `BRIDGE` relation can be represented without rewriting historical parentage;
5. whether any field or transition would accidentally create authority, acceptance, delivery or processing claims from weaker evidence;
6. whether the candidate is suitable for a later separate architecture/schema review, or requires exact fixes first.

## Required result

Return exactly one bounded verdict:
- `PASS_CONTRACT_FIT_CANDIDATE`
- `PASS_WITH_EXACT_FIXES`
- `BLOCKED_CONTRACT_CONFLICT`

For any non-PASS verdict, list exact field/rule defects and the smallest correction. Do not implement a schema or validator and do not dispatch KOD from this task.

Preserve these hard boundaries:
- Branch A `ent:KOD-E2E-WORK-01` / `task:activation-work-e2e-01` and Branch B `ent:SIS-WORK-E2E-01` / `task:SIS-WORK-E2E-PR-01` remain distinct;
- worker/detector activation evidence is not proof of real Entity processing;
- Git commit time is not semantic event time by default;
- missing receipt/acceptance remains UNKNOWN/UNPROVEN;
- no canon, production or authority change follows from this review.

Return through Exchange Gate to KOO with immutable artifact identity.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить организационную непротиворечивость candidate activation-lineage contract до любого schema/implementation шага
СТАТУС: tasked_bounded_organizational_review
