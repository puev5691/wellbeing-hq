# SHD → OPERATOR: GitHub repository inventory and TERA/WBN source map r0.1

terminal_result: `PASS_WITH_BOUNDARIES`
scope: `READ_ONLY_GITHUB_REPOSITORY_INVENTORY`
project_time: omitted; trusted project-time source not used

## Human meaning

OPERATOR explicitly authorized broad read-only GitHub reconnaissance so SHD could stop guessing the TERA source lineage.

Inventory result:
- 14 repositories are visible to the linked GitHub account under owner `puev5691`;
- 13 public repositories were read at metadata/HEAD/root/README level;
- private `puev5691/HAS` is visible in repository listing but private content access is unavailable from the current GitHub connector because GitHub returned a private-service access restriction;
- four repositories are directly relevant to TERA/WBN source lineage;
- three additional historical parent/source repositories outside the current owner were read to reconstruct genealogy.

No repository content was modified during the inventory.

## Current SHD continuity

Fresh HQ preflight at inventory start:
`27eb4f48e69bbdfdb9f71f559f9ffde05e4eafe5`.

Current SHD writer:
`entities/shardovik/current/SHD__replacement-initiation-current-writer.md`
blob `88473e85feab1ae5482ff33268ca488abc42f8a4`
state `replacement_current_writer_established`.

Approved SHD operational role blob:
`29df9468da37fb4e9cda0a5912e1f41dffe08a13`.

OPERATOR authorized this broad read-only repository inventory directly.

## Complete current puev5691 repository list

### TERA / WBN source lineage

1. `puev5691/teraOrigin`
   - visibility: public
   - default branch: `master`
   - HEAD: `7fa8aa3fbaec04ce42b68a3bcc19299b5749357b`
   - HEAD message: `0.1303`
   - fork: yes
   - parent: `pev5691/teraOrigin`
   - ultimate GitHub source: `e210e8fd368d7614/teraOrigin`
   - root: `Doc/`, `Source/`, README, run-node/run-nw
   - `Source/` has no `jinn/`
   - `Source/run-node.js` blob: `d5ad761487911513c79bf42a7b458ab99ffe20c3`
   - `Source/package.json` blob: `c784b0223e7ee910f7b0fd64c7749746e92a3e70`
   - interpretation: legacy pre-JINN TERA snapshot lineage.

2. `puev5691/wellbeing`
   - visibility: public
   - default branch: `master`
   - HEAD: `6cc4955442700c2605378f76a0dd4304ad88aa23`
   - fork: yes
   - parent/source: `pev5691/wbn`
   - description: copy of TERA cryptoplatform sources for DAO WELLBEING
   - root includes `Doc/`, `Source/`, `fork-run.js`
   - `Source/jinn/` present
   - `Source/run-node.js` blob: `7e8e721ddfa3ec985f69d16d044411cde73f94f8`
   - run-node default: `MODE_RUN="MAIN_JINN"`
   - fork config: `NETWORK="WBN-MAIN"`, `MODE_RUN="FORK"`
   - historical commits explicitly mention JINN updates
   - interpretation: 2020 TERA2/JINN-derived WBN experiment, not pristine upstream.

3. `puev5691/wbn2026`
   - visibility: public
   - default branch: `master`
   - HEAD: `1d701c1c4a7d6ccca0053bdf50f413ad31ffe99f`
   - fork: yes
   - parent/source: `pev5691/wbn1995`
   - description: clone test with latest JINN engine
   - `Source/jinn/` present
   - `Source/run-node.js` blob equals legacy run-node blob `d5ad761...`
   - `fork-run.js` blob `3a06563e32a00aef501a1452bc25b97f9a6973ee`
   - fork config contains:
     - `FORK_MODE=1`
     - `NETWORK="WBN-MAIN"`
     - fixed `START_NETWORK_DATE=1590951200000`
     - `CONSENSUS_PERIOD_TIME=2000`
     - explicit seed IP list
   - interpretation: separate 2020 WBN/JINN fork experiment.

4. `puev5691/wbchain-lab`
   - visibility: public
   - default branch: `wblab`
   - HEAD: `df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   - independent repository, not marked GitHub fork
   - history directly contains legacy TERA commits:
     - `09769c68e5dcd9d0c5605c636ae4267218b01f53`
     - `7fa8aa3fbaec04ce42b68a3bcc19299b5749357b`
   - current `Source/` tree:
     `219df8f657bd8ff51ff54c0d62b371de86392072`
   - that Source tree is the same legacy tree used by `teraOrigin` at the inspected boundary
   - newer 2026 commits add lab/deployment material, not a replacement of the embedded legacy Source tree
   - root adds:
     - `deploy/`
     - `start-wblab-cerber.sh`
   - interpretation: active project lab/deployment repository containing a legacy source snapshot plus newer deployment tooling.

## Critical wbchain-lab finding

The active 2026 WBN deployment bundle does NOT rely on the repository's embedded legacy `Source/` as its deployed TERA2 runtime.

Exact installer:
`deploy/wbn-node/install/install-third-node.sh`
blob `467021abefefdee39cdde9be7c622cff45cecaf0`.

It explicitly:

1. clones:
   `https://gitlab.com/terafoundation/tera2.git`
2. checks out exact upstream commit:
   `6cc2061c12986bbaea182786c42d89fd979eeb33`
3. installs dependencies in upstream `Source/`
4. overlays WBN identity/config files.

Therefore the project itself contains an exact historical upstream TERA2 source locator for the reproduced WBN deployment:

`terafoundation/tera2 @ 6cc2061c12986bbaea182786c42d89fd979eeb33`.

Existence/content of that GitLab commit was not independently fetched in this GitHub-only inventory; it is verified here as an exact immutable locator embedded in our deployment installer.

### WBN identity overlay

`deploy/wbn-node/configs/shard.js`
blob `5625684aa71b370465e5d855bf2d9ccac1e27dd9`

contains:
- `NETWORK="WELLBEING"`
- `SHARD_NAME="WBN"`
- `START_NETWORK_DATE=1778186522932`
- seed `185.39.19.240:30000`
- `CONSENSUS_PERIOD_TIME=3000`
- `START_HISTORY=1`
- `START_MINING=10`.

Deployment bundle also contains:
- systemd service blob `464422752189ceeb60ba80f463137de9f20c8294`;
- third-node installer blob `467021abefefdee39cdde9be7c622cff45cecaf0`;
- safe const generator blob `e5324005603d87ae653f6f4ad54a9d26da810a7c`.

The README claims clean third-node deployment, WBN identity sync, peer connectivity and reproducibility. Those are repository claims/historical evidence in this inventory, not a fresh runtime re-verification.

## Historical parent genealogy

Public parent/source repositories inspected:

### `pev5691/wbn1995`
- HEAD `1d701c1c4a7d6ccca0053bdf50f413ad31ffe99f`
- current `puev5691/wbn2026` points to it as parent/source.
- Current puev fork therefore mirrors this old repository lineage.

### `pev5691/wbn`
- HEAD `6cc4955442700c2605378f76a0dd4304ad88aa23`
- current `puev5691/wellbeing` points to it as parent/source.

### `pev5691/teraOrigin`
- HEAD `7fa8aa3fbaec04ce42b68a3bcc19299b5749357b`
- fork of `e210e8fd368d7614/teraOrigin`.

### `e210e8fd368d7614/teraOrigin`
- independent source repository
- inspected HEAD `ddd378007659958ff296be89efd47402bdfa9989`
- later than the exact commit copied into our legacy teraOrigin/wbchain-lab lineage.

This establishes genealogy but does not make the external repository an approved current project source.

## Project infrastructure repositories

5. `puev5691/wellbeing-hq`
   - independent
   - branch `main`
   - survey-start HEAD `27eb4f48e69bbdfdb9f71f559f9ffde05e4eafe5`
   - operational routing/inbox/outbox/current/dispatch/registry layer.

6. `puev5691/wellbeing-entity-bootstrap`
   - independent
   - branch `main`
   - surveyed HEAD `ab4c7ad12db9760fe825d2a93b6467499e1a09f4`
   - recovery/bootstrap packages, policies, profiles, manifests, templates.

7. `puev5691/wellbeing-archivist`
   - independent
   - branch `main`
   - surveyed HEAD `f847be7635124dc155d99d8b62c4e105da8c8cb3`
   - local Archivist index/query/service-layer and package tooling.

8. `puev5691/wellbeing-experience`
   - independent
   - branch `main`
   - HEAD `b653d2e18d3b7087924aa3ba3453c080c6c54fef`
   - accumulated experience / Continuity v2 candidate / anti-regression corpus.
   - README status `bootstrap_candidate`, not active canon.

9. `puev5691/wellbeing-log16`
   - independent
   - branch `master`
   - HEAD `c240d688422ae0b49045e67280c8245c6e41e4b8`
   - early laboratory prototype for knowledge/dialog/task/evidence processing.

10. `puev5691/wellbeing-cooperation`
    - independent
    - branch `main`
    - HEAD `fcd31ea92f0f743eac5a80ea0a65c42b5d2f4dd6`
    - evidence-first research corpus on cooperation/co-ownership/federative models.
    - README status `bootstrap_initialized`.

## External technology forks in the account

11. `puev5691/MiroFish`
    - fork of `666ghj/MiroFish`
    - HEAD `985f89f49acbb44ee14d9d680682c741a44eeebe`
    - multi-agent/swarm simulation and forecasting engine.
    - potentially useful to project simulation/research, not TERA source.

12. `puev5691/PromeTorch`
    - fork of `barometech/PromeTorch`
    - HEAD `ec2b4df25c6e89320c147d5b2e233d814a363af9`
    - C++/CUDA training framework with Elbrus/Russian-platform work.
    - not TERA source.

13. `puev5691/sglang`
    - fork of `sgl-project/sglang`
    - HEAD `e3258d3b5488eee77d76150b616e06f3a7343734`
    - LLM serving framework.
    - not TERA source.

## Private repository

14. `puev5691/HAS`
    - visibility: private
    - default branch: `main`
    - repository list reports size 125
    - content inventory unavailable from current GitHub connector because GitHub rejected private-service access under an account restriction.

State:
`UNAVAILABLE_FROM_CURRENT_GITHUB_ACCESS`.

No content or purpose is inferred.

## Practical source map for future TERA research

The project contains four distinct source/evidence classes and they must not be conflated.

### Class A — legacy original-line TERA snapshot

Use:
`puev5691/teraOrigin@7fa8aa3fbaec04ce42b68a3bcc19299b5749357b`

Purpose:
understand legacy TERA 0.1303 architecture, Terahash-era pre-JINN entry/config/network/consensus/storage code.

### Class B — historical WBN/JINN experiments

Use only as historical fork evidence:
- `puev5691/wellbeing@6cc4955442700c2605378f76a0dd4304ad88aa23`;
- `puev5691/wbn2026@1d701c1c4a7d6ccca0053bdf50f413ad31ffe99f`.

Purpose:
understand earlier attempts to adapt TERA/JINN into WBN.

Do NOT use them as proof of pristine upstream TERA2 behavior.

### Class C — current project lab/deployment history

Use:
`puev5691/wbchain-lab@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`.

Purpose:
understand what the project actually deployed/configured in 2026 and which upstream/version it pinned.

The embedded legacy `Source/` is not the deployed TERA2 source.

### Class D — exact official upstream TERA2 version selected by our deployment bundle

Discovered locator:
`terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33`.

This should be the first-choice immutable source authority for reconstructing the TERA2 chain-start path used by the documented WBN deployment, once independently fetched from the official source.

Official docs should be pinned separately at a compatible immutable revision before docs claims are used normatively.

## Recommended research split

Research should be separated into two tracks.

### Track 1 — original Terahash architecture

Source:
`puev5691/teraOrigin@7fa8aa3fbaec04ce42b68a3bcc19299b5749357b`.

Question:
`entry → config → network identity → peer discovery → PoW/Terahash → block production → DB/state`.

This answers how the legacy Terahash-era system worked.

### Track 2 — TERA2/JINN chain/shard architecture used by WBN deployment

Primary source authority candidate:
official `terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33`.

Project overlay/evidence:
`puev5691/wbchain-lab@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`.

Question:
`entry → shard.js/const.lst → network/shard identity → JINN peer discovery → consensus/block timing → block production/mining → persistent state`.

This answers what the current WBN deployment bundle was actually designed around.

These tracks must not be merged into one source tree.

## Immediate conclusion

The earlier research blocker is now narrowed.

We do not need OPERATOR to guess a repository/commit anymore.

For the project-history side, exact commits are now known.

For the actual TERA2 source used by the 2026 deployment, the project itself points to:
`6cc2061c12986bbaea182786c42d89fd979eeb33`.

The next honest step is to fetch that exact commit from the official TERA2 source and begin Track 2 static research, while separately retaining `teraOrigin@7fa8...` for Track 1 Terahash research.

No code/source/genesis/DATA/DB mutation is required for either first static-analysis track.
