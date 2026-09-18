# KOO current active queue r0.4

status: CURRENT_QUEUE

## PRIORITY 1 — KOD / Entity AI booster blocker fix

Task:
`entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-ledger-race-fix-r01__KOD.md`

Commit:
`388d3b67d0d2e0de008ca1dd8cef872da46a4338`

Blocker source:
`d15b88501d227f778b657af638e86bf028f1948b`

Goal:
remove nondeterministic SQLite initialization race without weakening one-shot/live boundaries.

Next after KOD PASS:
SIS exact re-verification of new candidate.

Next after SIS PASS:
account/project/model/credential gate → one exact LIVE_EXECUTION_AUTHORITY → one bounded OpenAI D0 live call → independent result verification.

## PRIORITY 2 — WEB replacement initiation

ARH recovery package:
`PASS_ARH_WEB_RECOVERY_PACKAGE_READY_FOR_REPLACEMENT_INITIATION_R01`

External locator:
`puev5691/wellbeing-entity-bootstrap@70fa5df171903e5ec914cfd93b0cf60ec79c7664:entities/web/preservation/pending/emergency-replacement-r01`

KOO cold-start authorization:
`entities/koordinator/outbox/KOO__WEB-replacement-cold-start-authorize-r01__OPERATOR.md`
commit `d94d0b152ef4aa35903dc22f9c1878607fd23b7a`.

Old WEB remains frozen.
Presentation r0.2 remains pending/unknown until verified terminal evidence exists.

After replacement `initiation_verified`:
separate writer-gate/failover → reconcile r0.2 → resume exact task if still incomplete.

## NEXT — preservation / backup

ARH→SIS host-access pilot remains queued:
`9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

Start only after SIS completes booster re-verification.

Then:
mazhor physical readback → independent verify → burzh/erefia scale → mirror/offsite research → tooling → restore drill → scheduling authority.

## NEXT — Telegram facilitator

SemanticInput independent PASS:
`8d738f6a2eafb84485ab5e11e1961adb60d017ac`.

Next KOD slot after booster fix:
upstream semantic privacy/admission gate for real discussion excerpts.

## NEXT — public portal

Replacement WEB first.
After recovery/failover:
- reconcile presentation r0.2;
- if incomplete, resume exact r0.2;
- then deterministic static build;
- static readback/verification;
- public-ready decision only afterward.

## OPERATOR DECISIONS STILL OPEN

Backup:
- RPO;
- RTO;
- independent backup location/provider;
- critical repository/data scope;
- host/lab dataset scope;
- secret disaster-recovery boundary.

## POLICY

WIP limit: 2 active profile tasks.
A blocked task frees its execution slot but keeps dependency priority.
Published/queued does not mean executing.
UI state does not establish project completion.
