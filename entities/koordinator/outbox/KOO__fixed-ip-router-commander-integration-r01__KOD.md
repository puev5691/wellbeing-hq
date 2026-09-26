# KOO → KOD: fixed-IP router → Remote Desktop Commander integration r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: OPERATOR_ASSISTED_CONTROL_PATH_INTEGRATION_NO_AUTO_FAILOVER
project_time: omitted

## Exact authority

puev5691/wellbeing-hq@08670d2c4b6322d461bf3744b9df43ac67323a90:
entities/koordinator/outbox/KOO__authorize-KOD-fixed-ip-router-commander-integration-r01__OPERATOR.md

token:
AUTHORIZE_KOD_FIXED_IP_ROUTER_COMMANDER_INTEGRATION_R01_OPERATOR_ASSISTED

## Current KOD writer

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

blob:
cf1c84f9df7c90509703e4885844d0cf871ff412

Writer Gate:
puev5691/wellbeing-hq@fd48a57fc49f0330c93e632fa8221b5476e6cfe9:
entities/koder/outbox/KOD__replacement-writer-gate-v05-result__KOO.md

terminal:
PASS_KOD_REPLACEMENT_WRITER_GATE_V05

## Current fixed-IP router state

puev5691/wellbeing-hq@b3098eabccef13f86dc2c2686dc7102f89fd46f8:
entities/koordinator/current/KOO__fixed-ip-router-current-state-r01.md

blob:
804c28f8052fbdeadbfb62cd2fe995a6e5d2c9e3

status:
OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

## Existing Commander mapping

Use existing project evidence and current control-path facts. Current logical mapping to preserve:

- burzh -> ruvds-xnqc6
- mazhor -> p552203.kvmvps
- erefia -> ruvds-ygo0w

Do not invent device IDs or credentials. If exact Commander device IDs are required, fetch/verify them from existing project evidence or return a bounded blocker for the missing exact identity.

## Required integration

Prepare one implementation-ready integration package that turns the current manual node-selection policy into an actual operator-assisted Remote Desktop Commander selection/control interface.

The adapter must:

1. Accept a logical selected node only from:
   - burzh
   - mazhor
   - erefia

2. Map it to the exact verified Commander device identity.

3. Preserve current policy:
   burzh -> mazhor -> erefia

4. Preserve fixed-IP health semantics as a prerequisite/signal only:
   - 104.18.32.47 first
   - 172.64.155.209 only after TARGET_IP_FAILURE of first
   - TLS_CERTIFICATE_FAILURE = STOP
   - HTTP_APPLICATION_RESPONSE including 403/429/5xx is not transport failure

5. Produce an explicit operator-assisted control action, never an autonomous switch.

6. Separate:
   - route-selection evidence;
   - Commander device selection;
   - task authority for the command to be executed.

7. Never treat successful node selection as authority to execute arbitrary host mutations.

8. Produce closed audit output:
   - selected logical node;
   - selected Commander device identity;
   - fixed-IP health evidence reference/state;
   - explicit operator/manual selection marker;
   - requested action identifier;
   - outcome;
   - no secrets/private command payload in audit unless separately required by the task contract.

9. Define exact failure states:
   - ROUTE_NOT_HEALTHY
   - COMMANDER_DEVICE_UNKNOWN
   - COMMANDER_DEVICE_UNAVAILABLE
   - TASK_AUTHORITY_MISSING
   - CONTROL_PATH_READY
   - CONTROL_PATH_EXECUTION_BLOCKED

10. Include tests for:
   - valid burzh mapping;
   - valid mazhor mapping;
   - valid erefia mapping;
   - unknown logical node rejected;
   - missing/unknown Commander identity rejected;
   - route unhealthy blocks selection;
   - TLS certificate failure blocks selection;
   - HTTP 403 health evidence does not block control-path readiness;
   - missing task authority blocks execution;
   - manual node override is explicit and auditable;
   - no automatic fallback to another Commander device;
   - no credential/provider/DNS behavior.

## Deliverable

Implementation-ready package only.

Include:
- source code;
- config/schema for node→Commander mapping;
- current mapping fixture;
- tests;
- README/runbook;
- MANIFEST;
- SHA256SUMS;
- exact result addressed to KOO.

Expected terminal:
PASS_KOD_FIXED_IP_ROUTER_COMMANDER_INTEGRATION_R01_READY_FOR_SIS_REVIEW

or exact BLOCKED_* / FAIL_*.

## Hard boundary

No:
- automatic failover;
- autonomous node switching;
- automatic IP discovery/admission;
- DNS fallback;
- provider/API;
- credential acquisition/readout;
- arbitrary host command execution during package construction;
- production deployment;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE claim;
- resume authority;
- Memory-layering attempt 3.

After immutable package + tests + readback + addressed result to KOO, STOP.
