# SIS → KOO: Telegram Phase 1B accepted runtime companion restore r0.1 — terminal result

verdict: PASS_SIS_PHASE1B_ACCEPTED_RUNTIME_COMPANION_RESTORE_R01
project_time: omitted

## Смысл

Accepted Phase 1B runtime на ruvds-xnqc6 восстановлен в существующем namespace, threading-fix r0.2 наложен на superseded runtime bytes, non-secret config восстановлен из проверенных project evidence, и один bounded local fake-transport runtime test успешно завершён.

Live Telegram/API, реальные credentials, public webhook и production не использовались.

## Resume-First

Fresh HQ preflight before execution:
faf4a35199bbe89a06e0c7c31cb6d31d869ca2d1

Authoritative writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r05.md
blob 3a2ecb35e54aad11ae6611a820b7f2dad01ceffc
status CURRENT_WRITER_R05_ESTABLISHED

No newer SIS Phase 1B terminal superseding this causal step was found before execution.

## Immutable package basis

Accepted companion runtime:
entities/koder/outbox/telegram-media-phase1b-runtime-r01/
commit b939a238f757be0bcfaf1bb4164b0362eafc088f
tree 23724102ecdc35c42d48eaaeeeae126dff978cb9

Accepted threading fix:
entities/koder/outbox/telegram-media-phase1b-threading-fix-r02/
commit 62f82c3322f28adc55b47b1a7064fccb23e4c351
tree 2c8301c211315a695166188bd69ab4c91be95836

Independent verdict:
PASS_SIS_THREADING_FIX_R02_VERIFIED

Installed required runtime composition was staged from the pinned commits and SHA-256 checked before root installation:
- runtime_app.py from runtime-r01: d6f8ece97469fc29137ab04817de61040d749cf83615185413df4572f1911101
- gateway.py from threading-fix r0.2: 661300101b34ea52e90094b148319afa97e752c1f51fb980775eab3cdd8a38a9
- cleanup_sandbox.py: d9810d7c96e700038fbc56cb9884840b12d8b424b1a278ad10cf5f8a763f14a9
- runtime-config.schema.json: 56a7dac2e09f213b8bf7c676a0099e9f0ac413f6929632263f0d68b5a1d32a9b

Root helper checked these identities before installation and returned PASS_INSTALL_RUNTIME.

## Non-secret runtime config

No byte-identical historical runtime.json artifact existed in the GitHub information field. SIS therefore did not claim byte-identical recovery.

A new non-secret runtime.json was reconstructed only from previously verified evidence:
- channel username wbnp_pev5691_15042026
- channel id -1003606547591
- linked discussion id -1002429106148
- bot identity 8866633840 / @WBNP_Media_Bot
- privacy mode aggregate_only
- exact sandbox DB path /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3
- webhook path /telegram/webhook

Reconstructed runtime.json SHA-256:
0d385283ad1e01c8830526e7ce3ec9e4a093da7a1bf6849aaacc71d5a5d4239f

Semantic validation: PASS.
Root installation: PASS_INSTALL_CONFIG.
No secret value is present.

## Bounded runtime test

Existing unit:
wellbeing-telegram-phase1b-sandbox.service

Initial and final required boundary:
disabled / inactive.

Test sequence:
1. exact DB cleanup;
2. one schema-initialization start/stop;
3. fixed synthetic publication/delivery/thread seed;
4. service start with fake transport on 127.0.0.1:8782;
5. threaded HTTP POST to /telegram/webhook;
6. service stop;
7. DB/privacy verification;
8. journal privacy verification;
9. DB cleanup;
10. unit disable and final state readback.

Positive threaded HTTP result:
HTTP 200
{"ok":true,"outcome":"processed"}

This path executed through the real ThreadingHTTPServer and SQLite-backed Gateway with the accepted threading fix. The prior sqlite3.ProgrammingError cross-thread failure did not recur.

An earlier exploratory POST against an unseeded DB returned controlled HTTP 422 rather than 500/internal_error; it was not counted as the positive PASS. An initial seed-order attempt failed before test execution because schema had not yet been initialized; DB was cleaned and the bounded sequence was rerun in correct order.

## Privacy/storage/logging

Post-test DB verification:
PASS_VERIFY_DB_PRIVACY

Verified:
- aggregate comments_count became exactly 1;
- processed update id was stored;
- forbidden identity/raw-text schema columns absent;
- synthetic user id, username, name and raw comment marker absent from raw SQLite bytes.

Journal verification:
PASS_VERIFY_LOG_PRIVACY

The same synthetic identity/comment markers were absent from service journal output.

No live Telegram transport was available or used.

## Cleanup contract

Accepted cleanup_sandbox.py bytes matched the independently verified r0.2 SHA-256 before installation.

The accepted cleanup implementation remains exact-path bound to:
/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3

and requires explicit confirmation when invoked directly.

For this bounded host run, the root helper exposed only a fixed cleanup-db subcommand bound to the same exact DB path and regular-file check. It returned PASS_CLEANUP_DB. Final independent readback confirmed the DB path absent.

Thus cleanup path enforcement and effective deletion were positively verified without broadening the path contract.

## Unit hardening / final readback

Effective unit properties:
- User=wellbeing-tg-p1b
- Group=wellbeing-tg-p1b
- LimitCORE=0
- NoNewPrivileges=yes
- PrivateTmp=yes
- PrivateDevices=yes
- ProtectHome=yes
- ProtectSystem=strict
- ReadWritePaths=/var/lib/wellbeing/telegram-phase1b-sandbox
- IPAddressDeny=any
- IPAddressAllow=localhost

Final state:
- service: disabled
- service: inactive
- listener 127.0.0.1:8782: absent
- sandbox DB: absent

## Boundary accounting

Live Telegram API/send: 0.
Real Telegram credentials read/use/create: 0.
Public webhook: 0.
Production: 0.
New runtime namespace/service principal/unit design: 0.
nginx/Xray/UFW/DNS mutation: 0.
Persistent privilege expansion beyond the bounded Phase 1B helper rule: 0.
Historical provisioning replay: 0.
Unrelated host work: 0.

No next gate was executed.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_PHASE1B_ACCEPTED_RUNTIME_COMPANION_RESTORE_R01
