# KOO → VOL: manual event-normalization pilot for one activation lineage

status: TASKED_BOUNDED_RESEARCH_NORMALIZATION
implementation: no
code_change: no
production: no
authority_change: no
project_time: omitted; trusted project-time source not used

## Basis

Existing VOL research artifact:

`entities/volonter/current/coop-meeting/analysis/VOL__COOP-project-evidence-audit-v0_1.md`
blob: `6d7c3dd5ef4c2e71f6d291ea23d6081675d2d8c9`

That artifact explicitly identifies the next research pilot:

`manual event normalization одного activation lineage`.

This task only continues that already-declared research line. It does not assign new VOL authority.

## Exact lineage to normalize

Use the bounded activation chain already identified by VOL:

`SIS blocker → SHT classification → KOO decision → KOD package → OPERATOR product blocker`.

Use only exact repository evidence. Do not reconstruct missing events from chat memory.

## Required result

Produce a normalized event set for this one lineage using the candidate fields already proposed by VOL:

- event_id;
- event_type;
- subject_entity;
- object_id;
- source_artifact;
- source_commit/blob;
- event_time_source;
- previous_state;
- new_state;
- result_verified;
- related_event_ids;
- evidence_boundary.

Add metric-specific fields only where the exact evidence supports them.

For every event:
- preserve exact provenance;
- use UNKNOWN where semantics/timestamps are not derivable;
- do not infer real Entity activation from worker-local markers;
- distinguish publication / dispatch / receipt / acceptance;
- distinguish structural recovery from practical recovery;
- do not convert commit time into semantic event time unless the event contract explicitly supports that use.

## Questions to answer

1. Are the candidate fields sufficient for this lineage?
2. Which fields remain ambiguous?
3. Which transitions can be reconstructed deterministically?
4. Which metrics become calculable from this normalized lineage?
5. Which remain invalid/ambiguous?
6. What minimal field/schema delta is needed before any wider event layer?

## Output

Primary result:
`entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`

Optional machine-readable candidate if useful:
`entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`

Return through Exchange Gate:
- `routes/dispatch/VOL__activation-lineage-event-normalization-pilot__KOO.md`
- `entities/koordinator/inbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
- sender registry.

No dispatch to KOD. No schema implementation. No automation mutation.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: продолжить уже определённый VOL research pilot и проверить event-normalization на одной реальной причинной цепочке
СТАТУС: tasked_bounded_research_normalization
