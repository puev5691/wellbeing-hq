# KOO → SIS: verify/bind OpenAI restricted credential reference r0.1

status: TASK
execution_mode: BOUNDED_INFRASTRUCTURE_REFERENCE_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight: `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## OPERATOR authority

Decision:
`AUTHORIZE_OPENAI_RESTRICTED_CREDENTIAL_REF_BIND_R01`

Decision record:
`entities/koordinator/current/KOO__openai-credential-ref-bind-r01-decision.md`

decision commit:
`a919db2fe8298eafba9ee134698be332674d26b8`.

## Purpose

Establish the exact active reference identifier of the already provisioned restricted OpenAI project credential, in the form:
`secretref:openai:<identifier>`.

The credential value itself must remain unread and undisclosed.

## Verified basis

SIS live-path preparation PASS:
`entities/sisadmin/outbox/SIS__openai-booster-live-path-prep-r01-independent-verify__KOO.md`
commit `5b5ee3bb76dbcc5ce7d8c1d7872ec553f557a47d`.

That verification established:
- the restricted OpenAI project credential exists outside project artifacts;
- the exact secret-reference identifier is the remaining external gate input;
- no live call is authorized.

## Required action

1. Reconcile the current runtime/secret-store configuration for the OpenAI booster path.
2. Identify the exact active reference name only.
3. Verify that the reference resolves to the already provisioned restricted project credential by metadata/reference-level checks that do not read or expose the secret value.
4. Do not print, copy, hash, compare, export, log or otherwise inspect the credential value.
5. If no exact reference currently exists, STOP with a blocker. Do not invent one and do not create/rebind a credential without separate authority.
6. Distinguish tool-history/test strings from actual runtime secret-reference configuration. Self-generated search history is not evidence.
7. Return the exact verified reference identifier only if independently supported.

## Forbidden

- credential value read/use/create;
- provider/OpenAI call;
- credential rotation/replacement;
- billing/account mutation;
- production deployment;
- Project Sources changes;
- automation;
- project acceptance.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_RESTRICTED_CREDENTIAL_REF_BOUND_R01`

or

`BLOCKED_SIS_OPENAI_RESTRICTED_CREDENTIAL_REF_BIND_R01: <exact blocker>`

or exact FAIL.

Human-facing result must say:
- whether an active exact secret reference exists;
- the exact reference identifier if PASS;
- how existence/identity was verified without reading the value;
- credential value reads = 0;
- provider calls = 0;
- whether KOO may now prepare the one-call D0 OPERATOR live gate.

Address terminal result to KOO.
Stop after terminal result.