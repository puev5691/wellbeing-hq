# KOO → SIS: P552203 /run/wb-shard-gateway read-only inspection/classification r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.7
scope: ROOT_LEVEL_READ_ONLY_RUNTIME_DIR_INSPECTION_CLASSIFICATION_ONLY
project_time: omitted

Resume-First.

## Current KOO writer

puev5691/wellbeing-hq@9c5e330719fa4410eca76e91a128bfcc29d56c45:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

## Intended SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

SIS must fresh-verify writer continuity, supersession and exact authority/task before inspection.

## Exact authority

puev5691/wellbeing-hq@c9715f53774c1761879db49801c64b1c246d3cea:
entities/koordinator/outbox/KOO__authorize-P552203-run-wb-shard-gateway-read-only-inspection-r01__OPERATOR.md

blob:
2c120b95f8d8d4c0189a084fb06ace4da54eb2f7

decision:
AUTHORIZE_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_INSPECTION_CLASSIFICATION_R01

## Exact blocker basis

puev5691/wellbeing-hq@4cdbf38d484609737d057b6d0ae5e2cf9191e8c7:
entities/sisadmin/outbox/SIS__P552203-gateway-retirement-r01-operator-assisted-blocker__KOO.md

blob:
1fc910f18df94ba0451b9f8759b1c955622829f4

terminal:
BLOCKED_SIS_P552203_GATEWAY_RETIREMENT_R01_RUNTIME_DIR_NONEMPTY

Verified:
- host p552203.kvmvps;
- service inactive/dead;
- unit disabled;
- mutation NONE;
- /run/wb-shard-gateway non-empty.

## Task

Perform only bounded root-level read-only inspection/classification of:

/run/wb-shard-gateway

Goal:
establish what currently occupies the directory, what evidence supports who/what created or uses it, whether any object is active/in-use, and whether a separate later retirement decision is supportable.

Fresh-check before inspection:
- current SIS writer and task/authority identities;
- exact host identity;
- no superseding task/result/authority;
- no mutation occurred after blocker that invalidates the basis.

Collect only necessary read-only evidence, including as applicable:
- exact directory entries;
- file type;
- size;
- owner/group;
- mode;
- inode/link metadata where useful;
- filesystem timestamps only as metadata, never sole event truth;
- process/open-file/socket references;
- systemd/process relationship;
- safe file-content inspection only if necessary and non-secret.

If content may contain secrets, tokens, credentials or sensitive payloads:
do not return raw values; classify safely and stop if safe inspection cannot establish the needed fact.

For each relevant entry classify only from evidence as one of:
- ACTIVE_DEPENDENCY;
- STALE_RETIRABLE_CANDIDATE;
- UNKNOWN;
- another exact evidence-based classification, with reason.

Determine:
1. what occupies /run/wb-shard-gateway;
2. whether any current process/service/socket references it;
3. plausible creator/consumer only where supported;
4. whether it is safe to place the exact contents into a later separate retirement decision;
5. exact additional evidence or authority still required.

## Prohibited

Do NOT:
- delete, truncate, edit, move, rename, chmod or chown anything;
- stop/start/reload services;
- perform gateway retirement;
- mutate /opt/wb-shard-gateway;
- mutate /var/lib/wellbeing/shard-gateway;
- mutate /var/log/wb-shard-gateway;
- mutate /data/wellbeing-lab;
- create proof roots;
- select/install/run backend;
- execute T01-T20;
- claim CHECKPOINT_DURABLE;
- run memory-layering attempt 3;
- mutate Project Sources/canons;
- replay historical PROMPT.

## Operator-assisted root path

If SIS cannot obtain required root-level read-only evidence directly through its available tool path, it may prepare one exact self-contained privileged read-only command block for OPERATOR.

That block must:
- be inspection-only;
- perform zero mutation;
- identify host;
- expose no secret values unnecessarily;
- print sufficient evidence for SIS classification;
- stop on unexpected condition.

OPERATOR returns the complete output to SIS.

Publication/dispatch/inbox of this task do not prove receipt or processing_started.

## Expected result

Return one immutable SIS result:

PASS_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01

or exact:
BLOCKED_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01_<reason>

or exact:
FAIL_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01_<reason>

The result must state whether a separate bounded retirement decision is supportable.

No later retirement authority is created by this task.

After immutable result/readback and addressed return to KOO, STOP.
