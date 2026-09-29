# SIS -> KOO: Telegram discussion bounded live activation r0.1 result

status: FAIL
terminal: FAIL_SIS_TELEGRAM_DISCUSSION_PILOT_R01_TESTER_IDENTITY_MISCLASSIFIED
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Human result

The bounded live pilot was started only after the exact pre-live gate passed.

The service entered active/running state and one live OpenAI-backed Telegram reply was observed.

However, the tester identity used by the live gate was wrong.

The discovered value 777000 is not proven to be the intended human tester. Telegram Bot API documents that messages sent on behalf of a chat use sender_chat and, for backward compatibility, may expose a fake sender user in from. Telegram's Bot API changelog specifically documents user 777000 for messages automatically forwarded to a discussion group.

The discovery r0.2 accepted that fake from.id as TESTER_1_CANDIDATE because it did not exclude sender_chat / automatic-forward messages.

As a result:
- the allowlist admitted 777000;
- one automatically forwarded channel message was admitted and produced one committed dialogue/provider/send effect;
- the intended human tester's later message was not admitted because its real from.id is different from 777000;
- the required second same-thread human turn never entered the ledger.

This invalidates the live acceptance attempt.

OPERATOR stopped the service after the root cause was identified.

## Exact task

puev5691/wellbeing-hq@3b602ff34a30fc4ba2667fabec5b225a41066eb8:
entities/koordinator/outbox/KOO__telegram-discussion-bounded-live-activation-r01__SIS.md

blob:
a096e398ff25fea68fd512c3ce564c1bdaf431cb

## Pre-live gate evidence

PRELIVE_GATE=PASS
WEBHOOK_ACTIVE=NO
ALLOWLIST_EXACT=777000
PROVIDER=OpenAI
MODEL=gpt-5.6-luna
TRANSPORT=Telegram_long_polling
LIVE_STARTED=YES
SERVICE_ENABLED=NO

## Live evidence before stop

Observed database state during diagnosis:

UPDATES_TOTAL=1
COMMITTED=1
FALLBACK_COMMITTED=0
OUTCOME_UNKNOWN=0
CLAIMED=0
SENDING=0
SENDING_FALLBACK=0
MESSAGES_TOTAL=2

Committed update:
560511119

One conversation key existed with exactly two stored messages, corresponding to one user/assistant turn.

This proves one admitted live turn, not the required two-turn intended-human dialogue.

Observed intended-human second message:
not represented as a second ledger update.

## External protocol evidence

Telegram Bot API Message semantics:
- sender_chat identifies a chat/channel sending on behalf of a chat;
- automatically forwarded linked-channel messages in a discussion group use sender_chat;
- backward-compatible from may contain a fake sender user.

Telegram Bot API changelog further documents:
- fake user 777000 for messages automatically forwarded to a discussion group.

Official sources:
https://core.telegram.org/bots/api
https://core.telegram.org/bots/api-changelog

## Root cause

Discovery r0.2 candidate acceptance logic was insufficient.

It required:
- exact discussion chat;
- exact command;
- integer from.id;
- sender != bot.

It did NOT require:
- sender_chat absent;
- is_automatic_forward != true;
- human-user provenance.

Therefore TESTER_1_CANDIDATE=777000 was a false human identity classification.

## Hard-stop / failure classification

The live pilot cannot claim tester acceptance or multi-turn success because the configured tester identity does not represent the intended human.

Mandatory criteria:
1. intended tester receives two consecutive same-thread replies = FAIL / identity invalid
2. coherent intended-human multi-turn context = FAIL / second human turn not admitted
7. privacy/log check = NOT COMPLETED AS FINAL PASS
8. clean stop = PASS

Optional:
foreign user = NOT_OBSERVED
live replay = NOT_OBSERVED
controlled failure = NOT_OBSERVED

OUTCOME_UNKNOWN:
0 observed

Provider/model:
OpenAI / gpt-5.6-luna

Observed committed provider-backed turns:
1

Exact billed cost:
NOT OBSERVED

## Final stop evidence

After OPERATOR stop:

MainPID=0
ActiveState=inactive
SubState=dead
UnitFileState=disabled
NRestarts=0

Detached live helper also exited after observing service stop.

Final helper terminal:
FAIL_SERVICE_DIED

This helper terminal is a consequence of the deliberate OPERATOR stop after the identity defect was found; it is not the root cause.

## Preserved state

Config:
PRESERVED

Secrets:
PRESERVED

SQLite state:
PRESERVED

Installed r0.2 package:
PRESERVED

Allowlist:
still contains 777000 and MUST NOT be treated as valid human tester admission for a future live task.

## Required correction

Before another live attempt:

1. issue a NEW exact tester-ID discovery/correction task;
2. discovery must reject any candidate when:
   - sender_chat is present; or
   - is_automatic_forward is true; or
   - from.id is Telegram's backward-compatible fake sender;
3. discover the intended human from.id from a fresh direct human message in the exact discussion;
4. require OPERATOR confirmation of the new human candidate;
5. atomically replace allowlist with only that confirmed human ID;
6. rerun final live-gate prep;
7. only then issue a NEW bounded live task.

Do not replay the consumed r0.1 live task.

## Lifecycle

live execution:
FAILED / CONSUMED / NON_REPLAYABLE

service:
inactive / dead / disabled

## RETURN KOO

This file is the mandatory SIS return to KOO.

## Terminal

FAIL_SIS_TELEGRAM_DISCUSSION_PILOT_R01_TESTER_IDENTITY_MISCLASSIFIED
