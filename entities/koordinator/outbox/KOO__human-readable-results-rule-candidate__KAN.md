# KOO → KAN: candidate norm for human-readable Russian project results

status: TASK
execution_mode: BOUNDED_NORMATIVE_CANDIDATE_DRAFT
approved_source_mutation_authority: no
source_activation_authority: no
project_time: omitted; trusted project-time source not used

## OPERATOR instruction

ОПЕРАТОР поручил подготовить изменение действующих правил проекта, которое сделает человекочитаемое русское изложение нормой для результатов работы Сущностей, не создавая дополнительной бюрократии и не ухудшая точность технических данных.

Новая норма становится действующей только после отдельного явного решения ОПЕРАТОРА и предусмотренной процедуры активации источников.

## Exact active source basis

Use only the currently active approved source set and exact task evidence.

Relevant approved sources:

- `project-instructions-core-v2_2-approved.md`
- `entity-roles-short-v2_4-approved.md`
- `file-work-canon-universal-v2_4-approved.md`
- `source-loading-policy-v2_2-approved.md`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`
- `task-conveyor-canon-v1-approved.md`

Do not edit or supersede any approved source in this task.

## Existing relevant rules that MUST be reconciled, not duplicated

From project core:
- verified results;
- minimal document flow;
- no new approved norm without OPERATOR decision.

From file-work canon:
- documents exist only when useful;
- one task → one result → one short fixation;
- human-facing documents begin with short meaning/purpose/required action/status;
- service/provenance data go below;
- RED role translates materials into readable-first format.

From entity roles:
- KAN owns short policy/regulation boundaries and must not create bureaucracy;
- RED owns readable text/readability and may not change factual status.

## Problem to solve

A significant share of results/states/reports is currently understandable mainly through:
- machine identifiers;
- English terminal statuses;
- technical field names;
- commit/locator/path constructions.

These are needed for verification/automation, but the human meaning is often not stated plainly.

The required human-facing order is:

`что произошло → что это означает → что теперь возможно, разрешено или требуется`

Only after that, when useful, provide exact:
- machine status;
- version;
- commit/blob/tree;
- locator;
- path;
- protocol field;
- other literal technical evidence.

Literal technical material must remain literal where changing it would reduce correctness:
source code, commands, config, logs, protocol fields, identifiers and machine-readable values.

## KAN task

Prepare one concise normative candidate.

Primary question:
Is the minimal proper normative location an amendment to
`project-instructions-core`
rather than a separate new source or a duplicated amendment to file-work canon?

Default presumption:
prefer a short delta to project core because the rule is cross-cutting and applies to human-facing results beyond formal documents.

Override that presumption only if an active source creates a clear conflict.

## Required output

Create one candidate file only:

`entities/kancelar/outbox/KAN__human-readable-results-rule-candidate__KOO-RED.md`

Status must be clearly:
`candidate / not approved / not active`.

The candidate must contain:

### 1. Recommended normative location

State the exact source and insertion point/section.

Prefer an existing section or one short new subsection.
Do not propose a new standalone canon unless strictly necessary.

### 2. Exact proposed delta

Provide the exact Russian text proposed for insertion.

The norm should be short enough to live in core instructions without turning them into a style manual.

It must establish:

- for material intended for human understanding, first explain in normal Russian:
  what happened → what it means → what is now possible/allowed/required;

- exact machine identifiers/statuses/versions/commits/locators/paths follow as technical verification data when needed;

- technical accuracy has priority and literal technical material is not translated/rephrased when literal preservation matters;

- the rule does not require creation of extra documents, reports, summaries, cover notes or duplicate “human-readable versions” if the same artifact can contain the readable explanation;

- purely machine-consumed artifacts/logs/config/code/protocol data are exempt from prose rewriting;

- when a result is both human- and machine-consumed, readable explanation and exact machine fields coexist in the same result where practical;

- an English machine status alone is not considered sufficient human-facing explanation when the result is addressed to OPERATOR or another human reader.

### 3. Non-duplication / minimal-document-flow check

Explicitly check against:
- file-work canon §4.1 minimal document flow;
- file-work canon §23 document format;
- RED role readable-first;
- core minimal document flow.

State why the proposed delta complements rather than duplicates them.

### 4. Scope boundaries

State that the candidate does NOT:
- require translation of source code/commands/config/logs/protocol literals;
- change machine status vocabularies;
- alter delivery/recovery/task-conveyor protocols;
- create new mandatory artifacts;
- approve a human-readable event journal;
- activate itself.

### 5. RED review handoff

State what RED should review:
- readability of the exact proposed text;
- natural Russian wording;
- preservation of technical meaning;
- absence of stylistic overgrowth.

RED must not expand the norm or add journal requirements in this review.

## Quality gate

The candidate is acceptable only if it improves human understanding without:
- lowering technical precision;
- adding mandatory document types;
- duplicating active canons;
- obstructing automation/parsing;
- turning machine fields into prose-only text.

## Terminal result

Return exactly one:

`PASS_KAN_HUMAN_READABLE_RESULTS_RULE_CANDIDATE_READY_FOR_RED_REVIEW`

or

`BLOCKED_KAN_HUMAN_READABLE_RESULTS_RULE_CANDIDATE: <exact blocker>`

or exact FAIL.

Terminal result must include:
- candidate file locator/commit/blob;
- recommended normative location;
- short explanation why no other approved source needs simultaneous amendment;
- confirmation: approved source mutations = 0;
- next owner: RED for bounded readability review.

Address result to KOO and RED.
Stop after terminal result.
