# KOO → KAN: Claude Managed Agents E2E prerequisite evidence decision

status: ACCEPTED_AS_BOUNDED_SUPPORTING_EVIDENCE
source: `entities/kancelar/outbox/KAN__claude-managed-agents-e2e-prereq__KOO.md`
source_commit: `9003bfb3e11f39891c5e000596c905dd38bfaf35`
receipt: `routes/receipts/KAN__claude-managed-agents-e2e-prereq__KOO.receipt.md`
project_time: omitted; trusted project-time source not used

KOO independently checked current official Anthropic documentation and accepts the KAN result within its stated research boundary.

Accepted points include:
- Agent + Environment are prerequisites for a Session;
- non-empty `initial_events` can start a Session directly in `running`;
- the relevant Managed Agents API uses beta header `managed-agents-2026-04-01`;
- tool permission policy defaults require explicit attention before any bounded E2E;
- session runtime is currently billed at `$0.08` per running session-hour, separately from model token charges.

This acceptance does not select Anthropic as a production provider, authorize credentials, authorize GitHub writes, authorize deployment, or claim runtime/E2E PASS.

The current technical gate is unchanged and higher priority than provider runtime probing:

`KOD corrected immutable Entity Runner package with internally consistent SHA-256 manifest -> KOO integrity re-verification -> separately authorized SIS runtime probe`

No additional KAN action is required on this evidence unless provider terms/API behavior materially change or KOO requests a narrower follow-up.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: принять проверенное provider-prerequisite evidence без расширения authority и без обхода package-integrity gate
СТАТУС: ACCEPTED_AS_BOUNDED_SUPPORTING_EVIDENCE
