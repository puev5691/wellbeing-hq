# KOO -> SIS: Telegram discussion delivery/admission diagnosis r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact blocker basis:
puev5691/wellbeing-hq@284473bb5b3304308e0942fe6f3cd094c43ea407:
entities/sisadmin/outbox/SIS__telegram-discussion-human-tester-id-discovery-r03-result__KOO.md
blob 7f8cc8d0e7124e8cc5de2fb243b6d85873061ad1

terminal:
BLOCKED_SIS_TELEGRAM_DISCUSSION_HUMAN_TESTER_ID_DISCOVERY_R03_NO_FRESH_HUMAN_EVENT

Consumed prior live result:
puev5691/wellbeing-hq@be7799ecb52e1c1a66f49f301b82d8db410c751e:
entities/sisadmin/outbox/SIS__telegram-discussion-bounded-live-activation-r01-result__KOO.md

terminal:
FAIL_SIS_TELEGRAM_DISCUSSION_PILOT_R01_TESTER_IDENTITY_MISCLASSIFIED

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Observed facts so far:
- webhook absent;
- Bot API polling reachable;
- operator reports sending fresh command from intended human UI context;
- getUpdates did not expose an admissible direct-human event during r0.3;
- five observed target-context events had chat/channel sender provenance;
- service remains inactive/dead/disabled;
- no OpenAI/sendMessage/dialogue DB mutation in r0.3.

Goal:
determine, with bounded read-only Telegram evidence, why a fresh direct human command in the linked discussion is not appearing to the bot token as an admissible human message update.

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact blocker/result lineage;
   - no superseding Telegram diagnosis/discovery/live task/result;
   - dialogue service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - no dialogue process running;
   - protected Telegram credential remains locally available;
   - webhook remains absent by one fresh read-only getWebhookInfo.

2. Perform bounded read-only Bot API diagnosis only.
   No sendMessage and no Telegram settings mutation.

3. Inspect current bot-visible metadata needed to reason about delivery:
   - getMe minimal non-secret fields relevant to bot identity/capabilities;
   - getChat for exact discussion_chat_id;
   - getChatMember for bot in exact discussion;
   - any other read-only Bot API call strictly necessary to establish bot status/permissions relevant to receiving group messages.
   Preserve only minimal non-secret fields.

4. Diagnose likely delivery/admission classes with evidence, not guesses:

   A. BOT_PRIVACY_MODE_OR_COMMAND_DELIVERY
   - determine what can be established from Bot API-visible behavior/capabilities;
   - do not assume privacy mode value if Bot API cannot expose it directly;
   - distinguish official Bot API delivery rules from observed facts.

   B. USER_MESSAGE_SENT_AS_CHAT
   - check whether observed discussion messages use sender_chat;
   - distinguish “Send As channel/chat” UI behavior from direct human sender provenance.

   C. LINKED_CHANNEL_AUTOFORWARD
   - identify automatic linked-channel forward semantics separately from human message.

   D. TOPIC/THREAD_ROUTING
   - determine whether forum/topic/thread context changes update shape or command routing for this discussion.

   E. BOT_MEMBERSHIP/ADMIN/RESTRICTED_STATE
   - read bot membership/status/permissions in discussion;
   - identify any read-only evidence that could prevent visibility/commands.

   F. UPDATE_CURSOR/ALLOWED_UPDATES
   - inspect the actual discovery helper/getUpdates parameters and cursor behavior;
   - verify whether message updates are requested;
   - verify no stale offset/cursor accidentally skipped the intended human event;
   - do not mutate dialogue DB.

   G. COMMAND_ENTITY_SHAPE
   - establish from bounded observed events / official semantics whether /ask@WBNP_Media_Bot sent by a direct human would appear as message + bot_command entity;
   - do not retain raw text beyond exact trigger classification.

5. Run one supervised bounded observation window, only if needed after metadata checks, in which OPERATOR may send a fresh exact command in the discussion.
   During that window classify every relevant update into minimal categories only:
   - DIRECT_HUMAN_MESSAGE
   - SENDER_CHAT_MESSAGE
   - AUTOMATIC_FORWARD
   - BOT_MESSAGE
   - WRONG_CHAT
   - OTHER_RELEVANT_TYPE
   Do not store raw Update JSON, username, display name, unrelated participant data or arbitrary message content.

6. If a direct human update is observed:
   do NOT convert it into allowlist or start live service.
   Return minimal provenance evidence and diagnosis of why prior r0.3 missed it.

7. If no direct human update is observed:
   return exact strongest supported blocker class, for example:
   - BLOCKED_TELEGRAM_DISCUSSION_HUMAN_DELIVERY_NOT_VISIBLE_TO_BOT
   - BLOCKED_TELEGRAM_DISCUSSION_SEND_AS_CHAT_MODE_OBSERVED
   - BLOCKED_TELEGRAM_DISCUSSION_BOT_DELIVERY_POLICY_UNRESOLVED
   - BLOCKED_TELEGRAM_DISCUSSION_GETUPDATES_CURSOR_DEFECT
   - or another exact evidence-based class.

8. For each possible root cause, state:
   - VERIFIED;
   - RULED_OUT;
   - UNKNOWN;
   with exact minimal evidence.

9. Return one exact next condition/task class only.
   Examples:
   - user must switch Telegram “Send As” from channel/chat to personal identity and retry;
   - BotFather privacy setting requires separate OPERATOR action;
   - getUpdates helper/cursor requires code correction;
   - topic/command trigger requires KOD correction;
   - other precise condition.

10. DO NOT:
   - modify tester allowlist;
   - start/enable dialogue service;
   - call OpenAI;
   - send Telegram message;
   - change BotFather settings;
   - change Telegram chat/channel rights/settings;
   - change credentials;
   - mutate dialogue DB;
   - replay r0.3 discovery;
   - replay failed live r0.1.

Expected terminal:

PASS_SIS_TELEGRAM_DISCUSSION_DELIVERY_ADMISSION_DIAGNOSIS_R01

with a verified root cause / precise next condition,

or exact BLOCKED_/FAIL_ if diagnosis itself cannot close.

Mandatory RETURN KOO:
- minimal metadata evidence;
- classification of root-cause hypotheses;
- whether a direct human update was observed;
- exact next condition/task class;
- service inactive confirmation;
- explicit statement no allowlist/live/OpenAI mutation occurred.

Then STOP.
