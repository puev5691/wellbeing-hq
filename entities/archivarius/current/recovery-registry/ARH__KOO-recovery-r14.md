# ARH recovery registry — KOO recovery r1.4

status:
EXTERNAL_RECOVERY_PUBLICATION_READBACK_FAIL

attempt:
ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_READBACK_AND_COLD_START_PREPARATION_ONLY

authority:
puev5691/wellbeing-hq@2729c7ad066ad1ba5dc7dc802db2c96fc995a3dc:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_authority.md

authority_blob:
3a92721b8a12ebe3d20632d610130ecccca5cb14

registry_input_blob:
003e2ea1e282de130961d241031bf4eb760a0987

accepted_frontier:
puev5691/wellbeing-hq@026ac6db4b3eec5d2c1263e195147c981a9ed8e6:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_frontier.md

frontier_blob:
3bab160572ffef647c902eff1dddfabf1858fbbd

PROCESSING_STARTED:
puev5691/wellbeing-hq@3dac10bfde28298874a91bf027efbd12fb5b85ce:entities/archivarius/outbox/execution-evidence/ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

PROCESSING_STARTED_blob:
874cefeca16ae64cf6ce5073381f720c9b7ef025

## Exact source identities

KOO self-snapshot:
puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md

blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

KOO current-writer:
puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:entities/koordinator/current/KOO__replacement-current-writer-r13.md

blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

ARH current-writer:
entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

Human Interface Contract source:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13/KOO__human-interface-contract-r02.md

blob:
fdea31034c370220dfb961993059500716ccfe20

## Predecessor and published successor

Predecessor r13:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13

tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

predecessor disposition:
LAST_EXTERNALLY_VERIFIED_KOO_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOO_R13_WORK

New r14 publication:
puev5691/wellbeing-entity-bootstrap@f89bc6a414038fb741b968b620189c35cbd39006:entities/koo/recovery/versions/koo-recovery-r14

package_tree:
408111bf55bde1fe036bdf7519b969a34b83af71

## Publication/readback

External main ref:
f89bc6a414038fb741b968b620189c35cbd39006

Path-to-tree:
PASS

Composition:
9/9 PASS

Exact copied source Git blob equality:
3/3 PASS

Manifest-to-tree correspondence:
PASS

Missing/extra files:
NONE

Independent immutable readback:
PATH/TREE/COMPOSITION PASS

SHA256SUMS claimed coverage:
8/8

Independent SHA-256 recomputation:
FAIL / STOPPED AT FIRST MISMATCH

Exact mismatch:
file:
KOO__human-interface-contract-r02.md

package/source Git blob:
fdea31034c370220dfb961993059500716ccfe20

SHA256SUMS expected:
34e365fb9675dccc6deaa5f48095cd65975f723f1ac798ea6bd5271f193df2ce

independently recomputed SHA-256:
b8f9cfa56636127ed013bda7a67c2b0bb77f75099ac081c13f5b06f8a2aa0175

independent byte length:
4015

Remaining checksum entries:
NOT_RECOMPUTED_AFTER_FAIL-FAST

Recoverability classification:
BLOCKED_SHA256SUMS_MISMATCH

r14 classification:
NOT_A_VERIFIED_CURRENT_EXTERNAL_RECOVERY_BASIS

r13 remains the last externally verified KOO recovery basis.

## Cold-start and replacement boundaries

Cold-start PROMPT:
NOT_CREATED / BLOCKED_BY_RECOVERY_INTEGRITY_FAILURE

KOO r1.4 Initiation Gate:
NOT_EXECUTED

KOO r1.4 Writer Gate:
NOT_EXECUTED

KOO r1.4 current-writer:
NOT_ESTABLISHED

Prepared SHD task:
NOT_ACTIVATED

Historical replay:
NONE

KOO authoritative current-state mutation:
NONE

Project Source/canon mutation:
NONE

No deployment/provider/API/Telegram/live effect.

terminal:
FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH
