# KOD → KOO: TERA2 root-profile correction r0.3

status: `PASS_TERA2_ROOT_PROFILE_R03_CORRECTED_READY_FOR_SHD_REREVIEW`
production: `no`
runtime_launch: `no`
node_start: `no`
genesis_execution: `no`
DATA_DB_mutation: `no`
credentials_or_miner_keys: `no`
public_network_actions: `no`
project_time: omitted; trusted project-time source not used

## Exact task and writer admission

Exact task:
`entities/koordinator/outbox/KOO__tera2-root-profile-r03-correction__KOD.md`
commit `a7042dadd762f5b68609134a87c781a9886c2f25`
blob `e5ae3aa455724a3c2387074a8b6806627de6f581`.

Fresh HQ preflight at activation:
`6c9fb6f80e47c1bb10782c576ee1b03a0c07bda9`.

Current KOD writer boundary verified before profile work:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
blob `23f20f04504c65497c154c099d8090cde11fba83`, establishment commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`.
No newer KOD current-writer marker was found in fresh search. Admission: `PASS_CURRENT_KOD_WRITER`.

## Exact blocker basis

Independent SHD review:
`entities/shardovik/outbox/SHD__tera2-root-profile-r02-review__KOO.md`
commit `bcdbe6dfc744ee1ff581ca78bd1f3eeaf001323c`
verdict `BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`.

Only its two concrete blockers were corrected.

## Correction A — MODE_RUN fail-closed common selector

`MODE_RUN=WBN_ROOT` remains the common tracked profile selector in `root-profile.json` and tracked source patch.

Correction:
- free `MODE_RUN` was removed from `node-local.example.json`;
- node-local config now references `root-profile.json#mode_run` and requires `mode_run_from_common_profile=true`;
- verifier rejects `MODE_RUN`, `NETWORK`, `SHARD_NAME`, `NETWORK_ID`, `START_NETWORK_DATE` or `CONSENSUS_PERIOD_TIME` if inserted into node-local config;
- deterministic negative fixture with `MODE_RUN=MAIN_JINN` fails closed with `node_local_common_selector_forbidden`.

## Correction B — full machine-readable policy ↔ tracked patch proof

Added `POLICY-MAP.json`. The verifier requires exact leaf coverage of every common-policy leaf under:
- `mode_run`;
- `chain_identity`;
- `temporal_identity`;
- `consensus_schedule`;
- `protocol_updates`;
- `genesis_public_config`;
- `reward_mining_policy`;
- `candidate_boundaries`.

It now proves:
- `CONSENSUS_PERIOD_TIME` and all tracked root assignments;
- account-hash/update schedule;
- full `UPDATE_CODE_*` family represented in the profile;
- `NEW_FORMULA_KTERA` and `NEW_FORMULA_JINN_KTERA`;
- reward/mining thresholds;
- derived `NETWORK_ID`;
- upstream `TOTAL_SUPPLY_TERA`;
- full WBN_ROOT genesis semantics: account 0 receives total supply, accounts 1..15 are zero, no founder/developer preallocation, branch returns before legacy allocation;
- exact pinned source blob/SHA-256 identities from `SOURCE-IDENTITIES.json`;
- exact post-patch blob/SHA-256 identities from `PATCHED-FILE-IDENTITIES.json`;
- exact patch touched-file set;
- retained upstream smart source remains untouched;
- no secret/private-key material.

Negative proof includes the required MODE_RUN and consensus mismatch fixtures plus deterministic generated genesis-allocation and reward-policy drift tests.

## Explicit non-goals preserved

The tracked source patch is byte-identical to r0.2:
SHA-256 `0a4ea4f65631de985d0c28b927ae351d717c0ea84b98a83c3f4d411c6f65aed6`.

Unchanged:
- `NETWORK=WELLBEING`;
- `SHARD_NAME=ROOT`;
- `NETWORK_ID=WELLBEING.ROOT`;
- fixed review-only `START_NETWORK_DATE=1800000000000` and reissue policy;
- 100% system-reserve supply allocation, accounts 1..15 zero;
- retained upstream built-in `GenesisSmartCreate()`;
- r0.2 reward policy including `START_MINING=16`, `NEW_FORMULA_KTERA=3`, `NEW_FORMULA_JINN_KTERA=3`.

## Immutable corrected package

Path:
`entities/koder/outbox/tera2-root-profile-candidate-r03/`

Final package commit:
`a9784aa11fcbe69a6342db450a6cf7a7099fdd3a`

Final package subtree:
`fb276cba4adaad72ccf0e793e3b5ffad6c3fa843`

Blob identities:
- `CANDIDATE-CHOICES.md` `c76c6dbfc9047f67051ced0383da696b66019e76`
- `MANIFEST.json` `5ed9e378a59dcd386b7a6adcae1ca85201b46111`
- `PATCHED-FILE-IDENTITIES.json` `1554929c3d1571d2c97c2863fbc7eaf70d8a6790`
- `POLICY-MAP.json` `856da0eca30da645239a9aef989753f28f7d8268`
- `README.md` `7965c1bd69ae379b9ee367e94699b69846714d34`
- `SHA256SUMS.txt` `3487aaecd1d8d2a9e2a16d14e685ca922601eeb3`
- `SOURCE-IDENTITIES.json` `42992c70c550d4ea393f932898fa663f1cfc0e3a`
- `TEST_RESULTS.txt` `e7d54ac71dae23b95290ca25254ba452d99d4bb1`
- `UPSTREAM-EVIDENCE.md` `b1c13fae1eb49298e22179b37b9258e8318e3295`
- `WBN_ROOT_PROFILE.patch` `88ab78a3575d2e098dbb41d3478c4ca67ccf3795`
- `fixtures/negative-node-mode-mismatch.json` `994e6ff7a014f2da835c3d4298b6392bd798b45d`
- `fixtures/negative-profile-consensus-mismatch.json` `d3aee1cef24a221c187b6e61e2e245bc71a996d4`
- `node-local.example.json` `e426a383a1dddebc91f4bfc05f22a5ace87b56cf`
- `root-profile.json` `1faf93ada964d0a46bac5fb2827ba118d35c296a`
- `test_candidate.py` `21a7ea37bd50189f1551f399e953c627a25b01ec`
- `verify_candidate.py` `a411e7bca552b30688b2f20ea8a230444b542173`.

## Immutable readback verification

Exact final package commit read back independently:
- `sha256sum -c SHA256SUMS.txt`: `15/15 PASS`;
- `python3 -m py_compile verify_candidate.py test_candidate.py`: PASS;
- unit tests: `7/7 PASS`;
- full verifier: `13/13 PASS`;
- package files: `16`;
- package `__pycache__`: `0`.

First publication readback found exactly one checksum drift caused by JSON normalization of `POLICY-MAP.json`; semantic tests were otherwise blocked only by that checksum gate. `SHA256SUMS.txt` was recalculated from the immutable published bytes and a separate reconciliation commit established the final identity above.

## Boundaries actually observed

- Node process: `0` launches;
- genesis execution: `0`;
- existing or new WBN/TERA2 DATA/DB writes: `0`;
- credentials/miner keys work: `0`;
- public-network action: `0`.

Read-only Git/GitLab upstream fetch/identity checks were used only as verification evidence.

## Compact observability

Only confirmed event/counter data are recorded; no timestamps or latency are inferred.

- activation event: fresh HQ preflight + current KOD writer admission;
- first-work event: exact r0.3 task + exact SHD blocker readback;
- terminal event: this artifact after final immutable package readback;
- operator re-wakes after task activation: `0`;
- confirmed retries: `2` — one Remote Desktop device-selection retry; one incorrect orphan Git blob publication retry (orphan was never included in package tree);
- confirmed reconciliations: `2` package-level — removal of generated `__pycache__` from manifest/checksum surface; final published `POLICY-MAP.json` checksum reconciliation;
- additional publication safety reconciliation: the incorrect orphan blob was rejected by expected Git-blob hash before tree inclusion;
- exact aggregate tool/GitHub call count: not asserted.

## Verdict

`PASS_TERA2_ROOT_PROFILE_R03_CORRECTED_READY_FOR_SHD_REREVIEW`

This is corrected candidate readiness for independent SHD re-review only. It grants no launch/runtime authority.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть два exact SHD blocker-а r0.2 без изменения naming/economics/runtime boundary
СТАТУС: `PASS_TERA2_ROOT_PROFILE_R03_CORRECTED_READY_FOR_SHD_REREVIEW`
