# KOO -> SIS: Telegram single-entity live-pilot runtime preflight r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Priority authority:
puev5691/wellbeing-hq@e360ce75dfc8c803a54f69a3aae4188659bf6938:
entities/koordinator/outbox/KOO__telegram-single-entity-mvp-priority__OPERATOR.md

Goal:
prepare the exact host/runtime path needed for a closed live Telegram dialogue pilot with one neural Entity and invited human testers.

Known historical Phase1B host blocker:
commit a49040d2e9b4ecceeb4827d9e224e0a5e1eee952
terminal BLOCKED_PRIVILEGE_REQUIRED

Task:
perform fresh read-only runtime/deployment preflight and produce one exact provisioning/deployment plan compatible with the current intended KOD MVP.

Required:
1. current host/service/path state;
2. current privilege boundary;
3. exact config/data/service paths to use or exact reason a new bounded path is required;
4. bot token and OpenAI credential secret-reference mechanism without reading secret values;
5. network/listener/webhook or polling feasibility;
6. closed-tester allowlist mechanism;
7. logging/privacy/retention boundary;
8. startup/stop/rollback commands;
9. exact privileged actions requiring OPERATOR assistance;
10. live-pilot go/no-go checklist.

Do not deploy.
Do not start live service.
Do not send Telegram messages.
Do not call provider.
Do not read/print secrets.
Do not mutate billing/accounts.
Do not change Sources/canons.
Do not replay old host tasks.

Return one immutable result to KOO with exact blocker or READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING.

Mandatory RETURN KOO.
Then STOP.
