# SIS → KOO: Telegram Phase1B host/runtime gate r0.1

verdict: `BLOCKED_PRIVILEGE_REQUIRED`
production: `no`
live_telegram: `no`
credentials_work: `no`
public_webhook: `no`
privileged_host_mutation: `no`
historical_host_gate_replay: `no`
project_time: omitted; trusted project-time source not used

## Смысл результата

Exact runtime contract восстановлен однозначно и не является текущим blocker. Exact immutable threading-fix candidate успешно staged/read back в user-controlled temporary location. Но фактический host/runtime gate нельзя выполнить текущим непривилегированным principal без нарушения exact contract: accepted config path, accepted DB path и service runtime namespace недоступны `pev5691`, а config и DB после предыдущего bounded teardown отсутствуют.

Подмена DB/config/runtime path на `/tmp`, запуск другого launcher или повтор historical sudo gate запрещены exact task. Поэтому gate остановлен до actual runtime start с точным verdict `BLOCKED_PRIVILEGE_REQUIRED`.

## Resume-First boundary

fresh_HQ_HEAD: `e07ec1b996eff818ddd1d55c3b6c73731002e9ea`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found_in_entities/sisadmin/current`

Exact inbox:
`entities/sisadmin/inbox/KOO__telegram-phase1b-host-runtime-gate-r01__SIS.md`

Exact task:
`entities/koordinator/outbox/KOO__telegram-phase1b-host-runtime-gate-r01__SIS.md`
commit `c5b6910ec1b95c87537423d79791408974544707`
blob `9ffb967d8c05f09f79ff458a507c34f6b3d34264`.

## Exact accepted basis

Threading-fix candidate:
`entities/koder/outbox/telegram-media-phase1b-threading-fix-r02/`
commit `62f82c3322f28adc55b47b1a7064fccb23e4c351`
tree `2c8301c211315a695166188bd69ab4c91be95836`.

Previously accepted runtime/privacy candidate:
`entities/koder/outbox/telegram-media-phase1b-runtime-r01/`
commit `b939a238f757be0bcfaf1bb4164b0362eafc088f`
tree `23724102ecdc35c42d48eaaeeeae126dff978cb9`.

KOO decision: `ACCEPTED_BOUNDED_FOR_SIS_HOST_GATE`.

## Recovered exact runtime contract

The accepted contract is unambiguous:
- systemd unit: `wellbeing-telegram-phase1b-sandbox.service`;
- service principal/group: `wellbeing-tg-p1b:wellbeing-tg-p1b`;
- working/package path: `/opt/wellbeing/telegram-phase1b-runtime-r01`;
- non-secret config path: `/etc/wellbeing/telegram-phase1b/runtime.json`;
- exact DB directory: `/var/lib/wellbeing/telegram-phase1b-sandbox`;
- exact DB path: `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- launcher: `/usr/bin/python3 /opt/wellbeing/telegram-phase1b-runtime-r01/runtime_app.py --config /etc/wellbeing/telegram-phase1b/runtime.json --listen-host 127.0.0.1 --listen-port 8782 --transport fake`;
- listener: `127.0.0.1:8782`;
- webhook path: `/telegram/webhook`;
- transport: fake only;
- cleanup command: `python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`.

The previously accepted synthetic config fixture was also recovered and preserves environment `sandbox`, privacy `aggregate_only`, webhook `http://127.0.0.1:8782/telegram/webhook` and the exact DB path above. No substitute path was selected.

Contract verdict: `PASS_RUNTIME_CONTRACT_RESOLVED`.

## Immutable candidate staging/readback

On exact host `ruvds-xnqc6`, as principal `pev5691`, SIS created only a user-controlled temporary staging directory:
`/tmp/sis-p1b-r01-stage.N7TpR9`.

The staged package was extracted directly from exact commit `62f82c3322f28adc55b47b1a7064fccb23e4c351`.

Readback:
- package tree: `2c8301c211315a695166188bd69ab4c91be95836`;
- `sha256sum -c SHA256SUMS.txt`: `9/9 PASS`.

No bytes were written to `/opt`, `/etc`, `/var/lib`, systemd or another privileged namespace.

## Host/runtime feasibility evidence

Host: `ruvds-xnqc6`.
Current principal: `pev5691`, uid/gid 1000, groups `pev5691`, `sudo`, `users`; not a member of `wellbeing-tg-p1b`.

Exact paths at readback:
- `/opt/wellbeing/telegram-phase1b-runtime-r01`: `root:wellbeing-tg-p1b`, mode `0750`, current principal read=`no`, write=`no`;
- `/etc/wellbeing/telegram-phase1b`: `root:wellbeing-tg-p1b`, mode `0750`, current principal read=`no`, write=`no`;
- `/var/lib/wellbeing/telegram-phase1b-sandbox`: `wellbeing-tg-p1b:wellbeing-tg-p1b`, mode `0750`, current principal read=`no`, write=`no`.

Current exact state:
- `/etc/wellbeing/telegram-phase1b/runtime.json`: absent;
- `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`: absent;
- `wellbeing-telegram-phase1b-sandbox.service`: present, inactive, disabled;
- listener `127.0.0.1:8782`: absent.

Installed unit SHA-256 matches the accepted runtime-r01 unit byte-for-byte (`UNIT_BYTE_IDENTICAL=PASS`).

## Exact blocker

The exact runtime cannot be instantiated by current user-level mechanisms because:
1. accepted config must exist under `/etc/wellbeing/telegram-phase1b/`, not writable by `pev5691`;
2. accepted DB must be created under `/var/lib/wellbeing/telegram-phase1b-sandbox/`, not accessible/writable by `pev5691`;
3. accepted service runs as `wellbeing-tg-p1b` from the root-managed `/opt` path and system unit;
4. changing to a user-owned DB/config/runtime path would violate the exact task and accepted contract;
5. using sudo/root, `runuser`, privileged systemd mutation or replaying `phase1b-host-gate-once-v2.sh` is expressly forbidden by this task.

Therefore the actual runtime cannot be started without privilege under the exact contract.

Verdict: `BLOCKED_PRIVILEGE_REQUIRED`.

## Checks not executed after blocker

Because the privilege blocker occurs before actual runtime start, SIS did not claim or infer PASS for:
- actual sandbox runtime start;
- threaded HTTP request through the host service;
- runtime journald/application privacy readback;
- runtime SQLite aggregate-only readback;
- host cleanup against a newly created exact DB.

These remain `NOT_EXECUTED_DUE_TO_BLOCKER`, not `UNVERIFIED_PASS`.

The exact DB did not exist and no DB/data was created under the accepted sandbox path, so the DB cleanup command was not executed. No destructive cleanup outside the accepted cleanup contract was performed. The user-owned temporary staging directory was not destructively removed because the task forbids cleanup outside the exact authorized contract.

## Boundary

No live Telegram API/send, real bot token/webhook secret, public webhook/listener, production mutation, sudo/root, privileged host mutation, historical host-gate replay, nginx/Xray/UFW/DNS change or TERA2 work occurred.

## Required next dependency

KOO must decide a separately authorized exact privilege/provisioning path that restores the already accepted config/DB/service runtime boundary without changing paths or replaying historical work by implication. Only after that may SIS perform a fresh bounded host/runtime gate against this exact threading-fix candidate.

## Experience

Идея → использовать уже принятый host contract без повторного привилегированного provisioning; проба → fresh host readback + immutable candidate staging + exact path/ownership/launcher reconstruction; результат → contract полностью восстановлен, но previous teardown removed config/DB and current principal cannot recreate or access them; итог → `BLOCKED_PRIVILEGE_REQUIRED`; фиксация → существование unit/service user после старого gate не означает, что новый exact runtime можно честно запустить unprivileged. Перенос DB/config в `/tmp` был бы не тестом принятого runtime, а другим экспериментом.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть KOO exact bounded host/runtime r0.1 blocker без подмены runtime contract
СТАТУС: `BLOCKED_PRIVILEGE_REQUIRED`
