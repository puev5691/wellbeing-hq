# SIS → ARH + KOO: burzh/erefia shard benchmark r0.1

verdict: `PASS_SIS_SHARD_BENCHMARK_R01_READY_FOR_SELECTION`
execution_mode: `FAST_PATH_READ_ONLY`
production_mutation: `false`
accounts_created: `false`
ssh_firewall_changed: `false`
unrestricted_root_used: `false`
secrets_private_keys_read: `false`
shard_tooling_deployed: `false`
git_write_fetch_push_reset: `false`
project_time: omitted; trusted project-time source not used

## Resume-First

fresh_HQ_HEAD: `178a7ec35a75c4d33f6f8e545c7c0b0fd5332c17`
prewrite_reconciliation_HEAD: `178a7ec35a75c4d33f6f8e545c7c0b0fd5332c17`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__shard-benchmark-r01__SIS.md`
commit `22feb9d604e428eb4a5170fe7a95f6f4c1e5ca75`.

Inbox placement:
commit `bdca89b2da53a8a2cdca00c00a26fe7f65cf1dd4`.

Mazhor comparison basis:
ARH commit `758e7500c914472c35b7e5b521e51d374aa8d198`,
verdict `PASS_ARH_MAZHOR_READBACK_R01_READY_FOR_SHARD_BENCHMARK`.

## Authorized device/host identity

### burzh
Remote Desktop Commander:
- device id: `dd09a197-f716-4dd6-80bb-7f8e5d8260ff`;
- device name: `ruvds-xnqc6`;
- observed online.

Fresh host facts:
- hostname: `ruvds-xnqc6`;
- user: `pev5691`;
- uid: `1000`;
- groups include `sudo`, therefore current execution identity is not acceptable as a permanent least-privilege shard/preservation identity;
- OS: `Ubuntu 24.04.4 LTS`;
- kernel: `Linux 6.17.0-1022-azure x86_64`;
- root filesystem: ext4;
- root filesystem use: approximately 34%;
- free blocks reported by df: approximately 25.75 GB.

### erefia
Remote Desktop Commander:
- device id: `c55d5659-f2c8-416d-8b40-9bac8c80c30d`;
- device name: `ruvds-ygo0w`;
- observed online.

Fresh host facts:
- hostname: `ruvds-ygo0w`;
- user: `pev5691`;
- uid: `1000`;
- groups include `sudo`, therefore current execution identity is not acceptable as a permanent least-privilege shard/preservation identity;
- OS: `Ubuntu 24.04.4 LTS`;
- kernel: `Linux 6.17.0-1022-azure x86_64`;
- root filesystem: ext4;
- root filesystem use: approximately 32%;
- free blocks reported by df: approximately 26.79 GB.

SIS did not invoke sudo/root on either host.

## Bounded approved/non-secret surfaces

No broad filesystem search was performed.

Common bounded project surface on both hosts:
`/data/wellbeing/obs/sysadmin/outbox/netcheck-0505/`

Observed test artifacts:
- burzh:
  `net_visibility_report_20260504_223836.md`, 9068 bytes;
- erefia:
  `net_visibility_report_20260505_004355.md`, 8710 bytes.

These existing sysadmin outbox artifacts were used only for stat/read/hash timing. Their contents were not reproduced into this result.

Bounded Git surface:
- burzh: `/home/pev5691/wellbeing-hq` exists and is a Git repository;
- erefia: no Git repository was present at the approved exact candidate paths checked for this task, including `/home/pev5691/wellbeing-hq` and the previously used wellbeing-lab repository path. SIS did not broaden the filesystem search.

No bounded approved archive artifact comparable to the Mazhor backup locator was identified on burzh/erefia within the allowed exact surfaces, therefore archive-list timing is `N/A` for these two hosts rather than inferred from unrelated files.

## Read-only latency evidence

Measurements are local host warm-cache microbenchmarks. Different small report sizes mean stat/read/hash values are operation-family comparisons, not byte-for-byte identical workloads.

| Operation, median | mazhor basis | burzh | erefia |
|---|---:|---:|---:|
| file stat | 0.010 ms | 0.003 ms | 0.002 ms |
| small file read | 0.019 ms | 0.012 ms | 0.008 ms |
| SHA-256 small file | 0.021 ms | 0.042 ms | 0.029 ms |
| archive list | 0.277 ms | N/A | N/A |
| git status --porcelain | 11.210 ms | 13.588 ms | N/A |
| git rev-parse HEAD | 1.538 ms | 1.923 ms | N/A |
| git rev-parse HEAD^{tree} | 1.727 ms | 2.720 ms | N/A |
| bounded git cat-file blob | 1.697 ms | 2.998 ms | N/A |

### burzh exact benchmark evidence
File:
`/data/wellbeing/obs/sysadmin/outbox/netcheck-0505/net_visibility_report_20260504_223836.md`

- size: 9068 bytes;
- SHA-256: `c457363a1b09a3cd131ffb9e17c670291d4ec9e77b94ebf1b66a0f703a3b7bd2`;
- stat n=20: min `0.003 ms`, median `0.003 ms`, max `0.012 ms`;
- read n=20: min `0.012 ms`, median `0.012 ms`, max `1.397 ms`;
- SHA-256 n=20: min `0.032 ms`, median `0.042 ms`, max `0.100 ms`.

Git:
`/home/pev5691/wellbeing-hq`

- porcelain status: empty;
- HEAD: `3dc4b4a2dba268905613f441c57a475478c6697e`;
- HEAD tree: `4a52cfa65d4079c24f680a78465bd9f0ed80da2f`;
- README blob: `3abde8a828bc6e688ec29cedc5d3286ecac153f6`;
- bounded blob read size: 1119 bytes;
- git status n=10: min `11.851 ms`, median `13.588 ms`, max `110.840 ms`;
- git HEAD n=10: min `1.697 ms`, median `1.923 ms`, max `2.373 ms`;
- git tree n=10: min `2.327 ms`, median `2.720 ms`, max `3.048 ms`;
- git cat-file n=10: min `2.296 ms`, median `2.998 ms`, max `5.701 ms`.

### erefia exact benchmark evidence
File:
`/data/wellbeing/obs/sysadmin/outbox/netcheck-0505/net_visibility_report_20260505_004355.md`

- size: 8710 bytes;
- SHA-256: `681e8850f9865b37269b339c821fc8af58e3e514d424bbfb21e8249c66e1bb3c`;
- stat n=20: min `0.002 ms`, median `0.002 ms`, max `0.008 ms`;
- read n=20: min `0.008 ms`, median `0.008 ms`, max `0.508 ms`;
- SHA-256 n=20: min `0.029 ms`, median `0.029 ms`, max `0.053 ms`.

No bounded approved Git repository was available at the exact checked paths, so Git timing is intentionally not fabricated.

## Tool/channel reliability

All requested read-only host commands used the already-authorized Remote Desktop Commander channels.

Observed:
- burzh command channel remained usable throughout identity, directory, stat/read/hash and Git checks;
- burzh shell emitted repeated stale-current-working-directory `getcwd` warnings inherited from the Remote Desktop Commander process environment; commands using absolute paths still executed correctly;
- erefia command channel executed the requested bounded checks without the same repeated cwd warnings;
- no command required privilege elevation;
- no host mutation was needed to complete the evidence collection.

The burzh cwd warning is an operational cleanliness issue, not a benchmark failure, but should be removed before using that channel as a long-lived automated worker.

## Classification

### mazhor
Existing ARH classification retained:
`SUITABLE_FOR_BOUNDED_SHARD_BENCHMARK_WITH_LEAST_PRIVILEGE_GATEWAY_CONDITION`.

Strengths:
- independently verified backup/archive locator;
- independently verified checksum/archive readback;
- healthy bounded Git surface;
- low local read/Git latency.

### burzh
Classification:
`SUITABLE_WITH_CONDITIONS`.

Evidence:
- authorized host/tool access is stable;
- bounded non-secret file operations are fast;
- clean bounded Git repository is available;
- Git identity/blob operations complete in low-millisecond range;
- storage headroom comparable to mazhor.

Conditions:
- current `pev5691` identity is sudo-capable and must not become the permanent shard/preservation identity;
- dedicated least-privilege gateway/identity remains required;
- Remote Desktop Commander stale-cwd warning should be repaired/avoided for unattended automation;
- no approved archive artifact was available, so archive readback is not independently compared with mazhor.

### erefia
Classification:
`SUITABLE_WITH_CONDITIONS`.

Evidence:
- authorized host/tool access is stable;
- bounded non-secret stat/read/hash operations are fast;
- storage headroom is slightly larger than burzh/mazhor in this snapshot;
- no privilege elevation required for the benchmark.

Conditions:
- current `pev5691` identity is sudo-capable and must not become the permanent shard/preservation identity;
- no bounded approved Git repository was available at the exact checked surfaces, so erefia is not yet evidence-complete for Git-shard selection;
- no approved archive artifact was available for archive readback comparison;
- before selecting erefia for a Git operational shard, a separate exact task must establish an approved bounded Git test surface without broad filesystem search or production mutation.

## Comparison inputs for selection

Evidence currently supports:
- `mazhor`: strongest preservation/archive evidence and complete bounded Git/file evidence;
- `burzh`: complete bounded Git/file evidence, but no comparable approved archive artifact and a minor tool-channel cwd hygiene issue;
- `erefia`: strong bounded file/storage evidence, but Git-shard evidence is incomplete because no approved Git surface was available.

SIS does not select or deploy a shard in this task. Selection remains a KOO/ARH downstream decision using these inputs.

## Boundary

No accounts were created.
No SSH/firewall policy was changed.
No unrestricted root was used.
No secrets/private keys were accessed.
No shard tooling was deployed.
No Git write/fetch/push/reset occurred.
No production/runtime mutation occurred.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: bounded burzh/erefia Git/file shard benchmark against mazhor baseline
СТАТУС: `PASS_SIS_SHARD_BENCHMARK_R01_READY_FOR_SELECTION`
