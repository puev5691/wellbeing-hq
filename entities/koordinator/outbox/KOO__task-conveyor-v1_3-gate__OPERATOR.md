# KOO → OPERATOR: task-conveyor canon v1.3 incremental journal-feed decision

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Exact verified basis

KAN terminal:
`entities/kancelar/outbox/KAN__literary-journal-feed-r02-norm-review__KOO.md`

commit:
`603c6a4fb02733d8e807bd6d7f2c5d3434f0ba92`

blob:
`231cac214e3e616846cbffface3318939196be79`

terminal:
`PASS_KAN_JOURNAL_FEED_R02_NORMATIVE_READY_FOR_KOO_GATE`

Successor delta:
`entities/kancelar/outbox/KAN__task-conveyor-v1_3-journal-feed-r02-delta-candidate__KOO.md`

commit:
`d06773bbd91f1105e6c2657f6a3ccf8f51748e00`

blob:
`1f561d4a0e0c8f8129687ed609aca4397d817b39`

status:
`candidate / not approved / not active`

## Current active source

`task-conveyor-canon-v1_2-approved.md`

Active v1.2 already contains:
- optional positive `JOURNAL_CANDIDATE` fast path;
- KOO batching;
- RED editorial filter;
- no automation;
- no automatic journal inclusion.

Exact journal-feed subsection and insertion area before `## 11. Failure modes` were verified present.

## Proposed single-source successor

`task-conveyor-canon-v1_2-approved.md`
→
`task-conveyor-canon-v1_3-approved.md`

Only task-conveyor canon changes.

## Sources explicitly unchanged

- project core;
- entity roles;
- file-work canon;
- source-loading policy;
- recovery canon.

## Exact v1.3 meaning

`JOURNAL_CANDIDATE` remains optional fast path.

Additionally, during each normal fresh KOO reconciliation, KOO performs one bounded significance sweep only over new terminal results after the saved cursor.

The sweep is incremental triage, not per-result classification or reporting.

KOO records only positive pending refs and the cursor boundary.
Routine negative decisions are not separately recorded.

RED remains the sole editorial filter and decides include / merge / defer / reject.

## Minimal operational state

v1.3 requires only:

`last_scanned_commit + pending_candidate_refs + last_red_journal_sweep_ref`

This is operational KOO current-state, not a new Project Source and not a required per-cycle artifact.

Exact filename is not mandated.

## Cursor semantics

`last_scanned_commit` advances after every successfully completed bounded significance sweep, including sweeps with zero candidates.

If candidates are found, cursor may still advance while their exact refs remain in `pending_candidate_refs`.

If scan range is incomplete, ambiguous, contains a gap, or cannot be deterministically linked to the previous cursor, cursor MUST NOT advance.

No full-history reconstruction by guess is allowed.

After RED journal-sweep:
- processed refs are removed from pending;
- rejected routine/duplicate refs count as processed;
- `last_red_journal_sweep_ref` is updated to the exact RED terminal identity.

## Initial activation baseline

On first activation of v1.3:
- no historical full scan;
- initial `last_scanned_commit` = exact verified activation/reconciliation boundary of v1.3;
- only already known explicit unprocessed signals may seed `pending_candidate_refs` without historical scan;
- historical backfill requires a separate explicitly authorized bounded task.

## Mandatory anti-bureaucracy boundaries

The successor MUST preserve:
- `JOURNAL_CANDIDATE` optional fast path;
- no full-history rescan;
- no mandatory classification of every result;
- no per-task reporting;
- no mandatory `JOURNAL_CANDIDATE: no`;
- no separate artifact for routine result;
- no automation / cron / scheduler;
- no automatic journal inclusion;
- no new Project Source;
- no new Entity role;
- OPERATOR is not a manual literary dispatcher;
- RED remains editorial filter.

## Effectivity

v1.3 is NOT active merely because this decision gate exists.

After explicit OPERATOR approval KOO must:
1. materialize full `task-conveyor-canon-v1_3-approved.md` from active v1.2 plus only the exact KAN delta;
2. update only version/lineage/service-card fields required by the successor;
3. perform exact readback and structural comparison;
4. perform source activation/readback barrier;
5. mark v1.3 active only after barrier PASS;
6. initialize journal-feed operational state at the exact activation boundary, with no historical full scan.

Until that PASS, v1.2 remains active.

## Decision requested

`APPROVE_TASK_CONVEYOR_CANON_V1_3_INCREMENTAL_JOURNAL_FEED`

Any other response does not approve or activate v1.3.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED