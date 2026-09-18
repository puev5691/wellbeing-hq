# KOO current active queue r0.7

status: CURRENT_QUEUE

## SLOT 1 — KOD / LIVEWORKER HASH METADATA FIX

Task:
`entities/koordinator/outbox/KOO__liveworker-hash-metadata-fix-r01__KOD.md`

Commit:
`628ff93bc70aab8ed77556cc3d216df180cf43fc`

Blocker:
`BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`

Important:
behavioral race blocker is independently closed.
This task is exact identity/metadata correction unless byte reconciliation proves code mismatch.

Next:
SIS exact independent re-verification of new immutable package.

## SLOT 2 — replacement WEB / WRITER GATE

Verified initiation:
`5c1d156456858c05e7df840547d32ac6dd1e7ed6`

Writer-gate authorization:
`entities/koordinator/outbox/KOO__WEB-replacement-writer-gate-r01__WEB.md`
commit `ee02d0bb3c2b58da9e0135739ebefd8851260162`

Goal:
establish replacement current-writer under recovery canon, with old WEB frozen.

After writer gate PASS:
reconcile portal presentation r0.2.
If no verified terminal artifact exists, resume exact task:
`37f051ac7fc01ecb0a96b8d15891aa549e22764e`.

## NEXT — SIS / BOOSTER REVERIFY

After KOD hash-fix:
reverify exact immutable candidate:
- blob/SHA identity;
- preserved concurrency behavior;
- no-live authority boundaries.

If PASS:
account/project/model/credential gate → one exact LIVE_EXECUTION_AUTHORITY → one bounded OpenAI D0 call → independent result verification.

## NEXT — SIS / BACKUP HOST PILOT

ARH task:
`9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

Start after booster reverify slot frees.

First target:
mazhor physical backup readback.

## NEXT — KOD / TELEGRAM SEMANTIC ADMISSION

After booster lane frees:
upstream semantic privacy/admission gate for real discussion excerpts → SemanticInput.

Use Rizzoma input only as non-priority architectural reference:
`880efdc8b03f9bcce8749fc17301106a193afa2c`.

## NEXT — PORTAL

After replacement writer gate:
- reconcile/resume r0.2;
- presentation r0.2 PASS;
- deterministic static build;
- independent verification;
- separate public-ready decision.

## OPEN OPERATOR BACKUP DECISIONS

- RPO;
- RTO;
- independent backup provider/location;
- critical repository/data scope;
- host/lab dataset scope;
- secret disaster-recovery boundary.

## NAMING RULE

Operator-facing downloadable files:
distinguishing topic/action first;
entity/mode/revision/service suffix later.

## POLICY

WIP limit: 2 profile slots.
UI/browser state is not completion evidence.
Published task is not execution.
