# KOO → KOD: Entity booster runtime consolidation r0.2

status: TASK
priority: P0
execution_mode: BOUNDED_NON_LIVE_ENGINEERING
project_time: omitted; trusted project-time source not used

## Operator direction

Entity AI resource boosters are the primary infrastructure priority.

Goal:
increase the practical reasoning/resource capability of Entities through a provider-neutral bounded resource path, without transferring Entity authority to external models/providers.

## Resume-First

Start with fresh GitHub preflight of:
`puev5691/wellbeing-hq`.

Verify current KOD writer/recovery boundary before mutation.

Do not trust historical chat state when it conflicts with current evidence.

## Verified technical basis

Use, after exact readback, the current verified lineages including:

- booster priority record:
  commit `9ab3205f99bfb4865a11369b34b92c8d0f8f582e`;

- Entity Resource Gateway MVP independent PASS:
  commit `fd49601948827cc43e46331ae98ab1f680101c0a`;

- final Entity Resource Gateway live-worker independent PASS:
  commit `18af0b778d5b30f15c20da989a39006f503dcff3`;

- current exact final live-worker package referenced by that PASS:
  `entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/`;

- provider-neutral orchestrator/runtime line:
  inspect current exact artifacts associated with orchestrator MVP/runtime integration and use only current verified identities;

- OpenAI and Anthropic provider adapters:
  use only current independently verified exact candidates/identities discovered by fresh preflight.

Historical cost probe blocker:
`BLOCKED_ENTITY_BOOSTER_COST_PROBE_R01_ACCOUNT_GATE_ABSENT`.

That blocker remains binding for real provider calls unless fresh evidence proves the exact gates now exist.

## Required work

Build one coherent booster runtime consolidation candidate r0.2 from the already verified components.

The candidate must make the path understandable and executable as:

`Entity bounded request → authority/policy gate → Resource Gateway → provider-neutral orchestrator → selected provider adapter → bounded result → requesting Entity review`.

### 1. Consolidate, do not rewrite

Prefer composition/reuse of existing verified components.

Do not create a competing orchestrator or second gateway unless an exact incompatibility proves it necessary.

Document any component that must be replaced and why.

### 2. Stable Entity-facing entrypoint

Provide one clear local entrypoint/API/CLI contract suitable for later Entity use.

It must:
- accept a bounded request envelope;
- bind requester Entity/task/writer identities;
- bind provider + model explicitly;
- bind data/privacy class;
- bind tools/capabilities explicitly;
- fail closed on missing/invalid authority;
- never silently change provider/model;
- never silently fall back to another provider.

### 3. Non-live end-to-end execution

Implement/test a complete synthetic/replay end-to-end path for at least:
- OpenAI adapter;
- Anthropic adapter.

No real provider network calls.
No real credential reads.
No billing/account mutation.

Use exact verified fixtures/replay mechanisms or create bounded synthetic fixtures where needed.

### 4. Preserve live-worker safety

The r0.2 candidate must preserve the verified live-worker boundaries, including:
- durable one-shot attempt ledger;
- exactly-one claimant behavior;
- no automatic provider retry;
- no provider fallback;
- hard timeout;
- bounded response/read;
- redirect fail-closed;
- secret-reference-only credential interface;
- no credential material in project artifacts;
- no provider/gateway writer authority;
- project acceptance remains NOT_GRANTED;
- no project-state mutation by provider result.

### 5. Entity result contract

Return a bounded machine-verifiable result plus a human-facing summary suitable for the requesting Entity.

The result must clearly distinguish:
- technical execution success;
- provider/model actually used;
- usage/cost fields where genuinely available;
- blocker;
- project acceptance;
- routing/dispatch state.

Do not invent latency, cost, usage or provider facts.

### 6. Live-readiness matrix

Produce a concise readiness matrix separating:
- already verified technical capability;
- exact missing account/billing/credential/model-entitlement facts;
- exact missing LIVE_EXECUTION_AUTHORITY;
- what can be tested without those facts;
- one smallest future live probe after all gates are proven.

Do not perform that future live probe in this task.

### 7. Tests

Add deterministic tests covering at minimum:
- OpenAI synthetic/replay PASS;
- Anthropic synthetic/replay PASS;
- wrong Entity/task/writer blocked;
- privacy/data-class violation blocked;
- unauthorized tools blocked;
- provider unavailable blocked without fallback;
- model mismatch blocked;
- duplicate/replay attempt blocked or deterministically handled by the existing one-shot contract;
- malformed/oversized provider response blocked;
- no credential/network access in non-live mode;
- result does not alter caller writer/project acceptance.

## File Artifact Service boundary

Do not expand this task into a general File Artifact Service integration.

If a small direct dependency is necessary for booster input/output packaging, use the already independently verified service by exact identity and document that limited dependency.

Otherwise leave File Artifact Service for its separate backlog item.

## Forbidden

- real OpenAI/Anthropic/provider calls;
- credential create/read/use;
- account or billing mutation;
- production deployment;
- provider fallback;
- external model authority over Entity/project decisions;
- Project Source changes;
- automation/cron;
- unrelated portal/Telegram/memory work.

## Expected terminal result

Return exactly one:

`PASS_KOD_ENTITY_BOOSTER_RUNTIME_R02_READY_FOR_INDEPENDENT_VERIFY`

or

`BLOCKED_KOD_ENTITY_BOOSTER_RUNTIME_R02: <exact blocker>`

or exact FAIL.

Terminal result must include:
- exact candidate locator/identity;
- tests executed/results;
- reused verified components;
- changed/new components;
- live calls = 0;
- credential reads = 0;
- next independent verifier: SIS.

Address result to KOO and SIS.
Stop after terminal result.
