# KOO -> SHT: SECE r0.1 EFFECTIVE_CONTEXT architecture clarification

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

## Exact OPERATOR architecture clarification

OPERATOR clarified:

SECE is a dynamic context engine.

Entity behavior is compositionally formed from:

ACTIVE SOURCES
+ SEMANTIC INVARIANTS
+ ROLE
+ INSTANCE
+ CURRENT STATE
+ TASK
+ AUTHORITY
+ PROFILE
+ EXPERIENCE
+ EVENTS
+ HUMAN INPUT
+ UNKNOWN
+ CONFLICTS
+ CONTEXT CORRECTIONS.

Primary context transformation:

RAW CONTEXT
-> semantic atoms
-> applicable rules/bindings
-> collision detection
-> context corrections
-> EFFECTIVE_CONTEXT
-> SEMANTIC_EXECUTION_CONTRACT
-> validator
-> ONE SAFE STEP
-> RESULT/EVENT
-> CONTEXT DELTA
-> successor EFFECTIVE_CONTEXT.

This clarification is architecture-local.
It does not activate Project Sources/canons and does not authorize runtime implementation.

## Existing outcome aggregation MUST be preserved

Existing architecture-local outcome aggregation successor:

entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

Exact result:

puev5691/wellbeing-hq@4a5dc3c7939967a4a2ee6c3af73abf815b1b06c5:
entities/shtabist/outbox/SHT__SECE-r01-outcome-aggregation-correction__KOO.md

blob:
7ee96ccff78949265f780fb5d72879ef9d99b825

terminal:
PASS_SHT_SECE_R01_OUTCOME_AGGREGATION_CORRECTION_READY_FOR_SHD_REVIEW

Selected model:
MULTI_OUTCOME_AGGREGATION

Exact package:
entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

Key blobs:
OUTCOME-AGGREGATION.md
7f8710eafd618a185159b79a8ceff0d55eaef635

EXECUTION-CONTRACT-SCHEMA.md
cb8bea18e6fc132f789eabcd933719a8a8a98da4

ARCHITECTURE.md
38f898d6cf7bc92235695eb434473d5a58c790c3

OUTCOME-FIXTURES.md
0ead740f96a014f25fdf3f3b811ba633c618bbc8

CORRECTION-DIFF.md
5206b613513d096069e88f18af6cb29f934ea3a2

MANIFEST.md
7a05a25c0974f1e1941866fff87d9fe8dfce949c

Boundary:

MULTI_OUTCOME_AGGREGATION remains local to L7 for deterministic handling of multiple simultaneously true validator predicates relative to ONE proposed transition.

Do NOT generalize it into the overall Context Engine composition model.

Do NOT cancel it.

Do NOT replace it with a global winner-takes-all rule.

## Architecture basis to preserve

Unified L0-L9 topology remains:

L0 ACTIVE AUTHORITATIVE SOURCES
-> L1 SEMANTIC SEED / INITIATION KERNEL
-> L2 SOURCE-TO-OPERATIONAL-RULE COMPILER
-> L3 CURRENT STATE / EVENT / TASK BINDING
-> L4 PROFILE SELECTION
-> L5 EXPERIENCE SELECTION
-> L6 SEMANTIC EXECUTION CONTRACT
-> L7 STATIC VALIDATOR
-> L8 RUNTIME ONE-SAFE-STEP GUARD
-> L9 RESULT / FIXATION / NEXT-GATE DERIVATION

Do not alter this topology without a separately proven blocker.

C1/C2/C3 remain closed and must not be reopened:
- per-action authorization provenance binding;
- causal event/handoff state;
- current-state evidence model.

## Goal

Add the MINIMAL architecture clarification necessary to make SECE explicitly model a dynamically changing composition of Entity context.

Do not redesign the whole system.

The correction must define:

1. formal EFFECTIVE_CONTEXT representation;
2. context composition semantics;
3. collision/correction semantics;
4. affected-scope recomputation;
5. context delta transition;
6. explicit boundary:
   context composition != validator outcome aggregation;
7. MULTI_OUTCOME_AGGREGATION remains local to L7;
8. SEMANTIC_EXECUTION_CONTRACT is a bounded derived projection of EFFECTIVE_CONTEXT for a specific next step, not the whole Entity context.

## EC1. EFFECTIVE_CONTEXT representation

Define a machine-checkable EFFECTIVE_CONTEXT structure.

At minimum it must represent independently:

- context_id / version;
- entity;
- instance;
- role;
- active source set;
- semantic invariants;
- current-state evidence;
- current selected state basis by exact scope;
- current task(s) / task currentness by exact scope;
- authority bindings;
- profile;
- experience set;
- capability set;
- event set / causal events;
- human input facts;
- UNKNOWN facts;
- conflict set;
- context corrections;
- derived bindings;
- provenance;
- scope index;
- dependency graph / affected-binding graph;
- prior_context_ref;
- context_delta_ref.

Do not flatten all state into one status axis.

Preserve orthogonal semantic / epistemic / lifecycle / authority-effect dimensions.

## EC2. Context composition semantics

Define how multiple applicable semantic lines coexist.

Required principle:

context composition is conjunctive/compositional where compatible.

Example:

MAY inspect
+ MUST_NOT mutate
+ UNKNOWN current consumer

must preserve simultaneously:

inspect = potentially allowed;
mutation = forbidden;
consumer = UNKNOWN;
evidence requirement = active.

Do not choose one "winning" statement merely because it is stronger or appears later.

Each line keeps:
- exact scope;
- semantic type;
- provenance;
- applicability;
- authority implications;
- epistemic state.

Independent semantic lines remain in EFFECTIVE_CONTEXT unless directly affected by a collision/correction.

## EC3. Collision detection

Define a closed set or extensible typed classes for collisions.

At minimum distinguish:

- DIRECT_NORM_CONFLICT
- SCOPE_OVERLAP_CONFLICT
- AUTHORITY_CONFLICT
- CURRENT_STATE_CONFLICT
- SOURCE_STATUS_CONFLICT
- TASK_CURRENTNESS_CONFLICT
- EVIDENCE_CONFLICT
- PROFILE_CONSTRAINT_CONFLICT
- EXPERIENCE_CONFLICT_WITH_RULE
- HUMAN_INPUT_CONFLICT_WITH_VERIFIED_EVIDENCE
- UNKNOWN_REQUIRED_EVIDENCE
- SUPERSESSION/REFINEMENT relation

Do not classify every coexisting difference as a conflict.

Difference across independent scopes must coexist.

## EC4. Context correction semantics

Define how a collision changes EFFECTIVE_CONTEXT only in the affected scope.

Required principles:

- applicable active-source conflict => STOP/block dependent effect in exact scope;
- FORBIDDEN limits action-space in exact scope;
- authority absence removes authority-sensitive actions from effective action-space;
- verified delta may refine/supersede older evidence only for exact scope;
- UNKNOWN preserves uncertainty and evidence requirement;
- profile/experience/capability may alter proposal/action-space but cannot create authority;
- experience conflicting with active rule loses for affected decision but remains historical/advisory evidence if useful;
- human input cannot override verified project state unless that input itself is an authorized decision/evidence event.

Do not erase unrelated context lines.

## EC5. Affected-scope recomputation

Define deterministic dependency-based recomputation.

When a verified Event/Result arrives:

1. identify exact changed semantic atoms/evidence;
2. identify scopes touched;
3. traverse dependency graph to find derived bindings affected;
4. invalidate/recompute only affected bindings;
5. retain unaffected bindings and causal context;
6. produce new EFFECTIVE_CONTEXT version.

No full-context reset merely because one fact changed.

No stale derived binding may survive if its dependency changed.

## EC6. Context delta

Define:

Context(n) + VERIFIED EVENT/RESULT -> CONTEXT_DELTA -> Context(n+1)

CONTEXT_DELTA must include at minimum:

- delta_id;
- parent_context_id;
- triggering_event/result ref;
- added_facts[];
- removed_or_superseded_facts[];
- refined_facts[];
- new_unknowns[];
- resolved_unknowns[];
- new_conflicts[];
- resolved_conflicts[];
- changed_scopes[];
- invalidated_bindings[];
- recomputed_bindings[];
- preserved_unaffected_bindings[];
- provenance[];
- resulting_context_id.

No delta may silently rewrite history.

Prior context remains immutable evidence.

## EC7. Context composition vs L7 outcome aggregation

Make this boundary explicit.

CONTEXT COMPOSITION:
- produces EFFECTIVE_CONTEXT;
- preserves multiple compatible semantic lines;
- resolves/corrects only exact affected scope;
- maintains UNKNOWN/conflict/evidence state over time;
- is not an effect decision.

MULTI_OUTCOME_AGGREGATION at L7:
- applies only after one bounded SEMANTIC_EXECUTION_CONTRACT exists;
- evaluates simultaneous validator predicates for one proposed transition;
- derives one effect decision / machine outcome / terminal mapping;
- retains causal reason set;
- does not replace EFFECTIVE_CONTEXT;
- does not determine global Entity context.

No cross-layer leakage.

## EC8. SEMANTIC_EXECUTION_CONTRACT boundary

Clarify:

SECE_EXECUTION_CONTRACT_R01 =
derived projection of EFFECTIVE_CONTEXT for ONE bounded next-step candidate.

It contains only the subset needed to:
- evaluate one proposed action/transition;
- validate task/authority/currentness/input constraints;
- produce one-safe-step admit/reject/STOP/UNKNOWN decision;
- derive result/next-gate.

It is NOT:
- entire Entity memory;
- entire semantic context;
- authority source;
- permanent state;
- substitute for Recovery/Task Conveyor/current-writer/source set.

Contract must retain exact reference to:
- effective_context_id;
- context version;
- selected scope;
- projection basis;
- all context facts/bindings used by the contract.

## EC9. Profile / experience / capability effect on context

Clarify:

PROFILE:
may select constraints, tools and task-specific interpretation frame.
No authority creation.

EXPERIENCE:
may add advisory proposals, ordering hints and diagnostic heuristics.
No current-state/authority/approval creation.

CAPABILITY:
may define what actions are technically possible to propose.
No authority creation.

All three may affect candidate action-space.
Only valid authority bindings can move authority-sensitive actions into executable action-space.

## EC10. Context correction fixtures

Add architecture-level fixtures at minimum:

CXT1:
MAY inspect + MUST_NOT mutate + UNKNOWN consumer.
Expect all three preserved.

CXT2:
experience suggests mutate; active rule forbids mutate.
Expect experience retained advisory, mutate removed/forbidden in effective action-space.

CXT3:
verified delta refines recovery for scope S.
Expect delta current in S; recovery preserved outside S where applicable.

CXT4:
new terminal supersedes current task in scope T.
Expect task-derived action bindings in T invalidated/recomputed; unrelated scopes unchanged.

CXT5:
new authority granted for exact action A.
Expect only authority-dependent bindings for A/scope recomputed.

CXT6:
new source conflict affects scope S1.
Expect STOP/block in S1; independent scope S2 retained.

CXT7:
UNKNOWN evidence resolved by verified event.
Expect unknown removed, affected dependent bindings recomputed only.

CXT8:
human input claims state conflicting with verified GitHub state but is not an authorized decision.
Expect verified state preserved; human claim recorded as conflicting/untrusted input.

CXT9:
authorized OPERATOR decision arrives.
Expect bounded context delta updates authority/decision bindings in exact scope.

CXT10:
one result event changes next gate but leaves role/profile/independent experience intact.

Each fixture must state:
- Context(n);
- triggering event;
- affected scopes;
- invalidated bindings;
- preserved bindings;
- Context(n+1).

## EC11. Relationship to existing architecture

Do not create a third semantic contour.

Map clarification into existing L0-L9.

Preferred local placement to evaluate:

- composition begins across L1-L5;
- EFFECTIVE_CONTEXT is the coherent current derived state after L5 / before L6 projection;
- L6 projects bounded execution contract from EFFECTIVE_CONTEXT;
- L9 emits RESULT/EVENT and CONTEXT_DELTA inputs for successor context.

Equivalent placement is acceptable if L0-L9 topology remains unchanged and boundaries stay explicit.

## Required output

Create one immutable architecture clarification successor package, e.g.:

entities/shtabist/outbox/sece-r01-effective-context-clarification/

Include at minimum:

- EFFECTIVE-CONTEXT.md
- CONTEXT-COMPOSITION.md
- COLLISION-CORRECTION.md
- CONTEXT-DELTA.md
- corrected ARCHITECTURE.md
- corrected EXECUTION-CONTRACT-SCHEMA.md if projection reference fields are needed
- CONTEXT-FIXTURES.md
- CORRECTION-DIFF.md
- MANIFEST.md

Status:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

## Required closure markers

EFFECTIVE_CONTEXT_FORMALIZED=YES
CONTEXT_COMPOSITION_MACHINE_SPECIFIED=YES
COLLISION_CORRECTION_SCOPE_BOUNDED=YES
AFFECTED_SCOPE_RECOMPUTATION_DEFINED=YES
CONTEXT_DELTA_DEFINED=YES
CONTEXT_COMPOSITION_DISTINCT_FROM_L7_AGGREGATION=YES
MULTI_OUTCOME_AGGREGATION_PRESERVED_LOCAL_TO_L7=YES
EXECUTION_CONTRACT_DEFINED_AS_BOUNDED_CONTEXT_PROJECTION=YES

## Boundaries

Do NOT:
- activate Sources/canons;
- implement runtime;
- resume simulator design;
- modify L0-L9 topology without a new proven blocker;
- reopen C1/C2/C3;
- cancel MULTI_OUTCOME_AGGREGATION;
- mutate Entity roles;
- mutate recovery/current-writer;
- replay historical tasks;
- call providers/Telegram;
- mutate host/storage;
- create production authority.

## Expected terminal

PASS_SHT_SECE_R01_EFFECTIVE_CONTEXT_CLARIFICATION_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package locator/blobs;
- EFFECTIVE_CONTEXT structure summary;
- composition semantics;
- collision/correction semantics;
- affected-scope recomputation;
- context delta semantics;
- explicit distinction from L7 aggregation;
- execution-contract projection boundary;
- CXT1-CXT10 results;
- closure markers;
- confirmation L0-L9/C1-C3/outcome aggregation preserved;
- exact next gate recommendation:
  independent bounded architecture clarification review only.

Then STOP.
