# KOO -> ARH: SHT replacement external recovery preservation r0.1

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_SHT_REPLACEMENT_EXTERNAL_RECOVERY_PRESERVATION_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

OPERATOR explicitly requires ARH external preservation/checkpoint for preparation of a genuinely new SHT instance.

Perform ONLY external SHT recovery preservation + immutable readback + recovery-registry accounting.

Do NOT perform Initiation Gate, Writer Gate, writer transfer, profile work or historical task replay.

## Exact authority

puev5691/wellbeing-hq@b8be901dec5a3b976522b6602ebbd490149c8544:
entities/koordinator/outbox/ARH_SHT_replacement_external_recovery_preservation_R01_authority.md

blob:
ec1ac4f482d108c077fb3acc2aad03b7b1ee6ed2

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Exact registry

puev5691/wellbeing-hq@9c7210a85d706d1a5058c1c09e965638062833bf:
entities/koordinator/outbox/ARH_SHT_replacement_external_recovery_preservation_R01_registry.md

blob:
b6b60b5efa7ee4e98af8a08a4ff3c32b81680360

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@f997662396537d9e640a36e3ef22be1efef2b9e4:
entities/koordinator/outbox/ARH_SHT_replacement_external_recovery_preservation_R01_frontier.md

blob:
6cb8244c795a6959214e3b8b030637ab6ba29740

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

If ARH writer is replaced/frozen/superseded or competing writer evidence exists:
STOP and return exact blocker.

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check authority, registry, frontier, current ARH writer, exact SHT self-snapshot, SHT writer, external SHT recovery inventory and supersession;
2. confirm exact attempt:
   ARH_SHT_REPLACEMENT_EXTERNAL_RECOVERY_PRESERVATION_R01_A1;
3. create positive PROCESSING_STARTED evidence bound to:
   commit f997662396537d9e640a36e3ef22be1efef2b9e4
   blob 6cb8244c795a6959214e3b8b030637ab6ba29740;
4. immutable-readback PROCESSING_STARTED;
5. only then perform preservation.

Publication/inbox/dispatch/automatic activation do NOT prove processing_started.

## Exact authoritative SHT self-snapshot

puev5691/wellbeing-hq@71f850f6b539a5b6d0625cae081bb422900e7271:
entities/shtabist/outbox/SHT__replacement-self-snapshot-preservation-r01__KOO-ARH.md

blob:
d00ce349aebad0fa7e72719cb99d616185b65d93

immutable readback:
MATCH

Snapshot author:
current authoritative SHT writer.

## Current SHT writer evidence

entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

writer_generation:
SHT-CURRENT-INSTANCE-R01

status:
CURRENT_WRITER

ARH may COPY exact bytes/reference this writer evidence for recovery.
ARH must NOT edit its substantive meaning and must NOT transfer/freeze writer authority.

## SHT replacement/profile boundary

Further SHT profile continuation:
PAUSED_BY_OPERATOR

automatic historical task/PROMPT replay:
FORBIDDEN

New SHT instance:
NOT_CREATED

New SHT Initiation Gate:
NOT_YET_PERFORMED

New SHT Writer Gate:
NOT_AUTHORIZED / NOT_PERFORMED

Current SHT writer remains current until separate lawful change.

## Current completed SECE evidence to preserve

attempt:
SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1

authority:

puev5691/wellbeing-hq@48dbe1b9d942c764cd10105264d26a795c0bd13f:
entities/koordinator/outbox/SHT_SECE_sandbox_gate_design_D1D2_correction_R02_authority.md

blob:
87ce1458c58493d87fd4568c698562feb67c0313

accepted frontier:

puev5691/wellbeing-hq@24729f0c89d6608a15ef9b8e2a47b8af952ba7ff:
entities/koordinator/outbox/SHT_SECE_sandbox_gate_design_D1D2_correction_R02_frontier.md

blob:
3d7f6717e3ed162464192ecf6f2880591f405d8b

PROCESSING_STARTED:

puev5691/wellbeing-hq@a73a69f104c79444a5ea21bc44e7b96bf995b309:
entities/shtabist/outbox/execution-evidence/SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1__PROCESSING_STARTED_E1.md

blob:
8ba91ff5088755524f077c59a2310bc6b729304c

terminal/result:

puev5691/wellbeing-hq@0ff3709612df21ca4e0f8abc914f1831a8ec2657:
entities/shtabist/outbox/SHT__SECE-r01-sandbox-gate-design-D1D2-correction-r02__KOO.md

blob:
e32ba475182b059709ed97c48973f43c8a071411

terminal:
PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW

corrected package tree:
84979101d6bd19fd939f978652f03317f6e524b9

classification:
COMPLETED_PASS

Earlier terminal-not-found observation:
HISTORICAL_EVIDENCE_ONLY

Narrow rereview:
NOT_STARTED
NOT_AUTHORIZED solely from terminal PASS

Do NOT reinterpret this attempt as unfinished.

## Previous independently verified external SHT recovery

puev5691/wellbeing-entity-bootstrap@b34dd2cda94c2f61acc59a5f066c38bd24fdae0c:
entities/sht/recovery/current

Independent ARH checksum verification:

puev5691/wellbeing-hq@7f309553d1fa098e5759782055ae184f7d7a2977:
entities/archivarius/outbox/ARH__SHT-recovery-checksum-verify-r01-result__KOO-SHT.md

blob:
fa6f3ec51e17b3b399ca7475942178f2906dbf7e

terminal:
PASS_ARH_SHT_RECOVERY_CHECKSUM_VERIFY_R01_4_OF_4

This is the last independently verified external SHT recovery lineage/basis.

It is STALE relative to the new current-writer self-snapshot.

Do NOT delete it.
Do NOT rewrite it in place.
Do NOT mutate entities/sht/recovery/current under this task.

## Active approved Project Sources

Use the active source-set confirmed by:

puev5691/wellbeing-hq:
entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Active source identities:

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

Do not substitute candidate/draft source revisions.

## Prior delivery/activation boundary

Self-snapshot dispatch:

7eed76a3b9e0151e26d2d21034803251603c9714

ARH inbox placement:

1005f687cc1e50396ca495d7aa6f5d7b041fe3d7

Automatic activation record:

3d954c0cc8b5aaf19725eb420171029f58634434

activation_status:
activation_failed

processing_started:
no

receipt:
NOT_PROVEN

acceptance:
NOT_PROVEN

This manual PROMPT is the activation handoff for the newly authorized preservation attempt.
Do not treat the older inbox/activation attempt as processing_started.

# Required preservation procedure

## 1. Fresh external inventory

Before external mutation:

- inspect puev5691/wellbeing-entity-bootstrap SHT recovery contour;
- verify old exact recovery ref/path still exists;
- verify no newer SHT recovery successor already exists;
- verify no competing ARH SHT preservation attempt/result;
- verify SHT source snapshot/blob unchanged;
- verify SHT current-writer evidence unchanged;
- verify no superseding OPERATOR replacement decision;
- verify no narrow rereview/profile continuation authority has been inferred.

Any competing successor/current-state conflict:
STOP with exact blocker.

## 2. New immutable successor only

Create ONE new immutable versioned SHT recovery successor in:

repository:
puev5691/wellbeing-entity-bootstrap

recovery root:
entities/sht/recovery/versions/

Select one fresh non-colliding version directory after inventory.

Return the exact chosen version path.

Do NOT:
- overwrite old entities/sht/recovery/current;
- delete historical recovery;
- rewrite old commit/ref;
- infer a new current-writer.

The immutable versioned successor itself will be the later cold-start locator if preservation PASSes.

## 3. Package authorship boundary

The exact SHT self-snapshot is foreign authoritative self-state authored by SHT current-writer.

ARH may:
- copy exact bytes;
- preserve exact references;
- create ARH-owned recovery metadata, manifest, checksum list, source/lineage record and procedural recovery/initiation boundary.

ARH must NOT:
- edit/rewrite SHT self-snapshot semantics;
- manufacture missing SHT profile state;
- reconstruct hidden/unwritten chat-state;
- convert UNKNOWN to known by inference.

If active Recovery Canon requires a current-writer-authored input that is not available and cannot be satisfied by exact immutable existing inputs:
STOP with BLOCKED_MISSING_CURRENT_WRITER_AUTHORED_RECOVERY_INPUT.
Do not invent it.

## 4. Minimum successor package

Build a standalone recovery package sufficient for a later NEW SHT Initiation Gate.

Minimum expected functions/files:

A. exact copy of current SHT self-snapshot:
SHT__replacement-self-snapshot-preservation-r01__KOO-ARH.md

B. exact current-writer evidence copy or immutable identity carrier:
source writer path/blob/generation/status.

C. recovery-owned procedural initiation boundary:
must state only:
- genuinely new SHT instance;
- Initiation-required;
- verify exact immutable external recovery locator/version/integrity;
- load active approved Project Sources;
- historical PROMPT/task replay forbidden;
- Initiation Gate only;
- Writer Gate not included;
- profile work not included;
- current predecessor writer remains current until separate lawful Writer Gate;
- after initiation, return result to KOO/OPERATOR and STOP.

This procedural file is recovery metadata, NOT SHT self-state and NOT authority for Initiation Gate by itself.

D. SOURCES / exact active source identity list.

E. recovery lineage:
- old external recovery exact ref/path;
- old checksum verification;
- stale limitation;
- exact current self-snapshot;
- exact completed D1D2 state;
- PAUSED_BY_OPERATOR;
- narrow rereview NOT_STARTED/NOT_AUTHORIZED;
- historical replay FORBIDDEN.

F. RECOVERY-MANIFEST.

G. SHA256SUMS or equivalent canon-compliant integrity list.

You may use different filenames if necessary, but package functions above must be explicit and independently verifiable.

Do not create unrelated reports/files.

## 5. Integrity and secret boundary

Before publication:
- verify final package composition;
- verify provenance of every file;
- calculate SHA-256 after final file bytes are fixed;
- record Git blob identity where applicable;
- scan for secret/private-key/credential-value content inappropriate for external recovery;
- do not place secrets into recovery package.

If exact-byte hashing is unavailable:
BLOCK.
Do not substitute Git blob equality for an independently required checksum if the package manifest claims SHA-256 verification.

## 6. External publication

Publish the package into the fresh version directory under:

entities/sht/recovery/versions/

Record:
- exact publication commit/ref;
- exact version path;
- package tree if available;
- exact composition count;
- each external file blob;
- each required checksum.

Old recovery remains immutable lineage.

## 7. Immutable external readback

After publication, independently read back the external version.

Verify:
- expected composition exactly present;
- source snapshot external copy bytes/blob match the accepted source;
- source writer evidence copy/identity matches expected;
- manifest references exact version;
- checksum file matches final external contents;
- independently recomputed checksums PASS;
- no missing/extra unexplained files;
- immutable ref/path sufficient for new instance verification.

Publication alone is NOT PASS.

## 8. Recovery registry

Create or update one minimal SHT recovery record in the established ARH recovery-registry contour.

It must state at minimum:
- entity SHT;
- source snapshot locator/blob;
- source writer locator/blob/generation;
- previous external recovery locator/ref;
- new external recovery immutable locator/ref/path;
- composition/integrity/readback;
- stale/recoverability limitations;
- profile continuation PAUSED_BY_OPERATOR;
- D1D2 current task classification COMPLETED_PASS;
- narrow rereview NOT_STARTED/NOT_AUTHORIZED;
- Initiation Gate NOT_PERFORMED;
- Writer Gate NOT_PERFORMED;
- current writer transfer NOT_PERFORMED;
- historical replay NONE.

If a competing SHT registry record appears during execution:
reconcile before writing; do not last-write-wins.

## 9. Recoverability classification

Return one exact classification:

READY_FOR_REPLACEMENT_INITIATION_HANDOFF

only if:
- exact source snapshot accepted;
- package composition sufficient;
- external immutable publication PASS;
- external readback/integrity PASS;
- registry PASS;
- no current-state conflict;
- no required recovery input is missing.

Otherwise return exact BLOCKED_/FAIL_ status.

Do NOT perform the Initiation Gate itself.

# Hard boundaries

Do NOT:
- transfer/freeze SHT current-writer;
- establish a new SHT current-writer;
- execute Initiation Gate;
- execute Writer Gate;
- create or execute narrow rereview;
- resume SECE profile work;
- replay historical task/PROMPT;
- mutate the D1D2 package;
- mutate Project Sources/canons;
- infer receipt/acceptance from inbox;
- create automation authority;
- perform production/live effects.

# Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__SHT-replacement-external-recovery-r01__KOO-SHT.md

Result must include:

- exact ARH attempt;
- authority/registry/frontier identities;
- PROCESSING_STARTED locator/blob;
- exact accepted SHT self-snapshot locator/blob;
- source SHT writer locator/blob/generation;
- previous recovery locator/ref and stale classification;
- chosen new external version locator/ref/path;
- package composition;
- manifest/checksum identities;
- external publication result;
- immutable external readback;
- checksum verification;
- secret boundary;
- recovery registry locator/commit/blob;
- recoverability classification;
- Initiation Gate NOT_PERFORMED;
- Writer Gate NOT_PERFORMED;
- current-writer transfer NOT_PERFORMED;
- profile continuation PAUSED;
- historical replay NONE;
- exact terminal;
- commit;
- blob.

Expected PASS terminal class:

PASS_ARH_SHT_REPLACEMENT_EXTERNAL_RECOVERY_R01_READY_FOR_INITIATION_HANDOFF

or exact BLOCKED_/FAIL_ terminal.

# Mandatory return block to KOO

After durable result + immutable readback, the final chat content must be one copy-paste block beginning literally:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- exact ARH attempt;
- result locator;
- commit;
- blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- exact new external recovery immutable locator/ref/path;
- package tree/composition;
- integrity/checksum/readback verdicts;
- recovery registry locator/commit/blob;
- recoverability classification;
- predecessor writer state;
- Initiation Gate state;
- Writer Gate state;
- profile continuation state;
- remaining blockers/UNKNOWNs if any;
- what was NOT authorized/performed;
- exact instruction:

Fresh-reconcile this exact preservation result. If and only if recovery is READY_FOR_REPLACEMENT_INITIATION_HANDOFF, prepare one human-ready NEW SHT cold-start PROMPT for Initiation Gate only. Do not infer Writer Gate or profile continuation authority.

End literally:

STOP.

After that block add nothing.
