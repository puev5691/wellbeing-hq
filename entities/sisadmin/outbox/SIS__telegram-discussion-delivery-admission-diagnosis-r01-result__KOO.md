# SIS -> KOO: Telegram discussion delivery/admission diagnosis r0.1 result

status: PASS
terminal: PASS_SIS_TELEGRAM_DISCUSSION_DELIVERY_ADMISSION_DIAGNOSIS_R01
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Человекочитаемый итог

Диагностика закрыла причину предыдущего r0.3 blocker.

Свежий exact trigger /ask@WBNP_Media_Bot дошёл до Bot API в exact linked discussion, был распознан как bot_command и имел корректный thread context.

Но Telegram представил отправителя не как прямого пользователя, а через message.sender_chat:

sender_chat_present = true
sender_chat_id = -1002183933851
sender_chat_type = channel

Прямого human sender в этом событии нет.

Следовательно r0.3 не "пропустил" допустимое human-сообщение: он корректно отклонил сообщения, отправленные от имени канала/чата.

Подтверждённый root cause:
USER_MESSAGE_SENT_AS_CHAT / SEND_AS_CHANNEL.

## Exact task

puev5691/wellbeing-hq@8c16b80d2afbb9716813ba0dc0d106a15d4a450d:
entities/koordinator/outbox/KOO__telegram-discussion-delivery-admission-diagnosis-r01__SIS.md

blob:
41214dccea97e44e6b0ff9b50db18d6de410f58f

## Current writer verified

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Blocker lineage verified

puev5691/wellbeing-hq@284473bb5b3304308e0942fe6f3cd094c43ea407:
entities/sisadmin/outbox/SIS__telegram-discussion-human-tester-id-discovery-r03-result__KOO.md

blob:
7f8cc8d0e7124e8cc5de2fb243b6d85873061ad1

terminal:
BLOCKED_SIS_TELEGRAM_DISCUSSION_HUMAN_TESTER_ID_DISCOVERY_R03_NO_FRESH_HUMAN_EVENT

## Fresh reconciliation

HQ HEAD before execution:
8c16b80d2afbb9716813ba0dc0d106a15d4a450d

No later Telegram diagnosis/discovery/live task or result was observed before result publication.

gate:
CLEAN

## Runtime safety state

host:
ruvds-xnqc6

dialogue service:
wellbeing-telegram-single-entity-pilot.service

final:
- LoadState = loaded
- ActiveState = inactive
- SubState = dead
- UnitFileState = disabled
- MainPID = 0

Dialogue process:
ABSENT

Allowlist mutation:
NONE

OpenAI call:
NONE

Telegram sendMessage:
NONE

Telegram rights/settings mutation:
NONE

Credential mutation:
NONE

Dialogue DB mutation:
NONE

## Read-only Bot API metadata

Webhook:
- active = NO
- pending_update_count = 0

getMe:
- bot_id = 8866633840
- is_bot = true
- can_join_groups = true
- can_read_all_group_messages = false

Interpretation:
Bot privacy mode is enabled at bot configuration level.
This is not the cause of the observed exact command delivery failure because the exact addressed command was in fact delivered to the bot during the supervised observation.

getChat exact discussion:
- id = -1002429106148
- type = supergroup
- is_forum = false
- linked_chat_id = -1003606547591

getChatMember for bot:
- status = administrator
- is_anonymous = false
- can_manage_chat = true
- can_delete_messages = true
- can_restrict_members = true
- can_pin_messages = true
- can_manage_topics = true

Bot membership/admin state therefore does not prevent receipt of the observed command.

## Supervised observation

Observation used getUpdates with:
allowed_updates = ["message"]

No webhook was active.

Baseline pending message updates:
0

Observed target:
- update_id = 560511141
- exact trigger = true
- bot_command entity match = true
- message_thread_id = 90
- is_topic_message = false
- is_automatic_forward = false
- sender_chat_present = true
- sender_chat_id = -1002183933851
- sender_chat_type = channel

Classification:
SENDER_CHAT_MESSAGE

Direct-human from.id:
NOT PRESENT AS ADMISSIBLE HUMAN PROVENANCE

Counters:
- DIRECT_HUMAN_MESSAGE = 0
- SENDER_CHAT_MESSAGE = 1
- AUTOMATIC_FORWARD = 0
- BOT_MESSAGE = 0
- WRONG_CHAT = 0
- OTHER_RELEVANT_TYPE = 0

## Root-cause classification

### A. BOT_PRIVACY_MODE_OR_COMMAND_DELIVERY

Privacy mode enabled:
VERIFIED

Evidence:
getMe.can_read_all_group_messages = false

Privacy mode as cause of exact /ask@WBNP_Media_Bot not reaching Bot API:
RULED_OUT

Evidence:
the exact addressed command was delivered as an Update and its bot_command entity matched.

Official Telegram Bot API / bot-feature semantics:
- privacy-enabled bots receive commands explicitly addressed to them;
- getMe.can_read_all_group_messages indicates whether privacy mode is disabled.

Sources:
https://core.telegram.org/bots/api
https://core.telegram.org/bots/features

### B. USER_MESSAGE_SENT_AS_CHAT

VERIFIED

Evidence:
- exact target event had sender_chat present;
- sender_chat.type = channel;
- sender_chat.id = -1002183933851;
- no admissible direct-human provenance was present.

This is the verified root cause.

### C. LINKED_CHANNEL_AUTOFORWARD

RULED_OUT for the observed target command

Evidence:
- is_automatic_forward = false;
- observed sender_chat_id = -1002183933851;
- linked discussion channel id = -1003606547591;
- the two IDs differ.

Therefore the observed target was not the linked-channel automatic forward class that caused the earlier 777000 misclassification.

### D. TOPIC/THREAD_ROUTING

RULED_OUT as delivery blocker

Evidence:
- is_forum = false;
- observed message_thread_id = 90;
- is_topic_message = false;
- the target command still arrived in getUpdates.

Thread context therefore did not prevent delivery.

### E. BOT_MEMBERSHIP/ADMIN/RESTRICTED_STATE

RULED_OUT

Evidence:
bot status = administrator in the exact discussion and the target command was delivered.

### F. UPDATE_CURSOR/ALLOWED_UPDATES

RULED_OUT as cause of the reproduced missing-human result

Evidence:
- allowed_updates = ["message"] is correct for the observed target;
- supervised observation used a non-negative baseline and received the fresh command;
- the event provenance itself is sender_chat/channel, explaining why r0.3 rejected it.

r0.3 used offset=-1 for baseline. Official Bot API semantics state that a negative getUpdates offset retrieves from the end of the queue and forgets earlier updates. That baseline pattern is not needed for future discovery helpers, but the reproduced fresh target proves the current failure class is sender provenance rather than update type/cursor invisibility.

Official source:
https://core.telegram.org/bots/api

### G. COMMAND_ENTITY_SHAPE

VERIFIED

Evidence:
- exact trigger matched;
- bot_command entity matched;
- update type was message.

The command syntax is therefore valid for Bot API delivery.

## Why r0.3 returned no human candidate

r0.3 required:
sender_chat absent

The reproduced target command has:
sender_chat present
sender_chat.type = channel

Therefore r0.3 correctly rejected this event as non-human chat sender provenance.

The Telegram client UI presentation is not sufficient evidence of direct-user provenance.

## Exact next condition

OPERATOR must change the Telegram sender identity in the linked discussion from channel/chat identity to the personal user identity before any new human tester-ID discovery.

After that UI-side identity switch is completed, KOO may issue one NEW exact human tester-ID discovery task.

If Telegram does not offer a personal-user sender choice in that discussion, the next task must instead diagnose/change that Telegram-side sender-identity condition with explicit OPERATOR authority.

Do NOT:
- reuse 777000;
- infer human ID from sender_chat;
- modify allowlist before a direct-human event is proven;
- replay r0.3;
- replay failed live r0.1.

## Mandatory RETURN KOO

Verified root cause:
USER_MESSAGE_SENT_AS_CHAT / SEND_AS_CHANNEL

Direct human update observed:
NO

Exact target update observed:
YES

Exact next condition:
OPERATOR switches discussion sender identity to personal user, then NEW human tester-ID discovery.

Service inactive:
CONFIRMED

Allowlist/live/OpenAI mutation:
NONE

## Terminal

PASS_SIS_TELEGRAM_DISCUSSION_DELIVERY_ADMISSION_DIAGNOSIS_R01
