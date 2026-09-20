# KOO → SIS: establish executable canonical OpenAI secretref resolver path r0.1

status: TASK
execution_mode: BOUNDED_INFRASTRUCTURE_RESOLVER_PATH
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact causal blocker

KOD terminal blocker:
`entities/koder/outbox/KOD__openai-entity-booster-d0-live-r01-blocker__KOO.md`

commit:
`dc87be84e0ea7ab136745b6d26da4e25da671a14`

blob:
`b42fb0862066f2fa82ccf324888b57b5f308f3a3`

status:
`BLOCKED_KOD_OPENAI_ENTITY_BOOSTER_D0_LIVE_R01: CANONICAL_SECRETREF_RESOLVER_NOT_EXECUTABLE_IN_AVAILABLE_KOD_RUNTIME`

Verified from blocker:
- exact task/writer/provider/model/bounds matched;
- canonical secretref metadata matched;
- durable one-shot claim count = 0;
- provider calls = 0;
- credential value reads = 0;
- old TTY injection was not substituted.

## Exact canonical reference

`secretref:openai:wellbeing-entity-boosters-restricted`

Verified store/object:
- store: `systemd-creds`;
- host: `ruvds-xnqc6`;
- object: `openai-wellbeing-entity-boosters-restricted`;
- encrypted object path: `/etc/credstore.encrypted/openai-wellbeing-entity-boosters-restricted.cred`.

Do not change the canonical reference or object identity.

## Goal

Create or prove one executable resolver execution path on `ruvds-xnqc6` that lets the bounded live worker obtain the already-bound canonical systemd credential through an approved runtime mechanism, without exposing the credential value to KOD/chat/GitHub/logs and without any provider call.

## Required work

1. Freshly inspect current host/runtime/service state.
2. Determine the smallest supported systemd execution mechanism that can consume the existing encrypted credential object and expose it only to the exact child process/runtime that needs it.
3. Prefer an established systemd credential mechanism such as `LoadCredentialEncrypted=` or equivalent exact systemd facility if suitable.
4. Do not decrypt/read/print/hash/return the credential value during verification.
5. Build only the minimum resolver path needed for later KOD invocation.
6. Ensure the resolver path binds the exact canonical secretref to the exact existing encrypted object.
7. Ensure the child runtime receives the credential through the systemd credential facility or another approved reference-based mechanism, not through the historical interactive TTY injection.
8. Verify executable accessibility under the intended KOD-triggered invocation boundary without performing a provider call.
9. Verify fail-closed behavior when:
   - secretref mismatches;
   - object is missing;
   - resolver mapping mismatches;
   - caller/task/writer metadata expected by the bounded path is absent or wrong;
   - runtime lacks required privilege/capability.
10. Produce metadata-only evidence of the resolver path and execution boundary.

## One-shot authority state

The previous one-call OPERATOR authority must NOT be reused automatically.
KOD reported claim count = 0, but the original activation-session expiry must be treated as ended unless a later KOO reconciliation explicitly reauthorizes execution.

This SIS task grants no provider call authority.

## Security caveat

The systemd host credential key remains not located on encrypted media.
Do not claim full-disk/host-key compromise protection.

## Forbidden

- OpenAI/provider call;
- reading/printing/exporting/hash-comparing credential value;
- canonical secretref change;
- credential rotation/replacement;
- provider/model task mutation;
- billing/account mutation;
- project acceptance;
- production deployment beyond the minimum resolver-path installation/config needed for this bounded verification;
- fallback to legacy TTY injection;
- new live-call authority.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_CANONICAL_SECRETREF_RESOLVER_PATH_R01_READY`

or

`BLOCKED_SIS_OPENAI_CANONICAL_SECRETREF_RESOLVER_PATH_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- whether an executable canonical resolver path now exists;
- exact mechanism used;
- whether KOD can invoke the bounded path without elevated manual intervention;
- credential value reads/exposure = 0;
- provider calls = 0;
- whether KOO may now reconsider a fresh one-shot live authority gate.

Address terminal result to KOO.
Stop after terminal result.