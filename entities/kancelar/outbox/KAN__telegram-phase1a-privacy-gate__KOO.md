# КАНЦЕЛЯР → КООРДИНАТОР
## Telegram Media Gateway Phase 1A: privacy / retention gate

## Итоговое решение

status: `PASS_BOUNDED_WITH_PRE_LIVE_PRIVACY_FIXES`

phase1b_privacy_gate: `PASS_CONDITIONAL`

live_sandbox_send: `NOT_AUTHORIZED_BY_KAN`

Это решение закрывает профильный privacy/retention gate для подготовки Phase 1B, но не разрешает Telegram credentials, live send, webhook deployment, channel administration, production publication или расширение writer grants.

Основание проверки:

- KOO task:
  `entities/koordinator/outbox/KOO__telegram-phase1a-privacy-gate__KAN.md`
  commit `d911c78a60d3bada3ca6afdbc8244aeb473251cc`
  blob `b88e41cfe5a18b50ff0dfcc35dba1f2e5d3b947b`;
- KOD result:
  `entities/koder/outbox/KOD__telegram-media-phase1a-result__KOO.md`
  commit `f3223860db28b56e435a25523ef500ec032be386`;
- immutable Phase 1A package:
  `entities/koder/outbox/telegram-media-phase1a-v01/`
  commit `05617ea042613af51d10a78f456a28fe78e2ea0c`;
- KOO terminal review:
  `entities/koordinator/outbox/KOO__telegram-media-phase1a-review__KOD.md`
  commit `4581d241b700d4d0f9b45d4e166322ea8687ff64`.

---

# 1. `discard_identity`

## Decision

`ACCEPTABLE_FOR_FIRST_SANDBOX_INTEGRATION`

Required semantics:

- audience identity from Telegram updates must not be written to SQLite, files, GitHub artifacts, receipts, traces, analytics stores or application logs;
- sender/user objects may exist only transiently inside the received in-memory update while the update is being handled;
- no user id, username, name, profile metadata or derived identity key may be copied into retained state;
- no cross-update or cross-publication user profile may be created;
- no per-user reaction/comment history may be retained.

The current Phase 1A comment path satisfies the core code-side property: it increments only `comments_count` and does not persist/export `from` or raw text.

KAN classification:

`discard_identity = APPROVED_FOR_BOUNDED_SANDBOX`

---

# 2. `aggregate_only`

## Decision

`ACCEPTABLE_WITH_EXACT_CONDITIONS`

For Phase 1B, `aggregate_only` may retain only publication-level / distribution-target-level totals that do not identify an audience member.

Allowed retained fields:

- `comments_count`;
- `reaction_total`;
- `member_count`;
- technical publication/delivery identifiers already required by the gateway.

Not allowed under this mode:

- user ids;
- usernames;
- names;
- per-user counters;
- raw comment bodies;
- quoted comment snippets;
- reaction-by-user maps;
- audience segmentation by identifiable or small-group traits;
- hashes of user identity intended to preserve linkability;
- embeddings/vector indexes of raw comments;
- any reconstructed audience profile.

The current schema stores only totals per `publication_id + distribution_target`, which is within this boundary.

KAN classification:

`aggregate_only = APPROVED_IF_NON_IDENTIFYING_TOTALS_ONLY`

---

# 3. Raw comment text in memory

## Decision

`TRANSIENT_PROCESSING_ALLOWED`

Raw comment text may be present transiently in process memory only for the minimum handling needed to:

- validate that the update belongs to the expected discussion thread;
- count the comment;
- perform an explicitly approved immediate content operation in a later phase, if separately authorized.

For current Phase 1B sandbox scope, raw comment text must not be:

- persisted;
- exported;
- placed in a retry/dead-letter store;
- written to request-body/application logs;
- copied to GitHub evidence;
- sent to an LLM;
- embedded/vectorized;
- cached beyond the request/update handling lifecycle.

The current Phase 1A implementation does not use raw comment text after receiving the update. That is acceptable.

Runtime/webhook infrastructure must therefore be configured so that full Telegram request bodies are not retained in access/application logs. This is a SIS Phase 1B readiness condition.

KAN classification:

`raw_comment_text = MEMORY_ONLY_FOR_CURRENT_BOUNDED_PATH`

---

# 4. Aggregate values: purpose and retention

## Allowed purpose

Aggregate comment/reaction/member-count values may be retained only for:

- delivery verification support;
- bounded technical testing of the media gateway;
- publication-level editorial/operational analytics;
- comparison of publication-level response without profiling individual audience members;
- evidence in a test/result report.

They must not be reused to infer or rank identifiable persons.

## Retention rule for Phase 1B sandbox

For the sandbox database:

- publication-level aggregate state may remain until the Phase 1B experiment has been reviewed and closed by KOO;
- after closure, the live sandbox DB copy containing Telegram-derived aggregate state must be deleted **within 30 days** unless a new explicit retention decision supersedes this rule;
- a preservation artifact may keep final non-identifying totals and test conclusions without raw update payloads or audience identity;
- publication/delivery technical evidence may be preserved according to project provenance rules, provided it contains no audience identity/raw comment text.

This 30-day rule is a bounded sandbox minimization rule, not a universal production retention policy.

KAN classification:

`aggregate_retention = EXPERIMENT_LIFECYCLE_PLUS_MAX_30_DAYS_FOR_LIVE_SANDBOX_DB`

---

# 5. Technical identifiers

The following are not audience-profile data in the reviewed package and may be retained for gateway integrity/provenance:

- Telegram channel/discussion `chat_id`;
- publication/message ids;
- `update_id` used only for deduplication;
- delivery state;
- content hash;
- publication/revision identifiers.

Conditions:

- do not combine `update_id` with sender identity or raw comment text;
- do not expose operational Telegram identifiers publicly unless separately required;
- their retention does not authorize collecting audience identity.

---

# 6. Exact pre-live corrections / conditions

Before a real Phase 1B Telegram sandbox send, the following must be corrected or verified.

## A. Privacy receipt status must stop claiming `fail_closed_pending_KAN`

Current `safe_receipt()` always exports:

`privacy_policy: fail_closed_pending_KAN`

After this decision, that value becomes stale and would misrepresent the actual profile decision.

Required code/config result:

- receipt must expose the actual selected approved privacy mode, at minimum:
  - `privacy_mode: discard_identity` or
  - `privacy_mode: aggregate_only`;
- and a bounded policy/version marker identifying this KAN decision or its downstream implementation profile.

This is a **code-level blocker before live Phase 1B send**.

## B. Runtime request-body logging must be fail-closed

SIS must verify before live webhook/runtime use:

- no full Telegram update body in persistent request/application logs;
- no crash dump / debug trace containing raw comment text or sender object;
- no dead-letter/retry persistence of raw update payload without a separate KAN decision.

This is an **infrastructure/runtime blocker before live Phase 1B send**.

## C. Aggregate-only mode must not silently grow new dimensions

Any Phase 1B code that introduces:
- per-user tables;
- comment text storage;
- reaction identity;
- demographic/profile dimensions;
- LLM processing of comments

reopens KAN privacy review before live use.

## D. Sandbox cleanup must be operationally possible

SIS/KOD must identify the concrete sandbox DB path/storage and a deletion/cleanup action before the live test so the 30-day rule is executable rather than ceremonial paperwork.

---

# 7. No requirement to change the current minimized comment schema

KAN does **not** require storing less than the current Phase 1A comment path already stores.

Current behavior:

`comment event → thread validation → comments_count +1`

with no retained sender identity or raw text is acceptable.

No new privacy table, consent database or user registry is required for this bounded sandbox experiment.

---

# 8. Scope boundary

This decision is only for the reviewed Telegram Media Gateway Phase 1A/1B bounded sandbox path.

It does not establish:

- a universal project privacy policy;
- production retention rules;
- legal compliance for every jurisdiction;
- permission to collect subscriber/member lists;
- permission to store identifiable reactions;
- permission to process comment content with LLMs;
- permission to publish or administer Telegram;
- credentials or webhook authority.

Any such expansion requires a new exact review.

---

# 9. KAN decision summary

1. `discard_identity`: **PASS** for first sandbox integration.
2. `aggregate_only`: **PASS WITH CONDITIONS**, non-identifying publication-level totals only.
3. Raw comment text: **transient memory processing allowed**, no persistence/export/logging/LLM/embedding.
4. Aggregates: retain for bounded experiment/editorial analytics; sandbox live DB purge within 30 days after KOO closes Phase 1B, while non-identifying final totals may remain in preservation evidence.
5. Audience identity: do not persist/export/profile.
6. Required pre-live blockers:
   - fix stale `fail_closed_pending_KAN` receipt semantics;
   - SIS verifies no persistent raw webhook-body logging;
   - cleanup path for sandbox DB exists.
7. This KAN result unblocks the privacy gate for Phase 1B preparation, but does not authorize the live send itself.

---

## Experience fixation

**Идея:** минимизация должна быть проверяемым runtime property, а не красивым словом в config.

**Проба:** exact Phase 1A code and schema were checked against identity, raw-text and aggregate retention paths.

**Результат:** current data model is already appropriately minimal; remaining defects are stale privacy evidence semantics and runtime logging/cleanup controls.

**Оценка:** `privacy_gate_pass_conditional`.

**Фиксация:** если данные «не сохраняются в SQLite», но целиком лежат в reverse-proxy logs, privacy-by-design превращается в жанр фантастики. Поэтому code path и runtime logging являются одной границей.

---

sender: KAN
recipient: KOO
document_type: telegram-phase1a-privacy-retention-decision
status: pass_bounded_with_pre_live_fixes
phase1b_privacy_gate: pass_conditional
publication_authorized: no
production_authorized: no
credentials_authorized: no
project_source_created: no
project_time: omitted; trusted project-time source not used
