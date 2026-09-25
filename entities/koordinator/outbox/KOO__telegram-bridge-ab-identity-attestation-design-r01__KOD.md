# КОО → КОДЕР: A+B identity profile and separate attestation contract r0.1

status: TASK_AUTHORIZED_PENDING_MANUAL_ACTIVATION
scope: DOCUMENT_ONLY / NON_LIVE_DESIGN
project_time: omitted

## Purpose

ОПЕРАТОР выбрал A+B как направление проектирования защищённого read-only Bot API bridge. Подготовь конкретный non-live identity profile и отдельный attestation contract, чтобы стало проверяемо, что защищённый credential slot относится к intended bot, а вызовы двух диагностических методов не могут быть перенаправлены на чужие bot/channel identities. Не создавай код или credential bridge этой задачей.

## Exact authority and inputs

ОПЕРАТОР прямо ответил:
ИДЕНТИЧНОСТЬ: A+B
КОД: KOD
СЕКРЕТ_И_ХОСТ: SIS
НЕЗАВИСИМАЯ_БЕЗОПАСНОСТЬ: SHD
ЭКСПЛУАТАЦИОННАЯ_ПРИЁМКА: OPERATOR
СТАТУС: DESIGN_ONLY.

KOO immutable decision: puev5691/wellbeing-hq@91f4dd2452a082ac9025fe4211407dce47dd4629:entities/koordinator/outbox/KOO__telegram-readonly-bridge-ab-ownership-design-choice-r01__OPERATOR.md; blob b028b023c5892483eea9118489968eff848ddf21.

KOD predecessor contract: puev5691/wellbeing-hq@bcfe46af1be40b347bc1e8d829446d999e61c2de:entities/koder/outbox/KOD__telegram-readonly-bot-api-bridge-r01-design__KOO.md; blob cdcfd65fc18ce6d6124c5710f3de27febf35ada7.

SIS independent documentary review: puev5691/wellbeing-hq@124cc535f562e53570690a8b93ae18b0d77440fe:entities/sisadmin/outbox/SIS__telegram-readonly-bot-api-bridge-r01-independent-review__KOO.md; blob 6d8228cca029c67797e7d417fb13847ebbe5cc44; terminal PASS_SIS_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_REVIEW_WITH_BOUNDARIES.

Prior SIS blocker: puev5691/wellbeing-hq@b080637a3b7a58e4645b89ea030a06c34d888e28:entities/sisadmin/outbox/SIS__telegram-direct-message-path-diagnostic-r01__KOO.md; blob 734146576f35942c6b584b898c83129521a7bc2a; remains active.

At KOO preflight HQ HEAD d0c8b0186680eae7197152ebd6d2bf62894f8c46, KOO v0.8 writer blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd and KOD v0.5 writer blob cf1c84f9df7c90509703e4885844d0cf871ff412 matched. Six approved Project Sources matched current attachments; roles v2.4 active, PRV v2.5 staged pending UI verification. KOD must do own fresh preflight and writer/supersession check.

## Deliverable: exact non-live A+B design

1. Define a proposed immutable supervisor-owned A profile schema with bot ID 8866633840, username @WBNP_Media_Bot, channel ID -1003606547591, protected credential-slot reference without token, provenance locators and exact blobs, issuer, approval/effectivity, version/generation, expiry/revocation, supersession, independent readback and conflict/fail-closed policy. Do not treat these historical project IDs as independently proven live bindings.
2. Define B as a SEPARATE attestation contract and possible evidence methods, each with exact operation/authority boundary, fixed target and sanitized evidence envelope. Clearly distinguish what can be derived from existing immutable provisioning records with no host/token/API use from what would require a separately authorized future protected one-time Bot API identity query or equivalent independent proof. Do not invoke getMe or other methods now and do not add them to the existing two-method diagnostic bridge.
3. Specify how supervisor verifies profile, immutable attestation evidence, credential-slot binding, caller/host/executable identity and operation-specific authority before any future protected credential injection. Mark unresolved supervisor implementation/issuer/trust root and secure systemd credential transfer UNKNOWN.
4. Include positive and negative documentary cases for wrong bot/token, wrong channel, username changes, profile/path/symlink/Git substitution, stale/revoked attestation, slot rotation, split evidence, unknown issuer, missing dependency and leaked token-bearing URL. For each define fail-closed and no probe of arbitrary bot/channel. No executed test claim.
5. Describe handoff boundaries: KOD authors future code under separate authority; SIS owns future host/credential/deployment design under separate authority; SHD is independent technical reviewer only after exact task and verified competence; OPERATOR accepts operational outcome only after gates. No automatic role/privilege grant.
6. Provide exact list of remaining operator decisions/evidence, including when B attestation operation would be necessary, as proposal only. Compare A+B successor text to existing KOD contract; show exact diff/provenance if changing that contract. Prefer one separate candidate that leaves predecessor immutable.

Return one PASS_WITH_BOUNDARIES / FAIL / BLOCKED document-only terminal with exact file identity and UNKNOWN. Publish/readback/address KOO. If next step requires another chat, give one complete manual activation handoff. Publication/inbox/dispatch != KOD receipt or processing_started.

## Hard limits

No code, executable, tests, host, secret or credential contents, Bot API calls, getMe, getWebhookInfo, getChatMember, getUpdates, visitor messages, Telegram send/mutation, deployment, unit/helper/sudoers changes, Project Sources/canon/automation mutation. Prior diagnostic blocker remains. Memory-layering attempt 3 NOT_AUTHORIZED. Historical PROMPT no replay.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: TASK_AUTHORIZED_PENDING_MANUAL_ACTIVATION
