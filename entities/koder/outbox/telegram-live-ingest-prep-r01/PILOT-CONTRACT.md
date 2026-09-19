# Telegram real-discussion ingestion pilot contract r0.1

status: PREPARED_NOT_AUTHORIZED
execution_mode: PREPARATION_ONLY
live_authority: NOT_GRANTED

## Purpose

Define one bounded first real-discussion read pilot that converts only privacy-minimized discussion excerpts into the already verified SemanticInput → facilitator-core path. This contract itself performs no Telegram read/send and grants no authority.

## Exact target and read scope

Target discussion is bound by numeric chat id `-1002429106148`, previously verified by SIS. The observed title discrepancy is deliberately not used for authorization.

A future OPERATOR authority MUST bind all of these values explicitly before execution:
- chat_id: `-1002429106148`;
- direction: read-only;
- maximum accepted messages: 20;
- one contiguous Telegram message_id interval with explicit inclusive `min_message_id` and `max_message_id`;
- maximum UTF-8 text accepted from any one message before minimization: 4096 bytes;
- no historical pagination outside that interval;
- retries: 0;
- sends: 0;
- provider calls: 0.

If exact message_id bounds are absent, the pilot MUST NOT read Telegram. The execution layer may make only the minimum API request(s) required to obtain that exact bounded interval and must stop once 20 accepted messages or max_message_id is reached.

## Privacy/minimization boundary

Raw Telegram response/update objects are transient input only and MUST NOT be written to disk, database, logs, project artifacts, stdout/stderr diagnostics or Git.

For each accepted text message, before SemanticInput construction:
1. verify exact authorized chat_id and message_id interval;
2. reject non-text/service/media-only messages;
3. discard raw envelope fields not required for this pilot;
4. strip username, first/last name, phone, user/chat/member ids, reply/forward origin identity, profile/link metadata and other Telegram identity fields;
5. create an optional discussion-local opaque pseudonym only when distinction between speakers is semantically necessary; otherwise participant=null;
6. pseudonym MUST be generated from an execution-local random salt plus source sender identity, must not contain/reveal the source id, and the salt/mapping MUST remain memory-only and be destroyed at pilot end;
7. minimize text to the smallest excerpt/claim needed for one declared semantic category; maximum minimized text 512 UTF-8 bytes;
8. classify only into the already accepted declared categories; no undeclared inference or automatic LLM/provider classification;
9. create `admitted_minimized` SemanticInput with `minimized_derived` + `memory_only` policy and bounded expiry;
10. destroy the raw message object as soon as its minimized projection is admitted or rejected.

No raw Telegram text is a permitted persistent output.

## Identity boundary

Persistent/project-visible outputs MUST NOT contain Telegram user_id, username, first/last name, phone, raw chat member identity, forward/reply identity or the pseudonymization salt/mapping.

A discussion-local opaque pseudonym may exist only inside the bounded in-memory semantic run when required for distinguishing positions. It must not be exported into NormalizedEvent/candidate artifacts.

## Safe outputs

The only permitted semantic outputs are:
- bounded `discussion_state` projection;
- candidate questions;
- candidate summary;
- `candidate_task` proposal.

Every candidate task MUST remain:
- `status=candidate_only`;
- `executable=false`;
- `approved_for_execution=false`;
- no dispatch;
- no project acceptance;
- no execution authority.

For real minimized input, persistence/export of discussion_state is forbidden unless a separate persistence/privacy authority exists. Therefore the default pilot output is an in-memory state plus redacted metadata/result counts and candidate text stripped of participant identity.

## OPERATOR authority gate

Before the first real Telegram read, require a new immutable OPERATOR/KOO authority artifact that explicitly references this contract's exact commit/blob and states:
- authorized chat_id;
- inclusive min_message_id/max_message_id;
- max_messages <= 20;
- read-only;
- retries=0;
- sends=0;
- provider_calls=0;
- credential access permitted only to the designated Telegram read executor for this single bounded pilot;
- raw-envelope persistence forbidden;
- automatic dispatch/acceptance forbidden;
- authority is single-use and consumed at first bounded read attempt.

Existing one-send/readback authority `09b6fdfd04da84533185b11b0861b2220b72dfb3` is consumed and MUST NOT be reused.

## Abort/failure conditions

Abort before or during read on any of:
- missing/mismatched/ambiguous authority identity;
- chat_id mismatch;
- missing or invalid message_id bounds;
- request would paginate outside bounds or exceed 20 accepted messages;
- any need for retry;
- credential unavailable/invalid;
- raw envelope would be persisted/logged;
- minimization cannot occur before SemanticInput;
- identity cannot be stripped safely;
- unsupported content requires media/file download;
- semantic category cannot be declared without inference outside accepted contract;
- SemanticInput admission/privacy/retention proof fails;
- any candidate becomes executable/accepted/dispatched;
- provider/tool/web/file/code execution becomes necessary;
- any mutation/send/moderation/right change would occur.

On abort, persist only fixed error code + bounded non-sensitive counters and immutable authority/contract references. Do not persist rejected raw text or identity.

## Deterministic verification fixture

Before live authority may be consumed, an independent verifier should exercise a synthetic Telegram-shaped fixture containing:
- in-range and out-of-range message_ids;
- text and service/media-only messages;
- user_id/username/name/forward/reply identity fields;
- repeated sender identity;
- >512-byte candidate text;
- unknown/unsupported fields.

Required assertions:
- only in-range bounded text enters minimization;
- identity fields do not appear in SemanticInput/core/candidate serialization;
- stable same-speaker pseudonym within one run, unlinkable across runs;
- no salt/mapping persistence;
- raw envelope persistence/logging = 0;
- accepted SemanticInput is admitted_minimized/memory_only;
- safe outputs only;
- candidate task remains non-executable/non-accepted/non-dispatched;
- Telegram calls/provider calls/credential reads = 0 during fixture verification.

## Boundary

This preparation does not authorize a live read, send, credential access, provider call, deployment, moderation, or automatic task routing.
