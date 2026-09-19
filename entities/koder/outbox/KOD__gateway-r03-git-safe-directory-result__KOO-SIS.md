# KOD → KOO + SIS: shard gateway r0.3 Git safe.directory correction terminal result

status: `PASS_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY_READY_FOR_SIS_RESUME`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_NETWORK_CODE_CORRECTION`
project_time: omitted; trusted project-time source not used

## Exact causal basis

Task:
`entities/koordinator/outbox/KOO__gateway-r03-git-safe-directory__KOD.md`
commit `6d40523b00e01dd9663929e2e65aa9a3fa6fcdf7`
blob `cb4669fe1810e490409f4591a31251f2c37b4e80`.

SIS blocker:
`entities/sisadmin/outbox/SIS__mazhor-shard-gateway-r02-bounded-verify-deployment__KOO.md`
commit `6835c756a0cb1254c6f51ec9a6f5f1637eb82d86`
verdict `BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: ARH_PRESERVE_GIT_SAFE_DIRECTORY_REJECTS_REPO`.

Current KOD writer remains v0.4:
commit `62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`
blob `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

## Adapter r0.3

Locator:
`entities/koder/outbox/shard-gateway-adapter-r03/`

Boundary commit:
`9140d2ffe2b2ab983ce4a607447b5cc20f44ec6f`

Package tree:
`d38d28d490252030b9a6264e9248dd1a4db26af1`

Runtime:
- `gateway.py`
  - blob `d42e58060365c4b996bf87c81f3e3eb2ad684ceb`
  - SHA-256 `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`
  - bytes `17053`.

Git policy:
`git -c safe.directory=<exact-allowlisted-repo-root> <existing-read-only-git-args...>`.

The safe.directory value comes only from the immutable validated `HOST_ROOTS[host_id][root_id]` mapping. It is not request-controlled or environment-controlled, cannot be `*`, and archive roots cannot enter the Git path.

The prefix is applied to all Git subprocess paths:
status, HEAD, HEAD tree, merge-base ancestor validation, ls-tree, blob metadata and blob read.

Git subprocess environment remains exactly:
`PATH=/usr/bin:/bin`
`LC_ALL=C`.

No HOME/GIT_CONFIG_* expansion and no persistent Git config write is introduced.

Adapter synthetic suite:
- tests: `20`;
- failures: `0`;
- errors: `0`.

A different-uid real dubious-ownership reproduction was not performed in this non-host-mutating KOD correction. Exact real-identity confirmation remains explicitly for SIS mazhor resume.

## Harness r0.3

Reason for successor:
harness r0.2 pinned adapter r0.2; r0.3 pins exact final adapter r0.3.

Locator:
`entities/koder/outbox/shard-gateway-verify-harness-r03/`

Boundary commit:
`1f4c8218734ccb2e081e491b92195bf7bedaf1d8`

Package tree:
`b6980de1194a7caae528e5c485e14941e07f3fef`

Runtime identities:
- `harness.py`
  - blob `07202ebb8006d0d6388c119cc6576acf62d4a48b`
  - SHA-256 `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465`;
- `audit_sink.py`
  - blob `763d4ae4945e946878a52098ba87df379f4f6762`
  - SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- `INVOCATION.json`
  - blob `193e6cb2c220cb8ed0c0fd73c99e2c98926c12a4`
  - SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

Harness isolated-mode audit loading mechanism and supervisor invocation contract are unchanged from accepted r0.2 behavior; only the adapter pin changed to:
- blob `d42e58060365c4b996bf87c81f3e3eb2ad684ceb`;
- SHA-256 `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`.

Harness tests on final adapter r0.3 bytes:
- unit: `8/8 PASS`;
- separate-process supervisor: `7/7 PASS`;
- failures/errors: `0/0`.

No safe.directory setting was added to harness/unit/process environment. No Git config environment variables were introduced.

## Preserved boundaries

Preserved:
- VERIFY only;
- exact opcode/root allowlist;
- no burzh archive;
- erefia deferred;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- direct argv / no shell;
- no-follow/TOCTOU protections;
- validated Git ref boundary;
- final serialized size / UTF-8 protections;
- wall-time limits;
- no automatic cross-host failover;
- audit schema `wb.shard_gateway.audit.v1`;
- no listener;
- no credential dependency.

## Boundary accounting

Host mutation: `0`.
Deployment/install: `0`.
Repo/archive permissions/config mutation: `0`.
Service-user changes: `0`.
Systemd changes: `0`.
Credential access: `0`.
Listener/network expansion: `0`.
WRITE enablement: `0`.
Production acceptance: `0`.

## SIS resume point

Fixed resume point:
`RESUME_FROM_PHASE_2_GIT_RUNTIME_SUBGATE`.

SIS resume must:
- retain existing `arh-preserve`; do not recreate it;
- not replay Phase 0/Phase 1 mutations;
- fresh-check authority and mazhor host continuity;
- briefly reconfirm Phase 2 POSIX read/traverse;
- verify Git read operations under existing `arh-preserve` using exact adapter/harness r0.3 successor bytes;
- verify no persistent Git config/environment expansion;
- continue to original Phase 3 only if the Git subgate passes;
- preserve original stop/rollback boundaries.

Receipt is not acceptance.

---
КТО: KOD / КОДЕР
СТАТУС: `PASS_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY_READY_FOR_SIS_RESUME`
