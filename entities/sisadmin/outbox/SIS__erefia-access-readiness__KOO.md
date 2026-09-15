# SIS → KOO: readiness доступа к эРэФии

status: `WAITING_OPERATOR_EXACT_HUMAN_ACTION_AFTER_AUTOMATED_PATHS_EXHAUSTED`
production_mutation: `no`
tera_wbn_mutation: `no`
telegram_phase1b: `PAUSED_BY_HIGHER_CURRENT_PRIORITY`
project_time: omitted; trusted project-time source not used

## Fresh Resume-First boundary

fresh_HQ_HEAD: `bceae0e1ba79d0bc6ec851badc54afd51ddf7398`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found_at_fresh_boundary`

Exact KOO task:
`entities/koordinator/outbox/KOO__sis-current-priority-erefia-access__SIS.md`
commit `bcaeccfefb992aafab16c3c7b0678d0072c65a5e`
blob `6e0c6e2dde96699c867d197207c872748ceb77b7`.

## Exact host identity

Host label: `эРэФия`.
Exact SSH endpoint: `194.87.107.135:2222`.
Port 22 is not used as current SSH endpoint.

Verified earlier SHD hosting-panel evidence:
- public IP `194.87.107.135`;
- Ubuntu 24.04 LTS;
- 2 GiB RAM, 40 GiB HDD;
- administrative login `root`;
- password remains OPERATOR secret and is not stored/published.

Immutable evidence source:
`entities/shardovik/outbox/SHD__erefia-exact-locator-live-node__SIS.md`
commit `a9b70ded72d743e2abc5438d7f40afa7d9d197cf`.

## What was independently checked in this SIS pass

1. `194.87.107.135:2222` is TCP-open; sshd responds with OpenSSH Ubuntu banner.
2. Existing batch key-auth attempts from available SIS-controlled hosts do not authenticate:
   - `pev5691@194.87.107.135:2222` from Буржуиния → `Permission denied (publickey,password)`;
   - `shd@194.87.107.135:2222` from МАЖОР → same;
   - confirmed admin `root@194.87.107.135:2222` from Буржуиния → same.
3. Буржуиния already had a known-host entry for `[194.87.107.135]:2222`, proving prior SSH contact with this exact endpoint, but not current authentication capability.
4. Remote Desktop Commander device list contains:
   - `ruvds-xnqc6` — online;
   - `p552203.kvmvps` — intermittently online during the pass;
   - `ruvds-ygo0w` — offline, device id `c55d5659-f2c8-416d-8b40-9bac8c80c30d`, created after the older SHD state that said Erefia Commander was not registered/online.
   The link `ruvds-ygo0w ↔ эРэФия` remains plausible but unproved; it is not promoted to fact.
5. On working Буржуиния the DC runtime is confirmed as a tmux-hosted process using `npx @wonderwhy-er/desktop-commander@latest remote`; no systemd DC service is used there.
6. Provider-side automatic alternatives were checked:
   - no RUVDS/provider CLI/config path found on Буржуиния;
   - HQ GitHub Actions contains activation/exchange-gate workflows only; no SSH/deploy workflow exists for Erefia.
7. Public WBN API `:8780` remains live and returns `NETWORK=WELLBEING`, `SHARD_NAME=WBN`; it exposes no hostname useful for proving `ruvds-ygo0w` identity.
8. An attempt to use a local private SSH key explicitly was blocked by the tool security boundary; SIS did not bypass that protection and did not read/export key material.

## Commander state

`NOT_READY_ON_EXACT_HOST`.

Host network and sshd are alive. The remaining exact blocker is administrative authentication: no machine-usable credential path available to this chat/connected hosts can authenticate as confirmed admin `root` on port 2222.

## Exact remaining human action

Only after the automated paths above were exhausted, the minimal OPERATOR action is now:

1. SSH once to `root@194.87.107.135` on port `2222` using the existing OPERATOR-held password/credential.
2. Run one SIS-provided diagnostic/restart block that only checks/returns existing DC runtime and starts the already-present DC runtime if its prerequisites are present; it must not change TERA/WBN.

Credentials must not be pasted into chat or GitHub.

This replaces the earlier weaker request to return only `hostname && id -un`; host identity and admin login are already established from accepted hosting-panel evidence.

## Boundary

TERA/WBN service, chain identity, DB, DATA, genesis/reward logic, shard.js, const.lst, blockchain ports, nginx, Xray, UFW and DNS were not modified.
No credentials were created, read, reconstructed or published.
Telegram Phase1B was not resumed or executed in parallel.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: зафиксировать DC-first автоматическую проверку и минимальный остаточный human gate для exact Erefia access lane
СТАТУС: waiting_operator_exact_human_action_after_automated_paths_exhausted
