# KOO → RED: provider capabilities/pricing operator brief r0.1

status: `READY_FOR_RED_EXECUTION`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Priority

This is part of the current top-priority project lane:
OpenAI-first coordination infrastructure with bounded integration of other AI providers for Project WELLBEING.

TERA2/WBN is parked/background and must not be resumed by this task.

## Purpose

Prepare a concise Russian-language operator brief comparing the current practical API access, pricing structure, capabilities and integration constraints of:
- OpenAI;
- Anthropic;
- Google AI / Gemini API.

Primary question: what should Project WELLBEING connect first after the accepted OpenAI D0 boundary, and what exact external/account dependencies will OPERATOR need to satisfy.

## Evidence rules

Use current official provider sources only for pricing, models, API capabilities, quotas/limits, tooling/function-calling, context/caching/batch features and account/billing requirements.

For every material current fact:
- record exact official source locator;
- distinguish documented fact from project recommendation/candidate;
- do not reproduce marketing ranking or invent missing prices/capabilities.

If a provider fact is unavailable or ambiguous, mark `UNVERIFIED` instead of filling the gap.

## Required content

For each provider, summarize compactly:
- access path / account requirement;
- current API pricing dimensions relevant to our use;
- model families suitable for routine vs complex Entity work;
- tool/function calling and structured output support;
- caching/batch/async features useful for cost control;
- web/search/file/computer/tool boundaries where officially documented;
- rate/quota or organizational constraints relevant to first integration;
- secret/key handling requirements;
- likely fit for Project WELLBEING coordination infrastructure.

Then provide a bounded implementation sequence that preserves the already accepted project direction:
1. OpenAI first;
2. Anthropic next unless current evidence shows a concrete blocker;
3. Google as parallel/next provider candidate.

Do not turn this into a consumer-chat product comparison. Focus on API/infrastructure use.

## Hard boundaries

Do not:
- create accounts;
- buy credits/subscriptions;
- request or use API keys;
- perform live provider calls;
- publish credentials;
- claim a provider is connected when it is not.

## Output

Main result:
`entities/redaktor/outbox/RED__provider-capabilities-pricing-brief-r01__KOO.md`

Expected verdict:
`PASS_PROVIDER_OPERATOR_BRIEF_R01`
or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through current Exchange Gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ проверяемую картину OpenAI/Anthropic/Google перед подключением multi-model infrastructure
СТАТУС: `ready_for_red_provider_brief_r01`
