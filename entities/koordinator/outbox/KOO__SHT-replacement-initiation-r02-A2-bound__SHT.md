# KOO -> bound SHT chat: replacement Initiation Gate r0.2 A2

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ONLY the exact SHT chat instance that authored the durable conflict result e80dd56...

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A2

scope:
INITIATION_GATE_ONLY

instance_binding_id:
SHT_R02_A2_BOUND_TO_FAIL_RESULT_E80DD56

project_time:
omitted

Resume-First.

This PROMPT is valid ONLY in the exact same SHT chat instance that authored:

puev5691/wellbeing-hq@e80dd56a6e92284ae875540dcb062114b9837489:
entities/shtabist/outbox/SHT__replacement-initiation-gate-r02-result__KOO.md

blob:
144a4e549ee84772e55af6b6b958de313f247abe

If this is NOT that exact same chat instance:
STOP before PROCESSING_STARTED.

Do not forward this PROMPT to another SHT chat.
Do not create a new SHT chat for A2.

## Exact authority

puev5691/wellbeing-hq@0256d7c47dce16356cbc2357cf2f293ca0843557:
entities/koordinator/outbox/KOO__authorize-SHT-replacement-initiation-r02-A2-bound__OPERATOR.md

blob:
9c5de02c26ceb5065dc8943a1ebf7c09c2cd32d7

decision:
AUTHORIZE_SHT_REPLACEMENT_INITIATION_GATE_R02_A2_BOUND_TO_E80DD56 = YES

scope:
INITIATION_GATE_ONLY

## Exact governing reconciliation

puev5691/wellbeing-hq@2fb868bb68567d93de98bfd247f6af3e0394faab:
KOO reconciliation selecting bound A2 as controlling successor gate.

A1 is non-executable.

## Exact A2 registry

puev5691/wellbeing-hq@7506e3332ddb5b175b78249922fd53b7197fc415:
entities/koordinator/outbox/SHT_replacement_initiation_gate_R02_A2_registry.md

blob:
c40025601dede9b32e51f047b8241ca87a777c8b

state:
INITIAL_NOT_STARTED

## Exact A2 frontier

puev5691/wellbeing-hq@77a52d38a60a7b9339dd0b2de06b5fffb094cb77:
entities/koordinator/outbox/SHT_replacement_initiation_gate_R02_A2_frontier.md

blob:
5e6036f58f7355215a70944c2f05633f19e4c075

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## A1 disposition

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A1

disposition:
BLOCKED_NON_EXECUTABLE_INSTANCE_BINDING_CONFLICT

Do NOT:
- resume A1;
- replay A1;
- reuse A1 PROCESSING_STARTED;
- overwrite A1 evidence;
- infer A1 success.

Existing A1 PROCESSING_STARTED remains conflict evidence only:

puev5691/wellbeing-hq@5c73b03649363d982de29ea887a5f5216e03e344:
entities/shtabist/outbox/execution-evidence/SHT_REPLACEMENT_INITIATION_GATE_R02_A1__PROCESSING_STARTED_E1.md

blob:
d2cf63b0650a4185d9088fd0f09028d44bbcc78f

## Mandatory A2 instance-binding confirmation

Before any A2 write, verify all of the following:

1. this is the same chat that authored the binding-anchor result e80dd56...;
2. the current conversation retains that exact prior result as this chat's own durable return;
3. no competing A2 PROCESSING_STARTED or A2 result exists;
4. A1 remains BLOCKED_NON_EXECUTABLE_INSTANCE_BINDING_CONFLICT;
5. recovery r02 remains current;
6. predecessor writer remains unchanged;
7. profile continuation remains PAUSED_BY_OPERATOR.

If any item cannot be established:
STOP with exact blocker.

## Mandatory A2 PROCESSING_STARTED

Use ONLY this fresh path:

entities/shtabist/outbox/execution-evidence/SHT_REPLACEMENT_INITIATION_GATE_R02_A2__PROCESSING_STARTED_E1.md

Before creation:
fresh-search exact A2 attempt and exact path.

If any A2 PROCESSING_STARTED already exists:
STOP.
Do not reuse it and do not choose a winner by time.

The new A2 PROCESSING_STARTED artifact must bind:

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A2

instance_binding_id:
SHT_R02_A2_BOUND_TO_FAIL_RESULT_E80DD56

binding_anchor_commit:
e80dd56a6e92284ae875540dcb062114b9837489

binding_anchor_blob:
144a4e549ee84772e55af6b6b958de313f247abe

accepted_frontier_commit:
77a52d38a60a7b9339dd0b2de06b5fffb094cb77

accepted_frontier_blob:
5e6036f58f7355215a70944c2f05633f19e4c075

accepted_state:
INITIAL_NOT_STARTED_V1

recovery_ref:
c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5

recovery_tree:
f561246223a48ac885d7baae383898cc8e89af16

After publication:
immutable-readback the A2 PROCESSING_STARTED artifact.

Only after that perform substantive Initiation Gate verification.

## Exact immutable recovery

repository:
puev5691/wellbeing-entity-bootstrap

immutable ref:
c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5

path:
entities/sht/recovery/versions/sht-recovery-r02

package tree:
f561246223a48ac885d7baae383898cc8e89af16

composition:
9 files

ARH recoverability:
READY_FOR_REPLACEMENT_INITIATION_HANDOFF

Exact ARH preservation result:

puev5691/wellbeing-hq@9e70bf13ea140df373196822b1145962b9fdb157:
entities/archivarius/outbox/ARH__SHT-replacement-external-recovery-r01__KOO-SHT.md

blob:
710858dd2dae00324a5537322b7ee80b4a288c08

terminal:
PASS_ARH_SHT_REPLACEMENT_EXTERNAL_RECOVERY_R01_READY_FOR_INITIATION_HANDOFF

Recovery registry:

entities/archivarius/current/recovery-registry/ARH__SHT-recovery-r02.md

blob:
eaacb33dfadc75e0ce8a10943c5b7617c4837081

## Recovery verification

Independently verify the immutable package.

Expected exact files/blobs:

SHT__replacement-self-snapshot-preservation-r01__KOO-ARH.md
blob d00ce349aebad0fa7e72719cb99d616185b65d93
SHA-256 160e1ab221ed717e7a0e936f318cdb00d2d9b26338c5771337d0d4b37e8acd9b

SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da
SHA-256 c91cf6ee26f31db5bfea6375fda201b4e1a9bf44f8b2482c3090469606fa0a73

ROLE-IDENTITY.md
blob d8bbd65b3dc7d1cb707201f32741d6155eaa885c
SHA-256 56fe444b20752371f7c0544b1d3d0bd240f03a3ce221b4f69e98e8882f74ecd7

SOURCES.md
blob e828e7e7c9db7466ba0a80278d7f5a3726f8178b
SHA-256 9bf65e4a1c299ba288169792a3fab9bbd12addbe38e262743cb0e83f2581fc5b

TASK-STATE.md
blob 50c0885cc4644deeb20d18909de503f363ea68ca
SHA-256 11f85d769393bd4a462587d689ef0998e78d4d528efa5a0caaa9cf4a416dfcf1

SHT__replacement-initiation-boundary-r02.md
blob 600bb87ea7cea880625aea2026b0bc42dc258166
SHA-256 6303f77b0156777739a106de98223ed760cccaad08f5abaf38bb385a4237fa16

RECOVERY-LINEAGE.md
blob e740480f3e4f386edb8daaa4bc8e4c4c6ed73de5
SHA-256 c89820c0ba04eed5b86755311589eb80b60946132a46621c57f53e81e83372c3

RECOVERY-MANIFEST.md
blob f5a2e5494a19dfe40c85b7d6db925c0d21983927
SHA-256 89ebe68eb811b4cf0dee6812f65d103ecaee2bc2424549a4276924e906147396

SHA256SUMS.txt
blob ed24f2d925361d749a0d5b7c6420f109342ca5f5
self SHA-256 20b0b8ea4f984123fb2c014027a37a00c7e067d57933539c9be72b1dbc51231e

SHA256SUMS coverage:
8/8 non-checksum files

Required:
- exact ref/path/tree;
- 9/9 composition;
- exact Git blobs;
- manifest;
- checksum list;
- independent SHA-256 recomputation for all covered files;
- active Project Source identities;
- self-snapshot provenance;
- predecessor writer identity;
- task-state/replacement boundaries.

If independent checksum verification cannot be completed:
return initiation_loaded_external_unverified.

If package is missing/corrupt/contradictory:
return initiation_failed.

Do not infer PASS.

## Active Project Sources

source-set basis:

entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Required active blobs:

Project Core v2.5:
a42f7dca6a7469a54fa2da24aae0da4e549c9d33

Entity Roles v2.4:
1772339cb74dae8550bfbd2e33401c34a929e911

File Work Canon v2.4:
e9c29d62057f34e4f771d6057a36d9b7f72e74c2

Source Loading Policy v2.2:
69eb657f260a019f76e8e707c880ea88c1dfa0bf

Recovery Canon v1.6:
233117e1c9509d730e1f5ec532b1cabe3f786609

Task Conveyor Canon v1.2:
df7896d867eeeffff506319538fedad938856686

Do not activate candidates/drafts.

## Predecessor writer

entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

writer_generation:
SHT-CURRENT-INSTANCE-R01

status:
CURRENT_WRITER

A2 success does NOT change this writer.

Writer Gate is separate.

## Preserved task state

profile_continuation:
PAUSED_BY_OPERATOR

D1D2:
COMPLETED_PASS

terminal:
PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW

corrected package tree:
84979101d6bd19fd939f978652f03317f6e524b9

narrow_rereview:
NOT_STARTED / NOT_AUTHORIZED

historical task/PROMPT replay:
FORBIDDEN

hidden/unwritten predecessor state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Required A2 Initiation outcome

Return exactly one:

initiation_verified_waiting_writer_gate

only if exact recovery + integrity + active source identities are independently verified;

or

initiation_loaded_external_unverified

if recovery is loaded but required verification remains incomplete;

or

initiation_failed

for exact failure/blocker.

## Required durable A2 result

Create a NEW result path distinct from A1:

entities/shtabist/outbox/SHT__replacement-initiation-gate-r02-A2-result__KOO.md

It must bind:

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A2

instance_binding_id:
SHT_R02_A2_BOUND_TO_FAIL_RESULT_E80DD56

binding_anchor_commit:
e80dd56a6e92284ae875540dcb062114b9837489

binding_anchor_blob:
144a4e549ee84772e55af6b6b958de313f247abe

Report:
- A2 PROCESSING_STARTED locator/blob;
- recovery locator/ref/tree;
- composition/blob/checksum verdicts;
- active-source verification;
- predecessor writer;
- profile continuation;
- D1D2 state;
- narrow rereview state;
- historical replay;
- current_writer_created=NO;
- Writer_Gate=NOT_PERFORMED;
- profile_work=NOT_PERFORMED;
- exact blockers/UNKNOWNs.

## Hard boundaries

NOT AUTHORIZED:
- Writer Gate;
- current-writer establishment/transfer;
- predecessor freeze/retirement;
- profile continuation;
- narrow rereview;
- SECE execution;
- Project Source/canon mutation;
- deployment/live/production effect;
- automatic downstream continuation.

## Mandatory return to KOO

After durable A2 result + immutable readback, output one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include exact A2 result locator/commit/blob, outcome, A2 PROCESSING_STARTED, instance binding, recovery verification, predecessor writer and all preserved boundaries.

Include exact line:

Fresh-reconcile this exact A2 Initiation Gate result. Do not infer Writer Gate or profile continuation authority.

End:

STOP.

After that block add nothing.
