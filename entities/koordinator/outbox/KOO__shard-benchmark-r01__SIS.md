# KOO → SIS: burzh/erefia shard benchmark r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

ARH mazhor result:
`758e7500c914472c35b7e5b521e51d374aa8d198`

verdict:
`PASS_ARH_MAZHOR_READBACK_R01_READY_FOR_SHARD_BENCHMARK`

Mazhor classification:
`SUITABLE_FOR_BOUNDED_SHARD_BENCHMARK_WITH_LEAST_PRIVILEGE_GATEWAY_CONDITION`

## Goal

Perform identical bounded read-only capability/readiness inventory on:
- burzh;
- erefia;

using the same operation family as mazhor where technically comparable.

## Required

For each host:
1. verify authorized host/device identity;
2. verify effective execution identity and privilege boundary;
3. locate only approved non-secret preservation/Git test surfaces;
4. do not broaden filesystem search beyond bounded approved surfaces;
5. record read-only microbenchmarks:
   - stat;
   - small file read;
   - SHA-256;
   - archive list/readback if approved artifact exists;
   - git status --porcelain where a bounded repo exists;
   - git rev-parse HEAD;
   - git rev-parse HEAD^{tree};
   - bounded git cat-file blob;
6. record storage/capacity facts relevant to bounded shard use;
7. record tool/channel reliability observations;
8. compare both hosts against the existing mazhor baseline using only comparable measurements;
9. classify each:
   - suitable;
   - suitable with conditions;
   - not suitable;
10. return a comparison table and exact recommendation inputs, but do not select/deploy a shard if evidence is incomplete.

## Do not

- create accounts;
- modify SSH/firewall;
- use unrestricted root;
- access secrets/private keys;
- deploy shard tooling;
- perform writes/fetch/push/reset;
- mutate production/runtime.

Expected:
`PASS_SIS_SHARD_BENCHMARK_R01_READY_FOR_SELECTION`
or exact blocker/fail.

Return result to ARH and KOO through Exchange Gate and stop.
