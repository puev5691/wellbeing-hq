# KOO → KOD: Entity Resource Gateway live-executor preparation r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Basis

Gateway independent PASS:
`fd49601948827cc43e46331ae98ab1f680101c0a`
verdict:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_MVP_R01`

Primary gateway package:
`entities/koder/outbox/entity-resource-gateway-mvp-r01/`
commit `f4807a5f2e3231fda3e4ba0f258de647b055c6e4`

OpenAI technical final gate:
`787ec5df1878c7ddb0a5f2928c61e265b40959b0`
verdict:
`PASS_SIS_OPENAI_LIVE_D0_FINAL_GATE_R02_READY_FOR_OPERATOR_ACCOUNT_GATE`

Anthropic adapter independent PASS:
`d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`

## Goal

Prepare the gateway execution boundary that can later perform one separately authorized bounded live provider call without changing gateway authority semantics.

Required:
- live executor interface separated from gateway core;
- explicit `LIVE_EXECUTION_AUTHORITY` object/gate;
- exact requester/task/writer binding;
- provider/model binding;
- credential reference only, never credential value in request/result/log;
- OpenAI live transport adapter binding to the already verified runtime contract;
- Anthropic transport boundary compatible with verified Messages adapter but no live call;
- exact no-live default;
- zero-network self-tests;
- timeout/retry policy explicit and bounded;
- result returns to Entity as unaccepted resource;
- project_acceptance remains NOT_GRANTED;
- caller writer unchanged;
- no auto-dispatch / no project-state mutation.

No live provider call.
No credential read/create.
No billing/account mutation.
No production deployment.
Do not mutate accepted gateway package or existing provider candidates.
No Telegram/TERA2/WBN changes.

Expected:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_EXECUTOR_PREP_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker.

Return immutable candidate + tests + execution boundary through Exchange Gate and stop.
