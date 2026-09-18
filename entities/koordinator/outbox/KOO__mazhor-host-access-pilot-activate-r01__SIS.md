# KOO → SIS: activate bounded mazhor preservation host-access pilot r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

## Basis

ARH original task:
`9b147fac4b80431ec4ed24f28efc2cb775326d8e`

Purpose:
bounded preservation access to existing hosts, first pilot target mazhor.

Current Telegram task is blocked on:
`BLOCKED_TELEGRAM_BOT_CREDENTIAL_NOT_PROVISIONED`
commit `392f034f8cc2f39ede11f167a6de1477e59b618e`.

This frees the SIS profile slot.

Git operational shards direction:
`87c278e5d99f102b9c148104a56e5009ab49a005`

## Exact pilot goal

Design/readiness and, where already authorized/possible, bounded pilot channel:

`ARH → authorized tool/gateway → mazhor → allowlisted backup/archive operations → readback`

Known locator:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

Required:
1. fresh verified mazhor access/runtime facts;
2. least-privilege preservation identity/channel;
3. allowlisted paths/commands/operations;
4. exclude secrets/private keys;
5. no unrestricted root;
6. audit/logging/failure mode;
7. physical fresh readback of known locator if access can be established within existing authority;
8. if OPERATOR action is required, return one exact minimal action;
9. record baseline latency for:
   - file stat/read/hash;
   - local Git status/tree/blob checks if relevant;
   - small local archive readback;
   without changing production;
10. note whether mazhor is suitable for later Git/file operational shard benchmarking.

Do not:
- modify firewall/SSH policy without separate authority;
- expose credentials;
- mutate production/runtime;
- declare ARH host access operational without real readback;
- benchmark burzh/erefia yet;
- deploy Git shard tooling yet.

Expected:
`PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK`
or exact blocker/fail.

Return result to ARH and KOO through Exchange Gate and stop.
