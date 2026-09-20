# KOO → KAN: human interface norm + separate literary project journal proposal

status: TASK
execution_mode: BOUNDED_NORMATIVE_DELTA_PREPARATION
approved_source_mutation_authority: no
source_activation_authority: no
project_time: omitted; trusted project-time source not used

## OPERATOR instruction

ОПЕРАТОР уточнил требуемую архитектуру взаимодействия человека и Сущностей.

Главный принцип:

`человеку — человеческие тексты; машинам — машиночитаемые данные; истории проекта — человеческий контекст и события`.

Нужно подготовить минимальную нормативную дельту без лишней бюрократии.

## Current active source state

Source-set r0.4 is active.

Current active project core:
`project-instructions-core-v2_3-approved.md`.

Current active task-conveyor:
`task-conveyor-canon-v1_1-approved.md`.

Other active sources unchanged:
- `entity-roles-short-v2_4-approved.md`;
- `file-work-canon-universal-v2_4-approved.md`;
- `source-loading-policy-v2_2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`.

## Existing reviewed human-readable basis

KAN candidate:
`entities/kancelar/outbox/KAN__human-readable-results-rule-candidate__KOO-RED.md`
commit `4753d2c1903bec2501b7a79c6031068d7b0e2f5a`.

RED review:
commit `fbb2e9d428221dac9f4ab75f1bac7c1ce0f8e2c2`
verdict `PASS_RED_HUMAN_READABLE_RESULTS_RULE_CANDIDATE_R01`.

Use this as reviewed basis. Do not restart the earlier review from zero.

## New OPERATOR clarification to incorporate

For ordinary chat dialogue and human-facing results:

1. The main answer should use normal Russian vocabulary understandable to an ordinary technically literate person who is comfortable with engineering terminology.

2. Chat should show technical details only when they are useful to the human for:
   - understanding the meaning;
   - making a decision;
   - performing a required action;
   - diagnosing a blocker;
   - preserving necessary continuity or handoff.

3. Paths, hashes, commits, blobs, locators, machine statuses, route history and detailed provenance should normally remain in the project information field when they are not needed by the human in the current dialogue.

4. Do not repeat machine-readable evidence in chat merely because it exists in GitHub.

5. Do not hide or simplify technical data when the human actually needs exact values for action, verification, safety, debugging, recovery or transfer.

6. Source code, commands, configuration, logs, protocol fields, identifiers and exact technical values remain literal when literal form matters.

7. No additional mandatory “human version” artifact is created when the same result can contain both the readable explanation and exact machine data.

8. Human-facing response should normally prioritize:
   `что произошло → что это означает → что теперь возможно, разрешено или требуется`.

9. Machine-facing evidence remains available in the information field for Entities, programs and later verification.

## Required minimal normative location

Primary presumption:
amend only `project-instructions-core-v2_3-approved.md` → candidate successor v2.4.

KAN must verify whether this is sufficient.

Do NOT propose changes to file-work canon, roles or task-conveyor unless an actual contradiction or missing mandatory boundary requires it.

The existing manual activation handoff rule in core/conveyor remains in force and is not to be rewritten.

## Required candidate output 1 — general human interface norm

Create one candidate file:

`entities/kancelar/outbox/KAN__human-interface-norm-core-v24-candidate__KOO-RED.md`

Status:
`candidate / not approved / not active`.

It must provide:
- exact insertion point in current core v2.3;
- exact proposed Russian text;
- short non-duplication check against file-work canon and task-conveyor;
- confirmation that no new document type is required;
- confirmation that machine evidence remains in information field and is not lost;
- confirmation that chat brevity must not suppress exact data needed for human action or verification.

Recommended conceptual title:
`## Человекочитаемый интерфейс проекта`
or another equally concise title if KAN finds a better one.

## Required candidate output 2 — separate literary journal proposal

Do NOT mix journal activation into the core-language amendment.

Create a second separate proposal:

`entities/kancelar/outbox/KAN__project-literary-journal-proposal__KOO-RED.md`

Status:
`proposal / not approved / not active`.

Purpose:
define a low-bureaucracy human-readable journal of significant project events that gives RED useful source material for:
- Telegram;
- project portal;
- future book/history of the project.

The proposal should establish only principles, not a heavy workflow.

Required properties:
- not a full transcript of every chat;
- not a duplicate technical log;
- record only significant events, decisions, turning points, failures, discoveries, funny/characteristic episodes, reasons for choices and important human context;
- preserve useful quotations or paraphrased dialogue fragments where appropriate;
- link to technical evidence only when useful, without copying machine detail into the narrative;
- suitable for later editorial selection;
- should not require a new journal document for every task;
- should allow periodic/episodic accumulation rather than per-message bureaucracy;
- should have a clear likely owner or owners, but not silently change approved roles;
- must not become active in this task.

KAN should recommend the minimum future normative location/ownership for this journal, but activation is a separate later decision.

## Scope boundary

This task must NOT:
- modify any active Project Source;
- activate v2.4;
- rewrite task-conveyor v1.1;
- create event-journal automation;
- invent new Entity roles;
- require a separate human-readable copy of every artifact;
- require OPERATOR to manually reconstruct technical evidence from GitHub.

## Next owner after KAN PASS

RED / РЕДАКТОР.

RED bounded review should cover:
- natural Russian;
- clarity for technically literate human readers;
- whether machine detail suppression is bounded safely;
- whether journal proposal is editorially useful without becoming bureaucracy.

RED must not expand technical authority or activate anything.

## Expected terminal result

Return exactly one:

`PASS_KAN_HUMAN_INTERFACE_AND_JOURNAL_CANDIDATES_READY_FOR_RED`

or

`BLOCKED_KAN_HUMAN_INTERFACE_AND_JOURNAL: <exact blocker>`

or exact FAIL.

Address terminal result to KOO and RED.
Stop after terminal result.
