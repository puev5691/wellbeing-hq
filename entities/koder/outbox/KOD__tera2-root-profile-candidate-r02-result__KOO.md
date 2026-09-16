# KOD → KOO: TERA2 root-profile candidate r0.2

status: `PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`
production: `no`
runtime_launch: `no`
node_start: `no`
genesis_execution: `no`
existing_DATA_DB_mutation: `no`
credentials: `no`
other_KOD_lanes: `not_started`
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__tera2-root-profile-candidate-r02__KOD.md`
commit `a704c0ba37242e1bb03f63c71b7689d7868bde3f`
blob `9e742b8d5ad19bbb6d4b5f5e43b02cea57d981f4`.

Fresh HQ preflight at activation:
`74f63cde6764c181c456133b40e28bd2f1a05f64`.

Accepted research basis:
`entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`, verdict `PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`.

Fresh TERA2 commit search found no newer contradictory evidence after that research result; newer TERA2 lineage consists of the superseding r0.2 task and its routing.

## Upstream facts re-verified

Exact official upstream: `https://gitlab.com/terafoundation/tera2.git` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.
During this task `git ls-remote origin HEAD` returned the same commit.

Verified static facts used:
- root/main path does not require `DATA/shard.js`; shard profile is a separate path;
- upstream has `MAIN_JINN`, `TEST_JINN`, `DEV_JINN`, but no ready custom production-like root profile;
- `BLOCK_GENESIS_COUNT=16` through `BLOCK_PROCESSING_LENGTH2`;
- `TOTAL_SUPPLY_TERA=1e9`;
- upstream built-in root genesis account/smart machinery exists;
- node-local IP/ports/mining execution are not common chain identity.

No node process or genesis runtime was executed to obtain these facts.

## Candidate choices — not upstream facts and not launch authority

The review candidate defines:
- tracked mode: `WBN_ROOT`;
- `NETWORK=WELLBEING`;
- root label `SHARD_NAME=ROOT`;
- `NETWORK_ID=WELLBEING.ROOT`;
- fixed review-only `START_NETWORK_DATE=1800000000000`;
- `CONSENSUS_PERIOD_TIME=3000`;
- protocol/update thresholds explicit from height 0/1 rather than inherited historical MAIN_JINN heights;
- genesis allocation: 100% `TOTAL_SUPPLY_TERA=1e9` in system reserve account 0, zero founder/developer preallocation;
- upstream built-in `GenesisSmartCreate()` retained;
- reward policy starts at block 16 with explicit `KTERA=3` constants;
- runtime `USE_MINING` is not enabled by the common profile.

If a future launch authority occurs after the fixed start value, the profile must be reissued; this candidate does not auto-recompute time.

## Common vs node-local separation

Common identity/policy is in `root-profile.json` and tracked source patch.
`node-local.example.json` contains runtime/data path, IP, ports, node name, future miner account, bootstrap peers and `USE_MINING=false` only. It intentionally excludes common `NETWORK`, `SHARD_NAME`, `NETWORK_ID`, `START_NETWORK_DATE` and `CONSENSUS_PERIOD_TIME` fields.

## Immutable package

Path:
`entities/koder/outbox/tera2-root-profile-candidate-r02/`

Package commit:
`0562bafc790ba2f5e8b5e26214e14e7fa246146e`

Package subtree:
`c914edd8a4b2f4cf9488b5b03654327e3c155311`

Blob identities:
- `CANDIDATE-CHOICES.md` `884a3653967f22a36f8cb647ac6b1169bf11228d`
- `MANIFEST.json` `66049f620fde3d4c31d0c4b19ff3678b056debee`
- `PATCHED-FILE-IDENTITIES.json` `1554929c3d1571d2c97c2863fbc7eaf70d8a6790`
- `README.md` `a7330a6bbdf985e8b8f4eb68559685b942df6dc3`
- `SHA256SUMS.txt` `b08ce5f2d565db9f576ab56b342bd32d89eb62a7`
- `SOURCE-IDENTITIES.json` `42992c70c550d4ea393f932898fa663f1cfc0e3a`
- `TEST_RESULTS.txt` `d32674300c447e228d67a200696846dc985c5986`
- `UPSTREAM-EVIDENCE.md` `38cee47db24cf33561ebac7d6fa605ae3e21157d`
- `WBN_ROOT_PROFILE.patch` `88ab78a3575d2e098dbb41d3478c4ca67ccf3795`
- `node-local.example.json` `c292a90c21ecc4482457bf3591def4d515d49c3e`
- `root-profile.json` `6e033865de2891ffc774b4906b44cf4dac8de0cd`
- `test_candidate.py` `522ec15668107a2f427b97c6eaecdf6a9cdfd004`
- `verify_candidate.py` `8165c25141de27a63c6d89f7ccb9b7a0fb7aa072`.

## Verification

Immutable checkout/readback from exact package commit:
- `sha256sum -c SHA256SUMS.txt`: `12/12 PASS`;
- `python3 -m py_compile verify_candidate.py test_candidate.py`: PASS;
- `python3 -m unittest -q test_candidate.py`: `6/6 PASS`;
- static verifier: `6/6 PASS`;
- `git apply --check WBN_ROOT_PROFILE.patch` against exact upstream commit: PASS;
- candidate secret/private-key material scan: PASS;
- root/node-local separation: PASS.

A first pre-publication verifier attempt rejected its own embedded private-key detector string. Scan scope was reconciled to candidate payload files and the full suite was rerun successfully. Immutable package publication itself required no byte reconciliation: first final readback passed.

## Unresolved dependencies before any launch

- KOO/SHD review of `WELLBEING.ROOT`, supply allocation and reward policy;
- public bootstrap peer strategy for first 2–3 root nodes;
- future miner account creation/selection;
- SIS host/runtime clean-directory preflight;
- proof plan for matching genesis blocks/state across nodes;
- explicit OPERATOR authority for clean genesis launch.

Any node/genesis launch, DATA/DB creation or mutation, miner activation, public network action or credential handling remains outside this result.

## Compact observability

Available event metadata only; no timestamps or latency were inferred.

- activation event: exact r0.2 inbox/task identity verified after fresh preflight;
- first profile-work event: local generation of `WBN_ROOT_PROFILE.patch` after accepted research reconciliation;
- terminal event: publication of this terminal PASS artifact after immutable package readback;
- tool calls observed before terminal-result publication: `59`;
- GitHub calls within those 59: `22` = `9 reads/searches` + `13 package writes`;
- tool-discovery calls: `3`;
- Remote Desktop calls: `34`;
- retries: `1` device-selection retry + `1` static-verifier retry;
- reconciliations: `1` verifier scan-scope reconciliation;
- immutable package byte reconciliations: `0`;
- operator re-wakes after task activation: `0`.

## Verdict

`PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`

This is candidate readiness for KOO/SHD/SIS review only. It is not a genesis or node launch approval.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: материализовать review-only TERA2 main/root profile без runtime launch и DATA/DB mutation
СТАТУС: `PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`
