# SHD → KOO: TERA2 root-profile candidate r0.2 independent review

status: `BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`
production: `no`
runtime_launch: `no`
node_start: `no`
genesis_execution: `no`
DATA_DB_mutation: `no`
credentials: `no`
project_time: omitted; trusted project-time source not used

## Краткий результат

Immutable candidate r0.2 в целом семантически согласован с accepted SHD research и pinned upstream TERA2, но terminal PASS пока недопустим: common chain identity ↔ node-local contract не fail-closed по `MODE_RUN`, а static verifier не доказывает полное соответствие machine-readable chain-policy manifest фактически применяемому tracked source patch.

Это review blocker, а не запрет выбранной экономики/имени сети. Node/genesis не запускались, DATA/DB не создавались и не менялись, credentials/miner keys не использовались, candidate package не переписывался.

## 1. Fresh preflight и instance admission

Fresh `puev5691/wellbeing-hq` preflight перед terminal result:
- observed HEAD: `c21307722f94e4ad65f4b54f15d1471ab0d9a7fa`;
- required current boundary: `entities/shardovik/current/SHD__current-state.md`;
- observed blob: `1cc5ec5c0766328ab24ded239f020f75d8cf7524`;
- required blob: `1cc5ec5c0766328ab24ded239f020f75d8cf7524`;
- admission: `PASS`.

Fresh HEAD содержит lifecycle sample `sample-0003-SHD` со `source_instance_status=replaced`, но sample явно относится к прежнему SHD instance: в нём remembered last task — VPN/Xray/SSH-SOCKS и handoff replacement. Текущий review instance не возвращается в этот retired lineage и обрабатывает более поздний exact KOO TERA2 task. Поэтому это historical evidence о старом instance, а не conflicting current-instance evidence.

## 2. Exact task и immutable candidate identity

Exact task verified:
- `entities/koordinator/outbox/KOO__tera2-root-profile-r02-review__SHD.md`;
- commit `dbbf5950a1657d92c683287905d11a1980d282a7`;
- blob `dddc8dd9f4d7d02d27b709b835de80ccae6cbe5e`.

KOD terminal result verified:
- `entities/koder/outbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md`;
- commit `94c6ecff6a7aa0fcdbba3b549a14c3de0664a9f9`.

Candidate package verified:
- path `entities/koder/outbox/tera2-root-profile-candidate-r02/`;
- commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`;
- observed subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`;
- expected subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`.

Accepted SHD research basis:
- `entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`;
- commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`.

Official upstream boundary was independently rechecked read-only through existing checkout/remote:
- repository `https://gitlab.com/terafoundation/tera2.git`;
- pinned commit `6cc2061c12986bbaea182786c42d89fd979eeb33`;
- fresh `git ls-remote origin HEAD` observed the same commit.

## 3. Evidence classification

### 3.1 Verified upstream facts

- root/main path can use tracked `const-mode.js` without `DATA/shard.js`;
- `DATA/shard.js` is a distinct shard-profile path;
- `BLOCK_GENESIS_COUNT=16`;
- `TOTAL_SUPPLY_TERA=1e9` at pinned upstream;
- built-in `GenesisSmartCreate()` exists;
- built-in `DoCoinBaseTR()` returns before `START_MINING`;
- when block height is at/above `UPDATE_CODE_JINN_KTERA`, coinbase uses `NEW_FORMULA_JINN_KTERA`;
- upstream has no ready custom production-like `WELLBEING` root mode.

### 3.2 Accepted SHD research facts

- custom root must be a tracked common profile, not `DATA/shard.js`;
- common nodes require identical root/profile identity, temporal identity, protocol schedule and genesis state policy;
- `JINN_IP`, ports, node name and runtime mining execution are node-local;
- fixed `START_NETWORK_DATE` is required for reproducible cluster genesis;
- launch requires later proof of matching genesis blocks/state and real peer connectivity.

### 3.3 KOD project candidate choices

These are coherent candidate choices, not upstream facts:
- `MODE_RUN=WBN_ROOT`;
- `NETWORK=WELLBEING`;
- `SHARD_NAME=ROOT`;
- derived `NETWORK_ID=WELLBEING.ROOT`;
- fixed review-only `START_NETWORK_DATE=1800000000000` with reissue rule;
- `CONSENSUS_PERIOD_TIME=3000`;
- update/protocol thresholds moved to height `0/1`;
- 100% `1e9` supply in system reserve account 0; accounts 1..15 zero; no founder/developer preallocation;
- exact upstream built-in `GenesisSmartCreate()` retained;
- `START_MINING=16`, no referral window, explicit `NEW_FORMULA_KTERA=3` and `NEW_FORMULA_JINN_KTERA=3`;
- common profile does not enable runtime mining.

### 3.4 Exact unresolved KOO/OPERATOR decisions before launch

- accept/change public chain identity `WELLBEING.ROOT`;
- accept/reissue fixed start date when actual launch window is known;
- accept/change 100% system-reserve genesis allocation;
- accept/change reward/economic policy;
- authorize future clean genesis launch.

Bootstrap peers, clean-directory host preflight and future miner account are launch dependencies, not defects in the current semantic candidate by themselves.

## 4. Semantic review by required points

### PASS — root identity and shard exclusion

Candidate correctly uses tracked `WBN_ROOT` and does not use `DATA/shard.js` as root identity. Patch changes tracked `Source/core/const-mode.js` and `Source/system/accounts.js` only.

### PASS — `WELLBEING.ROOT`

`NETWORK=WELLBEING`, `SHARD_NAME=ROOT`, and declared `NETWORK_ID=WELLBEING.ROOT` are internally consistent. This remains a project naming choice requiring KOO/OPERATOR acceptance, not an upstream fact.

### PASS — fixed temporal identity

`START_NETWORK_DATE=1800000000000` is fixed rather than auto-derived, with explicit `launch_after_start_date_requires_reissue=true`. This satisfies the reproducibility concern from r0.1. Actual launch must still use an approved, non-expired profile.

### PASS — consensus period

`CONSENSUS_PERIOD_TIME=3000` is explicit and matches the reviewed upstream period.

### PASS_WITH_POLICY_DECISION — thresholds from height 0/1

The candidate explicitly avoids inherited historical MAIN_JINN heights. The values are internally materialized in both profile and patch. They are project policy choices and need launch-stage acceptance; no contradictory upstream fact was found in this review.

### PASS_WITH_POLICY_DECISION — genesis allocation

Patch deterministically changes root-mode account genesis to 100% `TOTAL_SUPPLY_TERA` in account 0 and zero balances for accounts 1..15. No founder/developer preallocation remains. This is semantically clear, but it is an economic/governance choice, not an upstream requirement.

### PASS — smart genesis

Candidate does not add a custom shard `GenesisSmartCreate()` and does not patch `Source/system/smart.js`; therefore the pinned upstream built-in `GenesisSmartCreate()` remains the intended path.

### PASS_WITH_POLICY_DECISION — reward from block 16

Independent read-only upstream check confirms built-in `DoCoinBaseTR()` returns for blocks `< START_MINING`. With candidate `START_MINING=16`, `UPDATE_CODE_JINN_KTERA=0`, and explicit `NEW_FORMULA_JINN_KTERA=3`, block 16+ uses the intended KTERA=3 branch. This is internally coherent but remains a project economic choice.

### PASS — safe mining default / unresolved miner account

Common profile does not set `USE_MINING=1`; node-local example has `USE_MINING=false`. Future miner account creation/selection is explicitly unresolved. No miner key or credential is part of this candidate review.

## 5. Concrete blocker A — `MODE_RUN` is mis-layered and not fail-closed

`root-profile.json` correctly declares `mode_run: WBN_ROOT`, but `node-local.example.json` also places `MODE_RUN: WBN_ROOT` inside a file whose stated purpose is `per-node operational example only; not chain identity`.

This is semantically unsafe because `MODE_RUN` is the selector that chooses the tracked chain profile. A node with another `MODE_RUN` does not merely differ operationally; it can select another network/profile and therefore cease to implement the same root chain policy.

The static verifier does not close this gap:
- its `forbidden_chain_fields` excludes `MODE_RUN`;
- it never asserts `node-local.MODE_RUN == root-profile.mode_run`;
- therefore a node-local mode divergence can pass the advertised `chain_vs_node_local_separation` check.

Smallest correction:
1. classify `MODE_RUN` as a common immutable profile selector;
2. either remove it from freely variable node-local config and derive it from common profile, or require exact equality to `root-profile.mode_run`;
3. add a negative test where node-local `MODE_RUN` differs and verification must fail closed.

## 6. Concrete blocker B — machine-readable policy ↔ tracked patch proof is incomplete

The exact current bytes of `root-profile.json` and `WBN_ROOT_PROFILE.patch` were independently read and are materially consistent on the reviewed fields. However the candidate's verifier does not prove that full property.

`verify_candidate.py` checks only a subset of policy values against the patch: identity strings, start date, `START_MINING`, reserve markers and several boundaries. It does not fail closed on drift for, among others:
- `CONSENSUS_PERIOD_TIME` in patch vs profile;
- account-hash/update schedule values;
- `UPDATE_CODE_*` family;
- `NEW_FORMULA_KTERA` / `NEW_FORMULA_JINN_KTERA` and reward targets;
- full genesis allocation semantics accounts 1..15.

It also does not consume `SOURCE-IDENTITIES.json` or `PATCHED-FILE-IDENTITIES.json` to prove source/post-patch identities, despite those artifacts being present.

Consequently the advertised static verifier can return PASS for a future package revision in which machine-readable chain policy and applied source policy disagree. For a genesis identity package, that is not sufficiently fail-closed.

Smallest correction:
1. extend verifier to cross-check every common chain-policy field against the actual patched source representation;
2. validate pinned source identities and declared post-patch identities;
3. add at least two negative fixtures: one mode-selector mismatch and one consensus/reward/genesis-policy mismatch;
4. keep current economic/naming values unchanged unless KOO/OPERATOR separately changes them.

## 7. Terminal verdict

`BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`

The r0.2 candidate is substantially coherent and no runtime/genesis defect was demonstrated because runtime execution was intentionally prohibited. The blocker is narrower: the immutable package does not yet provide a fail-closed common identity contract sufficient for later multi-node genesis preflight.

A corrected candidate does not need a redesign of `WELLBEING.ROOT`, supply allocation, smart genesis or reward policy merely because of this verdict. Those remain explicit policy choices pending KOO/OPERATOR acceptance.

## 8. Smallest next bounded action

KOO → KOD: issue one correction-only task for r0.2/r0.3 that changes only the common-vs-node-local identity contract and verifier coverage described in sections 5–6; no runtime launch, no DATA/DB, no credentials. Then return the immutable corrected package to SHD for one independent read-only re-review.

## 9. Compact observability

- activation boundary: fresh HQ preflight + exact required current-state blob check;
- admission reconciliation: latest retired SHD lifecycle sample was read only to disambiguate the historical old instance from this later review instance;
- first profile-work event: exact KOO task + exact candidate commit/subtree readback;
- independent upstream reconciliation: read-only `git ls-remote` and `git show/grep` on pinned upstream; no node process launched;
- terminal-result event: publication of this artifact;
- runtime retries: `0`;
- candidate rewrites: `0`;
- operator re-wakes after this task activation: `0`;
- exact aggregate tool-call/latency counts are not asserted.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: independently review semantic/chain-policy TERA2 root-profile candidate r0.2
СТАТУС: `BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`
