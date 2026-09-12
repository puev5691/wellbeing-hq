# WEB → KOO: Telegram experimental surface public readback

status: RESULT_FOR_KOO_REVIEW
scope: read-only public surface verification
production_changed: false
telegram_write_action: none

## Target

`https://t.me/wbnp_pev5691_15042026`

channel_key:
`wbnp_pev5691_15042026`

## Verified by WEB

WEB performed read-only HTTP checks from an authorized remote host.

### Direct channel URL

`https://t.me/wbnp_pev5691_15042026`

Observed:
- HTTP `200`;
- final URL unchanged;
- HTML title: `Telegram: View @wbnp_pev5691_15042026`;
- `og:title`: `Медиа Благополучие`;
- public description identifies it as the media contour channel of the Wellbeing project and mentions drafts, discussion, critique, plans and participant employment.

### Public preview URL

`https://t.me/s/wbnp_pev5691_15042026`

Observed:
- HTTP `200`;
- final URL unchanged;
- HTML title: `Медиа Благополучие – Telegram`;
- public preview exposes channel posts;
- observed post locators include `wbnp_pev5691_15042026/13` through later posts in the returned preview;
- preview exposed an observed subscriber count of `5` during this verification pass.

The subscriber count is volatile operational data and is not promoted to a stable project fact.

## Public/private result

Because the `/s/` public preview is directly available and exposes channel posts, WEB classifies:

`channel_public_state: PUBLIC_VERIFIED`

This verifies public web visibility only.

It does NOT prove project admin control.

## Discussion-group verification

WEB searched the returned public preview HTML for discussion/comment/linkage indicators.

No reliable linked-discussion identifier or public comments linkage was found.

Therefore:

`discussion_linked_state: UNKNOWN`

Absence of a public HTML hint is not evidence that no discussion group exists.

## Numeric chat id

WEB searched the public HTML for peer/channel/chat/entity id fields.

No reliable numeric Telegram chat id was exposed.

Therefore:

`channel_numeric_chat_id: UNKNOWN`

It must be obtained from Telegram-side Bot API/client evidence during bounded Phase 1 bootstrap, not inferred from username or synthetic Phase 0 ids.

## Still unknown

- project/admin control of this channel;
- exact numeric channel chat id;
- linked discussion existence;
- exact numeric discussion chat id;
- existing publisher bot;
- bot admin permissions;
- webhook configuration;
- Telegram-side moderation settings.

## Mapping contract update

Current verified mapping may now be represented as:

```yaml
telegram_surface:
  channel_key: wbnp_pev5691_15042026
  channel_username: wbnp_pev5691_15042026
  public_state: PUBLIC_VERIFIED
  public_title: "Медиа Благополучие"
  channel_chat_id: UNKNOWN
  admin_control: UNKNOWN
  discussion:
    linked: UNKNOWN
    discussion_chat_id: UNKNOWN
  bot:
    configured: UNKNOWN
    admin_in_channel: UNKNOWN
    admin_in_discussion: UNKNOWN
```

## Phase 1 implication

Before first real synthetic send:

1. verify owner/admin can manage the channel;
2. obtain exact channel numeric chat id from Telegram-side evidence;
3. verify linked discussion state;
4. obtain discussion numeric chat id if linked;
5. verify/create publisher bot;
6. grant minimum rights;
7. hand bot token only to SIS-controlled secret storage;
8. KOD real adapter must bind on `(chat_id, message_id)`, not message id alone;
9. first send must be explicitly synthetic/experimental;
10. verify returned message id and readback before `delivered_verified`.

## Relation to previous WEB result

Supplements:
`entities/webmaster/outbox/WEB__telegram-phase0-verify-phase1-mapping__KOO.md`

That result remains unchanged.

---
created_by: WEB
to_entity: koordinator
document_type: telegram-experimental-surface-public-readback
purpose: replace public/private guesswork with verified web-surface evidence while preserving unknown admin/discussion/numeric-id facts
project_time: not_recorded_no_trusted_source