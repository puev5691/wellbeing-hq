# KOO — parallel-lane operating delta v0.1

status: ACTIVE_WORKING_DIRECTIVE
canon: no
scope: KOO scheduling/reconciliation only
production_mutation: no
automation_change: no
project_time: omitted; trusted project-time source not used

## Basis

Existing dynamic route algorithm:
`entities/koordinator/current/KOO__dynamic-next-route-algorithm.md`
commit `8db0d5a8231256bc01d9b49fd7afcfac48d8d6b6`.

Accepted SHT review:
`entities/shtabist/outbox/SHT__adaptive-parallel-queue-review__KOO.md`
commit `f4134b18ac16a862cae7a78e2b7d78212e406bcc`
blob `f3523e4522805294bf049a64f0b7a00c03dd9561`.

## Working change

Replace operational selection:

`SELECT ONE NEXT OWNER`

with:

`BUILD CONFLICT GRAPH → SELECT SAFE READY_PARALLEL SET → PRIORITIZE/AGE → DISPATCH EXACT LANES → RECONCILE RETURNS`.

A task is `READY_PARALLEL` only when:
- exact task/input and profile owner exist;
- no causal dependency exists between selected lanes;
- mutable write/current-writer domains do not conflict;
- no unsafe shared privileged/runtime resource exists;
- no shared release/authority decision is being concurrently mutated;
- each lane returns an immutable standalone result through Exchange Gate.

Operational states:
`READY_PARALLEL`, `RUNNING`, `WAITING_EXTERNAL`, `WAITING_ENTITY`, `WAITING_OPERATOR`, `CONFLICT`, `CLOSED`.

Inbox placement or activation request does not prove `RUNNING`.

Returned results are reconciled by causal decision node, not arrival order.

SHD remains:
- `queue_participation: excluded_operator_direct_control`;
- `scheduler_eligible: no`;
- pending return event preserved;
- re-entry only after verified return or OPERATOR direction.

No fixed numeric concurrency cap is asserted yet. KOO emits only a bounded activation batch whose lanes have passed conflict checks.

This file is a working scheduling directive under existing KOO authority. It is not Project Source/canon and does not create new Entity authority.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: practically adopt accepted SHT parallel-lane model without pretending it is approved canon
СТАТУС: active_working_directive
