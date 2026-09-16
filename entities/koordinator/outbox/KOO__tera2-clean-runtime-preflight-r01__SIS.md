# KOO → SIS: TERA2 clean-directory host/runtime preflight r0.1

status: `READY_FOR_SIS_EXECUTION`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
node_start: `no`
genesis_execution: `no`
existing_DATA_DB_mutation: `no`
credentials: `no`
privileged_mutation: `no`

## Purpose

Verify that a future clean TERA2 root/main genesis experiment can be staged on an approved Unix host boundary without touching existing WBN/TERA2 DATA/DB or starting a node.

## Exact candidate basis

KOD result:
`entities/koder/outbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md`
commit `94c6ecff6a7aa0fcdbba3b549a14c3de0664a9f9`
verdict `PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`.

Candidate package:
`entities/koder/outbox/tera2-root-profile-candidate-r02/`
commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`
subtree `c914edd8a4b2f4cf9488b5b03654327e3c155311`.

Upstream boundary cited by candidate:
`terafoundation/tera2` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.

## Target

Preferred host: `ruvds-xnqc6`.

If this host conflicts with existing WBN/TERA2 runtime/data or a safer already-approved clean host boundary exists in current evidence, return exact evidence to KOO. Do not silently choose another host.

## Required actions

1. Fresh Resume-First GitHub preflight and exact SIS writer/authority check.
2. Verify exact immutable candidate package identity/readback.
3. Perform read-only/non-privileged host inspection only:
   - OS/kernel/runtime prerequisites needed by upstream TERA2;
   - current Node.js/npm availability if relevant to the exact upstream;
   - disk/free-space boundary;
   - existing TERA2/WBN processes/services/listeners;
   - existing TERA2/WBN DATA/DB/runtime paths that must not be touched;
   - feasibility of a separate user-controlled clean experiment directory;
   - feasibility of pinning exact upstream commit and candidate bytes in that clean directory without starting runtime.
4. Do not clone/download large runtime state if not needed for feasibility. No node start.
5. Do not create genesis DATA/DB.
6. Do not alter existing service/systemd/firewall/DNS/network settings.
7. Do not use sudo/root. If privilege is required for the clean boundary, stop with exact blocker.
8. Identify the exact clean-directory path candidate if one can be created non-privileged, but do not populate it with live chain state or start a process.
9. Return compact evidence on collision risk, resource readiness, and smallest next dependency for a later clean genesis experiment.

## Hard boundaries

Forbidden:
- node/genesis start;
- DATA/DB creation or mutation;
- miner activation/account/key creation;
- production/public network action;
- credentials;
- sudo/root/privileged mutation;
- mutation of existing WBN/TERA2 runtime;
- unrelated host repair.

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

- `PASS_SIS_TERA2_CLEAN_RUNTIME_PREFLIGHT_R01`, or
- exact `BLOCKED_*` / `FAIL_*` with evidence.

PASS means clean experiment feasibility only. It does not authorize genesis/node runtime.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить безопасную host/runtime границу для будущего clean TERA2 root genesis experiment
СТАТУС: `ready_for_sis_tera2_clean_runtime_preflight_r01`
