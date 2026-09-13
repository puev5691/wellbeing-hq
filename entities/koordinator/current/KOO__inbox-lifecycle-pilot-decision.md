# KOO inbox lifecycle v0.1 — ARH constraints acceptance

status: ACCEPTED_WITH_PRESERVATION_CONSTRAINTS
scope: KOO_ONLY_BOUNDED_PILOT

## Decision

KOO accepts the ARH operational/preservation review:

`entities/archivarius/outbox/ARH__inbox-lifecycle-operational-review__KOO.md`
artifact_commit: `1b6aab5e50c759a7027b3c5b370475fe35417eec`
artifact_blob: `1f8217d29fcc294178734b303df756113066662a`
result: `PASS_WITH_PRESERVATION_CONSTRAINTS`

The next bounded implementation step is authorized only for KOO:

- create `entities/koordinator/current/inbox-lifecycle.jsonl` as append-only recipient-owned event log;
- create `entities/koordinator/current/active-queue.json` as materialized current view;
- leave `entities/koordinator/inbox/` unchanged;
- perform classification-only migration;
- exclude waiting/service/superseded/closed items from immediate active queue;
- perform immutable readback and reconciliation;
- do not enable production automation;
- do not create queue files for other Entities;
- do not move, delete, rename or rewrite raw inbox evidence.

This decision does not authorize physical cleanup or archive migration.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: принять preservation-ограничения ARH и открыть bounded KOO-only pilot active queue
СТАТУС: accepted_with_preservation_constraints
