# KOO → KOD: Entity Resource Gateway live worker r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Basis

Gateway MVP independent PASS:
`fd49601948827cc43e46331ae98ab1f680101c0a`

Live-executor prep independent PASS:
`888e9fe64dccc2c12571b246cdf8d754e0df1214`

OpenAI technical final gate:
`787ec5df1878c7ddb0a5f2928c61e265b40959b0`

Anthropic adapter independent PASS:
`d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`

## Goal

Implement an isolated live-worker / LiveExecutorPort candidate that satisfies the already verified execution-prep contract, while keeping all real provider access disabled in this cycle.

Required:
- exact LiveExecutorPort implementation boundary;
- durable/atomic one-shot attempt ledger suitable for restart-safe reservation/consumption;
- hard timeout enforcement;
- max response byte limit;
- redirect policy fail-closed unless exact allowed target;
- provider/model/request-plan binding before egress;
- credential resolver interface accepting secret reference only;
- no credential material in logs/results/files;
- explicit OpenAI worker binding to accepted D0 transport contract;
- explicit Anthropic worker binding to verified Messages plan/reply boundary;
- exact one-call semantics;
- no retries;
- no project-state application;
- no external dispatch beyond provider request itself;
- returned ResourceResult remains NOT_GRANTED/unaccepted.

Tests:
- zero-network synthetic harness;
- restart/replay ledger tests;
- timeout;
- oversized response;
- redirect rejection;
- provider/model mismatch;
- stale authority;
- duplicate call prevention;
- credential-ref resolution boundary without secret value exposure.

Do not:
- perform real provider call;
- read/create real credential;
- mutate billing/account;
- deploy production;
- change accepted gateway/executor-prep/provider bytes;
- touch Telegram/TERA2/WBN.

Expected:
`PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker.

Return immutable candidate + tests + live-attachment boundary to KOO through Exchange Gate.
