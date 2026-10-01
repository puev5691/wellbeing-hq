# KOO -> SHT: Semantic Entity Control Engine r0.1 architecture reconciliation

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current SHT writer

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

status:
CURRENT_WRITER

## Exact OPERATOR priority authority

puev5691/wellbeing-hq@8613ec56d65ff52dd887503ba893f2d2a9128613:
entities/koordinator/current/KOO__semantic-entity-control-engine-r01-priority-decision__OPERATOR.md

blob:
d0521905627b306a4888261a9d414148ac64f265

Exact decisions:

SEMANTIC_ENTITY_CONTROL_ENGINE_R01_PRIMARY_PRIORITY = YES
PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE = YES

This authority makes the semantic control line the primary coordination priority.
It does NOT activate any Project Source/canon and does NOT authorize runtime implementation.

## New concept candidate

puev5691/wellbeing-hq@3519f61181ad1c32cd342ec0f9040fc024947b7e:
entities/koordinator/outbox/KOO__semantic-entity-control-engine-concept-r01__PROJECT.md

blob:
badb46346ffde3e4f674ce567d614bedb5af37dc

status:
DESIGN_CONCEPT_CANDIDATE

Core proposed chain:

SEMANTIC_SEED
-> ACTIVE_SOURCE_LOAD
-> NORM_EXTRACTION
-> CURRENT_EVENT/TASK_BINDING
-> PROFILE_SELECTION
-> RELEVANT_EXPERIENCE_RETRIEVAL
-> SEMANTIC_EXECUTION_CONTRACT
-> STATIC_VALIDATION
-> ONE_ALLOWED_STEP
-> RESULT_VALIDATION
-> STATE/FIXATION

## Existing Semantic Bootstrap line

KOO reconciliation:

puev5691/wellbeing-hq@a09d63ae86dbc2e16f6412c4d4f46eb1611b705a:
entities/koordinator/outbox/KOO__entity-semantic-bootstrap-gap-reconciliation-r01__OPERATOR.md

blob:
240d840abcc92537c40a62cb76fb73b8ee224574

Confirmed existing gap:
- no canonical semantic seed representation;
- no deterministic source-to-seed mapping/load contract;
- no mandatory semantic initiation self-test;
- no explicit global bootstrap -> profile -> Entity role -> exact task handoff.

Existing progressive semantic context concepts must be reconciled, not duplicated.

Known last exact Semantic Bootstrap correction task:

puev5691/wellbeing-hq@a9e167acc49aaae40486526a8d3db6c9437f4970:
entities/koordinator/outbox/KOO__entity-semantic-bootstrap-profile-r01-D2-MAP-correction__SHT.md

blob:
dde64ec33e6e428107ec474c57167e3a94d53b10

Fresh KOO search found no terminal result for this historical exact task.

Classification:
HISTORICAL_UNRESOLVED_EVIDENCE
DO_NOT_REPLAY

Use its inputs/status only as evidence when reconciling the architecture.

## Existing Semantic Dialogue Engine line

Development roadmap:

puev5691/wellbeing-hq@ac269e3c1effb3fc6622351db54a2cc8efea8f5e:
entities/koordinator/outbox/semantic-dialogue-engine-r01/KOO__semantic-dialogue-engine-r01-development-roadmap__OPERATOR.md

blob:
9e71944268ab08666abfb5306db4fc15f18fa204

Existing PROJECT_OPERATIONS profile already includes:

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

Existing engine chain includes:

semantic extraction
-> semantic relations
-> current-state resolution
-> relevant memory/experience retrieval
-> CONTEXT_PACKET
-> ECL command
-> provider/role routing
-> response normalization
-> continuity validation
-> durable semantic memory/index update

Existing semantic dialogue design inputs named by that roadmap:

- ECL r0.1
  commit puev5691/wellbeing-hq@1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f

- Semantic Dialogue Lexicon r0.1
  commit puev5691/wellbeing-hq@df4cce558482e9c6c9664120fd4ceaa04081ea04

- Semantic Relations Lexicon r0.1
  commit puev5691/wellbeing-hq@653ba2de3c04238b21e258c4172826a392875347

- semantic dialogue package index
  puev5691/wellbeing-hq@d4fa522c25306c3c1bcc7cce162505bafda4e784

- CONTEXT_PACKET r0.1
  roadmap says local candidate existed but durable GitHub fixation was pending at that point.

Fresh-check all of these before using them.
Do not invent missing durable identities.

## Existing parallel semantic tasks

Historical KOD architecture task:

puev5691/wellbeing-hq@f2d318bc415dd0ae4dec0b9b912a0685b7e97e4:
KOO task KOD semantic dialogue engine r01 architecture

Fresh KOO search found no exact terminal result.

Classification:
HISTORICAL_UNRESOLVED_EVIDENCE
DO_NOT_REPLAY

SHT semantic/process result and SHD adversarial review exist in the Semantic Dialogue Engine line.
Fresh-discover exact locators/identities before relying on them.

## Active Project Sources

Fresh-load exact active sources only:

- Project Core v2.5
  blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33

- Entity Roles v2.4
  blob 1772339cb74dae8550bfbd2e33401c34a929e911

- Source Loading Policy v2.2
  blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf

- Recovery Canon v1.6
  blob 233117e1c9509d730e1f5ec532b1cabe3f786609

- File Work Canon v2.4
  blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2

- Task Conveyor Canon v1.2
  blob df7896d867eeeffff506319538fedad938856686

Pending/candidate sources remain non-active unless exact activation barrier evidence proves otherwise.

## Goal

Produce one unified ARCHITECTURE CANDIDATE that reconciles:

1. Semantic Bootstrap;
2. Semantic Entity Control Engine concept;
3. Semantic Dialogue Engine PROFILE A / PROJECT_OPERATIONS;
4. ECL / lexicons / semantic relations / CONTEXT_PACKET;
5. active Project Sources;
6. Task Conveyor / Recovery / current-writer / authority boundaries.

The result must define how a new Entity instance moves from initiation to exact task execution without relying on free-form helpful self-initiative.

## Required architecture

At minimum reconcile these layers:

L0 ACTIVE AUTHORITATIVE SOURCES
L1 SEMANTIC SEED / INITIATION KERNEL
L2 SOURCE -> OPERATIONAL RULE COMPILER
L3 CURRENT STATE + EVENT/TASK BINDING
L4 PROFILE SELECTION
L5 EXPERIENCE SELECTION
L6 SEMANTIC_EXECUTION_CONTRACT
L7 STATIC VALIDATOR
L8 RUNTIME STEP GUARD / ONE SAFE STEP
L9 RESULT VALIDATOR / FIXATION / NEXT-GATE DERIVATION

For each layer specify:
- inputs;
- outputs;
- what may be neural/probabilistic;
- what must be deterministic/machine-checkable;
- provenance requirements;
- authority boundary;
- failure/UNKNOWN behavior.

## A1. Semantic atom system

Define the minimum canonical operational atom set.

At minimum consider:

ENTITY
INSTANCE
ROLE
CAPABILITY
AUTHORITY
CURRENT_WRITER
APPROVAL
TASK
TASK_STATUS
SOURCE_STATUS
INPUT_IDENTITY
UNKNOWN
CONFLICT
STOP
ACTION
RESULT
TERMINAL
HANDOFF
HISTORICAL_REPLAY
DELIVERY
RECEIPT
ACCEPTANCE
PRODUCTION_AUTHORITY

For each atom define:
- canonical meaning;
- allowed state values;
- forbidden inference;
- provenance/evidence requirement;
- how it maps to execution-contract fields.

Do not create new project norms by definition.
Atoms must compile existing active norms.

## A2. Source-to-rule compiler

Define a candidate intermediate rule representation such as:

MUST
MAY
MUST_NOT
REQUIRES
STOP_IF
AUTHORITY_FROM
INPUT_REQUIRED
OUTPUT_REQUIRED
NEXT_GATE

Each compiled rule must retain provenance to:
- source locator/version/blob;
- exact section/semantic slot when possible.

If active sources conflict:
STOP / explicit authorized resolution required.
Do not invent precedence unless active sources already define it.

## A3. Initiation self-test

Define a mandatory semantic self-test for a newly initiated Entity before profile work.

It must prove the instance correctly applies at least:

- capability != authority;
- writer != task authority;
- task authority != production authority;
- UNKNOWN remains UNKNOWN;
- historical PROMPT != active task;
- publication/dispatch != processing_started;
- recovery != current state;
- candidate source != active source;
- current verified evidence dominates stale convenience;
- conflict => STOP.

Self-test must have machine-checkable expected outcomes.

## A4. Task/profile compiler

Define how exact current event/task is bound after bootstrap.

Required separation:

ROLE remains stable.
PROFILE selects relevant operational behavior.
EXPERIENCE provides advice only.
TASK_AUTHORITY defines executable scope.

Profile/experience must never create authority.

Define deterministic rules for selecting:
- profile pack;
- source subset;
- experience subset;
- tool capability subset;
- required validators.

## A5. SEMANTIC_EXECUTION_CONTRACT

Define a versioned schema.

At minimum:

ENTITY
INSTANCE
ROLE_PROFILE
CURRENT_STATE
TASK_IDENTITY
TASK_STATUS
AUTHORITY_BASIS
SOURCE_SET
INPUTS
ALLOWED_ACTIONS
FORBIDDEN_ACTIONS
REQUIRED_PRECONDITIONS
STOP_IF
EXPECTED_RESULT
EXPECTED_TERMINAL
NEXT_GATE_RULE
PROVENANCE

The contract is derived.
It is NOT itself an authority source.

## A6. Static validator

Define deterministic validation before first effect:

- writer gate if required;
- exact task authority;
- currentness/supersession;
- immutable inputs;
- source-set compatibility;
- allowed action membership;
- forbidden action exclusion;
- stop conditions;
- expected output shape.

Proposed action outside ALLOWED:
REJECT before effect.

## A7. Runtime revalidation

Before every new external/irreversible effect:
revalidate task, authority, writer and relevant inputs.

Specify which operations count as effects.

No automation/capability may create authority.

## A8. Result / next-gate compiler

Define how PASS/BLOCKED/FAIL/UNKNOWN are derived.

Do not infer:
- delivery from publication;
- receipt from dispatch;
- acceptance from receipt;
- next task from historical queue;
- activation from detector event;
- processing_started from activation attempt.

Next gate must come only from active authority + current result + Task Conveyor rules.

## A9. Experience boundary

Define how project experience is retrieved and used.

Experience:
- may improve ordering/diagnosis;
- must carry context/provenance;
- cannot override current sources/task;
- cannot create authority/current-state.

Provide a failure case:
experience recommends an action that current contract forbids.
Expected: validator rejects action.

## A10. Existing-system reconciliation

Create one explicit mapping table:

EXISTING OBJECT
-> KEEP / INCORPORATE / RENAME / DEFER / CONFLICT
-> TARGET LAYER
-> REASON

Must include:
- Semantic Bootstrap Profile candidate;
- Reflex Kernel / Situational Awareness / Profile Pack if present;
- ECL;
- Semantic Dialogue Lexicon;
- Semantic Relations Lexicon;
- CONTEXT_PACKET;
- PROJECT_OPERATIONS profile;
- Task Conveyor;
- Recovery;
- current-writer;
- semantic memory/experience.

Do not silently deprecate or supersede anything.
This task has no authority to change existing status.

## A11. Adversarial fixtures

At minimum model:

T1 writer established but no task authority.
T2 task exists but writer required and absent.
T3 historical task UNKNOWN after replacement.
T4 publication/dispatch exists but processing_started=no.
T5 stale task receives newer terminal/supersession.
T6 recovery older than verified GitHub delta.
T7 experience recommends forbidden action.
T8 profile implies capability outside task.
T9 model proposes useful extra action outside ALLOWED.
T10 UNKNOWN tempts YES/NO inference.
T11 active source conflict.
T12 automation capability without automation authority.
T13 current-writer established after replacement but old task remains UNKNOWN.
T14 candidate source available but not activated.
T15 OPERATOR gives decision in current KOO chat and KOO must not route it back to itself.

Each fixture must have:
- inputs;
- compiled contract;
- proposed bad transition;
- validator outcome;
- expected terminal/next gate.

## A12. Human-readable causality

The same execution contract must support a concise human explanation:

what was checked
-> what is known
-> what is authorized
-> what is forbidden
-> what happened
-> why it matters
-> exact next action.

No separate human narrative may silently invent authority absent from the contract.

## Output

Create one immutable architecture candidate package, e.g.:

entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-reconciliation/

Include:
- ARCHITECTURE.md
- SEMANTIC-ATOMS.md
- EXECUTION-CONTRACT-SCHEMA.md or JSON
- SOURCE-RULE-MAPPING.md
- EXISTING-SYSTEM-MAP.md
- INITIATION-SELF-TEST.md
- ADVERSARIAL-FIXTURES.md
- NEXT-GATES.md
- manifest/checksums if package form is used.

Status:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

## Boundaries

Do NOT:
- activate Project Sources;
- modify canon;
- implement runtime code;
- change Entity roles;
- create new Entity;
- mutate current-writer/recovery;
- replay historical semantic tasks;
- issue Telegram/PKTB/media profile work;
- call live providers;
- mutate host/storage;
- create production authority.

## Expected terminal

PASS_SHT_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_CANDIDATE_READY_FOR_KOO_RECONCILIATION

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/identity;
- architecture summary;
- existing-system reconciliation map;
- deterministic vs neural boundary;
- execution-contract schema identity;
- self-test/adversarial fixture summary;
- unresolved conflicts/UNKNOWNs;
- status ARCHITECTURE_CANDIDATE_NOT_ACTIVE;
- exact next gate recommendation.

Then STOP.
