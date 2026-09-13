# KOO — multi-model worker gateway pilot specification v0.1

status: PILOT_SPEC__LOCAL_SYNTHETIC_ONLY
external_provider_calls: forbidden
project_data_transfer: forbidden
credentials: forbidden
production: no
project_time: omitted; trusted project-time source not used

## Purpose

Test the project-side mechanics of a future multi-model worker gateway before any real provider is connected.

Basis:
- KOO research: `entities/koordinator/outbox/KOO__ai-capacity-expansion-study-v01__OPERATOR.md` commit `603e9192bba447dd6174825cbcddbac79d35f035`;
- KAN boundary: `entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md` commit `05ce3d065e86265de45bc4df17a931bb78ffc29d`.

## Pilot data class

Only `D0_SYNTHETIC`.

No real project artifact contents, private repository data, user data, infrastructure data, credentials, unreleased governance text or third-party restricted material may be placed in mock model context.

## Required architecture

`task envelope → policy guard → router → fake provider adapter(s) → author result → independent fake verifier adapter → reconciliation result → immutable provenance envelope`.

Required mock provider IDs:
- `mock-provider-a/mock-model-author-v1`;
- `mock-provider-b/mock-model-verifier-v1`.

They must be deterministic local stubs, not network clients.

## Task envelope

Minimum fields:
- task_id;
- task_class;
- data_class;
- input_locator(s);
- synthetic_payload_hash;
- requested_role = author|verifier;
- allowed_provider/model set;
- max_cost_usd = 0 for r01;
- external_tools_allowed = false;
- project_mutation_allowed = false.

## Policy guard

Must fail closed if:
- data_class != D0_SYNTHETIC;
- provider/model outside allowlist;
- any credential field/value is supplied;
- external tool/network mode requested;
- project mutation requested;
- automatic fallback outside exact allowlist requested.

## Provenance result

Record:
- task_id;
- provider/model identity;
- adapter identity/version;
- author/verifier role;
- input locator list;
- synthetic payload hash;
- output hash;
- policy decision;
- verifier agreement/disagreement;
- final candidate status;
- cost = 0;
- external_network_used = false.

No output may directly mutate Project Sources/current state. Results are candidate artifacts for KOO review.

## Test cases

At minimum:
1. valid D0 author → verifier PASS;
2. verifier disagreement retained, not overwritten;
3. D2/D5/D6/D7 request fails closed;
4. credential-like field/value fails closed;
5. unknown provider/model fails closed;
6. fallback request fails closed;
7. external tool/network request fails closed;
8. provenance complete and deterministic;
9. outputs cannot mark themselves accepted/current/canon;
10. identical input + same mock adapter version yields reproducible result identity where designed.

## Output expected from KOD

Package:
`entities/koder/outbox/multi-model-gateway-mock-r01/`

Result:
`entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`

No provider API, SDK, key, purchase, account connection or real network request is allowed.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать KOD exact safe implementation target for a local D0 synthetic multi-model gateway mock
СТАТУС: pilot_spec_local_synthetic_only
