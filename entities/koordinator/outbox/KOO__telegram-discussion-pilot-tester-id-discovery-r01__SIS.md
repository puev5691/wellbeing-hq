# KOO -> SIS: Telegram discussion pilot tester-ID discovery gate r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Current installed discussion package PASS:
puev5691/wellbeing-hq@59455e46db80c490e740ce96fa3834348576506c:
entities/sisadmin/outbox/SIS__telegram-discussion-admission-r02-independent-review-install-verify__KOO.md
blob 3ed6d57f020f526f6c383e62c71498050c48bcd3
terminal PASS_SIS_TELEGRAM_DISCUSSION_ADMISSION_R02_READY_FOR_BOUNDED_LIVE_DISCUSSION_PILOT_GATE

Previous OPERATOR bounded-live decision record:
puev5691/wellbeing-hq@e49c80bd77c19276a4d30f015ea4b648aeed2e58:
entities/koordinator/outbox/KOO__telegram-single-entity-live-activation-missing-tester-ids-r01__OPERATOR.md

Recorded OPERATOR decisions:
- bounded live activation = YES;
- Telegram bot token available for root-only local provisioning = YES;
- OpenAI API key available for root-only local provisioning = YES;
- count-bounded dialogue transcript accepted = YES;
- only missing required input was exact tester numeric user ID.

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
type supergroup

Goal:
obtain one exact tester numeric user ID without requiring OPERATOR to discover/copy it manually.

Bounded procedure:

1. Fresh-verify current SIS writer, task, installed package state and service remains inactive/dead/disabled.
2. Using OPERATOR-assisted root-only procedure, populate Telegram bot-token credential source if still empty WITHOUT printing or returning the token.
3. Do NOT populate/use OpenAI key in this task unless needed only to verify the protected slot exists; no OpenAI call is permitted.
4. Perform exactly one read-only Telegram getWebhookInfo check.
5. If an active webhook exists:
   STOP and return exact webhook-removal blocker. Do not delete it under this task.
6. If no active webhook exists, perform a bounded Telegram getUpdates discovery cycle solely to identify the sender of an exact addressed command in the exact linked discussion:
   /ask@WBNP_Media_Bot
7. Accept a candidate tester ID only when all match:
   - chat.id == -1002429106148;
   - chat.type == supergroup;
   - message text/entity resolves to exact /ask@WBNP_Media_Bot command;
   - from.id is an integer;
   - sender is not the bot itself.
8. The first exact matching sender after this task activation becomes TESTER_1_CANDIDATE.
9. Do not persist raw message text, username, display name, raw Update JSON or unrelated member data.
10. Preserve only minimal evidence:
   - update_id;
   - exact discussion chat_id;
   - numeric from.id;
   - trigger class;
   - generic success/failure metadata.
11. Do NOT write the allowlist yet unless the exact task can prove this sender is the OPERATOR/tester intended by the human interaction in the same supervised cycle. Otherwise return the numeric ID to KOO/OPERATOR for one explicit confirmation.
12. Service remains inactive/dead/disabled throughout.
13. No Telegram sendMessage.
14. No OpenAI call.
15. No dialogue state mutation.
16. No Telegram rights/settings mutation.
17. No historical task replay.

Expected result:

PASS_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERED_R01
with exact numeric tester ID and minimal evidence,

or exact BLOCKED_* reason.

Mandatory RETURN KOO.
Then STOP.
