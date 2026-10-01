# Semantic Entity Control Engine r0.1 — concept candidate for detailed development

status: DESIGN_CONCEPT_CANDIDATE
effectivity: NOT_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Human purpose

Reduce Entity self-initiative errors by moving operational permission and task execution from free-form prompt interpretation toward a compiled, machine-checkable semantic execution contract.

The concept does NOT replace current Project Sources, Recovery Canon, Task Conveyor Canon, Entity roles, Writer Gate, task authority or OPERATOR decisions.

It is a design candidate for a control/compiler layer connecting:
1. Semantic Bootstrap / Entity operational semantics;
2. Semantic Dialogue Engine PROFILE A — PROJECT_OPERATIONS;
3. exact current task execution.

No source/canon activation is created by this artifact.

## Existing project basis

### A. Semantic Bootstrap gap already confirmed

Exact reconciliation:

puev5691/wellbeing-hq@a09d63ae86dbc2e16f6412c4d4f46eb1611b705a:
entities/koordinator/outbox/KOO__entity-semantic-bootstrap-gap-reconciliation-r01__OPERATOR.md

blob:
240d840abcc92537c40a62cb76fb73b8ee224574

Already confirmed missing functions:
- canonical semantic seed representation;
- deterministic source-to-seed mapping/load contract;
- mandatory semantic initiation self-test;
- explicit handoff boundary:
  global bootstrap -> contour/profile -> Entity role -> exact task.

Existing progressive semantic context concepts must be reconciled, not duplicated.

### B. Semantic Dialogue Engine r0.1 already exists

Development roadmap:

puev5691/wellbeing-hq@ac269e3c1effb3fc6622351db54a2cc8efea8f5e:
entities/koordinator/outbox/semantic-dialogue-engine-r01/KOO__semantic-dialogue-engine-r01-development-roadmap__OPERATOR.md

blob:
9e71944268ab08666abfb5306db4fc15f18fa204

Existing PROJECT_OPERATIONS profile already identifies:
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

Existing engine flow already includes:
semantic extraction
-> current-state resolution
-> relevant memory/experience retrieval
-> CONTEXT_PACKET
-> command/routing
-> response/result
-> continuity validation
-> durable semantic memory.

This concept therefore refines the PROJECT_OPERATIONS control path rather than creating a separate competing semantic system.

## Problem observed

Long natural-language prompts and source packs are interpreted probabilistically.

Even when exact instructions say:
- ONLY;
- MUST NOT;
- DO NOT REPLAY;
- WAIT FOR WRITER GATE;
- UNKNOWN remains UNKNOWN;

an Entity may still create an extra transition, replay stale work, infer authority from capability/writer status, or ask OPERATOR to transport information already available by locator.

The core defect is not merely wording quality.
It is that the model is often asked to both:
1. interpret norms;
2. decide what they permit;
3. construct a work algorithm;
4. execute it;
inside the same free-form reasoning step.

The proposed engine separates these functions.

## Core architecture

Recommended pipeline:

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

## Stage 1 — Semantic Seed

Purpose:
establish invariant operational identity before profile work.

Seed contains only canonical meanings such as:

ENTITY
INSTANCE
ROLE
CAPABILITY
AUTHORITY
CURRENT_WRITER
APPROVAL
TASK
UNKNOWN
CONFLICT
STOP
RESULT
TERMINAL
HANDOFF
HISTORICAL_REPLAY

The seed must not itself authorize a profile task.

Example semantic state:

ENTITY:SIS
INSTANCE:NEW
LIFECYCLE:INITIATION
WRITER:NOT_ESTABLISHED
PROFILE_WORK:FORBIDDEN
HISTORICAL_REPLAY:FORBIDDEN
UNKNOWN:PRESERVE
CONFLICT:STOP

## Stage 2 — Active Source Compilation

Load only required approved/current sources according to Source Loading Policy.

Translate applicable source statements into normalized operational rules.

Candidate rule classes:

MUST
MAY
MUST_NOT
REQUIRES
STOP_IF
AUTHORITY_FROM
INPUT_REQUIRED
OUTPUT_REQUIRED
NEXT_GATE

Example:

WRITER_GATE = REQUIRED
PROFILE_WORK_REQUIRES = CURRENT_WRITER_ESTABLISHED
INSTALL_REQUIRES = SEPARATE_EXACT_TASK_AUTHORITY
HISTORICAL_PROMPT_REPLAY = FORBIDDEN

Important:
source text remains authoritative.
Compiled rules are a derived execution representation and must preserve provenance back to exact source/version.

## Stage 3 — Current Event / Task Binding

Bind only the current verified event or exact task.

Example:

EVENT = NEW_TASK
TASK_TYPE = TELEGRAM_INSTALL_VERIFY_READINESS
TASK_AUTHORITY = exact locator + immutable identity
TASK_STATUS = CURRENT
WRITER = ESTABLISHED

Do not infer a task from:
- recovery;
- historical PROMPT;
- writer status;
- publication/dispatch;
- capability;
- old queue state.

## Stage 4 — Profile Selection

Select a task-specific operating profile without changing Entity role.

Example:

ENTITY = SIS
PROFILE =
  TELEGRAM
  + INSTALL_VERIFY_READINESS
  + READ_ONLY
  + FAIL_CLOSED

Profile selection determines which semantic rules, checks, tools and experience families become relevant.

Profiles are not authorities.

## Stage 5 — Relevant Experience Retrieval

Experience is loaded only after active rules and exact task are known.

Purpose:
help execution ordering, diagnostics and efficient checks.

Experience may say:
"in this class of task, verify X before Y."

Experience must never create:
- authority;
- current state;
- approval;
- writer;
- task activation.

Current verified sources/task dominate prior experience.

## Stage 6 — Semantic Execution Contract

Before action, compile one machine-checkable object.

Candidate form:

SEMANTIC_EXECUTION_CONTRACT

ENTITY = SIS
INSTANCE = r08
ROLE_PROFILE = TELEGRAM_INSTALL_VERIFY_READINESS

CURRENT_STATE:
  writer = ESTABLISHED
  service = STOPPED

TASK:
  exact_id = ...
  authority = ...

ALLOWED:
  read_host_state
  inspect_db_readonly
  verify_package

FORBIDDEN:
  install
  mutate_db
  start_service
  telegram_call

REQUIRED_INPUTS:
  package_hash
  runtime_hash
  predecessor_hash

STOP_IF:
  hash_mismatch
  competing_writer
  task_superseded
  db_integrity_fail

EXPECTED_TERMINAL:
  PASS_READINESS
  BLOCKED
  FAIL

NEXT_GATE:
  SEPARATE_INSTALL_AUTHORITY

The contract is a derived executable plan, not a new authority source.

## Stage 7 — Static Validator

Before first productive action, validate:

- current writer requirement;
- task authority;
- task currentness/supersession;
- immutable input identities;
- source compatibility;
- allowed action set;
- forbidden action set;
- stop conditions;
- expected result form.

Any proposed action outside ALLOWED must be rejected before execution.

Example:

PROPOSED_ACTION = INSTALL_CANDIDATE
ALLOWED_SET = READ_ONLY

VALIDATION =
REJECT_ACTION_NOT_AUTHORIZED

This is the key boundary that prevents helpful model initiative from silently becoming project authority.

## Stage 8 — One Safe Step / Runtime Guard

Execute only one causally permitted step at a time.

Before each new effect:
revalidate current task, authority and relevant inputs.

For irreversible/external effects:
require the exact production/action authority defined by active sources.

## Stage 9 — Result Validation and Fixation

After execution:
- compare result to expected contract;
- classify PASS/BLOCKED/FAIL/UNKNOWN;
- preserve exact evidence;
- do not infer acceptance/delivery/next authority;
- derive next gate only from active authority/task conveyor rules.

## Semantic Atom Dictionary

The concept requires a canonical operational lexicon.

Words are not intended as stronger prompt rhetoric.
Each atom maps to a defined operational rule.

Examples:

UNKNOWN:
- do not convert to YES;
- do not convert to NO;
- do not reconstruct;
- preserve UNKNOWN;
- identify minimum evidence able to change state.

STOP:
- no next causal effect;
- preserve obtained result;
- return exact blocker;
- do not seek an unauthorized workaround.

CURRENT_WRITER:
- grants authoritative state-writing boundary for the Entity instance;
- does not create profile task authority.

TASK_AUTHORITY:
- binds exact task scope;
- does not imply install/live/production authority beyond that scope.

HISTORICAL_REPLAY_FORBIDDEN:
- old task/PROMPT may be evidence;
- it cannot become executable without a new authorized transition.

The dictionary should be small, versioned and provenance-linked.

## Three-layer model

The control architecture can be summarized as:

1. SEMANTIC SEED
   who the Entity is and how it must interpret project invariants.

2. SEMANTIC COMPILER
   what active sources mean for this role, current state and event.

3. TASK COMPILER
   what exact algorithm is allowed now.

Then:

EXECUTOR
-> VERIFIER
-> FIXATION

## Relation to current project work

This concept should be reconciled with, not replace:

- Semantic Bootstrap Profile candidate line;
- Semantic Dialogue Engine r0.1;
- ECL r0.1;
- Semantic Dialogue Lexicon r0.1;
- Semantic Relations Lexicon r0.1;
- CONTEXT_PACKET concept;
- PROJECT_OPERATIONS profile;
- Task Conveyor Canon;
- Recovery Canon;
- Entity Roles and Source Loading Policy.

Likely architectural placement:

Semantic Bootstrap
-> Semantic Entity Control Compiler
-> Semantic Dialogue Engine / PROJECT_OPERATIONS runtime
-> task-specific executor.

## Candidate development questions

Detailed design should establish:

D1. canonical semantic atom schema;
D2. exact source-to-rule compilation representation;
D3. provenance from each compiled rule to source/version/section;
D4. conflict resolution when active sources disagree;
D5. profile-selection algorithm;
D6. experience-selection boundary;
D7. execution-contract schema;
D8. static validator;
D9. runtime revalidation before effects;
D10. UNKNOWN/BLOCKED/STOP semantics;
D11. self-test fixtures for new Entity initiation;
D12. adversarial tests for unauthorized helpful initiative;
D13. compatibility with Task Conveyor/current-writer/recovery;
D14. offline simulator before runtime integration;
D15. human-readable explanation generated from the same execution contract.

## Required adversarial fixtures

At minimum test:

- writer established but no task authority;
- task exists but writer absent;
- historical task has no terminal but replacement instance appears;
- publication/dispatch exists but processing_started=no;
- stale task receives newer terminal/supersession;
- recovery contains older state than GitHub verified delta;
- experience recommends action forbidden by current source;
- profile selection suggests capability not authorized by task;
- model proposes a useful extra action not in ALLOWED;
- UNKNOWN result tempts inference;
- two candidate source versions conflict;
- automatic activation capability exists without automation authority.

Expected:
engine rejects unauthorized transition before effect.

## Success criterion

The goal is not to make the neural model deterministic in all reasoning.

The goal is to make project-critical transitions deterministic enough that:

neural interpretation may propose;
compiled contract constrains;
validator authorizes or rejects;
only authorized effects execute.

In short:

word
-> canonical semantic atom
-> operational rule
-> execution contract
-> validation
-> allowed action.

## Boundary

This artifact is:
DESIGN_CONCEPT_CANDIDATE

It is NOT:
- active Project Source;
- canon;
- source-set activation;
- runtime implementation;
- authority to pause existing tasks;
- authority to change Entity roles;
- authority to deploy a semantic engine.

Any development priority change, task suspension or implementation work requires separate current authority.

terminal:
SEMANTIC_ENTITY_CONTROL_ENGINE_R01_CONCEPT_FIXED_FOR_DETAILED_DEVELOPMENT
