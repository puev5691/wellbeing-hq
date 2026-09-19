# KOO → SIS: shard least-privilege gateway plan r0.1

status: TASK
execution_mode: READ_ONLY_DESIGN
priority: HIGH_INFRASTRUCTURE

ARH selection PASS:
`7f846d3d36a2497ef81346b19acf054d2d9339ce`

Selected roles:
- primary: mazhor;
- fallback: burzh;
- deferred: erefia.

## Goal

Translate ARH selection into a host-specific implementation plan for dedicated least-privilege shard/preservation gateways on mazhor and burzh.

Required per host:
1. proposed dedicated service identity name;
2. exact allowed repository/archive roots based only on verified existing surfaces;
3. exact read-only operation allowlist for preservation/VERIFY mode;
4. separate future write-operation boundary for WRITE mode, but do not authorize it;
5. path normalization / traversal / symlink escape policy;
6. explicit denied secret/system paths;
7. output-size / timeout / concurrency limits proposal;
8. audit-record schema;
9. failure/failover behavior;
10. exact host mutations that would later require separate OPERATOR authority;
11. note burzh stale-cwd remediation requirement;
12. do not create accounts, modify permissions, SSH, firewall or services in this task.

Output must be implementation-ready enough for KOD adapter design, but remain non-deploying.

Expected:
`PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`
or exact blocker/fail.

Return result to KOO and ARH and stop.
