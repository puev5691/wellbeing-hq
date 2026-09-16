# KOO → SIS: OpenAI D0 Unix-host preflight r0.1

status: `READY_FOR_SIS_EXECUTION`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_api_call: `no`
api_key: `no`
billing_change: `no`
privileged_mutation: `no`

## Purpose

Prepare one Unix host for a future bounded OpenAI D0 live gate without using credentials or contacting the OpenAI API with an authenticated request.

## Accepted basis

KOD terminal result:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`
verdict `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`.

Exact immutable package:
`entities/koder/outbox/openai-responses-d0-adapter-r01/`
commit `4fd2c0bb930e81fd5c9e023f674131f086f0e814`
tree `79e0701df2582f412a3f7358b3702a26b5ed8763`.

## Target

Preferred host for this bounded preflight: `ruvds-xnqc6`.

If this host has a concrete conflict or unsuitable boundary, stop and return exact evidence. Do not silently choose another host.

## Required actions

1. Fresh Resume-First GitHub preflight.
2. Confirm SIS current-writer/authority state and exact task identity.
3. On `ruvds-xnqc6`, perform read-only/non-privileged checks only:
   - OS/kernel;
   - Python version;
   - available disk/home space;
   - DNS resolution for `api.openai.com`;
   - outbound HTTPS/TLS reachability to `https://api.openai.com/v1/models` without credentials;
   - whether Python stdlib needed by the accepted package is available;
   - whether an isolated user-owned runtime directory can be created without sudo.
4. A provider response such as unauthenticated `401` may be recorded as evidence that DNS/TLS/network path reached the provider, but it is not account/auth readiness.
5. Do not install packages unless the exact package already requires them and installation is possible without privilege. If privilege or package installation is needed, stop with exact blocker.
6. Do not create or request `OPENAI_API_KEY`.
7. Do not perform a live authenticated OpenAI request.
8. Return a compact result with host suitability, exact blockers, and the smallest next dependency for the future live gate.

## Telemetry / observability

Record compactly if available from actual project evidence:
- task dispatch/activation boundary identity;
- first profile work commit/event;
- terminal result commit/event;
- tool calls;
- GitHub reads/writes;
- retries;
- operator re-wake count if known.

Do not invent timestamps or latency values. Git commit timestamps may be used only where they correspond to actual lifecycle events.

## Expected result

- `PASS_SIS_OPENAI_D0_HOST_PREFLIGHT_R01`, or
- exact `BLOCKED_*` / `FAIL_*` with evidence.

PASS does not authorize billing, API-key creation, authenticated provider call or production deployment.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить Unix-host boundary до отдельного OpenAI live D0 gate
СТАТУС: `ready_for_sis_openai_d0_host_preflight_r01`
