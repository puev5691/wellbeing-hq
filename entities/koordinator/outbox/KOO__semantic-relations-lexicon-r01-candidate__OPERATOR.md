# Semantic Relations Lexicon r0.1

status: CANDIDATE_READY_NOT_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Role

Companion to:

Semantic Dialogue Lexicon r0.1
puev5691/wellbeing-hq@df4cce558482e9c6c9664120fd4ceaa04081ea04:
entities/koordinator/outbox/KOO__semantic-dialogue-lexicon-r01-candidate__OPERATOR.md
blob 414e2fb05e35718ec0dc2e1ea2a3e46f5ea72b79

Entity Command Layer / ECL r0.1
puev5691/wellbeing-hq@1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f:
entities/koordinator/outbox/KOO__entity-command-layer-ECL-r01-candidate__OPERATOR.md
blob 98cdd744972fcfd47f2aa2ece2a862d97b785061

Purpose:
define the first controlled vocabulary of relations between semantic units in the future Semantic Dialogue Engine.

This is not Project Core, not a canon, and not active authority.

## Principle

A semantic engine needs not only typed units, but typed edges between them.

Minimal relation record:

subject
relation
object
source_ref
status
evidence_refs
confidence_or_verification_state

Relation itself does not create truth or authority.

## Core relations

### ПОДТВЕРЖДАЕТ / SUPPORTS

Meaning:
subject provides evidence that increases support for object.

Typical:
DATA -> FACT candidate
OBSERVATION -> CONCLUSION
RESULT -> ASSUMPTION

Rule:
SUPPORTS is not equivalent to PROVES.

### ОПРОВЕРГАЕТ / REFUTES

Meaning:
subject provides evidence incompatible with object under the same relevant conditions.

Typical:
FACT -> ASSUMPTION
RESULT -> CONCLUSION

Rule:
must preserve scope/conditions of refutation.

### ПРОТИВОРЕЧИТ / CONTRADICTS

Meaning:
subject and object cannot both be accepted as stated within the same scope/context.

Rule:
contradiction triggers reconciliation; no last-write-wins.

### СЛЕДУЕТ_ИЗ / DERIVED_FROM

Meaning:
subject is inferred from object or object set through ANALYSIS.

Typical:
CONCLUSION -> FACT/DATA/ASSUMPTION set

Rule:
dependency chain must remain inspectable.

### ПОРОЖДАЕТ / PRODUCES

Meaning:
subject causally or procedurally creates object.

Typical:
DECISION -> ACTION
ACTION -> RESULT
RESULT -> EXPERIENCE
PROBLEM -> QUESTION

Rule:
PRODUCES does not imply authority unless separately present.

### ЗАВИСИТ_ОТ / DEPENDS_ON

Meaning:
subject cannot be correctly resolved/executed without object.

Typical:
ACTION -> AUTHORITY
DECISION -> DATA
TASK -> prerequisite

Rule:
missing dependency can create BLOCKER/UNKNOWN.

### БЛОКИРУЕТ / BLOCKS

Meaning:
subject prevents progression of object toward its next valid state.

Typical:
PROBLEM -> ACTION
UNKNOWN -> DECISION
ACTIVE_DEPENDENCY -> RETIREMENT

Rule:
BLOCKS must identify affected continuation when known.

### РАЗБЛОКИРУЕТ / UNBLOCKS

Meaning:
subject removes a previously established blocker for object.

Rule:
UNBLOCKS must refer to the exact blocker/state it resolves.

### ЗАМЕНЯЕТ / SUPERSEDES

Meaning:
subject becomes the current successor of object for a defined scope.

Rule:
must preserve old object as historical evidence.
SUPERSEDES does not erase prior result.

### УТОЧНЯЕТ / REFINES

Meaning:
subject narrows, specifies or clarifies object without replacing its core identity.

Typical:
new DATA -> IDEA
correction -> RULE candidate

### ИСПРАВЛЯЕТ / CORRECTS

Meaning:
subject explicitly changes an erroneous or defective part of object.

Rule:
correction scope must be explicit; unchanged parts remain unchanged.

### ДОПОЛНЯЕТ / EXTENDS

Meaning:
subject adds non-conflicting information or scope to object.

Rule:
EXTENDS does not silently supersede.

### ОБЪЕДИНЯЕТ / COMBINES

Meaning:
subject is a synthesis constructed from multiple objects.

Typical:
SYNTHESIS -> several ANALYSIS outputs

Rule:
source components remain traceable.

### РАЗДЕЛЯЕТ / SPLITS

Meaning:
subject decomposes object into several distinct semantic units/scopes.

Typical:
MESSAGE -> THOUGHT units
PROBLEM -> subproblems

### ОТВЕЧАЕТ_НА / ANSWERS

Meaning:
subject resolves or partially resolves object QUESTION.

Rule:
may be COMPLETE, PARTIAL or UNVERIFIED.

### ТРЕБУЕТ / REQUIRES

Meaning:
subject explicitly needs object before valid continuation.

Typical:
RETIREMENT -> PRESERVATION
ACTION -> AUTHORITY

### РАЗРЕШАЕТ / AUTHORIZES

Meaning:
subject grants permission for object within an explicit scope.

Rule:
only a valid AUTHORITY/DECISION source may create this relation.
Model inference cannot create AUTHORIZES.

### ЗАПРЕЩАЕТ / PROHIBITS

Meaning:
subject forbids object within an explicit scope.

Rule:
must preserve authority/provenance.

### АКТИВИРУЕТ / ACTIVATES

Meaning:
subject starts an already-authorized execution instance.

Rule:
AUTHORIZES != ACTIVATES.
File appearance/dispatch/inbox does not imply ACTIVATES.

### ЗАВЕРШАЕТ / COMPLETES

Meaning:
subject establishes completion of object under its completion criterion.

Rule:
execution completion != handoff completion unless both criteria are satisfied.

### ПОТРЕБЛЯЕТ / CONSUMES

Meaning:
subject makes an execution instance non-replayable after terminal completion.

Rule:
CONSUMED does not invalidate historical evidence.

### ПРИНАДЛЕЖИТ_К / BELONGS_TO

Meaning:
subject is part of object context/contour/task/thread.

Typical:
THOUGHT -> MESSAGE
TASK -> PROJECT_LINE
FILE -> LEGACY_CONTOUR

Rule:
membership does not create mutation authority.

### ССЫЛАЕТСЯ_НА / REFERENCES

Meaning:
subject explicitly points to object without asserting truth, ownership or authority.

### ИСТОЧНИК_ДЛЯ / SOURCE_FOR

Meaning:
subject is provenance for object.

Rule:
source provenance and semantic truth remain separate.

### СОЗДАНО_ИЗ / EXTRACTED_FROM

Meaning:
subject semantic unit was extracted from object message/document/data.

Typical:
THOUGHT -> MESSAGE

### ПОДТВЕРЖДЕНО_ИСТОЧНИКОМ / VERIFIED_BY

Meaning:
subject has been checked against object source/evidence and matched under the stated verification criterion.

Rule:
verification criterion must be known.

### ТРЕБУЕТ_ПРОВЕРКИ / NEEDS_VERIFICATION

Meaning:
subject cannot safely be promoted/used for the requested purpose without additional verification.

### СОГЛАСУЕТСЯ_С / AGREES_WITH

Meaning:
subject and object are materially consistent.

Rule:
agreement between models is not FACT proof.

### РАСХОДИТСЯ_С / DISAGREES_WITH

Meaning:
subject and object reach materially different claims/options/conclusions.

Rule:
disagreement is an arbitration input, not a failure by itself.

### ПРЕДШЕСТВУЕТ / PRECEDES

Meaning:
subject comes before object in an established causal/procedural order.

Rule:
chronology alone does not prove causation.

### ВЫЗЫВАЕТ / CAUSES

Meaning:
subject is established as a causal contributor to object.

Rule:
use only when causal evidence is sufficient; otherwise use ASSUMPTION + SUPPORTS.

### СВЯЗАНО_С / RELATED_TO

Meaning:
weak generic relation when a more precise relation is not yet established.

Rule:
should be refined later where possible.
Do not use RELATED_TO as a substitute for unknown causality.

## Relation families

Evidence:
SUPPORTS
REFUTES
CONTRADICTS
VERIFIED_BY
NEEDS_VERIFICATION

Reasoning:
DERIVED_FROM
REFINES
CORRECTS
EXTENDS
COMBINES
SPLITS

Causality/process:
PRODUCES
CAUSES
PRECEDES
COMPLETES
CONSUMES

Dependency/control:
DEPENDS_ON
REQUIRES
BLOCKS
UNBLOCKS

Authority:
AUTHORIZES
PROHIBITS
ACTIVATES

Dialogue:
ANSWERS
EXTRACTED_FROM
REFERENCES
SOURCE_FOR
BELONGS_TO

Arbitration:
AGREES_WITH
DISAGREES_WITH

Fallback:
RELATED_TO

## Directionality

Relations are directional unless explicitly modeled as symmetric.

Symmetric candidates:
CONTRADICTS
AGREES_WITH
DISAGREES_WITH
RELATED_TO

All others are directional by default.

## Critical non-equivalences

SUPPORTS != PROVES
AGREES_WITH != VERIFIED_BY
REFERENCES != SOURCE_FOR
BELONGS_TO != AUTHORIZES
AUTHORIZES != ACTIVATES
ACTIVATES != COMPLETES
COMPLETES != CONSUMES
PRECEDES != CAUSES
REFINES != SUPERSEDES
CORRECTS != SUPERSEDES unless exact scope says so
RELATED_TO != CAUSES

## Candidate edge schema

relation_id
subject_id
relation_type
object_id
scope
source_ref
evidence_refs
status
created_from
verification_state

Candidate verification_state:
VERIFIED
UNVERIFIED
DISPUTED
STALE
SUPERSEDED

## Example: conveyor failure

OBSERVATION_1
"terminal есть, следующий шаг не выдан"

BLOCKS -> GOAL_CONTINUOUS_CONVEYOR

IDEA_1
"обязательный terminal return KOO"

ANSWERS -> PROBLEM_HANDOFF_LOSS

DECISION_1
"ввести mandatory return"

AUTHORIZES -> ACTION_UPDATE_HANDOFF_RULE

RESULT_1
"KOO получает terminal и выбирает следующий шаг"

SUPPORTS -> IDEA_1

EXPERIENCE_1
"execution terminal без handoff недостаточен"

DERIVED_FROM -> RESULT_1

## Example: multi-model arbitration

CLAIM_OPENAI
DISAGREES_WITH -> CLAIM_DEEPSEEK

SOURCE_DATA_1
SUPPORTS -> CLAIM_OPENAI

SOURCE_DATA_2
CONTRADICTS -> CLAIM_OPENAI

SYNTHESIS
COMBINES -> CLAIM_OPENAI
SYNTHESIS
COMBINES -> CLAIM_DEEPSEEK

SYNTHESIS
NEEDS_VERIFICATION -> QUESTION_MISSING_EVIDENCE

No provider majority creates VERIFIED_BY.

## Engine rule

Prefer the most precise relation supported by evidence.

If no precise relation is established:
use RELATED_TO or UNKNOWN rather than inventing causality/authority.

## Planned parent specification

SEMANTIC_DIALOGUE_ENGINE_R01

Companion candidates:
- Semantic Dialogue Lexicon r0.1
- Semantic Relations Lexicon r0.1
- Entity Command Layer / ECL r0.1
- future CONTEXT_PACKET schema
- future semantic memory/index
- future arbitration/synthesis policy

## Boundary

This candidate does NOT:
- activate implementation;
- change Project Sources/canons;
- create project authority;
- modify task priority;
- define final storage format;
- require visible graph markup in human chats.

terminal:
CANDIDATE_SEMANTIC_RELATIONS_LEXICON_R01_READY_FOR_DESIGN_REVIEW
