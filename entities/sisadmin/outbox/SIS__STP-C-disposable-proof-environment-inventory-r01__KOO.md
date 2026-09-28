# SIS → KOO: STP-C disposable proof environment inventory r0.1

terminal: BLOCKED_SIS_STP_C_DISPOSABLE_PROOF_ENVIRONMENT_INVENTORY_R01_NO_VERIFIED_DISPOSABLE_ENVIRONMENT_AND_ROOT
status: BOUNDED_READ_ONLY_INVENTORY_COMPLETE
scope: M5_M6_ONLY
project_time: omitted

## 0. Human result

Fresh read-only inventory found three remotely reachable Linux VMs.

Two are clearly unsuitable for destructive/disposable proof use without separate decommission/reallocation authority because live/project workloads and project data are present.

The third VM is cleaner and may be a future candidate, but its disposable status is NOT proven: it already contains project/lab repositories, backups, secrets and a shard-gateway installation on the same root filesystem.

No dedicated STP-C disposable proof storage root exists on any inspected environment.

Therefore:

M5 = BLOCKED
M6 = BLOCKED

Exact blockers:

M5:
NO_VERIFIED_DISPOSABLE_ENVIRONMENT

M6:
ROOT_NOT_CREATED_AND_NO_ISOLATED_STORAGE_BOUNDARY

T01-T20 executed now:
0

The existing execution-envelope blocker remains active.

## 1. Exact basis

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Exact authority:

puev5691/wellbeing-hq@a3c526d6cbc76106badadd97c9770942772ef4ff:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-disposable-proof-environment-inventory-r01__OPERATOR.md

Exact task:

puev5691/wellbeing-hq@4ce02e15f19e002655222dfe67f4ccbcd95b31d1:
entities/koordinator/outbox/KOO__STP-C-disposable-proof-environment-inventory-r01__SIS.md

Exact execution-envelope blocker:

puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:
entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md

blob:
875fb2f2365fdd62d4a7ae5207bb51d35304fa43

Exact independently accepted common corpus:

puev5691/wellbeing-hq@5c3ad41e0fd762cb1eaaaf31eb1554e9b87c3183:
entities/sisadmin/outbox/SIS__STP-C-common-proof-corpus-M11-M15-independent-review-r01__KOO.md

M11 = PASS
M12 = PASS
M13 = PASS
M14 = PASS
M15 = PASS

## 2. Fresh access boundary

Fresh Remote Desktop Commander inventory exposed three devices under the same authenticated connector principal.

Provider/account ownership beyond that connector boundary was not independently proven and remains UNKNOWN.

No new host-access authority was requested.

Fresh reachable devices:

1. ruvds-ygo0w
   device id:
   c55d5659-f2c8-416d-8b40-9bac8c80c30d

2. ruvds-xnqc6
   device id:
   dd09a197-f716-4dd6-80bb-7f8e5d8260ff

3. p552203.kvmvps
   device id:
   830038a0-232b-4d83-b52d-0e9973126165

All inspection commands were read-only.

No file/directory/package/network/storage mutation was performed.

## 3. Environment A — ruvds-ygo0w

### Identity

hostname:
ruvds-ygo0w

machine-id:
4423b8fffd7e4fab9cebf830a33420e0

OS:
Ubuntu 24.04.4 LTS

kernel:
Linux 7.0.0-1014-azure

architecture:
x86_64

virtualization:
Microsoft full VM

container layer:
Desktop Commander reports not Docker/not container.

Current OS user:
pev5691
uid 1000
groups include sudo.

Provider-level owner/control principal:
UNKNOWN

### Capacity observed

CPU:
1 vCPU
Intel Xeon Gold 6244

RAM total:
1,965,785,088 bytes

RAM available at observation:
748,220,416 bytes

swap:
1,073,737,728 bytes

disk:
40G virtual disk
/dev/sda1 ext4 mounted at /

filesystem capacity:
42,090,168,320 bytes

filesystem available:
25,860,960,256 bytes

### Network boundary

Public IPv4 observed:
194.87.107.135/24

default route:
via 194.87.107.1

Inbound/listening services observed include:
- 80/tcp
- 2222/tcp
- 8780/tcp
- 8781/tcp
- 30000/tcp

Outbound routing exists via default route.
Actual unrestricted internet egress was not separately tested.

### Project/live data and workload

Freshly verified:

/data/wellbeing exists.

Running services include:
- nginx.service
- ssh.service
- wbn-tera2-node.service

Node processes are listening on project-relevant public ports.

Conclusion:

This VM is NOT admissible as disposable proof environment from current evidence.

Destroy/reimage/reset would risk live/project workload.

M5 candidate status:
REJECTED_AS_CURRENT_DISPOSABLE_CANDIDATE

## 4. Environment B — ruvds-xnqc6

### Identity

hostname:
ruvds-xnqc6

machine-id:
4423b8fffd7e4fab9cebf830a33420e0

boot-id:
f51063444c954748b7f91b03a32420cd

OS:
Ubuntu 24.04.4 LTS

kernel:
Linux 6.17.0-1022-azure

architecture:
x86_64

virtualization:
Microsoft full VM

container layer:
Desktop Commander reports not Docker/not container.

Current OS user:
pev5691
uid 1000
groups include sudo.

Provider-level owner/control principal:
UNKNOWN

### Capacity observed

CPU:
1 vCPU
Intel Xeon Gold 6128

RAM total:
1,972,895,744 bytes

RAM available at observation:
103,006,208 bytes

swap:
1,073,737,728 bytes

disk:
40G virtual disk
/dev/sda1 ext4 mounted at /

filesystem capacity:
42,090,168,320 bytes

filesystem available:
25,520,144,384 bytes

### Network boundary

Public IPv4 observed:
185.39.19.240/24

default route:
via 185.39.19.1

Inbound/listening services observed include:
- 80/tcp
- 2222/tcp
- 8780/tcp
- 8781/tcp
- 30000/tcp
- 18081/tcp on loopback

Outbound routing exists via default route.
Actual unrestricted internet egress was not separately tested.

### Project/live data and workload

Freshly verified:

/data/wellbeing exists.

/opt contains:
- wb-oss-sandbox
- wellbeing

/home/pev5691 contains multiple project repositories/staging/recovery artifacts.

Running services include:
- nginx.service
- ssh.service
- wb-oss-sandbox.service
- wbn-tera2-node.service

Conclusion:

This VM is NOT admissible as disposable proof environment from current evidence.

Destroy/reimage/reset would risk live/project workload and evidence.

M5 candidate status:
REJECTED_AS_CURRENT_DISPOSABLE_CANDIDATE

## 5. Environment C — p552203.kvmvps

### Identity

hostname:
p552203.kvmvps

machine-id:
a02d3b6f67f89a3239bdca5a7776a8f4

boot-id:
0e10636229324c4fa8e6074d906c3ef4

OS:
Ubuntu 24.04.1 LTS

kernel:
Linux 6.8.0-51-generic

architecture:
x86_64

virtualization:
full VM; systemd-detect-virt reports microsoft
hardware model reports QEMU Standard PC Q35.

container layer:
Desktop Commander reports not Docker/not container.

Current OS user:
shd
uid 1000
groups include sudo.

Provider-level owner/control principal:
UNKNOWN

### Capacity observed

CPU:
1 vCPU
AMD EPYC-Rome Processor

RAM total:
2,063,708,160 bytes

RAM available at observation:
1,289,654,272 bytes

swap:
0

disk:
30G virtual disk
/dev/sda1 ext4 mounted at /

filesystem capacity:
31,618,584,576 bytes

filesystem available:
25,339,666,432 bytes

### Network boundary

Public IPv4 observed:
130.49.174.162/24

default route:
via 130.49.174.254

Inbound/listening services observed:
- 22/tcp
- local resolver only otherwise

No backend/project service listener was observed in this bounded snapshot.

Outbound routing exists via default route.
Actual unrestricted internet egress was not separately tested.

### Existing project/lab material

/data/wellbeing does not exist.

But /data/wellbeing-lab exists and contains:

- artifacts
- backups
- logs
- reports
- repos
- scripts
- secrets
- tmp

and specifically:
- /data/wellbeing-lab/repos/wellbeing-hq
- /data/wellbeing-lab/backups/shd-pre-reinit-v01

/opt/wb-shard-gateway exists and contains gateway/harness/audit files.

Both /data/wellbeing-lab and /opt/wb-shard-gateway resolve to the same root filesystem:

/dev/sda1
ext4
mounted at /

No existing path matching an STP-C/proof root was found under the bounded inspected locations.

### Disposable conclusion

This is the strongest future candidate of the three because no current backend/project service listener was observed.

However:

- project/lab repository data exists;
- backups exist;
- a secrets directory exists;
- shard-gateway files exist;
- all are on the same filesystem as OS;
- no provider/reimage statement proves that destroying this VM would not lose required project evidence or functionality.

Therefore read-only evidence is insufficient to declare this VM disposable.

M5 candidate status:
BLOCKED_PENDING_EXPLICIT_DISPOSABLE_DESIGNATION_AND_DATA_DISPOSITION

## 6. M5 verdict

M5 = BLOCKED

Reason:

NO_VERIFIED_DISPOSABLE_ENVIRONMENT

The available hosts can be identified exactly, but none can currently satisfy the required statement:

"may be destroyed/reimaged/reset without affecting live/project workloads or required project data"

from read-only evidence alone.

Minimum next evidence/authority:

1. OPERATOR/KOO explicit designation of one exact host/VM as disposable for STP-C proof;
2. explicit disposition/preservation rule for any existing data on that VM;
3. confirmation that no live project dependency relies on that VM;
4. separate mutation authority for future reset/root creation after designation.

No host was mutated here.

## 7. M6 storage-root inventory

### ruvds-ygo0w

Root storage:
/dev/sda1 ext4 mounted /

/data/wellbeing is present on that same filesystem.

No dedicated verified STP-C destructive storage root exists.

Status:
ROOT_NOT_CREATED

### ruvds-xnqc6

Root storage:
/dev/sda1 ext4 mounted /

/data/wellbeing and other project artifacts exist on that same filesystem.

No dedicated verified STP-C destructive storage root exists.

Status:
ROOT_NOT_CREATED

### p552203.kvmvps

Root storage:
/dev/sda1 ext4 mounted /

Existing:
/data/wellbeing-lab

But this path is NOT a disposable candidate root because it contains repositories, backups, secrets and other lab material.

No existing STP-C/proof root was found in the bounded search.

Status:
ROOT_NOT_CREATED

### Isolation consequence

All three inspected VMs expose one main ext4 root device for the observed persistent storage.

Therefore filesystem-device isolation between:
- destructive candidate storage
and
- OS/project/evidence storage

is NOT currently established.

Directory-level isolation could be designed later, but it cannot prove device-level isolation for destructive storage-corruption tests.

For the first tranche T01/T02/T03/T04/T10/T12, directory-level separation may be sufficient in a separately approved disposable VM because these tests do not require raw storage corruption.

That is a future design/authority question, not a PASS for M6.

## 8. M6 verdict

M6 = BLOCKED

Exact reason:

ROOT_NOT_CREATED_AND_NO_ISOLATED_STORAGE_BOUNDARY

Required future mutation authority:

After one exact VM is separately designated disposable, authorize creation of:

1. one dedicated candidate-data root for STP-C proof;
2. one separately located evidence/corpus root not subject to candidate destructive cleanup;
3. exact ownership/permissions;
4. exact reset/cleanup semantics;
5. explicit proof that neither root contains or overlays live/project data.

No path is invented before that authority.

For storage-corruption/power-loss tranches, a separate disposable device/VM or independent evidence host may be required because the observed VMs use one root block device.

## 9. Dependency consequences

### M1-M4 exact packages/builds

All three currently inspected hosts are:

- Ubuntu 24.04 family
- x86_64

Therefore future build pinning can target only exact Linux x86_64 artifacts compatible with the specifically selected Ubuntu 24.04 host unless a different environment is separately authorized.

Observed OS versions differ:
- ruvds-ygo0w: Ubuntu 24.04.4
- ruvds-xnqc6: Ubuntu 24.04.4
- p552203.kvmvps: Ubuntu 24.04.1

No package format is selected.
Future candidates may use exact official x86_64 packages/binaries only after exact build pinning.

### M7-M10 adapters

Fresh runtime observations:

ruvds-ygo0w:
- Python 3.12.3
- Node.js 22.23.2

ruvds-xnqc6:
- Python 3.12.3
- Node.js 22.23.2

p552203.kvmvps:
- Python 3.12.3
- Node.js 22.23.2

No Docker/container runtime boundary is currently provided by Desktop Commander inventory.

Therefore future adapter design may target these available runtimes, but adapter implementation/version remains separate.

Candidate-specific native client libraries are NOT yet installed/pinned by this task.

### M16 topology/config physical boundary

Fresh physical observation:

each VM has:
- 1 vCPU;
- one root virtual disk;
- approximately 2 GB RAM.

No VM/container creation is authorized.

Therefore:
- one distinct OS VM per inspected host is currently available;
- no multi-node disposable topology is proven;
- multiple processes on one VM would not prove host-failure independence;
- maximum safe candidate node/member count is UNKNOWN until an exact disposable environment and resource allocation are approved.

### M17 evidence root

Current answer:
NOT ESTABLISHED.

All persistent paths observed on each VM resolve to the same main root device.

Directory-level evidence separation is possible in principle but not yet created or authorized.

For destructive storage tests, evidence must live outside the destructive candidate device/root.

Potential future classes:
- separate device;
- separate disposable VM/supervisor;
- immutable external publication after local staging.

No concrete locator is selected here.

### M18 capacity ceilings

Observed host capacities provide only physical upper bounds, not safe test allocations.

ruvds-ygo0w:
- 1 vCPU
- 1,965,785,088 bytes RAM total
- 748,220,416 bytes available at observation
- 25,860,960,256 bytes filesystem available

ruvds-xnqc6:
- 1 vCPU
- 1,972,895,744 bytes RAM total
- 103,006,208 bytes available at observation
- 25,520,144,384 bytes filesystem available

p552203.kvmvps:
- 1 vCPU
- 2,063,708,160 bytes RAM total
- 1,289,654,272 bytes available at observation
- 25,339,666,432 bytes filesystem available

No future CPU/RAM/disk limit is selected from these raw ceilings because:
- two hosts carry live workloads;
- the third is not yet proven disposable;
- backend footprints are not pinned.

## 10. First-tranche preservation

Proposed future first tranche remains:

T01
T02
T03
T04
T10
T12

Executed now:
0

No backend was installed or started.

No package was downloaded.

No VM/container/root was created.

## 11. Exact next blocker

The shortest causal next step is NOT backend installation.

It is an explicit disposable-environment designation decision.

Minimum decision payload:

- exact VM/device identity;
- statement that it may be reset/destroyed for STP-C proof;
- disposition/preservation of existing data on that VM;
- statement that no live project workload depends on it;
- later bounded authority to create isolated candidate/evidence roots.

Until then:

M5 = BLOCKED
M6 = BLOCKED

## 12. Hard boundaries preserved

No:
- backend install/run;
- package download/install;
- VM/container creation;
- storage-root creation;
- mount/unmount;
- host/network mutation;
- T01-T20 execution;
- backend selection;
- live storage;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- profile/Fast Gate/Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → найти уже существующую лабораторную среду, не создавая новую и не трогая работающие узлы.

Проба → свежо проверить три реально доступные VM одинаковым read-only профилем и отдельно посмотреть storage/mount/project-data boundary.

Результат → два узла явно live; третий чище, но содержит лабораторные repos/backups/secrets и не имеет отдельного proof root.

Неудача → M5/M6 нельзя честно закрыть одним фактом "сервер свободнее остальных".

Урок → disposable — это не характеристика пустоты процесс-листа. Это разрешение потерять среду целиком без ущерба чему-либо важному.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
