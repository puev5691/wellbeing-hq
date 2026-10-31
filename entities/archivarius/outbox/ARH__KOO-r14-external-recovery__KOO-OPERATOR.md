# ARH -> KOO / OPERATOR: KOO recovery r1.4 external preservation result

status:
FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH

terminal:
FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH

attempt:
ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_READBACK_AND_COLD_START_PREPARATION_ONLY

project_time:
omitted

## Human result

The exact KOO r1.3 self-snapshot and current-writer were copied byte-for-byte into one new external r14 package. The external path, package tree, 9-file composition, three source-copy Git identities and manifest-to-tree correspondence all read back correctly.

The package cannot be accepted as a verified recovery basis: independent SHA-256 recomputation found a mismatch in the first checked checksum entry, the Human Interface Contract. The package is immutable after publication, so ARH did not rewrite it or silently replace its checksum file.

The predecessor r13 remains the last externally verified KOO recovery basis. No cold-start PROMPT was created because the exact task permits it only after r14 PASS.

## Exact task / authority / frontier

task:
puev5691/wellbeing-hq@cadb19b2e2e5a4c1db008565330b2d51d1fad420:entities/koordinator/outbox/KOO__ARH-KOO-r14-external-recovery__ARH.md

task_blob:
1b303f63fb4dc08306eb507b84977da14d6845a1

authority:
puev5691/wellbeing-hq@2729c7ad066ad1ba5dc7dc802db2c96fc995a3dc:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_authority.md

authority_blob:
3a92721b8a12ebe3d20632d610130ecccca5cb14

authority_status:
OPERATOR_TASK_AUTHORITY_RECORDED

accepted_frontier:
puev5691/wellbeing-hq@026ac6db4b3eec5d2c1263e195147c981a9ed8e6:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_frontier.md

frontier_blob:
3bab160572ffef647c902eff1dddfabf1858fbbd

accepted_state:
INITIAL_NOT_STARTED_V1

## PROCESSING_STARTED

locator:
puev5691/wellbeing-hq@3dac10bfde28298874a91bf027efbd12fb5b85ce:entities/archivarius/outbox/execution-evidence/ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

blob:
874cefeca16ae64cf6ce5073381f720c9b7ef025

immutable_readback:
PASS

## Exact source identities

KOO self-snapshot:
puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md

blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

terminal:
PASS_KOO_R13_SELF_SNAPSHOT_R14_READY_FOR_ARH_PRESERVATION

KOO current-writer:
puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:entities/koordinator/current/KOO__replacement-current-writer-r13.md

blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

status:
WRITER_ESTABLISHED

ARH current-writer:
entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

Human Interface Contract source:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13/KOO__human-interface-contract-r02.md

source/package blob:
fdea31034c370220dfb961993059500716ccfe20

## Predecessor r13 and new r14

Predecessor:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13

tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

disposition:
LAST_EXTERNALLY_VERIFIED_KOO_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOO_R13_WORK

New external r14:
puev5691/wellbeing-entity-bootstrap@f89bc6a414038fb741b968b620189c35cbd39006:entities/koo/recovery/versions/koo-recovery-r14

package_tree:
408111bf55bde1fe036bdf7519b969a34b83af71

Composition:
9/9 PASS

Exact copied source Git blob equality:
3/3 PASS

Manifest-to-tree correspondence:
PASS

External path-to-tree and immutable readback:
PASS

Missing/extra files:
NONE

## SHA-256 integrity blocker

SHA256SUMS.txt claims coverage:
8/8

Independent recomputation:
FAIL / STOPPED AT FIRST MISMATCH

Exact first mismatch:

file:
KOO__human-interface-contract-r02.md

package Git blob:
fdea31034c370220dfb961993059500716ccfe20

SHA256SUMS expected:
34e365fb9675dccc6deaa5f48095cd65975f723f1ac798ea6bd5271f193df2ce

independently recomputed SHA-256:
b8f9cfa56636127ed013bda7a67c2b0bb77f75099ac081c13f5b06f8a2aa0175

byte length:
4015

remaining checksum entries:
NOT_RECOMPUTED_AFTER_FAIL-FAST

This mismatch is sufficient to fail the package integrity gate. No in-place repair or replacement publication was attempted.

## Recovery registry

locator:
puev5691/wellbeing-hq@1172fff6b8290f26d128a2d85580f1ac7cfde957:entities/archivarius/current/recovery-registry/ARH__KOO-recovery-r14.md

blob:
60837400e0dda55566cfc730a8a1f30f8bce8571

immutable_readback:
PASS

registry_status:
EXTERNAL_RECOVERY_PUBLICATION_READBACK_FAIL

recovery_classification:
BLOCKED_SHA256SUMS_MISMATCH

r14 is NOT a verified current external recovery basis.
r13 remains the last externally verified recovery basis.

## Cold-start and hard boundaries

Cold-start PROMPT:
NOT_CREATED / BLOCKED_BY_RECOVERY_INTEGRITY_FAILURE

KOO r1.4 Initiation Gate:
NOT_EXECUTED

KOO r1.4 Writer Gate:
NOT_EXECUTED

KOO r1.4 current-writer:
NOT_ESTABLISHED

Prepared SHD task:
PREPARED_NOT_ACTIVATED / NOT_ACTIVATED

SHD R02 rereview:
NOT_AUTHORIZED / NOT_PERFORMED

G4/G5/G6:
NOT_CREATED

Historical PROMPT/task/queue replay:
NONE

KOO authoritative current-state mutation:
NONE

Project Source/canon mutation:
NONE

Deployment/provider/API/Telegram/live effect:
NONE

Hidden/unwritten KOO state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Required next reconciliation

KOO must fresh-reconcile this exact ARH r14 attempt and failure evidence. Do not treat the published r14 directory as a valid recovery basis, do not activate any cold-start prompt, and do not infer Initiation Gate or Writer Gate authority.

The next step that could create a corrected immutable recovery successor requires a separate exact task/authority and a new non-colliding version locator. This ARH attempt does not authorize that work.

STOP.
