# KOO → KOD: Entity booster cost-probe r0.1

status: PREPARE_AND_RUN_WHEN_ACCOUNT_GATE_PRESENT
execution_mode: BOUNDED_COST_PROBE
priority: TOP_INFRASTRUCTURE

## Verified technical basis

Final live-worker PASS:
`18af0b778d5b30f15c20da989a39006f503dcff3`

Current KOD writer v0.4:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

## Purpose

Measure actual provider usage/cost for a small representative Entity-resource request instead of estimating from list prices alone.

## Probe matrix

OpenAI models, same exact prompt/input/output cap:
- `gpt-5.6-luna`
- `gpt-5.6-terra`
- `gpt-5.6-sol`

Anthropic comparative leg, only if an authorized Anthropic credential/account gate is already present:
- Claude Sonnet 5

Do not block OpenAI probe on Anthropic availability.

## Exact workload shape

Use one compact project-neutral benchmark task with:
- input target <= 10,000 text tokens;
- max output <= 2,000 text tokens;
- no tools/web/files;
- no private/project-secret content;
- identical semantic task across models;
- one request per model;
- retries = 0;
- fallback = none.

Record per call:
- provider/model;
- request id;
- input tokens;
- cached input tokens if reported;
- output/reasoning tokens as provider reports them;
- latency;
- provider finish/stop reason;
- HTTP/provider status;
- calculated list-price estimate;
- actual usage/cost field if provider exposes one;
- bounded qualitative output check without ranking a model as an authority.

## Hard gate

Do NOT make any live provider call until SIS/KOO verifies:
- exact API organization/project/account;
- API billing/prepaid active;
- project-scoped credential stored outside project artifacts;
- target model entitlement;
- exact LIVE_EXECUTION_AUTHORITY for this cost probe.

If gate is absent, return the exact minimal missing inputs and stop.

Expected after live execution:
`PASS_ENTITY_BOOSTER_COST_PROBE_R01`
or exact blocker/fail.
