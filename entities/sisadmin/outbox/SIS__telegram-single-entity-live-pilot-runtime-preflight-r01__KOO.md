# SIS -> KOO: Telegram single-entity live-pilot runtime preflight r0.1

status: PASS
terminal: READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР
scope: READ_ONLY_RUNTIME_PREFLIGHT_ONLY

## Human result

Fresh runtime/deployment preflight was completed for the closed single-Entity Telegram live pilot.

The current host is capable of supporting a bounded pilot, but the old Phase1B runtime must not be reused as the live dialogue runtime:

- its accepted privacy mode is aggregate_only;
- its unit runs fake transport only;
- its unit denies all non-loopback IP traffic;
- its state contract forbids audience identity, raw message text and per-user history;
- the new dialogue MVP requires bounded chat/thread identity and multi-turn dialogue state.

Therefore a separate bounded live-pilot contour is required.

For the shortest pilot path, SIS recommends Telegram long polling, not webhook.

Reason:
polling requires outbound HTTPS only and avoids public listener, TLS certificate, DNS/reverse-proxy and inbound webhook logging boundaries.

Webhook remains technically possible as a later separately provisioned route, but is not required for the first closed pilot.

No deployment, live Telegram action, provider call, secret read, billing/account action or production mutation was performed.

## Exact task

puev5691/wellbeing-hq@16894f8cd86ca0a6c2b4eb9f499f9badf00e9e9e:
entities/koordinator/outbox/KOO__telegram-single-entity-live-pilot-runtime-preflight-r01__SIS.md

blob:
f932d1a98bfcab14d79fd9650fdb75432ae64620

## Priority direction

puev5691/wellbeing-hq@e360ce75dfc8c803a54f69a3aae4188659bf6938:
entities/koordinator/outbox/KOO__telegram-single-entity-mvp-priority__OPERATOR.md

Priority target:
one closed Telegram dialogue path using OpenAI first.

## Current intended KOD MVP task

puev5691/wellbeing-hq@a856fda15bd69b2aa64faf4a2b2baeff984608f2:
entities/koordinator/outbox/KOO__telegram-single-provider-entity-dialogue-mvp-r01__KOD.md

blob:
3d14c75115f0b642b24168064465d9a9e7820717

The KOD task requires:
- real text ingress;
- per-chat/thread dialogue state;
- bounded Entity bootstrap;
- one OpenAI adapter path;
- Telegram reply;
- replay protection;
- privacy/logging;
- closed tester allowlist;
- error fallback;
- deploy/run/stop/rollback instructions;
- multi-turn tests.

No immutable terminal KOD MVP result/package was present in current HQ during this preflight.

Therefore package-specific command line/options remain a future exact dependency and are not invented here.

# 1. Fresh host state

Selected host:
ruvds-xnqc6

OS:
Ubuntu 24.04.4 LTS

Python:
3.12.3

systemd:
255

filesystem capacity:
approximately 24 GiB free on root filesystem at readback.

DNS resolution:
- api.telegram.org -> IPv4 resolution PASS
- api.openai.com -> IPv4 resolution PASS

This proves local resolver feasibility only.
No external HTTPS/API request was made.

## Existing historical Phase1B state

service account:
wellbeing-tg-p1b uid 996
group:
wellbeing-tg-p1b gid 989

unit:
wellbeing-telegram-phase1b-sandbox.service

current state:
- LoadState=loaded
- ActiveState=inactive
- SubState=dead
- UnitFileState=disabled

existing paths:
- /opt/wellbeing/telegram-phase1b-runtime-r01
  root:wellbeing-tg-p1b 0750
- /etc/wellbeing/telegram-phase1b
  root:wellbeing-tg-p1b 0750
- /var/lib/wellbeing/telegram-phase1b-sandbox
  wellbeing-tg-p1b:wellbeing-tg-p1b 0750

no listener on 8782 observed.
no Phase1B process observed.

The exact runtime.json / DB state could not be read as unprivileged pev5691 because the accepted directories are intentionally closed to that principal.

Historical result a49040d2e9b4ecceeb4827d9e224e0a5e1eee952 remains historical only and was not replayed.

# 2. Privilege boundary

Current principal:
pev5691

groups:
pev5691, sudo, users

The current read-only tool principal cannot write:
- /opt/wellbeing
- /etc/wellbeing
- /var/lib/wellbeing
- /etc/systemd/system

Root/sudo is therefore required for provisioning.

This is not an unresolved architectural blocker because OPERATOR-assisted sudo is available as an explicit provisioning mechanism.

DC/non-root tooling should prepare immutable files and verify user-readable evidence where possible.
OPERATOR should execute one reviewed root provisioning script after a separate provisioning task authorizes mutation.

# 3. New bounded live-pilot contour

A separate contour is required because the old aggregate-only Phase1B state contract is incompatible with bounded multi-turn dialogue state.

Proposed exact runtime identity:

service:
wellbeing-telegram-single-entity-pilot.service

service principal:
wellbeing-tg-dialog

group:
wellbeing-tg-dialog

package path:
/opt/wellbeing/telegram-single-entity-mvp-r01

config directory:
/etc/wellbeing/telegram-single-entity-pilot

non-secret config:
/etc/wellbeing/telegram-single-entity-pilot/runtime.json

closed tester allowlist:
/etc/wellbeing/telegram-single-entity-pilot/testers.allow

secret source directory:
/etc/wellbeing/telegram-single-entity-pilot/secrets

Telegram token source:
/etc/wellbeing/telegram-single-entity-pilot/secrets/telegram_bot_token

OpenAI key source:
/etc/wellbeing/telegram-single-entity-pilot/secrets/openai_api_key

state directory:
/var/lib/wellbeing/telegram-single-entity-pilot

dialogue/replay state:
/var/lib/wellbeing/telegram-single-entity-pilot/dialogue.sqlite3

No public listener is required for the recommended polling route.

The final package contents/launcher CLI must be taken from the immutable KOD MVP result once published. SIS does not invent a launcher interface before that result exists.

# 4. Polling vs webhook

## Recommended first route: polling

Provisioning model:
Telegram Bot API long polling over outbound HTTPS.

Advantages for this exact pilot:
- no public inbound port;
- no TLS certificate;
- no reverse proxy;
- no DNS endpoint required;
- no webhook request-body logging risk;
- simpler stop/rollback;
- easiest closed tester gate.

Host DNS resolution for Telegram and OpenAI passed.

Actual outbound HTTPS and Telegram polling must be proven only in the later separately authorized live gate.
No API connection was made in this preflight.

Important future live gate:
if the bot currently has a Telegram webhook configured, the live polling activation must reconcile/remove that webhook through a separately authorized Telegram API action before relying on getUpdates.
Current webhook state is UNKNOWN because querying Telegram would be an external service action.

## Alternative: webhook

Feasible only with additional infrastructure:
- public HTTPS endpoint;
- TLS certificate;
- reverse proxy;
- webhook secret;
- ingress firewall;
- request-body-safe proxy logging;
- exact webhook registration action.

Those are unnecessary for the shortest first pilot and remain outside this preflight.

# 5. Secret-reference mechanism

Secrets must not appear in:
- GitHub;
- runtime.json;
- testers.allow;
- command-line arguments;
- journald;
- traceback/error artifacts.

Preferred mechanism:
systemd credentials.

Persistent root-only source files:
- telegram_bot_token
- openai_api_key

required modes:
root:root 0600

systemd unit should use:

LoadCredential=telegram_bot_token:/etc/wellbeing/telegram-single-entity-pilot/secrets/telegram_bot_token
LoadCredential=openai_api_key:/etc/wellbeing/telegram-single-entity-pilot/secrets/openai_api_key

Runtime obtains only credential file references from:
$CREDENTIALS_DIRECTORY

The KOD MVP package must support either:
1. direct credential-file inputs; or
2. a bounded launcher that resolves these files into process memory without logging/serialization.

Exact credential values are never read by SIS preflight.

If KOD publishes a package that only accepts raw secret command-line values or repository configuration:
NO-GO until corrected.

# 6. Closed tester allowlist

Required file:
/etc/wellbeing/telegram-single-entity-pilot/testers.allow

Ownership/mode:
root:wellbeing-tg-dialog 0640

Contents:
only explicitly invited Telegram numeric tester identifiers required by the KOD gate.

No names/usernames/display names are required.

Application behavior:
- reject non-allowlisted sender/chat before provider invocation;
- rejected content must not be sent to OpenAI;
- rejected raw text must not be logged/persisted;
- allowlist changes require root-controlled config update and service restart/reload according to the final KOD runtime contract.

Exact identifier semantics (user_id vs chat_id vs both) must match the final immutable KOD MVP package.
SIS will not guess this before package publication.

# 7. Dialogue state / privacy / retention

Old aggregate-only Phase1B DB must not be silently repurposed.

New state may contain only what is required for:
- bounded per-chat/thread multi-turn context;
- replay/duplicate protection;
- minimal operational state.

Forbidden persistent material unless the final exact KOD package explicitly requires and bounds it:
- raw Telegram Update JSON;
- usernames/display names;
- bot token/API key;
- request headers;
- unrestricted full-history transcripts;
- provider raw error bodies;
- debug locals/traceback payload dumps.

Logging must exclude:
- message/prompt text;
- tester IDs/chat IDs;
- provider response text;
- credentials;
- raw Telegram updates.

Permitted logs should be bounded operational metadata only:
event class, generic status/error class, retry count, bounded latency/status counters where actually observed.

Unit hardening requirement:
- UMask=0077
- LimitCORE=0
- NoNewPrivileges=yes
- PrivateTmp=yes
- PrivateDevices=yes
- ProtectSystem=strict
- ProtectHome=yes
- ReadWritePaths=/var/lib/wellbeing/telegram-single-entity-pilot
- StandardOutput=journal
- StandardError=journal

Unlike the old fake/webhook unit, the polling service must NOT use IPAddressDeny=any because it needs outbound Telegram and OpenAI HTTPS.

No inbound listener should be configured in polling mode.

Retention/cleanup behavior for conversation text/state must be supplied and tested by the final KOD package before GO-LIVE.
No retention interval is invented by this SIS task.

# 8. Exact privileged provisioning actions

A future separately authorized provisioning task should have OPERATOR execute one reviewed root script performing only:

1. create system principal/group wellbeing-tg-dialog if absent;
2. create:
   - /opt/wellbeing/telegram-single-entity-mvp-r01
   - /etc/wellbeing/telegram-single-entity-pilot
   - /etc/wellbeing/telegram-single-entity-pilot/secrets
   - /var/lib/wellbeing/telegram-single-entity-pilot
3. install exact immutable KOD package bytes into /opt;
4. package files root:wellbeing-tg-dialog and non-writable by service principal;
5. install runtime.json without secrets;
6. install testers.allow;
7. install the two secret source files by OPERATOR-only input, without echo/log/readback of values;
8. set secret source mode root:root 0600;
9. install exact reviewed systemd unit;
10. systemctl daemon-reload;
11. enable service only if the separate provisioning task explicitly permits enablement;
12. do NOT start live service until the later live activation gate.

DC should not be relied upon for interactive sudo.

# 9. Startup / stop / rollback

These are the intended operator controls after exact unit publication.

Start after separate live authorization:
sudo systemctl start wellbeing-telegram-single-entity-pilot.service

Status:
sudo systemctl status wellbeing-telegram-single-entity-pilot.service --no-pager

Stop:
sudo systemctl stop wellbeing-telegram-single-entity-pilot.service

Emergency stop:
sudo systemctl disable --now wellbeing-telegram-single-entity-pilot.service

Initial rollback boundary:
- stop/disable service;
- preserve installed package/config/state in place for inspection;
- do not automatically delete dialogue DB or secret source files;
- any destructive cleanup requires its own bounded cleanup action.

This makes rollback reversible and preserves failure evidence.

# 10. Provisioning go/no-go checklist

## GO for provisioning only when all are PASS

- current KOD MVP result/package exists immutably;
- package checksum/readback PASS;
- launcher/runtime interface is known exactly;
- package supports polling;
- package supports systemd credential references without secret logging;
- closed tester gate semantics are exact;
- bounded multi-turn state schema/retention/cleanup are documented;
- no raw update/unbounded transcript logging;
- OpenAI route uses already accepted bounded provider path where compatible;
- exact systemd unit reviewed;
- OPERATOR root provisioning script reviewed;
- old Phase1B service remains inactive;
- new state path is separate from old aggregate-only DB.

## GO for live activation only when all are additionally PASS

- Telegram bot token provisioned by reference only;
- OpenAI credential provisioned by reference only;
- tester allowlist exact and non-empty;
- outbound HTTPS to Telegram/OpenAI proven;
- Telegram webhook state reconciled for polling;
- unit hardening readback PASS;
- no public listener;
- no secret/raw-message material in journal;
- state DB ownership/mode PASS;
- replay protection/multi-turn/error-fallback tests PASS;
- explicit live-pilot authority exists.

## NO-GO

Any missing package identity, secret leakage, unrestricted tester access, public listener in polling mode, unknown state retention, raw update logging, current-writer/task mismatch, or requirement to weaken the accepted provider/security boundary.

# 11. Current exact readiness

Host/runtime infrastructure:
READY

Privilege path:
READY_WITH_OPERATOR_ASSISTED_SUDO

Polling route:
FEASIBLE / RECOMMENDED

Webhook route:
FEASIBLE_IN_PRINCIPLE / NOT REQUIRED / PUBLIC_INFRA_NOT_PREFLIGHTED

Secret mechanism:
READY_AS_SYSTEMD_CREDENTIAL_DESIGN

Closed tester mechanism:
READY_AS_ROOT_CONTROLLED_ALLOWLIST_DESIGN

Final deploy package:
WAITING_CURRENT_KOD_MVP_IMMUTABLE_RESULT

Live Telegram/provider activation:
NOT AUTHORIZED

Production:
NOT AUTHORIZED

## Terminal

READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING

Meaning:
there is no host/infrastructure blocker preventing a bounded provisioning task once KOD publishes the exact immutable MVP package.

This is not GO-LIVE and grants no deployment/live-send/provider-call authority.

## Recommended next causal step

KOO should wait for/reconcile the parallel KOD Telegram single-provider MVP terminal result.

If KOD returns an immutable package compatible with:
- polling;
- systemd credential files;
- explicit tester allowlist;
- bounded dialogue state/privacy;

then KOO should issue one NEW exact SIS provisioning task binding:
- exact KOD package commit/tree/blob identities;
- ruvds-xnqc6;
- the exact paths in this preflight;
- one OPERATOR-assisted root provisioning script;
- install/verify only, no live start/send/provider call.

If the KOD package conflicts with these boundaries, return a targeted compatibility blocker instead of improvising runtime semantics.

## Experience

Идея -> shortest live pilot should minimize public infrastructure, not reuse a privacy contract built for aggregate comments.

Проба -> fresh host inspection plus reconciliation of old Phase1B runtime and new KOD dialogue requirements.

Результат -> polling on ruvds-xnqc6 removes the need for public webhook infrastructure, while a separate state contour avoids violating aggregate-only privacy assumptions.

Успех -> runtime provisioning is causally ready once the exact KOD MVP package exists.

Урок -> reusing an old service account/path is not automatically simpler when the new workload has a different data model; separation can reduce both privacy ambiguity and rollback risk.

## RETURN KOO

This file is the mandatory immutable SIS return to KOO.

