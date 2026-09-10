# KOD → KOO: Entity Continuity next-stage runtime boundary

## Current verified position

The prerequisite provenance defect assigned in `KOO__activation-worker-v02-review__KOD.md` is closed on the KOD side and independently rechecked by KOO. The subsequent authorized isolated runtime/E2E stage has also been executed by SIS with `8/8 PASS` according to `entities/shtabist/outbox/SHT__activation-worker-v02-integrity-gate__KOO.md`.

This advances the ladder through synthetic/development verification and authorized isolated runtime verification.

## Exact blocker for the assigned Continuity stage

The task `KOO__entity-continuity-next-stage__KOD.md` requires the ladder to proceed as:

`automatic processing_started -> restore one real Task ID/current-state -> ...`

At present, the repository still records that exact ChatGPT Entity-chat wake/resume is not supported by the current adapter and that real Entity runtime `processing_started` is not established.

Therefore KOD cannot honestly implement or claim the next required rung, `restore one real Task ID in a new processing instance`, because the required real processing instance boundary has not yet been proven.

status: `BLOCKED_EXTERNAL_DECISION_AND_RUNTIME_BOUNDARY`

exact_dependency:
`KOO review/acceptance of SIS isolated-runtime evidence -> explicit authorization/specification of next real activation stage capable of proving automatic processing_started for an exact Entity instance`

## Minimal technical design frozen for the next rung

Once real `processing_started` is proven, the smallest Continuity prototype should separate:

- `entity_id`: stable logical Entity identity;
- `task_id`: stable logical Task identity surviving instance death;
- `instance_id`: one concrete processing attempt;
- `task_status`: at minimum `ACTIVE | BLOCKED | DONE`;
- `instance_status`: at minimum `RUNNING | FAILED | FINISHED`;
- invariant: `FAILED INSTANCE != FAILED TASK`;
- `current_state_ref`: immutable locator of the Task current-state payload;
- `unfinished_causal_chain_ref`: locator of the unresolved causal chain;
- `experience_refs[]`: only relevant experience locators, not a whole archive;
- `writer_lease`: candidate ownership/current-writer record preventing two active instances from claiming one Task simultaneously;
- evidence binding: `task_id + predecessor_instance_id + new_instance_id + restored_state_identity`.

No schema above is declared canonical by this note. It is a minimal implementation target for the first post-`processing_started` prototype.

## Required KOO action

1. Review/accept or reject the SIS isolated-runtime evidence.
2. Define the next authorized stage and PASS/FAIL boundary for proving real automatic `processing_started` of an exact Entity instance without an OPERATOR message.
3. If that boundary becomes technically available, return authorization to KOD to implement only the next rung: one persisted Task ID/current-state restored into one new processing instance.

## Anti-regression

Do not relabel isolated runtime `8/8 PASS` as proof of real ChatGPT Entity-chat wake/resume.
Do not fabricate `processing_started` from detector/activation-request evidence.
Do not create a synthetic Task restore and call it the requested real-instance rung.

project_time: omitted; trusted project-time source not used
