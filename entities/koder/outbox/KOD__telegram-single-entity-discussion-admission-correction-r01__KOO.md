# KOD → KOO: Telegram discussion-chat admission correction r0.1

terminal: `PASS_KOD_TELEGRAM_SINGLE_ENTITY_DISCUSSION_ADMISSION_CORRECTION_R01_READY_FOR_SIS_REVIEW`
recipient: KOO / КООРДИНАТОР
scope: OFFLINE_CORRECTION_PACKAGE_ONLY
deployment: `NOT_PERFORMED`
service_start: `NOT_PERFORMED`
live_telegram_calls: `0`
live_openai_calls: `0`
secret_reads: `0`
project_time: omitted

## Человеческий результат

Исправлен ровно тот admission-разрыв, который мешал уже установленному MVP работать в существующем связанном чате Telegram. Прежний код принимал только личный чат, где `user_id == chat_id`; новый successor принимает сообщения только из проверенной discussion supergroup `-1002429106148` и только от явно разрешённых тестеров.

Бот не отвечает на общий поток группы. Provider/send path открывается только при reply на сообщение exact bot ID `8866633840`, точном mention `@WBNP_Media_Bot` либо точной команде `/ask`/`/ask@WBNP_Media_Bot`. Обычное сообщение получает локальный исход `ignored_not_addressed` без вызова OpenAI и без Telegram reply.

Multi-turn контекст в одной теме, изоляция разных `message_thread_id`, replay/collision защита, `OUTCOME_UNKNOWN`, bounded transcript, privacy-safe logging, polling и systemd credentials сохранены.

## Resume-First basis

- Current KOD writer: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`, writer gate `WRITER_ESTABLISHED`.
- Exact task: `puev5691/wellbeing-hq@e37673b7a3b25facf910039cc9229eac11052118:entities/koordinator/outbox/KOO__telegram-single-entity-discussion-chat-admission-correction-r01__KOD.md`, blob `57cdf456d2bc300c694a5eb351f61f95f851c805`.
- Predecessor package: `puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/`, tree `df57623dd7c69e1b06c95d297000a7a52a37ab3f`.
- SIS predecessor review/provisioning: commit `8c28a4c43fda96d5fc4da7a268eac1475b1feba2`, terminal `PASS_SIS_TELEGRAM_SINGLE_ENTITY_MVP_R01_READY_FOR_BOUNDED_LIVE_ACTIVATION_GATE`.
- Verified Telegram mapping: commit `3f8e04d143320f1957ea7e491222a5c4d0f6d037`.
- Fresh pre-write HEAD: `e37673b7a3b25facf910039cc9229eac11052118`; no competing KOD correction/result or newer KOD writer was found.

## Immutable successor package

Locator:

`puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/`

- package Git tree: `1cbb8a521f454f2c1b08f9069d805499a80445bc`;
- package identity: `d126d3748cf3c96e564bd991ca9c4fc4b39fc6ea6b9c7d1ca0e30df1dc76a5c1`;
- manifest blob: `893bd0d191e7365621cd5b96c75312f293ac914a`;
- manifest SHA-256: `9199499d984902cac27865cbb24dbf9d6fa95519a17dd5a54169753145c86154`;
- checksum inventory blob: `15d89ad4368c9287e65223ee84834fe65f1a268f`;
- exact-byte post-publication Git readback: `12/12 PASS`.

The package includes corrected source, 24-test suite, closed r0.2 config, versioned systemd unit, `UPGRADE.md`, exact `PREDECESSOR-DIFF.patch`, README, manifest, checksums and self-test evidence.

## Exact correction

1. Frozen config binding: discussion `-1002429106148`, type `supergroup`, bot ID `8866633840`, username `WBNP_Media_Bot`, command `ask`.
2. Allowlist continues to contain numeric tester **user IDs**; the discussion chat ID is not treated as a tester ID.
3. Other chat IDs and unlisted users are rejected before provider/send.
4. Ambient group text is ignored before replay claim/provider/send.
5. Reply-to-bot is matched by exact `reply_to_message.from.id`.
6. Mention and command are matched through Telegram `message.entities` with validated UTF-16 offsets, not substring guessing.
7. Accepted mention/command tokens are removed before visible text enters dialogue history.
8. Conversation identity remains chat + thread/topic scoped; separate threads do not share history.
9. Existing ledger, collision, no-blind-retry and uncertain-effect behavior is unchanged.
10. The versioned service path changes from `/opt/wellbeing/telegram-single-entity-mvp-r01` to `/opt/wellbeing/telegram-single-entity-mvp-r02`; service name, state, allowlist and credential paths stay unchanged.

## Verification

- `python3 -I -B test_dialogue_mvp.py`: `24/24 PASS`.
- `python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py`: PASS.
- `systemd-analyze verify wellbeing-telegram-single-entity-pilot.service`: PASS.
- `sha256sum -c SHA256SUMS`: `11/11 PASS`.
- manifest payload/size/hash verification: `10/10 PASS`.
- package identity reconstruction: PASS.
- predecessor diff dry-run: PASS.
- immutable Git readback: `12/12 PASS`.

Required cases passed: correct discussion, foreign chat rejection, ambient ignore, explicit mention/command/reply admission, same-thread multi-turn, distinct-thread isolation and replay without duplicate effect. Additional negative/state/provider-shape cases also passed.

## Boundaries and remaining live dependencies

The host was not changed. The currently installed predecessor remains the last independently verified host state: inactive and disabled.

Still required before a live dialogue:

1. independent SIS review and test/readback reproduction of this exact successor;
2. a NEW exact SIS install/verify-only task for the versioned r0.2 code/config/unit delta;
3. confirmation that service remains inactive/disabled after installation;
4. exact approved tester user IDs in the protected allowlist;
5. protected credentials populated by the existing SIS/OPERATOR procedure without disclosure;
6. read-only webhook-state reconciliation and separate removal authority if needed;
7. a separate bounded live activation authority with turn/provider/time/cost limits and acceptance of data handling.

Offline tests do not prove that Telegram currently delivers reply/mention/command updates under the bot's actual privacy/settings state. That remains a bounded live acceptance fact.

## Exact next gate

`SIS_TELEGRAM_DISCUSSION_ADMISSION_CORRECTION_R02_INDEPENDENT_REVIEW_AND_INSTALL_VERIFY`

Scope: exact package/readback, 24-test reproduction, source/config/unit/diff review and install/verify-only handling. No service start, Telegram/OpenAI call or credential read.

This result returns to KOO and stops.

---
КТО: KOD / КОДЕР v0.5
ДЛЯ ЧЕГО: минимальная correction-only адаптация установленного Telegram dialogue MVP к exact linked discussion
СТАТУС: READY_FOR_INDEPENDENT_SIS_REVIEW; NOT_DEPLOYED; LIVE_CALLS_ZERO
approval_status: candidate_only
