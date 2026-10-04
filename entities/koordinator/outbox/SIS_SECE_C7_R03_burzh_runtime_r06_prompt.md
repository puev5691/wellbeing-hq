# SIS task — SECE C7 R03 burzh runtime proof R06

conveyor_attempt:
SIS_SECE_C7_R03_BURZH_EXEC_R06_A1

attempt_state:
AWAITING_OPERATOR_TRANSFER

project_time:
omitted

АДРЕСАТ: СИСАДМИН / SIS r0.9

Resume-First.

Выполни только one NEW independent runtime-proof attempt of the exact R03 candidate on burzh.

Authority:

puev5691/wellbeing-hq@d41057922d26d191a8403b4ec43a84213342b618:
entities/koordinator/outbox/KOO__authorize-SIS-SECE-C7-R03-burzh-R06__OPERATOR.md

blob:
b4b88fa8b2bd007e2002d2dbdfbae964746e3c5b

Current SIS writer:

puev5691/wellbeing-hq@1de10d5d61430fae49f8e27bccbd655c3ed2c972:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r09.md

blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

Exact candidate/package specification:

puev5691/wellbeing-hq@be00203248d134cf47415aa834386e87d774fa2a:
entities/koder/outbox/KOD__SECE-r01-D1D2-C7-grounding-regression-r03__KOO.md

blob:
8b0f27c826613c4adc6db2736666591d82d3b8ab

Exact candidate:
puev5691/wellbeing-hq@51b3654b1f5b802009b0e61d6c52df841420d306:
entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-c7-r03/

tree:
4080fb9195fac4ebdfcb144fe3bdab83323485b4

target:
burzh / ruvds-xnqc6

device_id:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

workspace:
/tmp/wellbeing-sece-c7-r03-r06-a1

Use the prior successful R05 burzh execution procedure only for the execution flow on burzh, not as task authority, replay, or package-integrity source:

puev5691/wellbeing-hq@743e035c95901e39752de74c4cf9fc8a72bc5adb:
entities/koordinator/outbox/SIS_SECE_D1D2_burzh_exec_r05_prompt.md

blob:
c08ca216c0eb67253927520d1b6c1e4708a095d3

For R06:
- use the exact R06 attempt/workspace above;
- acquire only the exact R03 candidate commit/tree above;
- derive and verify all package member/blob/hash identities from the exact R03 package and its own SHA256SUMS/KOD result;
- do NOT reuse predecessor R05 package hashes or predecessor package identity.

Before first host/network action create/read back PROCESSING_STARTED for this exact attempt.

Required PASS and boundaries are defined by the exact authority and KOD result above.

Required result:

entities/sisadmin/outbox/SIS__SECE-r01-C7-R03-burzh-runtime-proof-r06__KOO.md

Allowed terminal:
PASS_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06
or
BLOCKED_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06
or
FAIL_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06

After immutable publication/readback return KOO exact locator + commit + blob and STOP.

No activation. No automatic SHD rereview.
