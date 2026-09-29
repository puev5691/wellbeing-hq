# SIS -> KOO: Telegram personal sender identity condition diagnosis r0.1 result

status: PASS
terminal: PASS_SIS_TELEGRAM_PERSONAL_SENDER_IDENTITY_CONDITION_DIAGNOSED_R01
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Человекочитаемый итог

Read-only diagnosis установила Telegram-side причину отсутствия personal sender identity в linked discussion.

В exact discussion Bot API показывает:
- administrators_total = 2;
- creator_count = 1;
- creator_anonymous_count = 1;
- administrator_count = 1;
- bot_admin_count = 1;
- bot_admin_anonymous_count = 0.

Следовательно:
- единственный creator/owner exact discussion имеет is_anonymous = true;
- единственный второй administrator является bot @WBNP_Media_Bot;
- bot is_anonymous = false.

Предыдущая supervised delivery diagnosis уже доказала, что свежий exact /ask@WBNP_Media_Bot от OPERATOR UI context пришёл как message.sender_chat с sender_chat.type = channel и без admissible direct-human provenance.

Совокупность этих фактов соответствует Telegram administrator setting "Remain Anonymous".

Telegram также документирует, что:
- ChatMemberOwner.is_anonymous = true означает, что присутствие владельца скрыто;
- sender_chat используется для сообщений, отправленных от имени чата, в том числе anonymous administrators;
- при привязке канала к discussion group Telegram может автоматически включить "Remain Anonymous" для owner, после чего для возврата personal sender identity нужно отключить этот режим у владельца.

Подтверждённый diagnosis class:

OPERATOR_ADMIN_ANONYMOUS_MODE

Exact correction:
в exact discussion открыть настройки группы -> Administrators / Администраторы -> собственный owner profile -> отключить "Remain Anonymous" / "Оставаться анонимным"; затем вернуться в composer и выбрать personal user identity в "Написать от имени...".

После этого STOP. В этой задаче никакой human tester-ID discovery не выполняется.

## Exact task

puev5691/wellbeing-hq@3dea6c6a9eb694bad8c75a5485a111a119cad8b8:
entities/koordinator/outbox/KOO__telegram-personal-sender-identity-diagnosis-r01__SIS.md

blob:
7c4695deeea0e26565b065034a31a51d33f7d689

## Previous diagnosis

puev5691/wellbeing-hq@8b459a1c55348cce7a9636408ddfdc5ddb8dbd3e:
entities/sisadmin/outbox/SIS__telegram-discussion-delivery-admission-diagnosis-r01-result__KOO.md

blob:
63e50bb513b1b7e37ca0f06139a9aac70ed258e8

terminal:
PASS_SIS_TELEGRAM_DISCUSSION_DELIVERY_ADMISSION_DIAGNOSIS_R01

Verified prior root cause:
USER_MESSAGE_SENT_AS_CHAT / SEND_AS_CHANNEL

## Fresh reconciliation

HQ HEAD before execution/result publication:
3dea6c6a9eb694bad8c75a5485a111a119cad8b8

No later sender-identity diagnosis/correction task or result was observed before publication.

gate:
CLEAN

## Runtime safety state

Dialogue service:
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

Telegram settings mutation:
NONE

Admin-rights mutation:
NONE

Credential mutation:
NONE

Dialogue DB mutation:
NONE

## Read-only exact discussion evidence

chat_id:
-1002429106148

chat_type:
supergroup

is_forum:
false

linked_chat_id:
-1003606547591

Administrator aggregate evidence:
- ADMINS_TOTAL = 2
- ADMINS_CREATOR = 1
- ADMINS_CREATOR_ANONYMOUS = 1
- ADMINS_ADMINISTRATOR = 1
- ADMINS_ADMINISTRATOR_ANONYMOUS = 0
- ADMINS_BOT_ADMIN = 1
- ADMINS_BOT_ADMIN_ANONYMOUS = 0

Exact bot:
- status = administrator
- is_anonymous = false

No administrator usernames, display names, raw user records or unrelated participant identities were preserved.

## Root-cause classification

### A. OPERATOR_ADMIN_ANONYMOUS_MODE

VERIFIED

Evidence:
- exact discussion has exactly one creator;
- that creator has is_anonymous = true;
- the only other administrator is the bot;
- bot is not anonymous;
- prior exact target command from OPERATOR UI context was delivered via sender_chat/channel rather than direct human provenance;
- OPERATOR reports personal identity absent from "Написать от имени..." chooser.

This is the supported cause of the missing personal sender identity.

### B. SEND_AS_CHANNEL_SELECTION_STATE

RULED OUT as sole cause

Evidence:
the server-side owner state itself is anonymous; the issue is not merely that another sender was temporarily selected in the composer.

### C. CHAT_PERMISSIONS_OR_ADMIN_RIGHTS_EFFECT

VERIFIED in the specific form:
OWNER_ANONYMOUS_ADMIN_PRIVILEGE

No evidence supports a generic member permission restriction as the cause.

### D. LINKED_DISCUSSION_CHANNEL_ROLE_EFFECT

VERIFIED as configuration context, not as an independent blocker

Evidence:
- exact supergroup has linked_chat_id -1003606547591;
- Telegram documents that linking a channel to a discussion group can automatically enable Remain Anonymous for the owner.

### E. CLIENT_UI_STATE_ONLY

RULED OUT

Evidence:
server-side ChatMemberOwner anonymous state is independently visible through Bot API.

### F. UNKNOWN_TELEGRAM_SIDE_IDENTITY_CONDITION

RULED OUT for the current condition.

## What Bot API proves

Bot API proves:
- exact discussion owner exists;
- owner is anonymous;
- bot is the only other admin and is not anonymous;
- previous exact command arrived using sender_chat/channel provenance.

Bot API does not expose:
- the exact visual arrangement of the Android "Написать от имени..." chooser;
- whether Telegram Android immediately refreshes that chooser after the setting is changed;
- OPERATOR's local client cache state.

Those are UI observations only.

## Official Telegram semantics

Telegram Bot API:
https://core.telegram.org/bots/api

Relevant semantics:
- ChatMemberOwner.is_anonymous = true means the owner's presence in the chat is hidden;
- Message.sender_chat identifies a chat on whose behalf a message was sent, including anonymous administrator messages.

Telegram issue/official support clarification:
https://bugs.telegram.org/c/26783
https://bugs.telegram.org/c/9895/4

Telegram's published clarification states that after linking a channel to a discussion group, "Remain Anonymous" can be automatically enabled for the owner and can be disabled in Group Settings -> Administrators -> owner's profile.

## Exact OPERATOR action

On Telegram Android, in the exact linked discussion group:

1. Open the discussion group itself, not the channel.
2. Open group profile/settings.
3. Open Administrators / Администраторы.
4. Open your own owner profile.
5. Disable "Remain Anonymous" / "Оставаться анонимным".
6. Return to the discussion composer.
7. Open "Написать от имени..." and verify that the personal user identity is now available.
8. Select the personal user identity.

STOP after this UI correction.

Do not send a new discovery command until KOO issues a NEW exact human tester-ID discovery task.

If the "Remain Anonymous" control is unexpectedly absent or cannot be disabled, return that exact UI fact to KOO; do not improvise rights changes elsewhere.

## Mandatory RETURN KOO

Diagnosis class:
OPERATOR_ADMIN_ANONYMOUS_MODE

Evidence:
exact discussion owner is server-side anonymous; only other admin is non-anonymous bot; previous target arrived via sender_chat/channel.

UNKNOWN boundaries:
only client presentation/refresh behavior after correction remains UI-side.

Exact operator-side next action:
disable "Remain Anonymous" on the owner's own admin profile in the linked discussion, then select personal user identity in "Написать от имени...".

Service inactive:
CONFIRMED

Telegram settings mutated by SIS:
NONE

## Terminal

PASS_SIS_TELEGRAM_PERSONAL_SENDER_IDENTITY_CONDITION_DIAGNOSED_R01
