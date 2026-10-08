# KOO -> ARH: KOD external recovery v08 preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_KOD_V08_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

Perform ONLY external preservation of the exact current KOD v0.7 post-review self-snapshot into a NEW immutable KOD recovery successor v08, followed by integrity verification, immutable readback and recovery-registry accounting.

Do NOT implement corrections.
Do NOT mutate candidate af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2.
Do NOT create or infer G4/G5/G6 authority.
Do NOT execute sandbox effects.
Do NOT select a sandbox target.
Do NOT change KOD writer-state.
Do NOT replay historical tasks/prompts.

## Exact authority

puev5691/wellbeing-hq@aa73b2756240aa8f784e6726baf07bd49d24699f:
entities/koordinator/outbox/ARH_KOD_v08_external_recovery_authority.md

blob:
f558be055cc5c5a40249f224e29077f72d1431e8

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Registry

puev5691/wellbeing-hq@9bbb40deb800d803a62d7052e3286dfa79425e91:
entities/koordinator/outbox/ARH_KOD_v08_external_recovery_registry.md

blob:
d0a178b3af72c7a7c8b060761833bdc5d9059b12

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@962c872ceffc3743678668a5f1b08efd4ed52512:
entities/koordinator/outbox/ARH_KOD_v08_external_recovery_frontier.md

blob:
7f98785a2c9af21af2a8428acf4be2237aaa3612

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

If ARH writer changed/superseded or a competing KOD v08 preservation attempt/result/registry exists:
STOP with exact blocker.

## Exact KOD self-snapshot

puev5691/wellbeing-hq@6253f8d01c8c89175cf6d7c9c222c905cae722b1:
entities/koder/outbox/KOD__v07-post-sandbox-impl-review-pre-correction-self-snapshot__KOO-ARH.md

blob:
2f75948fbb8171a0ff59a1c397a8d5936015e963

terminal:
PASS_KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION_SELF_SNAPSHOT_R01_READY_FOR_ARH_EXTERNAL_RECOVERY_V08

immutable_readback:
PASS

This exact file is authoritative KOD self-state authored by the current KOD writer.
ARH may preserve exact bytes/reference it.
ARH must NOT rewrite or reconstruct its substantive KOD self-state.

## Current authoritative KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

## Previous external KOD recovery

puev5691/wellbeing-entity-bootstrap@34650c6b255ad204674b778de8d39910a61ba8f1:
entities/kod/recovery/versions/kod-recovery-v07

tree:
70d9ab5f452541c3fd697b40711be4242e0c6969

classification:
LAST_EXTERNALLY_VERIFIED_KOD_RECOVERY_BEFORE_SANDBOX_IMPLEMENTATION_R01 / STALE_RELATIVE_TO_LATER_SANDBOX_IMPLEMENTATION_R01_AND_SHD_REVIEW_R01

Do NOT rewrite or delete v07.

## Target successor

Repository:
puev5691/wellbeing-entity-bootstrap

Create exactly one NEW immutable successor at:

entities/kod/recovery/versions/kod-recovery-v08

Before publication verify the target path does NOT already exist.

If v08 exists or any competing v08 recovery/registry/result appears:
STOP with exact conflict.

## Active approved Project Sources

Active source-set:
r07

Basis:
entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Required active identities:

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

## Exact later KOD state to preserve

Implementation R01 result:

puev5691/wellbeing-hq@c7979afefeb7dc7c33ab24d84039aa374112954e:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-r01__KOO.md

blob:
69a24ea931db365089393c75d13f1ac151593def

candidate:

puev5691/wellbeing-hq@27134205e21ebc44308606de4cb59f7b3b3ed577:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-r01/

tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

candidate:
NOT_ACTIVATED

real_sandbox_effect:
NOT_EXECUTED

sandbox_target:
UNKNOWN / NOT_SELECTED

Exact SHD review:

puev5691/wellbeing-hq@ab128ba972282ea10ed3ebef51e64bab067036b4:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-r01-review-r01__KOO.md

blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

terminal:
NEEDS_REWORK_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_REVIEW_R01

final_verdict:
NEEDS_REWORK_SANDBOX_IMPLEMENTATION_R01

Preserved PASS:
- candidate integrity PASS;
- outcome fail-closed PASS;
- non-live boundary preserved;
- accepted D1/D2 architecture remains valid.

Preserve exact bounded defect classes:

D1-A:
canonical sandbox/root binding validation missing.

D1-B:
CREATED_SANDBOX_OBJECT_IDENTITY missing mandatory no_symlink_reparse_evidence binding.

D2-A:
cleanup eligibility missing exact operation/owner/root/target identity comparisons.

P1:
Linux/POSIX profile identity-class/profile binding validation incomplete.

Tests/evidence hygiene:
negative coverage missing for the above mismatch/forgery cases;
top-level TEST-SUMMARY.json is stale predecessor R04 metadata and must not be used as sandbox-candidate PASS evidence.

Correction authority/task/result:
NOT_CREATED

G4/G5/G6 authority:
NOT_CREATED

G4 execution:
NOT_STARTED

historical replay:
FORBIDDEN

hidden/unwritten KOD state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check exact authority, registry and frontier;
2. verify current ARH writer;
3. verify exact KOD self-snapshot commit/blob;
4. verify current KOD writer exact blob/status;
5. verify v07 exists and remains immutable predecessor recovery;
6. verify target v08 path absent;
7. verify no competing ARH KOD v08 attempt/result/registry exists;
8. verify source-set r07 current;
9. verify exact implementation R01 result/candidate tree;
10. verify exact SHD NEEDS_REWORK result;
11. verify correction authority/task/result remain NOT_CREATED;
12. verify G4/G5/G6 authority remain NOT_CREATED.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_KOD_V08_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_KOD_V08_EXTERNAL_RECOVERY_R01_A1

authority_blob:
f558be055cc5c5a40249f224e29077f72d1431e8

frontier_commit:
962c872ceffc3743678668a5f1b08efd4ed52512

frontier_blob:
7f98785a2c9af21af2a8428acf4be2237aaa3612

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
6253f8d01c8c89175cf6d7c9c222c905cae722b1

source_snapshot_blob:
2f75948fbb8171a0ff59a1c397a8d5936015e963

source_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

previous_recovery_ref:
34650c6b255ad204674b778de8d39910a61ba8f1

candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

SHD_review_blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

target_path:
entities/kod/recovery/versions/kod-recovery-v08

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Recovery package authorship boundary

ARH may create recovery-owned metadata only.

ARH must preserve exact current-writer-authored self-snapshot without substantive alteration.

ARH must NOT:
- reconstruct hidden/unwritten KOD state;
- implement corrections;
- mutate candidate R01;
- create correction authority/task;
- create G4/G5/G6 authority;
- select sandbox target;
- change KOD writer-state;
- replay historical tasks/prompts.

## Required v08 package

Build one standalone immutable package under:

entities/kod/recovery/versions/kod-recovery-v08

Required functions:

1. exact copy:
   KOD__v07-post-sandbox-impl-review-pre-correction-self-snapshot__KOO-ARH.md

2. exact copy:
   KOD__replacement-current-writer-v07.md

3. ROLE-IDENTITY.md

4. SOURCES.md

5. TASK-STATE.md

Preserve only confirmed current state:
- implementation R01 result/candidate tree;
- candidate NOT_ACTIVATED;
- real sandbox effect NOT_EXECUTED;
- sandbox target UNKNOWN / NOT_SELECTED;
- SHD NEEDS_REWORK review and exact bounded defect classes;
- candidate integrity PASS;
- outcome fail-closed PASS;
- non-live boundary preserved;
- correction authority/task/result NOT_CREATED;
- G4/G5/G6 authority NOT_CREATED;
- historical replay FORBIDDEN;
- hidden/unwritten KOD state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

6. KOD__recovery-initiation-boundary-v08.md
   ARH-owned procedural recovery metadata only.
   Recovery itself creates no Writer Gate, correction authority, G4/G5/G6 authority or sandbox-effect authority.

7. RECOVERY-LINEAGE.md
   bind v07 predecessor, current KOD writer and exact self-snapshot.

8. RECOVERY-MANIFEST.md

9. SHA256SUMS.txt

Do not create unrelated reports inside external package.

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
entities/kod/recovery/versions/kod-recovery-v08

Record:
- publication commit/ref;
- exact version path;
- package tree;
- composition;
- external blobs;
- SHA-256 identities.

## Immutable readback

After publication independently read back exact immutable v08.

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

entities/archivarius/current/recovery-registry/ARH__KOD-recovery-v08.md

It must include:
- source self-snapshot locator/blob;
- KOD current-writer locator/blob/status;
- predecessor recovery v07 immutable locator/tree/stale classification;
- new v08 immutable locator/ref/path/tree;
- composition/integrity/readback;
- implementation R01 candidate tree/status;
- exact SHD NEEDS_REWORK result;
- exact bounded defect classes;
- correction authority/task/result remain NOT_CREATED;
- G4/G5/G6 authority NOT_CREATED;
- KOD current-writer mutation NONE;
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

On PASS classify v08 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION

Do NOT infer correction implementation or G4/G5/G6 authority.

If required evidence is missing/conflicting:
return exact BLOCKED_/FAIL_ terminal and do not claim v08 current.

## Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__KOD-v08-external-recovery__KOO-KOD.md

Expected PASS terminal:

PASS_ARH_KOD_V08_EXTERNAL_RECOVERY

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED locator/blob;
- source self-snapshot locator/blob;
- current KOD writer;
- predecessor v07 locator/tree/classification;
- new v08 locator/ref/path/tree;
- package composition/checksums/readback;
- registry locator/commit/blob;
- candidate tree/status;
- SHD review/defect set;
- correction authority status;
- G4/G5/G6 status;
- exact terminal.

## Hard boundaries

Do NOT:
- implement corrections;
- mutate candidate R01;
- create correction authority/task;
- create G4/G5/G6 authority;
- execute sandbox effect;
- select/mutate sandbox target;
- change KOD writer-state;
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
- v08 immutable recovery locator/ref/path/tree;
- composition/checksum/readback verdicts;
- registry locator/commit/blob;
- current KOD writer identity;
- previous v07 disposition;
- implementation R01 candidate tree/status;
- exact SHD NEEDS_REWORK result/defect classes;
- correction authority/task/result status;
- G4/G5/G6 status;
- remaining blockers/UNKNOWNs.

Include exact line:

Fresh-reconcile this exact ARH KOD v08 recovery result. Do not infer correction implementation or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
