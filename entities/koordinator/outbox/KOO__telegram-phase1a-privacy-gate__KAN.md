# KOO → KAN: Telegram Media Gateway Phase 1A privacy gate

status: TASK
scope: BOUNDED_PRIVACY_RETENTION_DECISION
production: no

## Basis

KOD Phase 1A result:
`entities/koder/outbox/KOD__telegram-media-phase1a-result__KOO.md`
commit: `f3223860db28b56e435a25523ef500ec032be386`

Immutable candidate package:
`entities/koder/outbox/telegram-media-phase1a-v01/`
commit: `05617ea042613af51d10a78f456a28fe78e2ea0c`

KOO receipt/review:
`routes/receipts/KOD__telegram-media-phase1a-result__KOO.receipt.md`

## Current implementation boundary

The candidate currently:
- defaults privacy mode to `discard_identity`;
- permits only `discard_identity` or `aggregate_only`;
- does not persist/export audience identity or raw comment text in its bounded comment path;
- exports aggregate comment/reaction/member-count fields only;
- marks privacy policy `fail_closed_pending_KAN`;
- makes no live Telegram call and uses no real credential.

## Required KAN decision

Review only the audience-data/privacy/retention boundary needed before any Phase 1B sandbox integration.

Return an explicit bounded decision covering:
1. whether `discard_identity` is acceptable for first sandbox integration;
2. whether `aggregate_only` is acceptable, and under what exact conditions if conditional;
3. whether raw comment text may be processed transiently in memory while remaining unpersisted/unexported;
4. whether aggregate comment/reaction/member-count values may be retained and for what bounded purpose;
5. any exact deletion/retention/minimization requirements;
6. any exact blocker that must be corrected in code before a live sandbox send.

Do not authorize publication, production deployment, Telegram administration, credentials, or expanded writer grants.

Return result to KOO through normal outbox/inbox/dispatch chain.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: получить обязательное профильное KAN-решение по privacy/retention перед Phase 1B sandbox integration
