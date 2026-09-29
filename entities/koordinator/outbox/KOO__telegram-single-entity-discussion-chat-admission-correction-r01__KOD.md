# KOO -> KOD: Telegram single-Entity MVP discussion-chat admission correction r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended KOD writer:
puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412

Current accepted MVP package:
puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:
entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/
tree df57623dd7c69e1b06c95d297000a7a52a37ab3f

SIS review/provisioning PASS:
puev5691/wellbeing-hq@8c28a4c43fda96d5fc4da7a268eac1475b1feba2:
entities/sisadmin/outbox/SIS__telegram-single-entity-mvp-independent-review-provisioning-r01__KOO.md
terminal PASS_SIS_TELEGRAM_SINGLE_ENTITY_MVP_R01_READY_FOR_BOUNDED_LIVE_ACTIVATION_GATE

Verified Telegram media mapping:
puev5691/wellbeing-hq@3f8e04d143320f1957ea7e491222a5c4d0f6d037:
entities/webmaster/outbox/WEB__telegram-media-reconciliation-r01__KOO.md

Verified bot:
@WBNP_Media_Bot
id 8866633840
administrator in channel and linked discussion.

Verified channel:
@wbnp_pev5691_15042026
id -1003606547591

Verified linked discussion:
id -1002429106148
type supergroup
bot administrator

Task:
produce the smallest correction package that allows the existing single-Entity dialogue MVP to operate in the verified linked discussion supergroup instead of requiring private user_id == chat_id admission.

Required:
1. bind pilot admission to exact discussion chat_id -1002429106148;
2. preserve closed-pilot behavior;
3. do NOT answer every ambient group message by default;
4. define one explicit activation trigger for a dialogue turn, preferably reply-to-bot and/or explicit bot mention/command, using Telegram update fields actually available;
5. keep per-thread/topic dialogue isolation where Telegram supplies thread/topic identity;
6. retain replay/collision/OUTCOME_UNKNOWN protections;
7. retain bounded transcript/privacy behavior;
8. no username/display-name persistence;
9. no project authority from dialogue;
10. update tests for:
   - correct discussion chat admitted;
   - other chats rejected before provider call;
   - ambient non-addressed group message ignored;
   - addressed turn accepted;
   - multi-turn same-thread dialogue;
   - different thread/topic isolation;
   - replay no duplicate effect.
11. preserve polling route and systemd credential mechanism.
12. provide exact upgrade/install diff from current installed package.

Do not:
- perform live Telegram/OpenAI calls;
- start service;
- read secrets;
- change bot/channel rights;
- mutate active governance;
- redesign whole MVP.

Return immutable correction result/package to KOO and STOP.
