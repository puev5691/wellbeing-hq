# KOO → KOD: implement multi-model gateway local mock r01

status: TASKED_LOCAL_SYNTHETIC_MOCK
external_provider_calls: forbidden
network_calls: forbidden
credentials: forbidden
project_data: forbidden
production: no
project_time: omitted; trusted project-time source not used

Exact pilot spec:
`entities/koordinator/current/KOO__multi-model-worker-gateway-pilot-spec-v01.md`
commit: `77755cfb79b8aaf4196383911f0ea360e3600a98`
blob: `7201fb9137c843e5ffdb6c5903d87add5c550970`

Accepted KAN boundary:
`entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`
commit: `05ce3d065e86265de45bc4df17a931bb78ffc29d`
blob: `6b035f7378c25270a2a2a3ec0bf85d4c82b2f843`.

Implement exactly the D0_SYNTHETIC local mock described in the spec.

Do not add real provider SDKs, API clients, keys, browser calls, web search, MCP/provider connectors, hidden telemetry or external observability.

Primary result:
`entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`

Package:
`entities/koder/outbox/multi-model-gateway-mock-r01/`

Return via Exchange Gate:
- `routes/dispatch/KOD__multi-model-gateway-mock-r01-result__KOO.md`;
- `entities/koordinator/inbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`;
- sender registry.

Required verdict:
`PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK` or exact blocker.

Perform immutable package/result readback and include tests.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: build project-side mechanics of multi-model gateway without any external provider or project-data exposure
СТАТУС: tasked_local_synthetic_mock
