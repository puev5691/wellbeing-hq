# КОО → КОДЕР: protected read-only Bot API bridge contract r0.1

status: TASK_AUTHORIZED_PENDING_MANUAL_ACTIVATION
scope: DOCUMENT_ONLY
project_time: omitted

## Authority
OPERATOR explicitly authorized:
AUTHORIZE_KOD_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_ONLY.
KOO routes exactly that documentary scope to KOD current-writer v0.5; this artifact and its publication do not establish KOD receipt, activation or processing_started.

KOO preflight HQ HEAD: 801fd04405a13dfc3ee6452c65cef2470ea62e78.
KOO writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md, blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd.
KOD writer to verify again at KOD activation: entities/koder/current/KOD__replacement-current-writer-v05.md, blob cf1c84f9df7c90509703e4885844d0cf871ff412.

## Inputs
1. SIS diagnostic:
puev5691/wellbeing-hq@b080637a3b7a58e4645b89ea030a06c34d888e28:
entities/sisadmin/outbox/SIS__telegram-direct-message-path-diagnostic-r01__KOO.md
blob 734146576f35942c6b584b898c83129521a7bc2a
terminal BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS.

2. KOO receipt/decision preparation:
puev5691/wellbeing-hq@771458166e75c481d44b7e03acd2a8d6fa950d16:
entities/koordinator/outbox/KOO__telegram-direct-message-diagnostic-reconciliation-r01__OPERATOR.md
blob b6d18738bbcf538b2b88a85a48b0d9112f269399.

3. KOD read-only fit-gap:
puev5691/wellbeing-hq@0ece5979ab5e0fbab485eb1491a4f51ce5bee105:
entities/koder/outbox/KOD__telegram-channel-direct-message-fitgap-r01__KOO.md
blob cb6a41bb1cc577835e6ca036d264a287afa6b353.

## Deliverable
Prepare one non-live design candidate for a protected credential bridge accessible to the verified SIS identity on the verified host ruvds-xnqc6. Design exactly two bounded operations:
- getWebhookInfo for bot @WBNP_Media_Bot, bot_id=8866633840, with no arbitrary target; output only sanitized webhook-present/configuration summary, allowed_updates, pending and sanitized error counters/status, explicitly excluding token-bearing URL or content.
- getChatMember for fixed channel_id=-1003606547591, user_id=8866633840; output only membership/admin state and can_manage_direct_messages when the field exists.

Describe: exact executable/service identity binding and trusted provenance of bot/channel IDs; where the existing systemd protected credential may be consumed without ever returning/logging it; fixed command/argument allowlist and privilege boundary; request/time budget and zero-retry default; TLS/HTTP validation; JSON output schema/redaction; audit without visitor content; safe failure when token/rights/identity/network is absent, endpoint errors, privilege expansion, command injection or symlink/path replacement; negative matrix and independent SIS security-review acceptance criteria.

Show a minimal deployment and rollback proposal as DESIGN_ONLY for later decision, not an instruction to execute it. Distinguish direct-message channel rights from private-chat /start; webhook configuration is not update receipt or bot response. The currently installed Phase 1B service remains disabled/inactive with --transport fake, listener absent. Any future real responder requires additional separate gates.

## Boundaries
No source-code implementation or executable patch. No host access, file/service/sudoers change, credentials or secrets access, Bot API invocation, getUpdates, visitor data, message send, provider call, webhook or admin-right mutation, runtime activation, Project Source/canon change, or memory-layering attempt 3. Historical PROMPT not replay.

On activation, KOD first loads approved Project Sources, verifies current-writer, exact task authority, supersession and competing result. Return one candidate or exact BLOCKED; publish, immutable readback and address KOO. If continuation needs a new Entity-chat, include one complete manual activation handoff; do not treat inbox/dispatch as processing_started.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
