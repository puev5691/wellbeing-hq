# KOO -> SIS: Telegram discussion human tester-ID discovery r0.3

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact failed live result:
puev5691/wellbeing-hq@be7799ecb52e1c1a66f49f301b82d8db410c751e:
entities/sisadmin/outbox/SIS__telegram-discussion-bounded-live-activation-r01-result__KOO.md
blob a5d027102c043f901af3160bbb161d58c4ca4860

terminal:
FAIL_SIS_TELEGRAM_DISCUSSION_PILOT_R01_TESTER_IDENTITY_MISCLASSIFIED

Failed live execution:
CONSUMED / NON_REPLAYABLE

Known invalid pseudo-tester:
777000

Classification:
Telegram backward-compatible fake sender for automatically forwarded linked-channel message.
MUST NOT be accepted as human tester.

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Installed dialogue runtime:
host ruvds-xnqc6
service wellbeing-telegram-single-entity-pilot.service
package /opt/wellbeing/telegram-single-entity-mvp-r02

Current service expected prestate:
inactive / dead / disabled / MainPID=0

Goal:
discover the intended human tester numeric user ID from one fresh direct human-addressed command in the exact linked discussion, with explicit exclusion of channel-forward/fake-sender events.

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact failed-live result identity;
   - no superseding Telegram discovery/live task/result;
   - service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - no dialogue process running;
   - Telegram bot protected credential remains locally available;
   - do not modify current allowlist in this task.

2. Perform one read-only getWebhookInfo.
   If webhook active:
   STOP with exact blocker.
   Do not remove it.

3. If webhook absent, perform bounded getUpdates discovery only.

4. Discovery target:
   exact addressed command:
   /ask@WBNP_Media_Bot

   exact discussion:
   chat.id == -1002429106148
   chat.type == supergroup

5. A candidate human tester may be accepted ONLY when ALL are true:

   a. exact addressed command matches;
   b. message.sender_chat is ABSENT / null;
   c. message.is_automatic_forward is NOT true;
   d. message.from exists;
   e. message.from.id is integer;
   f. message.from.id != 8866633840;
   g. message.from.id != 777000;
   h. message.from.is_bot is not true, where field is present;
   i. update is a fresh direct human message observed after this task activation/discovery boundary;
   j. event is not an automatic linked-channel forward and not a message sent on behalf of a chat/channel.

6. Explicit rejection classes:
   - sender_chat present -> REJECT_NON_HUMAN_CHAT_SENDER
   - is_automatic_forward true -> REJECT_AUTOMATIC_FORWARD
   - from.id == 777000 -> REJECT_TELEGRAM_FAKE_SENDER_777000
   - from.is_bot true -> REJECT_BOT_SENDER
   - wrong chat -> REJECT_WRONG_CHAT
   - wrong/not-addressed command -> IGNORE_NOT_TARGET_DISCOVERY_EVENT

Rejected events MUST NOT become candidates.

7. The first event satisfying ALL human criteria becomes:
   HUMAN_TESTER_1_CANDIDATE=<numeric from.id>

8. Preserve only minimal evidence:
   - update_id;
   - discussion_chat_id;
   - numeric from.id;
   - sender_chat_present = false;
   - is_automatic_forward = false;
   - from_is_bot = false/absent;
   - trigger_class;
   - generic validation outcome.

9. Do NOT preserve/return:
   - raw message text;
   - username;
   - display name;
   - raw Update JSON;
   - unrelated participants;
   - channel-forward payloads beyond generic rejection counters/classes.

10. Do NOT:
   - modify tester allowlist;
   - start/enable dialogue service;
   - call OpenAI;
   - send Telegram messages;
   - modify Telegram rights/settings;
   - mutate credentials;
   - mutate dialogue DB;
   - replay prior discovery/live tasks.

11. After discovering candidate:
   STOP.
   Return candidate to KOO/OPERATOR for explicit human confirmation.
   Do NOT infer that candidate is intended tester merely because it passed protocol-level human provenance.

Expected terminal:

PASS_SIS_TELEGRAM_DISCUSSION_HUMAN_TESTER_ID_DISCOVERED_R03

with exact HUMAN_TESTER_1_CANDIDATE,

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- minimal evidence above;
- rejected fake/automatic-forward count/classes if observed, without raw content;
- service inactive confirmation;
- explicit statement that allowlist remains unchanged;
- explicit next condition: OPERATOR confirmation of candidate identity.

Then STOP.
