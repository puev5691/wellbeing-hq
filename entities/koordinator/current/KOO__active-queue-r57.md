# KOO current active queue r0.57

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## OPERATOR deployment authority remains bounded

Decision:
`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

Authority commit:
`0aadf1753e442ff792b2d43f402ad47ebeb984ee`.

The authority remains limited to mazhor bounded VERIFY deployment and does not authorize:
- existing repo/archive chmod/chown/ACL/group mutation;
- credentials;
- network listener;
- WRITE;
- burzh/erefia mutation;
- production acceptance.

## Fresh SIS terminal blocker reconciliation

SIS result:
`entities/sisadmin/outbox/SIS__mazhor-shard-gateway-r02-bounded-verify-deployment__KOO.md`

commit:
`6835c756a0cb1254c6f51ec9a6f5f1637eb82d86`

verdict:
`BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: ARH_PRESERVE_GIT_SAFE_DIRECTORY_REJECTS_REPO`.

Verified host state at blocker:
- target `mazhor / p552203.kvmvps`;
- Phase 0 read-only predeploy PASS;
- Phase 1 created `arh-preserve`;
- uid 999 / gid 988;
- groups: `arh-preserve` only;
- shell: `/usr/sbin/nologin`;
- credentials: none;
- POSIX repo read/traverse PASS;
- POSIX archive read/traverse PASS;
- archive listing PASS;
- Git read as `arh-preserve` fails with dubious ownership / safe.directory;
- existing repo/archive remain `0775 shd:shd`;
- runtime install paths remain absent;
- unit/request/audit/smoke not created/run;
- repo/archive/shard mutation = 0;
- production acceptance = no.

Existing bounded host mutation retained:
`arh-preserve` exists and is reversible.

## Exact defect ownership

Owner:
KOD / КОДЕР.

Reason:
the defect is in Git subprocess invocation policy inside the adapter.
The existing adapter invokes Git without an exact command-scoped safe.directory exception.

KOO synthetic verification confirmed:
- same-owner-mismatch Git read fails normally;
- `git -c safe.directory=<exact-root> ...` succeeds;
- no persistent Git config write is required.

Correction must remain code-local/per-invocation.
No service/global/user Git config or environment authority expansion.

## ACTIVE SLOT 1 — KOD / GATEWAY R0.3 GIT SAFE.DIRECTORY CORRECTION

KOD current-writer:
`entities/koder/current/KOD__replacement-current-writer-v04.md`

writer establishment commit:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

writer blob:
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

Exact task:
`entities/koordinator/outbox/KOO__gateway-r03-git-safe-directory__KOD.md`

task commit:
`6d40523b00e01dd9663929e2e65aa9a3fa6fcdf7`

task blob:
`cb4669fe1810e490409f4591a31251f2c37b4e80`.

Dispatch:
`8aed1c792aab8f28369acdabae4b7d1a1a94eab2`.

KOD inbox:
`3b2024925e5d9fcb879ace94c0635f27c18e3ef8`.

Sender registry:
`4181053441f8956c325a78824d62d34024745bce`.

Automatic activation boundary:
`0ade8c84bcc38e1a7a6fd2c4f11408cd7743b172`.

activation_status:
`activation_failed`.

processing_started:
`no`.

operator_manual_ping_required:
`yes`.

State:
`AWAITING_OPERATOR_TRANSFER`.

## Required successor design

KOD must publish:
- immutable adapter r0.3;
- immutable harness r0.3 with exact adapter-r0.3 pin.

Git safe.directory policy:
- command-scoped only;
- exact selected allowlisted repo root only;
- every Git subprocess;
- no wildcard;
- no request-controlled safe.directory;
- no archive root;
- no global/system/local config mutation;
- no HOME/GIT_CONFIG_*/PYTHONPATH environment expansion.

Expected design form:
`git -c safe.directory=<exact-allowlisted-repo-root> <existing-read-only-git-args...>`.

## SIS resume point after KOD successor

No executable SIS resume task is created yet because exact immutable successor identities do not exist.

Creating it now would violate locator/version exactness.

The resume point is already fixed:

`RESUME_FROM_PHASE_2_GIT_RUNTIME_SUBGATE`.

After KOD terminal PASS and fresh reconciliation, the exact SIS resume task must:
- retain existing `arh-preserve`; do not recreate it;
- do not replay Phase 0/Phase 1 mutations;
- fresh-check current host/authority continuity;
- briefly reconfirm Phase 2 POSIX read/traverse;
- verify exact successor runtime Git read under existing `arh-preserve`;
- independently verify no persistent Git config/environment expansion;
- only on Git subgate PASS continue at original Phase 3;
- preserve all original rollback/stop boundaries.

## Expected KOD terminal

`PASS_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY_READY_FOR_SIS_RESUME`

or exact blocker/fail.

## EXACT NEXT CAUSAL STATE

`KOD_GATEWAY_R03_GIT_SAFE_DIRECTORY_AWAITING_OPERATOR_ACTIVATION`

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: state after mazhor Phase-2 Git ownership blocker and exact KOD correction routing
СТАТУС: CURRENT_QUEUE
