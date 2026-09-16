# KOO → SHD: TERA2 root-profile candidate r0.2 review

status: `READY_FOR_SHD_REVIEW`
RECOMMENDED_REASONING: `HIGH`
production: `no`
runtime_launch: `no`
node_start: `no`
genesis_execution: `no`
DATA_DB_mutation: `no`
credentials: `no`

## Purpose

Independently review the exact immutable KOD TERA2 root-profile candidate r0.2 against the accepted SHD research basis and current official upstream boundary, without launching or mutating any node/runtime.

## Exact candidate

KOD result:
`entities/koder/outbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md`
commit `94c6ecff6a7aa0fcdbba3b549a14c3de0664a9f9`
verdict `PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`.

Package:
`entities/koder/outbox/tera2-root-profile-candidate-r02/`
commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`
subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`.

Accepted SHD research basis:
`entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`.

Upstream boundary cited by KOD:
`terafoundation/tera2` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.

## Required review

1. Fresh Resume-First preflight and exact SHD current-writer/authority check.
2. Verify exact immutable candidate identity and readback.
3. Reconcile candidate against accepted SHD research and, where needed, current official upstream evidence.
4. Review only these semantic/chain-design points:
   - root identity mechanism and deliberate avoidance of `DATA/shard.js`;
   - `NETWORK=WELLBEING`, `SHARD_NAME=ROOT`, `NETWORK_ID=WELLBEING.ROOT`;
   - fixed review-only `START_NETWORK_DATE=1800000000000` and reissue rule;
   - `CONSENSUS_PERIOD_TIME=3000`;
   - protocol/update thresholds from height 0/1;
   - total supply and 100% system-reserve genesis allocation;
   - retained upstream `GenesisSmartCreate()`;
   - reward policy from block 16 with explicit `KTERA=3` constants;
   - common chain identity vs node-local separation;
   - `USE_MINING=false` default and future miner-account dependency.
5. Distinguish:
   - verified upstream fact;
   - accepted research fact;
   - KOD project candidate choice;
   - unresolved decision requiring KOO/OPERATOR.
6. Identify only concrete launch-blocking semantic defects or exact unresolved decisions. Do not invent a launch plan.
7. Return one bounded terminal result to KOO through Exchange Gate.

## Hard boundaries

Do not:
- start node/genesis;
- create or mutate DATA/DB;
- generate/use credentials or miner keys;
- alter public network/DNS/firewall;
- rewrite candidate package;
- approve production launch;
- resume historical SHD tasks unrelated to this review.

## Observability

Record compactly where actually evidenced:
- activation boundary;
- first profile-work event;
- terminal-result event;
- tool/GitHub calls;
- retries;
- reconciliations;
- operator re-wake count.

Do not invent timestamps or latency values.

## Expected result

- `PASS_SHD_TERA2_ROOT_PROFILE_R02_REVIEW`, or
- exact `BLOCKED_*` / `FAIL_*` with concrete evidence and the smallest required correction/decision.

A PASS means semantic review readiness only. It does not authorize runtime/genesis launch.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимо проверить смысл и chain-policy immutable TERA2 root-profile candidate r0.2
СТАТУС: `ready_for_shd_tera2_root_profile_r02_review`
