# Telegram Phase 1B runtime/provisioning contract r01

Status: non-production candidate for SIS provisioning review. KOD did not deploy or mutate any host.

## Exact service identity and paths

- proposed systemd unit: `wellbeing-telegram-phase1b-sandbox.service`;
- proposed service principal: `wellbeing-tg-p1b`;
- proposed group: `wellbeing-tg-p1b`;
- package/working directory: `/opt/wellbeing/telegram-phase1b-runtime-r01`;
- non-secret config: `/etc/wellbeing/telegram-phase1b/runtime.json`;
- exact sandbox DB directory: `/var/lib/wellbeing/telegram-phase1b-sandbox`;
- exact sandbox DB path: `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- loopback listener: `127.0.0.1:8782`;
- webhook path: `/telegram/webhook`.

Candidate ownership/modes for next SIS pass:

- service user/group: system account `wellbeing-tg-p1b:wellbeing-tg-p1b`;
- `/opt/wellbeing/telegram-phase1b-runtime-r01`: `root:wellbeing-tg-p1b`, mode `0750`, package files non-writable by service principal;
- `/etc/wellbeing/telegram-phase1b`: `root:wellbeing-tg-p1b`, mode `0750`;
- `runtime.json`: `root:wellbeing-tg-p1b`, mode `0640`, no secret values;
- `/var/lib/wellbeing/telegram-phase1b-sandbox`: `wellbeing-tg-p1b:wellbeing-tg-p1b`, mode `0750`;
- `gateway.sqlite3`: expected service-created mode no broader than `0600` under `UMask=0077`.

## Non-production network boundary

r01 supports `--transport fake` only. `--transport real` first requires both systemd credential slots and then still fails closed with `real_transport_not_implemented_in_r01`.

The candidate systemd unit additionally uses:

- `IPAddressDeny=any`;
- `IPAddressAllow=localhost`;
- exact loopback bind `127.0.0.1:8782`.

Therefore this r01 candidate cannot call Telegram or expose a public listener. Any future real transport requires a new separately reviewed runtime/network contract.

## Credential slots

No secret value is present in this package.

Future exact slot names:

- `telegram_bot_token`;
- `telegram_webhook_secret`.

Runtime lookup uses systemd-provided `$CREDENTIALS_DIRECTORY/<slot>`, corresponding to paths such as:

`/run/credentials/wellbeing-telegram-phase1b-sandbox.service/telegram_bot_token`

and

`/run/credentials/wellbeing-telegram-phase1b-sandbox.service/telegram_webhook_secret`.

SIS may later choose `LoadCredential=` or `LoadCredentialEncrypted=` with root-controlled persistent sources. The repository must never contain those values. Missing/empty slots fail closed if future real mode is requested.

## No-core / crash boundary

Candidate unit requires:

- `LimitCORE=0`;
- no debug/local-variable dump facility;
- journald output limited by `LOGGING-CONTRACT.md`;
- package path read-only to the service principal;
- writable path limited to the sandbox DB directory;
- `NoNewPrivileges=yes` and listed systemd hardening directives.

SIS must verify effective `LimitCORE=0` and host coredump behavior after authorized installation. If host tooling can still persist process memory despite the unit boundary, readiness remains blocked until SIS adds host-appropriate protection.

## Reverse-proxy contract

No reverse proxy is installed by KOD. If SIS later adds one:

- upstream exactly `http://127.0.0.1:8782`;
- only `POST /telegram/webhook` is required;
- no request-body logging;
- no raw update, headers, query string or webhook secret in access/error/debug logs;
- external TLS/public endpoint remains separately authorized infrastructure scope;
- proxy retries must not persist request bodies to disk/dead-letter storage.

## Exact post-provision SIS verification commands

These commands are requirements for a future separately authorized non-production provisioning pass; KOD did not run them on a host.

1. Identity and permissions:
   `getent passwd wellbeing-tg-p1b && getent group wellbeing-tg-p1b`
   `namei -l /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`
   `stat -c '%U:%G %a %n' /var/lib/wellbeing/telegram-phase1b-sandbox`

2. Unit hardening/readback:
   `systemctl cat wellbeing-telegram-phase1b-sandbox.service`
   `systemctl show wellbeing-telegram-phase1b-sandbox.service -p User -p Group -p LimitCORE -p NoNewPrivileges -p PrivateTmp -p PrivateDevices -p ProtectSystem -p ProtectHome -p ReadWritePaths -p IPAddressDeny -p IPAddressAllow`

3. Listener boundary:
   `ss -ltnp | grep '127.0.0.1:8782'`
   and independently confirm no `0.0.0.0:8782` / public bind.

4. Credential mechanism without values:
   `systemctl show wellbeing-telegram-phase1b-sandbox.service -p LoadCredential -p LoadCredentialEncrypted`
   and verify only the two approved slot names are exposed if a future real-transport unit is separately approved.

5. Logs:
   `journalctl -u wellbeing-telegram-phase1b-sandbox.service --no-pager`
   using only synthetic test payloads, then search for the synthetic identity/comment sent by the approved test fixture and require zero matches.

6. DB writable/readback:
   run the candidate with synthetic/fake transport only, verify exact DB exists at the approved path, owner/group/mode are restrictive, and inspect schema for absence of audience-identity/raw-comment columns.

7. Core boundary:
   `systemctl show wellbeing-telegram-phase1b-sandbox.service -p LimitCORE`
   plus host-specific coredump/apport inspection sufficient to prove the service cannot leave a request-memory core artifact.

## Retention

Accepted Phase 1B cleanup contract remains unchanged: after KOO closes Phase 1B, the live sandbox DB must be deleted within 30 days unless superseded by explicit retention policy.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: дать SIS exact provisioning/runtime contract для следующего bounded non-production pass
СТАТУС: candidate_runtime_contract_for_sis
