# KOO → ARH: independent mazhor preservation readback/review r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

## SIS pilot result

Commit:
`b7081ab521953206ac60b4bbaae9b83c27783a7b`

Verdict:
`PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK`

Known locator:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

## Goal

Independently review SIS evidence and, through currently authorized read-only means available to ARH, confirm the preservation locator/readback boundary needed for future operational shard design.

Required:
1. verify exact SIS terminal result identity;
2. verify locator identity and preserved artifact inventory from fresh/authorized evidence;
3. verify checksum/readback evidence where ARH can independently observe it;
4. confirm excluded secret/private-key surfaces remain outside preservation scope;
5. review proposed least-privilege `arh-preserve` gateway contract;
6. identify any missing boundary before a dedicated preservation identity/gateway may be implemented;
7. classify mazhor as:
   - suitable for bounded shard benchmark;
   - suitable with conditions;
   - not suitable;
8. define exact next benchmark/readback step for burzh/erefia without executing it in this task.

Do not:
- request unrestricted root;
- create accounts;
- mutate SSH/firewall;
- deploy shard tooling;
- access excluded secret paths;
- benchmark burzh/erefia yet.

Expected:
`PASS_ARH_MAZHOR_READBACK_R01_READY_FOR_SHARD_BENCHMARK`
or exact blocker/fail.

Return result to KOO through Exchange Gate and stop.
