# KOO → KOD: OpenAI Responses API D0 adapter/transport r0.1

status: `READY_FOR_KOD_EXECUTION`
scope: `D0_SYNTHETIC_ONLY`
live_api_call: `no`
real_api_key: `no`
billing_purchase: `no`
project_private_data: `no`
tools_search_files_computer_use: `no`
fallback: `no`
production: `no`

## Purpose

Prepare the OpenAI provider path for the existing provider-neutral multi-model/entity-runner architecture without making any live provider call. Reuse proven policy/provenance mechanics instead of building a second orchestration stack.

## Verified project basis

### Multi-model gateway mock

`entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`
verdict: `PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK`
blob: `2bbf4b1562e29eedb665eda383698ff8ca6d0064`.

Preserve its essential boundaries:
- strict D0 envelope;
- fail-closed policy guard;
- provider identity explicit;
- author/verifier/reconciliation separation;
- immutable provenance;
- no project acceptance manufactured by provider output.

### Anthropic adapter/transport as implementation reference only

`entities/koder/outbox/KOD__anthropic-direct-adapter-r01__KOO.md`
verdict: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`.

`entities/koder/outbox/KOD__anthropic-live-transport-r01__KOO.md`
verdict: `PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE`.

These are design/provenance references. Do not copy Anthropic-specific protocol assumptions into OpenAI without fresh official-document verification.

## Target provider contract

Provider: `OpenAI`.

Target API family: `Responses API`.

Expected endpoint for this candidate:
`POST https://api.openai.com/v1/responses`.

Pilot target model:
`gpt-5.6-luna`.

Credential reference only:
`OPENAI_API_KEY`.

Before implementation, verify the endpoint/model/request/usage contract against current official OpenAI developer documentation. If current official documentation conflicts materially with this task, do not silently rewrite the task. Return `BLOCKED_PROVIDER_DOC_DRIFT` with the exact conflicting evidence and the smallest proposed correction.

## Required candidate

Prepare one immutable credential-free, live-capable-but-default-deny OpenAI Responses adapter/transport package that:

1. accepts only `D0_SYNTHETIC` for r0.1;
2. stores no API key or secret value in source, tests, fixtures, logs, provenance or Git artifacts;
3. represents auth only by runtime secret reference `OPENAI_API_KEY`;
4. represents only the exact OpenAI endpoint/model approved by the verified contract;
5. has network execution disabled by default;
6. allows injected/mock HTTP execution for deterministic tests;
7. performs no actual OpenAI request in this task;
8. has no provider fallback;
9. has no tools, web search, file search, computer use, code execution or external project mutation;
10. parses and normalizes at minimum:
   - response ID;
   - model identity;
   - output text/content under the verified Responses schema;
   - response completion/status where available;
   - usage fields available from the verified response contract, including input/output token counts and any separately exposed cached/reasoning token detail without inventing absent fields;
11. handles at minimum auth failure, rate limit, provider 5xx, timeout/network error and malformed/mismatched response fail-closed;
12. records immutable provenance with provider/model/adapter version, request/response hashes, normalized usage, policy decision, D0 identity, external-network-used flag, tools/fallback/project-mutation flags and final result identity;
13. preserves provider output as candidate/evidence only and cannot self-declare project acceptance/current/canon state.

## Tests

Use deterministic mock/injected transport. Network must be guarded so tests cannot accidentally contact the provider.

Cover at minimum:
- valid D0 request/response;
- model mismatch;
- malformed usage/content;
- non-D0 reject before provider invocation;
- secret-like field/value rejection where applicable;
- tools/search/files/computer-use/fallback/project-mutation reject;
- auth/rate-limit/5xx/timeout handling;
- deterministic provenance/result identity for same fixture + adapter version;
- live execution remains default-deny;
- no actual network/provider calls occur during the suite.

Run compile/tests/checksums and publish tested bytes as one immutable package with exact commit/tree/blob identities and readback.

## Expected result

Return to KOO through Exchange Gate:
- `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`, or
- exact `BLOCKED_*` / `FAIL_*` with evidence.

For PASS include:
- official-document contract checked and the exact boundary used;
- immutable package identity;
- test evidence;
- exact future live-gate prerequisites;
- explicit confirmation: real API calls = 0, credentials = 0, billing changes = 0, project/private data sent = 0.

## Future gate, not authorized now

A later task may authorize exactly one D0 synthetic OpenAI live request after OPERATOR/account/billing/key readiness and a chosen Unix-host preflight. This task does not authorize that later call.

Do not start TERA2 root-profile or another KOD lane in this task.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: добавить OpenAI Responses provider path к уже существующей provider-neutral архитектуре без live credentials/network use
СТАТУС: `ready_for_kod_openai_d0_adapter_r01`
