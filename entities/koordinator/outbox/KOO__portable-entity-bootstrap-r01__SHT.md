# KOO -> SHT: portable Entity bootstrap r0.1 for cross-model dialogue testing

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SHT writer:
puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da

Priority authority:
puev5691/wellbeing-hq@e360ce75dfc8c803a54f69a3aae4188659bf6938:
entities/koordinator/outbox/KOO__telegram-single-entity-mvp-priority__OPERATOR.md

Goal:
prepare one compact provider-agnostic Entity bootstrap for manual testing in different neural chat systems and for later use inside the Telegram MVP.

Task:
design a minimal human-readable bootstrap that can instantiate one bounded project Entity in an arbitrary capable neural chat.

It must carry only what is necessary:
- ENTITY / ROLE / PURPOSE;
- allowed and forbidden actions;
- Resume-First rule;
- task/authority/current-state distinction;
- UNKNOWN discipline;
- minimal relevant source/context loading;
- current task slot;
- stop conditions;
- result contract;
- return/handoff rule;
- explicit handling when the host model lacks tools/memory/files/plugins;
- no model/platform-specific hidden assumptions.

Also provide:
- one concrete example Entity bootstrap suitable for the first Telegram dialogue pilot;
- one small cross-model test script with 5-10 prompts;
- observable success/failure criteria for role retention, dialogue continuity, non-invention, boundary compliance and human usability.

Do not activate any Entity.
Do not modify active governance.
Do not call providers.
Do not change Sources/canons.
Do not create automation.

Return one immutable candidate to KOO.

Mandatory RETURN KOO.
Then STOP.
