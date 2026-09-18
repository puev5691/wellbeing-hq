# KOO current active queue r0.15

status: CURRENT_QUEUE

## ACTIVE SLOT 1 — SIS / MAZHOR HOST ACCESS PILOT

Task:
`1594c534200fcebd94467f51a3d6094f37bcdbab`

Inbox:
`4328bee5907fc994c22f731cae04908714afa26f`

State:
no terminal SIS result observed yet.

Goal:
bounded preservation access/readback + baseline file/Git latency evidence.

## ACTIVE SLOT 2 — SHD / PORTAL FIX REVERIFY

Task:
`entities/koordinator/outbox/KOO__portal-fix-reverify-r01__SHD.md`

Commit:
`2c88f277e6703678b9bb1dc482a9ac10b078851d`

Corrected candidate:
`d268ff079ac04abce109caf3c3b33521c2b63f7c`

Goal:
reverify only corrected presentation boundary.

If PASS:
separate public-ready decision for portal.

## QUEUED NEXT — RED / HISTORY RECONSTRUCTION R0.2

Original completed wording is not recoverable.

New reconstruction task:
`entities/koordinator/outbox/KOO__project-history-reconstruct-r02__RED.md`

Commit:
`57d134a494e07ed59a3548cd55738340200fc372`

Do not claim lost r0.1 recovery.
Create a new evidence-grounded r0.2.

## QUEUED — KOD / FILE ARTIFACT SERVICE MVP

Direction:
`b62896ff271ab0480a4ff1fcecef386a7c65b1b6`

Queued task:
`f1753621b1181f425b574f68fca36e3bc40d115a`

Activate at next free KOD infrastructure slot.

## GIT SHARDS

After SIS mazhor pilot:
ARH physical readback → benchmark mazhor/burzh/erefia → select shard host(s) → READ/WRITE/VERIFY/ROUTE adapters.

## BOOSTERS

Final worker PASS:
`18af0b778d5b30f15c20da989a39006f503dcff3`

Waiting only OPERATOR account/project/model/credential/live authority inputs.

## TELEGRAM

Target mapping PASS:
`977a482936a8c0b4ad809c1b718048b1903fec9e`

First bounded one-send + public readback PASS:
`a8d46d205a3233b04aa9cf95cb4b349a166df119`

No automatic second send authority.

## POLICY

WIP limit: 2 active profile slots.
Queued RED and KOD tasks start only when a slot is clear.
