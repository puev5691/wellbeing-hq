# KOO → SIS: bind durable OpenAI secret reference r0.1

status: TASK
execution_mode: BOUNDED_INFRASTRUCTURE_BINDING
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary.

## OPERATOR authority

Decision:
`AUTHORIZE_OPENAI_DURABLE_SECRETREF_BIND_R01`

Decision record:
`entities/koordinator/current/KOO__openai-durable-secretref-r01-decision.md`

decision commit:
`0ce2142e9a19e03829e37a1c8cf2a89c869b0540`

## Exact target

Canonical reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

Host:
`ruvds-xnqc6`

Storage mechanism:
`systemd-creds`

Credential object name:
`openai-wellbeing-entity-boosters-restricted`

Existing runtime lineage:
`/home/pev5691/openai-d0-runtime-r01`

## Required action

1. Freshly reconcile the host/runtime state and confirm `systemd-creds` is available.
2. Prepare the exact local binding command/procedure for the canonical reference and object name.
3. Require OPERATOR to enter the existing restricted OpenAI project credential interactively through a no-echo TTY prompt on the host.
4. Do not receive, print, return, log, hash or otherwise inspect the entered value.
5. Do not pass the value in command arguments or write it to plaintext temporary files.
6. Create the durable encrypted object using the authorized systemd-creds mechanism.
7. Establish the exact runtime mapping:
`secretref:openai:wellbeing-entity-boosters-restricted`
→ `openai-wellbeing-entity-boosters-restricted`.
8. Verify metadata/reference mapping only after binding.
9. Verify no plaintext credential value appears in project files, logs, shell history or task artifacts.
10. Do not make any provider call.

## Stop conditions

Stop with exact blocker if:
- host/runtime differs materially from verified state;
- `systemd-creds` is unavailable or unsuitable;
- binding would require exposing the credential value to ChatGPT/GitHub/logs;
- binding would require credential replacement/rotation;
- metadata-only verification cannot prove the exact mapping.

Do not improvise another storage mechanism without new authority.

## Forbidden

- OpenAI/provider call;
- credential rotation/replacement;
- account/billing mutation;
- production deployment;
- automation beyond this exact binding operation;
- Project Sources changes;
- project acceptance;
- LIVE_EXECUTION_AUTHORITY.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_DURABLE_SECRETREF_BOUND_R01`

or

`BLOCKED_SIS_OPENAI_DURABLE_SECRETREF_BIND_R01: <exact blocker>`

or exact FAIL.

Human-facing result must say:
- whether the canonical reference was successfully bound;
- whether metadata-only verification passed;
- exact canonical reference identifier;
- credential value exposure/read = 0 by SIS;
- provider calls = 0;
- whether KOO may now open the separate one-call D0 live decision gate.

Address terminal result to KOO.
Stop after terminal result.