# KOO → KOD: Telegram facilitator core r0.1

status: `TASK_READY`
execution_mode: `FAST_PATH`

## Authority

Operator-approved product direction:
`entities/koordinator/outbox/KOO__telegram-facilitator-product-direction-r01__OPERATOR.md`
commit `26b9c121402a5c72260d1f8d6d3a36d539d2ea78`.

Design input:
`entities/koordinator/outbox/KOO__telegram-media-facilitator-integration-r01__OPERATOR.md`
commit `0c8fa7ff50158411b69f87e3e693c13b5fdb3057`.

## Goal

Implement the first isolated provider-neutral Discussion Facilitation / Task Synthesis core without modifying the accepted Telegram Phase 1B transport/runtime/privacy implementation.

## Required artifact

Create a self-contained candidate package under KOD outbox containing:

1. machine-readable schemas/types for at least:
   - `normalized_event`;
   - `discussion_state`;
   - `candidate_task`;
   - `decision_record`;
2. optionally separate `disagreement`, `candidate_question`, `candidate_summary` if cleaner;
3. deterministic state transition logic;
4. explicit provenance/source references;
5. retention/privacy classification fields;
6. authority boundary: `candidate_task != approved/executable task`;
7. synthetic fixtures covering a small discussion sequence;
8. tests proving no Telegram API, credentials, live provider, production storage or privileged runtime dependency is required;
9. short integration contract showing where this layer plugs into existing Phase 1B after normalization and before approval/dispatch.

## Domain requirements

The core must be able to represent, without making decisions for participants:
- topic/problem;
- concepts/terms needing clarification;
- facts/evidence claims;
- goals;
- criteria;
- means/options;
- procedure/next-step candidates;
- positions;
- preliminary agreements;
- disagreements and their level/type;
- open questions;
- candidate question/summary/task.

These are analysis categories, not hard-coded truth and not automatic consensus.

## Privacy / authority constraints

Do not require persistent raw Telegram message text.
Do not require persistent Telegram user_id/username.
A short-lived processing input may be represented abstractly, but persistent objects must support minimized/derived state.
No automatic publication.
No automatic project-task creation.
No automatic participant agreement claim.
No destructive cleanup.
No Telegram send.
No live LLM call.
No new DB/runtime/service deployment.
No sudo/root.
No TERA2/WBN.

## Compatibility

Existing Telegram Phase 1B transport/runtime must remain byte-unchanged unless an exact change is strictly necessary. If any modification would be required, stop and return a blocker instead of changing it.

## Acceptance

Expected terminal:
`PASS_TELEGRAM_FACILITATOR_CORE_R01_READY_FOR_INDEPENDENT_VERIFY`

or exact `BLOCKED_* / FAIL_*`.

Return immutable candidate identity, tests/check counts, integration boundary, privacy/authority invariants and route result to KOO through Exchange Gate.
