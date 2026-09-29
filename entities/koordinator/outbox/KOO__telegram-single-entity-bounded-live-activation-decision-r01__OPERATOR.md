# KOO -> OPERATOR: Telegram single-Entity bounded live activation decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

## Exact readiness basis

SIS install/verify PASS:

puev5691/wellbeing-hq@8c28a4c43fda96d5fc4da7a268eac1475b1feba2:
entities/sisadmin/outbox/SIS__telegram-single-entity-mvp-independent-review-provisioning-r01__KOO.md

blob:
a0daf8c624f348c910596105910c3a743b56cd9d

terminal:
PASS_SIS_TELEGRAM_SINGLE_ENTITY_MVP_R01_READY_FOR_BOUNDED_LIVE_ACTIVATION_GATE

KOD package:

puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:
entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/

tree:
df57623dd7c69e1b06c95d297000a7a52a37ab3f

Target:
ruvds-xnqc6
service wellbeing-telegram-single-entity-pilot.service

Current service state:
inactive / dead / disabled

Live Telegram calls:
0

Live OpenAI calls:
0

## Proposed bounded live pilot

Purpose:
closed human dialogue pilot with invited testers using one Telegram bot and one OpenAI-backed dialogue Entity.

Transport:
Telegram long polling.

Provider:
OpenAI only.

No tools/project mutation.
No multi-provider routing.
No media publication automation.

### Proposed limits

tester_count_max:
5

accepted_user_turns_total_max:
50

provider_calls_total_max:
50

pilot_window:
2 hours from observed successful service start

nominal_cost_ceiling:
USD 5

Cost boundary:
if exact live monetary spend cannot be observed during the pilot, the hard technical safety boundary is provider_calls_total_max=50 plus the package-configured output-token bound. No claim of exact monetary spend is made without provider billing evidence.

### Transcript/privacy acceptance

Admitted dialogue text:
- is sent to OpenAI;
- is retained locally only as the package's bounded visible user/assistant transcript;
- is not stored as raw Telegram Update JSON;
- usernames/display names are not persisted;
- secrets are not logged/persisted;
- retention is count-bounded, not time-bounded.

Before an external tester begins, they must be informed of this boundary.

### Success criteria

PASS live pilot requires:
1. at least one admitted tester receives replies for at least two consecutive turns in the same dialogue;
2. dialogue context remains coherent across those turns;
3. exact replay causes no duplicate provider/send effect;
4. non-allowlisted tester causes no OpenAI call and no raw-text persistence;
5. controlled provider failure yields visible fallback;
6. no secret/raw-message leakage in operational logs;
7. service can be stopped cleanly.

### Stop conditions

STOP immediately on:
- secret exposure or suspected secret logging;
- non-allowlisted provider call;
- cross-chat/thread context contamination;
- replay collision or OUTCOME_UNKNOWN requiring reconciliation;
- three consecutive provider/runtime failures;
- provider call limit reached;
- pilot window reached;
- operator stop instruction;
- any unexpected project mutation;
- any requirement to widen scope beyond this decision.

Emergency stop:
sudo systemctl disable --now wellbeing-telegram-single-entity-pilot.service

## Required OPERATOR decision/input

To authorize the next SIS live task, OPERATOR must provide one response containing:

AUTHORIZE_TELEGRAM_SINGLE_ENTITY_PILOT_R01_BOUNDED_LIVE_ACTIVATION = YES

TESTER_NUMERIC_TELEGRAM_IDS = <one to five exact numeric IDs>

TELEGRAM_BOT_TOKEN_AVAILABLE_FOR_ROOT_ONLY_LOCAL_PROVISIONING = YES

OPENAI_API_KEY_AVAILABLE_FOR_ROOT_ONLY_LOCAL_PROVISIONING = YES

ACCEPT_COUNT_BOUNDED_DIALOGUE_TRANSCRIPT_FOR_THIS_PILOT = YES

The secret values themselves MUST NOT be placed in chat or GitHub.

If the OPERATOR wants different limits, change them in the same decision response.

## Effect of approval

Approval authorizes KOO to issue one NEW exact SIS live-activation task that may:
- populate tester allowlist with the exact approved IDs;
- use an OPERATOR-assisted root-only secret provisioning procedure without displaying values;
- perform read-only Telegram webhook-state check;
- if webhook is active, STOP and return an exact separate removal decision requirement unless the same future task carries explicit removal authority;
- start the exact installed service only after all pre-live checks PASS;
- execute the bounded closed pilot within the approved limits;
- stop and return exact terminal evidence.

Approval does not authorize any broader Telegram/provider/project activity.

terminal:
WAITING_OPERATOR_TELEGRAM_SINGLE_ENTITY_PILOT_R01_BOUNDED_LIVE_ACTIVATION_DECISION
