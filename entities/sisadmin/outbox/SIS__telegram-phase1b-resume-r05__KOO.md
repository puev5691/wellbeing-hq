# SIS → KOO: Telegram Phase 1B resume gate r0.5

verdict: `WAITING_OPERATOR_EXACT_HUMAN_ACTION`
production: `no`
live_telegram: `no`
privileged_execution_in_this_pass: `no`
project_time: omitted; trusted project-time source not used

## Resume-First boundary

fresh_HQ_preflight_HEAD: `24cf9f5269831930c71ff2ef5f73db1b8b3f7221`
fresh_HQ_prewrite_HEAD: `94b3bf0eae815314c5377a548c16b7188aba8ff6`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found_at_prewrite_boundary`

Exact r0.5 task:
`entities/koordinator/outbox/KOO__telegram-phase1b-resume-after-erefia-r05__SIS.md`
commit `81e686eee63ddbcf45a527345f58cf942068cdae`
blob `5d8431d2bba17cd3e23eab2ecb71fc9a42a0748c`.

Historical r0.4 was read as evidence. The historical v1 one-shot was not executed or replayed.

## Fresh host/tooling readback

Host: `ruvds-xnqc6`; current DC principal: `pev5691`.

Observed bounded sandbox state:
- service user `wellbeing-tg-p1b` exists with home `/nonexistent`, shell `/usr/sbin/nologin`, primary group `wellbeing-tg-p1b`;
- `/opt/wellbeing/telegram-phase1b-runtime-r01` exists, owner `root:wellbeing-tg-p1b`, mode `0750`;
- `/etc/wellbeing/telegram-phase1b` exists, owner `root:wellbeing-tg-p1b`, mode `0750`;
- `/var/lib/wellbeing/telegram-phase1b-sandbox` exists, owner `wellbeing-tg-p1b:wellbeing-tg-p1b`, mode `0750`;
- `/etc/systemd/system/wellbeing-telegram-phase1b-sandbox.service` exists, owner `root:root`, mode `0644`;
- unit is `inactive` and `disabled`;
- exact sandbox DB is absent;
- port `8782` has no listener;
- `runtime.json` is absent.

Resume-aware script:
`/home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once-v2.sh`
SHA-256 `1208ff4e123afcd407115c476c549b7c24730624dc2e01bd0c2751ad448e9d3d` = expected r0.4 identity `PASS`.

Staged package identity:
- source commit `b939a238f757be0bcfaf1bb4164b0362eafc088f`;
- source tree `23724102ecdc35c42d48eaaeeeae126dff978cb9`;
- staged `SHA256SUMS.txt`: 13/13 `PASS`;
- installed unit matches staged unit exactly.

Current unit effective hardening readback includes:
`User=wellbeing-tg-p1b`, `Group=wellbeing-tg-p1b`, `LimitCORE=0`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, `PrivateDevices=yes`, `ProtectSystem=strict`, `ProtectHome=yes`, loopback-only IP allow and global IP deny, and the exact sandbox state path as `ReadWritePaths`.

Apport is currently active and `kernel.core_pattern` is piped to Apport. The verified v2 script explicitly handles this boundary only during its bounded synthetic test and restores Apport on exit.

The existing `host-gate-evidence.txt` is stale evidence from the historical failed v1 pass and ends at `HOST_GATE=FAIL reason=user_collision`; it cannot support a PASS.

## Decision

The host gate is **not already proven satisfied**. The missing evidence is the v2 bounded synthetic runtime/privacy pass and cleanup/readback. The verified v2 script remains the smallest current bounded mechanism because it is resume-aware and first validates the exact pre-existing sandbox objects before any privileged mutation.

The v2 script requires UID 0. Current DC principal is unprivileged `pev5691`; no password/privileged credential is available to SIS and no privilege-bypass workaround is authorized. Therefore one interactive OPERATOR sudo action is genuinely required.

Fresh transport readback:
- `uk.wbnetrus.ru` resolves to `185.39.19.240`;
- `ruvds-xnqc6` `eth0` is `185.39.19.240/24`;
- SSH listens on port `2222`.

## One exact Termux human-action block

```sh
ssh -t -p 2222 pev5691@uk.wbnetrus.ru 'sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once-v2.sh; rc=$?; echo; echo "=== SIS RETURN r05 ==="; tail -n 100 /home/pev5691/sis-phase1b-tooling/host-gate-evidence.txt 2>/dev/null || true; echo "SCRIPT_RC=$rc"'
```

OPERATOR enters only the existing SSH/sudo password if requested. Passwords, tokens and secrets must not be pasted into chat or GitHub.

After this one block, SIS must read back the fresh evidence and return the final host-gate verdict. No live Telegram call is authorized by this result.

## Boundary

No historical sudo command was replayed. No live Telegram API call, real Telegram credential, public webhook, production deployment, nginx/Xray/TERA2/UFW/DNS mutation or destructive cleanup occurred in this r0.5 pass.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть KOO fresh Phase1B resume-gate и единственное необходимое интерактивное действие
СТАТУС: waiting_operator_exact_human_action
