# KOO → KAN: multi-model worker gateway privacy/authority boundary v0.1

status: TASKED_BOUNDED_POLICY_REVIEW
implementation: no
provider_connection: no
credentials: no
external_data_transfer: no
purchase_authorization: no
project_time: omitted; trusted project-time source not used

## Purpose

The OPERATOR has directed exploration of increased compute and multiple AI providers/models to reduce queue latency and allow safe parallel work.

KOO research basis:

`entities/koordinator/outbox/KOO__ai-capacity-expansion-study-v01__OPERATOR.md`
commit: `603e9192bba447dd6174825cbcddbac79d35f035`
blob: `6427f6ff0d5e8ae6e073db34ca4c735f33aaab7e`

This study is decision support only, not active policy and not authorization to connect providers.

## KAN task

Produce a bounded privacy/public/legal/authority boundary for a future multi-model worker gateway.

Do **not** choose a final provider, buy a plan, create API credentials, transmit project data externally, or implement the gateway.

Define at minimum:

1. **Data sensitivity classes**
   - public/project-public;
   - internal operational;
   - credentials/secrets;
   - personal/sensitive personal data;
   - security-sensitive infrastructure;
   - unreleased/candidate governance material;
   - any other class KAN can justify from active project rules.

2. **Provider eligibility rules**
   For each data class, state whether external model/provider processing is:
   - allowed;
   - allowed only with named conditions;
   - blocked;
   - unknown pending evidence.

3. **Minimum provider evidence before use**
   Examples to assess:
   - retention/training controls;
   - data residency where relevant;
   - zero-retention/no-training mode;
   - subprocessors/provider routing visibility;
   - account/API boundary;
   - deletion/retention semantics;
   - logging/telemetry exposure;
   - contractual vs marketing claims;
   - ability to pin provider/model where routing services are used.

4. **Router/gateway boundary**
   Compare policy implications of:
   - direct provider API;
   - third-party router/aggregator;
   - self-hosted gateway/router.
   Do not assume one is permitted merely because it is technically convenient.

5. **Author/verifier separation**
   Define privacy/authority conditions for:
   `AUTHOR(provider/model A) → VERIFIER(provider/model B) → KOO acceptance`.

6. **Artifact/provenance requirements**
   Specify what every external-model result must record without leaking secrets:
   - task class;
   - provider/model identifier/version when available;
   - exact input artifact locators, not necessarily full sensitive input content;
   - data sensitivity class;
   - output/result identity;
   - verifier identity;
   - acceptance/rejection;
   - cost/usage metadata if appropriate;
   - provider-policy evidence locator.

7. **Hard prohibitions**
   Explicitly identify categories that may never be sent to an external provider without a later separate OPERATOR decision and appropriate technical controls.

8. **Pilot boundary**
   Recommend a safe first pilot dataset/task class using only material permissible under the proposed rules.

9. **Unknowns**
   Mark provider-specific claims as UNKNOWN unless supported by fresh official evidence. This task may define the evidence required; it must not manufacture current provider policy from stale assumptions.

## Output

Primary result:

`entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`

Return through Exchange Gate:

- `routes/dispatch/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`
- `entities/koordinator/inbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`
- sender registry `registry/by-sender/kancelar.jsonl`

Verdict should distinguish:
- `PILOT_POLICY_BOUNDARY_READY`, or
- exact blockers/unknown evidence required before even a bounded pilot.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: определить безопасные границы использования нескольких внешних ИИ-провайдеров до подключения API и передачи проектных данных
СТАТУС: tasked_bounded_policy_review
