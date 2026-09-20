# KOO → OPERATOR: Entity booster OpenAI live-path decision gate

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Human meaning

Entity booster runtime r0.2 has passed independent SIS verification.

What is already proven:
- exact immutable booster package and dependencies;
- deterministic OpenAI replay path;
- deterministic Anthropic replay path;
- one-shot ledger and concurrency safety;
- no silent provider/model fallback;
- authority/result boundaries;
- OpenAI project/account/prepaid readiness;
- OpenAI Luna/Terra/Sol/Astra entitlement evidence.

What is not yet true:
- current booster runtime is still REPLAY_ONLY;
- LIVE_EXECUTION_AUTHORITY is NOT_GRANTED;
- current runtime does not read/use a real credential;
- Anthropic live account/billing/credential/model gates are not proven.

Therefore no live provider call is authorized now.

## Current technical recommendation

The first live booster path should be OpenAI, not Anthropic.

Before one real bounded OpenAI call, the project needs one more technical step:
build and independently verify a live-capable integration that binds the already verified live-worker to the Entity-facing booster authority/result contract without weakening:
- one-shot execution;
- retries=0;
- no fallback;
- explicit provider/model;
- exact Entity/task/writer binding;
- privacy/tools binding;
- bounded output;
- project_acceptance=NOT_GRANTED;
- no provider/gateway writer authority.

That preparation itself must make zero live provider calls.

## Decision requested

Approve the bounded preparation of the first OpenAI live booster path.

Exact decision token:

`AUTHORIZE_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01`

## Effect if approved

KOO will:
1. create one exact KOD task to build the live-capable OpenAI booster integration using the already verified booster r0.2 + live-worker;
2. prohibit live calls, credential reads/use, billing/account mutation and production deployment during that task;
3. route the resulting candidate to SIS for independent verification;
4. after SIS PASS, return a separate OPERATOR decision gate for exactly one bounded D0 OpenAI live call.

The future live-call gate will bind at minimum:
- exact Entity/task/writer;
- provider OpenAI;
- one exact already-entitled model, default minimal candidate Luna;
- D0 synthetic input;
- one call;
- retries=0;
- fallback=none;
- no tools;
- bounded output;
- restricted project credential reference without exposing its value;
- requester Entity review;
- project acceptance remains separate.

## What this decision does NOT authorize

- any live OpenAI call;
- any Anthropic live call;
- credential value disclosure;
- credential read/use during preparation;
- billing/account mutation;
- production deployment;
- Project Sources changes;
- provider authority over Entity/project decisions.

## If not approved

Booster r0.2 remains a verified replay-only capability and no live-path preparation begins.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED
