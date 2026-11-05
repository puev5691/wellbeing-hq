# ARH KOO external recovery r15 registry

status:
EXTERNALLY_PRESERVED_READBACK_PASS

terminal:
PASS_ARH_KOO_R15_EXTERNAL_RECOVERY_AND_COLD_START_PREPARED

attempt:
ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1

scope:
IMMUTABLE_EXTERNAL_RECOVERY_SUCCESSOR_PRESERVATION_INTEGRITY_READBACK_REGISTRY_AND_COLD_START_PROMPT_PREPARATION_ONLY

project_time:
omitted

## Human result

The exact KOO r1.3 self-snapshot and current-writer were preserved byte-for-byte. A new immutable external recovery successor r15 was published. The full package was independently read back and verified: exact 9/9 composition, all 8 SHA-256 entries correct, and copied source Git blobs equal their exact source identities.

The failed r14 package remains immutable. It is not used as a recovery basis.

## Exact authority and execution evidence

OPERATOR authority record:
puev5691/wellbeing-hq@60c4f26bcffa6b20f90f8e2439477131e91c950d:entities/archivarius/outbox/ARH__KOO-r15-external-recovery-authority__OPERATOR.md

authority_blob:
0f6a051098bb5af85571277892cbf3f8924766bb

PROCESSING_STARTED:
puev5691/wellbeing-hq@d148ee3084307f2a6145429c6792557cd96583ad:entities/archivarius/outbox/execution-evidence/ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

PROCESSING_STARTED_blob:
fba94df192fbde9897bb468a4d0c850a1a20660b

ARH current-writer:
puev5691/wellbeing-hq@5ba2c74ae00cf8414925341084f8a3bb352f5628:entities/archivarius/current/ARH__replacement-current-writer-r04.md

ARH_writer_blob:
57fed46548bda0eb78d87387e209cf91c5233aaf

status:
WRITER_ESTABLISHED

## Exact KOO source state

KOO current-writer r1.3:
puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:entities/koordinator/current/KOO__replacement-current-writer-r13.md

blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

status:
WRITER_ESTABLISHED

KOO self-snapshot:
puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md

blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

terminal:
PASS_KOO_R13_SELF_SNAPSHOT_R14_READY_FOR_ARH_PRESERVATION

Human Interface Contract:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13/KOO__human-interface-contract-r02.md

source/package Git blob:
fdea31034c370220dfb961993059500716ccfe20

## Failed intermediate r14

External publication:
puev5691/wellbeing-entity-bootstrap@f89bc6a414038fb741b968b620189c35cbd39006:entities/koo/recovery/versions/koo-recovery-r14

tree:
408111bf55bde1fe036bdf7519b969a34b83af71

ARH result:
puev5691/wellbeing-hq@68adc5cd8d9b98cdb7b028c6a25ca3b7a7a4a12c:entities/archivarius/outbox/ARH__KOO-r14-external-recovery__KOO-OPERATOR.md

blob:
85b1b19e0e6db7698c8e0f2c0084a1dbfa3c7657

terminal:
FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH

Fresh full checksum reconciliation of exact r14 package:
8/8 r14 SHA256SUMS entries mismatched.

| File | r14 claimed SHA-256 | exact package recomputation |
|---|---|---|
| KOO__human-interface-contract-r02.md | 34e365fb9675dccc6deaa5f48095cd65975f723f1ac798ea6bd5271f193df2ce | b8f9cfa56636127ed013bda7a67c2b0bb77f75099ac081c13f5b06f8a2aa0175 |
| KOO__planned-chat-replacement-self-snapshot-r14.md | 0f82792f73a2d149937a90875ed6e7e32ff6c5bb5f0df9e415d039f464cf35f7 | 64cc214effe0bc23cab9e60a20a251b89b441d3285d565659970ad0add840ef7 |
| KOO__recovery-initiation-boundary-r14.md | ee58c42b36847c600c76bd087c8b3253e2d962f17191c751d96fce83b2505489 | 11190ac1af2dd2c2197ff22972fe7ae747d29e6e685334cc906d77683d330c11 |
| KOO__replacement-current-writer-r13.md | cccc80f85f76ca1fcebd54fe9cef9fae1f404ac3802e59a4f5712f5ce5517749 | 5353ce3b90cbbe68ea34d715467965651d80dc9cea582265e292b5dd43754deb |
| RECOVERY-LINEAGE.md | 718e0e55965cd9b2a7ce54db2c54dcaf631f8c3f99989d60f6ea8aa803f68688 | 5a992566f002c4b2a1747d8fe19898b1aaa904f01444ab7bf9acfa8ef3543700 |
| RECOVERY-MANIFEST.md | bd606c9c7bf1958ebcab5082c2c25655f92d4259b9819ad2e572aa6cea72a6e1 | 07489861b1b8e97225f636ff7a63c3bf8deff6ff0480cfc05c4262fd2acf2ce3 |
| SOURCES.md | 615429abaee012a3acf246ac946b99ac54134c62e1a1fea6a4543db46045a05f | 0aee0c78556965be5ab84b5641cc9213f84e2c9d4701266988b3a5715df5dc43 |
| TASK-STATE.md | c7f4487c206d1316b22fbaaeb611ad0cbd7040286ca5b9bc491587ff1830b504 | 322bf49bbd1974ff44cd77763a7fa0f367e07fef4109462528a61c5f38d823a8 |

The mismatch is in the checksum inventory, not in the exact copied source Git blob identities. r14 is immutable and failed.

## New immutable external recovery r15

Repository:
puev5691/wellbeing-entity-bootstrap

Publication commit:
07f02668d0fab6ceaaa8e1e774914dca753d93ad

Locator:
puev5691/wellbeing-entity-bootstrap@07f02668d0fab6ceaaa8e1e774914dca753d93ad:entities/koo/recovery/versions/koo-recovery-r15

target_path:
entities/koo/recovery/versions/koo-recovery-r15

package_tree:
29fd5a13b48e5bcc309d7db02d1ed24fbea43cf4

root_tree:
6aefa60fb5c8942a6d516d84cc3f7bdbd7c6ceba

composition:
9/9 PASS

Exact composition:
- KOO__planned-chat-replacement-self-snapshot-r14.md
- KOO__replacement-current-writer-r13.md
- KOO__human-interface-contract-r02.md
- SOURCES.md
- TASK-STATE.md
- KOO__recovery-initiation-boundary-r15.md
- RECOVERY-LINEAGE.md
- RECOVERY-MANIFEST.md
- SHA256SUMS.txt

Copied source Git blob equality:
3/3 PASS

ARH metadata source blob equality for copied SOURCES/TASK-STATE:
2/2 PASS

Independent SHA256SUMS:
8/8 PASS

Immutable readback:
9/9 PASS

Manifest/tree correspondence:
PASS

Missing/extra files:
NONE

SHA-256 computation validation:
standard SHA-256 test vector `abc` PASS; independent recomputation performed over final readback content.

## Current approved Project Sources and control state

Source-set:
R07

Activation:
puev5691/wellbeing-hq@d148ee3084307f2a6145429c6792557cd96583ad:entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

activation_blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Approved active source identities:
- Project Core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911
- File Work Canon v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Source Loading Policy v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609
- Task Conveyor Canon v1.2: df7896d867eeeffff506319538fedad938856686

Task Conveyor v1.3:
NOT_ACTIVE

Old global profile-task pause:
RELEASED

SECE primary priority:
ACTIVE_COORDINATION_DECISION

PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE:
YES

KOD recovery v09:
CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPLEMENTATION_CORRECTION_R02

KOD R02 candidate:
NOT_ACTIVATED

Real sandbox effect:
NOT_EXECUTED

R02 combined runtime PASS:
NOT_INFERRED

SHD current writer:
r04 / AUTHORITATIVE_CURRENT_WRITER

SHD recovery:
r05 / STALE_RELATIVE_TO_LATER_SHD_R01_IMPLEMENTATION_REVIEW

Prepared SHD preservation task:
PREPARED_NOT_ACTIVATED

SHD start_proven:
NO

SHD R02 rereview:
NOT_AUTHORIZED / NOT_PERFORMED

G4/G5/G6:
NOT_CREATED

Known SHD frontier discrepancy:
task blob cites b16894c2119bbac96f8a49e607ad25b28d950fc0; KOO snapshot/current HQ frontier identifies 81082bc94bf8db76196139626291409bef853f7c. Preserve unresolved; do not repair/replay.

## KOO replacement boundaries

KOO r1.4 Initiation Gate:
NOT_EXECUTED_BY_ARH

KOO r1.4 Writer Gate:
NOT_EXECUTED

KOO r1.4 current-writer:
NOT_ESTABLISHED

Cold-start PROMPT:
prepared after r15 PASS; exact locator recorded in ARH result

KOO authoritative current-state mutation:
NONE

Historical PROMPT/task/queue replay:
NONE

Project Source/canon mutation:
NONE

Production/provider/API/Telegram/live effect:
NONE

Hidden/unwritten KOO state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Classification

r15 is:
`CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOO_R13_PLANNED_CHAT_REPLACEMENT_R14`

This establishes verified external recovery for a genuinely NEW KOO r1.4 Initiation Gate only. It does not establish KOO r1.4 current-writer or authorize profile work.

STOP.
