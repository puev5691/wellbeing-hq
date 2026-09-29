# KOO -> SIS: Telegram discussion bounded live activation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Authority

OPERATOR bounded live activation decision:
AUTHORIZE_TELEGRAM_SINGLE_ENTITY_PILOT_R01_BOUNDED_LIVE_ACTIVATION = YES

OPERATOR tester confirmation:
TESTER_1_CANDIDATE=777000
IS_INTENDED_FIRST_TESTER=YES

OPERATOR accepted:
- Telegram bot credential provisioning;
- OpenAI credential provisioning;
- count-bounded dialogue transcript for this pilot.

## Exact readiness evidence

Installed discussion package PASS:

puev5691/wellbeing-hq@59455e46db80c490e740ce96fa3834348576506c:
entities/sisadmin/outbox/SIS__telegram-discussion-admission-r02-independent-review-install-verify__KOO.md
blob 3ed6d57f020f526f6c383e62c71498050c48bcd3

terminal:
PASS_SIS_TELEGRAM_DISCUSSION_ADMISSION_R02_READY_FOR_BOUNDED_LIVE_DISCUSSION_PILOT_GATE

Installed package:
/opt/wellbeing/telegram-single-entity-mvp-r02

Verified Telegram bot credential PASS:

puev5691/wellbeing-hq@457a39e62354640f0f8de1b5cd2938de2eeabf93:
entities/sisadmin/outbox/SIS__telegram-bot-credential-replacement-r01__KOO.md

terminal:
PASS_SIS_TELEGRAM_BOT_CREDENTIAL_REPLACED_R01

Tester discovery PASS:

puev5691/wellbeing-hq@fbbcb48ca30488bb8060744194b5d460a8984bf9:
entities/sisadmin/outbox/SIS__telegram-discussion-tester-id-discovery-r02__KOO.md
blob d2136e52a8a167fca7527dedff16e8b3b25cc951

terminal:
PASS_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERED_R02

Evidence:
WEBHOOK_ACTIVE=NO
discussion_chat_id=-1002429106148
tester_id=777000
trigger_class=EXACT_BOT_COMMAND

OpenAI credential/model entitlement PASS:

puev5691/wellbeing-hq@0173534d45132d4b15aa0e4e5c8279b1821fb52f:
entities/sisadmin/outbox/SIS__openai-credential-validation-for-telegram-pilot-r01__KOO.md
blob 9a9c91397f1bd67b95fe5d623997c1cb2aaa2a8e

terminal:
PASS_SIS_OPENAI_CREDENTIAL_VALIDATED_FOR_TELEGRAM_PILOT_R01

validation:
VALID_AUTH_AND_REQUIRED_MODEL_ENTITLEMENT
model:
gpt-5.6-luna
HTTP:
200
billed_generation:
NO

## Exact Telegram binding

bot:
@WBNP_Media_Bot
bot_id:
8866633840

discussion:
chat_id -1002429106148
type supergroup

accepted triggers:
- reply-to-bot;
- exact @WBNP_Media_Bot mention;
- exact /ask;
- exact /ask@WBNP_Media_Bot.

ambient non-addressed group messages:
IGNORE before provider/send.

## Exact runtime

host:
ruvds-xnqc6

service:
wellbeing-telegram-single-entity-pilot.service

service principal:
wellbeing-tg-dialog

code:
/opt/wellbeing/telegram-single-entity-mvp-r02

config:
/etc/wellbeing/telegram-single-entity-pilot/runtime.json

allowlist:
/etc/wellbeing/telegram-single-entity-pilot/testers.allow

Telegram credential:
/etc/wellbeing/telegram-single-entity-pilot/secrets/telegram_bot_token

OpenAI credential:
/etc/wellbeing/telegram-single-entity-pilot/secrets/openai_api_key

state DB:
/var/lib/wellbeing/telegram-single-entity-pilot/dialogue.sqlite3

## Task

Perform one bounded live discussion pilot execution.

### A. Mandatory fresh pre-live gate

Before any service start, fresh-verify all of the following:

1. current SIS writer exact match;
2. this exact task/authority is current and not superseded;
3. exact installed r0.2 package/config/unit identities still match accepted evidence;
4. service prestate:
   - LoadState=loaded;
   - ActiveState=inactive;
   - SubState=dead;
   - UnitFileState=disabled;
   - MainPID=0;
5. no competing dialogue process;
6. tester allowlist contains exactly:
   777000
   and no other ID;
   if not, atomically set it to exactly 777000 with:
   owner root:wellbeing-tg-dialog
   mode 0640;
7. Telegram credential source:
   exists / root:root / 0600 / non-empty;
8. OpenAI credential source:
   exists / root:root / 0600 / non-empty;
9. systemd LoadCredential refs match those exact protected paths;
10. config binds exact discussion chat -1002429106148;
11. model is exact gpt-5.6-luna;
12. transport is Telegram long polling;
13. no public listener;
14. current webhook state is checked read-only immediately before start and remains NO.

If any check fails:
STOP before start and return exact blocker.

If webhook is active:
STOP.
Do not remove webhook under this task.

### B. Live limits

Exact allowed tester IDs:
[777000]

Accepted user turns total max:
50

OpenAI provider calls total max:
50

Live pilot time window:
2 hours from observed successful service start

Nominal cost ceiling:
USD 5

Provider:
OpenAI only

Model:
gpt-5.6-luna

Telegram transport:
long polling

Tools:
none

Project mutation:
none

Fallback provider:
none

Retries:
no blind external-effect retry; preserve package behavior.

Cost rule:
If exact monetary spend cannot be observed live, the hard technical cap is 50 OpenAI calls plus package-configured output-token limit.
Do not invent cost evidence.

### C. Service activation

Only after A PASS:

1. start the exact service;
2. do not broaden enablement/persistence beyond what this bounded pilot requires;
3. record observed successful service start boundary;
4. verify one polling process only;
5. verify no inbound listener.

### D. Live pilot success criteria

PASS requires evidence for:

1. tester 777000 receives at least two consecutive replies in the same discussion thread/topic;
2. multi-turn context is coherent across those two turns;
3. ambient non-addressed group message causes no provider/send effect;
4. an unlisted/foreign user attempt, if safely available during pilot, causes no OpenAI call;
   if no such external attempt occurs, mark this live criterion NOT_OBSERVED and rely only on offline test evidence; do not fabricate;
5. exact replay causes no duplicate provider/send effect if a replay can be safely observed/injected within package-supported bounded method;
   otherwise mark live replay criterion NOT_OBSERVED and retain offline evidence;
6. controlled provider failure/fallback visibility may be tested only if it can be induced without credential/account mutation or unsafe provider manipulation;
   otherwise NOT_OBSERVED, not FAIL;
7. operational logs contain no secret/raw-dialogue leakage under the defined privacy checks;
8. service can be stopped cleanly.

Minimum live acceptance for this first pilot:
- criteria 1, 2, 7, 8 must PASS;
- no hard STOP condition may occur;
- optional live observations 4/5/6 may remain NOT_OBSERVED if unsafe/unavailable, with prior offline PASS preserved separately.

### E. Hard STOP conditions

STOP immediately on:

- secret exposure or suspected secret logging;
- provider effect for unlisted user;
- wrong discussion chat effect;
- cross-chat/thread context contamination;
- replay collision / OUTCOME_UNKNOWN requiring manual reconciliation;
- three consecutive provider/runtime failures;
- 50 provider calls reached;
- 50 accepted user turns reached;
- 2-hour window reached;
- OPERATOR stop instruction;
- unexpected project/Telegram settings mutation;
- unexpected model/provider substitution;
- need to widen scope;
- service identity/package/config mismatch.

Emergency stop:
sudo systemctl disable --now wellbeing-telegram-single-entity-pilot.service

### F. End of pilot

At bounded pilot end or STOP:

1. stop service;
2. verify inactive/dead/MainPID=0;
3. do not destructively delete config/secrets/state;
4. preserve state/evidence for review;
5. report exact call/turn counts actually observed;
6. report live success criteria as PASS / FAIL / NOT_OBSERVED individually;
7. report any OUTCOME_UNKNOWN separately.

Do not:
- mutate Telegram rights/settings;
- use another provider/model;
- add testers;
- expose credentials;
- mutate billing/account;
- publish project content automatically;
- create project authority from dialogue;
- change Sources/canons.

## Expected terminal

PASS_SIS_TELEGRAM_DISCUSSION_PILOT_R01_LIVE_COMPLETE

only if mandatory live acceptance criteria PASS and no hard STOP occurred.

Otherwise exact BLOCKED_/FAIL_ terminal.

Mandatory RETURN KOO:
- service start/stop evidence;
- tester/turn/provider-call counts;
- exact model/provider;
- mandatory success criteria;
- optional NOT_OBSERVED items;
- privacy/log check;
- final service inactive state;
- exact next recommendation.

Then STOP.
