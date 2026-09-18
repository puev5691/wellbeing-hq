# KOO → OPERATOR: WEB chat degradation freeze r0.1

status: OPERATOR_DECISION_RECORDED
entity: WEB / ВЕБМАСТЕР

## Observed symptom supplied by OPERATOR

- WEB chat in browser appears to show the task as completed;
- WEB chat in the application remains stuck in a thinking state;
- OPERATOR directs preservation/recovery preparation and replacement initiation.

This record does not infer hidden chat state from UI behavior.

## Project-state consequence

WEB profile execution is frozen pending preservation/recovery processing.

The currently addressed WEB task remains an active dependency with unverified terminal state:

`entities/koordinator/outbox/KOO__public-info-portal-presentation-r02__WEB.md`
commit `37f051ac7fc01ecb0a96b8d15891aa549e22764e`.

No terminal GitHub result for that task is claimed by KOO at this boundary.

## Required procedure

Use current recovery canon:
1. external coordination checkpoint;
2. request/collect authoritative WEB self-snapshot if current writer is still usable;
3. if current writer is not usable, record failure-state and do not reconstruct self-state;
4. preserve current active dependencies and accepted results;
5. build/verify external recovery package;
6. prepare replacement initiation runbook;
7. only after verified initiation establish replacement current-writer according to canon.

Historical continuity candidate may be used as evidence only:
package commit `f4d45cc977b0c8f0e16e61ce39cd7ce264261411`
verdict `PASS_WEB_CONTINUITY_CANDIDATE_READY`.

It is explicitly NOT canonical recovery by itself.

No deployment/publication/runtime mutation is authorized.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: freeze degraded WEB instance and trigger canonical preservation/replacement procedure
СТАТУС: WEB_PROFILE_FROZEN_FOR_RECOVERY
