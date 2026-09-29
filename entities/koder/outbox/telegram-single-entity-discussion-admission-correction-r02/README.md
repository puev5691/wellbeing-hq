# Telegram single-Entity discussion admission correction r0.2

Status: immutable offline correction candidate for independent SIS review. It has not been deployed, the service was not started, and no Telegram or OpenAI call was made.

## Human result

This successor keeps the already reviewed dialogue MVP but moves its admission boundary from a private chat to the one verified linked discussion supergroup. It still serves only explicitly allowlisted testers and does not answer ambient group traffic.

A turn is accepted only when all of these are true:

1. the update contains a text `message`;
2. `chat.type` is exactly `supergroup`;
3. `chat.id` is exactly `-1002429106148`;
4. `from.id` is present in the root-controlled tester allowlist;
5. the text is explicitly addressed to the verified bot by reply, exact mention, or exact `/ask` command.

Ordinary group messages are acknowledged locally as `ignored_not_addressed`; they cause no provider or Telegram send effect.

## Exact basis

- Exact KOO task: `puev5691/wellbeing-hq@e37673b7a3b25facf910039cc9229eac11052118:entities/koordinator/outbox/KOO__telegram-single-entity-discussion-chat-admission-correction-r01__KOD.md`, blob `57cdf456d2bc300c694a5eb351f61f95f851c805`.
- Current KOD writer: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`.
- Immutable predecessor: `puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/`, tree `df57623dd7c69e1b06c95d297000a7a52a37ab3f`.
- Independent predecessor review/provisioning PASS: `puev5691/wellbeing-hq@8c28a4c43fda96d5fc4da7a268eac1475b1feba2:entities/sisadmin/outbox/SIS__telegram-single-entity-mvp-independent-review-provisioning-r01__KOO.md`.
- Verified Telegram mapping: `puev5691/wellbeing-hq@3f8e04d143320f1957ea7e491222a5c4d0f6d037:entities/webmaster/outbox/WEB__telegram-media-reconciliation-r01__KOO.md`.

Frozen target identities:

- bot username: `WBNP_Media_Bot`;
- bot user ID: `8866633840`;
- channel ID: `-1003606547591` (mapping evidence only, not admitted for dialogue);
- linked discussion ID: `-1002429106148`;
- linked discussion type: `supergroup`.

## Exact flow

`Telegram getUpdates polling → exact discussion/tester/trigger admission → replay claim → per-discussion-thread history → bounded Entity bootstrap + OpenAI Responses API → Telegram sendMessage to the same chat/thread → committed turn`

The provider request remains the predecessor contract: `instructions`, visible message-array `input`, `max_output_tokens`, `store=false`, and `tools=[]`. Only completed assistant `output_text` is accepted. A reasoning-only response produces the configured visible fallback.

## Trigger semantics

An allowlisted tester turn is explicit when at least one condition is true:

- `reply_to_message.from.id == 8866633840`;
- a Telegram `message.entities` item of type `mention` resolves by Telegram UTF-16 offsets to exact `@WBNP_Media_Bot`, case-insensitively;
- a `bot_command` entity resolves to exact `/ask` or `/ask@WBNP_Media_Bot`, case-insensitively.

The accepted mention/command token is removed before the visible user text is added to dialogue history. Empty addressed text is rejected. Reply-to-someone-else, a lookalike username, malformed entity offsets and ambient text do not open a provider call.

The implementation deliberately does not infer a trigger from arbitrary substring matching.

## Preserved behavior

- Long polling only; no public listener or webhook runtime.
- Root-controlled numeric tester allowlist.
- Conversation key derived from exact chat, `message_thread_id`, and direct-topic ID when supplied.
- Same thread retains bounded visible multi-turn history; distinct topics/threads remain isolated.
- Exact update replay creates no second provider/send effect.
- Same `update_id` with changed canonical bytes is a conflict.
- In-progress or uncertain effect remains `manual_reconciliation_required` / `OUTCOME_UNKNOWN`; no blind retry.
- SQLite stores bounded visible transcript, opaque conversation key, replay state and poll cursor.
- No raw update, username, display name, provider raw response/error, token or API key persistence/logging.
- Dialogue output creates no project, task, writer, production or acceptance authority.
- Existing systemd `LoadCredential` mechanism is unchanged.

## Files

- `dialogue_mvp.py` — corrected exact discussion admission and explicit trigger parser plus preserved runtime.
- `test_dialogue_mvp.py` — offline fake-transport suite.
- `config.example.json` — closed r0.2 config with frozen bot/discussion identities.
- `UPGRADE.md` — exact install/verify/rollback delta from installed r0.1.
- `PREDECESSOR-DIFF.patch` — exact non-generated file diff against immutable r0.1.
- `entity_bootstrap.txt` — unchanged bounded Entity bootstrap.
- `testers.allow.example` — unchanged synthetic numeric tester fixture.
- `wellbeing-telegram-single-entity-pilot.service` — same service/credential contour, versioned package path.
- `MANIFEST.json`, `SHA256SUMS`, `SELFTEST.json` — package integrity and test evidence.

## Offline verification

Run only from a disposable package copy:

```sh
python3 -I -B test_dialogue_mvp.py
python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py
systemd-analyze verify wellbeing-telegram-single-entity-pilot.service
sha256sum -c SHA256SUMS
```

The 24 fake-transport tests cover the exact discussion chat, foreign chat rejection, tester rejection, ambient ignore, mention, command, reply-to-bot, UTF-16 entity offsets, multi-turn same-thread state, thread isolation, replay, collision, bounded input/history, fallback, `OUTCOME_UNKNOWN`, privacy-safe logs, poll cursor/request and unchanged OpenAI response-shape rules.

These are offline implementation tests. They do not prove live Bot API delivery, Telegram privacy-mode behavior, provider success, deployment or user acceptance.

## Deployment boundary

The independently reviewed predecessor is installed on `ruvds-xnqc6`, inactive and disabled. This package does not mutate that host.

The next SIS step may independently review exact bytes and prepare/install the versioned package in **install/verify-only** mode. Starting or enabling the service, checking/removing a webhook, reading credentials, calling Telegram/OpenAI, changing Telegram rights or running a live turn require separate exact authority.

The exact target changes are documented in `UPGRADE.md`. In summary:

- new immutable code root: `/opt/wellbeing/telegram-single-entity-mvp-r02`;
- existing state DB, allowlist, protected credential slots and service name remain unchanged;
- runtime schema becomes `TELEGRAM_ENTITY_DIALOGUE_MVP_R02` and adds exact bot/discussion/trigger bindings;
- systemd `WorkingDirectory` and `ExecStart` move from the r0.1 code root to the r0.2 code root;
- rollback restores the preserved r0.1 unit/config bytes and leaves state/secrets untouched.

## Next causal gate

`SIS_TELEGRAM_DISCUSSION_ADMISSION_CORRECTION_R02_INDEPENDENT_REVIEW_AND_INSTALL_VERIFY`

Scope: exact package/readback, 24-test reproduction, config/unit/diff review, and install/verify-only preparation or execution under a NEW exact SIS task. No service start and no live call.

Only after that PASS may KOO return a separately bounded live-activation decision to OPERATOR.

---
КТО: KOD / КОДЕР v0.5
ДЛЯ ЧЕГО: correction-only linked-discussion admission successor
СТАТУС: READY_FOR_INDEPENDENT_SIS_REVIEW; NOT_DEPLOYED; LIVE_CALLS_ZERO
approval_status: candidate_only
responsibility_boundary: offline code/package correction; no host, credential, Telegram, provider or governance mutation
