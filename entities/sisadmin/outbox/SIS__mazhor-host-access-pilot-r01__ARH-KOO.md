# SIS → ARH + KOO: mazhor host-access pilot r0.1

verdict: `PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK`
production_mutation: `false`
firewall_ssh_policy_changed: `false`
unrestricted_root_granted: `false`
secrets_private_keys_read: `false`
burzh_erefia_benchmarked: `false`
shard_tooling_deployed: `false`
project_time: omitted; trusted project-time source not used

## Resume-First

fresh_HQ_HEAD: `be0a3f67eecc59f9036cae85dee34f7349b4218f`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact KOO task:
`entities/koordinator/outbox/KOO__mazhor-host-access-pilot-activate-r01__SIS.md`
commit `1594c534200fcebd94467f51a3d6094f37bcdbab`.

SIS inbox placement:
commit `4328bee5907fc994c22f731cae04908714afa26f`.

ARH basis:
commit `9b147fac4b80431ec4ed24f28efc2cb775326d8e`.

## Fresh mazhor access/runtime facts

Authorized Remote Desktop Commander device:
- device id: `830038a0-232b-4d83-b52d-0e9973126165`;
- device name: `p552203.kvmvps`;
- observed status: `online`;
- app version: `0.2.50`.

Fresh host readback:
- hostname: `p552203.kvmvps`;
- effective user: `shd`;
- uid: `1000`;
- OS: `Ubuntu 24.04.1 LTS`;
- kernel: `Linux 6.8.0-51-generic x86_64`;
- root filesystem: `ext4`;
- root filesystem usage at readback: approximately 14%.

The current SIS tool channel executes as existing user `shd`. Historical host-state shows that user is in the sudo group, therefore this identity is NOT accepted as the future least-privilege ARH preservation identity. SIS did not use sudo or root for this pilot.

## Known locator physical readback

Exact locator:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

Fresh stat:
- exists: `true`;
- type: directory;
- mode: `0775`;
- owner/group: `shd:shd`.

Top-level composition observed:
- `README.md`, 548 bytes;
- `host-state.txt`, 3728 bytes;
- `lab-tree.txt`, 4533 bytes;
- `repo-state.txt`, 328 bytes;
- `lab-workfiles.tar.gz`, 920 bytes;
- `sha256sums.txt`, 404 bytes.

README explicitly states the backup is non-secret preservation state and excludes:
- `/data/wellbeing-lab/secrets`;
- `/data/wellbeing-lab/logs`;
- `/data/wellbeing-lab/tmp`;
- `/data/wellbeing-lab/backups` from the archived workfile payload;
- Git object database from the archive payload.

SIS did not traverse or read the excluded secret/private-key surfaces.

## Integrity/readback

Fresh `sha256sum -c sha256sums.txt`:
- README.md: `OK`;
- host-state.txt: `OK`;
- lab-tree.txt: `OK`;
- repo-state.txt: `OK`;
- lab-workfiles.tar.gz: `OK`.

Fresh independently observed hashes:
- README.md: `b45563fdccde8b5c2c023c09e42395e60be504d3f3d62ea48522acde2346fa24`;
- lab-workfiles.tar.gz: `a2854f299dd42cff0175d947a148b952861fbfbe9508c87e988e26cb496c880c`.

Small archive readback with `tar -tzf` succeeded. Observed members:
- `reports/`;
- `reports/LAB01_MARKER.txt`;
- `reports/host_inventory.txt`;
- `scripts/`;
- `artifacts/`.

Archive was listed only; no extraction or mutation occurred.

## Fresh local Git readback

Repository:
`/data/wellbeing-lab/repos/wellbeing-hq`

Fresh current state:
- working tree porcelain status: empty;
- HEAD: `22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`;
- HEAD tree: `c4607f6a85effc771fb7c9d32da92ed66d0bdf8b`;
- README.md blob used for bounded blob readback: `3abde8a828bc6e688ec29cedc5d3286ecac153f6`;
- blob readback size: 1119 bytes.

The repository current HEAD is newer than the preserved `repo-state.txt` snapshot, which records historical HEAD `6c5bbfc1f54ce7b66463d71d9326075de60d9774`. This is not treated as corruption; the backup is explicitly a pre-reinit state snapshot.

## Baseline latency evidence

All measurements are local on mazhor, read-only, and mostly warm-cache microbenchmarks. They are a baseline, not network/offsite throughput claims.

File operations:
- stat README.md, n=20: min `0.010 ms`, median `0.010 ms`, max `0.048 ms`;
- read README.md, n=20: min `0.018 ms`, median `0.019 ms`, max `0.034 ms`;
- SHA-256 README.md, n=20: min `0.020 ms`, median `0.021 ms`, max `0.047 ms`;
- SHA-256 lab-workfiles.tar.gz, n=10: min `0.021 ms`, median `0.024 ms`, max `0.364 ms`;
- archive member listing, n=10: min `0.255 ms`, median `0.277 ms`, max `0.951 ms`.

Git operations:
- `git status --porcelain`, n=10: min `10.714 ms`, median `11.210 ms`, max `24.477 ms`;
- `git rev-parse HEAD`, n=10: min `1.476 ms`, median `1.538 ms`, max `1.642 ms`;
- `git rev-parse HEAD^{tree}`, n=10: min `1.666 ms`, median `1.727 ms`, max `1.764 ms`;
- `git cat-file blob <README blob>`, n=10: min `1.640 ms`, median `1.697 ms`, max `1.751 ms`.

## Least-privilege ARH preservation channel design

The existing `shd` account is suitable for SIS-administered pilot readback but is too broad for permanent ARH access because it is sudo-capable.

Required future ARH channel should use a dedicated identity, proposed logical role:
`arh-preserve`.

Properties:
- no sudo membership;
- no unrestricted interactive root;
- no access to secret/private-key paths;
- only read operations through a forced/allowlisted gateway;
- no general shell authority from the preservation channel.

Initial allowlisted filesystem surface:
- `/data/wellbeing-lab/backups/shd-pre-reinit-v01/**`;
- bounded read-only Git metadata queries against `/data/wellbeing-lab/repos/wellbeing-hq`.

Explicitly denied surfaces:
- `/data/wellbeing-lab/secrets/**`;
- SSH private keys and credential stores;
- system credential directories;
- arbitrary `/etc`, `/root`, runtime secrets;
- writes, deletes, chmod/chown, package/service/firewall operations.

Initial allowlisted preservation operations:
- stat / metadata read;
- bounded file read of approved preservation artifacts;
- SHA-256 calculation;
- `sha256sum -c` against an approved manifest in the allowlisted locator;
- archive listing with `tar -tzf` without extraction;
- `git status --porcelain`;
- `git rev-parse HEAD`;
- `git rev-parse HEAD^{tree}`;
- `git cat-file blob <verified blob>` with output-size bound.

Not allowed by this pilot:
- arbitrary shell;
- `sudo`;
- archive extraction;
- Git mutation/fetch/push/checkout/reset;
- arbitrary recursive filesystem scans outside allowlist;
- service/process/network/firewall mutation.

## Audit / logging / failure mode

Recommended gateway contract for the next implementation task:
- each invocation records requester/entity, host, allowlisted operation, normalized target path, exit status and result digest;
- never log credential values, private-key material or excluded file contents;
- reject path traversal/symlink escape outside allowlisted roots;
- reject unknown command/argument shapes fail-closed;
- read/output size limits;
- timeout per operation;
- no retry on mutation because mutations are not allowed;
- if gateway/locator/version cannot be verified, return blocker and do not widen access.

## Suitability for Git/file operational-shard benchmarking

`mazhor` is suitable as the first local Git/file benchmark host:
- host is freshly reachable through the authorized tool channel;
- known preservation locator physically exists and passes checksum readback;
- local Git repo is healthy/clean at readback;
- file/hash/archive/Git operations are low-latency in the measured local warm-cache baseline;
- the host has sufficient free root filesystem capacity for bounded metadata/file experiments.

Limitations:
- these measurements do not establish remote-network latency, cold-cache I/O, large-object throughput, concurrent write behavior, or offsite durability;
- burzh/erefia were intentionally not benchmarked;
- no Git shard tooling was deployed.

## Pilot conclusion

Physical mazhor readback is real and verified. The locator and local Git/file surfaces are technically suitable for the next ARH preservation readback and later bounded benchmark work.

This PASS means `READY_FOR_ARH_READBACK`, not `ARH_UNRESTRICTED_HOST_ACCESS_OPERATIONAL`.

A dedicated least-privilege ARH identity/gateway has not been installed because that would be a new host authorization/mutation step beyond this read-only pilot. No OPERATOR action is required to accept this pilot result; implementation of the dedicated ARH channel should arrive as a separate exact task after ARH independent readback/review.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: bounded mazhor preservation access/readback pilot and baseline latency evidence
СТАТУС: `PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK`
