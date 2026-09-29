# KOO -> SHT: SEMANTIC_DIALOGUE_ENGINE_R01 semantic/process model r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SHT writer:
puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da

Authority:
puev5691/wellbeing-hq@d5f1580f933d6bef1648b8e5ba630094653665cb:
entities/koordinator/outbox/semantic-dialogue-engine-r01/KOO__authorize-semantic-dialogue-engine-r01-parallel-design__OPERATOR.md

Roadmap:
puev5691/wellbeing-hq@ac269e3c1effb3fc6622351db54a2cc8efea8f5e:
entities/koordinator/outbox/semantic-dialogue-engine-r01/KOO__semantic-dialogue-engine-r01-development-roadmap__OPERATOR.md

Application profiles:
puev5691/wellbeing-hq@225f4392de4083d70ea2837def66c6a782919074:
entities/koordinator/outbox/semantic-dialogue-engine-r01/KOO__semantic-dialogue-engine-r01-application-profiles-r01__DESIGN.md

Design inputs:
Semantic Dialogue Lexicon r0.1 @ df4cce558482e9c6c9664120fd4ceaa04081ea04
Semantic Relations Lexicon r0.1 @ 653ba2de3c04238b21e258c4172826a392875347
ECL r0.1 @ 1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f

Task:
produce the semantic/process state-model candidate for SEMANTIC_DIALOGUE_ENGINE_R01.

Required:
1. validate semantic unit lifecycle and relation semantics;
2. identify missing/duplicate/ambiguous semantic types;
3. define state-transition skeleton for:
   - project operations;
   - media portal dialogue;
   - project economy/task/contract/accounting profile;
4. separate descriptive fact, inference, decision, authority, action, result and acceptance;
5. define failure/unknown/conflict states;
6. identify which transitions can be machine-checkable;
7. identify which transitions require human/OPERATOR decision;
8. define contribution -> task -> delivery -> verification -> acceptance -> accounting/contract event boundaries;
9. define publication -> claim -> source -> argument/counterargument -> correction/update boundaries;
10. stress-test for false authority, false completion, stale context and semantic last-write-wins.

Do not change active governance.
Do not create implementation authority.
Do not call providers or mutate runtime/economy.

Return:
one immutable semantic/process model result to KOO with contradictions, corrections and exact recommended changes to current candidates.

Mandatory RETURN KOO.
Then STOP.
