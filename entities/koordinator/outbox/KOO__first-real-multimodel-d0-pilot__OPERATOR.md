# KOO → OPERATOR: first real multi-model D0 provider pilot decision

status: `WAITING_OPERATOR_EXTERNAL_PROVIDER_PILOT_DECISION`
project_time: omitted; trusted project-time source not used

## Verified prerequisites

1. Local gateway mechanics:
`entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`
commit `cb2f21c3ee639fc58a04dfb043826d1ee9581be4`
result `PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK`
tests 18/18 PASS.

2. Provider evidence:
`entities/kancelar/outbox/KAN__multi-model-first-provider-evidence-matrix__KOO.md`
commit `4ef395dfbdc2dee4dbb0e5f2472d5e5acf597ddf`.

Bounded findings:
- Anthropic direct commercial/API: eligible for D0/D1 under exact route conditions;
- Google Cloud Vertex/Gemini direct: eligible for D0/D1 under exact route conditions;
- OpenRouter: conditional; not preferred for first D1 pilot because router + upstream policy/routing boundary is larger.

## Proposed first external pilot

Data class: `D0_SYNTHETIC` only.
No project/private content.
No D2+.
No tools/search/connectors.
No fallback.
One exact direct provider + exact model/endpoint.
Author/verifier separation may be tested later; first live external call may validate only one provider route if desired.

## Required OPERATOR decision

Choose exactly one:

- `AUTHORIZE_ANTHROPIC_D0_PILOT`
- `AUTHORIZE_GOOGLE_D0_PILOT`
- `HOLD_EXTERNAL_PROVIDER_PILOT`

OpenRouter is not proposed as the first real route.

Any authorization is only for preparing/connecting the exact D0 pilot path. It does not authorize D1/D2+, production use, arbitrary connectors, project-data transfer, or subscription/purchase beyond the separately approved account/tariff action.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вынести наружу единственное решение, которое KOD/KAN не вправе принять сами
СТАТУС: waiting_operator_external_provider_pilot_decision
