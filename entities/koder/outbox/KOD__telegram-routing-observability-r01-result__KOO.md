# KOD → KOO: Telegram routing observability r0.1

terminal: `PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW`
recipient: KOO / КООРДИНАТОР
scope: `BOUNDED_OFFLINE_CANDIDATE_ONLY`
status: `CANDIDATE_NOT_INSTALLED`
deployment: `NOT_PERFORMED`
service_start: `NOT_PERFORMED`
live_telegram_calls: `0`
live_openai_calls: `0`
credential_reads: `0`
project_time: omitted

## Человеческий результат

Подготовлен минимальный successor действующего Telegram dialogue runtime, который сохраняет ровно те routing-поля, которых не хватило для доказательства места размещения ответа в live pilot r0.3. Он не меняет admission, модель/provider, allowlist, polling или формулу `conversation_key`.

Для каждого принятого update теперь сохраняются inbound message/thread/direct-topic, точный класс trigger и outbound message ID. Из успешного `sendMessage` сохраняется только privacy-safe проекция возвращённого `Message`: message/chat/thread/direct-topic/is-topic. Полный Update, полный Message, username/display name, raw provider response и credentials не сохраняются.

Добавлен read-only diagnostic для одного `update_id`. Если Telegram уже вернул успешный send, но routing metadata не удалось зафиксировать, результат становится `OUTCOME_UNKNOWN`, а повтор того же update не вызывает вторую отправку.

Это offline candidate. Он не установлен и не доказывает видимость ответа в Telegram UI.

## Resume-First / currentness

- Current KOD writer: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`, outcome `WRITER_ESTABLISHED`.
- Exact task: `puev5691/wellbeing-hq@90b175bd299ea377350faa347307ff10a47b3b9e:entities/koordinator/outbox/KOO__telegram-routing-observability-r01__KOD.md`, blob `09ca88739b067a29174925d84923ff4c96c6629a`.
- Exact predecessor source: `puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/dialogue_mvp.py`, blob `0ea2cb8c9fe4872bfbfd1ec348ba23bfa9dbce6d`.
- Blocker basis: commit `826068657421e3f2209f3c289528a5577884246c`, terminal `BLOCKED_SIS_TELEGRAM_SAME_THREAD_LIVE_R03_REPLY_VISIBILITY_NOT_CONFIRMED`.
- Diagnostic basis: commit `ef033331a12cc0faf47ccaef78012d94fa6e7477`, terminal `PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01`.
- Fresh pre-write HEAD was exact task commit `90b175bd299ea377350faa347307ff10a47b3b9e`; no newer KOD writer, freeze/handoff conflict, superseding task, or competing terminal result was present.

## Immutable package

Locator:

`puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:entities/koder/outbox/telegram-routing-observability-r01/`

- package Git tree: `bbe40dc80670b33594f997cea52e42508a7ae12b`;
- package identity: `537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c`;
- manifest blob: `d3c45c856c6ea43d727397fc9c7f3059e58ff711`;
- manifest SHA-256: `9798137bccf7ac3b849d1b1f3d8e112e820d7cdda11d326df40bb3b34e505783`;
- checksum inventory blob: `aeec7b08673e07d540954c1be91a829c8bac954e`;
- checksum inventory SHA-256: `4c08a73642f2d3fce2c6d48bcfb56cc3c55d8273ef853563c02a689882739e23`;
- exact Git blob readback: `13/13 PASS`;
- payload SHA-256 readback: `11/11 PASS`;
- package identity reconstruction: PASS.

## Changed files / Git blobs

| File | Git blob | Role |
|---|---|---|
| `dialogue_mvp.py` | `394788b67e25f6c574aab0d65906309418e6cabe` | additive migration, trigger class, send-result projection, fail-closed commit, diagnostic |
| `test_dialogue_mvp.py` | `361a4c6ecf2e785f76075f484ac07daf4d08d30b` | predecessor suite + T1–T9 |
| `ROUTING-OBSERVABILITY-SCHEMA.json` | `9835f31bf7229ba6728b1db757b3d2e427abc3bf` | exact machine-readable fields/privacy/migration contract |
| `README.md` | `2fb2beeb0ec2b3107da8fa03c8ee87cca5f2c929` | behavior, limits and next gate |
| `UPGRADE.md` | `ca24c4401b3803bf1f62eeeb0dc6ec1ab7142038` | future SIS install-readiness/rollback boundary |
| `PREDECESSOR-DIFF.patch` | `7df83c9f76f09f9447b1483e1f9566d04bd710e7` | exact source/package delta |
| `SELFTEST.json` | `98121df3d113f9599e36cea99c95a4dd9d6965ba` | offline results |
| `MANIFEST.json` | `d3c45c856c6ea43d727397fc9c7f3059e58ff711` | package inventory/identity |
| `SHA256SUMS` | `aeec7b08673e07d540954c1be91a829c8bac954e` | payload checksums |

Unchanged predecessor fixtures were republished byte-identically: config, Entity bootstrap, tester fixture and systemd unit. Their presence does not install or activate the candidate.

## Schema / migration

The migration adds only nullable columns to `updates`, in deterministic order:

- `inbound_message_id`;
- `message_thread_id`;
- `direct_topic_id`;
- `trigger_class`;
- `outbound_message_id`;
- `returned_chat_id`;
- `returned_message_thread_id`;
- `returned_direct_topic_id`;
- `returned_is_topic_message`.

It is idempotent, uses no destructive rewrite/backfill, preserves the existing DB and keeps committed r0.2 history readable. Legacy rows keep the new fields as `NULL`; missing historical evidence is not guessed.

## Routing fields and Bot API mapping

Successful `sendMessage` returns a Telegram `Message`. The candidate projects only:

- `result.message_id` → `returned_message_id` / persisted `outbound_message_id`;
- `result.chat.id` → `returned_chat_id`;
- optional `result.message_thread_id` → `returned_message_thread_id`;
- optional `result.direct_messages_topic.topic_id` → `returned_direct_topic_id`;
- optional `result.is_topic_message` → `returned_is_topic_message`.

Official reference used: `https://core.telegram.org/bots/api#message` and `#sendmessage`. No Bot API call was made.

## Trigger classification

Bounded persisted enum:

- `reply-to-bot`;
- `command`;
- `exact-mention`.

Reply-to-bot has classification precedence. Otherwise the first already-admitted valid command/mention entity supplies the class, preserving predecessor admission and token selection.

## Diagnostic helper

Command:

`dialogue_mvp.py diagnose-routing --config CONFIG --update-id UPDATE_ID`

It opens SQLite read-only, requires no credential and returns only:

`update_id, inbound_message_id, message_thread_id, direct_topic_id, trigger_class, conversation_key, outbound_message_id, returned_chat_id, returned_message_thread_id, returned_direct_topic_id, returned_is_topic_message, state, error_class`.

## Offline matrix and results

- T1 same chat/thread/topic → same `conversation_key`: PASS.
- T2 different thread → different key: PASS.
- T3 different direct topic → different key: PASS.
- T4 bounded deterministic trigger classes persisted: PASS.
- T5 only minimal routing projection persisted from successful send: PASS.
- T6 send success + routing persistence failure → `OUTCOME_UNKNOWN`, no duplicate resend: PASS.
- T7 no new raw Update/full Message/names/raw provider response/credentials in persistence/logs: PASS.
- T8 r0.2 DB migrates additively/idempotently and history remains readable: PASS.
- T9 read-only diagnostic returns only bounded fields: PASS.

Commands/results:

- `python3 -I -B test_dialogue_mvp.py`: `35/35 PASS`;
- `python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py`: PASS;
- `systemd-analyze verify wellbeing-telegram-single-entity-pilot.service`: PASS;
- `sha256sum -c SHA256SUMS`: `11/11 PASS`;
- privacy: PASS;
- external/live calls: `0`;
- deployment/service start: `0`.

## Effect ordering / uncertainty

Claim → provider → durable `SENDING` → one `sendMessage` → route validation → atomic transcript+routing commit remains the order. Successful send followed by validation/persistence failure is not silently retried: it becomes `OUTCOME_UNKNOWN`; replay returns reconciliation-required without another provider/send effect. Existing update collision and unresolved-turn gates remain intact.

## Boundaries

- `conversation_key` formula is byte-for-byte unchanged (`tg-dialogue-r02` domain plus chat/thread/direct-topic).
- Admission, allowlist, credentials, provider/model, polling and service unit are unchanged.
- No install, service start, Telegram send/edit/delete, OpenAI call, host mutation or secret access occurred.
- No claim of Telegram UI placement or reply visibility is made.
- r0.1/r0.2/r0.3 live authorities were not replayed.

## Exact next gate

`SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INDEPENDENT_REVIEW_INSTALL_READINESS`

Scope: independently read back this exact package, reproduce the 35 offline tests and checksum identity, review migration/privacy/effect ordering, and determine a separately authorized install/verify step. No service start or live call.

This result returns to KOO and stops.

---
КТО: KOD / КОДЕР v0.5
ДЛЯ ЧЕГО: minimal privacy-safe routing observability successor
СТАТУС: CANDIDATE_NOT_INSTALLED; READY_FOR_INDEPENDENT_SIS_REVIEW; LIVE_CALLS_ZERO
approval_status: candidate_only

## Terminal

PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW
