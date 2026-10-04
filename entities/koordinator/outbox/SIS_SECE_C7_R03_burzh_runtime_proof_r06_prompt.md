# SIS task — SECE C7 R03 burzh runtime proof R06

conveyor_attempt:
SIS_SECE_C7_R03_BURZH_EXEC_R06_A1

attempt_state:
AWAITING_OPERATOR_TRANSFER

project_time:
omitted

АДРЕСАТ: СИСАДМИН / SIS r0.9

Resume-First.

Выполни только exact independent runtime proof, заданный следующими immutable artifacts.

Authority:

puev5691/wellbeing-hq@d41057922d26d191a8403b4ec43a84213342b618:
entities/koordinator/outbox/KOO__authorize-SIS-SECE-C7-R03-burzh-R06__OPERATOR.md

blob:
b4b88fa8b2bd007e2002d2dbdfbae964746e3c5b

Runtime-proof specification:

puev5691/wellbeing-hq@8e74fad2c374207f50d9f4c0c44261a52b3af9e2:
entities/koordinator/outbox/KOO__SECE-C7-R03-burzh-runtime-proof-decision__OPERATOR.md

blob:
a8ff705955b40a76bbd3bee6dac8fc0aa9ccfc77

Current writer:

puev5691/wellbeing-hq@1de10d5d61430fae49f8e27bccbd655c3ed2c972:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r09.md

blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

Before first host/network action create/read back PROCESSING_STARTED for:

SIS_SECE_C7_R03_BURZH_EXEC_R06_A1

Execute only the proof defined by the authority/specification above.

Required terminal result:

entities/sisadmin/outbox/SIS__SECE-r01-C7-R03-burzh-runtime-proof-r06__KOO.md

Allowed terminal:
PASS_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06
or
BLOCKED_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06
or
FAIL_SIS_SECE_R01_C7_R03_BURZH_RUNTIME_PROOF_R06

After immutable publication/readback return KOO exact locator + commit + blob and STOP.

No activation or automatic SHD rereview.
