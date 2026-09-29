# SIS-GWR-MAINT-R01 r0.3 — approved standing authority

status: APPROVED_DORMANT
decision: APPROVE_SIS_GWR_MAINT_R01_R03
project_time: omitted
entity: SIS / СИСАДМИН
host: p552203.kvmvps

## Approval basis

OPERATOR explicitly approved SIS-GWR-MAINT-R01 r0.3.

Exact approved candidate:

puev5691/wellbeing-hq@7b989544d8cbd8514f8cad20987bfe0f8c8b14a6:
entities/sisadmin/outbox/SIS__GWR-MAINT-R01-r03-candidate__OPERATOR-KOO.md

blob:
1ad16d12155ceee4bcdbf7ff24d28b16aefb1740

## Effect

SIS-GWR-MAINT-R01 r0.3 becomes the approved standing bounded authority for future NEW exact maintenance tasks concerning the legacy wellbeing-shard-gateway contour on exact host p552203.kvmvps.

standing authority:
APPROVED / DORMANT

Approval alone does NOT start work.

Execution still requires:
- current authoritative SIS writer;
- Resume-First PASS;
- a NEW exact task addressed to current SIS;
- exact host verification;
- required preservation/evidence prerequisites by object class;
- no supersession/conflict.

No automatic activation.
No historical PROMPT replay.

## r0.3 correction effect

r0.3 supersedes r0.2 semantics for future NEW exact maintenance tasks.

EPHEMERAL_RUNTIME_RESIDUE is treated separately from durable/state-bearing objects.

For an admitted ephemeral object, fresh pre-mutation reverify outcomes include:

- same object still exists and matches -> RETIRE exact object;
- object already absent -> RETIREMENT_ALREADY_SATISFIED / no mutation;
- same pathname now identifies a different object -> NEW_OBJECT / inspect from zero;
- active/unknown/sensitive/out-of-scope state -> STOP.

Disappearance of an admitted ephemeral object is not by itself an object-identity blocker.

## Preservation semantics

DURABLE_STATE_OR_DATA and CONFIG_OR_EXECUTABLE:
exact preservation/rollback requirements remain mandatory.

EPHEMERAL_RUNTIME_RESIDUE:
full byte-for-byte preservation is not mandatory when recoverability does not depend on the object, but required evidence must still include exact identity/metadata, hash where applicable, dependency/current-use evidence, sensitivity classification and classification rationale.

If an object is required audit/recovery evidence, it is not eligible for ephemeral treatment.

## Mutation boundary

Classification does NOT itself authorize deletion.

Mutation still requires:
- approved standing authority;
- NEW exact current task;
- object admission;
- fresh pre-mutation revalidation.

State/DATA deletion, whole state/runtime data directory deletion, recursive/mass cleanup, wildcard/path-class deletion, multi-object cleanup as one operation, or irreversible removal without demonstrated rollback still require a separate explicit OPERATOR decision.

## Hard exclusions

No authority for:
- /data/wellbeing-lab mutation;
- proof roots;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canons mutation;
- unrelated host/service cleanup;
- reset/reimage;
- historical PROMPT replay;
- automatic activation.

## Current activation state

No task is activated by this approval.

host mutation:
NONE

standing authority:
APPROVED / DORMANT

## Terminal

PASS_SIS_GWR_MAINT_R01_R03_APPROVED_DORMANT
