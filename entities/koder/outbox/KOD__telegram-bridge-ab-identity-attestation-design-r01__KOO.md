# КОДЕР → КООРДИНАТОР: A+B профиль идентичности и отдельная аттестация credential slot r0.1

terminal: PASS_KOD_TELEGRAM_BRIDGE_AB_IDENTITY_ATTESTATION_DESIGN_R01_WITH_BOUNDARIES
scope: DOCUMENT_ONLY / NON_LIVE_DESIGN
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Смысл

Направление A+B уточняет ранее проверенный проект двухоперационного диагностического моста. A закрепляет, какого бота и какой канал мы намерены проверять; B отдельно свидетельствует, что защищённый слот действительно содержит действующий для этого бота токен. Пока B не получено и независимо не проверено, безопасный диагностический вызов не допускается. Ни профиль, ни аттестация не создаются работающими средствами в этом шаге.

## Fresh admission и точные основания

Preflight HQ main `a78cab660069a80c787ad8aa711797a2cd8cfdbb`, tree `a085164b289720ab10a9e211f054c15b6f169c07`, recursive scan truncated=false. Current KOD v0.5 writer `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`; v0.4 freeze persists. Exact addressed task `puev5691/wellbeing-hq@d4694135330d41531d1f42b65cc030d9787bf472:entities/koordinator/outbox/KOO__telegram-bridge-ab-identity-attestation-design-r01__KOD.md`, blob `c6742c613e81e9b50eef4ee948e06e6b7000b8d7`; OPERATOR decision `@91f4dd2452a082ac9025fe4211407dce47dd4629:entities/koordinator/outbox/KOO__telegram-readonly-bridge-ab-ownership-design-choice-r01__OPERATOR.md`, blob `b028b023c5892483eea9118489968eff848ddf21`. Both read at pinned commits; exact tree has no newer KOD writer, successor task or competing A+B terminal. Six attached approved Project Sources read: recovery v1.6, roles v2.4, source-loading v2.2, file-work v2.4, task-conveyor v1.2, core v2.5. Staged PRV roles v2.5 do not expand this scope.

Further immutable inputs:
- KOD predecessor `@bcfe46af1be40b347bc1e8d829446d999e61c2de:entities/koder/outbox/KOD__telegram-readonly-bot-api-bridge-r01-design__KOO.md`, blob `cdcfd65fc18ce6d6124c5710f3de27febf35ada7`.
- SIS independent review `@124cc535f562e53570690a8b93ae18b0d77440fe:entities/sisadmin/outbox/SIS__telegram-readonly-bot-api-bridge-r01-independent-review__KOO.md`, blob `6d8228cca029c67797e7d417fb13847ebbe5cc44`, terminal `PASS_SIS_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_REVIEW_WITH_BOUNDARIES`.
- SIS original diagnostic `@b080637a3b7a58e4645b89ea030a06c34d888e28:entities/sisadmin/outbox/SIS__telegram-direct-message-path-diagnostic-r01__KOO.md`, blob `734146576f35942c6b584b898c83129521a7bc2a`, blocker `NO_VERIFIED_READONLY_BOT_API_CREDENTIAL_BRIDGE_FOR_CURRENT_SIS_ACCESS`.

The pinned records establish **intended project IDs**: bot `8866633840`, username `@WBNP_Media_Bot`, channel `-1003606547591`. They do not independently attest a live token→bot link or live channel rights. SIS observed protected credential configuration, not the token or secure reuse of its slot in a separate one-shot process. No live bot/slot binding is established.

## A — proposed immutable supervisor-owned identity profile

This is a proposed schema, not an issued profile. Canonical encoding must be specified exactly before generation (for example, constrained canonical JSON with UTF-8, fixed field order/normalization and no duplicate keys); hash the **actual canonical bytes**, not a rendered display. Require an immutable repository locator with commit and blob plus independently trusted signature/approval or equivalent anchoring. Git publication alone does not select the trusted issuer or current version.

| Field | Proposed value or derivation | Evidence/state |
| --- | --- | --- |
| `schema_id`, `profile_id`, `generation` | Versioned A schema, globally unique profile identity, monotonic generation for this exact bot/channel/slot scope | PROPOSED; issuer/generation registry UNKNOWN |
| `bot_id`, `bot_username_hint` | `8866633840`, `@WBNP_Media_Bot` | Project intended identity VERIFIED_FROM_DOCUMENTS; live username mutable/UNKNOWN |
| `channel_id` | `-1003606547591` as fixed `getChatMember.chat_id` | Intended target VERIFIED_FROM_DOCUMENTS; live administration UNKNOWN |
| `credential_slot_ref`, `slot_generation` | Opaque supervisor-controlled protected slot reference and exact rotation generation; **no** token, token-derived digest or readable secret path in public profile | PROPOSED; exact protected slot binding/transfer UNKNOWN |
| `host_identity`, `caller_identity`, `executable_identity` | Exact independently anchored host/caller principal and future pinned executable hash/locator, or explicit unresolved dependency IDs; later must match measured runtime | Host `ruvds-xnqc6` documented by SIS; other future exact identities UNKNOWN |
| `operations`, `fixed_parameters` | Exactly `getWebhookInfo` (none) and `getChatMember` (`chat_id=-1003606547591`, `user_id=8866633840`) | PROPOSED; no third bridge method |
| `source_evidence` | Each project ID and policy claim: repository, exact path, commit, blob, claim type, verifier and provenance; never upgrade historical record to live proof | Pinned inputs above VERIFIED_AS_DOCUMENTS |
| `issuer`, `trust_anchor_id`, `approval` | Independently authorized issuer identity; trust-root reference; exact OPERATOR approval/accepted scope and immutable evidence | OPERATOR chose A+B direction only; issuer/root/effectivity UNKNOWN |
| `validity`, `supersedes`, `revocation_ref` | Defined effective start, expiration policy, predecessor ID, independently anchored revocation/current-generation reference | PROPOSED; no assumed dates, revocation owner UNKNOWN |
| `profile_digest`, `readback` | Digest of canonical bytes, Git commit/blob identity, independent readback matching canonical bytes and approval binding | PROPOSED; no issued A bytes yet |

A supervisor must resolve the profile by exact immutable identity plus trusted approval, verify bytes/hash/issuer/approval, consult an authoritative non-caller-controlled current-generation and revocation state, and compare the runtime host/caller/executable/slot identity. If the currentness source is unavailable or two valid-looking generations conflict, `BLOCKED_PROFILE_CURRENTNESS`. An immutable old profile by itself cannot tell whether it has since been revoked. No caller-supplied mirror, profile path, symlink, env, cwd or username resolves trust. Username is display evidence only: a changed username with unchanged independently attested bot ID does not silently rewrite A; require separately approved successor A if policy needs the new hint. A channel rename does not authorize a different numeric channel ID.

## B — separate proposed slot→bot attestation

A is not B. B is an independently checkable claim about **one exact credential slot generation** and bot ID, with provenance bound to A; the raw token and token-derived public verifier never leave protected scope. B is not an added method in the existing two-method diagnostic bridge.

Proposed closed B evidence envelope:
`schema_id`, `attestation_id`, `A_profile_digest`, `A_generation`, `slot_ref` (opaque), `slot_generation`, `host_identity`, `claimed_bot_id=8866633840`, `method`, `method_authority_locator`, `issuer`, `issuer_trust_anchor`, `observation_id`, `evidence_locator+commit+blob+canonical_digest`, `validity`, `revocation_ref`, `sanitized_outcome`, `independent_review_ref`. No token, URL, token hash, raw network response, IP, visitor content, caller-set bot/channel targets or secret-bearing path. A verifier checks exact byte/hash, issuer/authority, A and slot generation, currentness and method-specific confidence. Proposed `sanitized_outcome=bot_id_match` is permissible only when exact underlying independently reviewable evidence proves the claim; a self-assertion is insufficient. Separately scoped private evidence can be examined under later authority without exposing the token to KOD or Git.

Possible methods, **alternatives requiring their own decision**:
1. **Offline provisioning lineage:** existing immutable provisioning record may suffice only if an independently trusted issuer recorded the exact protected slot generation, credential material binding to verified bot ID, authorized transfer chain and no later unaccounted rotation. Read-only repository documents here do **not** prove such a complete chain. Current status `UNKNOWN_INSUFFICIENT_EVIDENCE`. A historical send or unit's `LoadCredential` presence is insufficient.
2. **Future protected one-time identity query:** a separately authorized, isolated SIS-operated process could use the exact protected slot for one bounded identity query (e.g. Telegram `getMe`) and retain only sanitized exact returned numeric bot ID plus an independently auditable operation/slot binding. It requires distinct exact OPERATOR authority for that operation, host/secret/egress/security admission, future pinned executable, no retry/fallback, and independent SHD review of evidence. **No query is performed or authorized here.** This method belongs to a separate attestation path, not to the two-method diagnostic bridge. Telegram success alone without independently verified slot/process provenance is insufficient. A username match without numeric ID is insufficient.
3. **Equivalent independent proof:** only after OPERATOR selects and SHD reviews exact evidence strength and issuer; no unspecified equivalent is accepted by default.

If provisioning evidence and a later live query disagree, do not pick the more convenient record: `BLOCKED_CONFLICT`, quarantine admission until new investigation/decision. B for slot generation n is invalid for generation n+1 even if a slot alias is unchanged. Rotating a token requires new B and possibly new A if protected reference, generation or approved scope changes; old evidence is explicitly revoked/superseded. No token-derived public fingerprint is proposed. Expiry and revocation require trusted current-state evidence; inability to read it is a blocker, not evidence of no revocation.

## Proposed supervisor admission sequence (future only)

1. Verify exact separately approved operation-specific task authority: allowed requester, host, action, fixed IDs, budget, validity and consumed/unused state. DESIGN_ONLY cannot be used for an operation.
2. Verify A canonical bytes, digest/commit/blob, trusted issuer approval, current generation, no revocation or unresolved conflict.
3. Verify B separately: method authority, underlying evidence/provenance, independently anchored issuer and review, matching `A_profile_digest`, bot ID, exact slot generation and host, currentness. Fail if B missing/stale/ambiguous.
4. Verify pinned caller, process executable bytes, supervisor trust root, protected credential transfer semantics and fixed two-method allowlist; reject path/symlink/mirror/env substitutions. Secure systemd credential transfer to a distinct process is UNKNOWN pending SIS design and later test.
5. Only then inject protected credential into that pinned process for separately authorized exact operation. The internal Bot API token-bearing URL exists in protected process memory as required by the API; it must never be exposed in argv/env/proxy/log/error/trace/audit/output. No network call or arbitrary bot/channel probe is allowed before successful admission. Existing service, unit and helper remain unchanged by this design.

A/B verification is an admission dependency, not a grant to call API. Positive attestation does not prove update receipt, visitor message delivery, or ability to answer. `getWebhookInfo` and `getChatMember` remain the only diagnostic bridge operations. Existing SIS blocker continues until a separately authorized implementation and independent verification establish protected access.

## Documentary verification matrix — no tests executed

| Case | Future input / condition | Required outcome |
| --- | --- | --- |
| P01 | Trusted current A with immutable readback; independently accepted B of same A digest and slot generation; exact caller/host/executable and later operation authority | Admission may proceed to protected injection only after all dependencies; this document makes no live PASS claim. |
| P02 | Independently proven numeric bot ID same; username hint changed | Do not silently replace A; new hint requires approved successor A if required by policy; no redirection. |
| N01 | Different bot token or B returned different numeric bot ID | `BLOCKED_BOT_BINDING`; no diagnostic probe of that token. |
| N02 | Wrong channel ID or caller supplies alternate target/username | `BLOCKED_TARGET`; no arbitrary `getChatMember`. |
| N03 | A swapped by path, symlink, altered hash, untrusted Git mirror or self-approved issuer | `BLOCKED_PROFILE_IDENTITY`; no credential injection. |
| N04 | B issued for different profile digest, slot ref, generation, host or executor | `BLOCKED_ATTESTATION_MISMATCH`; no credential injection. |
| N05 | A or B expired/revoked; missing currentness/revocation service or split/conflicting valid-looking evidence | `BLOCKED_CURRENTNESS` / `BLOCKED_CONFLICT`; no inference from cached prior PASS. |
| N06 | Slot rotates in place; old B persists; aliases unchanged | `BLOCKED_SLOT_GENERATION`; new B required. |
| N07 | Unknown/untrusted issuer, missing approval or independent review, unsupported method, historical send only | `BLOCKED_TRUST_ROOT` or `BLOCKED_EVIDENCE`. |
| N08 | Credential source missing/inaccessible, transfer method unknown, unit/helper/sudoers change needed | `BLOCKED_CREDENTIAL_BOUNDARY`; no fallback. |
| N09 | Token-bearing URL, raw response, error or token-derived verifier appears in proposed Git/output/log | Reject and contain evidence; do not publish secret; security incident handling needs separate policy. |
| N10 | Authority permits only design or another operation; attempts query `getMe` inside existing bridge or retries | `BLOCKED_AUTHORITY`; zero unauthorized API calls. |
| N11 | Host/caller/executable differs, caller overrides trusted profile | `BLOCKED_EXECUTION_IDENTITY`; no credential injection. |
| N12 | A/B both valid historically but supersession ancestry unresolved | `BLOCKED_CONFLICT`; no default to latest filename/commit. |

All entries are proposed acceptance/denial criteria; **executed tests: 0**. SHD independent review needs an exact task and verified scope/competence; role name alone does not certify this design.

## What exists, what remains UNKNOWN, and next decisions

Published documents establish intended IDs, previous two-operation security design, SIS document review and exact credential-access blocker. They do **not** establish an issued A profile, trusted issuer/supervisor/revocation root, issued B attestation, token-to-bot binding, slot generation, complete immutable provisioning lineage, secure transfer from current systemd credential to one-shot process, future executable, diagnostic authority, or operation acceptance. No profile B proof is inferred from the historical one-send, current unit properties or bot username.

OPERATOR must separately decide: (1) supervisor/issuer trust root and who approves current A and revocations; (2) whether independently verifiable offline provisioning lineage suffices for B, or whether a *separately authorized* protected one-time bot-identity query is required; (3) exact owner of B production and independent review with evidence access; (4) later implementation and live diagnostic authorities after SIS proves credential boundary. KOD authors future code only under separate scope; SIS owns future host/secret/deployment boundary only under separate scope; SHD independently reviews exact future technical evidence only with separately verified task/competence; OPERATOR alone makes operational acceptance after gates. These are functional assignments in OPERATOR's design decision, not current privileges.

**Relation to predecessor:** this is a separate immutable successor candidate. The existing KOD bridge document and its two-method allowlist are unchanged (diff to predecessor artifact: **zero bytes modified**). Added here: explicit A schema, separate B envelope/methods, binding/currentness/revocation checks, split-evidence negative cases and responsibility boundaries. No canon or Project Sources change.

terminal: `PASS_KOD_TELEGRAM_BRIDGE_AB_IDENTITY_ATTESTATION_DESIGN_R01_WITH_BOUNDARIES`
operational_bridge: NOT_CREATED
token_to_bot_binding: UNKNOWN
secure_credential_transfer: UNKNOWN
diagnostic_blocker: BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS
memory_layering_attempt_3: NOT_AUTHORIZED
historical_PROMPT_replay: 0
provider_or_Bot_API_calls: 0
host_or_secret_access: 0
tests: 0

Next causal gate: KOO arranges independently scoped SHD **document review** of exact immutable A+B result, checking trust-root and evidence logic, then brings remaining owner/attestation-method decisions to OPERATOR. No implementation or live query follows automatically.

---
КТО: KOD / КОДЕР v0.5
КОМУ: KOO / КООРДИНАТОР
