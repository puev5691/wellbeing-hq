# SIS → KOO: mazhor shard gateway r0.2 bounded VERIFY deployment terminal result

verdict: `BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: ARH_PRESERVE_GIT_SAFE_DIRECTORY_REJECTS_REPO`
execution_mode: `BOUNDED_MAZHOR_VERIFY_DEPLOYMENT`
production_acceptance: no
project_time: omitted; trusted project-time source not used

## Authority

OPERATOR authority:
`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

Authority record commit:
`0aadf1753e442ff792b2d43f402ad47ebeb984ee`.

Exact task:
`entities/koordinator/outbox/KOO__mazhor-gateway-r02-bounded-deploy__SIS.md`
commit `d1e777e1e29e2847100808fb518884451824dcee`
blob `a3b98d1afd25ddb8858496d7e87f0fc0dd2559f6`.

Fresh queue:
`entities/koordinator/current/KOO__active-queue-r56.md`
commit `79da806bdb35521de05b180bcdeb58732c8e691f`.

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

## Phase 0 — read-only predeploy

Target:
`mazhor` / `p552203.kvmvps`.

Verified:
- OS: Ubuntu 24.04.1 LTS;
- Python: `/usr/bin/python3`, Python 3.12.3;
- systemd tool: `/usr/bin/systemctl`;
- repo root exists: `/data/wellbeing-lab/repos/wellbeing-hq`;
- archive root exists: `/data/wellbeing-lab/backups/shd-pre-reinit-v01`;
- repo top-level state before mutation: mode 0775, owner/group `shd:shd`;
- archive top-level state before mutation: mode 0775, owner/group `shd:shd`;
- `wellbeing-shard-gateway-verify.service`: not found / inactive;
- no conflicting shard-gateway listener matched bounded listener check;
- `arh-preserve`: absent before Phase 1;
- exact deployment paths absent:
  - `/opt/wb-shard-gateway`;
  - `/run/wb-shard-gateway`;
  - `/var/lib/wellbeing/shard-gateway`;
  - `/var/log/wb-shard-gateway`.

The local mazhor checkout does not contain the pinned historical source commits, so runtime bytes cannot be sourced from that checkout. This is not the terminal blocker because exact immutable bytes remain available through the shared GitHub information field and no install phase was reached.

## Phase 1 — service identity

Created only:
`arh-preserve`.

Observed identity:
- uid: `999`;
- gid: `988`;
- groups: `988(arh-preserve)` only;
- passwd entry: `arh-preserve:x:999:988::/nonexistent:/usr/sbin/nologin`;
- no sudo/admin group;
- non-interactive shell: `/usr/sbin/nologin`;
- no credential material provisioned.

`shard-write` was not created.

## Phase 2 — mandatory read/traverse gate

POSIX filesystem access under `arh-preserve`:
- repo root read/traverse: PASS;
- archive root read/traverse: PASS;
- archive top-level listing under `arh-preserve`: PASS.

Additional exact runtime-relevant read test on the allowed repository root:

`sudo -u arh-preserve git -C /data/wellbeing-lab/repos/wellbeing-hq rev-parse HEAD`

Observed result:
`fatal: detected dubious ownership in repository at '/data/wellbeing-lab/repos/wellbeing-hq'`
with Git requiring a `safe.directory` exception.

Exit:
`128`.

This is a material deployment blocker because the exact gateway r0.2 exposes allowlisted Git read operations on this repository, but under the required service identity those operations fail before repository reads due to Git ownership safety policy.

The current authority explicitly forbids:
- chmod/chown/setfacl on the existing repo root;
- group changes on the existing repo root;
- credential/config improvisation outside the bounded design.

No attempt was made to bypass Git safety by changing the existing root, adding service-user Git config, expanding unit environment, or modifying adapter/harness bytes.

## Fail-closed stop

Execution stopped immediately after the access/runtime gate finding.

Not executed:
- Phase 3 gateway directory creation;
- Phase 4 runtime installation;
- Phase 5 unit artifact creation;
- Phase 6 systemd install;
- Phase 7 request creation;
- Phase 8 audit sink creation;
- Phase 9 smoke;
- Phase 10 post-smoke verification.

Therefore:
- installed runtime hashes: `NOT_APPLICABLE_NOT_INSTALLED`;
- unit artifact: `NOT_CREATED_DUE_TO_PREINSTALL_BLOCKER`;
- request hash: `NOT_CREATED`;
- service execution result: `NOT_RUN`;
- audit delta: `0 / audit sink not created`;
- unit state: `not-found / inactive`.

## Final host verification

Existing roots remained unchanged:
- repo: `0775 shd:shd`;
- archive: `0775 shd:shd`.

Deployment paths remain absent:
- `/opt/wb-shard-gateway`;
- `/run/wb-shard-gateway`;
- `/var/lib/wellbeing/shard-gateway`;
- `/var/log/wb-shard-gateway`.

`arh-preserve` remains present as the only bounded host mutation already completed before the blocker and is reversible.

No rollback was required by the Phase-2 stop condition; the authority explicitly permits already-created deployment-only state to remain reversible while the blocker is returned.

## Accounting

deployment runtime installed: `0`
systemd unit installed: `0`
smoke attempts: `0`
automatic retries: `0`
credential access/provisioning: `0`
network listener exposure: `0`
WRITE / shard-write: `0`
repo/archive/shard mutation: `0`
burzh mutation: `0`
erefia action: `0`
production acceptance: `no`

## Exact next causal requirement

KOO must route the blocker to the appropriate owner for an explicit design correction that makes Git read operations usable under `arh-preserve` without mutating existing repo/archive permissions and without silently expanding the service environment/config authority.

Possible solution class must be explicitly designed and re-reviewed before SIS resumes Phase 3. No solution is chosen by SIS in this terminal result.

## Terminal result

`BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: ARH_PRESERVE_GIT_SAFE_DIRECTORY_REJECTS_REPO`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: bounded mazhor shard gateway r0.2 VERIFY deployment
СТАТУС: exact blocker before runtime installation
