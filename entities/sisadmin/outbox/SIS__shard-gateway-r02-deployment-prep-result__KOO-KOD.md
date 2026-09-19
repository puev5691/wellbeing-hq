# SIS → KOO + KOD: shard gateway r0.2 deployment preparation terminal result

verdict: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`
execution_mode: `BOUNDED_DESIGN_DEPLOYMENT_PREPARATION`
deployment_performed: 0
host_mutation_performed: 0
credential_access: 0
production_acceptance: 0
project_time: omitted; trusted project-time source not used

## Resume-First

Fresh HQ HEAD at preparation start:
`8806bdc0c92b6507eb78c177e681dc77b5eb5fc7`.

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Exact task:
`entities/koordinator/outbox/KOO__shard-gateway-r02-deployment-prep__SIS.md`
commit `7f68933d779fa553911f6879157e47d77f19562d`
blob `80eb50997fa7da0a3fbb10a88f94d196ef20fcbf`.

## Unchanged exact r0.2 identity

Adapter locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`.

Boundary commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`.

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`.

SIS independent reverify PASS:
`ed56678fb190c278440aa2bcfa83a258d54daf27`.

ARH preservation/read-only PASS:
`36b1c3c5c823358e9e32a14a9102d556be431265`.

No r0.2 byte was changed.

## Deployment-preparation package

Locator:
`entities/sisadmin/outbox/shard-gateway-r02-deployment-prep/`.

Sealing commit:
`7f8c093f70da0d3f9f8ac6d631bc7a77cb1fad97`.

Package subtree:
`939fc1eba4661aa0cdcb22d8ed70ea9d12637dfc`.

Composition:
8 files.

Exact prep artifact blobs:
- `AUDIT-RETENTION-PLAN.md` → `c2b9d1af06ebc54205ba285d49201fd9a1247ca8`
- `CREDENTIAL-BOUNDARY.md` → `ee25ced9f44cdb1121d3205b87600790353588bf`
- `DEPLOYMENT-PLAN.md` → `28f35ba20c0cbe825da352b6750680d507db7448`
- `DEPLOYMENT-PREP-MANIFEST.md` → `0907954c6382e5e6fffb09eeb3683a167082b723`
- `MUTATION-AUTHORITY-GATE.md` → `fda538e92d8539d5624753d0ab3061b3299e17c1`
- `PERMISSIONS-MATRIX.md` → `c4d6b951f55489e2f235d01783d6c5f2088e76d4`
- `PREDEPLOY-CHECKLIST.md` → `19b10fea323d5aeadcf90865c24700d9fac24cc0`
- `SERVICE-UNIT-CANDIDATE.md` → `19b3c16cf7c9a6ea923a90f50232b6e990576928`

## Architecture summary

Primary future deployment:
`mazhor`.

Fallback future deployment:
`burzh`, only as a separate explicitly authorized step; no automatic failover.

Deferred:
`erefia`.

Read-only identity:
`arh-preserve`.

Future WRITE identity:
`shard-write`, reserved only.

Verified roots remain unchanged:
- mazhor repo `/data/wellbeing-lab/repos/wellbeing-hq`;
- mazhor archive `/data/wellbeing-lab/backups/shd-pre-reinit-v01`;
- burzh repo `/home/pev5691/wellbeing-hq`;
- no burzh archive;
- no erefia mapping.

## Bounded read-only host observations

mazhor:
- host `p552203.kvmvps`;
- current interactive identity `shd`, sudo-capable;
- Python 3.12.3 at `/usr/bin/python3`;
- systemd tooling present;
- `arh-preserve` absent;
- repo top-level mode 0775 owner/group `shd:shd`;
- archive top-level mode 0775 owner/group `shd:shd`;
- proposed gateway /opt, /etc and audit directories absent.

burzh:
- host `ruvds-xnqc6`;
- current interactive identity `pev5691`, sudo-capable;
- Python 3.12.3 at `/usr/bin/python3`;
- systemd tooling present;
- `arh-preserve` absent;
- repo top-level mode 0775 owner/group `pev5691:pev5691`;
- proposed gateway /opt, /etc and audit directories absent;
- Remote Desktop Commander stale-cwd/getcwd warning persists;
- no matching shard/wellbeing listener observed;
- unrelated disabled `wellbeing-telegram-phase1b-sandbox.service` observed and left untouched.

No secret-like environment variable names were observed in the bounded shell-name check; values were not read.

## Exact blocker found during preparation

The immutable r0.2 package is not itself a deployable service/CLI package.

It contains the verified gateway library and tests, but no executable request-processing entrypoint, no persistent/one-shot invocation contract suitable for supervision, and no audit-sink persistence harness.

Therefore the task requirement to provide a truthful functional exact `ExecStart` cannot be satisfied from unchanged r0.2 bytes.

`/usr/bin/python3 /opt/wellbeing/shard-gateway/r02/gateway.py`
is explicitly NOT accepted as a service command because the module only defines the adapter and exits; it does not process gateway requests.

The audit serializer exists, but a fail-closed append-only audit sink is not implemented by the r0.2 package.

This is a deployment-integration/code packaging blocker. Per task boundary, SIS did not modify r0.2.

## UNKNOWN_REQUIRES_PREDEPLOY_CHECK

- recursive effective read/traverse permissions for future `arh-preserve` on each exact root;
- burzh stale-cwd root cause and clean unattended working-directory behavior;
- exact future audit sink implementation and permissions;
- future systemd service environment after a real harness exists;
- exact rollback behavior of future installed harness/unit after authority;
- optional sandbox/bind-mount model if chosen.

Additionally:
`execution_harness_identity = BLOCKED_REQUIRES_KOD_SUCCESSOR`.

## Future mutation classes requiring OPERATOR decision

After the harness blocker is closed, separate explicit human authority remains required for:
1. create `arh-preserve` on mazhor, then separately burzh;
2. any ACL/chmod/chown/group changes;
3. create executable/config/working/audit directories;
4. install exact adapter and execution-harness bytes;
5. install/enable supervisor/systemd unit;
6. audit directory/permissions/retention;
7. optional sandbox/bind/chroot/container setup;
8. any SSH forced-command design if later chosen;
9. any firewall change if later listener is designed;
10. any listener/socket exposure;
11. any credential provisioning;
12. any `shard-write` / WRITE mode;
13. fallback deployment/replication activation.

Baseline design does NOT require SSH forced-command, firewall mutation, listener exposure, credentials, WRITE or replication.

## Boundary accounting

deployment: `0`
host mutation: `0`
credential access: `0`
production acceptance: `0`
WRITE enablement: `0`
listener exposure: `0`
repository/archive/shard mutation: `0`

## Next causal gate only

Required next owner:
KOD / КОДЕР.

Required bounded task:
design and publish an immutable non-network VERIFY execution/audit harness for the exact r0.2 adapter, preserving all existing read-only boundaries.

Expected successor must make it possible to define:
- exact request input;
- exact `Gateway.execute` invocation;
- canonical result output;
- fail-closed `wb.shard_gateway.audit.v1` sink behavior;
- exact process exit semantics;
- no credential inheritance;
- no listener by default;
- no WRITE;
- truthful exact supervisor `ExecStart`.

Only after independent verification of that successor should KOO form an OPERATOR host-mutation/deployment decision gate.

## Terminal result

`REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: bounded deployment preparation of exact shard gateway adapter r0.2
СТАТУС: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`
