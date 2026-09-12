# KOO: Telegram experimental surface

status: OPERATOR_APPROVED_EXPERIMENTAL_TARGET
production_status: not_production_authorized_by_this_record

## Target

Telegram channel:
`https://t.me/wbnp_pev5691_15042026`

channel_key:
`wbnp_pev5691_15042026`

## Operator decision

ОПЕРАТОР явно предоставил этот Telegram-канал как площадку для экспериментов и работы проекта и разрешил использовать его в рамках текущего Telegram media-contour.

Это решение:
- разрешает считать канал реальным экспериментальным target для Phase 1 и последующих bounded tests;
- позволяет готовить публикацию synthetic/test materials после прохождения required technical gates;
- отменяет необходимость создавать отдельный новый test channel, если этот канал технически пригоден;
- не требует сохранять текущий контент/оформление неизменными.

## Important boundary

Фраза ОПЕРАТОРА «делайте с ним, что хотите» трактуется как широкое разрешение на экспериментальное использование канала, но не отменяет базовые project safety boundaries.

Без отдельного подтверждённого technical authority запрещено:
- публиковать secrets, bot tokens, webhook secrets, private session credentials;
- раскрывать private user identifiers или сырые приватные audience data;
- выполнять destructive moderation/bans без policy;
- использовать MTProto user-session credentials;
- переносить в public GitHub raw audience comment database;
- выдавать отправку за verified delivery без message_id/readback;
- считать experimental channel production source-of-truth.

## Current verification state

KOO attempted public web readback of the supplied Telegram URL.

Result:
- target URL is operator-supplied and accepted as project experimental target;
- ordinary web fetch/search did not return reliable channel-state evidence;
- current public/private status, admin rights, linked discussion presence, subscriber count and existing bot configuration are NOT independently verified by KOO.

No assumptions are made for these fields.

## Use in current Telegram media cycle

Phase 0:
- remains credential-free;
- uses fake adapter and synthetic fixtures;
- no Telegram network call;
- current KOD task remains unchanged in acceptance semantics.

Phase 1 preferred target:
- use `wbnp_pev5691_15042026` as the first real Telegram channel if WEB/SIS verification confirms it is controllable;
- linked discussion group may be existing or newly linked, but exact state must be verified;
- bot must be added as admin with minimum required rights;
- bot token goes only to SIS-controlled secret storage;
- first real test content must be synthetic and clearly marked experimental;
- first send must produce exact Telegram message id and readback evidence.

## Required next facts before real send

Need verified answers for:
1. can the project owner/admin manage this channel;
2. is the channel public/private and what is its numeric chat id;
3. is a discussion supergroup already linked;
4. if linked, what is its numeric chat id;
5. is there already a project bot suitable for publishing;
6. can that bot be granted minimal admin rights;
7. what secret-store path will SIS use for bot token/webhook secret;
8. what exact publication/readback method will be used for first sandbox message.

## Plugin/control surface check

KOO checked current ChatGPT plugin catalog for Telegram publishing/control.

Result:
`NO_TELEGRAM_CONTROL_PLUGIN_FOUND`.

Therefore current implementation path remains:
`Media Gateway + Telegram Bot API`.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать предоставленный ОПЕРАТОРОМ Telegram-канал как approved experimental target текущего media-contour
СТАТУС: operator_approved_experimental_target
