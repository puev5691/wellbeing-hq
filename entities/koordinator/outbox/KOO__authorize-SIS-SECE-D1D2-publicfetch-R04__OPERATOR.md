# KOO record — OPERATOR authority for SIS SECE D1+D2 public-fetch R04

status:
OPERATOR_TASK_AUTHORITY_RECORDED

project_time:
omitted

Exact OPERATOR decision in current KOO r1.2 chat:

AUTHORIZE_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R04 = YES

## Scope

Authorized:
one NEW bounded SIS r0.9 execution-proof attempt only.

attempt:
SIS_SECE_D1D2_PUBLICFETCH_R04_A1

target:
p552203.kvmvps

device_id:
830038a0-232b-4d83-b52d-0e9973126165

workspace:
/data/wellbeing-lab/tmp/sece-d1d2-publicfetch-r04-a1

public_source:
https://github.com/puev5691/wellbeing-hq.git

exact_candidate_commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

exact_package_path:
entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-r02/

exact_package_tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

Purpose:
fresh exact-byte materialization and exact offline Python execution proof of the immutable D1+D2 candidate.

Required before first host/network action:
fresh durable PROCESSING_STARTED evidence for exact R04 attempt.

## Predecessor R03 boundary

R03:
SIS_SECE_D1D2_PUBLICFETCH_R03_A1

disposition:
NONTERMINAL / DO_NOT_REPLAY

R03 authority:
CONSUMED_BY_R03_ONLY

R03 workspace reuse:
FORBIDDEN

R03 cleanup by R04:
NOT_AUTHORIZED

## Boundaries

Authorized effects:
- fresh read-only target/currentness checks;
- create only the fixed R04 disposable workspace;
- anonymous public Git exact-object acquisition only from the exact source;
- exact package materialization and integrity verification;
- exact offline Python workload;
- immutable execution evidence;
- safe cleanup only of the R04 workspace if ownership/safety is proven.

Not authorized:
- R03 resume/replay/cleanup;
- reuse of R03 workspace;
- modification of existing project repo/worktree/object database;
- full-clone fallback or branch/main synchronization;
- authenticated Git or credential access;
- candidate modification;
- package installation;
- simulator activation/use/deploy;
- production service/storage mutation;
- provider/model/API/Telegram calls;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- automatic SHD rereview.
