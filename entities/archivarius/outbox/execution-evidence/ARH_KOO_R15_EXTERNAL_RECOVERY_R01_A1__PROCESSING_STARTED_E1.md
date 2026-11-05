# ARH KOO recovery r15 — PROCESSING_STARTED

attempt:
ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1

status:
PROCESSING_STARTED

scope:
IMMUTABLE_EXTERNAL_RECOVERY_SUCCESSOR_PRESERVATION_INTEGRITY_READBACK_REGISTRY_AND_COLD_START_PROMPT_PREPARATION_ONLY

project_time:
omitted

## Exact task authority

authority:
puev5691/wellbeing-hq@60c4f26bcffa6b20f90f8e2439477131e91c950d:entities/archivarius/outbox/ARH__KOO-r15-external-recovery-authority__OPERATOR.md

authority_blob:
0f6a051098bb5af85571277892cbf3f8924766bb

authority_status:
OPERATOR_TASK_AUTHORITY_RECORDED

OPERATOR authority:
- prior explicit emergency instruction: `Разрешаю любые действия, которые позволят восстановить работу чата КООРДИНАТОРа.`
- current instruction: `Writer Gate нового ARH утверждаю. Продолжай процедуру.`

## Fresh preflight

HQ main HEAD:
60c4f26bcffa6b20f90f8e2439477131e91c950d

Bootstrap main HEAD:
f89bc6a414038fb741b968b620189c35cbd39006

ARH current-writer r0.4:
blob 57fed46548bda0eb78d87387e209cf91c5233aaf
status WRITER_ESTABLISHED
PASS

KOO current-writer r1.3:
blob 5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1
status WRITER_ESTABLISHED
PASS

KOO r1.3 self-snapshot:
blob 8a39b17be502cfa4f356e69fb6f6374fdc2b5029
terminal PASS_KOO_R13_SELF_SNAPSHOT_R14_READY_FOR_ARH_PRESERVATION
PASS

Project Source set:
R07 / PASS
activation blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Current control state:
- old global pause RELEASED;
- SECE priority ACTIVE_COORDINATION_DECISION;
- PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE=YES;
- historical replay FORBIDDEN.

Failed KOO r14 recovery:
bootstrap ref f89bc6a414038fb741b968b620189c35cbd39006
package tree 408111bf55bde1fe036bdf7519b969a34b83af71
ARH registry blob 60837400e0dda55566cfc730a8a1f30f8bce8571
terminal FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH
r14 immutable / not to be modified.

Human Interface Contract source blob:
fdea31034c370220dfb961993059500716ccfe20
Independent SHA-256 recomputation:
b8f9cfa56636127ed013bda7a67c2b0bb77f75099ac081c13f5b06f8a2aa0175
r14 SHA256SUMS expected:
34e365fb9675dccc6deaa5f48095cd65975f723f1ac798ea6bd5271f193df2ce
Mismatch confirmed.

Target r15 path:
entities/koo/recovery/versions/koo-recovery-r15
pre-write path absence:
PASS

Competing r15 recovery publication/result/registry:
NOT_FOUND / PASS

KOO r1.4 initiation result:
NOT_FOUND / PASS

KOO r1.4 current-writer:
NOT_FOUND / PASS

## Exact source inputs

KOO self-snapshot:
HQ commit 5795ac734b4f6af1b948911c6da7f907d9a0427b
blob 8a39b17be502cfa4f356e69fb6f6374fdc2b5029

KOO current-writer:
HQ commit 210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd
blob 5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

Human Interface Contract:
bootstrap r13 commit 896b33f99551092bf50f7bef2657e3276d850fc3
blob fdea31034c370220dfb961993059500716ccfe20

Previous verified KOO recovery r13:
bootstrap commit 896b33f99551092bf50f7bef2657e3276d850fc3
tree 1aecd76c7cabe55d047eea6ea79700fed643d98d
classification LAST_EXTERNALLY_VERIFIED_KOO_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOO_R13_WORK

## Start boundary

All required authority, writer, source, target absence and no-conflict preconditions for this exact ARH r15 recovery attempt were checked.

This artifact proves processing started for this attempt only.

No external r15 package has yet been published.
No KOO authoritative current-state has been mutated.
No Project Source/canon has been mutated.
No KOO r1.4 Initiation Gate or Writer Gate has been executed.
No SHD task has been activated.
No historical task/PROMPT/queue has been replayed.
No production/provider/API/Telegram/live effect has been performed.

terminal:
PROCESSING_STARTED_ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1
