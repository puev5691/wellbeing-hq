# KOO -> KOD v0.7: SECE sandbox adapter/platform implementation R01

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
KOD / КОДЕР v0.7 current writer

attempt:
KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_A1

scope:
OFFLINE_SANDBOX_ADAPTER_AND_PLATFORM_PROFILE_IMPLEMENTATION_ONLY

project_time:
omitted

Resume-First.

Create exactly one NEW immutable offline implementation candidate based on the verified R04 runtime baseline and the independently accepted R02 sandbox design.

This task is CODE/STATIC/OFFLINE implementation only.

Do NOT execute a real sandbox effect.
Do NOT select a concrete sandbox target.
Do NOT create G4/G5/G6 authority.
Do NOT activate or deploy the candidate.

## Exact authority

puev5691/wellbeing-hq@1ea6dd4ffe40c92381a4d8a851517c14f9e8dc61:
entities/koordinator/outbox/KOD_SECE_sandbox_adapter_platform_impl_R01_authority.md

blob:
fe249b9defe1f37f5afe5f10d417d3c14a6e08e8

decision:
AUTHORIZE_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01 = YES

## Registry

puev5691/wellbeing-hq@b9d15fa3409a28bcd732da81ec7132d89005d976:
entities/koordinator/outbox/KOD_SECE_sandbox_adapter_platform_impl_R01_registry.md

blob:
c4187fb80ca70ba76ae722ab2b9ee635c9327ddc

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@b608bfa3f29f393d10d40c37fcd0049b7b39974c:
entities/koordinator/outbox/KOD_SECE_sandbox_adapter_platform_impl_R01_frontier.md

blob:
96fc31c7f1a38f7425c902e892739ccfd89cacd7

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current KOD writer / recovery

Current writer:

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

Current external recovery:

puev5691/wellbeing-entity-bootstrap@34650c6b255ad204674b778de8d39910a61ba8f1:
entities/kod/recovery/versions/kod-recovery-v07

tree:
70d9ab5f452541c3fd697b40711be4242e0c6969

ARH result:

puev5691/wellbeing-hq@4ee29fc8fd12ef6eb2b8aed3da5fad2996259e0d:
entities/archivarius/outbox/ARH__KOD-v07-external-recovery__KOO-KOD.md

blob:
161c642ada7e5d5cbeaff8230e491fd816891d31

terminal:
PASS_ARH_KOD_V07_EXTERNAL_RECOVERY

If writer/recovery is superseded or conflicting:
STOP with exact blocker.

## Exact runtime baseline

KOD R04 result:

puev5691/wellbeing-hq@22134cff545f8670340e8c1848cbb31a2e0e023d:
entities/koder/outbox/KOD__SECE-r01-runtime-integration-task-grounding-correction-r04__KOO.md

blob:
2814edd2655eaca0011a7553f1d81e829eef1481

Exact R04 package:

puev5691/wellbeing-hq@bb5b66644cd9e6421613e2c3f22d3299549ed374:
entities/koder/outbox/sece-r01-runtime-integration-task-grounding-correction-r04/

tree:
1158f63954c78bb6023e7a05e2e702c110a5203c

candidate:
NOT_ACTIVATED

Independent R04 static PASS:

puev5691/wellbeing-hq@ca5b875f00f8d3b38c5827025239cfde7b6a89ca:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-task-grounding-correction-r04-rereview-r01__KOO.md

blob:
887fdc7523ea5d18541eb8324cc452ef7c327f46

Independent R04 runtime proof:

puev5691/wellbeing-hq@fd2c207588d0a14ed1a64e275aa3a12d00180db0:
entities/sisadmin/outbox/SIS__SECE-r01-runtime-integration-R04-burzh-combined-exec-r07__KOO.md

blob:
5815b818608dd5f95fed59557f142ea31659e5b4

runtime_integration:
22/22 PASS

live_effect:
NONE

Preserve R04 reviewed semantics unless exact R02 sandbox requirements require additive binding.

Do not activate R04.

## Exact sandbox design input

Corrected SHT result:

puev5691/wellbeing-hq@0ff3709612df21ca4e0f8abc914f1831a8ec2657:
entities/shtabist/outbox/SHT__SECE-r01-sandbox-gate-design-D1D2-correction-r02__KOO.md

blob:
e32ba475182b059709ed97c48973f43c8a071411

Corrected design package:

entities/shtabist/outbox/sece-r01-sandbox-gate-design-d1d2-correction-r02/

tree:
84979101d6bd19fd939f978652f03317f6e524b9

Mandatory design blobs:

CONFINEMENT-PROFILE.md
3e8e12a95f44db6c18a895d0ed83b69dc4b4ea6e

CLEANUP-IDENTITY.md
3dab9da97c5cfb4a055f5d5967791105a657c231

PRE-EFFECT-ADMISSION.md
c0926c3767e377e8e6c5cdbd5af0d063f51f629c

SANDBOX-EFFECT-ADAPTER.md
3f9891aa200224d3365d01cfdb3752243e9cf40c

SANDBOX-EFFECT-CLASS.md
f42f7f76bab51890bd4290b6217246776b90e223

OUTCOME-EVIDENCE.md
6e5ad629e775d0ad17082ad88e8a376298eaea3e

ROLLBACK-CLEANUP.md
d3f116f08ba51322c5eac933cb6a5a413858e608

G4-AUTHORITY-SHAPE.md
aa3b2bac844173430d07aeb70999158c97e87753

Independent D1/D2 review:

puev5691/wellbeing-hq@9c86a15691187b65287615e65755413f6f1f8188:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-gate-design-D1D2-correction-r02-rereview-r01__KOO.md

blob:
82a0b19bfe10930f62d738e842519b29935936a3

D1_CLOSED:
YES

D2_CLOSED:
YES

D1_D2_IDENTITY_MODEL_CONSISTENT:
YES

The implementation MUST conform to these exact design semantics.
Do not weaken a requirement merely because a primitive is inconvenient.

## Required implementation candidate

Create one NEW immutable package under a new KOD outbox path for this attempt.

The package must implement, at code/schema/profile level:

1. EphemeralFileSandboxEffectAdapterR01 candidate logic.

2. SECE_SANDBOX_CONFINEMENT_PROFILE_R02 validation and identity-binding logic.

3. OBJECT_BOUND_CLEANUP_R02 candidate logic.

4. One exact Linux/POSIX platform evidence profile candidate.
   It must explicitly map the design-required properties to proposed platform primitives/evidence and mark unsupported/unprovable properties as BLOCKED rather than silently weakening them.

5. Runtime integration binding:
   exact adapter/profile identities and versions must be carried through the R04 effect-sensitive structures required by the design, including admission and invocation-boundary verification.

6. Deterministic classification behavior:
   pre-effect missing proof => fail closed;
   post-possible-effect loss of required identity proof => unresolved classification;
   no optimistic fallback.

7. Static/pure/mock tests sufficient to exercise:
   - accepted/rejected name grammar;
   - identity-binding state transitions;
   - evidence-profile capability checks;
   - same-object continuity decisions;
   - cleanup eligibility decisions;
   - fail-closed classifications;
   - runtime binding/version-drift rejection.

Tests for this task MUST NOT depend on performing the real external sandbox effect.
Do not use a real effect execution as PASS evidence.

8. Package documentation/evidence:
   - MANIFEST;
   - implementation map;
   - platform evidence profile description;
   - test results;
   - exact file/blob identities after publication;
   - checksums for new/changed files where appropriate.

If faithful implementation is impossible with the selected Linux/POSIX primitive model:
return BLOCKED with the exact unsatisfied design property.
Do not downgrade the design requirement.

## Mandatory PROCESSING_STARTED

Before substantive implementation:

1. fresh-check authority, registry and frontier;
2. verify current KOD writer and recovery v07;
3. verify exact R04 package tree;
4. verify exact R02 design tree and mandatory blobs;
5. verify exact SHD D1/D2 PASS;
6. verify no competing implementation attempt/result exists;
7. verify no G4/G5/G6 authority appeared;
8. verify active Project Sources remain current.

Then create:

entities/koder/outbox/execution-evidence/KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_A1

authority_blob:
fe249b9defe1f37f5afe5f10d417d3c14a6e08e8

frontier_commit:
b608bfa3f29f393d10d40c37fcd0049b7b39974c

frontier_blob:
96fc31c7f1a38f7425c902e892739ccfd89cacd7

accepted_state:
INITIAL_NOT_STARTED_V1

KOD_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

KOD_recovery_ref:
34650c6b255ad204674b778de8d39910a61ba8f1

KOD_recovery_tree:
70d9ab5f452541c3fd697b40711be4242e0c6969

runtime_baseline_tree:
1158f63954c78bb6023e7a05e2e702c110a5203c

sandbox_design_tree:
84979101d6bd19fd939f978652f03317f6e524b9

D1D2_review_blob:
82a0b19bfe10930f62d738e842519b29935936a3

Immutable-readback PROCESSING_STARTED.

Only then perform implementation.

## Required standalone result

Create:

entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-r01__KOO.md

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED locator/blob;
- current KOD writer/recovery;
- R04 baseline identity;
- R02 design identity;
- D1/D2 review identity;
- NEW candidate package locator/commit/tree;
- package composition and key blobs;
- platform evidence profile ID/version;
- adapter implementation identity/version;
- confinement/cleanup implementation identity/version;
- test/static verification results;
- whether all exact D1/D2 semantics are faithfully represented;
- any BLOCKED property if not;
- candidate activation status;
- real effect execution status;
- G4/G5/G6 authority status;
- exact terminal.

PASS terminal:

PASS_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_READY_FOR_INDEPENDENT_REVIEW

PASS conditions include:
- immutable package publication/readback;
- static/pure/mock verification PASS;
- exact design binding PASS;
- real sandbox effect NOT_EXECUTED;
- candidate NOT_ACTIVATED;
- G4/G5/G6 authority NOT_CREATED.

Alternative terminal:

BLOCKED_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01

when an exact required property cannot be faithfully represented.

## Hard boundaries

NOT AUTHORIZED:
- actual sandbox effect execution;
- concrete sandbox target selection for effect execution;
- G4/G5/G6 authority or execution;
- activation/deployment;
- production/live/provider/API/Telegram effects;
- active Project Source/canon mutation;
- historical replay;
- automatic downstream continuation.

After KOD result:
return to KOO.
Independent SHD implementation review requires a separate future authority.

## Mandatory return to KOO

After durable result + immutable readback, return one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- implementation attempt;
- result locator/commit/blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- candidate package locator/commit/tree;
- adapter/profile implementation identities;
- verification verdict;
- real effect execution = NOT_EXECUTED;
- candidate = NOT_ACTIVATED;
- G4/G5/G6 authority = NOT_CREATED;
- exact blockers/UNKNOWNs.

Include exact line:

Fresh-reconcile this exact KOD sandbox implementation result. Do not infer G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
