# KOO → SIS: Entity Resource Gateway live-executor prep independent verify r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Candidate

`entities/koder/outbox/entity-resource-gateway-live-executor-prep-r01/`

commit:
`aeb20f06d82103570d6706b9c4d3201b5e2a542b`

tree:
`c11a5828a963a501151aad2f78f6dc7960c5598d`

KOD terminal report:
`16fff16c817e8b2bce046204a5ccebc97876b84f`

expected source verdict:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_EXECUTOR_PREP_R01_READY_FOR_INDEPENDENT_VERIFY`

## Independently verify

- exact immutable package and dependencies;
- 39 tests;
- gateway package remains unchanged;
- `LIVE_EXECUTION_AUTHORITY` exact requester/entity/task/writer/request/plan/provider/model binding;
- NO_LIVE default;
- LIVE remains blocked without separate port attachment;
- credential reference never becomes credential value;
- OpenAI binding matches already verified D0 runtime contract;
- Anthropic binding matches independently verified Messages adapter;
- exactly one attempt / zero automatic retries;
- timeout/size bounds;
- ResourceResult remains unaccepted;
- project_acceptance NOT_GRANTED;
- caller writer unchanged;
- no project-state mutation;
- no external dispatch;
- no provider call / credential read / account mutation.

Do not modify candidate bytes.
No live provider call.
No credentials.
No production deployment.

Expected:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_LIVE_EXECUTOR_PREP_R01`
or exact blocker/fail.

Return to KOO through Exchange Gate and stop.
