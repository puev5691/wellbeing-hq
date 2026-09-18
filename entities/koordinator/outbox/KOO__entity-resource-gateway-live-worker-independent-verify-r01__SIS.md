# KOO → SIS: Entity Resource Gateway live-worker independent verify r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-r01/`

commit:
`cd9f0c7327613ee29f9de54574ca141b557e5d18`

tree:
`222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`

KOD report:
`b56d5159bcf7951efcb21de6dd684d4f74907844`

expected source verdict:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY`

## Independently verify

- exact immutable package composition/blob/SHA256;
- 27 tests and successful rerun evidence;
- accepted gateway/executor-prep/provider dependencies unchanged;
- SQLite durable/atomic one-shot ledger:
  PRIMARY KEY, BEGIN IMMEDIATE, WAL, synchronous=FULL;
- restart/replay and concurrent duplicate prevention;
- reservation occurs before credential resolution/transport;
- hard timeout behavior and fail-closed unsupported execution environment;
- max response byte limit;
- redirect rejection;
- exact provider/model/request-plan binding before egress;
- CredentialResolver receives secret reference only;
- no credential value emitted to logs/results/files;
- exact OpenAI /v1/responses binding;
- exact Anthropic /v1/messages binding;
- one-call semantics, automatic retries=0;
- ResourceResult remains project_acceptance=NOT_GRANTED;
- caller writer unchanged;
- no gateway/provider writer authority;
- no project-state application;
- no external dispatch beyond future provider request;
- no real provider call;
- no real credential read/create;
- no account/billing mutation;
- no production deployment.

Do not modify candidate bytes.

Expected:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01`
or exact blocker/fail.

Return to KOO through Exchange Gate and stop.
