# KOD → KOO: Telegram Phase 1B runtime/privacy remediation r1 result

status: APPLICATION_B2_CANDIDATE_PASS__SIS_HOST_VERIFICATION_PENDING
production: no
live_telegram_send: no
real_credentials: no
host_deployment: no
privacy_mode: aggregate_only
project_time: omitted; trusted project-time source not used

## Результат

Bounded non-production remediation application/runtime стороны SIS blocker B2 выполнена без изменения принятой privacy policy.

Подготовлен executable webhook/application candidate вокруг принятого `Gateway`. Candidate остаётся fake/test-only, не содержит Telegram API transport, не регистрирует webhook, не создаёт public endpoint, не читает реальные credentials и не выполняет host mutation.

Полный pre-live runtime/privacy PASS **не заявляется**: B1 и host-instantiated часть B2 остаются за следующим отдельно разрешённым SIS provisioning/verification pass.

## Exact task / base

Task:
`entities/koordinator/outbox/KOO__telegram-phase1b-runtime-privacy-remediation-r1__KOD.md`
commit `68bcee42b33a1135764eccd7cc46afe58113007f`
blob `f3a7938426a4a4abd41578bba41e22e2f261e7b0`.

Accepted base package:
`entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
commit `cd81bbd98a4be334388f95ea948427d91fa82a05`.

Five inherited base files were preserved byte-identical to the accepted package:
- `gateway.py`;
- `test_gateway.py`;
- `cleanup_sandbox.py`;
- `test_cleanup.py`;
- `runtime-config.schema.json`.

Their accepted SHA-256 values were rechecked locally before candidate finalization: 5/5 PASS.

## Candidate package identity

Path:
`entities/koder/outbox/telegram-media-phase1b-runtime-r01/`

Immutable candidate commit:
`b939a238f757be0bcfaf1bb4164b0362eafc088f`

Package tree:
`23724102ecdc35c42d48eaaeeeae126dff978cb9`

Package contains 14 files. Final `SHA256SUMS.txt` blob:
`53a5a4f10995e7c6edbee44e2b7c194433ababce`.

Local checksum verification of all 13 payload files listed in `SHA256SUMS.txt`: 13/13 PASS.
GitHub immutable tree readback: 14/14 expected files present; inherited accepted files retain their original Git blob identities.

## Application/runtime remediation

### Webhook entrypoint

Added `runtime_app.py`:
- wraps accepted `Gateway`;
- accepts JSON update bodies only in non-production config;
- listener contract is exact loopback `127.0.0.1:8782`;
- webhook path is `/telegram/webhook`;
- raw request bytes and parsed payload remain in memory only for processing and are not persisted by the application;
- response bodies are generic and never echo incoming payload;
- public bind and alternate port fail closed;
- accepted exact sandbox DB path remains:
  `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`.

### Privacy-safe logging contract

`PrivacySafeLogger` accepts a closed field/value vocabulary only:
- bounded `event`;
- bounded `status`;
- bounded generic `error_class`;
- integer `http_status`;
- integer `request_bytes`;
- bounded `transport`.

Application logs cannot accept arbitrary request-derived fields. The application does not log:
- raw update/request body;
- audience user ID;
- username/name;
- raw comment text;
- headers;
- query string;
- peer address;
- credential contents;
- traceback/local-variable dumps.

There is no application retry/dead-letter body store in r01.

Full contract:
`LOGGING-CONTRACT.md` in the candidate package.

### Service/runtime contract for SIS

Proposed exact service unit:
`wellbeing-telegram-phase1b-sandbox.service`

Proposed exact principal/group:
`wellbeing-tg-p1b:wellbeing-tg-p1b`

Working directory:
`/opt/wellbeing/telegram-phase1b-runtime-r01`

Non-secret config:
`/etc/wellbeing/telegram-phase1b/runtime.json`

DB directory:
`/var/lib/wellbeing/telegram-phase1b-sandbox`

Candidate ownership/mode:
- package directory: `root:wellbeing-tg-p1b 0750`, not writable by service principal;
- config directory: `root:wellbeing-tg-p1b 0750`;
- non-secret config: `root:wellbeing-tg-p1b 0640`;
- DB directory: `wellbeing-tg-p1b:wellbeing-tg-p1b 0750`;
- service-created DB expected no broader than `0600` under `UMask=0077`.

Candidate unit includes:
- `LimitCORE=0`;
- `NoNewPrivileges=yes`;
- `PrivateTmp=yes`;
- `PrivateDevices=yes`;
- `ProtectSystem=strict`;
- `ProtectHome=yes`;
- kernel/control-group hardening;
- writable path limited to sandbox DB directory;
- `IPAddressDeny=any`;
- `IPAddressAllow=localhost`;
- exact fake-only ExecStart on `127.0.0.1:8782`.

`systemd-analyze verify` on the candidate unit: PASS / exit 0 / no diagnostics.

Host coredump/Apport behavior still requires SIS readback after authorized installation; code-level unit definition cannot prove host enforcement by itself.

### Credential boundary

No secret values are present.

Reserved future systemd credential slots:
- `telegram_bot_token`;
- `telegram_webhook_secret`.

Runtime consumes them only through systemd `$CREDENTIALS_DIRECTORY/<slot>`.

In r01:
- fake mode requires no credentials;
- real mode fails closed when credential files are absent;
- even with synthetic credential files, real transport fails closed with `real_transport_not_implemented_in_r01`.

Therefore r01 cannot make a live Telegram call.

### Reverse-proxy boundary

No proxy was deployed.

Future SIS contract:
- upstream exactly `http://127.0.0.1:8782`;
- only `POST /telegram/webhook`;
- no request-body/header/query-string/credential logging;
- no disk-backed proxy retry/dead-letter body persistence;
- public TLS/endpoint remains separately authorized infrastructure scope.

Full provisioning and verification commands are in:
`RUNTIME-CONTRACT.md`.

## Verification

Commands:
- `python3 -m py_compile gateway.py test_gateway.py cleanup_sandbox.py test_cleanup.py runtime_app.py test_runtime_app.py`;
- `python3 -m unittest -v`;
- `systemd-analyze verify systemd/wellbeing-telegram-phase1b-sandbox.service`;
- exact base SHA-256 validation;
- final package `sha256sum -c SHA256SUMS.txt`;
- explicit captured-test-output search for synthetic privacy markers.

Results:
- compile: PASS;
- full unit suite: **36/36 PASS**;
- accepted base suite: **23/23 PASS**;
- new runtime/privacy suite: **13/13 PASS**;
- systemd unit syntax/verification: PASS;
- final checksum payloads: **13/13 PASS**;
- GitHub tree readback: **14/14 expected files present**.

Synthetic privacy values tested:
- audience ID `9876543210123`;
- username `synthetic_private_user_71f2`;
- name `Synthetic Private Person 71f2`;
- comment `SYNTHETIC_RAW_COMMENT_71f2_DO_NOT_LOG`.

They are absent from captured application test logs and generic error responses. The runtime test also verifies these values are absent from the SQLite file after aggregate comment processing.

The unchanged accepted base tests emit Python `ResourceWarning` for some test-created SQLite connections; they remain warnings, not failures. Accepted base bytes were deliberately not edited to silence them.

## Remaining ownership / blockers

No stop condition from the KOO task was triggered.

KOD application-side remediation candidate is ready for review.

Still pending outside KOD:
1. SIS privileged provisioning of exact DB directory/service principal and writable-path proof (B1).
2. SIS installation/readback of the candidate unit on an authorized non-production host.
3. SIS proof of effective no-core/coredump boundary on that host.
4. SIS end-to-end proxy/application log readback using synthetic payloads.
5. Any future live transport/webhook/public endpoint/real credentials require separate authorization and a later contract; r01 intentionally cannot perform them.

## Experience

Идея → закрыть B2 не описанием намерений, а executable runtime + закрытым logging vocabulary + проверяемым service contract.

Проба → принятому Gateway добавлен loopback-only webhook runtime, synthetic privacy tests, candidate systemd unit и exact SIS provisioning contract.

Результат → 36/36 tests PASS; raw synthetic identity/comment не попали в application logs/error responses/SQLite; real transport и public bind fail-closed.

Промежуточная неудача → первый static network-import test искал слово `requests` текстовым поиском и поймал его в комментарии, а не импорт. Тест заменён на AST-проверку реальных imports; runtime code менять не потребовалось.

Упаковочная неудача → первый checksum pass случайно включил локальный `__pycache__`; pyc удалены до публикации, checksum set пересобран строго по manifest, после чего 13/13 PASS.

Фиксация → privacy runtime проверяется на трёх разных границах: application log vocabulary, process/crash service boundary и host/proxy readback. Ни одна из них не заменяет остальные.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть application/code сторону SIS blocker B2 и вернуть KOO проверяемый non-production candidate для следующего SIS pass
СТАТУС: application_b2_candidate_pass__sis_host_verification_pending
