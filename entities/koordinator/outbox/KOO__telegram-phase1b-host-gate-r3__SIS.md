# KOO → SIS: Telegram Phase 1B bounded host provisioning/readiness r3

status: `TASKED_BOUNDED_NONPRODUCTION_HOST_GATE`
production: no
live_telegram_send: forbidden
real_credentials: forbidden
public_endpoint: forbidden
mazhor_scope: excluded_by_operator_direct_control
project_time: omitted; trusted project-time source not used

## Exact inputs

Accepted KOD result:
`entities/koder/outbox/KOD__telegram-phase1b-runtime-privacy-remediation-r1__KOO.md`
commit: `97ae071f82de36757c99c3e7de4268efacc6ec28`
blob: `bc9d8630d4ce4fd55c51d71ac014dd7f52eeaf33`

Accepted candidate package:
`entities/koder/outbox/telegram-media-phase1b-runtime-r01/`
commit: `b939a238f757be0bcfaf1bb4164b0362eafc088f`
tree: `23724102ecdc35c42d48eaaeeeae126dff978cb9`

Previous SIS blocker result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-runtime-privacy-readiness-r2-result__KOO.md`
commit: `cff383e86644c6278b98db6a6d3769ab0fab8b5d`.

Previously selected verification host:
`ruvds-xnqc6`.

## OPERATOR boundary

SHD is currently working under direct OPERATOR control on MAZHOR. SIS must not use, provision or alter MAZHOR for this task.

## Step 1 — host-scope preflight

Freshly verify whether `ruvds-xnqc6` is still suitable for this bounded non-production sandbox pass.

Before mutation, confirm:
- no conflict with current production/security-sensitive service scope;
- no collision with existing service/user/path names;
- privileged provisioning is available;
- rollback/cleanup is possible.

If suitability cannot be confirmed, return:
`BLOCKED_NONPRODUCTION_HOST_SCOPE_NOT_CONFIRMED`
with exact reason. Do not silently select another host.

## Step 2 — bounded provisioning, only if Step 1 PASS

Provision the candidate exactly enough to verify B1 + host-instantiated B2:

- system principal/group: `wellbeing-tg-p1b:wellbeing-tg-p1b`;
- package working directory:
  `/opt/wellbeing/telegram-phase1b-runtime-r01`;
- non-secret config directory:
  `/etc/wellbeing/telegram-phase1b`;
- exact DB directory:
  `/var/lib/wellbeing/telegram-phase1b-sandbox`;
- exact DB:
  `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- candidate unit:
  `wellbeing-telegram-phase1b-sandbox.service`;
- exact listener:
  `127.0.0.1:8782`;
- transport: fake only.

Use ownership/modes and hardening from package `RUNTIME-CONTRACT.md` and the candidate systemd unit. No real Telegram credentials or public reverse proxy.

## Step 3 — host verification

Verify and report exact evidence for:

1. user/group and directory ownership/modes;
2. exact DB creation/writability and DB file mode no broader than expected;
3. effective unit properties including `LimitCORE=0`, user/group, hardening and writable path;
4. loopback listener present and no public bind on 8782;
5. host coredump/Apport behavior sufficient to rule out service memory core persistence, or exact blocker if this cannot be proved;
6. journald/application logs using only synthetic payloads:
   - synthetic user ID,
   - synthetic username/name,
   - synthetic raw comment text
   must produce zero persistent matches;
7. no proxy/wrapper/debug/retry store persists raw body/identity/comment text;
8. exact cleanup command remains executable against the provisioned DB:
   `python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`.

Do not perform cleanup until verification evidence that requires the DB is collected; then cleanup may be run as the final bounded sandbox teardown if doing so does not destroy evidence needed for the report.

## Step 4 — verdict

Return exactly one:

- `PASS_B1_B2_HOST_GATE` if B1 and host-instantiated B2 are both proved;
- `BLOCKED_HOST_GATE` with exact remaining blockers.

Even on PASS:
- no live Telegram send is authorized;
- no real bot token/webhook secret is authorized;
- no public webhook/TLS endpoint is authorized;
- no production deployment is authorized.

## Output

Primary result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-host-gate-r3-result__KOO.md`

Return through Exchange Gate:
- dispatch:
  `routes/dispatch/SIS__telegram-phase1b-host-gate-r3-result__KOO.md`
- KOO inbox:
  `entities/koordinator/inbox/SIS__telegram-phase1b-host-gate-r3-result__KOO.md`
- sender registry:
  `registry/by-sender/sisadmin.jsonl`

Perform immutable readback of exact result identities.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить на реальном non-production host закрытие SIS B1 и host-instantiated B2 без MAZHOR, live Telegram, credentials или production
СТАТУС: tasked_bounded_nonproduction_host_gate
