# KOO -> SHT: SECE r0.1 architecture correction-only after SHD review

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

## Exact SHD review result

puev5691/wellbeing-hq@b90883ecfb42600c3798588e282e3ebbdea556c3:
entities/shardovik/outbox/SHD__semantic-entity-control-engine-r01-architecture-boundary-review__KOO.md

blob:
8995441e0299925b0d01872ad4285e0107f06725

terminal:
NEEDS_REWORK_SHD_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_BOUNDARY_REVIEW

ARCHITECTURE_BOUNDARIES_REVIEWED=YES
ARCHITECTURE_STATUS=ARCHITECTURE_CANDIDATE_NOT_ACTIVE
SIMULATOR_DESIGN_READINESS=NO

Blocking defect count:
3

## Exact predecessor architecture package

puev5691/wellbeing-hq@d254249af6da2e6b1dd743d4bfae1fabc8c53af2:
entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-reconciliation/

Exact blobs:

ARCHITECTURE.md
5446206cd2413db76c46d2a5ceff4b3d585f3354

SEMANTIC-ATOMS.md
fa854994a7e2cbe626999f3bae0cf751de26897e

EXECUTION-CONTRACT-SCHEMA.md
728e6b218cff22b038ce17868cf198ebec28cf2e

SOURCE-RULE-MAPPING.md
1fd08c68c3b907d9962cf828a72897730a3fa3e4

EXISTING-SYSTEM-MAP.md
1bed6f2a89664928fe1e2b183d7a615f3cd4ffc0

INITIATION-SELF-TEST.md
06451b3cd3a22a42a14df1d32c17f8c83c609366

ADVERSARIAL-FIXTURES.md
e080c146062cbd58479ec6bf3236769c34986955

NEXT-GATES.md
a8ec49803f34a097ccb5371359c2555964028572

MANIFEST.md
4e90132733e26be8c143cd3241dcf6acafc5a05f

status:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

## Priority authority

puev5691/wellbeing-hq@8613ec56d65ff52dd887503ba893f2d2a9128613:
entities/koordinator/current/KOO__semantic-entity-control-engine-r01-priority-decision__OPERATOR.md

blob:
d0521905627b306a4888261a9d414148ac64f265

SEMANTIC_ENTITY_CONTROL_ENGINE_R01_PRIMARY_PRIORITY = YES
PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE = YES

## Scope

Perform ONLY bounded architecture correction for the three exact SHD blockers.

Do NOT redesign L0-L9.

Do NOT reopen already accepted architecture/boundary findings unless one of these corrections directly requires a local consistency edit.

Do NOT:
- activate Project Sources/canons;
- implement runtime;
- mutate Entity roles;
- mutate recovery/current-writer;
- replay historical tasks;
- issue Telegram/PKTB/media work;
- call providers;
- mutate host/storage;
- create production authority.

## C1. Per-action authorization provenance binding

Problem:
ALLOWED_ACTIONS[] is currently a bare list.
The validator cannot deterministically prove authority provenance for each specific action.

Add an explicit machine-checkable per-action authorization binding.

Required minimum fields per action:

- action_id
- action_class
- disposition = ALLOWED|FORBIDDEN
- compiled_rule_id
- exact source locator
- source version/blob
- authority_ref
- authority_scope
- authority_action_classes
- task_binding
- task_currentness_requirement
- writer_requirement
- production_or_effect_authority_requirement
- provenance_status
- conflict_status

Allowed equivalent closed structure is acceptable only if it deterministically proves the same relation.

Required invariant:

ACTION
-> COMPILED RULE
-> ACTIVE SOURCE PROVENANCE
-> EXACT AUTHORITY
-> CURRENT TASK/STATE CONDITIONS

No authority-sensitive action may appear executable if this exact binding is:
- absent;
- stale;
- conflicted;
- scope-mismatched;
- task-mismatched.

Compiled/derived contract remains NOT authority.

Update at minimum:
- EXECUTION-CONTRACT-SCHEMA
- SOURCE-RULE-MAPPING
- ARCHITECTURE L6/L7 wording as needed
- affected fixtures T1/T8/T9/T12

Do not create new authority semantics.

## C2. Explicit causal event / handoff state

Problem:
T4 and T15 currently depend on prose semantics not represented in closed contract state.

Add an explicit causal-event / handoff structure sufficient to machine-check:

- event_id
- event_type
- exact evidence_ref
- causal_parent_event_id or equivalent predecessor binding
- lifecycle/evidence_state
- dispatch_state
- delivery_state
- receipt_state
- processing_started_state
- handoff_recipient
- handoff_reason/purpose
- decision_id if relevant
- decision_owner
- decision_recipient
- current_decision_state
- proposed_handoff_target
- redundant_self_handoff = YES|NO|UNKNOWN
- causal_requirement_status

Closed enums are preferred.

Required deterministic rules:

1. dispatch does not imply delivery/receipt/processing_started;
2. receipt does not imply acceptance;
3. activation attempt does not imply processing_started;
4. if current decision already exists in current KOO context and proposed handoff target is KOO itself, and no new causal gate requires such handoff:
   REJECT_REDUNDANT_SELF_HANDOFF;
5. routing/handoff remains derived from active rules/current verified state/Task Conveyor, never a new authority source.

Update at minimum:
- EXECUTION-CONTRACT-SCHEMA
- SEMANTIC-ATOMS if needed only for local precision
- ARCHITECTURE L3/L6/L7/L9 wording as needed
- ADVERSARIAL-FIXTURES T4 and T15

T4 and T15 must become machine-decidable from explicit contract fields, not narrative convention.

## C3. Explicit current-state evidence model

Problem:
T6 recovery-vs-verified-delta precedence is described in prose but not representable explicitly enough for deterministic L3/L7/L8 evaluation.

Add CURRENT_STATE_EVIDENCE or equivalent closed structure with at least:

- evidence_id
- evidence_kind
- exact immutable identity
- scope
- provenance/source
- verified_state
- currentness_state
- relation_to_other_evidence:
  supersedes | refines | historical | conflicts | independent
- relation_target_evidence_id
- selected_current_basis = YES|NO
- selection_basis
- unresolved_conflict = YES|NO
- conflict_set[]
- unknown_fields[]

Required deterministic rules:

1. recovery does not automatically outrank later verified delta;
2. precedence is exact-scope/evidence based;
3. recency-by-filename is forbidden;
4. if a verified delta refines/supersedes recovery for exact scope, selected current basis uses that delta for that scope;
5. recovery remains historical/current evidence outside the refined scope as applicable;
6. unresolved applicable conflict => STOP;
7. missing current basis => UNKNOWN;
8. no state may be reconstructed from memory.

Update at minimum:
- EXECUTION-CONTRACT-SCHEMA
- ARCHITECTURE L3/L7/L8
- SOURCE-RULE-MAPPING only if needed for explicit rule provenance
- ADVERSARIAL-FIXTURES T6

T6 must become machine-decidable from explicit current-state evidence.

## Preserve already accepted architecture

Do not reopen:

- one unified semantic contour;
- L0-L9 architecture;
- Semantic Bootstrap at L1;
- Progressive Context Loader at L5;
- ECL predecessor/input to L6;
- Task Conveyor authoritative at L3/L9;
- Recovery authoritative at L1/L3/L8;
- current-writer evidence/precondition, not task authority;
- profile/experience non-authority;
- UNKNOWN non-promotable;
- active-source conflict => STOP;
- candidate sources non-active;
- one-safe-step revalidation;
- human explanation from same contract/result;
- CONTEXT_PACKET durable identity UNKNOWN/DEFER;
- historical unresolved tasks evidence only / no replay.

## Required corrected output

Create one immutable corrected architecture successor package.

Recommended path:

entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-correction-r01/

Include at minimum:

- corrected ARCHITECTURE.md
- corrected EXECUTION-CONTRACT-SCHEMA.md
- corrected SOURCE-RULE-MAPPING.md if changed
- corrected SEMANTIC-ATOMS.md if changed
- corrected ADVERSARIAL-FIXTURES.md
- exact CORRECTION-DIFF.md
- MANIFEST.md
- any unchanged referenced files either copied only if package canon requires or referenced by exact predecessor identity.

Status:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

## Required verification

Show explicitly:

C1_ACTION_BINDING_CLOSED=YES
C2_CAUSAL_HANDOFF_STATE_CLOSED=YES
C3_CURRENT_STATE_EVIDENCE_CLOSED=YES

Re-evaluate only affected fixtures:

- T1
- T4
- T6
- T8
- T9
- T12
- T15

and any directly dependent fixture.

Required:
all machine-decidable from explicit contract/validator fields.

No fixture may rely on prose convention.

## Expected terminal

PASS_SHT_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_CORRECTION_READY_FOR_SHD_REREVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact corrected package locator/blobs;
- exact correction diff;
- C1/C2/C3 closure;
- affected fixture results;
- confirmation L0-L9 unchanged;
- confirmation accepted findings preserved;
- status ARCHITECTURE_CANDIDATE_NOT_ACTIVE;
- exact next gate:
  SHD narrow rereview of C1/C2/C3 only.

Then STOP.
