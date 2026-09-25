# KOO → OPERATOR: Telegram bridge A+B SHD receipt and governance gate r0.1

status: READY_FOR_OPERATOR_AB_GOVERNANCE_DECISIONS_R01
scope: DOCUMENT_RECONCILIATION_AND_DECISION_PREPARATION_ONLY
project_time: omitted
fresh_preflight_HQ_HEAD: 7ab36a883eac3a95411ec5bc67985441c33d51f5
current_KOO_writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md
current_KOO_writer_blob: ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
current_KOO_writer_status: WRITER_ESTABLISHED

## Receipt and immutable inputs

KOO independently read exact SHD result:
puev5691/wellbeing-hq@c641965b9b9d1a3492c191042b5431a48bc2d702:entities/shardovik/outbox/SHD__telegram-bridge-ab-identity-attestation-r01-independent-document-review__KOO.md
blob: 17f3dba23a08968b186a23dcfa5d7db56e2924d1
terminal: PASS_SHD_TELEGRAM_BRIDGE_AB_IDENTITY_ATTESTATION_R01_WITH_BOUNDARIES
receipt: ESTABLISHED_BY_THIS_KOO_EXACT_READ
inbox pointer commit: 2e9e98fc10fd163455dc78751082f77c90e44681
dispatch commit: 8be441b0fdf55dedbca504eab4996fda5dc77d3d
inbox/dispatch status before KOO reading: routing evidence only, not receipt/activation/processing_started.

Exact reviewed KOD design:
puev5691/wellbeing-hq@871cb4e411a537ac2b9657a4b32710f88839d7b7:entities/koder/outbox/KOD__telegram-bridge-ab-identity-attestation-design-r01__KOO.md
blob: 575d5f03159f09de57d91c60fd99078c050f89d8

SHD task:
puev5691/wellbeing-hq@427b82307bead9cfac192b3b348f79b2c105b44f:entities/koordinator/outbox/KOO__telegram-bridge-ab-identity-attestation-r01-shd-independent-document-review__SHD.md
blob: 172dd70e47148a9daab0fc907b862cab117897aa

OPERATOR's prior A+B direction and functional assignments:
puev5691/wellbeing-hq@91f4dd2452a082ac9025fe4211407dce47dd4629:entities/koordinator/outbox/KOO__telegram-readonly-bridge-ab-ownership-design-choice-r01__OPERATOR.md
blob: b028b023c5892483eea9118489968eff848ddf21
status: DESIGN_ONLY

The active attached approved Project Sources were read and checked at their exact blob identities: recovery v1.6 233117e1c9509d730e1f5ec532b1cabe3f786609; roles v2.4 1772339cb74dae8550bfbd2e33401c34a929e911; source-loading v2.2 69eb657f260a019f76e8e707c880ea88c1dfa0bf; file-work v2.4 e9c29d62057f34e4f771d6057a36d9b7f72e74c2; task-conveyor v1.2 df7896d867eeeffff506319538fedad938856686; core v2.5 a42f7dca6a7469a54fa2da24aae0da4e549c9d33.
Fresh commits from SHD publication through HEAD only address/record/dispatch the same result; no later competing A+B terminal or superseding candidate observed in this bounded lineage check. Historical PROMPT not replayed.

## Disposition

SHD PASS accepted only as independent documentary evaluation of the A+B design. No issued A, issued B, proven token→bot binding or runnable protected bridge follows. Intended project bot_id 8866633840 and channel_id -1003606547591 are document claims, not live token/rights verification.

## Six OPERATOR governance choices — proposed package, not KOO approval

1. A issuer/trust root/currentness/revocation:
   Proposed design: KAN prepares/issues the documentary A candidate under an exact later task; OPERATOR approves its exact immutable digest and serves as trust root and authority for A current-generation/effectivity/revocation decisions, each captured in an explicit immutable decision; KOO records locators only. A Git commit, filename or KAN assertion by itself is not approval. Until a verifiable OPERATOR approval/currentness/revocation mechanism is specified and reviewed, A remains non-effective.

2. Exact canonical byte format of A:
   Proposed choice: RFC 8785 JSON Canonicalization Scheme on a closed, versioned A payload schema, UTF-8 output bytes with no BOM or appended LF; I-JSON, duplicate keys rejected; Unicode preserved as-is, no implicit normalization; identifier values whose exact decimal digits matter encoded as decimal strings; absent field and explicit null are distinct and the schema must permit one form per field. SHA-256 covers only the canonical payload bytes; profile_digest and repository readback metadata live outside that payload to avoid a self-referential digest. The exact closed field schema and example vectors require later independent documentary review before issuance. This is a proposal to adopt a format, not an issued profile.

3. B proof method:
   Proposed design choice: separately designed protected one-shot numeric-bot-ID query for the exact credential slot generation, subject to a later independent authorization and protected provenance review; no call authorized by this choice. Offline provisioning lineage may replace that method only if a separately reviewed complete, independent, current slot→numeric-ID chain is found; current repository evidence is insufficient. The query is a separate B attestation path, not a third operation in the existing two-method diagnostic bridge.

4. B producer / independent accepter:
   Proposed design: SIS produces sanitized B and maintains private underlying slot/operation evidence within future separately authorized scope; SHD independently reviews exact protected underlying evidence and issues a bounded evidence disposition under a separate task and verified competency; OPERATOR alone accepts the operational outcome. B producer self-assertion or a public sanitized equality alone is insufficient.

5. Separation of duties:
   Proposed design: four documentary trust functions must have distinct role principals: KAN=A issuer, SIS=B producer, OPERATOR=A currentness/revocation authority, SHD=B independent evidence accepter. OPERATOR additionally approves exact A and the eventual operational result. Distinct Entity names do not alone prove independent credentials, organizational control or cryptographic separation; the actual independent evidence access and trust roots require later verification. No principal may self-issue and self-accept B.

6. B supersession/currentness:
   Proposed design: explicit supersedes_attestation_id and slot_generation in each B successor plus an independently anchored OPERATOR currentness/revocation decision for the exact slot generation. B(n) does not carry to n+1; ambiguous ancestry, contradictory currentness, inaccessible authority or revoked generation => BLOCKED_CONFLICT. Neither latest timestamp nor latest Git commit/file selects B.

OPERATOR may approve this package as DESIGN_ONLY, amend any numbered line, or defer. A design approval does not issue A or B and does not authorize any implementation, protected query, host/token access or Telegram call.

## Exact preserved boundaries

prior_SIS_blocker: BLOCKED_SIS_TELEGRAM_DIRECT_MESSAGE_DIAGNOSTIC_NO_VERIFIED_READONLY_BOT_API_ACCESS
token_to_bot_binding: UNKNOWN
A_issued: NO
B_issued: NO
implementation_authority: NOT_GRANTED
live_Bot_API_authority: NOT_GRANTED
memory_layering_attempt_3: NOT_AUTHORIZED
candidate_or_Project_Source_mutation: NONE
historical_PROMPT_replay: NONE

next_gate: OPERATOR_DECISION_ON_SIX_AB_GOVERNANCE_ITEMS_ONLY
