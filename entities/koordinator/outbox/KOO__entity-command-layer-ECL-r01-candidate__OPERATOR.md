# KOO candidate: Entity Command Layer / ECL r0.1

status: CANDIDATE_READY_NOT_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Purpose

Create a compact structured command layer for Entities and the future multi-model Telegram context engine.

Goal:
replace long prose prompts with small machine-readable command objects plus separately referenced state/evidence.

## Core split

1. BEHAVIOR
Persistent project/model instructions.

2. STATE
Structured current state:
- task
- writer
- authority
- terminal
- blocker
- next transition
- evidence refs

3. COMMAND
One-step executable intent.

4. VALIDATION
Machine/arbiter checks before and after execution.

## Candidate command object

Fields:

command_id
mode
goal
entity
scope
authority_ref
task_ref
state_ref
evidence_refs
constraints
stop_conditions
expected_result
next_action_policy

Candidate modes:

FAST_SINGLE
PRIMARY_PLUS_CRITIC
PARALLEL_PANEL
FACT_THEN_SYNTHESIS
ADVERSARIAL_REVIEW
CONSENSUS_WITH_DISSENT

Candidate controls:

facts:
STRICT | NORMAL

critique:
NONE | OPTIONAL | REQUIRED

authority:
VERIFY | NOT_APPLICABLE

memory:
NONE | RELEVANT_ONLY | EXPLICIT_REFS

continuity:
REQUIRED | OPTIONAL

next_action:
SINGLE | WAIT_BASIS | NONE_JUSTIFIED

## State labels

FACT
INFERENCE
USER_PREFERENCE
PROJECT_RULE
CANDIDATE
UNKNOWN
BLOCKER
AUTHORITY
TASK
TERMINAL
MEMORY_HINT

No model output or memory hint self-promotes to FACT or AUTHORITY.

## Provider arbitration

Initial provider targets:
- OpenAI
- Anthropic
- Gemini
- DeepSeek

Roles are dynamic, not bound permanently to a provider.

Possible roles:
PRIMARY_REASONER
FACT_CHECKER
CRITIC
COUNTERARGUMENT
CODE_SPECIALIST
SOURCE_REVIEWER
SYNTHESIZER
HUMAN_INTERFACE_REVIEW

Arbitration principles:
- no majority vote equals truth;
- freeze same context packet for parallel comparison;
- preserve dissent when evidence remains unresolved;
- synthesis must cite normalized evidence/state, not provider prestige.

## Telegram integration target

Telegram ingress -> normalize event -> resolve state -> build CONTEXT_PACKET -> build COMMAND -> route models -> normalize outputs -> arbitrate -> validate continuity -> human answer -> persist durable state only.

## Search/index target

User messages should be semantically indexed by:
- topic
- intent
- entity/project line
- task/decision/question/idea/result/blocker
- causal parent
- status
- artifact refs
- model cycle

Derived index is searchable context, never authoritative task state.

## Boundaries

This candidate does NOT:
- activate implementation;
- alter current queue priority;
- change Project Sources/canons;
- authorize provider calls;
- authorize Telegram runtime changes;
- authorize credentials;
- activate automation;
- create execution authority.

## Readiness

development_line:
MULTIMODEL_TELEGRAM_CONTEXT_ENGINE_R01

component:
ENTITY_COMMAND_LAYER_ECL_R01

status:
READY_ON_BACKLOG

terminal:
CANDIDATE_ECL_R01_RECORDED_READY_FOR_FUTURE_DESIGN_REVIEW
