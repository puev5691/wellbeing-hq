# Telegram routing observability r0.1

Status: `CANDIDATE_NOT_INSTALLED`.

This is a minimal, privacy-safe successor of the accepted discussion runtime. It closes the evidence gap exposed by the bounded live pilot: after an admitted update and a successful `sendMessage`, the runtime can preserve the exact inbound route and a bounded projection of the returned Telegram `Message`. It does not claim that any reply was visible in the Telegram UI.

No service was installed or started while this package was built. No Telegram or OpenAI call, credential read, host mutation, allowlist change, provider/model change, or live replay occurred.

## Exact lineage

- Task: `puev5691/wellbeing-hq@90b175bd299ea377350faa347307ff10a47b3b9e:entities/koordinator/outbox/KOO__telegram-routing-observability-r01__KOD.md`, blob `09ca88739b067a29174925d84923ff4c96c6629a`.
- Predecessor source: `puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/dialogue_mvp.py`, blob `0ea2cb8c9fe4872bfbfd1ec348ba23bfa9dbce6d`.
- Live blocker: `BLOCKED_SIS_TELEGRAM_SAME_THREAD_LIVE_R03_REPLY_VISIBILITY_NOT_CONFIRMED`.
- Diagnostic: `PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01`.
- Current writer basis: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`.

## Preserved behavior

The following predecessor semantics are unchanged:

- exact linked-discussion admission, tester allowlist and long polling;
- explicit trigger requirement;
- provider `OpenAI`, model and request shape;
- multi-turn transcript bounds and thread/topic isolation;
- update replay/collision behavior;
- systemd credential mechanism;
- conversation key:

```text
SHA256(
  "tg-dialogue-r02\0"
  + chat_id
  + "\0"
  + message_thread_id
  + "\0"
  + direct_topic_id
)
```

The package does not add a new admission route and does not set `reply_to_message_id`.

## Additive routing schema

At startup, the existing `updates` table receives only missing nullable columns, in a fixed order:

| Column | Exact source |
|---|---|
| `inbound_message_id` | admitted `Update.message.message_id` |
| `message_thread_id` | admitted `Update.message.message_thread_id`, or runtime default `0` |
| `direct_topic_id` | admitted `Update.message.direct_messages_topic.topic_id`, or runtime default `0` |
| `trigger_class` | deterministic bounded classification |
| `outbound_message_id` | `sendMessage.result.message_id` |
| `returned_chat_id` | `sendMessage.result.chat.id` |
| `returned_message_thread_id` | optional `sendMessage.result.message_thread_id` |
| `returned_direct_topic_id` | optional `sendMessage.result.direct_messages_topic.topic_id` |
| `returned_is_topic_message` | optional `sendMessage.result.is_topic_message` |

The official Bot API defines successful `sendMessage` as returning a `Message`; `Message` contains `message_id`, `chat`, optional `message_thread_id`, optional `direct_messages_topic`, and optional `is_topic_message`. Therefore `returned_direct_topic_id` is a local projection name, not an invented Telegram field: it is read only from `result.direct_messages_topic.topic_id`.

Migration is deterministic and idempotent. It performs no table replacement, deletion, backfill guess, transcript rewrite, or legacy-state coercion. Existing r0.2 rows and messages remain readable; their new fields remain `NULL` because the original raw routing evidence does not exist.

The machine-readable field and migration contract is in `ROUTING-OBSERVABILITY-SCHEMA.json`.

## Trigger classification

Persisted enum:

- `reply-to-bot`;
- `command`;
- `exact-mention`.

`reply-to-bot` takes classification precedence when present. Otherwise the first valid command/mention entity in Telegram's ordered entity list supplies the class, exactly preserving the predecessor's token-selection behavior. This classifies an already admitted event; it does not widen admission.

## Effect ordering and uncertainty

The sequence remains:

1. claim the exact update;
2. obtain provider candidate;
3. durably mark `SENDING`;
4. call `sendMessage` once;
5. validate the bounded returned route;
6. atomically commit transcript plus routing projection.

If Telegram returns success but step 5 or 6 fails, the update becomes `OUTCOME_UNKNOWN` with `reply_routing_persistence_failed` (or the fallback equivalent). An identical replay returns `manual_reconciliation_required`; it cannot call the provider or `sendMessage` again. If even the uncertainty write is unavailable, the pre-send durable `SENDING` state still blocks a blind retry on recovery.

A returned chat mismatch, or a returned thread/direct-topic mismatch when Telegram supplies that optional field, is fail-closed uncertainty rather than a successful commit.

## Privacy boundary

Persisted/logged routing evidence excludes:

- raw Update JSON;
- the full returned Telegram Message;
- usernames and display names;
- unrelated identities;
- raw provider response;
- credentials.

The predecessor's bounded visible dialogue transcript remains unchanged; this extension does not add raw content to observability storage.

## Read-only diagnostic

After a future reviewed installation/migration, SIS can inspect one update without credentials or network access:

```sh
python3 -I -B dialogue_mvp.py diagnose-routing \
  --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json \
  --update-id 560511152
```

The SQLite connection uses read-only mode and returns exactly the fields listed in `Store.DIAGNOSTIC_FIELDS`. It does not migrate or mutate the database. Missing update IDs return only the same bounded projection with `state=NOT_FOUND` and `error_class=update_not_found`.

## Offline verification

Commands used on the candidate copy:

```sh
python3 -I -B test_dialogue_mvp.py
python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py
systemd-analyze verify wellbeing-telegram-single-entity-pilot.service
sha256sum -c SHA256SUMS
```

The suite includes all 24 predecessor tests plus T1–T9 coverage for key stability/isolation, all trigger classes, minimal send projection, fail-closed post-send persistence failure, privacy, idempotent r0.2 migration, and the bounded read-only diagnostic. These are fake-transport/offline tests only.

## Files

- `dialogue_mvp.py` — runtime candidate, additive migration and diagnostic command.
- `test_dialogue_mvp.py` — predecessor and routing-observability offline tests.
- `ROUTING-OBSERVABILITY-SCHEMA.json` — exact additive field/migration/privacy contract.
- `UPGRADE.md` — future SIS install/readiness boundary.
- `PREDECESSOR-DIFF.patch` — exact diff against immutable r0.2 source/package files.
- unchanged config/bootstrap/allowlist/unit fixtures.
- `SELFTEST.json`, `MANIFEST.json`, `SHA256SUMS` — reproducibility evidence.

## Limits and next gate

This package proves only offline candidate behavior. It does not prove Telegram UI placement, live returned-message fields, installation, migration on the host, credential availability, service readiness, or a successful live turn.

Next and only gate: independent SIS review/install-readiness. It must reproduce package identities and offline tests, review additive migration and read-only diagnostics, and decide a separately authorized install/verify task. It must not start the service or perform a live call under this result.

---
КТО: KOD / КОДЕР v0.5
ДЛЯ ЧЕГО: privacy-safe Telegram routing observability candidate
СТАТУС: CANDIDATE_NOT_INSTALLED; READY_FOR_INDEPENDENT_SIS_REVIEW; LIVE_CALLS_ZERO
