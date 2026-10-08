# KOO -> ARH: SHD external recovery r05 preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_SHD_R05_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

Perform ONLY external preservation of the exact current SHD self-snapshot into a NEW immutable SHD recovery successor r05, followed by integrity verification, immutable readback and recovery-registry accounting.

Do NOT review the pending KOD candidate.
Do NOT create or infer G4/G5/G6 authority.
Do NOT execute sandbox effects.
Do NOT select a sandbox target.
Do NOT change SHD writer-state.
Do NOT replay historical tasks/prompts.

## Exact authority

puev5691/wellbeing-hq@c1ac870b9125e0762a109f1ae8498ebc72142587:
entities/koordinator/outbox/ARH_SHD_r05_external_recovery_authority.md

blob:
e6d6fe525f5cdd717c97f686ed5db3b66d238a74

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Registry

puev5691/wellbeing-hq@ea2428174ca2e55908fb2289a1ae1dcc446382e7:
entities/koordinator/outbox/ARH_SHD_r05_external_recovery_registry.md

blob:
1e238b777377d0bbcf6269cb12af06409b5b5b16

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@fb0fead5cbd8ba93bda062d14deedcce5b4f9c31:
entities/koordinator/outbox/ARH_SHD_r05_external_recovery_frontier.md

blob:
577eab0e9494ef67ab9d989c1078c0f7ea6d9e33

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current ARH writer

entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

If ARH writer changed/superseded or a competing SHD r05 preservation attempt/result/registry exists:
STOP with exact blocker.

## Exact SHD self-snapshot

puev5691/wellbeing-hq@bb87dec39e8844b71f4a407c2df268b93aa8e839:
entities/shardovik/outbox/SHD__r04-pre-sandbox-implementation-review-self-snapshot__KOO-ARH.md

blob:
3ed8958f993954f432c0b48be3a6d498795dd642

terminal:
PASS_SHD_R04_PRE_SANDBOX_IMPL_REVIEW_SELF_SNAPSHOT_R01

This exact file is the authoritative SHD current-writer self-snapshot for this preservation step.

ARH may preserve exact bytes and add recovery-owned metadata.
ARH must NOT rewrite or reconstruct substantive SHD self-state.

## Current authoritative SHD writer

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

blob:
34b1b11d3cf2c607a8399e91ce066423ca3277e9

writer_generation:
replacement-r0.4

status:
AUTHORITATIVE_CURRENT_WRITER

## Previous external SHD recovery

puev5691/wellbeing-entity-bootstrap@6a5b09807bb8a6b4525620a1cbd7d6a4561f0817:
entities/shd/recovery/versions/shd-recovery-r04

tree:
6596df49fca602dd30532386d40308e821c83f59

classification:
LAST_EXTERNALLY_VERIFIED_SHD_RECOVERY_BUT_STALE_RELATIVE_TO_CURRENT_WRITER_AND_LATER_SECE_REVIEW_STATE

Do NOT rewrite or delete r04.

## Target successor

Repository:
puev5691/wellbeing-entity-bootstrap

Create exactly one NEW immutable successor at:

entities/shd/recovery/versions/shd-recovery-r05

Before publication verify the target path does NOT already exist.

If r05 already exists or a competing r05 attempt/result/registry appears:
STOP with exact conflict.

## Active approved Project Sources

Active source-set:
r07

Basis:
entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Required exact active identities:

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

Task Conveyor v1.3:
NOT_ACTIVE

Do not substitute candidates/drafts.

## Exact SHD state to preserve

### R04 runtime-integration static rereview PASS

puev5691/wellbeing-hq@ca5b875f00f8d3b38c5827025239cfde7b6a89ca:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-task-grounding-correction-r04-rereview-r01__KOO.md

blob:
887fdc7523ea5d18541eb8324cc452ef7c327f46

terminal:
PASS_SHD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04_REREVIEW_R01

Preserve:
TASK_EXECUTION_BINDING=PASS
C1=PASS
C2=PASS
C3=PASS
reviewed baseline core=UNCHANGED
candidate=NOT_ACTIVATED

### D1/D2 sandbox-design narrow rereview PASS

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

## Pending KOD candidate to preserve as PENDING_INPUT only

KOD result:

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

classification:
PENDING_INPUT_ONLY

candidate:
NOT_ACTIVATED

real_sandbox_effect_execution:
NOT_EXECUTED

independent_SHD_implementation_review:
NOT_STARTED / NOT_AUTHORIZED

G4_authority:
NOT_CREATED

G5_authority:
NOT_CREATED

G6_authority:
NOT_CREATED

sandbox_target:
UNKNOWN / NOT_SELECTED

Do not review or classify this candidate beyond the exact preserved current state.

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check exact authority, registry and frontier;
2. verify current ARH writer;
3. verify exact SHD self-snapshot commit/blob;
4. verify current SHD writer exact commit/blob/generation;
5. verify r04 exists and remains immutable predecessor recovery;
6. verify target r05 path absent;
7. verify no competing ARH SHD r05 attempt/result/registry exists;
8. verify source-set r07 current;
9. verify exact SHD R04 rereview and D1D2 rereview identities;
10. verify exact pending KOD result/candidate tree;
11. verify independent candidate review remains NOT_AUTHORIZED;
12. verify G4/G5/G6 authority remains NOT_CREATED.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_SHD_R05_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_SHD_R05_EXTERNAL_RECOVERY_R01_A1

authority_blob:
e6d6fe525f5cdd717c97f686ed5db3b66d238a74

frontier_commit:
fb0fead5cbd8ba93bda062d14deedcce5b4f9c31

frontier_blob:
577eab0e9494ef67ab9d989c1078c0f7ea6d9e33

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
bb87dec39e8844b71f4a407c2df268b93aa8e839

source_snapshot_blob:
3ed8958f993954f432c0b48be3a6d498795dd642

source_writer_commit:
5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e

source_writer_blob:
34b1b11d3cf2c607a8399e91ce066423ca3277e9

previous_recovery_ref:
6a5b09807bb8a6b4525620a1cbd7d6a4561f0817

pending_KOD_candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

target_path:
entities/shd/recovery/versions/shd-recovery-r05

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Recovery package authorship boundary

ARH may create recovery-owned metadata only.

ARH must preserve exact current-writer-authored self-snapshot without substantive alteration.

ARH must NOT:
- reconstruct hidden/unwritten SHD state;
- review the pending KOD candidate;
- create candidate-review authority;
- create G4/G5/G6 authority;
- select a sandbox target;
- change SHD writer-state;
- replay historical tasks/prompts.

## Required r05 package functions

Build one standalone immutable package under:

entities/shd/recovery/versions/shd-recovery-r05

Required functions:

1. Exact copy:
   SHD__r04-pre-sandbox-implementation-review-self-snapshot__KOO-ARH.md

2. Exact copy:
   SHD__replacement-r04-current-writer.md

3. ROLE-IDENTITY.md
   Exact SHD role identity / active role-source binding only.

4. SOURCES.md
   Exact active source-set r07 identities.

5. TASK-STATE.md
   Preserve only confirmed current state:
   - SHD R04 static rereview PASS;
   - TASK_EXECUTION_BINDING/C1/C2/C3 PASS;
   - SHD D1D2 rereview PASS;
   - D1/D2 CLOSED;
   - pending KOD candidate tree af63918a... as PENDING_INPUT_ONLY;
   - candidate NOT_ACTIVATED;
   - independent SHD implementation review NOT_STARTED / NOT_AUTHORIZED;
   - real sandbox effect NOT_EXECUTED;
   - G4/G5/G6 authority NOT_CREATED;
   - sandbox target UNKNOWN / NOT_SELECTED;
   - historical replay FORBIDDEN;
   - hidden/unwritten SHD state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

6. SHD__recovery-initiation-boundary-r05.md
   ARH-owned procedural metadata only.
   Future initiation, if separately authorized, must verify exact immutable r05 package.
   Recovery itself creates no Writer Gate, candidate-review authority, G4/G5/G6 authority or sandbox-effect authority.

7. RECOVERY-LINEAGE.md
   Bind r04 predecessor, current SHD writer and exact self-snapshot.

8. RECOVERY-MANIFEST.md

9. SHA256SUMS.txt

Do not create unrelated reports inside the external package.

## Integrity requirements

Before final publication:
- fix final composition;
- verify provenance for every file;
- compute SHA-256 from final bytes;
- record Git blob identities where applicable;
- ensure no secret/private-key/credential values are included.

SHA256SUMS must cover every non-checksum file.

Do not substitute Git blob identity for SHA-256 where checksum verification is claimed.

## External publication

Publish exactly to:

puev5691/wellbeing-entity-bootstrap:
entities/shd/recovery/versions/shd-recovery-r05

Record:
- publication commit/ref;
- exact version path;
- package tree;
- composition;
- each external blob;
- SHA-256 identities.

## Immutable readback

After publication independently read back exact immutable r05.

Verify:
- path -> tree binding;
- exact expected composition;
- source self-snapshot external equality;
- current-writer external equality;
- manifest matches actual tree;
- SHA256SUMS entries match independently recomputed final bytes;
- no missing/extra unexplained files;
- no current-state conflict.

Publication alone is NOT PASS.

## Recovery registry

Create a NEW registry entry:

entities/archivarius/current/recovery-registry/ARH__SHD-recovery-r05.md

It must include:
- source self-snapshot locator/blob;
- SHD current-writer locator/blob/generation/status;
- predecessor recovery r04 immutable locator/tree/stale classification;
- new r05 immutable locator/ref/path/tree;
- composition/integrity/readback;
- SHD R04 rereview PASS;
- SHD D1D2 rereview PASS;
- pending KOD candidate tree as PENDING_INPUT_ONLY;
- independent candidate review NOT_STARTED / NOT_AUTHORIZED;
- candidate NOT_ACTIVATED;
- real sandbox effect NOT_EXECUTED;
- G4/G5/G6 authority NOT_CREATED;
- SHD current-writer mutation NONE by this task;
- historical replay NONE.

Fresh-readback registry.

## Success classification

Return:

EXTERNALLY_PRESERVED_READBACK_PASS

only if:
- source snapshot exact;
- current writer exact;
- publication complete;
- immutable readback complete;
- checksums independently PASS;
- registry PASS;
- no conflict/supersession exists.

On PASS classify r05 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_SHD_R04_PRE_SANDBOX_IMPLEMENTATION_REVIEW

Do NOT infer candidate-review or G4/G5/G6 authority.

If any required evidence is missing/conflicting:
return exact BLOCKED_/FAIL_ terminal and do not claim r05 current.

## Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__SHD-r05-external-recovery__KOO-SHD.md

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED locator/blob;
- source self-snapshot locator/blob;
- SHD current-writer locator/blob/generation/status;
- predecessor recovery r04 locator/tree/classification;
- new r05 immutable locator/ref/path/tree;
- package composition;
- exact external blobs/checksums;
- immutable readback verdict;
- registry locator/commit/blob/readback;
- pending KOD candidate tree/classification;
- independent candidate-review status;
- G4/G5/G6 authority status;
- exact terminal.

Expected PASS terminal:

PASS_ARH_SHD_R05_EXTERNAL_RECOVERY

## Hard boundaries

Do NOT:
- review KOD candidate;
- create candidate-review authority;
- create G4/G5/G6 authority;
- execute sandbox effects;
- select/mutate sandbox target;
- change SHD writer-state;
- replay historical tasks/prompts;
- mutate Project Sources/canons;
- perform deployment/live/provider/API/Telegram effects;
- automatically continue downstream.

## Mandatory return to KOO

After durable result + immutable readback, return one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- exact ARH attempt;
- result locator/commit/blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- new r05 immutable recovery locator/ref/path/tree;
- composition/checksum/readback verdicts;
- registry locator/commit/blob;
- current SHD writer identity;
- previous r04 disposition;
- SHD R04 / SHD D1D2 state;
- pending KOD candidate tree/classification;
- independent candidate review status;
- G4/G5/G6 authority status;
- remaining blockers/UNKNOWNs.

Include exact line:

Fresh-reconcile this exact ARH SHD r05 recovery result. Do not infer candidate-review or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
