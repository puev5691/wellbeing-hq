# ARH -> KOO / OPERATOR: KOO external recovery r15 and cold-start preparation result

status:
PASS_ARH_KOO_R15_EXTERNAL_RECOVERY_AND_COLD_START_PREPARED

terminal:
PASS_ARH_KOO_R15_EXTERNAL_RECOVERY_AND_COLD_START_PREPARED

attempt:
ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1

scope:
IMMUTABLE_EXTERNAL_RECOVERY_SUCCESSOR_PRESERVATION_INTEGRITY_READBACK_REGISTRY_AND_COLD_START_PROMPT_PREPARATION_ONLY

project_time:
omitted

## Human result

Writer Gate для нового ARH r0.4 установлен и подтверждён readback. После него ARH выполнил ограниченное восстановление внешнего KOO recovery.

KOO recovery r14 оказался не просто с одной ошибкой: при полной повторной проверке все 8 его SHA256SUMS entries не совпали с точными байтами файлов. r14 оставлен неизменным.

Создан новый immutable recovery successor r15. В нём сохранены без изменения exact KOO r1.3 self-snapshot и current-writer; ARH metadata оформлены для r15; SHA-256 заново вычислены по окончательным байтам. Внешний readback прошёл: 9/9 files, 8/8 checksums, 3/3 copied source Git blob identities.

Подготовлен один полный cold-start PROMPT для действительно нового KOO r1.4 chat. Initiation Gate KOO в этом чате ARH не выполнялся.

## Exact authority and execution evidence

OPERATOR task authority:
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

Writer Gate result:
puev5691/wellbeing-hq@7ba677196ac8ed83b65df5d9f2be095cfb00cafd:entities/archivarius/outbox/ARH__emergency-replacement-writer-gate-r05-result__OPERATOR.md

## Exact KOO sources

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

## Failed r14

r14 publication:
puev5691/wellbeing-entity-bootstrap@f89bc6a414038fb741b968b620189c35cbd39006:entities/koo/recovery/versions/koo-recovery-r14

tree:
408111bf55bde1fe036bdf7519b969a34b83af71

terminal:
FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH

Fresh full verification:
8/8 SHA256SUMS entries mismatch exact file bytes.

r14 remains immutable and is NOT a verified recovery basis.

## New external recovery r15

Repository:
puev5691/wellbeing-entity-bootstrap

publication commit:
07f02668d0fab6ceaaa8e1e774914dca753d93ad

exact locator:
puev5691/wellbeing-entity-bootstrap@07f02668d0fab6ceaaa8e1e774914dca753d93ad:entities/koo/recovery/versions/koo-recovery-r15

package tree:
29fd5a13b48e5bcc309d7db02d1ed24fbea43cf4

root tree:
6aefa60fb5c8942a6d516d84cc3f7bdbd7c6ceba

composition:
9/9 PASS

SHA256SUMS:
8/8 PASS

copied KOO source Git blob equality:
3/3 PASS

copied ARH recovery metadata source blob equality (SOURCES/TASK-STATE):
2/2 PASS

immutable readback:
9/9 PASS

manifest/tree correspondence:
PASS

missing/extra files:
NONE

classification:
CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOO_R13_PLANNED_CHAT_REPLACEMENT_R14

## ARH recovery registry

puev5691/wellbeing-hq@bbe6c409689bbfa10e941e7d4de7a10995dc3912:entities/archivarius/current/recovery-registry/ARH__KOO-recovery-r15.md

registry_blob:
e1d10988eb9f023d1fdce3c1cc40ba814ec8b104

immutable readback:
PASS

## Cold-start PROMPT for NEW KOO r1.4

puev5691/wellbeing-hq@ee749c02bb217aac8403eb14abbb29105b4cb1c6:entities/archivarius/outbox/PROMPT__KOO__replacement-r15-cold-start__OPERATOR.md

prompt_blob:
4d04a526bad985bd5246e10fe23f46b03616d23b

immutable readback:
PASS

scope:
INITIATION_GATE_ONLY

## Fresh HQ boundary after prompt preparation

HQ main preflight:
ee749c02bb217aac8403eb14abbb29105b4cb1c6

KOO current-writer r1.3:
UNCHANGED / WRITER_ESTABLISHED

Active Project Sources:
R07 / PASS

KOO r1.4 initiation result:
NOT_FOUND

KOO r1.4 current-writer:
NOT_FOUND

No KOO Initiation Gate or Writer Gate was executed by ARH.

## Current boundaries preserved

- Old global profile-task pause: RELEASED.
- SECE primary priority: ACTIVE_COORDINATION_DECISION.
- PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE=YES.
- KOD recovery v09 remains current external basis for KOD v07 after R02.
- KOD R02 candidate: NOT_ACTIVATED.
- Real sandbox effect: NOT_EXECUTED.
- R02 combined runtime PASS: NOT_INFERRED.
- SHD writer r04 remains authoritative.
- SHD recovery r05 remains stale relative to later SHD R01 review.
- Prepared SHD preservation task remains PREPARED_NOT_ACTIVATED / start_proven=NO.
- SHD R02 rereview NOT_AUTHORIZED / NOT_PERFORMED.
- G4/G5/G6 NOT_CREATED.
- SHD frontier discrepancy remains unresolved; no repair or replay.
- KOO current-state mutation: NONE.
- Historical PROMPT/task/queue replay: NONE.
- Project Source/canon mutation: NONE.
- Production/provider/API/Telegram/live effect: NONE.
- Hidden/unwritten KOO state: UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

## Terminal

`PASS_ARH_KOO_R15_EXTERNAL_RECOVERY_AND_COLD_START_PREPARED`

Next allowed action:
OPERATOR manually opens a genuinely NEW KOO r1.4 chat and pastes the exact cold-start PROMPT. That new instance performs Initiation Gate only, then stops and returns its result. Writer Gate remains a separate OPERATOR decision.

STOP.
