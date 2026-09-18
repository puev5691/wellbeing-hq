# KOO current active queue r0.6

status: CURRENT_QUEUE

## SLOT 1 — SIS / BOOSTER REVERIFY

Task:
`entities/koordinator/outbox/KOO__liveworker-racefix-independent-reverify-r01__SIS.md`

Commit:
`78cbcdad58d2dd7da9200f09abcf30b37ad5d509`

Candidate:
`entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/`
commit `6880f16459c5424992fcbe2102f0889142fe533a`

Goal:
close prior `BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`.

If PASS:
- freeze accepted worker identity;
- resolve OpenAI account/project/model entitlement;
- confirm dedicated project-scoped credential exists outside project files;
- issue one exact LIVE_EXECUTION_AUTHORITY;
- perform exactly one bounded D0 live call;
- independently verify result and one-shot ledger.

## SLOT 2 — replacement WEB / MANUAL COLD-START

Old WEB remains frozen.

Recovery package:
`puev5691/wellbeing-entity-bootstrap@70fa5df171903e5ec914cfd93b0cf60ec79c7664:entities/web/preservation/pending/emergency-replacement-r01`

KOO authorization:
`d94d0b152ef4aa35903dc22f9c1878607fd23b7a`

State:
replacement WEB is not yet verified as initiated/current writer.

Action:
new WEB chat cold-start → initiation report → initiation_verified → separate writer gate → reconcile/resume portal r0.2.

## NEXT — SIS / BACKUP HOST PILOT

Queued after booster reverify:
ARH task `9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

First target:
mazhor.

Goal:
bounded preservation channel and physical readback of known backup locator.

## NEXT — KOD / TELEGRAM SEMANTIC ADMISSION

After booster lane frees:
upstream semantic privacy/admission gate for real discussion excerpts → SemanticInput.

Research input available:
Rizzoma architectural candidate `880efdc8b03f9bcce8749fc17301106a193afa2c`.

## NEXT — WEB / PORTAL

After replacement initiation and writer gate:
- reconcile r0.2;
- if no terminal artifact exists, resume exact task `37f051ac7fc01ecb0a96b8d15891aa549e22764e`;
- then static build;
- independent readback;
- separate public-ready decision.

## OPEN OPERATOR BACKUP DECISIONS

- RPO;
- RTO;
- independent backup provider/location;
- critical repository/data scope;
- host/lab dataset scope;
- secret disaster-recovery boundary.

## NAMING RULE FOR OPERATOR-FACING FILES

Put the distinguishing task/topic first.
Put entity, mode, revision and service suffixes later.

## POLICY

WIP limit: 2 profile slots.
UI/browser state is not project completion evidence.
Published task is not execution.
