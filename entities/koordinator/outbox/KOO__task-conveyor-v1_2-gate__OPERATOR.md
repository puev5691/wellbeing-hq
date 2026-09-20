# KOO → OPERATOR: task-conveyor canon v1.2 successor decision

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Exact verified basis

KAN terminal:
`entities/kancelar/outbox/KAN__literary-journal-feed-norm-review-r01__KOO.md`

commit:
`f4b8725d3dda4c8145cb80641b539d0992e760d4`

blob:
`1d0af9a0c02ad1e1e0ca9bb04c5bafe4a19c1438`

terminal:
`PASS_KAN_JOURNAL_FEED_NORMATIVE_READY_FOR_KOO_DECISION_GATE`

Successor delta candidate:
`entities/kancelar/outbox/KAN__task-conveyor-v1_2-journal-feed-delta-candidate__KOO.md`

commit:
`6f27acf12c9a2dc112f2a16c7a84dcc10b5654e2`

blob:
`25736c5998a1a67e087d4534467018dc95084455`

status:
`candidate / not approved / not active`

## Current approved source

`task-conveyor-canon-v1_1-approved.md`

Exact insertion point verified:
after §10 `Manual activation handoff после terminal result` and before §11 `Failure modes`.

## Proposed single-source successor

`task-conveyor-canon-v1_1-approved.md`
→
`task-conveyor-canon-v1_2-approved.md`

Only the materialized KAN delta is to be inserted.
No other normative source is changed.

## Sources explicitly unchanged

- `project-instructions-core-v2_4-approved.md`;
- `entity-roles-short-v2_4-approved.md`;
- `file-work-canon-universal-v2_4-approved.md`;
- `source-loading-policy-v2_2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`.

## Exact successor meaning

v1.2 adds an optional positive post-terminal `JOURNAL_CANDIDATE` signal for events with historical/editorial value.

The same terminal-result artifact may carry the compact signal after the human-readable part.

KOO may batch 1–3 positive signals for a bounded RED journal sweep.
RED remains the sole editorial filter and may include, merge, defer or reject candidates.

Signal absence has no negative semantic meaning.

## Mandatory boundaries

The successor MUST preserve all of the following:

- no per-task journal reporting;
- no mandatory `JOURNAL_CANDIDATE: no`;
- no separate journal/feed artifact for routine result;
- no cron/scheduler/automation;
- signal does not imply automatic journal inclusion;
- signal is not task authority;
- signal is not delivery/receipt/acknowledgement/acceptance;
- signal is not public/release approval;
- signal is not a completion criterion of the originating task;
- no second technical log;
- no full transcript ingestion;
- OPERATOR is not turned into a manual literary dispatcher;
- RED remains owner of editorial selection.

## Effectivity

Even after approval, v1.2 is not active merely because this decision exists.

After explicit OPERATOR approval KOO must:
1. materialize full `task-conveyor-canon-v1_2-approved.md` from current approved v1.1 plus only the exact KAN delta;
2. preserve all unchanged text byte-for-byte where practical;
3. perform full readback and structural comparison;
4. verify only the intended section/source-card/version changes occurred;
5. perform source-set/activation barrier;
6. mark v1.2 active only after barrier PASS.

Until that PASS, v1.1 remains the active source.

## Decision requested

Approve the exact single-source successor:

`APPROVE_TASK_CONVEYOR_CANON_V1_2_JOURNAL_FEED`

Any other response does not activate or approve v1.2.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED