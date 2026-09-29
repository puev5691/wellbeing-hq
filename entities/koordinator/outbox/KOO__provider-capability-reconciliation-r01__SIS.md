# KOO -> SIS: provider capability reconciliation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION

Resume-First.

Current SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Completed priority line:
puev5691/wellbeing-hq@e902bebb542197fb6e77184649bb82c1831e91c7
PASS_SIS_GWR_CONTOUR_RETIRE_R01_RETIREMENT_COMPLETE_CONSUMED

Next line:
multi-provider capability reconciliation.

Providers:
OpenAI
Anthropic
Gemini
DeepSeek

Task:
reconcile current project evidence for each provider and return:
- verified existing artifacts;
- current readiness;
- missing evidence;
- blockers;
- one next exact implementation or review task and its owner.

Read-only design/reconciliation only.
No external service actions.
No production changes.
No historical task replay.

Return immutable result to KOO.
Then STOP.
