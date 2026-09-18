# KOO current active queue r0.5

status: CURRENT_QUEUE

## ACTIVE / MANUAL ACTIVATION REQUIRED 1 — KOD / booster race fix

Task:
`entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-ledger-race-fix-r01__KOD.md`

Commit:
`388d3b67d0d2e0de008ca1dd8cef872da46a4338`

Inbox:
`029e79967bd76cb5bf7f693f047fe911c7e34bfe`

State:
published, no terminal KOD result observed yet.

Goal:
fix exact `BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`.

Next after KOD PASS:
SIS exact re-verification of corrected immutable candidate.

## ACTIVE / MANUAL ACTIVATION REQUIRED 2 — replacement WEB

Old WEB:
`WEB_PROFILE_FROZEN_FOR_RECOVERY`

ARH recovery result:
`PASS_ARH_WEB_RECOVERY_PACKAGE_READY_FOR_REPLACEMENT_INITIATION_R01`

External locator:
`puev5691/wellbeing-entity-bootstrap@70fa5df171903e5ec914cfd93b0cf60ec79c7664:entities/web/preservation/pending/emergency-replacement-r01`

KOO authorization:
`d94d0b152ef4aa35903dc22f9c1878607fd23b7a`

State:
replacement WEB not yet verified as initiated/current writer.

Next:
cold-start new WEB chat → initiation report → initiation_verified → separate writer gate → reconcile/resume portal presentation r0.2.

## QUEUED — SIS / preservation host access

ARH task:
`9b147fac4b80431ec4ed24f28efc2cb775326d8e`

Do not activate while SIS is reserved for immediate booster re-verification after KOD race fix.

After booster verification:
SIS bounded preservation host-access design → mazhor pilot → ARH physical readback → independent verification → burzh/erefia scaling.

## QUEUED — Telegram facilitator

SemanticInput independent PASS:
`8d738f6a2eafb84485ab5e11e1961adb60d017ac`

Next KOD task after booster lane frees:
upstream semantic privacy/admission gate for real discussion excerpts.

Rizzoma architectural research input:
`880efdc8b03f9bcce8749fc17301106a193afa2c`
is available as non-priority design input only.

## QUEUED — public information portal

After replacement WEB writer gate:
1. reconcile portal presentation r0.2;
2. if no verified terminal artifact exists, resume exact task
   `37f051ac7fc01ecb0a96b8d15891aa549e22764e`;
3. incorporate RED review `8484b16dbb6d46833af4096f8f9b5f8e442aec1a`;
4. use Rizzoma input only as optional future interaction-layer design reference;
5. after r0.2 PASS → deterministic static build → verification → separate public-ready decision.

## QUEUED — backups

ARH audit PASS:
`63355a8d3217493469def17524a8290c5f04685c`.

Still awaiting OPERATOR decisions:
- RPO;
- RTO;
- independent backup location/provider;
- critical repository/data scope;
- host/lab dataset scope;
- secret disaster-recovery boundary.

## RULE

WIP limit: 2 profile execution slots.
Current practical slots:
1. KOD race fix;
2. replacement WEB initiation.

No new profile task should displace these until one closes or blocks.
UI/browser state is not project completion evidence.
