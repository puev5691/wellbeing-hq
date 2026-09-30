# KOO -> SIS: Telegram routing observability r0.1 independent review / install-readiness

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59.

Exact KOD result:
puev5691/wellbeing-hq@b13efdd6fe32a72c4e8a0f58e2a009457b2e329b:
entities/koder/outbox/KOD__telegram-routing-observability-r01-result__KOO.md
blob 20aa087daec5497007b1cd307c36e17047156723

terminal:
PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW

Exact candidate package:
puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/
tree bbe40dc80670b33594f997cea52e42508a7ae12b

Status:
CANDIDATE_NOT_INSTALLED

Exact blocker basis:
puev5691/wellbeing-hq@826068657421e3f2209f3c289528a5577884246c:
entities/sisadmin/outbox/SIS__telegram-same-thread-bounded-live-pilot-r03-result__KOO.md
blob a9ff18cce3e54e830bc772cd5ae43eb9a561a628

terminal:
BLOCKED_SIS_TELEGRAM_SAME_THREAD_LIVE_R03_REPLY_VISIBILITY_NOT_CONFIRMED

Perform ONLY independent review and install-readiness verification.

Required:
1. exact package/tree/blob/readback verification;
2. reproduce KOD offline test suite, target 35/35;
3. review additive/idempotent DB migration and legacy-row preservation;
4. verify privacy boundary:
   - no raw Update JSON;
   - no full Telegram Message;
   - no usernames/display names;
   - no unrelated identities;
   - no raw provider response;
5. verify bounded routing fields:
   inbound_message_id,
   message_thread_id,
   direct_topic_id,
   trigger_class,
   outbound_message_id,
   returned_chat_id,
   returned_message_thread_id,
   returned_direct_topic_id,
   returned_is_topic_message;
6. verify conversation_key semantics unchanged;
7. verify admission/allowlist/provider/model/polling unchanged;
8. verify send-success + routing-persistence failure remains fail-closed OUTCOME_UNKNOWN with no duplicate resend;
9. verify read-only diagnose-routing helper returns only bounded metadata;
10. assess exact install/rollback procedure and host delta.

DO NOT:
- install package;
- mutate live host;
- start/enable service;
- call Telegram;
- call OpenAI;
- read/disclose credentials;
- mutate allowlist;
- change channel/bot settings;
- start live test;
- modify package.

Expected terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY
or exact NEEDS_REWORK_/BLOCKED_/FAIL_.

If PASS:
return exact separately bounded install/verify scope.
PASS does not authorize installation or live start.

Mandatory RETURN KOO.
Then STOP.
