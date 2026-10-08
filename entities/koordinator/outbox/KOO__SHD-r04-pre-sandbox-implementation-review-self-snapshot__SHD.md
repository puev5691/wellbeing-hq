# KOO -> SHD replacement-r0.4: pre-sandbox-implementation-review self-snapshot

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
SHD / ШАРДОВИК current writer replacement-r0.4

attempt:
SHD_R04_PRE_SANDBOX_IMPL_REVIEW_SELF_SNAPSHOT_R01_A1

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

project_time:
omitted

Resume-First.

Do NOT review the new KOD sandbox implementation candidate in this task.
Do NOT create G4/G5/G6 authority.
Do NOT execute any sandbox effect.
Do NOT replay historical tasks/prompts.

This task exists only to bring SHD recoverability up to the current authoritative writer and later SECE review state before a new independent implementation review gate is opened.

## Exact authority

puev5691/wellbeing-hq@16b4d28720188148164ac1429353ddfa0dde994c:
entities/koordinator/outbox/SHD_r04_pre_sandbox_impl_review_self_snapshot_authority.md

blob:
757fe4faddfbd0411c58f44715483655864b7457

status:
CANON_TRIGGER_AUTHORITY_RECORDED

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

## Registry

puev5691/wellbeing-hq@21e350eb434fe1e883d9a3a40ff6625e609f8f79:
entities/koordinator/outbox/SHD_r04_pre_sandbox_impl_review_self_snapshot_registry.md

blob:
fb587b2d51ad00e50a44bbef418260259f846255

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@6589c2583608b45c934c78cd9d0cda6685c3e5e3:
entities/koordinator/outbox/SHD_r04_pre_sandbox_impl_review_self_snapshot_frontier.md

blob:
dc4ddba2653e57925ab30c0be54d4add576cbce7

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current authoritative SHD writer

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

blob:
34b1b11d3cf2c607a8399e91ce066423ca3277e9

status:
AUTHORITATIVE_CURRENT_WRITER

writer_generation:
replacement-r0.4

This exact chat must verify continuity with the current SHD writer.

If writer changed/superseded or competing preservation attempt/result exists:
STOP with exact blocker.

## Existing SHD recovery

puev5691/wellbeing-entity-bootstrap@6a5b09807bb8a6b4525620a1cbd7d6a4561f0817:
entities/shd/recovery/versions/shd-recovery-r04

ARH registry:

entities/archivarius/current/recovery-registry/ARH__SHD-recovery-r04.md

registry_blob:
adb414b9f8fb9f2d7aa841dc40ab4f2c8a9f64e3

Current classification:

LAST_EXTERNALLY_VERIFIED_SHD_RECOVERY_BUT_STALE_RELATIVE_TO_CURRENT_WRITER_AND_LATER_SECE_REVIEW_STATE

Reason:
r04 recovery predates current replacement-r0.4 writer establishment and later SHD SECE review results.

Do NOT rewrite/delete r04.

No shd-recovery-r05 was found in fresh KOO reconciliation.

## Current SHD state to preserve

### 1. R04 runtime-integration static rereview PASS

puev5691/wellbeing-hq@ca5b875f00f8d3b38c5827025239cfde7b6a89ca:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-task-grounding-correction-r04-rereview-r01__KOO.md

blob:
887fdc7523ea5d18541eb8324cc452ef7c327f46

terminal:
PASS_SHD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04_REREVIEW_R01

Preserved facts:
- TASK_EXECUTION_BINDING PASS;
- C1 PASS;
- C2 PASS;
- C3 PASS;
- reviewed baseline core unchanged;
- candidate NOT_ACTIVATED.

### 2. D1/D2 sandbox-design narrow rereview PASS

puev5691/wellbeing-hq@9c86a15691187b65287615e65755413f6f1f8188:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-gate-design-D1D2-correction-r02-rereview-r01__KOO.md

blob:
82a0b19bfe10930f62d738e842519b29935936a3

terminal:
PASS_SHD_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_REREVIEW_R01

D1_CLOSED:
YES

D2_CLOSED:
YES

D1_D2_IDENTITY_MODEL_CONSISTENT:
YES

PRIOR_PASS_BOUNDARIES_PRESERVED:
YES

## New external dependency awaiting future review

KOD implementation result:

puev5691/wellbeing-hq@c7979afefeb7dc7c33ab24d84039aa374112954e:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-r01__KOO.md

blob:
69a24ea931db365089393c75d13f1ac151593def

terminal:
PASS_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_READY_FOR_INDEPENDENT_REVIEW

Candidate package:

puev5691/wellbeing-hq@27134205e21ebc44308606de4cb59f7b3b3ed577:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-r01/

tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

file_count:
58

candidate:
NOT_ACTIVATED

real_sandbox_effect_execution:
NOT_EXECUTED

G4/G5/G6 authority:
NOT_CREATED

Important:
this candidate is only a future review input.

independent_SHD_implementation_review:
NOT_STARTED / NOT_AUTHORIZED

Do NOT begin reviewing it in this preservation task.

## Mandatory PROCESSING_STARTED

Before substantive self-snapshot creation:

1. fresh-check authority, registry and frontier;
2. verify current SHD writer exact path/blob/status;
3. verify no newer SHD writer exists;
4. verify recovery r04 still exists and r05 does not;
5. verify exact SHD R04 static PASS;
6. verify exact SHD D1D2 PASS;
7. verify exact KOD implementation result/candidate tree;
8. verify no independent SHD candidate-review authority/attempt/result exists;
9. verify no G4/G5/G6 authority exists;
10. verify active Project Sources remain current.

Then create:

entities/shardovik/outbox/execution-evidence/SHD_R04_PRE_SANDBOX_IMPL_REVIEW_SELF_SNAPSHOT_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
SHD_R04_PRE_SANDBOX_IMPL_REVIEW_SELF_SNAPSHOT_R01_A1

authority_blob:
757fe4faddfbd0411c58f44715483655864b7457

frontier_commit:
6589c2583608b45c934c78cd9d0cda6685c3e5e3

frontier_blob:
dc4ddba2653e57925ab30c0be54d4add576cbce7

accepted_state:
INITIAL_NOT_STARTED_V1

SHD_writer_commit:
5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e

SHD_writer_blob:
34b1b11d3cf2c607a8399e91ce066423ca3277e9

previous_recovery_ref:
6a5b09807bb8a6b4525620a1cbd7d6a4561f0817

SHD_R04_review_blob:
887fdc7523ea5d18541eb8324cc452ef7c327f46

SHD_D1D2_review_blob:
82a0b19bfe10930f62d738e842519b29935936a3

pending_KOD_candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

Immutable-readback PROCESSING_STARTED.

Only then create self-snapshot.

## Required SHD self-snapshot

Create exactly one standalone current-writer self-snapshot:

entities/shardovik/outbox/SHD__r04-pre-sandbox-implementation-review-self-snapshot__KOO-ARH.md

Preserve only verified current state:

- entity SHD / ШАРДОВИК;
- current writer locator/commit/blob/generation/status;
- active approved Project Source identities;
- last external recovery r04 locator and stale classification;
- exact SHD R04 static rereview PASS;
- exact SHD D1D2 narrow rereview PASS;
- D1/D2 closed;
- exact KOD candidate result/tree as PENDING_INPUT only;
- independent SHD implementation review = NOT_STARTED / NOT_AUTHORIZED;
- KOD candidate = NOT_ACTIVATED;
- real sandbox effect = NOT_EXECUTED;
- G4/G5/G6 authority = NOT_CREATED;
- sandbox target for future G4 = UNKNOWN / NOT_SELECTED;
- historical replay = FORBIDDEN;
- hidden/unwritten SHD chat state = UNKNOWN / MUST_NOT_BE_RECONSTRUCTED;
- external SHD recovery r05 = NOT_YET_CREATED;
- safe next step = ARH external recovery r05 based on this exact self-snapshot.

Do NOT:
- review candidate af63918a...;
- modify KOD candidate;
- create G4/G5/G6 authority;
- execute sandbox effect;
- select sandbox target;
- mutate external recovery yourself;
- replay historical tasks/prompts.

After publication:
- immutable-readback snapshot;
- return exact locator/commit/blob;
- include PROCESSING_STARTED locator/blob;
- state external ARH preservation r05 = PENDING;
- STOP.

## Mandatory return to KOO

Final response must contain one copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- preservation attempt;
- PROCESSING_STARTED locator/blob;
- self-snapshot locator/commit/blob;
- current SHD writer identity;
- recovery r04 stale classification;
- SHD R04 review state;
- SHD D1D2 review state;
- pending KOD candidate tree;
- independent candidate review = NOT_AUTHORIZED;
- G4/G5/G6 authority = NOT_CREATED;
- external ARH preservation r05 = PENDING;
- exact UNKNOWNs/blockers.

Include exact line:

Fresh-reconcile this exact SHD self-snapshot. Prepare ARH external SHD recovery r05 successor only. Do not infer candidate-review or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
