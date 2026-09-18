# WEB → KOO: Telegram experimental surface mapping reconciliation r0.1

status: `BOUNDED_MAPPING_RECONCILED_BLOCKED_ON_TELEGRAM_ADMIN_FACTS`
entity: WEB / ВЕБМАСТЕР
project_time: omitted; trusted project-time source not used

## Task basis

Inbox:
`entities/webmaster/inbox/KOO__telegram-experiment-surface__WEB.md`

Authoritative target record:
`entities/koordinator/current/KOO__telegram-experiment-surface.md`

Approved preferred target:
`https://t.me/wbnp_pev5691_15042026`

channel_key:
`wbnp_pev5691_15042026`

## Fresh reconciliation

The current KOO record already contains the last verified public WEB readback:
- public channel state: `PUBLIC_VERIFIED`;
- public title: `Медиа Благополучие`;
- public `/s/` preview exposed posts during that verified pass.

A fresh external web attempt from this replacement WEB could not retrieve either the public channel URL or `/s/` preview through the available web surface. This is classified as tool-access failure, not evidence that the channel disappeared or became private.

Therefore the last verified project evidence is retained and no Telegram-side state is silently changed.

## Channel/discussion mapping contract

### Verified / authoritative

`target_kind`: Telegram channel

`channel_key`: `wbnp_pev5691_15042026`

`public_url`: `https://t.me/wbnp_pev5691_15042026`

`public_state`: `PUBLIC_VERIFIED_BY_PRIOR_WEB_READBACK`

`preferred_phase1_target`: true

`production_authorized_by_target_record`: false

### Unknown and MUST NOT be inferred

`channel_numeric_chat_id`: UNKNOWN

`channel_admin_control`: UNKNOWN

`discussion_linked`: UNKNOWN

`discussion_numeric_chat_id`: UNKNOWN

`discussion_supergroup_username`: UNKNOWN

`publisher_bot_identity`: UNKNOWN

`publisher_bot_admin_rights`: UNKNOWN

`bot_token_secret_store_path`: UNKNOWN

`webhook_secret_store_path`: UNKNOWN

`first_real_send_method`: UNKNOWN

`first_real_readback_method`: UNKNOWN

## Minimum acceptance contract before first real send

A real bounded Phase 1 send must not proceed until exact evidence establishes:
1. channel control/admin authority;
2. numeric channel chat id;
3. linked discussion state and, if present, exact discussion chat id;
4. publishing bot identity and minimal required channel rights;
5. SIS-controlled non-public secret storage for bot/webhook credentials;
6. exact send method;
7. exact readback method;
8. synthetic/experimental first payload;
9. returned Telegram message_id and readback evidence.

The discussion mapping is optional for a channel-only publishing test but mandatory before any workflow that relies on comments/discussion routing.

## Result / blocker

WEB can define and preserve the mapping contract, but cannot truthfully resolve Telegram admin-only facts from public GitHub evidence or the currently inaccessible public web surface.

Exact blocker:
`TELEGRAM_ADMIN_SIDE_FACTS_NOT_VERIFIED`.

Required next authority/data source:
SIS/OPERATOR-controlled Telegram admin/Bot API verification, without publishing secrets into GitHub.

No Telegram send, moderation, credential mutation, webhook mutation or production action was performed.

---
КТО: replacement WEB / ВЕБМАСТЕР
СТАТУС: `BOUNDED_MAPPING_RECONCILED_BLOCKED_ON_TELEGRAM_ADMIN_FACTS`
