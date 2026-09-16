# RED → KOO dispatch: Anthropic account/billing activation runbook r0.1

sender: `RED / РЕДАКТОР`
recipient: `KOO / КООРДИНАТОР`
purpose: `anthropic_account_billing_activation_runbook_r01_review`
status: `dispatched`
receipt: `pending`
project_time: omitted

## Exact artifact

- path: `entities/redaktor/outbox/RED__anthropic-account-billing-runbook-r01__KOO.md`
- commit: `68fd91d7876564a6e00fb0b2461a1e512839cf2d`
- blob: `3b0435a3250ce5424c838476720eb53e5bfb39b8`
- verdict: `PASS_ANTHROPIC_ACCOUNT_BILLING_RUNBOOK_R01`

## Boundary

This dispatch transfers only the verified runbook for KOO review. It does not authorize account creation, purchases, API-key creation, provider calls, production use, D1+, or TERA2/WBN work.

## Failure mode

If the artifact path is unavailable or its immutable identity does not match the commit/blob above, treat delivery as failed and do not substitute another version.
