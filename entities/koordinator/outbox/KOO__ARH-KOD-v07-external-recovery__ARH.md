# KOO -> ARH: KOD v0.7 external recovery v07 preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

Perform ONLY external preservation of the exact KOD v0.7 current-writer self-snapshot into a NEW immutable KOD recovery successor v07, followed by integrity verification, immutable readback and recovery-registry accounting.

Do NOT perform sandbox adapter implementation.
Do NOT create or infer G4/G5/G6 authority.
Do NOT select or mutate a sandbox target.
Do NOT change KOD writer-state.
Do NOT replay historical tasks/prompts.
Do NOT perform deployment/live/provider/API/Telegram/host effects.

## Exact authority

puev5691/wellbeing-hq@2a5080d2cd736670bf06ea594cf5b3d336b61f41:
entities/koordinator/outbox/ARH_KOD_v07_external_recovery_authority.md

blob:
3d0a47c93cff551322240fa7503090a35f168efc

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Exact registry

puev5691/wellbeing-hq@ba42bd7e0024a1475e5aa8ec6e972a0954a1d32f:
entities/koordinator/outbox/ARH_KOD_v07_external_recovery_registry.md

blob:
9a21192384516e247380ad7308900ab3ec29d354

state:
INITIAL_NOT_STARTED

## Exact accepted frontier

puev5691/wellbeing-hq@c7bff8dd4a77ed62689ce6bf3298fe6167dc25bb:
entities/koordinator/outbox/ARH_KOD_v07_external_recovery_frontier.md

blob:
34c863899cfd621899f82c3a040470b9bba595f1

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

If current ARH writer changed, was superseded, or a competing KOD v07 preservation attempt/result/registry exists:
STOP with exact blocker.

## Exact KOD v0.7 self-snapshot

puev5691/wellbeing-hq@84b468944a569eef7d2411366f4773c714d86de6:
entities/koder/outbox/KOD__v07-pre-sandbox-implementation-self-snapshot__KOO-ARH.md

blob:
c7ed1f606e87b843149732f4601edcffa559a4b8

terminal:
PASS_KOD_V07_PRE_SANDBOX_IMPL_SELF_SNAPSHOT_R01_READY_FOR_ARH_EXTERNAL_RECOVERY_V07

immutable_readback:
PASS

This exact file is authoritative KOD self-state authored by current KOD writer.

ARH may preserve exact bytes/reference it.
ARH must NOT rewrite or reconstruct its substantive KOD self-state.

## Current authoritative KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

continuity:
PROVEN_SAME_KOD_V07_CHAT_INSTANCE

## Previous external KOD recovery

puev5691/wellbeing-entity-bootstrap@51704f5eb7a4bf43210c9760905f486a2e58b5ce:
entities/kod/recovery/versions/kod-recovery-v06

classification:
LAST_EXTERNALLY_VERIFIED_KOD_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOD_WORK

Do NOT rewrite or delete v06.

## Target successor

Repository:
puev5691/wellbeing-entity-bootstrap

Create exactly one new immutable successor at:

entities/kod/recovery/versions/kod-recovery-v07

Before publication verify this path does NOT already exist.

If it exists, or any competing v07 recovery/registry/result appears:
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

## Exact later state that recovery v07 must preserve

### KOD R04

puev5691/wellbeing-hq@22134cff545f8670340e8c1848cbb31a2e0e023d:
entities/koder/outbox/KOD__SECE-r01-runtime-integration-task-grounding-correction-r04__KOO.md

blob:
2814edd2655eaca0011a7553f1d81e829eef1481

package:

puev5691/wellbeing-hq@bb5b66644cd9e6421613e2c3f22d3299549ed374:
entities/koder/outbox/sece-r01-runtime-integration-task-grounding-correction-r04/

tree:
1158f63954c78bb6023e7a05e2e702c110a5203c

candidate:
NOT_ACTIVATED

### SHD R04 static PASS

puev5691/wellbeing-hq@ca5b875f00f8d3b38c5827025239cfde7b6a89ca:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-task-grounding-correction-r04-rereview-r01__KOO.md

blob:
887fdc7523ea5d18541eb8324cc452ef7c327f46

terminal:
PASS_SHD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04_REREVIEW_R01

### SIS R07 combined runtime PASS

puev5691/wellbeing-hq@fd2c207588d0a14ed1a64e275aa3a12d00180db0:
entities/sisadmin/outbox/SIS__SECE-r01-runtime-integration-R04-burzh-combined-exec-r07__KOO.md

blob:
5815b818608dd5f95fed59557f142ea31659e5b4

terminal:
PASS_SIS_SECE_R01_RUNTIME_INTEGRATION_R04_BURZH_COMBINED_EXEC_R07

runtime integration:
22/22 PASS

candidate:
NOT_ACTIVATED

live effect:
NONE

### SHD D1D2 sandbox-design PASS

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

corrected design package tree:
84979101d6bd19fd939f978652f03317f6e524b9

design status:
DESIGN_ONLY / NOT_IMPLEMENTED / NOT_ACTIVE

## Preserved unresolved state

EphemeralFileSandboxEffectAdapterR01 implementation:
NOT_IMPLEMENTED

SECE_SANDBOX_CONFINEMENT_PROFILE_R02 implementation:
NOT_IMPLEMENTED

platform evidence profile:
NOT_IMPLEMENTED / TO_BE_BOUND

sandbox target:
UNKNOWN_LATER_GATE

future bounded KOD sandbox implementation authority:
NOT_CREATED

G4 task/authority:
NOT_CREATED

G5 authority:
NOT_CREATED

G6 authority:
NOT_CREATED

historical task/PROMPT replay:
FORBIDDEN

hidden/unwritten KOD chat state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

unknown predecessor chat-only work:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check exact authority, registry and frontier;
2. verify current ARH writer;
3. verify exact KOD self-snapshot commit/blob;
4. verify current KOD writer exact blob/status;
5. verify v06 still exists and remains immutable predecessor recovery;
6. verify target v07 path absent;
7. verify no competing ARH KOD v07 attempt/result/registry exists;
8. verify source-set r07 current;
9. verify exact KOD R04 / SHD R04 / SIS R07 / SHD D1D2 identities;
10. verify sandbox implementation and G4/G5/G6 authority remain NOT_CREATED.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1

authority_blob:
3d0a47c93cff551322240fa7503090a35f168efc

frontier_commit:
c7bff8dd4a77ed62689ce6bf3298fe6167dc25bb

frontier_blob:
34c863899cfd621899f82c3a040470b9bba595f1

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
84b468944a569eef7d2411366f4773c714d86de6

source_snapshot_blob:
c7ed1f606e87b843149732f4601edcffa559a4b8

source_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

previous_recovery_ref:
51704f5eb7a4bf43210c9760905f486a2e58b5ce

target_path:
entities/kod/recovery/versions/kod-recovery-v07

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Recovery package authorship boundary

ARH may create recovery-owned metadata only.

ARH must preserve the exact current-writer-authored self-snapshot without substantive alteration.

ARH must NOT:
- reconstruct hidden/unwritten KOD state;
- reconstruct predecessor chat-only work;
- modify KOD R04 or other implementation packages;
- create sandbox implementation authority;
- create or infer G4/G5/G6 authority;
- select an execution target;
- change KOD writer-state.

## Required v07 package functions

Build one standalone immutable recovery package under:

entities/kod/recovery/versions/kod-recovery-v07

Use a compact canon-compliant package.

Required functions:

1. exact copy of:
   KOD__v07-pre-sandbox-implementation-self-snapshot__KOO-ARH.md

2. exact copy of:
   KOD__replacement-current-writer-v07.md

3. ROLE-IDENTITY.md
   exact KOD role identity / active role-source binding only.

4. SOURCES.md
   exact active source-set r07 identities.

5. TASK-STATE.md
   preserve only confirmed state:
   - KOD R04 result/package/tree;
   - KOD R04 candidate NOT_ACTIVATED;
   - SHD R04 static PASS;
   - SIS R07 runtime PASS / 22/22 / no live effect;
   - SHD D1D2 PASS / D1 closed / D2 closed / corrected design tree;
   - sandbox adapter implementation NOT_IMPLEMENTED;
   - confinement profile implementation NOT_IMPLEMENTED;
   - platform evidence profile TO_BE_BOUND;
   - sandbox target UNKNOWN_LATER_GATE;
   - sandbox implementation authority NOT_CREATED;
   - G4/G5/G6 authority NOT_CREATED;
   - historical replay FORBIDDEN;
   - hidden/unwritten state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

6. KOD__recovery-initiation-boundary-v07.md
   ARH-owned procedural recovery metadata only.
   Future initiation, if separately authorized, must verify this exact immutable package.
   Recovery itself creates no Writer Gate, implementation authority, G4/G5/G6 authority or deployment/live authority.

7. RECOVERY-LINEAGE.md
   bind v06 predecessor, KOD v0.7 current writer and exact self-snapshot.

8. RECOVERY-MANIFEST.md

9. SHA256SUMS.txt

Do not create unrelated reports inside the external package.

## Integrity requirements

Before final publication:
- final composition fixed;
- provenance for every file verified;
- SHA-256 calculated from final bytes;
- Git blob identities recorded where applicable;
- no secrets/private-key/credential values included.

SHA256SUMS must cover every non-checksum file.

Do not substitute Git blob identity for SHA-256 where checksum verification is claimed.

## External publication

Publish exactly to:

puev5691/wellbeing-entity-bootstrap:
entities/kod/recovery/versions/kod-recovery-v07

Record:
- publication commit/ref;
- exact version path;
- package tree;
- composition;
- each external blob;
- SHA-256 identities.

## Immutable readback

After publication independently read back the exact immutable v07 version.

Verify:
- path -> tree binding;
- exact expected composition;
- source self-snapshot external equality;
- current-writer external equality;
- manifest matches actual tree;
- SHA256SUMS entries match independently recomputed final bytes;
- no unexplained missing/extra files;
- no current-state conflict.

Publication alone is NOT PASS.

## Recovery registry

Create a NEW registry entry:

entities/archivarius/current/recovery-registry/ARH__KOD-recovery-v07.md

It must include:
- source self-snapshot locator/blob;
- KOD current-writer locator/blob/status;
- predecessor recovery v06 immutable locator/tree and stale classification;
- new external v07 immutable locator/ref/path/tree;
- composition/integrity/readback;
- KOD R04 / SHD R04 / SIS R07 / SHD D1D2 state;
- sandbox implementation and G4/G5/G6 remain NOT_CREATED;
- historical replay NONE;
- KOD current-writer mutation NONE by this preservation task.

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

On PASS classify v07 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_PRE_SANDBOX_IMPLEMENTATION

Do NOT infer sandbox implementation or G4 authority from this classification.

If required evidence is missing/conflicting:
return exact BLOCKED_/FAIL_ terminal and do not claim v07 current.

## Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__KOD-v07-external-recovery__KOO-KOD.md

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED locator/blob;
- source self-snapshot locator/blob;
- KOD current-writer locator/blob/status;
- predecessor recovery v06 locator/tree/classification;
- new v07 immutable locator/ref/path/tree;
- package composition;
- exact external blobs/checksums;
- immutable readback verdict;
- registry locator/commit/blob/readback;
- success classification;
- preserved sandbox/G4 boundaries;
- exact terminal.

Expected PASS terminal:

PASS_ARH_KOD_V07_EXTERNAL_RECOVERY

## Hard boundaries

Do NOT:
- implement sandbox adapter or confinement/platform profile;
- create G4/G5/G6 authority;
- select/mutate sandbox target;
- change KOD writer-state;
- replay historical tasks/prompts;
- mutate Project Sources/canons;
- perform deployment/live/production/provider/API/Telegram effects;
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
- new v07 immutable recovery locator/ref/path/tree;
- composition/checksum/readback verdicts;
- registry locator/commit/blob;
- current KOD writer identity;
- previous v06 disposition;
- KOD R04 / SHD R04 / SIS R07 / SHD D1D2 state;
- sandbox implementation/G4/G5/G6 state;
- remaining blockers/UNKNOWNs.

Include exact line:

Fresh-reconcile this exact ARH KOD v07 recovery result. Do not infer sandbox implementation or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
