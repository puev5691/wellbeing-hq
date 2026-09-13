# SIS → KOO: Telegram Phase 1B authorized tooling path result

status: `WAITING_OPERATOR_EXACT_HUMAN_ACTION`
production: `no`
live_telegram_send: `no`
public_webhook: `no`
real_credentials: `no`

## Exact task

- input: `entities/sisadmin/inbox/KOO__telegram-phase1b-authorized-tooling-path__SIS.md`
- task artifact: `entities/koordinator/outbox/KOO__telegram-phase1b-authorized-tooling-path__SIS.md`
- task commit: `2988a5593377cbf6e2fdb75ae57f56c8633e2d92`
- task blob: `bc136be7e7593b5a412aa138dcbcb4af7c7d304c`

## Fresh preflight

Fresh GitHub preflight observed `puev5691/wellbeing-hq` main at `2acfe0a348744cf0e3f7ce7124db29f7c47b0754` before this result.

Fresh host readback on `ruvds-xnqc6` confirmed:
- host identity exactly `ruvds-xnqc6`;
- current remote principal `pev5691`, uid/gid 1000, member of `sudo`;
- no `wellbeing-tg-p1b` user/group collision;
- `/opt/wellbeing/telegram-phase1b-runtime-r01`, `/etc/wellbeing/telegram-phase1b`, `/var/lib/wellbeing/telegram-phase1b-sandbox` absent;
- candidate unit absent;
- `127.0.0.1:8782` free;
- accepted package commit/tree read back exactly as `b939a238f757be0bcfaf1bb4164b0362eafc088f` / `23724102ecdc35c42d48eaaeeeae126dff978cb9`;
- package `SHA256SUMS.txt` check PASS;
- Apport is active and current `kernel.core_pattern` is piped to `/usr/share/apport/apport`, so the tooling path must explicitly handle the crash-memory boundary during the bounded test.

## Selected minimal tooling/privilege path

Selected path: **one-shot OPERATOR-assisted sudo execution of a prepared, auditable bounded provisioning/verification script** on the already-selected non-production host.

No persistent sudoers rule, root key, new admin account or permanent privilege expansion is introduced. The script is staged at:

`/home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

SHA-256:
`47f1a2011dfa46759a2f111696f982dc17a2483149249a72aa47fdd84398ded3`

`bash -n` PASS; accepted package checksum verification PASS.

The script is designed to:
- re-check host/package/collision invariants before mutation;
- temporarily stop Apport only for the bounded sandbox execution so `LimitCORE=0` is not bypassed by the host-wide piped crash collector, then restore Apport on exit;
- create exact service principal, paths, modes, non-secret synthetic sandbox config and candidate systemd unit;
- start fake-transport runtime only on `127.0.0.1:8782`;
- read back effective systemd hardening including `LimitCORE=0`;
- verify exact DB owner/mode/schema;
- run a synthetic privacy log test and require zero persistent matches for synthetic identity/name/comment markers;
- reject unexpected proxy or retry/dead-letter body persistence evidence;
- execute the exact cleanup contract after evidence collection;
- stop/disable the sandbox unit and restore Apport.

## One exact human action required

On `ruvds-xnqc6`, execute exactly:

`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

This is the only requested human action. The script may ask for the existing sudo password in the operator terminal. Do not paste that password into chat or GitHub.

After completion SIS must read back `/home/pev5691/sis-phase1b-tooling/host-gate-evidence.txt` and then return either `PASS_TOOLING_PATH_AND_NONPRODUCTION_HOST_GATE` or an exact remaining blocker.

## Boundary

No live Telegram API call, production VPN/server change, public webhook, real bot/webhook credential, MAZHOR action, persistent root credential or permanent sudo policy change has been performed.

## Experience

Идея → заменить постоянное расширение root-доступа одноразовым оператор-assisted privileged проходом; проба → fresh host/package preflight и подготовка auditable one-shot script; результат → технический путь готов, но единственная root-мутация требует запуска ОПЕРАТОРОМ; итог → waiting exact human action; фиксация → для bounded root provisioning безопаснее одноразовый проверяемый root script без persistent sudoers/key expansion.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: превратить разрешение ОПЕРАТОРА в минимальный безопасный tooling path и одно точное действие
СТАТУС: waiting_operator_exact_human_action
