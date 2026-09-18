# KOO current active queue r0.8

status: CURRENT_QUEUE

## SLOT 1 — SIS / LIVEWORKER FINAL REVERIFY

Task:
`entities/koordinator/outbox/KOO__liveworker-final-immutable-reverify-r01__SIS.md`

Commit:
`f936349c74c1da43171d37f3824c1cc916e4242b`

Candidate:
`entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/`
commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`.

Goal:
close immutable SHA metadata blocker and confirm final no-live worker package.

If PASS:
- freeze accepted worker identity;
- resolve OpenAI account/project/model entitlement;
- confirm project-scoped credential outside project artifacts;
- issue one exact LIVE_EXECUTION_AUTHORITY;
- exactly one bounded OpenAI D0 live call;
- independent result verification.

## SLOT 2 — KOD / PORTAL STATIC BUILD

Task:
`entities/koordinator/outbox/KOO__portal-static-build-r01__KOD.md`

Commit:
`deb06cece3c4f10ed41562b010c7e14547d00b54`

Basis:
WEB presentation r0.2 PASS:
`6942b918fafb9d5f9646859f2c5fedd5ed4bd6bd`.

Goal:
deterministic local/static non-production build with exact pinned provenance and readback.

## NEXT — SIS / TELEGRAM TARGET VERIFICATION

WEB-authored task:
`f0ffa872b1873fda11b02f1731fabef91cc7f9c5`

State:
TASK_READY_FOR_SIS.

Start after live-worker final reverify completes.

Goal:
verify bot identity, channel numeric id/admin rights/discussion mapping/non-public secret storage and exact first bounded send/readback method, without sending.

## NEXT — SIS / BACKUP HOST PILOT

ARH task:
`9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

Start after Telegram target verification unless KOO/OPERATOR reprioritizes.

First target:
mazhor.

## NEXT — KOD / TELEGRAM SEMANTIC ADMISSION

SemanticInput independent PASS:
`8d738f6a2eafb84485ab5e11e1961adb60d017ac`.

After static portal build:
upstream semantic privacy/admission gate for real discussion excerpts → SemanticInput.

Rizzoma research candidate:
`880efdc8b03f9bcce8749fc17301106a193afa2c`
is non-priority architectural input only.

## NEXT — PORTAL

After KOD static build PASS:
independent verification/readback → separate public-ready decision → only then deployment/DNS/Pages/HTTPS task.

## WEB STATUS

Replacement WEB:
writer gate PASS.
Current writer established:
`e935c812e64683ac8be1a9a677b2d7d807f2a989`.

Portal presentation r0.2:
PASS ready for static build.

Telegram surface mapping:
`BOUNDED_MAPPING_RECONCILED_BLOCKED_ON_TELEGRAM_ADMIN_FACTS`
commit `faa09e7409672007948d36b5dca3a576b1b8ad88`.

## OPEN OPERATOR BACKUP DECISIONS

- RPO;
- RTO;
- independent backup provider/location;
- critical repository/data scope;
- host/lab dataset scope;
- secret disaster-recovery boundary.

## NAMING RULE

Operator-facing files:
distinguishing topic/action first;
entity/mode/revision/service suffix later.

## POLICY

WIP limit: 2 profile slots.
Published task is not execution.
Direct OPERATOR work may change queue; always preflight before issuing prompts.
