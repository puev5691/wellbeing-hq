# KOO -> SIS: Telegram single-Entity bounded live pilot r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact final live-gate PASS

puev5691/wellbeing-hq@a8a9aa8f7233c98bdf2d0b82b28726667dcd2042:
entities/sisadmin/outbox/SIS__telegram-confirmed-tester-allowlist-final-live-gate-r01-result__KOO.md

blob:
340be457b6dd5a681e0254f0816dde5f6bcb1495

terminal:
PASS_SIS_TELEGRAM_CONFIRMED_TESTER_ALLOWLIST_FINAL_LIVE_GATE_R01

final readiness:
READY_FOR_SEPARATE_NEW_BOUNDED_LIVE_TASK

Verified final allowlist:
ALLOWLIST_COUNT=1
ALLOWLIST_TESTER_ID=6384602715
ALLOWLIST_HAS_777000=NO

Verified pre-live service state:
loaded / inactive / dead / disabled / MainPID=0

Dialogue process:
ABSENT

Webhook:
ABSENT

OpenAI call in gate:
NONE

Telegram sendMessage in gate:
NONE

Dialogue DB content mutation in gate:
NONE

## Human provenance / identity basis

Protocol provenance:

puev5691/wellbeing-hq@8f137e7031b5c4f9e498a3c87996124b49b1320b:
entities/sisadmin/outbox/SIS__telegram-single-instance-human-provenance-verification-r06-result__KOO.md

blob:
6589435077b5351453fef493c5c1080f30371630

terminal:
PASS_SIS_TELEGRAM_SINGLE_INSTANCE_HUMAN_PROVENANCE_R06

OPERATOR confirmation:

puev5691/wellbeing-hq@aba0ba4bbbda5420233409289e0ae26c040513c3:
entities/koordinator/inbox/SIS__telegram-human-tester-id-operator-confirmation-r01__KOO.md

blob:
478c5d0606ce2cc2a9b483f05524897924a463c5

Confirmed intended tester:
6384602715

## Exact live bindings

Bot:
@WBNP_Media_Bot
bot_id:
8866633840

Discussion:
chat_id:
-1002429106148
type:
supergroup

Model:
gpt-5.6-luna

Provider:
OpenAI only

Transport:
Telegram long polling

Accepted addressed trigger classes remain only those already implemented/accepted in runtime:
- reply-to-bot;
- exact mention @WBNP_Media_Bot;
- exact /ask;
- exact /ask@WBNP_Media_Bot.

Ambient group text remains ignored.

## Authority

This task is the separate NEW live authority.

It authorizes SIS to:
- perform fresh live preflight;
- start the existing accepted dialogue service for this bounded pilot;
- allow provider-backed replies only for confirmed tester 6384602715 in exact discussion;
- observe and verify the bounded live behavior;
- stop the service at task completion or any stop condition;
- return immutable result to KOO.

It does NOT authorize:
- adding testers;
- widening chats;
- changing bot/admin rights;
- changing Telegram settings;
- changing credentials;
- changing provider/model;
- production deployment;
- persistent enablement/autostart;
- publication;
- Project Source mutation;
- unrelated service/host mutation.

## Pilot limits

Hard maximum:
- accepted user turns: 50;
- OpenAI provider calls: 50;
- duration: 2 hours from successful service start;
- nominal provider spend ceiling: USD 5 equivalent.

If any limit would be exceeded:
STOP.

Only one confirmed tester:
6384602715

Only one exact discussion:
-1002429106148

Only OpenAI model:
gpt-5.6-luna

No fallback provider/model.

## Pre-live gates

Before service start verify fresh:

1. current SIS writer unchanged;
2. no superseding Telegram live task/result;
3. exact final-gate result identity;
4. allowlist exactly one ID:
   6384602715
5. 777000 absent;
6. webhook absent;
7. service inactive/dead/disabled/MainPID=0;
8. no competing dialogue process;
9. runtime package/config exact bindings unchanged:
   - discussion -1002429106148
   - bot 8866633840
   - model gpt-5.6-luna
10. Telegram/OpenAI credential files present/nonempty with safe metadata; do not expose secret values;
11. no persisted blocking OUTCOME_UNKNOWN evidence;
12. dialogue DB/runtime state readable and suitable for bounded start.

If any pre-live gate fails:
STOP before service start with exact blocker.

## Start boundary

Start the existing service for the bounded pilot.

Do NOT enable it persistently.

After service is confirmed active and live admission is ready, emit to OPERATOR:

LIVE_READY=YES
TESTER_ID=6384602715
CHAT_ID=-1002429106148
SEND_TEST_NOW=YES

Then keep the live service active within the bounded pilot window.

## Required human test

After LIVE_READY=YES, OPERATOR sends at least two consecutive tester turns in the SAME Telegram discussion thread.

Minimum recommended interaction:

Turn 1:
address bot with exact /ask@WBNP_Media_Bot plus a simple Russian question/message.

Turn 2:
reply in the same thread to continue the same dialogue context.

The exact user text is not prescribed by this task beyond being safe, ordinary dialogue suitable for validating continuity.

## Mandatory PASS evidence

For PASS, establish at minimum:

1. tester provenance:
   accepted user id = 6384602715 only.

2. exact routing:
   effects only in chat -1002429106148.

3. first live provider-backed turn:
   - accepted;
   - OpenAI called with gpt-5.6-luna;
   - bot reply delivered to Telegram;
   - no OUTCOME_UNKNOWN.

4. second consecutive same-thread turn:
   - accepted from same tester;
   - dialogue continuity preserved;
   - provider-backed reply delivered;
   - no cross-thread contamination;
   - no OUTCOME_UNKNOWN.

5. same-thread coherence:
   runtime demonstrates context continuity sufficient for the second answer to belong to the same bounded dialogue session/thread.

6. privacy/log boundary:
   no persistent raw Telegram Update JSON, unnecessary audience identity, or raw unrelated comment text in proxy/application/debug/retry logs beyond accepted bounded runtime contract.

7. isolation:
   no evidence of provider/send effect for non-allowlisted user or wrong chat.

8. replay/collision:
   no detected replay collision;
   no duplicate provider/send effect for one accepted turn.

9. clean stop:
   service stopped after PASS or stop condition;
   final service state:
   inactive / dead / disabled / MainPID=0.

10. limits:
   accepted turns <= 50;
   OpenAI calls <= 50;
   duration <= 2h;
   nominal spend ceiling not exceeded.

Optional checks such as observing a foreign-user rejection may be NOT_OBSERVED if safely unavailable.
Do not recruit a second tester merely to prove rejection.

## Hard STOP conditions

Immediately stop service and end pilot if any occur:

- secret exposure;
- provider/send effect for non-allowlisted user;
- provider/send effect in wrong discussion/chat;
- cross-chat or cross-thread contamination;
- replay collision producing duplicate external effect;
- OUTCOME_UNKNOWN;
- unexpected provider/model substitution;
- unexpected mutation of admission/runtime config;
- need to widen scope;
- three consecutive provider/runtime failures;
- 50 accepted turns;
- 50 OpenAI calls;
- 2 hours from successful service start;
- nominal USD 5 ceiling reached/exceeded;
- OPERATOR says STOP;
- service cannot be cleanly controlled/stopped.

Do not improvise around a hard stop.

## Historical tasks

Do NOT replay:
- failed live r0.1;
- provenance r0.3/r0.4/r0.5/r0.6;
- final-gate r0.1.

They are evidence only.

## Data/evidence boundary

Preserve only what is needed to verify the pilot:
- RUN_ID;
- service start/stop state;
- accepted tester numeric ID;
- exact chat/thread IDs;
- accepted turn count;
- provider call count;
- model/provider identity;
- Telegram message IDs needed for effect/readback;
- generic outcome/status/error classes;
- bounded DB/session state evidence needed for continuity;
- privacy/log verification result.

Do not publish:
- credentials;
- unrelated participant identities;
- raw Update JSON;
- unnecessary raw dialogue content.

Dialogue content may exist in the runtime DB only under the accepted bounded transcript/privacy contract; do not broaden retention in this task.

## Completion

On PASS:
- stop service;
- verify final inactive/dead/disabled/MainPID=0;
- preserve immutable result artifact;
- exact readback;
- return KOO.

On FAIL/BLOCKED:
- stop service if it started;
- preserve exact failure point and side effects actually observed;
- do not retry automatically under the same authority;
- return KOO.

## Expected terminal

PASS_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02

or exact BLOCKED_/FAIL_ reason.

## Mandatory RETURN KOO

Return:
- exact task identity;
- RUN_ID;
- pre-live gates;
- service start evidence;
- LIVE_READY emission;
- confirmed tester/chat;
- accepted turn count;
- provider call count;
- exact provider/model;
- two-turn same-thread continuity result;
- Telegram delivery/readback evidence;
- replay/collision/OUTCOME_UNKNOWN status;
- privacy/log result;
- limit usage;
- final clean stop state;
- terminal verdict.

Then STOP.
