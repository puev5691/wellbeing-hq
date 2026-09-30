# Telegram linked-discussion conversation-root design r0.1

status: DESIGN_CANDIDATE_NOT_IMPLEMENTED
terminal: PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_READY_FOR_SIS_REVIEW
entity: KOD / КОДЕР
project_time: omitted

## 1. Human-readable result

The current tuple key `(chat_id, message_thread_id, direct_topic_id)` is not sufficient as the sole continuity identity for the exact linked-discussion Reply flow observed by SIS.

The selected successor design is **C5 HYBRID_FAIL_CLOSED**:

1. preserve an explicitly versioned project conversation root;
2. use an official/proven Telegram thread root when it is actually available as evidence;
3. for a direct Reply to a bot message, inherit the already-established root only when `reply_to_message.message_id` resolves uniquely to one prior committed outbound effect in the same chat/mode;
4. if root evidence is missing, conflicting, stale or non-unique, do not merge histories; create an isolated root or reject according to the bounded admission contract;
5. never treat the numeric equality observed in the fixture as a protocol rule.

This is a protocol/design candidate only. No runtime file, database, service, configuration, credential or live Telegram/OpenAI state was changed.

## 2. Exact task and project evidence

Exact task:

`puev5691/wellbeing-hq@a44bf9e3c439839684e358c006a85872cf938282:entities/koordinator/outbox/KOO__telegram-linked-discussion-conversation-root-design-r01__KOD.md`

blob:
`8d87ca543748f91c49bd42bc206297d470ac430d`

Current writer:

`puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:entities/koder/current/KOD__replacement-current-writer-v06.md`

blob:
`338f1bcf6f59b53356ea6fb20f2ac081af8cda7e`

Exact failure basis:

`puev5691/wellbeing-hq@d06ebe706473a0e96027322782c1b4f9b47e1ba8:entities/sisadmin/outbox/SIS__telegram-same-thread-two-turn-multiturn-r01-result__KOO.md`

blob:
`e513fc629ca02700571d7993080fa38ee567684e`

terminal:
`FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH`

Exact observed evidence:

Turn 1:
- chat_id = `-1002429106148`
- inbound_message_id = `111`
- message_thread_id = `110`
- direct_topic_id = `0`
- trigger_class = `command`
- conversation_key = `99db4a7a4b6f20d855cf770eebdad512de7804397f0f3f677712177b09c36bdd`
- outbound_message_id = `112`
- state = `COMMITTED`
- visible = YES

Turn 2:
- OPERATOR used Telegram Reply directly on exact visible bot reply from Turn 1
- chat_id = `-1002429106148`
- inbound_message_id = `114`
- message_thread_id = `112`
- direct_topic_id = `0`
- trigger_class = `reply-to-bot`
- conversation_key = `05553f46035a5bbf7a6acbad7c608c84391b49b30138aecc94c683557405c96e`
- outbound_message_id = `115`
- state = `COMMITTED`
- visible = YES

Project evidence classification:

- `110 -> outbound 112 -> Reply produces inbound thread 112` is **EXACT_PROJECT_EVIDENCE**.
- `112 == 112` is not promoted to Telegram semantics.
- Current runtime separated the turns exactly as its tuple-key contract requires.
- The defect is a continuity-model mismatch, not evidence of replay/effect corruption.

## 3. Official protocol source map

Only official Telegram sources are used for protocol semantics.

### S1 Bot API

Locator:
`https://core.telegram.org/bots/api`

OFFICIAL_PROTOCOL_FACT:
- `Message.message_id` is unique inside a chat.
- `Message.message_thread_id` is an optional unique identifier of a message thread or forum topic for supergroups/private chats.
- `Message.is_automatic_forward` is true when a channel post was automatically forwarded to the connected discussion group.
- `Message.reply_to_message` contains the original message for replies in the same chat and message thread.
- The nested `reply_to_message` does not recursively contain another `reply_to_message`.
- `sendMessage` returns a `Message` on success.
- Current Bot API documentation describes the `sendMessage.message_thread_id` parameter as a target forum/private-forum topic parameter.

Important absence:
- Bot API documentation does not expose MTProto `reply_to_top_id` or `top_msg_id` fields directly.

### S2 Discussion groups

Locator:
`https://core.telegram.org/api/discussion`

OFFICIAL_PROTOCOL_FACT:
- a channel can have a linked discussion supergroup;
- channel posts are automatically forwarded into the linked group;
- the comment section of a channel post is the message thread of that automatically forwarded channel-post message;
- that automatically forwarded message starts the comment section/thread;
- for replies in a comment section, MTProto `reply_to.reply_to_msg_id` identifies the direct replied message and `reply_to.reply_to_top_id` identifies the thread.

### S3 Message threads

Locator:
`https://core.telegram.org/api/threads`

OFFICIAL_PROTOCOL_FACT:
- replies to a message can create a thread whose ID is the top/root message ID;
- `reply_to_top_id` carries the thread ID;
- `reply_to_msg_id` can identify a direct reply target inside that thread;
- replies to messages inside an existing thread remain in that same thread and do not create nested threads;
- `top_msg_id` is used by MTProto operations to address the thread.

### S4 Forum topics

Locator:
`https://core.telegram.org/api/forum`

OFFICIAL_PROTOCOL_FACT:
- forum topics are a separate mode with explicit topic semantics;
- forum behavior must not be silently treated as linked-discussion behavior.

## 4. Fact / evidence / inference separation

### OFFICIAL_PROTOCOL_FACT

1. A linked-channel comment section is a message thread rooted at the automatically forwarded channel post in the discussion supergroup.
2. MTProto distinguishes the direct reply target (`reply_to_msg_id`) from the thread top/root (`reply_to_top_id`).
3. Replies within an existing thread do not create nested MTProto threads.
4. Bot API exposes `message_thread_id`, direct `reply_to_message`, and `is_automatic_forward`, but not `reply_to_top_id/top_msg_id` directly.
5. Bot API's direct reply object is intentionally one hop deep.

### EXACT_PROJECT_EVIDENCE

1. Turn 1 inbound `message_thread_id=110`.
2. Turn 1 bot outbound `message_id=112`.
3. OPERATOR replied directly to visible bot message 112.
4. Turn 2 inbound `message_thread_id=112`.
5. Current tuple-derived conversation keys differ.
6. Both bot replies were visible.
7. Turn 1 returned outbound routing fields did not include a returned thread ID.

### DESIGN_INFERENCE

1. A project conversation root must be distinct from merely trusting each inbound Bot API `message_thread_id`.
2. A direct reply to a uniquely known bot outbound effect can safely inherit that outbound effect's project conversation root when same-chat/mode guards pass.
3. The exact `112 == 112` relation is useful only as a lookup fixture, never as a general semantic rule.
4. In linked discussion, a Bot API `message_thread_id` may be used as an initial bounded root anchor, but the design must not claim it is always identical to MTProto `reply_to_top_id` unless that identity is independently proven.

## 5. D1: linked-discussion root semantics

### Stable Telegram semantic root

At MTProto level, the stable thread root is the top message ID (`reply_to_top_id/top_msg_id`). For a channel comment section, that top/root message is the auto-forwarded copy of the channel post in the linked discussion supergroup.

### Bot API availability

Bot API does not expose `reply_to_top_id/top_msg_id` directly.

Bot API can provide bounded evidence through:
- current `message_thread_id`;
- direct `reply_to_message.message_id`;
- optional `reply_to_message.message_thread_id`;
- `is_automatic_forward`;
- returned outbound `message_id`;
- the local durable mapping from a returned outbound message ID to the root under which it was created.

Therefore Bot API is sufficient for a **bounded fail-closed project root resolver**, but not sufficient to claim that every linked-discussion event exposes the canonical MTProto top root directly.

## 6. D2: exact Turn 1 / Turn 2 interpretation

The official MTProto thread documentation says that replying to a message inside a thread remains in the same thread and does not create a nested thread.

Therefore the observed Bot API transition from inbound `message_thread_id=110` to `message_thread_id=112` cannot safely be interpreted as proof that Telegram's canonical discussion root changed from 110 to 112.

Possible explanations remain:

1. Bot API projection semantics for this linked-discussion path differ from the canonical MTProto `reply_to_top_id`;
2. the existing bot send path passed `message_thread_id` in a context where current Bot API documentation only promises that parameter for forum/private-forum topics;
3. returned outbound routing metadata was insufficient to prove where Telegram considered the bot message rooted;
4. another linked-discussion/Bot API representation detail not documented in the cited official sources applies.

Classification:
`EXACT_CAUSE = UNKNOWN`.

The design does not require choosing among those explanations.

## 7. D3: candidate comparison

### C1 CURRENT: (chat_id, message_thread_id, direct_topic_id)

Determinism: HIGH.
Bot API availability: HIGH.
Privacy cost: LOW.
Replay safety: compatible with existing ledger.
Ambiguity risk: HIGH for the exact linked-discussion flow.
Cross-thread contamination risk: LOW, but false separation is proven.
Migration complexity: LOW.
Private/direct compatibility: current behavior.
Linked discussion: FAIL on exact evidence.
Forum/direct-topic compatibility: useful only as mode-specific tuple, not universal semantic root.

Decision:
REJECT as sole conversation root.

### C2 REPLY_ROOT: derive from reply_to_message lineage

Determinism: MEDIUM.
Bot API availability: one-hop direct target only.
Privacy cost: LOW.
Replay safety: GOOD if joined only to durable prior effects.
Ambiguity risk: MEDIUM/HIGH if the replied message is not a known bot effect.
Cross-thread contamination risk: requires strong same-chat guard.
Migration complexity: MEDIUM.
Private/direct compatibility: possible.
Linked discussion: useful for direct replies to known bot messages.
Forum/direct-topic: must remain mode-separated.

Critical limitation:
Bot API does not recursively expose arbitrary reply ancestry, so generic lineage walking cannot be reconstructed from one incoming Message alone.

Decision:
USE only as a proven bounded inheritance mechanism, not as the entire root model.

### C3 LINKED_DISCUSSION_TOP_ROOT

Determinism: IDEALLY HIGH.
Canonical protocol semantics: HIGH at MTProto layer.
Bot API availability: INCOMPLETE.
Privacy cost: LOW.
Replay/collision safety: HIGH if exact root is proven.
Ambiguity risk: LOW when auto-forward/top-root evidence exists, otherwise UNKNOWN.
Migration complexity: MEDIUM.
Linked discussion: semantically correct target.
Forum/private modes: must not be conflated.

Decision:
USE when exact top/root evidence is actually available; do not invent it when Bot API lacks proof.

### C4 EXPLICIT_SESSION_ANCHOR THROUGH PRIOR OUTBOUND EFFECT

Determinism: HIGH for a direct reply to a uniquely persisted bot outbound.
Bot API availability: HIGH for `reply_to_message.message_id`.
Privacy cost: LOW.
Replay safety: HIGH if only COMMITTED/FALLBACK_COMMITTED effect rows are eligible.
Ambiguity risk: LOW under unique same-chat lookup.
Cross-thread contamination risk: LOW with chat/mode/root guards.
Migration complexity: MEDIUM.
Linked discussion: directly addresses exact failure mode.
Private/direct: compatible if mode-scoped.
Forum/direct-topic: requires separate namespace/guards.

Decision:
ACCEPT as bounded continuity mechanism.

### C5 HYBRID_FAIL_CLOSED

Composition:
- canonical/proven top-root evidence when available;
- otherwise established project root from a bounded initial thread observation;
- exact reply-to-known-outbound inheritance;
- fail-closed isolation on ambiguity.

Determinism: HIGH.
Bot API availability: sufficient for bounded behavior.
Privacy cost: LOW.
Replay safety: preserves current ledger ordering.
Ambiguity risk: LOW because ambiguity never causes merge.
Cross-thread contamination risk: lowest among usable candidates.
Migration complexity: MEDIUM and additive.
Mode compatibility: explicit, namespaced, no forum/direct conflation.

Decision:
**SELECTED DESIGN CANDIDATE.**

## 8. D4: root derivation contract

The future resolver operates only after current admission has accepted the inbound event and before provider/history selection.

Define a versioned semantic domain:

`TG-CONVERSATION-ROOT-R01`

The stable root key is a hash over a canonical, mode-separated root descriptor. It is not a raw Telegram identity and it is not derived from participant identity.

### Root derivation classes

#### R1 PROVEN_AUTO_FORWARD_ROOT

Conditions:
- configured mode is linked discussion;
- inbound message has `is_automatic_forward=true`;
- current chat is the configured linked discussion chat;
- inbound message ID is valid.

Root anchor:
`(mode=linked_discussion, chat_id, auto_forward_message_id)`.

Semantics:
officially supported root evidence because the auto-forwarded post starts the comment thread.

#### R2 OBSERVED_LINKED_THREAD_ANCHOR

Conditions:
- linked-discussion mode is positively known from configuration/task scope;
- no prior outbound lineage applies;
- inbound `message_thread_id` is present and valid;
- no conflicting root evidence exists.

Root anchor:
`(mode=linked_discussion, chat_id, observed_message_thread_id)`.

Semantics:
project session anchor only.
It MUST NOT be labelled as proven MTProto `reply_to_top_id`.

Purpose:
establish a deterministic first root for new linked-discussion traffic while preserving evidence that the anchor came from Bot API `message_thread_id`.

#### R3 PROVEN_OUTBOUND_LINEAGE

Conditions:
- inbound is an admitted reply-to-bot;
- `reply_to_message.message_id` is present;
- lookup by `(current_chat_id, reply_target_message_id)` finds exactly one prior outbound effect;
- prior row state is `COMMITTED` or `FALLBACK_COMMITTED`;
- prior row has a non-null stable root;
- prior returned chat equals current chat;
- mode is identical;
- direct-topic/mode-specific guards do not conflict.

Action:
inherit the prior stable root exactly.
Do not recompute root from current `message_thread_id`.

The exact fixture is handled by this rule:
the second turn's direct reply target resolves to the previously persisted outbound effect, so it inherits Turn 1's root regardless of the new observed thread ID.

#### R4 SAME_ROOT_OBSERVATION

Conditions:
- current linked-discussion `message_thread_id` exactly matches an already-established root anchor in the same chat/mode;
- no conflicting evidence exists.

Action:
reuse that root.

#### R5 ISOLATED_UNRESOLVED

Conditions:
any required proof is missing, ambiguous, conflicting or legacy-incomplete.

Action:
never join an existing history.
Derive a one-event isolated root from:
`(mode, chat_id, inbound_message_id)`
or reject before provider according to the later implementation policy.

This is fail-closed with respect to history merging.

## 9. PROVEN / AMBIGUOUS / UNAVAILABLE

### PROVEN

A mapping is PROVEN only if one of these holds:

- the event is the auto-forwarded linked-discussion root itself; or
- the event's direct reply target uniquely resolves to one prior committed bot outbound effect carrying a stable root, under same-chat and same-mode guards; or
- an exact already-established root anchor equals the current same-mode thread observation without contradiction.

### AMBIGUOUS

Examples:
- reply target matches multiple prior effect rows;
- prior effect rows disagree on root;
- current chat/mode differs;
- root lineage conflicts with direct-topic mode boundary;
- multiple possible legacy roots exist;
- the root candidate would require assuming undocumented `112==112`-style semantics.

Behavior:
no merge.

### UNAVAILABLE

Examples:
- no reply target;
- target is not a known prior bot effect and no stable root evidence is present;
- legacy row lacks root metadata;
- Bot API omits fields needed for a proof.

Behavior:
no merge; isolate or reject.

## 10. Multi-hop lineage

Generic multi-hop walking is NOT required and should not be introduced in r0.1.

Reason:
Bot API's nested `reply_to_message` is intentionally non-recursive.

For the current bounded visitor-dialogue contract, one-hop lookup is sufficient when the visitor replies directly to a bot outbound message because the durable prior outbound row already carries the originating stable root.

If a future task requires arbitrary replies to arbitrary human messages across a long thread, that is a different protocol capability and requires separate authority/evidence.

## 11. D5: minimal privacy-safe metadata proposal

Future schema candidate, all nullable/additive:

1. `inbound_reply_to_message_id INTEGER`
   - justified: exact direct reply target needed for bounded lineage join.

2. `inbound_reply_to_message_thread_id INTEGER`
   - justified: bounded routing evidence/diagnostic; may help detect contradictions.
   - not sufficient by itself as canonical root.

3. `inbound_is_automatic_forward INTEGER`
   - justified: distinguishes official linked-discussion root messages.

4. `stable_conversation_root_id TEXT`
   - justified: versioned hashed project root used for history continuity.
   - contains no user identity/text.

5. `root_derivation_class TEXT`
   - bounded enum describing why the root is trusted:
     `PROVEN_AUTO_FORWARD_ROOT`,
     `OBSERVED_LINKED_THREAD_ANCHOR`,
     `PROVEN_OUTBOUND_LINEAGE`,
     `SAME_ROOT_OBSERVATION`,
     `ISOLATED_UNRESOLVED`.

6. `root_evidence_update_id INTEGER`
   - justified: local bounded evidence pointer to the root-establishing/lineage row.
   - no free-form/raw payload.

Reuse existing:
- `outbound_message_id`;
- `returned_chat_id`;
- state;
- update_id;
- existing message/thread/direct-topic observations.

No new participant identity is required.

### Outbound effect -> root relation

A prior outbound effect is eligible for reply lineage only when:
- `outbound_message_id IS NOT NULL`;
- `returned_chat_id = current chat_id`;
- state is `COMMITTED` or `FALLBACK_COMMITTED`;
- `stable_conversation_root_id IS NOT NULL`.

Lookup must return exactly one row.

A future migration may add a partial uniqueness/index constraint over `(returned_chat_id, outbound_message_id)` only after a preflight proves existing data compatible. The design does not assume such a constraint already exists.

### Explicitly forbidden persistence

Do not persist:
- raw Update JSON;
- full Message;
- username/display name;
- unrelated user/chat identities;
- raw provider response;
- nested raw reply objects;
- arbitrary reply-chain snapshots.

## 12. Conversation key / transcript semantics

Historical `conversation_key` values are immutable evidence and MUST NOT be rewritten.

For a future implementation after independent review:

- old rows retain tuple-derived `tg-dialogue-r02` keys unchanged;
- new turns after the semantic cutover use a new versioned root-derived key domain;
- `stable_conversation_root_id` is the authoritative continuity input for new turns;
- no legacy transcript is silently attached to a new root;
- a historical transcript can be associated only by a separate exact evidence-driven migration decision.

Recommended new key construction:

`SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)`

The root ID itself is derived from a canonical mode/chat/anchor descriptor with a distinct domain separator.

No user ID, username, display name or message text participates in the root key.

## 13. D6: fail-closed state rules

### Known unique reply target

If direct reply target maps uniquely to one eligible prior outbound effect:
- inherit stable root;
- record `PROVEN_OUTBOUND_LINEAGE`;
- proceed under existing replay/effect ledger.

### Unknown reply target

If no eligible prior outbound effect exists:
- do not search/guess historical roots;
- use `ISOLATED_UNRESOLVED` or reject per implementation policy;
- do not merge.

### Multiple roots / duplicate relation

If lookup yields multiple eligible rows or conflicting roots:
- classify AMBIGUOUS;
- do not merge;
- no provider/send effect until ambiguity policy is satisfied.

### Linked root cannot be proven

Use bounded observed anchor for a new session only if the event itself provides a valid mode-scoped `message_thread_id` and no conflict exists.
Otherwise isolate.

### Legacy rows lack lineage metadata

No backfill from guessed tuple similarity.
Legacy row is not eligible for outbound-root inheritance unless its exact root was independently materialized by a separately authorized migration.

### Duplicate update replay

Existing request-digest/update claim logic remains authoritative:
- same update and digest -> no second provider/send effect;
- conflict -> fail;
- unresolved effect -> reconciliation required.

Root derivation must be deterministic and persisted with the claim/turn state so replay cannot choose a different root.

### Send committed but root/lineage persistence fails

Preserve existing behavior:
`OUTCOME_UNKNOWN`.

No blind resend.
No second provider call.
No attempt to fabricate root metadata after the fact.

### Root candidate conflicts with current thread tuple

If exact direct outbound lineage is PROVEN under same-chat/mode guards:
- inherited project root may remain authoritative;
- record the current thread observation as conflicting evidence;
- do not reinterpret numeric thread IDs as root semantics.

If lineage is not PROVEN:
- no merge.

### Chat changes

Never inherit root across chat IDs.

### direct_topic_id changes

Never merge across direct-topic identities unless a future mode-specific contract explicitly proves equivalence.
Linked-discussion r0.1 treats nonzero direct-topic mode as a separate namespace.

### Different channel-post comment root

Never merge.
A known auto-forward/root anchor or a proven prior root mismatch causes separation.

## 14. Replay/effect safety ordering

The existing safety ordering remains conceptually intact:

1. parse/admit bounded inbound;
2. claim update using existing digest/collision semantics;
3. derive/persist root evidence before history/provider selection;
4. select history only by the resolved new root key;
5. provider call;
6. durable SENDING state;
7. one Telegram send;
8. validate returned bounded evidence;
9. atomically persist transcript + outbound message relation + root relation;
10. COMMITTED/FALLBACK_COMMITTED.

If step 8/9 fails after a successful send:
`OUTCOME_UNKNOWN`.

The root resolver must not create a path that resends an effect already possibly delivered.

## 15. D7: migration compatibility plan

Design only; no migration performed.

### Phase M0 preflight

- exact DB identity/integrity;
- unresolved/OUTCOME_UNKNOWN inventory;
- duplicate `(returned_chat_id,outbound_message_id)` scan;
- schema/version check;
- current committed-history readback.

Any conflict blocks migration.

### Phase M1 additive schema

Add only nullable root/lineage columns listed above.

Do not rewrite:
- old `conversation_key`;
- old transcript messages;
- old routing observations;
- effect states.

### Phase M2 semantic cutover

Only newly accepted turns receive root-r01 semantics.

Legacy rows:
- new fields remain NULL;
- remain historical evidence;
- are not guessed into a new root.

### Phase M3 optional evidence-driven bridge

Not part of this candidate.

If later exact evidence proves a mapping from a historical tuple key to a root, a separate authorized migration may record that mapping without rewriting the historical key.

No silent history merge.

### Rollback boundary

Because M1 is additive and M2 affects only new rows, rollback means disabling root-r01 selection and returning to the previous binary/runtime only if no unsafe cross-version state was created. Exact rollback conditions must be independently reviewed before implementation authorization.

## 16. D8: offline test matrix

All tests use fake transport, synthetic IDs and no Telegram/OpenAI calls.

### T1 Initial linked-discussion command establishes root

Given:
- linked-discussion mode;
- valid inbound thread observation;
- no prior lineage.

Expect:
- deterministic new root;
- derivation `OBSERVED_LINKED_THREAD_ANCHOR`;
- exactly one conversation history.

### T2 Direct Reply to bot reply with changed message_thread_id

Given:
- Turn 1 establishes root A;
- Turn 1 committed bot outbound message B;
- Turn 2 is admitted reply-to-bot;
- Turn 2 `reply_to_message.message_id=B`;
- Turn 2 observed `message_thread_id != Turn1 message_thread_id`.

Expect:
- unique prior outbound lookup;
- root A inherited;
- no new history;
- derivation `PROVEN_OUTBOUND_LINEAGE`.

No assertion may depend on B numerically equalling Turn 2 thread ID.

### T3 Reply within original thread without replying to bot

Given current observed thread matches an existing same-chat root anchor.

Expect:
same stable root only when exact root-anchor evidence proves it.

Otherwise isolate.

### T4 Reply to bot message from another linked-post comment root

Given direct reply target resolves to root B while current session/root candidate is A.

Expect:
root B only if direct target relation is valid and same-chat/mode;
must never merge A and B histories.

### T5 Unknown reply target

No eligible outbound effect row.

Expect:
`ISOLATED_UNRESOLVED` or rejection;
no merge;
no historical search by guessed numeric similarity.

### T6 Legacy row without lineage fields

Expect:
no guessed root;
no guessed merge;
legacy conversation_key unchanged.

### T7 Duplicate update replay

Same update/digest twice.

Expect:
one provider effect maximum;
one send effect maximum;
same persisted root decision;
no duplicate transcript.

### T8 Send succeeded but lineage/root persistence failed

Expect:
`OUTCOME_UNKNOWN`;
no blind resend;
replay requires manual reconciliation.

### T9 Cross-chat

Same numeric message/thread/reply IDs in different chats.

Expect:
never merge.

### T10 direct_topic change

Same chat but different direct_topic identity/mode.

Expect:
separate unless a separately approved mode contract proves equivalence.

### T11 Privacy

Inject raw Update with username/display name/text/provider response markers.

Expect:
root metadata contains none of those;
no raw Update/full Message stored;
only bounded scalar projection persisted.

### T12 Exact observed fixture shape

Parameterize symbols rather than hard-coded values:

- initial thread = A;
- bot outbound = B;
- direct visitor reply target = B;
- visitor's next observed thread = B;
- A != B.

Expect:
Turn 2 root equals Turn 1 root because of unique outbound lineage.
Test MUST NOT assert that `thread=B` means B is the Telegram top root.

### T13 Ambiguous outbound lookup

Two eligible prior rows match same chat/outbound ID.

Expect:
AMBIGUOUS;
no merge;
no provider/send.

### T14 Thread observation conflict without proven lineage

Current thread differs from known root and no unique outbound relation exists.

Expect:
isolated/rejected;
no merge.

### T15 Automatic-forward root

Inbound `is_automatic_forward=true`.

Expect:
root anchored to its own message ID under linked-discussion mode;
derivation `PROVEN_AUTO_FORWARD_ROOT`.

### T16 Forum contrast

Forum-topic fixture and linked-discussion fixture reuse numeric IDs.

Expect:
mode namespaces prevent merge;
forum-specific semantics are not imported into linked discussion.

## 17. Expected fixture behavior after future implementation

For the project fixture shape:

Turn 1:
- establish project root R from the accepted linked-discussion first-turn evidence;
- send bot response;
- persist `outbound_message_id=B -> root R`.

Turn 2:
- receive direct reply with `reply_to_message.message_id=B`;
- current observed `message_thread_id` may differ from Turn 1;
- resolve exactly one prior outbound B in same chat/mode;
- inherit R;
- history lookup uses R;
- current raw thread observation remains diagnostic evidence, not the continuity key.

This makes the observed conversation continuous because of a durable causal relation, not because any numeric equality was hard-coded.

## 18. What remains UNKNOWN

1. Whether Bot API `message_thread_id` for every linked-discussion comment is guaranteed to equal MTProto `reply_to_top_id`.
2. Why the exact second inbound event exposed `message_thread_id` equal to the prior bot outbound message ID.
3. Whether passing `sendMessage.message_thread_id` in this non-forum linked-discussion path has defined routing semantics beyond what current Bot API documentation states.
4. Why the successful bot send returned no `message_thread_id` in the exact live evidence.
5. Whether other Telegram clients/actions can produce additional linked-discussion Bot API projections not covered by the exact fixture.

None of these unknowns is filled by assumption.

## 19. Review notes / independent SIS gate

SIS should independently verify:

1. official-source fact map;
2. absence of unsupported claim that Bot API exposes `reply_to_top_id`;
3. same-chat/mode guards for outbound lineage;
4. one-hop sufficiency for the bounded direct-reply contract;
5. no cross-root merge path;
6. replay/effect ordering and `OUTCOME_UNKNOWN`;
7. additive/no-backfill migration;
8. privacy-minimal field set;
9. T1-T16 matrix, especially T2/T12 without ID hard-coding;
10. semantic distinction between linked discussion and forum topics.

SIS review must not install, start services, call Telegram/OpenAI, mutate DB/config/credentials, or replay the failed live task.

## 20. Boundary

Implementation:
NOT_PERFORMED

DB schema mutation:
NOT_PERFORMED

dialogue_mvp.py mutation:
NOT_PERFORMED

install/service start:
NOT_PERFORMED

Telegram/OpenAI calls:
0

credential/config/allowlist mutation:
NOT_PERFORMED

live task replay:
NOT_PERFORMED

approval_status:
DESIGN_CANDIDATE_NOT_IMPLEMENTED

exact_next_gate:
SIS independent semantic/design review only

terminal:
PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_READY_FOR_SIS_REVIEW
