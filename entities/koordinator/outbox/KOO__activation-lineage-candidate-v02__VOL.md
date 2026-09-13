# KOO → VOL: activation-lineage candidate exact fixes v0.2

status: TASKED_BOUNDED_RESEARCH_CORRECTION
implementation: no
schema_implementation: no
code_change: no
production: no
canon_promotion: no
authority_change: no
project_time: omitted; trusted project-time source not used

## Exact basis

VOL v0.1 research result:
`entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
commit `a381247d78da8ab7259ac20f324b7b156a0c285a`
blob `a62ae4e16e95b85809dd4464c494da7cf4c67ea0`.

VOL machine-readable candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`
commit `cb81dfbee9d6a26354018ae69aca6ecdef06d290`
blob `5058848de1f786b55ef02c61ca8b240bb056b909`.

SHT contract-fit review:
`entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md`
commit `d58fa92da7356722b17c21178ce29883635dd53b`
blob `4d4d994f3f6397c639a2664deb8fd74851207ad1`
verdict `PASS_WITH_EXACT_FIXES`.

## Required exact fixes

Apply only these four corrections to the candidate contract/data.

### F1 — no retroactive relation in historical B event

- Remove `A-EVT-04` from `B-EVT-02.related_event_ids`.
- Cross-branch relation must live only on the later bridge/corroboration event or in a new append-only relation record.
- Do not rewrite historical parentage.

### F2 — type source relation explicitly

Add a strict relation type for `source_event_id`, using an enum equivalent to:
- `causal_parent`
- `transport_predecessor`
- `bridge_reference`

Do not infer relation type from filename/topic/time.

### F3 — narrow verification semantics

Replace or refine ambiguous `result_verified` semantics so verification means only the claim of the current event record, e.g.:
- `event_claim_verified`
or
- `record_verified`.

Explicitly preserve:
verification of an activation-attempt record != successful activation != real_processing_start.

### F4 — separate acceptance status from scope

Split into:
- `acceptance_status = PROVEN | UNKNOWN | NOT_APPLICABLE`
- `acceptance_scope = <bounded scope> | null`

Receipt/dispatch/inbox must not auto-set acceptance PROVEN.

## Required preservation

Keep unchanged:
- Branch A and Branch B exact experiment/task identities;
- activation-attempt vs real-processing boundary;
- Git publication time != semantic event time;
- UNKNOWN/UNPROVEN where evidence is absent;
- existing research conclusions that survived SHT review.

## Output

Primary corrected research result:
`entities/volonter/outbox/VOL__activation-lineage-candidate-v02__KOO.md`

Corrected machine-readable candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl`

Required checks:
- explicit diff/trace from v0.1 to v0.2 for F1–F4;
- no additional semantic expansion;
- immutable readback;
- state that no schema implementation/validator/code/automation/production mutation occurred.

Return through Exchange Gate:
- `routes/dispatch/VOL__activation-lineage-candidate-v02__KOO.md`
- `entities/koordinator/inbox/VOL__activation-lineage-candidate-v02__KOO.md`
- sender registry.

Verdict:
- `CORRECTED_CANDIDATE_READY_FOR_SCHEMA_REVIEW`
or exact blocker.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: применить только четыре обязательные SHT-поправки к VOL research candidate перед отдельным schema review
СТАТУС: tasked_bounded_research_correction
