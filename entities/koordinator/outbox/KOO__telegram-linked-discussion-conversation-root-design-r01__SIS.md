# KOO -> SIS: Telegram linked-discussion conversation-root design r0.1 independent semantic review

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current intended SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact KOD result

puev5691/wellbeing-hq@13db3197031ca02a1eeb5775370ec7e59b08aea4:
entities/koder/outbox/KOD__telegram-linked-discussion-conversation-root-design-r01-result__KOO.md

blob:
7bc8e09f27c3a28c0d60f8cc6b187bde8784187a

terminal:
PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_READY_FOR_SIS_REVIEW

status:
DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Exact immutable design candidate

puev5691/wellbeing-hq@a554895b4305973d6ef836313870565d99810a3c:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/DESIGN.md

blob:
194590033c2c14e50f83d6fccf368febacc1b17c

Selected design:
C5 HYBRID_FAIL_CLOSED

## Exact failure basis

puev5691/wellbeing-hq@d06ebe706473a0e96027322782c1b4f9b47e1ba8:
entities/sisadmin/outbox/SIS__telegram-same-thread-two-turn-multiturn-r01-result__KOO.md

blob:
e513fc629ca02700571d7993080fa38ee567684e

terminal:
FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH

Exact evidence includes:

Turn 1:
- message_thread_id=110
- outbound_message_id=112
- visible YES

Turn 2:
- OPERATOR used Reply on exact visible bot reply 112
- message_thread_id=112
- trigger_class=reply-to-bot
- visible YES

Tuple/key mismatch:
PROVEN

Numeric equality 112==112:
PROJECT EVIDENCE ONLY, NOT TELEGRAM SEMANTICS.

## Scope

Perform ONLY independent semantic/design review.

Do NOT:
- implement code;
- modify dialogue_mvp.py;
- modify DB/schema;
- install;
- start/enable service;
- call Telegram;
- call OpenAI;
- mutate runtime.json;
- mutate allowlist;
- mutate credentials;
- replay failed live task.

## R1. Official-source map

Independently verify the design's use of official Telegram semantics from:

- https://core.telegram.org/bots/api
- https://core.telegram.org/api/discussion
- https://core.telegram.org/api/threads
- https://core.telegram.org/api/forum

Check specifically:

1. Bot API Message.message_thread_id semantics;
2. direct reply_to_message semantics and one-hop/non-recursive nature;
3. is_automatic_forward meaning;
4. linked channel post -> auto-forwarded discussion message -> comment thread semantics;
5. MTProto reply_to_msg_id vs reply_to_top_id/top_msg_id distinction;
6. replies inside an existing thread do not create nested MTProto threads;
7. Bot API does NOT directly expose reply_to_top_id/top_msg_id;
8. forum-topic semantics remain a separate mode.

Flag any overclaim.

## R2. Exact project evidence / protocol separation

Verify the design correctly separates:

OFFICIAL_PROTOCOL_FACT
EXACT_PROJECT_EVIDENCE
DESIGN_INFERENCE

Confirm it does NOT infer from:
Turn1 outbound_message_id=112
Turn2 message_thread_id=112

that 112 is Telegram's canonical root.

Exact cause may remain UNKNOWN.

## R3. C5 HYBRID_FAIL_CLOSED semantic validity

Review the selected model:

- proven canonical/top root when actually evidenced;
- bounded observed linked-thread anchor for initial session only;
- direct reply-to-known-bot-outbound can inherit prior stable project root;
- ambiguity never causes history merge;
- unresolved lineage isolates/rejects fail-closed.

Determine whether this preserves:
- deterministic continuity;
- cross-thread isolation;
- cross-chat isolation;
- mode separation;
- replay safety;
- no silent merge.

## R4. PROVEN_OUTBOUND_LINEAGE

Review exact conditions for inheriting prior root from a direct reply.

Required conditions in design:

- inbound is reply-to-bot;
- reply_to_message.message_id present;
- lookup by current chat + reply target finds exactly one prior eligible outbound effect;
- prior effect state COMMITTED or FALLBACK_COMMITTED;
- prior stable root non-null;
- returned/prior chat equals current chat;
- mode identical;
- direct-topic/mode guards non-conflicting.

Verify these are sufficient and not over-broad.

If additional exact guard is necessary, identify only the minimal one.

## R5. Root derivation classes

Review bounded classes:

- PROVEN_AUTO_FORWARD_ROOT
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

Check:
- names accurately reflect evidence strength;
- OBSERVED_LINKED_THREAD_ANCHOR is not falsely called canonical Telegram top root;
- SAME_ROOT_OBSERVATION cannot override conflicting stronger evidence;
- ISOLATED_UNRESOLVED cannot silently access existing history.

## R6. Minimal metadata / privacy

Review proposed additive nullable fields:

- inbound_reply_to_message_id
- inbound_reply_to_message_thread_id
- inbound_is_automatic_forward
- stable_conversation_root_id
- root_derivation_class
- root_evidence_update_id

Reuse existing:
- outbound_message_id
- returned_chat_id
- update/effect state
- current routing observations

Verify:
- sufficient for bounded root resolution;
- no unnecessary participant identity;
- no raw Update/full Message;
- no usernames/display names;
- no raw provider response;
- no nested reply-chain persistence.

If any proposed field is unnecessary or insufficient, state exact correction.

## R7. Fail-closed behavior

Independently stress-review:

1. unique eligible prior outbound -> inherit exact prior root;
2. unknown target -> no merge;
3. multiple/conflicting matches -> AMBIGUOUS, no provider/send until bounded policy resolves;
4. legacy row with no lineage -> no guessed merge;
5. cross-chat -> never merge;
6. direct-topic/mode conflict -> no merge;
7. different linked-post root -> no merge;
8. root/thread observation conflict with PROVEN lineage -> inherited project root may remain, but conflict must stay evidence;
9. send success + root/lineage persistence failure -> OUTCOME_UNKNOWN, no blind resend;
10. replay must reuse persisted deterministic root decision, not re-derive differently.

Check for any hidden path to wrong-history merge.

## R8. conversation_key / migration compatibility

Review proposed semantic cutover:

- historical tg-dialogue-r02 conversation_key values remain immutable evidence;
- old transcripts not rewritten;
- no synthetic legacy root backfill;
- new turns use versioned root-r01 semantics only after future implementation authority;
- optional legacy bridge requires separate evidence/authority.

Candidate new key:

SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)

Check whether:
- domain/version separation is sufficient;
- root ID itself must include mode/chat/anchor namespace;
- no user identity/text enters key;
- rollback/cross-version risks are adequately identified.

Do not design a full implementation; return only semantic defects/requirements if any.

## R9. Effect/replay ordering

Review conceptual ordering:

parse/admit
-> claim update
-> derive/persist root evidence
-> history selection
-> provider
-> durable SENDING
-> one Telegram send
-> bounded returned evidence validation
-> atomic transcript + outbound relation + root relation
-> COMMITTED/FALLBACK_COMMITTED

Verify:
- replay/effect ledger is not weakened;
- a possibly delivered effect cannot be resent after root persistence uncertainty;
- root derivation cannot occur after provider in a way that changes history selection nondeterministically.

## R10. Offline test matrix

Review T1-T16 from DESIGN.md.

Require at minimum:

- exact observed fixture shape without hard-coded IDs;
- direct reply to known outbound with changed message_thread_id inherits same stable root;
- reply to bot from another linked-post root does not merge wrong histories;
- unknown/ambiguous outbound lookup no merge;
- legacy rows no guessed merge;
- duplicate update no duplicate effect;
- post-send root persistence failure -> OUTCOME_UNKNOWN/no resend;
- cross-chat isolation;
- direct-topic/mode isolation;
- privacy;
- auto-forward root;
- forum vs linked-discussion namespace separation.

State if matrix is sufficient for a later implementation gate.

## Verdict

Return one immutable SIS review artifact to KOO.

Allowed terminals:

PASS_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

or

NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

If NEEDS_REWORK:
list only exact semantic/design defects and exact bounded correction scope.
Do not implement fixes.

If PASS:
state exact next gate:
KOD implementation candidate may be authorized only by a separate NEW exact task after fresh KOO reconciliation.

PASS is NOT:
- implementation authority;
- schema migration authority;
- install authority;
- service/live authority.

## Mandatory RETURN KOO

Return:
- official-source verification;
- project-evidence separation verdict;
- C5 semantic verdict;
- root-lineage guard verdict;
- metadata/privacy verdict;
- fail-closed verdict;
- migration/key verdict;
- replay/effect ordering verdict;
- T1-T16 matrix verdict;
- exact terminal;
- next bounded gate.

Then STOP.
