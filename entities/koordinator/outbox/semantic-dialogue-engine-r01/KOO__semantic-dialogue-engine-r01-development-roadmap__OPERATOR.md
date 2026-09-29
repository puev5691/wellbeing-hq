# SEMANTIC_DIALOGUE_ENGINE_R01 — development roadmap

status: DEVELOPMENT_PLAN_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Human purpose

Build one semantic dialogue engine reusable by:
- internal Entity/project work;
- Telegram multi-model dialogue;
- media/information portal;
- contribution/task/contract/accounting layer of the project economy.

The engine must keep human dialogue normal while internally structuring meaning, evidence, state, memory, decisions and causality.

## Existing design inputs

ECL r0.1:
puev5691/wellbeing-hq@1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f

Semantic Dialogue Lexicon r0.1:
puev5691/wellbeing-hq@df4cce558482e9c6c9664120fd4ceaa04081ea04

Semantic Relations Lexicon r0.1:
puev5691/wellbeing-hq@653ba2de3c04238b21e258c4172826a392875347

Package index:
puev5691/wellbeing-hq@d4fa522c25306c3c1bcc7cce162505bafda4e784

CONTEXT_PACKET r0.1:
working candidate exists locally but durable GitHub fixation remains pending.

## Core architecture

INGRESS
-> event/message normalization
-> semantic extraction
-> semantic relations
-> current-state resolution
-> relevant memory/experience retrieval
-> CONTEXT_PACKET
-> ECL command
-> provider/role routing
-> provider calls
-> provider response normalization
-> arbitration/synthesis
-> continuity validation
-> human response
-> durable semantic memory/index update

## Application profiles

### PROFILE A — PROJECT_OPERATIONS

Purpose:
Entity/task/authority/continuity work.

Key semantic objects:
TASK
AUTHORITY
DECISION
ACTION
RESULT
BLOCKER
TERMINAL
HANDOFF
MEMORY
EXPERIENCE

### PROFILE B — MEDIA_PORTAL

Purpose:
argumented, source-transparent, human-friendly dialogue from publications without advertising influence.

Key objects:
PUBLICATION
CLAIM
SOURCE
EVIDENCE
ARGUMENT
COUNTERARGUMENT
INTERPRETATION
UNCERTAINTY
CORRECTION
UPDATE
QUESTION

Desired modes:
EXPLAIN
VERIFY
SHOW_ARGUMENTS
WHAT_IS_DISPUTED
SHOW_SOURCE
WHAT_CHANGED
CONSEQUENCES_BY_EXPLICIT_CONDITIONS

### PROFILE C — PROJECT_ECONOMY

Purpose:
connect semantic events to contribution accounting, task marketplace, contracts and crypto-platform accounting.

Key objects:
CONTRIBUTION
TASK
OFFER
DELIVERY
ACCEPTANCE
OBLIGATION
CONTRACT
REWARD
PENALTY
ENTITLEMENT
SETTLEMENT
DISPUTE
REPUTATION
RESOURCE

Core causal line:
dialogue
-> contribution/task candidate
-> task
-> execution
-> result
-> verification
-> acceptance
-> accounting event
-> contract/settlement event

Rule:
model opinion never directly creates reward/entitlement.
Economic effect requires explicit evidence + task/contract/acceptance chain.

## Provider targets

OpenAI
Anthropic
Gemini
DeepSeek

Roles are dynamic, not brand-fixed.

## Workstreams

W1 KOD — technical architecture skeleton
- provider-neutral interfaces
- provider response normalization
- schema boundaries
- storage/runtime boundaries
- test harness outline
- no live provider calls yet

W2 SHT — process/semantic state model
- validate semantic object lifecycle
- validate profile A/B/C boundaries
- define state transitions and failure states
- identify what may become machine-checkable
- identify where human/OPERATOR decision remains mandatory

W3 SHD — adversarial integration review
- multi-provider disagreement/failure modes
- Telegram/event ordering
- stale context
- duplicate/replay
- partial provider outage
- source/evidence conflict
- media claim arbitration
- contribution/accounting abuse cases
- blockchain/contract boundary risks

W4 RED — human-interface/media dialogue profile
status: PLANNED_PENDING_CURRENT_WRITER_RECONCILIATION
- readable response forms
- argument/source presentation
- uncertainty explanation
- publication-to-dialogue UX
- no-ad influence boundary

W5 SIS — runtime/infrastructure
status: NOT_ISSUED while current gateway retirement line remains active
- secrets
- queues
- logs
- storage
- deployment
- observability

## Dependency order

KOD W1 and SHT W2 may run in parallel.

SHD W3 may run in parallel as an adversarial constraints study, but implementation review waits for KOD/SHT outputs.

RED W4 may start after writer verification.

SIS W5 starts only after architecture has a bounded runtime candidate and current SIS priority line is free.

## First integration checkpoint

Inputs:
- KOD architecture + provider normalization
- SHT semantic/process review
- SHD adversarial constraints

KOO then reconciles into:
SEMANTIC_DIALOGUE_ENGINE_R01_ARCHITECTURE_CANDIDATE

Then:
independent review -> bounded offline simulator -> provider sandbox -> Telegram/media pilot -> economy integration pilot.

## Boundary

No live provider calls.
No Telegram production mutation.
No blockchain/accounting mutation.
No credential work.
No Project Sources/canon mutation.
No automatic activation.

terminal:
SEMANTIC_DIALOGUE_ENGINE_R01_DEVELOPMENT_PLAN_READY_FOR_PARALLEL_DESIGN
