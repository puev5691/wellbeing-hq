# KOO -> ARH: SHT r02 post-Writer external recovery r03 preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

Perform ONLY external preservation of the exact current SHT post-Writer self-snapshot into a NEW immutable SHT recovery successor r03, followed by immutable readback, integrity verification and recovery-registry accounting.

Do NOT perform profile work, narrow rereview, Writer Gate, writer mutation, historical replay or SECE continuation.

## Exact authority

puev5691/wellbeing-hq@3a0292a49d396fc498467e17fe768eaa594b0411:
entities/koordinator/outbox/ARH_SHT_r02_post_writer_external_recovery_R03_authority.md

blob:
3055cad5e47a03be2d6a90d48fa34906896a0fce

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Exact registry

puev5691/wellbeing-hq@c6b1a6a7b4bcdca984daf70aa71811a67190cc16:
entities/koordinator/outbox/ARH_SHT_r02_post_writer_external_recovery_R03_registry.md

blob:
f6b841ebe9ac29f768a628491a4bc5560ced1fd0

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@fdeb7a240bcc31da190f8e3aea51e88668ba4157:
entities/koordinator/outbox/ARH_SHT_r02_post_writer_external_recovery_R03_frontier.md

blob:
041cccc62ba26b022c30027bf1072d782f4fc34b

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

If current ARH writer changed, was superseded, or a competing ARH preservation attempt/result exists:
STOP with exact blocker.

## Exact current SHT self-snapshot

puev5691/wellbeing-hq@f0a49469c6b318df0d1b436c011f1f459df29f47:
entities/shtabist/outbox/SHT__replacement-r02-post-writer-self-snapshot__KOO-ARH.md

blob:
6d48804adfb190d211ffea7c20f80fbde0135e64

status:
SELF_SNAPSHOT_PRESERVED_BY_CURRENT_WRITER

immutable_readback:
PASS

This exact file is authoritative SHT self-state authored by current SHT writer.

ARH may preserve exact bytes/reference it.
ARH must NOT rewrite its substantive SHT self-state.

## Current authoritative SHT writer

puev5691/wellbeing-hq@7ed8b5570d3aa610120ab4a541b4d03ca032cf3b:
entities/shtabist/current/SHT__replacement-current-writer-r02.md

blob:
591a5c474523f46ad84b5c49c62939832b87b15c

status:
WRITER_ESTABLISHED

writer_generation:
SHT-REPLACEMENT-R02

instance_binding_id:
SHT_R02_WRITER_BOUND_TO_A2_RESULT_7133F0

## Exact Writer Gate result

puev5691/wellbeing-hq@93fdb47de6014e16399614d2a185a95a841ade34:
entities/shtabist/outbox/SHT__replacement-writer-gate-r02-A1-result__KOO.md

blob:
4ed81c3587ae4d8efeee306b271e7a3ffcac1911

terminal:
PASS_SHT_REPLACEMENT_CURRENT_WRITER_R02

## Previous external recovery

puev5691/wellbeing-entity-bootstrap@c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5:
entities/sht/recovery/versions/sht-recovery-r02

tree:
f561246223a48ac885d7baae383898cc8e89af16

classification:
LAST_VERIFIED_RECOVERY_BASIS_BUT_STALE_AFTER_WRITER_HANDOFF

Do NOT rewrite or delete r02.

## Target successor

Repository:

puev5691/wellbeing-entity-bootstrap

Create exactly one new immutable successor at:

entities/sht/recovery/versions/sht-recovery-r03

Before publication verify this path does NOT already exist.

If it exists or any competing r03 successor/registry/result appears:
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

Do not substitute candidates/drafts.

## Preserved project/task boundary

profile_continuation:
PAUSED_BY_OPERATOR

D1D2:
COMPLETED_PASS

D1D2 terminal:
PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW

D1D2 corrected package tree:
84979101d6bd19fd939f978652f03317f6e524b9

narrow_rereview:
NOT_STARTED / NOT_AUTHORIZED

profile_task_authority:
NOT_CREATED

historical_task/PROMPT replay:
FORBIDDEN

SECE continuation:
NOT_AUTHORIZED

hidden/unwritten state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check exact authority, registry, frontier;
2. verify current ARH writer;
3. verify exact SHT self-snapshot commit/blob;
4. verify current SHT writer exact commit/blob/generation;
5. verify Writer Gate result exact commit/blob/terminal;
6. verify r02 still exists and remains immutable predecessor recovery;
7. verify target r03 path absent;
8. verify no competing ARH r03 attempt/result/registry exists;
9. verify source-set r07 current;
10. verify profile_continuation remains PAUSED_BY_OPERATOR and narrow rereview remains NOT_AUTHORIZED.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1

authority_blob:
3055cad5e47a03be2d6a90d48fa34906896a0fce

frontier_commit:
fdeb7a240bcc31da190f8e3aea51e88668ba4157

frontier_blob:
041cccc62ba26b022c30027bf1072d782f4fc34b

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
f0a49469c6b318df0d1b436c011f1f459df29f47

source_snapshot_blob:
6d48804adfb190d211ffea7c20f80fbde0135e64

source_writer_commit:
7ed8b5570d3aa610120ab4a541b4d03ca032cf3b

source_writer_blob:
591a5c474523f46ad84b5c49c62939832b87b15c

previous_recovery_ref:
c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5

target_path:
entities/sht/recovery/versions/sht-recovery-r03

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Recovery package authorship boundary

ARH may create recovery-owned metadata only.

ARH must preserve the exact current-writer-authored self-snapshot without substantive alteration.

ARH must NOT:
- reconstruct hidden/unwritten SHT state;
- rewrite SHT task conclusions;
- create profile authority;
- change writer-state;
- promote narrow rereview;
- infer continuation from D1D2 terminal PASS.

## Required r03 package functions

Build one standalone immutable recovery package under:

entities/sht/recovery/versions/sht-recovery-r03

Use a compact package with the same functional pattern as r02 unless a canon-compliant reason requires otherwise.

Required functions:

1. exact copy of current SHT self-snapshot:
   SHT__replacement-r02-post-writer-self-snapshot__KOO-ARH.md

2. exact copy of current writer:
   SHT__replacement-current-writer-r02.md

3. ROLE-IDENTITY.md
   exact role identity / active role-source binding only.

4. SOURCES.md
   exact active source-set r07 identities.

5. TASK-STATE.md
   preserve only confirmed state:
   - profile_continuation PAUSED_BY_OPERATOR;
   - D1D2 COMPLETED_PASS;
   - corrected package tree 84979101d6bd19fd939f978652f03317f6e524b9;
   - narrow rereview NOT_STARTED / NOT_AUTHORIZED;
   - profile_task_authority NOT_CREATED;
   - historical replay FORBIDDEN;
   - SECE continuation NOT_AUTHORIZED;
   - hidden/unwritten state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

6. SHT__recovery-initiation-boundary-r03.md
   ARH-owned procedural recovery metadata only.
   It must say that future initiation, if separately authorized, must verify this exact immutable r03 package and that recovery does not itself create Writer Gate/profile authority.

7. RECOVERY-LINEAGE.md
   bind r02 predecessor, post-Writer self-snapshot, current writer r02 and Writer Gate result.

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

Do not substitute Git blob identity for SHA-256 verification where checksums are claimed.

## External publication

Publish exactly to:

puev5691/wellbeing-entity-bootstrap:
entities/sht/recovery/versions/sht-recovery-r03

Record:
- publication commit/ref;
- exact version path;
- package tree;
- exact composition;
- each external file blob;
- SHA-256 identities.

## Immutable readback

After publication independently read back the exact immutable r03 version.

Verify:
- path -> tree binding;
- exact expected composition;
- source snapshot external equality;
- current-writer external equality;
- manifest matches actual tree;
- SHA256SUMS entries match independently recomputed final bytes;
- no unexplained missing/extra files;
- no current-state conflict.

Publication alone is NOT PASS.

## Recovery registry

Create/update the established ARH SHT recovery registry with a NEW r03 record:

entities/archivarius/current/recovery-registry/ARH__SHT-recovery-r03.md

It must include:
- source snapshot locator/blob;
- SHT current-writer locator/blob/generation;
- Writer Gate result locator/blob;
- predecessor recovery r02 immutable locator/tree and stale classification;
- new external r03 immutable locator/ref/path/tree;
- composition/integrity/readback;
- profile_continuation PAUSED_BY_OPERATOR;
- D1D2 COMPLETED_PASS;
- narrow rereview NOT_STARTED / NOT_AUTHORIZED;
- profile_task_authority NOT_CREATED;
- historical replay NONE;
- SECE continuation NOT_AUTHORIZED;
- current-writer mutation NONE by this preservation task.

Fresh-readback registry.

## Success classification

Return:

EXTERNALLY_PRESERVED_READBACK_PASS

only if:
- source snapshot exact;
- current writer exact;
- package publication complete;
- immutable readback complete;
- checksums independently PASS;
- registry PASS;
- no conflict/supersession exists.

On PASS, classify r03 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_SHT_REPLACEMENT_R02

Do NOT infer any profile authority from this classification.

If any required evidence is missing/conflicting:
return exact BLOCKED_/FAIL_ terminal and do not claim r03 current.

## Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__SHT-r02-post-writer-external-recovery-r03__KOO-SHT.md

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED locator/blob;
- source self-snapshot locator/blob;
- SHT current-writer locator/blob/generation;
- Writer Gate result locator/blob;
- previous recovery r02 locator/tree/classification;
- new r03 immutable locator/ref/path/tree;
- package composition;
- exact external blobs/checksums;
- immutable readback verdict;
- registry locator/commit/blob/readback;
- success classification;
- profile/task boundaries;
- exact terminal.

Expected PASS terminal:

PASS_ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03

## Hard boundaries

Do NOT:
- change SHT writer-state;
- perform SHT Initiation Gate or Writer Gate;
- authorize/perform narrow rereview;
- resume SECE;
- create any profile task;
- replay historical task/PROMPT;
- mutate Project Sources/canons;
- perform deployment/live/production/provider/API/Telegram effects;
- automatically continue downstream.

## Mandatory return to KOO

After durable result + readback, return one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- exact ARH attempt;
- result locator/commit/blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- new r03 immutable recovery locator/ref/path/tree;
- composition/checksum/readback verdicts;
- registry locator/commit/blob;
- current SHT writer identity;
- previous r02 disposition;
- profile_continuation;
- D1D2 state;
- narrow rereview state;
- profile_task_authority state;
- remaining blockers/UNKNOWNs;
- line:

Fresh-reconcile this exact ARH r03 preservation result. Do not infer profile continuation or narrow rereview authority.

End:

STOP.

After that block add nothing.
