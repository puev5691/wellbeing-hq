# SIS — SECE D1+D2 alternative-host execution proof R05

conveyor_attempt:
SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1

attempt_state:
AWAITING_OPERATOR_TRANSFER

execution_evidence_profile:
CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01

project_time:
omitted

АДРЕСАТ: СИСАДМИН / SIS r0.9

Resume-First.

Выполни только one NEW bounded R05 execution-proof attempt on burzh.

## Exact authority

puev5691/wellbeing-hq@9ae4cd2d597dc723efc7c77f5820fa5a4900f05c:
entities/koordinator/outbox/KOO__authorize-SIS-SECE-D1D2-burzh-R05__OPERATOR.md

blob:
257e9a0f56063b31aba8c9ba0f69e48a71bae03b

decision:
AUTHORIZE_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05 = YES

This authority artifact is the single source for scope, preflight and boundaries.

## Current SIS writer

puev5691/wellbeing-hq@1de10d5d61430fae49f8e27bccbd655c3ed2c972:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r09.md

blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

status:
CURRENT_WRITER_ESTABLISHED

## Exact target

target:
burzh / ruvds-xnqc6

device_id:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

workspace:
/tmp/wellbeing-sece-d1d2-publicfetch-r05-a1

Fresh KOO standing-transport observation before materialization:
inventory = ONLINE
ping = PASS

## Exact technical procedure source

Use only as immutable technical specification, NOT as task authority and NOT as replay:

puev5691/wellbeing-hq@813f8c0f15ad6522ee70bb99ec2436a3de56ec38:
entities/koordinator/outbox/SIS_SECE_D1D2_publicfetch_exec_r04_prompt.md

blob:
33dbb14846e10a1b23197b190326f95d5b4c2f7d

Reuse from that specification only:
- exact immutable candidate/source/commit/package/tree identities;
- exact package integrity checks;
- exact three Python workloads;
- exact runtime-gate matrix;
- evidence/result requirements.

R05-specific substitutions:
- attempt = SIS_SECE_D1D2_BURZH_PUBLICFETCH_R05_A1;
- target/device = exact burzh values above;
- workspace = exact R05 workspace above;
- existing burzh project repo must not be modified;
- R03/R04/p552203 are predecessor evidence only and must not be accessed, resumed, replayed or cleaned.

## Execution

1. Fresh-check exact authority, writer, target/currentness and supersession.
2. Before first host/network action create and read back PROCESSING_STARTED for the exact R05 attempt.
3. Perform every authority-required fresh preflight check.
4. If preflight passes, execute the exact technical procedure identified above inside the new R05 workspace only.
5. Publish and read back the required immutable R05 result.
6. Return KOO exact locator + commit + blob.
7. STOP.

## Required result

Create:

entities/sisadmin/outbox/SIS__SECE-r01-D1D2-burzh-publicfetch-exec-r05__KOO.md

Allowed terminal:
PASS_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05
or
BLOCKED_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05
or
FAIL_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05

No automatic SHD rereview.
