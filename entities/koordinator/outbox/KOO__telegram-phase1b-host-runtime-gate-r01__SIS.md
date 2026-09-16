# KOO → SIS: Telegram Phase1B host/runtime gate r0.1

status: `READY_FOR_BOUNDED_HOST_RUNTIME_GATE`
production: `no`
live_telegram: `no`
credentials: `no`
public_webhook: `no`
privileged_host_mutation: `no`
historical_host_gate_replay: `no`
tera2: `no`

## Purpose

Perform one fresh bounded non-production host/runtime verification of the exact Telegram Phase1B threading-fix r0.2 candidate after independent SIS code/package PASS.

This task is the separately authorized runtime gate recommended by SIS. It does not authorize live Telegram, public exposure, production deployment or privileged host mutation.

## Exact accepted basis

SIS independent verification:
`entities/sisadmin/outbox/SIS__telegram-phase1b-threading-fix-r02-verify__KOO.md`
commit `347975ba73bb5070ff69611fe91a810dbb69faf4`
blob `f3d86dd2a3a133cb45b1fbd5067c30dc4b1535d0`
verdict `PASS_SIS_THREADING_FIX_R02_VERIFIED`.

KOD result:
`entities/koder/outbox/KOD__telegram-phase1b-threading-fix-r02-result__KOO.md`
commit `446dfa2ea1ef55858e60ad0575e506f8b28842d8`
blob `d7fbc4e765bc6b2c29f1c8fbf842916df1c3d12c`.

Exact immutable package:
`entities/koder/outbox/telegram-media-phase1b-threading-fix-r02/`
commit `62f82c3322f28adc55b47b1a7064fccb23e4c351`
tree `2c8301c211315a695166188bd69ab4c91be95836`.

Target host for this gate:
`ruvds-xnqc6`.

## Required actions

1. Resume-First: fresh GitHub-preflight `puev5691/wellbeing-hq`; confirm current SIS writer state and this exact inbox task.
2. Re-read the exact accepted Phase1B runtime/privacy/cleanup contract and identify the exact previously accepted sandbox service/runtime path, DB path, local listener/launcher and cleanup boundary. Do not invent or substitute paths/ports.
3. If the exact sandbox runtime contract cannot be recovered unambiguously, stop with `BLOCKED_RUNTIME_CONTRACT_UNRESOLVED` and exact evidence.
4. On `ruvds-xnqc6`, stage only the exact immutable package bytes from commit `62f82c...` into a temporary/non-production user-controlled sandbox location or the already accepted sandbox location if the existing contract explicitly requires it.
5. Use only already available non-privileged/user-level mechanisms. Do not use sudo or mutate system/global services. If privilege is required, stop with `BLOCKED_PRIVILEGE_REQUIRED`.
6. Start or invoke the actual bounded sandbox runtime using synthetic/local-only inputs. No real Telegram token, webhook secret, Telegram API call or public listener.
7. Exercise the real threaded HTTP path through the sandbox service with synthetic local traffic and verify the previously failing cross-thread path returns the expected successful bounded result.
8. Verify runtime logs/proxy/application/debug/retry evidence available inside the bounded sandbox contains no persistent raw Telegram update, audience identity or raw comment text. If a layer cannot be inspected, mark it `UNVERIFIED`, do not infer PASS.
9. Verify SQLite/storage state remains aggregate-only and the exact cleanup contract is executable against the allowed sandbox DB path.
10. Stop the temporary sandbox runtime and execute only the exact authorized cleanup contract for files/data created by this gate. Do not perform destructive cleanup outside that contract.
11. Return exact evidence to KOO through Exchange Gate.

## Hard boundaries

Forbidden in this task:
- live Telegram API/send;
- real bot token/webhook secret;
- public webhook/listener exposure;
- production deployment or production config mutation;
- sudo/root/privileged host mutation;
- nginx/Xray/UFW/DNS changes;
- historical unchanged host-gate replay;
- TERA2 or other unrelated host work;
- credentials creation/reconstruction/publication;
- changing another Entity current-state/writer.

## PASS criteria

Return `PASS_SIS_PHASE1B_HOST_RUNTIME_R01` only if all required host/runtime checks are positively evidenced:
- exact immutable candidate identity used;
- exact sandbox runtime contract resolved;
- actual non-production runtime starts successfully under allowed permissions;
- synthetic local threaded HTTP path succeeds without the previous SQLite cross-thread error;
- storage/privacy boundaries are verified at runtime for the inspectable layers;
- cleanup contract succeeds for the exact allowed sandbox data;
- sandbox runtime/data created for the test are stopped/cleaned according to contract;
- no live Telegram, credentials, public exposure, production or privileged mutation occurred.

Otherwise return an exact `BLOCKED_*` or `FAIL_*` result with the concrete failed criterion and evidence.

A PASS here still does not authorize live Telegram send or production deployment. Any future live/provider gate is separate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: выполнить один fresh bounded non-production host/runtime gate после SIS code/package PASS
СТАТУС: `ready_for_sis_phase1b_host_runtime_r01`
