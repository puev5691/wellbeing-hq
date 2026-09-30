# KOO -> KOD: Telegram linked-discussion conversation-root semantics design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact failure basis

puev5691/wellbeing-hq@d06ebe706473a0e96027322782c1b4f9b47e1ba8:
entities/sisadmin/outbox/SIS__telegram-same-thread-two-turn-multiturn-r01-result__KOO.md

blob:
e513fc629ca02700571d7993080fa38ee567684e

terminal:
FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH

### Exact observed protocol evidence

Turn 1:
- update_id=560511156
- inbound_message_id=111
- message_thread_id=110
- direct_topic_id=0
- trigger_class=command
- conversation_key=99db4a7a4b6f20d855cf770eebdad512de7804397f0f3f677712177b09c36bdd
- outbound_message_id=112
- state=COMMITTED
- TURN1_REPLY_VISIBLE=YES

Turn 2:
- OPERATOR used Telegram Reply directly on exact visible Turn 1 bot reply
- update_id=560511158
- inbound_message_id=114
- message_thread_id=112
- direct_topic_id=0
- trigger_class=reply-to-bot
- conversation_key=05553f46035a5bbf7a6acbad7c608c84391b49b30138aecc94c683557405c96e
- outbound_message_id=115
- state=COMMITTED
- TURN2_REPLY_VISIBLE=YES

Critical:
TURN1_INBOUND_TUPLE=(-1002429106148,110,0)
TURN2_INBOUND_TUPLE=(-1002429106148,112,0)

INBOUND_TUPLE_EQUAL=NO
CONVERSATION_KEY_EQUAL=NO

Observed exact numeric relation:
Turn1 outbound_message_id=112
Turn2 message_thread_id=112

This numeric equality is evidence only.
Do NOT infer Telegram semantics from it without official-source support.

## Current runtime semantics

Installed/reviewed runtime currently derives:

conversation_key =
SHA256(
  "tg-dialogue-r02\0"
  + chat_id
  + "\0"
  + message_thread_id
  + "\0"
  + direct_topic_id
)

This behavior is internally consistent with current code but failed to preserve visible conversational continuity in the exact linked-discussion Reply flow above.

## Official Telegram sources to use

Use official Telegram sources only for protocol semantics in this task.

Primary sources:

1. Bot API — Message / sendMessage:
https://core.telegram.org/bots/api

Relevant facts to verify:
- Message.message_thread_id semantics;
- Message.reply_to_message semantics;
- is_automatic_forward;
- sendMessage message_thread_id behavior;
- returned Message optional routing fields.

2. Discussion groups:
https://core.telegram.org/api/discussion

Relevant facts to verify:
- channel post comments map to a message thread in linked discussion supergroup;
- auto-forwarded channel post starts the comment section/thread;
- thread-root semantics;
- reply_to_top_id/top_msg_id relation.

3. Message threads:
https://core.telegram.org/api/threads

Relevant facts to verify:
- thread root/top message semantics;
- reply_to_msg_id vs reply_to_top_id;
- replies within a thread stay in that thread;
- no nested thread assumption where applicable.

4. Forum topics, only for contrast/applicability:
https://core.telegram.org/api/forum

Do not treat forum-topic behavior as linked-discussion behavior unless exact applicability is proven.

## Goal

Produce a design/review candidate for stable conversational continuity in Telegram linked-channel discussion comments.

This task is DESIGN / PROTOCOL REVIEW ONLY.

NO runtime code change.
NO schema migration.
NO installation.
NO live test.
NO Telegram/OpenAI calls.

## Questions to answer

### D1. Exact Telegram semantics

Establish from official sources:

- what message_thread_id means in Bot API for this kind of supergroup message;
- how linked-channel comment sections are represented;
- what constitutes the stable thread/comment root;
- relation among:
  - message_id
  - message_thread_id
  - reply_to_message.message_id
  - reply_to_message.message_thread_id
  - reply_to_top_id / top_msg_id at MTProto layer
  - auto-forwarded channel-post message
- whether Bot API directly exposes enough data to recover stable linked-discussion root;
- where semantics remain undocumented/ambiguous.

Separate:
OFFICIAL_PROTOCOL_FACT
from
EXACT_PROJECT_EVIDENCE
from
DESIGN_INFERENCE.

### D2. Explain exact observed Turn 1 / Turn 2 behavior

Using only official semantics + project evidence, explain candidate causes for:

Turn 1:
inbound message_thread_id=110

Turn 1 bot reply:
outbound_message_id=112

Turn 2:
Reply directly on bot message 112
inbound message_thread_id=112

Determine whether this is:
- expected Bot API representation;
- a linked-discussion special case;
- an artifact of how sendMessage was invoked;
- a mismatch between Bot API message_thread_id and stable discussion root;
- or still UNKNOWN.

Do not promote the observed 112=112 coincidence beyond evidence.

### D3. Stable conversation-root candidates

Compare candidate continuity models.

At minimum evaluate:

C1 CURRENT:
(chat_id, message_thread_id, direct_topic_id)

C2 REPLY_ROOT:
derive root from reply_to_message lineage

C3 LINKED_DISCUSSION_TOP_ROOT:
derive stable root corresponding to reply_to_top_id/top_msg_id / auto-forwarded channel-post thread root

C4 EXPLICIT_SESSION_ANCHOR:
once Turn 1 establishes a stable root, map later reply-to-bot events to that proven root through persisted bounded lineage

C5 HYBRID_FAIL_CLOSED:
use proven stable root when derivable; otherwise isolate/UNKNOWN rather than merge.

For each candidate assess:
- determinism;
- Bot API data availability;
- privacy cost;
- replay/collision safety;
- ambiguity risk;
- cross-thread contamination risk;
- migration complexity;
- compatibility with direct bot private chat;
- compatibility with linked discussion;
- compatibility with future forum/direct-topic modes without accidental conflation.

Do NOT select a model merely because it makes current example pass.

### D4. Reply-lineage derivation

Determine whether a Turn 2 reply can safely map back to Turn 1 conversation using available Telegram fields.

Evaluate minimally:
- reply_to_message.message_id;
- reply_to_message.message_thread_id;
- whether replied bot message can be joined to prior outbound_message_id;
- whether that prior outbound row can safely resolve to its conversation/root;
- whether multi-hop reply lineage needs walking;
- whether one-hop mapping is sufficient under current bounded visitor-dialogue contract.

Define exact conditions under which mapping is:
PROVEN
AMBIGUOUS
UNAVAILABLE

If ambiguous/unavailable:
fail closed.
Do not merge histories.

### D5. Minimal privacy-safe metadata

Specify only metadata necessary for safe root resolution.

Candidate fields to consider, not automatically approve:
- inbound_reply_to_message_id
- inbound_reply_to_message_thread_id
- inbound_is_automatic_forward
- stable_conversation_root_id
- root_derivation_class
- root_derivation_evidence/update reference
- relation from outbound_message_id to originating conversation/root

Do NOT propose persistence of:
- raw Update JSON;
- full Message;
- usernames/display names;
- unrelated participant identities;
- raw dialogue text beyond current bounded transcript contract;
- raw provider response.

### D6. Fail-closed rules

Define exact behavior for:

- reply target known and uniquely linked to one prior outbound effect;
- reply target unknown;
- reply target maps to multiple roots;
- linked-discussion root cannot be proven;
- stale/legacy rows lack lineage metadata;
- replay of same update;
- outbound send committed but lineage persistence fails;
- root candidate conflicts with current thread tuple;
- chat changes;
- direct_topic_id changes;
- message belongs to a different channel-post comment root.

No silent merge.

### D7. Migration / compatibility

Assess impact of any future root model on existing DB/history.

Must preserve:
- current committed transcripts;
- replay/effect ledger semantics;
- OUTCOME_UNKNOWN behavior;
- old conversation_key values as immutable historical evidence;
- no synthetic backfill of unknown historical roots.

Design migration strategy only.

Possible acceptable pattern:
- introduce a new conversation_root_key / semantic version for new turns;
- keep legacy conversation_key unchanged for old rows;
- no retroactive merge unless exact evidence proves mapping.

Do not implement.

### D8. Offline test matrix before code authorization

Design a sufficient test matrix.

Include at minimum:

T1 initial linked-discussion command establishes root.

T2 Reply directly to bot reply:
new message_thread_id differs,
but proven reply lineage maps to same stable root.

T3 reply within same original thread without replying to bot:
same stable root if exact root evidence proves it.

T4 reply to bot message from another linked-post comment thread:
must not merge.

T5 unknown reply target:
fail closed / isolated / UNKNOWN.

T6 legacy row without lineage fields:
no guessed merge.

T7 duplicate update replay:
no duplicate provider/send effect.

T8 send succeeded but lineage/root persistence failed:
OUTCOME_UNKNOWN / no blind resend.

T9 cross-chat:
never merge.

T10 direct_topic change:
separate unless exact mode-specific contract proves otherwise.

T11 privacy:
no raw Update/full Message/name persistence.

T12 current exact observed 110 -> outbound 112 -> reply thread 112 fixture:
candidate design should explain expected root result without hard-coding IDs.

### D9. Recommended bounded successor

Return ONE recommended design candidate for later independent SIS verification.

The result must state:
- selected continuity-root semantics;
- exact evidence requirements;
- minimal schema additions;
- fail-closed rules;
- migration strategy;
- offline tests;
- what remains UNKNOWN.

Do NOT implement code.

## Output package

Produce one immutable design candidate artifact/package, e.g.:

entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/

Status:
DESIGN_CANDIDATE_NOT_IMPLEMENTED

Include:
- protocol-source map;
- exact project evidence map;
- candidate comparison;
- recommended root contract;
- schema proposal;
- fail-closed state transitions;
- migration compatibility plan;
- offline test matrix;
- review notes.

## Boundaries

Do NOT:
- change dialogue_mvp.py;
- change DB schema;
- install anything;
- start service;
- call Telegram;
- call OpenAI;
- mutate allowlist/config/credentials;
- create live authority;
- replay failed live task;
- claim official Telegram semantics not present in official sources.

## Expected terminal

PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_READY_FOR_SIS_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact current runtime/evidence basis;
- official source locators;
- fact/inference separation;
- comparison of root candidates;
- selected design candidate;
- minimal metadata;
- fail-closed behavior;
- migration plan;
- offline tests;
- DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- exact next gate:
  SIS independent semantic/design review only.

Then STOP.
