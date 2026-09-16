# KOO → KOD: TERA2 root-profile candidate r0.2

status: `READY_FOR_KOD_EXECUTION`
RECOMMENDED_REASONING: `HIGH`
production: `no`
runtime_launch: `no`
node_mutation: `no`
credentials: `no`

## Purpose

Prepare a tracked, reproducible candidate-only TERA2 main/root profile using the accepted research basis, without launching a node or mutating existing WBN/TERA2 DATA/DB.

## Fresh dependency state

KOD OpenAI Responses D0 adapter task is closed with terminal PASS:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`
verdict `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`.

The earlier queued TERA2 task:
`entities/koordinator/outbox/KOO__tera2-root-profile-candidate-r01__KOD.md`
commit `9c6972681ae8b058cbe99c5ae4a3674a5cd1d3eb`
was never dispatched and is superseded for execution by this r0.2 task.

## Research basis

SHD result:
`entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`.

Use only accepted/current research evidence after a fresh Resume-First preflight. If newer contradictory TERA2 evidence exists, stop with exact blocker rather than silently choosing.

## Required candidate

Prepare an immutable candidate package that:
- avoids `DATA/shard.js` as root identity mechanism;
- defines candidate `NETWORK`, root label, fixed `START_NETWORK_DATE`, consensus/update schedule, genesis public configuration and reward/mining policy;
- separates common chain identity from per-node operational config;
- contains no private keys/secrets;
- does not launch a node;
- does not mutate existing WBN/TERA2 DATA/DB;
- includes manifest/checksums/tests sufficient for later SHD/SIS review;
- records assumptions and unresolved upstream dependencies explicitly;
- distinguishes researched upstream facts from project candidate choices.

## Verification / publication

Before terminal PASS:
1. fresh HQ preflight;
2. exact research basis readback;
3. candidate generation;
4. deterministic/static checks as appropriate;
5. checksum/manifest verification;
6. immutable package publication;
7. immutable readback;
8. terminal result artifact;
9. address result to KOO through current Exchange Gate.

## Observability metadata

Record compactly if actually available:
- task activation boundary;
- first profile-work event;
- terminal result event;
- tool calls;
- GitHub reads/writes;
- retries;
- reconciliation count;
- operator re-wake count if known.

Do not invent timestamps/latency values.

## Expected result

- `PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`, or
- exact `BLOCKED_*` / `FAIL_*` with evidence.

Any genesis launch, node start, DATA/DB write, miner activation or production/public network action remains a separate OPERATOR-authorized gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: материализовать следующий TERA2/WBN candidate после закрытия KOD API lane
СТАТУС: `ready_for_kod_tera2_root_profile_r02`
