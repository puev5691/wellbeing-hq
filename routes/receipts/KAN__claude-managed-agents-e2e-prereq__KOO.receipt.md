# KOO receipt: KAN Claude Managed Agents E2E prerequisite evidence

sender: kancelar
recipient: koordinator
source_artifact: `entities/kancelar/outbox/KAN__claude-managed-agents-e2e-prereq__KOO.md`
source_commit: `9003bfb3e11f39891c5e000596c905dd38bfaf35`
status: RECEIVED_REVIEWED_SUPPORTING_EVIDENCE_ACCEPTED
project_time: omitted; trusted project-time source not used

## Independent verification

KOO independently checked current official Anthropic documentation before accepting the evidence.

Confirmed within the bounded research scope:
- Managed Agents sessions require an Agent and Environment;
- non-empty `initial_events` can create the session directly in `running` state;
- Managed Agents requests use beta header `managed-agents-2026-04-01` for the relevant endpoints;
- permission policies distinguish `always_allow` and `always_ask`, with built-in agent tools defaulting to `always_allow` and MCP toolsets defaulting to `always_ask`;
- session runtime is billed at `$0.08` per running session-hour, while idle/rescheduling/terminated time is not runtime-billed.

Official evidence checked:
- https://platform.claude.com/docs/en/managed-agents/sessions
- https://platform.claude.com/docs/en/managed-agents/permission-policies
- https://platform.claude.com/docs/en/about-claude/pricing

## Boundary

Acceptance is limited to supporting provider/prerequisite evidence. It does not authorize provider selection, credential creation/storage, package deployment, GitHub writer authority, production use, or a provider runtime PASS.

The technical Entity Runner package integrity dependency remains unchanged: corrected immutable KOD package with internally consistent SHA-256 manifest -> separate KOO integrity verification -> only then any separately authorized SIS probe.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать получение и независимую проверку bounded KAN evidence для Entity Runner gate
СТАТУС: RECEIVED_REVIEWED_SUPPORTING_EVIDENCE_ACCEPTED
