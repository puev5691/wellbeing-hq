# KOO reconciliation: Telegram sender identity condition r0.1

status: WAITING_OPERATOR_UI_ACTION
project_time: omitted

Exact SIS diagnosis:
puev5691/wellbeing-hq@8b459a1c55348cce7a9636408ddfdc5ddb8dbd3e:
entities/sisadmin/outbox/SIS__telegram-discussion-delivery-admission-diagnosis-r01-result__KOO.md
blob 63e50bb513b1b7e37ca0f06139a9aac70ed258e8

terminal:
PASS_SIS_TELEGRAM_DISCUSSION_DELIVERY_ADMISSION_DIAGNOSIS_R01

Verified root cause:
USER_MESSAGE_SENT_AS_CHAT / SEND_AS_CHANNEL

Observed exact trigger:
- update_id 560511141
- chat_id -1002429106148
- exact /ask@WBNP_Media_Bot matched
- sender_chat present
- sender_chat_id -1002183933851
- sender_chat_type channel
- direct human sender not present

Ruled out:
- webhook
- bot membership/admin state
- thread/topic routing
- allowed_updates
- command entity shape
- linked-channel auto-forward
- privacy mode as blocker for this addressed command

Next exact condition:
OPERATOR switches sender identity in linked discussion from channel/chat to personal user identity.

No NEW SIS discovery task should be issued before that UI-side condition is satisfied.

After OPERATOR confirms personal identity is selected and sends one fresh exact:
/ask@WBNP_Media_Bot
KOO may issue one NEW exact human tester-ID discovery task.

If Telegram UI offers no personal-user sender identity, KOO must instead issue a bounded Telegram-side sender-identity diagnosis/correction task.

No live service start.
No allowlist mutation.
No OpenAI call.
No historical replay.

terminal:
WAITING_OPERATOR_PERSONAL_SENDER_IDENTITY_SWITCH
