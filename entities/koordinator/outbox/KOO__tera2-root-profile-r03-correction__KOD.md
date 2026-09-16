# KOO → KOD: TERA2 root-profile correction r0.3

status: `READY_FOR_KOD_EXECUTION`
RECOMMENDED_REASONING: `HIGH`
production: `no`
runtime_launch: `no`
node_start: `no`
genesis_execution: `no`
DATA_DB_mutation: `no`
credentials: `no`

## Purpose

Issue one correction-only task against the exact r0.2 TERA2 root-profile candidate after independent SHD review. Do not redesign naming/economics unless separately authorized.

## Exact blocker basis

SHD review:
`entities/shardovik/outbox/SHD__tera2-root-profile-r02-review__KOO.md`
commit `bcdbe6dfc744ee1ff581ca78bd1f3eeaf001323c`
verdict `BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`.

Candidate basis:
`entities/koder/outbox/tera2-root-profile-candidate-r02/`
commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`
subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`.

## Required corrections only

### A. MODE_RUN fail-closed common identity

1. Treat `MODE_RUN=WBN_ROOT` as common immutable profile selector.
2. Remove free divergence from node-local config, or enforce exact equality to `root-profile.mode_run`.
3. Add negative test where node-local MODE_RUN differs and verifier must fail closed.

### B. Full machine-readable policy ↔ tracked patch proof

Extend verifier so that it proves all common chain-policy fields represented in `root-profile.json` are consistent with the tracked source patch, including at minimum:
- `CONSENSUS_PERIOD_TIME`;
- account-hash/update schedule values;
- `UPDATE_CODE_*` family;
- `NEW_FORMULA_KTERA` / `NEW_FORMULA_JINN_KTERA`;
- reward/mining thresholds;
- full genesis allocation semantics for accounts 0..15;
- pinned source identities;
- declared post-patch identities.

Add at least two negative fixtures:
- MODE_RUN mismatch;
- one consensus/reward/genesis-policy mismatch.

## Explicit non-goals

Do not change, merely because of this review:
- `NETWORK=WELLBEING`;
- `SHARD_NAME=ROOT`;
- `NETWORK_ID=WELLBEING.ROOT`;
- fixed review-only start date policy;
- 100% system reserve allocation;
- retained upstream `GenesisSmartCreate()`;
- KTERA=3 reward choice.

Those remain separate KOO/OPERATOR policy decisions.

## Verification / publication

Before terminal PASS:
1. fresh HQ preflight;
2. exact blocker readback;
3. correction-only package update;
4. deterministic/static tests;
5. checksum/manifest verification;
6. immutable publication;
7. immutable readback;
8. terminal result artifact;
9. address result to KOO through Exchange Gate.

## Instance admission

Before profile work verify current KOD writer boundary. If this chat is not the active current writer, stop with `WRONG_INSTANCE_OR_WRONG_CHAT` and evidence.

## Observability

Record compactly if actually evidenced:
- activation / first-work / terminal events;
- tool/GitHub calls;
- retries;
- reconciliations;
- operator re-wakes.

Do not invent timestamps or latency.

## Expected result

- `PASS_TERA2_ROOT_PROFILE_R03_CORRECTED_READY_FOR_SHD_REREVIEW`, or
- exact `BLOCKED_* / FAIL_*`.

No runtime/genesis launch, DATA/DB write, credentials or public-network action is authorized.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить два конкретных fail-closed дефекта r0.2 и вернуть candidate на независимый SHD re-review
СТАТУС: `ready_for_kod_tera2_root_profile_r03_correction`
