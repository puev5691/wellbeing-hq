# КОДЕР → КООРДИНАТОР: контракт защищённого read-only Bot API bridge r0.1

status: PASS_KOD_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_READY_FOR_SIS_REVIEW
scope: DOCUMENT_ONLY / DESIGN_CANDIDATE
authority: AUTHORIZE_KOD_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_ONLY
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Человеческий вывод

Проверенный доступ СИСАДМИНА к токену и двум диагностическим методам Bot API сейчас отсутствует. Данный документ фиксирует минимальный способ получить такой доступ в будущем без раскрытия токена, просмотра сообщений посетителей и изменения работающего Telegram-сервиса. Документ не создал bridge и не снял блокер диагностики; СИСАДМИН должен отдельно проверить реализацию и её границы после нового решения ОПЕРАТОРА.

## Admission и доказательства

Fresh HQ preflight: main `be688eee614d7d04cebdf7e734d0e42a4043c986`, tree `08178f57e404a6dfb5833049f4ec16a8a41a5b45`; checked current-writer KOD v0.5 `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`. Exact task `puev5691/wellbeing-hq@862a345a397f8bfd041d159b8c2110c8c1860bea:entities/koordinator/outbox/KOO__telegram-readonly-bot-api-bridge-r01-design__KOD.md`, blob `1d2b3220de3d0dca500b4ac195e4ec887db04414`, matches OPERATOR documentary authority. Six attached approved Project Sources loaded under source-loading policy: recovery v1.6, roles v2.4, source-loading v2.2, file-work v2.4, task-conveyor v1.2, core v2.5. Fresh current tree has no competing result or superseding task for this exact r0.1; no writer change.

Pinned causal inputs read by immutable identity:
- SIS `@b080637a3b7a58e4645b89ea030a06c34d888e28:entities/sisadmin/outbox/SIS__telegram-direct-message-path-diagnostic-r01__KOO.md`, blob `734146576f35942c6b584b898c83129521a7bc2a`, terminal `BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS`.
- KOO `@771458166e75c481d44b7e03acd2a8d6fa950d16:entities/koordinator/outbox/KOO__telegram-direct-message-diagnostic-reconciliation-r01__OPERATOR.md`, blob `b6d18738bbcf538b2b88a85a48b0d9112f269399`.
- KOD `@0ece5979ab5e0fbab485eb1491a4f51ce5bee105:entities/koder/outbox/KOD__telegram-channel-direct-message-fitgap-r01__KOO.md`, blob `cb6a41bb1cc577835e6ca036d264a287afa6b353`.

SIS independently observed host `ruvds-xnqc6`; `wellbeing-telegram-phase1b-sandbox.service` disabled/inactive, fake transport, no listener. Existing fixed root helper `/usr/local/sbin/wbn-phase1b-r01` (SHA-256 `a0873ef603bb331cb1bbc3d62c4e503daaf9945e92e08e24d5355a502930cbd0`) exposes neither method in current NOPASSWD allowlist. Systemd protected credential configuration exists but its value and availability to a separate process have **not** been established. SIS performed neither Bot API operation. The current blocker remains `NO_VERIFIED_READONLY_BOT_API_CREDENTIAL_BRIDGE_FOR_CURRENT_SIS_ACCESS`.

Official API reference: https://core.telegram.org/bots/api#getwebhookinfo ; https://core.telegram.org/bots/api#getchatmember ; https://core.telegram.org/bots/api#chatmemberadministrator . The Telegram HTTPS API embeds the token in its method URL. `getWebhookInfo` takes no parameters and its raw result can contain URL, address and error message; `getChatMember` takes `chat_id` and `user_id`. Administrator `can_manage_direct_messages` is optional for channels. These facts constrain redaction and three-state interpretation below.

## Proposed authority and trust boundary

| Layer | Candidate contract | Status now |
| --- | --- | --- |
| Requester | Exact independently verified SIS runtime identity on `ruvds-xnqc6`; no arbitrary caller, delegated bearer token or caller-supplied identity. A separately approved bounded diagnostic authority must identify caller, host, two operations, call budget and expiry. | PROPOSED; future authority UNKNOWN |
| Executable | A later pinned executable and supervised one-shot execution identity with SHA-256, immutable provenance and explicit allowlist for exactly two commands. Its identity must be verified before any protected credential is made available. It does **not** reuse or silently broaden the existing root helper. | PROPOSED; executable/service owner and bytes UNKNOWN |
| Bot/channel identity | Bind exact bot ID `8866633840`, username `@WBNP_Media_Bot`, and channel ID `-1003606547591` to independently checked provenance in a supervisor-controlled profile. The username alone is insufficient. Do not accept target IDs from user input, environment, cwd, symlink, untrusted Git mirror or caller-controlled config. Precall bot identity attestation requires separate approved evidence; a token merely functioning is insufficient proof of target identity. | IDs from pinned task VERIFIED; live token-to-bot binding UNKNOWN |
| Credential | Consume a supervisor-injected protected credential only inside the pinned short-lived process; no token in arguments, environment, stdout/stderr, logs, Git, diagnostic output or error text. Never pass raw HTTP/request tracing to caller. Whether existing protected systemd credential can be safely scoped to the new process without modifying the current unit is UNKNOWN and requires SIS proof. Missing, malformed or inaccessible credential: fail closed before network. | PROPOSED; feasibility UNKNOWN |
| Privilege | Dedicated minimal identity, no shell interpolation, arbitrary file reads, root session, general sudo, write permissions to service/webhook, arbitrary network or access to visitor data. A bounded Telegram endpoint egress exception, if necessary, requires separate authority. Current service must remain disabled/inactive. | PROPOSED; operational admission NOT_GRANTED |
| Transport | HTTPS to fixed Bot API origin with TLS hostname and certificate validation. Fixed method path chosen internally; request is built in memory with redacted telemetry. Disable redirects and proxy inheritance, reject untrusted URL overrides. Bounded request and response, deadline, exactly one call per separately admitted operation, retries=0; no fallback. Concrete numeric limits are an SIS-reviewed implementation choice, not established by this document. | PROPOSED |
| Audit | Record authorization identity, executable/profile hash, operation name, fixed target reference, attempt/outcome class, validation result and sanitized counts only. Never store token, raw URL, raw Telegram error description, webhook IP, visitor identifiers or content. | PROPOSED |
| Result | Closed, versioned JSON schema; whitelisted fields only; reject unsafe/malformed/oversize raw responses before output. Unknown stays UNKNOWN. Success and access authorization remain distinct from Telegram update delivery and actual bot reply. | PROPOSED |

A future implementation cannot create its own authority or attest its own caller, executable, token-to-bot binding or profile. An independently controlled supervisor verifies those before injection. Profile substitution, path/symlink swapping or Git mirror substitution must lead to `BLOCKED_IDENTITY`; exact trust root and implementing owner remain UNKNOWN for separate decision by ОПЕРАТОР and independent SIS review. A wrong token must not become a probe of arbitrary bots.

## Exactly two fixed operations and closed outputs

| Operation | Admitted arguments | Output fields on verified success |
| --- | --- | --- |
| `getWebhookInfo` | None. Internally fixed bot credential after identity admission. | `schema_version`, `operation`, `outcome=ok`, `webhook_configured` boolean derived solely from empty/nonempty URL, `has_custom_certificate` boolean, `pending_update_count` nonnegative integer, `allowed_updates` as `absent` or `present` plus bounded recognized update-type names, `delivery_error_present` boolean and `sync_error_present` boolean. Absent `allowed_updates` is not interpreted as an empty set. Do not return URL, hostname, path, IP, raw error messages, or dates if the implementation cannot prove they are safe. |
| `getChatMember` | `chat_id=-1003606547591`; `user_id=8866633840`. No caller overrides or extra parameters. | `schema_version`, `operation`, `outcome=ok`, `membership_status` from closed Telegram status enum, `administrator` boolean, `can_manage_direct_messages` as `true | false | unknown`. An absent optional right is `unknown`, never `false`. If not administrator, do not infer right or readiness. |
| Either failure | No arbitrary body/parameter. | `schema_version`, `operation`, `outcome=blocked | unknown`, closed `reason_code` (`AUTHORITY`, `IDENTITY`, `CREDENTIAL`, `PRIVILEGE`, `TRANSPORT`, `HTTP`, `RESPONSE_SHAPE`, `LIMIT`); sanitized audit identity. No raw API payload, token-bearing URL or Telegram description. |

Whitelisted response must pass Telegram envelope `ok=true` and exact expected `result` shape; HTTP 200 alone is insufficient. HTTP errors, `ok=false`, malformed content and unexpected fields are not affirmative evidence of webhook configuration or channel rights. Reject/erase unrecognized potentially sensitive fields from output; do not propagate a raw exception or URL. No `getUpdates`, messages, `sendMessage`, webhook mutation or bot rights change.

`getWebhookInfo` can show configured webhook/allowed updates and pending count at one instant. It cannot establish that an observed channel direct message generated an update, that the running service received it, or that a response was sent. `getChatMember` can establish the reported membership/administrative right for this bot and channel when its exact response is verified, but cannot establish delivery of a visitor message. Private `/start`, channel direct message, linked-group comment and `channel_post` are distinct routes.

## Fail-closed negative matrix for future SIS independent verification

Each case is **DESIGN_ONLY**, not a test performed in this turn. SIS must use synthetic/stub responses and supervisor-controlled fixtures first; any live Bot API read needs separate authority and its own evidence.

| Case | Stimulus | Expected result / evidence SIS must preserve |
| --- | --- | --- |
| P01 | Pinned caller/profile/executable, correct bot binding, valid webhook response | Sanitized whitelisted output; URL/IP/raw errors absent; one operation and one attempt in audit. |
| P02 | Same admission, valid `getChatMember` administrator response with right | Exact fixed IDs used; `can_manage_direct_messages=true`; no message/visitor fields. |
| N01 | Caller, host or authority mismatch/expired/consumed | `BLOCKED_AUTHORITY` before credential/network, nonzero failure. |
| N02 | Wrong bot ID, username-only binding, wrong channel ID, mismatched token attestation | `BLOCKED_IDENTITY` before operation; no arbitrary bot/channel probe. |
| N03 | Unpinned binary, changed hash, alternate unit/helper, profile substitution, untrusted mirror | `BLOCKED_IDENTITY`; preserve exact hash/provenance comparison. |
| N04 | Missing/empty/unreadable credential or permission escalation request | `BLOCKED_CREDENTIAL` or `BLOCKED_PRIVILEGE`; no fallback or credential dump. |
| N05 | Symlink/path replacement, cwd/config override or token accessible via argv/env/log/error | Refuse, no network; SIS inspects effective execution boundary and redacted stdout/stderr/audit, without exposing secret. |
| N06 | Extra method, arbitrary `chat_id`/`user_id`, parameter injection, shell metacharacters | Fixed allowlist rejects request before credential/network; no shell execution. |
| N07 | Proxy or redirect supplied, hostname/certificate mismatch, plaintext HTTP | Transport blocked; no redirect follow or proxy use; error contains no URL/token. |
| N08 | Timeout, disconnect, HTTP 401/403/429/5xx, Telegram `ok=false` | Closed `TRANSPORT` or `HTTP` reason; unknown diagnostic state; no automatic retry. |
| N09 | HTTP 200 with wrong `ok`, malformed/oversized JSON, wrong type, unexpected envelope | `BLOCKED_RESPONSE_SHAPE` or `BLOCKED_LIMIT`; never fabricate rights/config. |
| N10 | Webhook URL embeds token/secret, Telegram error message embeds content/IP | Output/audit contain only presence/class; no raw URL, message, address or token in any channel. |
| N11 | `allowed_updates` absent versus present empty/list | Preserve distinct states; no guess about accepted channel-direct-message update type. |
| N12 | Membership not administrator, member missing, optional right missing/unknown | No claim that direct messages are manageable; `unknown` remains unknown. |
| N13 | Caller requests repeated call or previous call fails | No retry, no fallback, per-operation budget enforced; attempts count exact. |
| N14 | Execution tries service restart, webhook/right mutation, user update read or reply | Capability absent; `BLOCKED_PRIVILEGE`; existing service state unchanged. |

Independent SIS acceptance requires (a) signed or otherwise independently anchored exact executable/profile and caller/host provenance, (b) proof protected token cannot be read by SIS caller and cannot leak through arguments, environment, URL logs, trace, audit, exception or output, (c) denial tests before network for identity and input failures, (d) simulated positive and failure response parsing/redaction, (e) audit and budget verification, (f) negative test of arbitrary bot/channel, redirect and proxy, (g) proof current unit/helper/sudoers/webhook/rights unchanged. SIS decides a later operational gate; KOD's candidate is not independent approval.

## Future staged admission and rollback — proposal only

A separate OPERATOR decision may authorize an implementation candidate and independent SIS security review. Only after exact byte/hash review and privilege analysis may a separate deployment gate decide how to stage a pinned one-shot process with a protected credential and fixed caller admission. Record pre-state of existing unit/helper/sudoers; rollback removes only the newly versioned bridge entry and restores its exact pre-state, with no service restart, token rotation or rights change implied by this design. A later explicit, narrowly scoped live diagnostic authority is required for each Bot API read. Missing trusted bot-token attestation or inability to isolate the credential remains an exact blocker; do not use the existing root helper's unrelated commands to work around it.

## Terminal and boundary

`PASS_KOD_TELEGRAM_READONLY_BOT_API_BRIDGE_R01_DOCUMENT_READY_FOR_SIS_REVIEW` means the documentary candidate is complete. Operational `BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS` remains. No source code, helper, host/credential/API access or tests were performed. No visitor information was read or recorded. No production or project acceptance is granted. Memory-layering attempt 3 remains NOT_AUTHORIZED. Publication/dispatch is not SIS receipt, activation, `processing_started` or review PASS.

Next causal gate: KOO requests independent SIS review of this exact immutable document and a separate OPERATOR decision about trust root, implementation owner and later bounded implementation authority. No live diagnostic follows automatically.

КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР
