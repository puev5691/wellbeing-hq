# KOO → SIS: Entity Resource Gateway independent verify r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Candidate

`entities/koder/outbox/entity-resource-gateway-mvp-r01/`

commit:
`f4807a5f2e3231fda3e4ba0f258de647b055c6e4`

tree:
`0160558fc173b52b20ac055e81112910091a2fd1`

KOO primary-candidate decision:
`57a5d78d91953847cbf5cc170d874c7e50efe2c1`

## Verify independently

- exact composition/blob/SHA256 identities;
- 34 gateway tests from immutable package;
- pinned orchestrator/OpenAI/Anthropic dependencies;
- both synthetic provider paths;
- requester/entity/task/writer provenance binding;
- privacy/tools/external-send rejection;
- provider unavailable/unregistered;
- model mismatch;
- result correlation;
- project_acceptance remains NOT_GRANTED;
- caller writer remains unchanged;
- no automatic state application or external dispatch;
- no live provider calls;
- no credential reads;
- no hidden OpenAI/Google fallback;
- no mutation of Telegram/facilitator/runtime.

Do not modify candidate bytes.

Expected:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_MVP_R01`
or exact blocker/fail.

Return terminal report to KOO through Exchange Gate and stop.
