# KOO receipt: KAN Anthropic direct D0 readiness

source_artifact: `entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md`
source_commit: `c84565bec9f602f1e0da4808107a0abd52e18a4b`
result: `READY_WITH_EXACT_ACCOUNT_PREREQUISITES_ACCEPTED`

Accepted bounded findings:
- direct route: Claude API `POST /v1/messages`;
- first technical/cost candidate: `claude-sonnet-5`;
- first external data class remains `D0_SYNTHETIC` only;
- tools/search/files/MCP/Managed Agents/code execution remain OFF for the first live pilot;
- account-specific prerequisites remain unverified: Console organization, billing/credits, API key/auth path, tier/rate/spend limits, model access.

This receipt does not create account/key, buy credits, make a live call, authorize D1/D2+, or expose secrets.

next_gate:
- KOD prepares credential-free direct Anthropic adapter/pilot harness;
- OPERATOR separately prepares Claude Console account/billing/key facts through a secret-safe path;
- live call remains blocked until both gates are ready.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: принять KAN readiness и открыть безопасную техническую подготовку первого Anthropic D0 пилота
СТАТУС: accepted_ready_with_exact_account_prerequisites
