# KOO → SIS: SIS-GWR-MAINT-R01 cycle 001 /var/log residue

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН current writer
authority: SIS-GWR-MAINT-R01 r0.2 APPROVED_DORMANT
project_time: omitted

Resume-First.

## Exact standing authority

puev5691/wellbeing-hq@8538840b06abfac333eb001449ee78106a5c92ab:
entities/sisadmin/current/SIS__GWR-MAINT-R01-r02-approved.md

status:
APPROVED_DORMANT

decision:
APPROVE_SIS_GWR_MAINT_R01_R02

## Current SIS writer basis

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Exact causal blocker

puev5691/wellbeing-hq@1cbbb48c6eb1cbef9f39e7d4dff963d773a53e26

terminal:
BLOCKED_SIS_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02_LOG_DIR_NONEMPTY

Exact object scope for this cycle:
/var/log/wb-shard-gateway

## Task

Activate one NEW execution instance under SIS-GWR-MAINT-R01 r0.2.

Run the standard bounded lifecycle only for /var/log/wb-shard-gateway:

1. Resume-First;
2. verify current SIS writer and exact host p552203.kvmvps;
3. run SIS-GWR-INSPECT against exact scoped path;
4. enumerate exact contained objects;
5. classify each object using standing-authority classes;
6. establish current dependency/use evidence;
7. establish preservation/rollback requirements where applicable;
8. determine whether any exact object is eligible for retirement under current authority;
9. do not perform any mutation that still requires separate OPERATOR decision;
10. return one immutable result/readback addressed to KOO.

If an exact object is independently eligible for retirement under the standing authority and does NOT fall into any separate-decision class, SIS may perform only that exact object retirement through SIS-GWR-RETIRE after fresh pre-mutation revalidation and then VERIFY.

If state/DATA deletion, whole-directory deletion, recursive/mass cleanup, wildcard/path-class deletion, multi-object cleanup as one operation, irreversible removal without demonstrated rollback, SECRET_SENSITIVE, UNKNOWN, ACTIVE_DEPENDENCY, path escape, host/writer mismatch, or any scope ambiguity occurs:
STOP affected object/cycle as required and return exact blocker/decision need to KOO.

## Hard exclusions

No authority for:
- /data/wellbeing-lab mutation;
- proof roots;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- Telegram/provider/credential work;
- Project Sources/canons;
- historical PROMPT replay.

## Mandatory return

Task is not conveyor-complete until SIS returns to KOO:
- exact task ref;
- terminal;
- immutable result locator/identity;
- classifications;
- mutations actually performed;
- remaining residue/blocker;
- next causal condition;
- whether OPERATOR action is required;
- consumed/non-replayable status.

After return KOO, STOP.
