# SIS → KOO: Telegram Phase 1B runtime/privacy readiness r2 result

status: `BLOCKED_PRE_LIVE_RUNTIME_PRIVACY_READINESS`
source_task_commit: `50cafb27a954026c8bc54c4fb2d89b126afa6f53`
source_task_blob: `5601f9402b586b8f78ecb17ae463c1f2169bad96`
accepted_package_commit: `cd81bbd98a4be334388f95ea948427d91fa82a05`
privacy_mode: `aggregate_only`
production: `no`
live_send: `no`
credential_values_used_or_published: `no`

## Verified package/runtime evidence

Fresh host checkout at exact package commit matched `cd81bbd98a4be334388f95ea948427d91fa82a05`. `sha256sum -c SHA256SUMS.txt`: 9/9 PASS. `python3 -m unittest -v`: 23/23 PASS.

Candidate code does not persist audience identity or raw comment text in SQLite. `processed_updates` stores only `update_id`; `aggregates` stores aggregate counts; there is no per-user/raw-comment table. Package static inspection found no application logger or retry/dead-letter store. Existing nginx readable configuration contains no `$request_body` logging directive.

Exact cleanup command executed on the host against the required path and returned `already_absent`:
`python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`.
The helper also has exact-path and exact-confirmation enforcement covered by tests.

## Exact blockers

### B1. Exact sandbox DB path is not currently provisioned/writable

Chosen non-production verification host: `ruvds-xnqc6`.
Runtime inspection as current unprivileged principal `pev5691`:
- `/var/lib/wellbeing` absent;
- `/var/lib/wellbeing/telegram-phase1b-sandbox` absent;
- exact DB absent;
- `/var/lib` is `root:root`, mode `0755`, not writable by `pev5691`;
- direct SQLite open/create at `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3` fails with `sqlite3.OperationalError: unable to open database file`.

Therefore the exact DB contract is not live-feasible until a separately authorized privileged provisioning step creates the directory and assigns an explicit service principal/ownership/mode. SIS did not improvise a different path because the KOO task forbids silent substitution.

### B2. Crash/debug persistence policy is not yet instantiated for a Phase 1B runtime service

The accepted package contains library/gateway code and tests, but no selected/installed Phase 1B service unit or webhook application runtime. Host `core_pattern` routes crashes through Ubuntu Apport. Without an exact future service definition, SIS cannot prove that crash/debug handling for that service will never persist request bodies or in-memory audience/comment data. A future bounded runtime must explicitly disable/limit core capture for this service and avoid debug/local-variable dumps before privacy readiness can PASS.

Existing nginx access configuration does not log request bodies, but no Phase 1B webhook location/upstream exists yet, so end-to-end proxy/application logging for the future webhook cannot be declared verified.

## Non-secret secret-storage contract for later authorization

Host systemd version is 255, so the preferred mechanism is systemd credentials rather than GitHub/config-file secret values:
- credential slot `telegram_bot_token`;
- credential slot `telegram_webhook_secret`;
- persistent secret source, if later separately provisioned: root-controlled systemd credential store, not repository content;
- runtime exposure: `/run/credentials/<phase1b-unit>/telegram_bot_token` and `/run/credentials/<phase1b-unit>/telegram_webhook_secret` via `LoadCredential=` / `LoadCredentialEncrypted=`;
- no token or webhook secret value is required or present for this task.

This is a non-secret mechanism/schema only, not credential creation or deployment.

## Exact remaining dependencies before one bounded sandbox send

1. Verified numeric `channel_chat_id` for the target experimental channel.
2. Verified `discussion_linked` state and, if true, verified numeric `discussion_chat_id`.
3. Exact publisher bot identity plus proof of required channel/admin rights.
4. Exact webhook endpoint and selected non-production application runtime/service definition.
5. Privileged provisioning of `/var/lib/wellbeing/telegram-phase1b-sandbox/` with explicit service owner/group and restrictive mode, followed by writable/readback test at the exact DB path.
6. Runtime privacy hardening/readback for crash/debug handling and the actual webhook proxy/application logging path.
7. Separate authorization/provisioning of bot token and webhook secret through the approved secret mechanism.

Until B1 and B2 are closed, future bounded sandbox send is `NOT_READY` even if channel IDs and bot rights become available.

## Check boundary

No Telegram API call, live send, production deployment, channel administration change, credential creation or credential publication occurred.

## Experience

Идея → проверить accepted package не только по тестам, но и на реальном host/runtime boundary; проба → exact checkout + 9/9 checksum + 23/23 tests + exact cleanup invocation + filesystem/nginx/crash-policy inspection; результат → code/privacy storage contract PASS, но exact `/var/lib` path неприменим текущему unprivileged principal и crash/webhook runtime policy ещё не существует; итог → bounded blocker; фиксация → pre-live privacy PASS нельзя выводить из package tests, пока exact host path и runtime logging/crash boundary не проверены на реальном сервисе.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть KOO bounded non-production runtime/privacy verification exact accepted Phase 1B package
СТАТУС: blocked_pre_live_runtime_privacy_readiness
