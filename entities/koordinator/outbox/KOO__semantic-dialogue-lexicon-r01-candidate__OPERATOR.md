# Semantic Dialogue Lexicon r0.1

status: CANDIDATE_READY_NOT_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Role

This lexicon is a semantic companion to:

Entity Command Layer / ECL r0.1

puev5691/wellbeing-hq@1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f:
entities/koordinator/outbox/KOO__entity-command-layer-ECL-r01-candidate__OPERATOR.md

It is intended for the future Semantic Dialogue / Context Engine used by human-readable chats and multi-model orchestration.

It is NOT Project Core, not a canon, and not active authority.

## Principle

The engine should process dialogue as typed semantic units rather than undifferentiated transcript text.

One message may contain several semantic units.

Each semantic unit has:
- type;
- source;
- current status;
- causal parent where known;
- evidence refs where applicable;
- possible next transformations.

## Core semantic types

### МЫСЛЬ / THOUGHT

Meaning:
minimal self-contained semantic unit extracted from a message.

Created from:
human or model message.

May become:
FACT, DATA, OBSERVATION, QUESTION, IDEA, ASSUMPTION, ANALYSIS, CONCLUSION, OPTION, DECISION, ACTION, RESULT, PROBLEM, UNKNOWN, GOAL, RULE.

Engine rule:
a message may contain multiple THOUGHT units.
THOUGHT itself does not imply truth or authority.

### ФАКТ / FACT

Meaning:
a proposition supported by sufficient verifiable evidence under the current context.

Created from:
verified DATA, RESULT, SOURCE, or authoritative state.

May become:
input to ANALYSIS, DECISION, MEMORY, EXPERIENCE.

Engine rule:
must retain provenance.
Model output or memory hint never self-promotes to FACT.

### ДАННЫЕ / DATA

Meaning:
received information before final interpretation.

Examples:
API response, log line, measurement, document field, tool output.

May become:
FACT, OBSERVATION, UNKNOWN, input to ANALYSIS.

Engine rule:
DATA is not automatically FACT.

### НАБЛЮДЕНИЕ / OBSERVATION

Meaning:
what was directly noticed or measured now, without causal explanation.

Created from:
DATA, direct tool output, human report.

May become:
FACT if verified, ASSUMPTION, ANALYSIS input, PROBLEM.

### ПАМЯТЬ / MEMORY

Meaning:
preserved context from prior interaction or state that may be relevant later.

Contains:
facts, preferences, decisions, summaries, pointers.

May become:
context input.

Engine rule:
memory is context, not current truth or authority by itself.

### ОПЫТ / EXPERIENCE

Meaning:
causally compressed record of a prior attempt:
idea -> action/probe -> result -> success/failure -> lesson.

Created from:
completed RESULT plus ANALYSIS.

May become:
MEMORY, RULE candidate, ANALYSIS input.

Engine rule:
experience must preserve the conditions under which the lesson was learned.

### ВОПРОС / QUESTION

Meaning:
explicitly missing knowledge that blocks or improves continuation.

Created from:
human inquiry, UNKNOWN, ANALYSIS gap.

May become:
DATA request, research task, ANSWER/FACT.

Engine rule:
question should identify what evidence would resolve it where possible.

### ИДЕЯ / IDEA

Meaning:
proposed possibility worth considering, not yet selected or proven.

May become:
ASSUMPTION, OPTION, ANALYSIS input, candidate RULE, DECISION.

Engine rule:
IDEA is not DECISION.

### ПРЕДПОЛОЖЕНИЕ / ASSUMPTION

Meaning:
tentative explanatory or predictive proposition lacking sufficient evidence.

Created from:
ANALYSIS, OBSERVATION, IDEA.

May become:
FACT if verified, rejected hypothesis, UNKNOWN.

Engine rule:
must remain visibly non-factual until verified.

### АНАЛИЗ / ANALYSIS

Meaning:
reasoned relation among FACT, DATA, OBSERVATION, EXPERIENCE, RULE, ASSUMPTION and GOAL.

Produces:
CONCLUSION, OPTION, QUESTION, UNKNOWN, PROBLEM.

Engine rule:
analysis is a transformation process, not an authority grant.

### ВЫВОД / CONCLUSION

Meaning:
proposition inferred from current analysis and evidence.

Created from:
ANALYSIS.

May become:
DECISION input, FACT only after appropriate verification when needed.

Engine rule:
retain dependency on evidence and assumptions.

### ВАРИАНТ / OPTION

Meaning:
one possible course of continuation.

Created from:
ANALYSIS, IDEA, CONCLUSION.

May become:
DECISION.

Engine rule:
an option is neither chosen nor authorized merely because it exists.

### РЕШЕНИЕ / DECISION

Meaning:
explicitly selected option by an authorized decision-maker for the relevant scope.

Created from:
OPTION plus decision authority.

May become:
ACTION authority input, RULE, MEMORY.

Engine rule:
DECISION != ACTION != RESULT.

### ДЕЙСТВИЕ / ACTION

Meaning:
an operation actually requested or performed.

Created from:
DECISION, TASK, command.

May become:
RESULT.

Engine rule:
planned action and observed action must be distinguishable.

### РЕЗУЛЬТАТ / RESULT

Meaning:
observed outcome of an action or process.

Created from:
ACTION execution or external event.

May become:
FACT, EXPERIENCE, PROBLEM, new ANALYSIS.

Engine rule:
intended result is not observed result.

### ПРОБЛЕМА / PROBLEM

Meaning:
a condition preventing or degrading progress toward a GOAL.

Includes:
BLOCKER, contradiction, missing dependency, failed operation.

May become:
QUESTION, ANALYSIS, TASK, DECISION.

Engine rule:
problem statement should identify affected goal/task when known.

### НЕИЗВЕСТНО / UNKNOWN

Meaning:
required knowledge or state is not established by current evidence.

Created from:
evidence gap, conflict, stale state.

May become:
QUESTION, research task, DATA.

Engine rule:
UNKNOWN must not be silently guessed away.

### ЦЕЛЬ / GOAL

Meaning:
desired future state or outcome.

Created by:
human intent, approved project objective.

May create:
QUESTION, ANALYSIS, OPTION, TASK.

Engine rule:
goal does not create execution authority.

### ПРАВИЛО / RULE

Meaning:
a constraint or repeatable instruction governing interpretation or action.

Created from:
approved governance, explicit instruction, validated experience promoted through proper authority.

May constrain:
ANALYSIS, DECISION, ACTION, VALIDATION.

Engine rule:
candidate rule and active rule must be distinct.

### КОНТЕКСТ / CONTEXT

Meaning:
the bounded set of currently relevant semantic units, state and evidence for one reasoning cycle.

Constructed from:
current message, MEMORY, EXPERIENCE, RULE, TASK, STATE, evidence refs.

Engine rule:
context should be minimal sufficient, not full transcript by default.

### ИСТОЧНИК / SOURCE

Meaning:
origin of DATA, FACT, RULE, MEMORY or other semantic unit.

Examples:
human message, approved file, Git commit/blob, tool result, external document.

Engine rule:
source provenance is preserved separately from semantic interpretation.

## Auxiliary semantic statuses

Candidate statuses:

CURRENT
STALE
VERIFIED
UNVERIFIED
SUPERSEDED
BLOCKED
CONSUMED
PENDING
UNKNOWN

These statuses describe semantic/state condition and do not automatically map to Task Conveyor machine classes.

## Suggested transformation graph

MESSAGE
-> one or more THOUGHT

THOUGHT
-> semantic type

MEMORY + EXPERIENCE + CURRENT CONTEXT + NEW DATA
-> ANALYSIS
-> CONCLUSION / OPTION / QUESTION / UNKNOWN
-> DECISION
-> ACTION
-> RESULT
-> EXPERIENCE / MEMORY / new ANALYSIS

## Critical distinctions

MEMORY != FACT
DATA != FACT
OBSERVATION != EXPLANATION
IDEA != DECISION
ASSUMPTION != FACT
ANALYSIS != DECISION
DECISION != ACTION
ACTION != RESULT
RESULT != EXPERIENCE
GOAL != AUTHORITY
SOURCE != TRUTH
MODEL CONSENSUS != FACT

## Multi-model use

For each provider response, the engine should normalize output into semantic units rather than compare prose blobs.

Arbitration input should support:
- FACT claims;
- DATA references;
- ASSUMPTIONS;
- ANALYSIS;
- CONCLUSIONS;
- OPTIONS;
- QUESTIONS;
- UNKNOWNs;
- dissent/conflict markers.

Provider agreement is evidence of agreement only, not proof of truth.

## Human-readable chat use

The human-facing chat remains normal prose.

Semantic tags are internal by default and surfaced only when useful.

Example human message:

"Сущности опять остановили конвейер. Наверное завершение задачи надо делать докладом координатору."

Candidate semantic extraction:

OBSERVATION:
конвейер снова остановился

IDEA:
завершение задачи должно включать адресный доклад координатору

## Future instruction linkage

Planned parent specification:

SEMANTIC_DIALOGUE_ENGINE_R01

Planned companion components:
- ECL command layer
- CONTEXT_PACKET schema
- semantic memory/index
- provider response normalization
- arbitration/synthesis policy
- continuity validator

## Boundary

This lexicon does NOT:
- activate implementation;
- change Project Sources/canons;
- create authority;
- alter task priority;
- define final machine schema;
- require visible tagging in human chats.

terminal:
CANDIDATE_SEMANTIC_DIALOGUE_LEXICON_R01_READY_FOR_DESIGN_REVIEW
