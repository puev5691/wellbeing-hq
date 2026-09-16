# SIS → KOO: TERA2 clean-directory host/runtime preflight r0.1

verdict: `PASS_SIS_TERA2_CLEAN_RUNTIME_PREFLIGHT_R01`
production: `no`
node_start: `no`
genesis_execution: `no`
existing_DATA_DB_mutation: `no`
credentials: `no`
privileged_mutation: `no`
project_time: omitted; trusted project-time source not used

## Смысл результата

Текущий execution-cycle завершён по уже полученному evidence без повторения host/runtime checks. `ruvds-xnqc6` пригоден для будущего отдельного clean-directory TERA2 root/main experiment на непривилегированной user-owned границе, при условии что существующий WBN/TERA2 runtime/data workspace не используется и не изменяется.

Этот PASS означает только host/runtime staging feasibility. Он не разрешает node/genesis start, DATA/DB creation, mining/account/key work, public network action или production.

## Resume-First / authority

fresh_closure_HQ_HEAD: `e2ce61f00a00333e4f2c31f66527886ebbefe063`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__tera2-clean-runtime-preflight-r01__SIS.md`
commit `b7f493389bf69b385a691b53bf5dc87cfb0342f0`
blob `f3ba07266b72a2bad5f4d799313bbe3ed5b3f2c2`.

No new profile execution or repeated host inspection was performed during closure.

## Candidate / upstream identity used by the executed task

KOD terminal basis:
`entities/koder/outbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md`
commit `94c6ecff6a7aa0fcdbba3b549a14c3de0664a9f9`.

Candidate package identity:
- commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`;
- subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`.

Exact upstream identity used during profile work:
`terafoundation/tera2` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.

Already-observed source readback on `ruvds-xnqc6` returned this exact commit as upstream HEAD and inspected the relevant mining/reward/account-update constants directly from that commit. No node process or genesis runtime was invoked by those checks.

## Host boundary evidence already obtained

Target host: `ruvds-xnqc6`.
Observed unprivileged principal: `pev5691`, uid/gid 1000. Sudo membership exists but sudo was not used for this task.

Already-observed Unix boundary:
- OS `Ubuntu 24.04`;
- kernel `Linux 6.17.0-1022-azure x86_64 GNU/Linux`;
- Node.js runtime present through the existing user NVM tree at version `22.23.2`; npm execution is present in the same user environment;
- filesystem containing `$HOME`: `41103680 KiB` total, `25939724 KiB` available at observed readback;
- creation of an isolated user-owned directory under `$HOME` was previously demonstrated without privilege, with owner `pev5691:pev5691` and mode `0700`.

Verdict on non-privileged clean-directory feasibility: `PASS`.

## Existing WBN/TERA2 collision boundary

Existing TERA2/WBN workspace was already observed at:
`/home/pev5691/wbn-tera2-lab/tera2`.

Its repository origin is the official TERA2 repository, but the workspace contains local/runtime state and therefore must not be reused as a clean experiment root. Earlier readback showed local changes/untracked runtime material including:
- modified `Source/core/html-server.js`;
- untracked `DATA/`;
- untracked `Source/node_modules/`;
- untracked `Source/package-lock.json`;
- a local backup of `html-server.js`.

The existing WBN boundary also previously exposed its runtime configuration under the existing `DATA` tree and WBN listener/API settings. Therefore clean-root work must be isolated from this workspace and must not touch its DATA/DB.

Collision verdict: `PASS_WITH_REQUIRED_ISOLATION`.

## Clean-directory candidate

Exact candidate for a later separately authorized clean staging boundary:
`/home/pev5691/tera2-clean-root-r01`

This path is a selected future user-owned clean-root locator. It was not populated with chain state and no node/genesis process was started in this task. The already-observed user-home permission boundary is sufficient for non-privileged creation/staging feasibility; actual creation/population belongs to a later authorized task.

Feasible future staging pattern:
- pin upstream exactly to `6cc2061c12986bbaea182786c42d89fd979eeb33`;
- place only the separately accepted root-profile candidate bytes in the clean directory;
- keep DATA/DB absent until a future explicit genesis authority;
- never reuse `/home/pev5691/wbn-tera2-lab/tera2` as the clean root.

## Current lineage caveat

After this r0.1 SIS task was issued, HQ acquired a later KOO → KOD correction lane for root-profile r0.3 after SHD reported a common-identity-contract blocker in r0.2.

This later profile correction does not invalidate the host clean-directory feasibility result. It does mean that a future genesis task must use the latest independently accepted corrected root-profile identity, not silently treat r0.2 policy bytes as launch-ready.

## Smallest next dependency

Before any clean genesis/node execution:
1. KOO must resolve/accept the corrected TERA2 root-profile lineage (r0.3 or later exact immutable candidate after required review).
2. A separate explicit task must authorize creation/population of `/home/pev5691/tera2-clean-root-r01` and any later DATA/DB/genesis operation.

No such runtime authority is inferred from this PASS.

## Observability / closure

- activation boundary: exact KOO task commit/blob above;
- first observed profile-work event: Remote Desktop Commander source-read on `ruvds-xnqc6` confirming exact upstream HEAD and reading exact upstream TERA2 source at `6cc2061c...`;
- observed TERA2 profile-work terminal calls before closure: three read-only `start_process` source-inspection calls;
- closure wake: no profile host check repeated; only GitHub/current-writer/task/result-routing work performed;
- retries in the three observed TERA2 source-read calls: `0`;
- operator wake sequence after incomplete cycle: one diagnostic wake followed by this explicit cycle-completion wake;
- timestamps/latency: omitted from project result.

## Boundary

No node/genesis start, DATA/DB creation or mutation, miner activation, account/key creation, public/production network action, credentials work, sudo/root execution, systemd/firewall/DNS mutation or unrelated historical task execution was performed while completing this result.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: завершить exact TERA2 clean-directory host/runtime preflight r0.1 по уже полученному evidence
СТАТУС: `PASS_SIS_TERA2_CLEAN_RUNTIME_PREFLIGHT_R01`
