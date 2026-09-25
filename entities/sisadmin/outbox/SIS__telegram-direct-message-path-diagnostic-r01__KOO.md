# SIS → KOO: Telegram direct-message path bounded diagnostic r0.1

terminal: BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS
scope: BOUNDED_READ_ONLY_DIAGNOSTIC
project_time: omitted

bot: @WBNP_Media_Bot
bot_id: 8866633840
channel: wbnp_pev5691_15042026
channel_id: -1003606547591

## Человеческий смысл

Ограниченная read-only диагностика установила текущее состояние Phase 1B host/service boundary, но не смогла безопасно выполнить разрешённые Bot API read-only вызовы.

Причина не в отсутствии токена как такового. Unit показывает sensitive credential configuration, а исторический one-send доказывает, что защищённый Bot API access ранее существовал. Но в текущем проверенном access contour нет разрешённого read-only helper/subcommand для getWebhookInfo или getChatMember.

Доступный пользователь имеет NOPASSWD только к фиксированным subcommands существующего helper-а wbn-phase1b-r01:
install-runtime, install-config, prepare-boundary, seed-test, verify-test, verify-logs, start, stop, disable, state, cleanup-db.

Ни один из них не предоставляет bounded Bot API read-only operation. Создавать новый helper, читать credential value, запускать service ради извлечения credentials или менять unit этой задачей запрещено.

Поэтому:
- getWebhookInfo: NOT_EXECUTED;
- getChatMember: NOT_EXECUTED;
- webhook state: UNKNOWN;
- allowed_updates: UNKNOWN;
- can_manage_direct_messages: UNKNOWN.

## Resume-First / authority

Direct OPERATOR authority:
one bounded read-only diagnostic for @WBNP_Media_Bot;
no replies, no getUpdates, no webhook/rights/service/file mutation.

Fresh HQ HEAD before diagnostic:
e2f6d0ca15be43171d45d01ba74b55ccf87185b1

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Approved Project Sources exact blobs matched:
- core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor v1.2 — df7896d867eeeffff506319538fedad938856686

No competing SIS result for this exact bounded diagnostic was found at prewrite reconciliation.

Historical PROMPT replay: 0.

## Exact KOD input

puev5691/wellbeing-hq@0ece5979ab5e0fbab485eb1491a4f51ce5bee105:
entities/koder/outbox/KOD__telegram-channel-direct-message-fitgap-r01__KOO.md
blob:
cb6a41bb1cc577835e6ca036d264a287afa6b353

KOD terminal:
PASS_KOD_TELEGRAM_CHANNEL_DIRECT_MESSAGE_FITGAP_R01_READ_ONLY

KOD conclusion preserved:
repository/code evidence does not prove that the exact bot receives channel direct-message updates; nearest diagnostic uncertainty is effective bot direct-message right plus functioning update delivery path.

## Verified host identity

Target host:
ruvds-xnqc6

Authorized Remote Desktop device:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

Current status:
online

Device name:
ruvds-xnqc6

Identity:
PASS_VERIFIED_TARGET

No other host was accessed.

## Service status

Unit:
wellbeing-telegram-phase1b-sandbox.service

Current unit state:
- UnitFileState=disabled
- ActiveState=inactive
- SubState=dead
- Type=simple

Service principal:
- User=wellbeing-tg-p1b
- Group=wellbeing-tg-p1b

Current ExecStart contract:
python runtime_app.py
--config /etc/wellbeing/telegram-phase1b/runtime.json
--listen-host 127.0.0.1
--listen-port 8782
--transport fake

Interpretation:
the currently configured service does NOT use real Telegram transport.

Service was not started, stopped, enabled, disabled or reloaded in this diagnostic.

## Listener status

Contract listener:
127.0.0.1:8782

Current observation:
no matching listening socket.

Interpretation:
no active Phase 1B local webhook listener was observed.

No network probe was performed.

## Runtime config status

Current shell could not read:
/etc/wellbeing/telegram-phase1b/runtime.json

This is consistent with the existing root/service-group protection.

Current config content:
UNKNOWN_FROM_CURRENT_CALLER

Historical independently recorded non-secret config identity remains:
- channel username wbnp_pev5691_15042026
- channel id -1003606547591
- linked discussion id -1002429106148
- bot identity 8866633840 / @WBNP_Media_Bot
- privacy mode aggregate_only
- webhook path /telegram/webhook

That historical record is not silently reclassified as a fresh read of runtime.json.

## Credential/access boundary

systemd unit reports sensitive credential configuration:
LoadCredential / LoadCredentialEncrypted properties are present but hidden as unprintable to current caller.

Merged unit text did not expose credential values.

Existing protected helper:
 /usr/local/sbin/wbn-phase1b-r01

Helper SHA-256 observed:
a0873ef603bb331cb1bbc3d62c4e503daaf9945e92e08e24d5355a502930cbd0

Current caller:
uid 1000 / pev5691

NOPASSWD helper subcommands available:
- install-runtime
- install-config
- prepare-boundary
- seed-test
- verify-test
- verify-logs
- start
- stop
- disable
- state
- cleanup-db

No authorized read-only Bot API subcommand exists for:
- getWebhookInfo
- getChatMember

Therefore no verified protected credential-use path is available for the exact permitted Bot API reads.

## Bot API calls

### getWebhookInfo

Authorized maximum:
1 read-only call.

Executed:
0.

Reason:
no verified permitted protected credential-use path.

Webhook URL/config:
UNKNOWN.

allowed_updates:
UNKNOWN.

pending_update_count / last_error fields:
UNKNOWN.

No claim is made about whether the past visitor message reached the bot.

### getChatMember

Target pair from previously verified evidence:
- channel id -1003606547591
- bot id 8866633840

Authorized maximum:
1 read-only call.

Executed:
0.

Reason:
same credential-access blocker.

Bot membership/current channel admin status:
UNKNOWN_FOR_THIS_CHANNEL_CURRENTLY.

can_manage_direct_messages:
UNKNOWN.

Historical discussion-supergroup admin evidence is not reused as proof of channel direct-message right.

## What is established about update path

Service local receiver path:
NOT_ACTIVE.

Reason:
service inactive and listener absent.

Service real Telegram transport:
NOT_IMPLEMENTED / not configured in current ExecStart.

External Telegram webhook:
UNKNOWN because getWebhookInfo could not be executed.

Bot channel direct-message admin right:
UNKNOWN because getChatMember could not be executed.

Therefore:
ACTING_UPDATE_DELIVERY_PATH = NOT_ESTABLISHED.

This does not prove that no path exists elsewhere; it means this bounded diagnostic could not establish one.

## Privacy / mutation accounting

getUpdates:
0

Visitor messages read:
0

Raw updates read:
0

Messages sent:
0

Webhook changes:
0

Channel-right changes:
0

Service mutations:
0

File mutations:
0

Credential values read/output:
0

Host access:
1 verified host only

Provider calls:
2 permitted Telegram reads were NOT performed because protected access was unavailable.

## Exact blocker

BLOCKER:
NO_VERIFIED_READONLY_BOT_API_CREDENTIAL_BRIDGE_FOR_CURRENT_SIS_ACCESS

Minimum next fact/action required before repeating this diagnostic:
a separately authorized and independently verified read-only helper/bridge that can execute only:
- getWebhookInfo for the exact bot;
- getChatMember for exact channel_id=-1003606547591 and user_id=8866633840;
while consuming the existing protected token internally and never returning/logging the token.

Creating or installing that bridge is NOT authorized by this diagnostic result.

## Terminal

BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
