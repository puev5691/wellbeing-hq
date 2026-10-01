# Conversation-root r0.1 semantics

status: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Ordering

parse/admit -> claim -> persist deterministic root decision -> history by root key -> provider -> SENDING -> one send -> bounded returned evidence -> atomic transcript/outbound/root relation -> COMMITTED/FALLBACK_COMMITTED.

Post-send persistence failure -> OUTCOME_UNKNOWN; replay does not resend.

## Root rules

Initial admitted linked-discussion human turn with valid observed message_thread_id and no stronger evidence:
OBSERVED_LINKED_THREAD_ANCHOR.

Direct reply-to-bot:
reply_to_message.message_id -> exact same-chat prior outbound_message_id -> exactly one COMMITTED/FALLBACK_COMMITTED row -> same mode/direct-topic -> non-null stable root -> PROVEN_OUTBOUND_LINEAGE.

Zero, multiple, conflicting, legacy-null or otherwise unproven lineage:
ISOLATED_UNRESOLVED; no history merge.

Exact same chat/mode/anchor with one unconflicted established root:
SAME_ROOT_OBSERVATION.

No fuzzy lookup. No inference from numeric equality between outbound ID and observed thread ID.

## D1 boundary

is_automatic_forward=true is explicitly ignored before claim/root/history/provider/send. It is not persisted and is not a root input. Normal tester admission is not widened.

## Privacy

Persist only bounded scalar routing/root metadata. No raw Update, full Message, username/display name, nested raw reply chain, raw provider response or credentials.

## Fixture

Parameterized A/B fixture:
Turn1 thread=A; bot outbound=B; Turn2 reply target=B; Turn2 observed thread=B; A != B.
Expected: PROVEN_OUTBOUND_LINEAGE, same stable root, same root-r0.1 conversation key, Turn2 receives Turn1 history. The test does not treat B==thread as Telegram semantics.

## I1 correction: raw relation cardinality before eligibility

For an admitted `reply-to-bot` turn, lineage resolution performs exactly one raw SQL read inside the already-open `BEGIN IMMEDIATE` root-resolution transaction:

`SELECT update_id,state,direct_topic_id,stable_conversation_root_id,root_conversation_key FROM updates WHERE returned_chat_id=? AND outbound_message_id=?`

No state/root/mode/direct-topic eligibility predicate is present in that query.

The returned row list itself is the cardinality evidence:
- 0 rows -> `ISOLATED_UNRESOLVED`, no history merge;
- >1 rows -> ambiguous -> `ISOLATED_UNRESOLVED`, no history merge;
- exactly 1 row -> and only then check state, non-null stable root/root key, same mode and exact direct-topic boundary.

Only a unique eligible row yields `PROVEN_OUTBOUND_LINEAGE`.

Because the raw read and eligibility decision occur inside the same `BEGIN IMMEDIATE` transaction and use the single returned rowset, there is no separate count/select TOCTOU window.
