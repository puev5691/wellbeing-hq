# SIS-GWR-MAINT-R01 r0.2 — approved standing authority

status: APPROVED_DORMANT
decision: APPROVE_SIS_GWR_MAINT_R01_R02
project_time: omitted
entity: SIS / СИСАДМИН
host: p552203.kvmvps

## Effect

OPERATOR approved SIS-GWR-MAINT-R01 r0.2 as a reusable bounded maintenance framework.

Approval creates:
STANDING_AUTHORITY = APPROVED / DORMANT

Approval does NOT start work.

Execution may start only from a NEW exact task addressed to the current authoritative SIS writer after Resume-First.

No alternative activation condition.
No automatic activation.
No historical PROMPT/task replay.

## Per-object gate

Before retirement of any exact object, the current task must establish:

1. exact path/object identity;
2. evidence of no current dependency/use;
3. immutable preservation and exact locator/version where required for recoverability;
4. exact retirement plan;
5. exact rollback plan.

If any required item is missing or UNKNOWN:
STOP affected object.

Classification:
- ACTIVE_DEPENDENCY -> STOP
- UNKNOWN -> STOP
- SECRET_SENSITIVE -> STOP + separate OPERATOR exception decision
- STALE_RETIRABLE_VERIFIED -> eligible for retirement decision only

STALE_RETIRABLE_VERIFIED does NOT itself authorize deletion.

## Separate OPERATOR decision always required

- state/DATA deletion;
- whole state/runtime data directory deletion;
- recursive or mass cleanup;
- wildcard/path-class deletion;
- multi-object cleanup treated as one operation;
- irreversible removal without demonstrated rollback.

## Allowed contour

- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- /run/wb-shard-gateway
- /var/lib/wellbeing/shard-gateway
- /var/log/wb-shard-gateway

Presence inside the allowed contour does not itself authorize mutation.

## Stable helpers

- /home/shd/SIS-GWR-INSPECT.sh
- /home/shd/SIS-GWR-RETIRE.sh

Helpers implement approved procedure only.
They do not create authority, select objects, bypass gates or convert UNKNOWN into PASS.

## Execution lifecycle

NEW exact task
-> Resume-First
-> INSPECT exact object
-> CLASSIFY
-> per-object gate
-> fresh pre-mutation revalidation
-> exact authorized mutation
-> VERIFY expected state and no collateral effect
-> next object only within same exact task scope
-> immutable result/readback
-> return KOO
-> EXECUTION_INSTANCE = CONSUMED

After completion:
STANDING_AUTHORITY = APPROVED / DORMANT

The consumed task is not replayable.

## Hard exclusions

This standing authority does NOT authorize:
- /data/wellbeing-lab mutation;
- proof roots;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay.

## Current activation state

No exact task is activated by this approval.

host mutation under this approval:
NONE

standing authority:
APPROVED / DORMANT
