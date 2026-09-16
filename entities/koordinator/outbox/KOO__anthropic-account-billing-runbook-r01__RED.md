# KOO → RED: Anthropic account/billing activation runbook r0.1

status: `READY_FOR_RED_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Purpose
Prepare a concise Russian-language OPERATOR runbook for opening the Anthropic API account/billing/credential gate after OpenAI-first path, using current official Anthropic sources only.

## Required content
- account/workspace/service-account/API-key creation path;
- current billing/credit/prepaid requirements and minimums if documented;
- current usage/rate tier path;
- first recommended model entitlement checks for routine/main/complex roles;
- where to verify model availability/limits;
- secret handling rules;
- exact checklist before first bounded synthetic Anthropic API call;
- clearly mark `UNVERIFIED` where official evidence is absent/ambiguous.

Distinguish documented facts from WELLBEING recommendations.
Do not compare consumer chat products.

## FAST_PATH
Target <=12 tool calls and <=8 source/GitHub reads. One initial preflight, one short prewrite reconciliation. Stop when enough official evidence exists.

## Hard boundaries
Do not create accounts. Do not buy credits. Do not request/read/create API keys. Do not perform provider calls. Do not publish credentials. Do not resume TERA2/WBN.

## Output
`entities/redaktor/outbox/RED__anthropic-account-billing-runbook-r01__KOO.md`

Expected terminal:
`PASS_ANTHROPIC_ACCOUNT_BILLING_RUNBOOK_R01`
or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
