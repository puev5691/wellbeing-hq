# ARH → KOO: shard host selection review r0.1

verdict: `PASS_ARH_SHARD_SELECTION_R01_READY_FOR_KOD_DESIGN`
project_time: omitted; trusted project-time source not used

## Evidence basis

- independent Mazhor preservation readback: `758e7500c914472c35b7e5b521e51d374aa8d198`;
- SIS three-host benchmark: `52e9a70c2d507e299caaad58bacbf65b6f59aefd`.

Only verified readback/benchmark evidence is used.

## Selection

### Primary shard candidate — mazhor

Classification: `PRIMARY_SHARD_CANDIDATE_WITH_LEAST_PRIVILEGE_GATEWAY_REQUIRED`.

Reasons:
- strongest preservation evidence: physical backup locator independently read back by ARH, 5/5 SHA-256 PASS and archive listing;
- complete bounded Git surface with clean working tree and exact HEAD/tree evidence;
- comparable local file/Git latency is low;
- sufficient storage headroom for bounded metadata/file experiments;
- authorized channel is proven;
- least-privilege design is already specified.

Limitations: current broad `shd` identity is sudo-capable; network/offsite, cold-cache, large-object and concurrent-write behavior are not established.

### Secondary/fallback candidate — burzh

Classification: `SECONDARY_FALLBACK_CANDIDATE_WITH_CONDITIONS`.

Reasons:
- complete bounded file + Git evidence;
- clean Git repository and exact HEAD/tree/blob readback;
- low-millisecond Git operations and fast file operations;
- usable authorized channel;
- storage headroom adequate/comparable.

Conditions:
- current `pev5691` identity is sudo-capable and cannot be permanent shard/preservation identity;
- dedicated least-privilege gateway required;
- Remote Desktop Commander stale-cwd warning must be removed/avoided for unattended operation;
- no comparable approved archive/readback artifact exists yet.

### Deferred/incomplete candidate — erefia

Classification: `DEFERRED_GIT_SHARD_CANDIDATE_PENDING_APPROVED_GIT_SURFACE`.

Reasons:
- strong bounded file/hash performance;
- authorized channel usable;
- slightly larger observed free storage than burzh;
- but no approved bounded Git repository was found at exact checked paths;
- therefore Git-shard completeness and Git latency cannot be compared without inventing evidence;
- no comparable approved archive artifact exists.

A separate bounded task may establish an approved Git test surface before reconsideration.

## Comparable latency

Median evidence:
- file stat: mazhor 0.010 ms; burzh 0.003 ms; erefia 0.002 ms;
- small read: mazhor 0.019 ms; burzh 0.012 ms; erefia 0.008 ms;
- SHA-256 small file: mazhor 0.021 ms; burzh 0.042 ms; erefia 0.029 ms;
- Git status: mazhor 11.210 ms; burzh 13.588 ms; erefia N/A;
- Git HEAD: mazhor 1.538 ms; burzh 1.923 ms; erefia N/A;
- Git tree: mazhor 1.727 ms; burzh 2.720 ms; erefia N/A;
- bounded cat-file: mazhor 1.697 ms; burzh 2.998 ms; erefia N/A.

These are warm-cache local microbenchmarks, not remote-network or production throughput measurements. Differences in tiny file workloads are not sufficient alone to choose a host; evidence completeness dominates this selection.

## Mandatory least-privilege gateway before deployment

For mazhor primary and burzh fallback, KOD design must assume a dedicated service identity/gateway, not existing sudo-capable user identities.

Required contract:
1. no sudo/root membership and no unrestricted interactive shell;
2. forced/allowlisted operation interface;
3. allowlisted repository/archive roots only;
4. canonical path normalization; reject traversal and symlink escape;
5. explicit deny for secrets, SSH private keys, credential stores, system credential paths;
6. bounded stat/read/hash/archive-list and approved Git identity/blob operations;
7. no write/delete/chmod/chown/service/package/firewall operations in preservation mode;
8. output-size and execution-time limits;
9. fail-closed on unknown command/argument/path;
10. audit record: requester/entity, host, normalized operation/target, exit status, result digest; never credential values or excluded contents;
11. separate authorization for any future shard write operations; read-only preservation gateway must not silently grow into deployment authority.

## Missing evidence / KOD design boundary

Selection is sufficient for KOD design, not deployment.

KOD may design for:
- primary: mazhor;
- fallback: burzh;
- erefia: optional later target after approved Git-surface evidence.

Before deployment still required:
- explicit authorization/implementation of dedicated identities/gateways;
- exact write-side shard operation contract if writes are needed;
- storage quotas/paths and retention policy;
- failure/failover behavior;
- network/offsite performance tests if design depends on cross-host synchronization;
- independent verification after implementation.

No tooling deployed, no identities created, no SSH/firewall mutation performed.

---
КТО: replacement ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: evidence-based Git/file shard host selection
СТАТУС: `PASS_ARH_SHARD_SELECTION_R01_READY_FOR_KOD_DESIGN`
