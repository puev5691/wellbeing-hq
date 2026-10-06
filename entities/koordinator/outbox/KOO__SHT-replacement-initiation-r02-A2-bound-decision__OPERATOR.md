# KOO r1.3 -> OPERATOR: authorize bound SHT replacement Initiation Gate r02 A2

status:
WAITING_OPERATOR_DECISION

project_time:
omitted

## Exact reconciliation basis

puev5691/wellbeing-hq@e73d59ce0f17ca4be459ff01330b8b3554136cc0:
entities/koordinator/current/KOO__SHT-r02-A1-instance-conflict-reconciliation__OPERATOR.md

blob:
c28fd1216ce7f2a0ff2222aa04f49785f61eb103

terminal:
PASS_KOO_R13_SHT_R02_A1_INSTANCE_CONFLICT_RECONCILED_TO_BOUND_A2_GATE

## A1 disposition

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A1

disposition:
BLOCKED_NON_EXECUTABLE_INSTANCE_BINDING_CONFLICT

Do not replay or resume A1.

Existing A1 PROCESSING_STARTED owner:
UNKNOWN_CONFLICT

## Exact successor proposal

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A2

scope:
INITIATION_GATE_ONLY

instance_binding_id:
SHT_R02_A2_BOUND_TO_FAIL_RESULT_E80DD56

Only the exact SHT chat instance that authored:

puev5691/wellbeing-hq@e80dd56a6e92284ae875540dcb062114b9837489:
entities/shtabist/outbox/SHT__replacement-initiation-gate-r02-result__KOO.md

blob:
144a4e549ee84772e55af6b6b958de313f247abe

may execute A2.

If the PROMPT is delivered to any other chat instance, that chat must STOP without creating PROCESSING_STARTED.

## Exact recovery reused

puev5691/wellbeing-entity-bootstrap@c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5:
entities/sht/recovery/versions/sht-recovery-r02

tree:
f561246223a48ac885d7baae383898cc8e89af16

recoverability:
READY_FOR_REPLACEMENT_INITIATION_HANDOFF

No new recovery package is required for A2.

## A2 start boundary

A2 must use a new distinct evidence path:

entities/shtabist/outbox/execution-evidence/SHT_REPLACEMENT_INITIATION_GATE_R02_A2__PROCESSING_STARTED_E1.md

The evidence must bind:
- A2 attempt;
- A2 accepted frontier;
- instance_binding_id;
- anchor result commit;
- anchor result blob;
- exact recovery ref/tree.

Before creating A2 PROCESSING_STARTED:
- fresh-check A1 non-executable disposition;
- fresh-check no A2 start/result already exists;
- fresh-check recovery r02 remains current;
- fresh-check predecessor writer unchanged;
- fresh-check profile continuation remains PAUSED_BY_OPERATOR.

## Preserved boundary

predecessor writer:
CURRENT_WRITER / unchanged

profile continuation:
PAUSED_BY_OPERATOR

D1D2:
COMPLETED_PASS

narrow rereview:
NOT_STARTED / NOT_AUTHORIZED

historical replay:
FORBIDDEN

## Not authorized

- Writer Gate;
- current-writer establishment/transfer;
- predecessor freeze/retirement;
- profile continuation;
- narrow rereview;
- historical replay;
- automatic activation.

## Exact OPERATOR decision

AUTHORIZE_SHT_REPLACEMENT_INITIATION_GATE_R02_A2_BOUND_TO_E80DD56 = YES

If approved, KOO may materialize exactly one new A2 authority/registry/frontier/PROMPT bound to the anchor instance above.

STOP at OPERATOR decision.
