# KOO → SIS: P552203 gateway retirement r0.1 operator-assisted privileged path

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.7
scope: OPERATOR_ASSISTED_PRIVILEGED_PRECHECK_AND_ALREADY_APPROVED_BOUNDED_RETIREMENT
project_time: omitted

Resume-First.

## Current KOO writer

puev5691/wellbeing-hq@9c5e330719fa4410eca76e91a128bfcc29d56c45:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

## Intended SIS writer basis

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

SIS must fresh-verify current-writer, supersession, replacement/freeze state and exact task authority before any profile work.

## Exact new authority

puev5691/wellbeing-hq@eb631f2d42b6c0ea16baaaa8cc02595095e6d896:
entities/koordinator/outbox/KOO__authorize-P552203-gateway-retirement-r01-operator-assisted-privileged-path__OPERATOR.md

blob:
6542798434b7bffc238d5f701615d066adb5f917

decision:
AUTHORIZE_P552203_GATEWAY_RETIREMENT_R01_OPERATOR_ASSISTED_PRIVILEGED_PATH

## Conveyor basis

puev5691/wellbeing-hq@a330e73003cbb7b62507b49f866df6113379211c:
entities/koordinator/outbox/KOO__task-conveyor-reconciliation-r10__OPERATOR.md

blob:
6a39f6862d55b033ac38f26de71fd92876ee0016

terminal:
PASS_KOO_TASK_CONVEYOR_RECONCILIATION_R10

## Prior retirement decision and blocked attempt

Prior OPERATOR retirement decision:

puev5691/wellbeing-hq@74c92d0c745e35ee4393e22b6db36a286b0f9bae:
entities/koordinator/outbox/KOO__P552203-gateway-retirement-approved-r01__OPERATOR.md

decision:
APPROVE_P552203_GATEWAY_RETIREMENT_R01

Prior blocked result:

puev5691/wellbeing-hq@e81cc1679cb95959be7fa0c5fb51e052c5c109fb:
entities/sisadmin/outbox/SIS__P552203-gateway-retirement-mutation-r01-blocker__KOO.md

terminal:
BLOCKED_SIS_P552203_GATEWAY_RETIREMENT_MUTATION_R01_PRIVILEGED_PRECHECK_UNAVAILABLE

Do not replay the old task. Use it only as historical dependency/evidence for the exact blocker and preserved scope.

## Exact preservation package

puev5691/wellbeing-hq@2f58bb83e43e6443335830e3e779cc4c6c38d0b6:
entities/sisadmin/outbox/p552203-stpc-preservation-r01/

tree:
9cf168ce696395872e57b81ea1bab64941006011

Freshly verify it remains readable before mutation.

## Exact host

expected hostname:
p552203.kvmvps

expected device:
830038a0-232b-4d83-b52d-0e9973126165

Fresh-verify host identity before giving OPERATOR any command.
If identity cannot be proven, STOP.

## Task

Perform only the operator-assisted privileged retirement path.

Phase 1 — fresh non-mutating reconciliation by SIS:
- verify exact current SIS writer and this task/authority;
- verify exact host identity;
- verify service still loaded/inactive/dead;
- verify unit still disabled;
- verify no reverse dependencies;
- verify no enable symlinks;
- verify no related active units;
- verify no current project runtime consumer;
- verify exact preservation package remains readable;
- verify no superseding task/result/authority.

If any check fails or is UNKNOWN:
STOP and return exact blocker.

Phase 2 — prepare ONE exact copy-paste privileged command block for OPERATOR.

The block may do only:
1. immediate root-level read-only emptiness verification of:
   - /var/lib/wellbeing/shard-gateway
   - /run/wb-shard-gateway
   - /var/log/wb-shard-gateway
2. fail closed before mutation if any approved runtime directory is non-empty, missing in an unexpected way, inaccessible, ambiguous or changed;
3. repeat/confirm mandatory dependency/service checks where root evidence is needed;
4. only after all prechecks PASS, remove exactly:
   - /etc/systemd/system/wellbeing-shard-gateway-verify.service
   - /opt/wb-shard-gateway
   - /var/lib/wellbeing/shard-gateway
   - /run/wb-shard-gateway
   - /var/log/wb-shard-gateway
5. run systemd daemon-reload only if needed after unit removal;
6. print sufficient exact post-mutation evidence for SIS verification.

The command block must:
- be self-contained;
- identify the host before mutation;
- stop on error;
- not suppress errors that affect proof;
- visibly separate PRECHECK PASS from mutation;
- print exact evidence needed for SIS to determine terminal result;
- not access secrets or unrelated paths.

OPERATOR will execute only this exact block and return the complete output to SIS.

Phase 3 — after OPERATOR returns output:
- verify exact output against this task;
- do not infer omitted evidence;
- if all required prechecks and postchecks are proven, publish immutable result/readback and return KOO;
- otherwise return exact BLOCKED_/FAIL_ with no further mutation attempt.

## Mandatory STOP conditions

STOP on:
- writer/task/authority mismatch;
- supersession;
- host identity mismatch;
- service state changed;
- unit enabled;
- reverse dependency;
- enable symlink;
- related active unit;
- project runtime consumer;
- any non-empty runtime directory;
- ambiguous/incomplete privileged evidence;
- preservation package failure;
- unexpected file/path;
- command output missing required evidence;
- any condition outside exact approved scope.

## Not authorized

- touching /data/wellbeing-lab preservation source;
- deleting/moving any unrelated object;
- reset/reimage;
- proof-root creation;
- backend selection/install/run;
- T01-T20 execution;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay.

## Expected result

Before OPERATOR executes:
return one exact privileged command block plus a short explanation of what OPERATOR must do with it.

After OPERATOR execution/output:
return one:
- PASS_SIS_P552203_GATEWAY_RETIREMENT_R01_OPERATOR_ASSISTED_COMPLETE
- exact BLOCKED_*
- exact FAIL_*

After immutable result/readback and addressed return to KOO, STOP.
