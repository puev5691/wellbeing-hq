# KOO current active queue r0.10

status: CURRENT_QUEUE

## SLOT 1 — SIS / TELEGRAM TARGET VERIFY

Source WEB task:
`f0ffa872b1873fda11b02f1731fabef91cc7f9c5`

KOO-addressed SIS inbox:
`ac75b05a01a33036e0bfdfc4dfec2f55843fda33`

State:
addressed, no terminal SIS result observed yet.

Goal:
verify exact bot/channel/admin/discussion/secret-storage mapping and exact first bounded send/readback method.

No send in this task.

## SLOT 2 — KOD / PORTAL PRESENTATION FIX

Task:
`entities/koordinator/outbox/KOO__portal-presentation-fix-r01__KOD.md`

Commit:
`4778a44e63da414f67681f30755350500f8a6463`

Independent failure:
`0710cdbb3c0817e5f1dba2df414a849af6f1cb34`

Goal:
replace machine/id-derived primary labels with Russian human-readable labels and render visible `Кандидат` badge, preserving deterministic/static/public-safe boundaries.

Next:
SHD exact reverify corrected build.

## BOOSTER LIVE STATUS

Final live-worker PASS:
`18af0b778d5b30f15c20da989a39006f503dcff3`.

Engineering chain is ready.
Waiting OPERATOR account gate:
- exact OpenAI API project/account;
- billing/prepaid readiness;
- model entitlement;
- project-scoped credential outside project artifacts;
- one exact LIVE_EXECUTION_AUTHORITY.

## NEXT — SIS / BACKUP HOST PILOT

After Telegram target verification:
ARH task `9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

First target: mazhor.

## NEXT — KOD / TELEGRAM SEMANTIC ADMISSION

After portal presentation fix:
upstream semantic privacy/admission gate for real discussion excerpts → SemanticInput.

## NEXT — PORTAL

After KOD presentation fix:
SHD reverify.
If PASS:
separate public-ready decision.
Only afterward deployment/Pages/DNS/HTTPS.

## NAMING RULE

Operator-facing prompt filenames:
recipient first → task/topic → short revision suffix.
Target length: about 40–50 characters.

## POLICY

WIP limit: 2 profile slots.
Addressed task is not execution.
Direct OPERATOR work may change queue; always preflight.
