# ARH KOO external recovery r15 authority record

status:
OPERATOR_TASK_AUTHORITY_RECORDED

recipient:
ARH / АРХИВАРИУС current-writer r0.4

attempt:
ARH_KOO_R15_EXTERNAL_RECOVERY_R01_A1

scope:
IMMUTABLE_EXTERNAL_RECOVERY_SUCCESSOR_PRESERVATION_INTEGRITY_READBACK_REGISTRY_AND_COLD_START_PROMPT_PREPARATION_ONLY

project_time:
omitted

## OPERATOR authority

Prior explicit emergency recovery authorization:
`Разрешаю любые действия, которые позволят восстановить работу чата КООРДИНАТОРа.`

Current OPERATOR instruction after replacement ARH Writer Gate:
`Writer Gate нового ARH утверждаю. Продолжай процедуру.`

This task is bounded to continuing the KOO chat recovery procedure after the ARH replacement Writer Gate. It does not expand into KOO current-state mutation or profile/production execution.

## Exact current ARH writer

`puev5691/wellbeing-hq@5ba2c74ae00cf8414925341084f8a3bb352f5628:entities/archivarius/current/ARH__replacement-current-writer-r04.md`

blob:
`57fed46548bda0eb78d87387e209cf91c5233aaf`

status:
`WRITER_ESTABLISHED`

## Recovery context

Failed immutable predecessor publication:
`puev5691/wellbeing-entity-bootstrap@f89bc6a414038fb741b968b620189c35cbd39006:entities/koo/recovery/versions/koo-recovery-r14`

tree:
`408111bf55bde1fe036bdf7519b969a34b83af71`

ARH registry:
`puev5691/wellbeing-hq@1172fff6b8290f26d128a2d85580f1ac7cfde957:entities/archivarius/current/recovery-registry/ARH__KOO-recovery-r14.md`

registry blob:
`60837400e0dda55566cfc730a8a1f30f8bce8571`

terminal:
`FAIL_ARH_KOO_R14_EXTERNAL_RECOVERY_SHA256_MISMATCH`

r14 is immutable and remains failed. Do NOT modify or overwrite r14.

## Exact KOO-authored inputs

KOO self-snapshot:
`puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md`

blob:
`8a39b17be502cfa4f356e69fb6f6374fdc2b5029`

KOO current-writer:
`puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:entities/koordinator/current/KOO__replacement-current-writer-r13.md`

blob:
`5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1`

Human Interface Contract:
`puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13/KOO__human-interface-contract-r02.md`

blob:
`fdea31034c370220dfb961993059500716ccfe20`

## Exact bounded task

Create one NEW immutable external recovery successor at:
`entities/koo/recovery/versions/koo-recovery-r15`

- Preserve exact bytes of the three KOO-authored/source files above.
- Reconcile/update only ARH-owned recovery metadata for the r15 locator and preserved verified state.
- Independently recompute SHA-256 for every non-checksum file after final bytes.
- Verify exact package composition, source Git blob equality, manifest/tree identity, immutable external readback and registry.
- Do not rewrite/delete r13 or r14.
- After r15 PASS, prepare one complete cold-start PROMPT for a genuinely NEW KOO r1.4 instance, Initiation Gate only.

## Explicit exclusions

This task does NOT authorize:
- KOO r1.4 Initiation Gate execution in this ARH chat;
- KOO r1.4 Writer Gate;
- KOO authoritative current-state mutation;
- activation/replay of prepared SHD task;
- SHD R02 rereview;
- G4/G5/G6 authority or execution;
- KOD/SIS/profile continuation;
- Project Source/canon mutation;
- production, deployment, provider, API, Telegram or live effects;
- historical task/PROMPT/queue replay.

## Success condition

Only classify r15 as:
`EXTERNALLY_PRESERVED_READBACK_PASS`
if independent checks and immutable readback pass completely.

If a conflict, missing authority, supersession or integrity failure appears, stop and record the exact blocker.
