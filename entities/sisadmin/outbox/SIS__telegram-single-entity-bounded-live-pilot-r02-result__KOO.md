# SIS -> KOO: Telegram bounded live pilot r0.2 result

status: FAIL
terminal: FAIL_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02_CROSS_THREAD_CONTAMINATION
project_time: omitted

## Exact task

puev5691/wellbeing-hq@9a6b28018babe97ab62756f072a09c507a36955d:
entities/koordinator/outbox/KOO__telegram-single-entity-bounded-live-pilot-r02__SIS.md

blob:
a9f3bf3fb0aa071b699f10f19b37e974b5455e25

## Execution

RUN_ID:
ff955c3db4ed8de3c4c7

Pre-live gates:
PASS

Service start:
PASS

LIVE_READY:
YES

Tester:
6384602715

Discussion:
-1002429106148

Provider/model:
OpenAI / gpt-5.6-luna

## New live turns

Baseline DB update before pilot:
560511119

New turn 1:
- update_id=560511149
- state=COMMITTED
- error_class=NONE
- conversation_key=a93afb2296e00d32d63d976452824376fae25b2dee0dcc39e1ac9a09879d6314
- telegram_reply_message_id=101
- message roles=user,assistant

New turn 2:
- update_id=560511151
- state=COMMITTED
- error_class=NONE
- conversation_key=6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a
- telegram_reply_message_id=104
- message roles=user,assistant

The two new conversation_key values differ.

Therefore the required same-thread two-turn continuity was not established.

## Provider/send evidence

Invocation journal:
- request complete 200 = 2
- request rejected 422 = 2
- runtime ready = 1
- non-allowlisted journal lines = 0

In runtime r0.2, COMMITTED/request-complete occurs only after provider response and successful Telegram sendMessage followed by commit_turn.

Therefore two provider-backed Telegram reply effects were completed.

No raw dialogue text is included here.

## Safety

OUTCOME_UNKNOWN:
NONE observed in new committed turns

Replay collision:
NO EVIDENCE

Duplicate external effect:
NO EVIDENCE

Privacy/log boundary:
PASS for inspected invocation journal

Persistent enablement:
NO

Accepted new turns:
2 / 50

Successful provider-backed completed turns:
2 / 50

Duration:
within 2h

Exact billing telemetry:
not available in this readback; pilot stopped after two completed turns and hard-stop

## Final clean stop

LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
MainPID=0
NRestarts=0

## Mandatory RETURN KOO

pre-live gates:
PASS

service start:
PASS

LIVE_READY:
PASS

tester:
6384602715

chat:
-1002429106148

provider/model:
OpenAI / gpt-5.6-luna

new accepted turns:
2

new committed provider-backed turns:
2

Telegram reply message IDs:
101, 104

same-thread continuity:
FAIL

reason:
distinct conversation_key values for the two new committed turns

OUTCOME_UNKNOWN:
NO

privacy/log:
PASS

final clean stop:
PASS

next causal condition:
do not replay r0.2; diagnose exact Telegram UI/thread routing and visibility of reply message IDs 101 and 104 without re-running provider calls before deciding on any successor live task.

terminal:
FAIL_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02_CROSS_THREAD_CONTAMINATION
