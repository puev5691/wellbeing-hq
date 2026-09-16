# KOO → RED: OpenAI account/billing/API activation runbook r0.1

status: `READY_FOR_RED_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Priority

Top-priority lane:
OpenAI-first coordination infrastructure → first bounded live call → measured routing by latency/cost/quality → Anthropic/Google adapters.

TERA2/WBN remains `PARKED_BACKGROUND`.

## Purpose

Prepare a short Russian-language OPERATOR runbook that closes the remaining external OpenAI gate before one bounded synthetic D0 live request.

Use current official OpenAI sources only.

## Required content

Confirm and explain compactly:
1. exact current path to enable API billing / credits / payment for an existing OpenAI account/project;
2. whether a minimum prepayment, balance, usage tier or other account gate currently applies;
3. exact current steps to create a project-scoped API key or service-account credential suitable for server use;
4. model entitlement/availability check for `gpt-5.6-luna` and, if relevant, `gpt-5.6-terra` / `gpt-5.6-sol`;
5. where current rate/usage limits are viewed;
6. what OPERATOR should verify before the first D0 call;
7. what must NOT be pasted into ChatGPT/GitHub/project files.

Distinguish:
- documented current fact;
- project recommendation;
- `UNVERIFIED` where official documentation does not support a point.

Do not broaden into general OpenAI product documentation.
Do not create accounts, keys, billing changes or live calls.

## Output

Main result:
`entities/redaktor/outbox/RED__openai-account-billing-activation-runbook-r01__KOO.md`

Expected verdict:
`PASS_OPENAI_ACCOUNT_BILLING_ACTIVATION_RUNBOOK_R01`

or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through current Exchange Gate.

## FAST_PATH

Target <=12 tool calls and <=8 source/GitHub reads.
One initial preflight, one short prewrite reconciliation.
Stop when enough current official evidence exists.

---
КТО: KOO
ДЛЯ ЧЕГО: закрыть операторский account/billing/key gate перед первым OpenAI D0 live call
СТАТУС: `ready_for_red_openai_account_billing_activation_runbook_r01`
