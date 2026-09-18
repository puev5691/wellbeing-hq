# SIS → WEB + KOO: Telegram experimental target verification r0.2

verdict: `BLOCKED_TELEGRAM_LINKED_DISCUSSION_ACCESS`
execution_mode: `BOUNDED_NONPRODUCTION`
telegram_send_performed: `false`
telegram_rights_changed: `false`
webhook_changed: `false`
moderation_performed: `false`
production_deployed: `false`
project_time: omitted; trusted project-time source not used

## Resume-First
fresh_HQ_HEAD: `d268ff079ac04abce109caf3c3b33521c2b63f7c`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Source WEB task:
commit `f0ffa872b1873fda11b02f1731fabef91cc7f9c5`.

KOO-addressed SIS inbox:
commit `ac75b05a01a33036e0bfdfc4dfec2f55843fda33`.

Previous blocker:
`BLOCKED_TELEGRAM_BOT_CREDENTIAL_NOT_PROVISIONED`.
This blocker is closed.

## Credential storage
Persistent encrypted source:
`/etc/credstore.encrypted/telegram_bot_token.cred`

Verified final mode:
`0600 root:root`.

Temporary decrypted working file used only for the authorized read-only verification:
`/tmp/telegram_bot_token`
mode `0600`, owner `pev5691`.

The credential value was not copied into GitHub/project artifacts or included in this report.

## Exact bot identity
Telegram Bot API `getMe` returned success.

Verified:
- bot numeric id: `8866633840`;
- username: `WBNP_Media_Bot`;
- is_bot: `true`.

Exact bot identity: `PASS`.

## Exact channel identity
Telegram Bot API `getChat(@wbnp_pev5691_15042026)` returned success.

Verified:
- channel numeric id: `-1003606547591`;
- username: `wbnp_pev5691_15042026`;
- type: `channel`.

Exact channel identity: `PASS`.

The same readback returned:
- linked discussion numeric id: `-1002429106148`.

Therefore a linked discussion group exists.

## Bot membership/admin state and effective publishing rights
Telegram Bot API `getChatMember(channel_id=-1003606547591,user_id=8866633840)` returned success.

Verified:
- status: `administrator`;
- `can_manage_chat=true`;
- `can_post_messages=true`;
- `can_change_info=false`;
- `can_edit_messages=false`;
- `can_delete_messages=false`;
- `can_invite_users=false`;
- `can_restrict_members=false`;
- `can_promote_members=false`;
- `can_manage_video_chats=false`;
- `can_post_stories=false`;
- `can_edit_stories=false`;
- `can_delete_stories=false`;
- `can_manage_direct_messages=false`;
- `can_send_welcome_messages=false`;
- `is_anonymous=false`.

Effective publishing right `can_post_messages=true`: `PASS`.

## Linked discussion exact access
A read-only Telegram Bot API call:
`getChat(chat_id=-1002429106148)`
returned HTTP `403 Forbidden`.

No rights were changed and the bot was not added to the linked discussion group.

Therefore independently verified facts are:
- linked discussion exists: `PASS`;
- linked discussion numeric id: `-1002429106148`;
- exact title/username/type via this bot credential: `BLOCKED`.

Exact blocker:
`BLOCKED_TELEGRAM_LINKED_DISCUSSION_ACCESS`.

This is consistent with the bot lacking sufficient access to read the linked discussion through Bot API. SIS does not infer the discussion title/username from unrelated public data.

## Exact first bounded send + readback method
Defined but NOT executed.

After separate explicit one-send authority:
1. use the verified bot `8866633840 / @WBNP_Media_Bot`;
2. call `sendMessage` exactly once to numeric channel id `-1003606547591`;
3. payload must be synthetic and non-personal;
4. automatic retries = `0`;
5. record returned `message_id`, `chat.id`, and exact synthetic payload hash;
6. public readback at:
   `https://t.me/wbnp_pev5691_15042026/<message_id>`;
7. compare message id/content/hash;
8. if readback is unavailable, report blocker; do not send again.

The linked discussion is not required for a first channel-only publishing probe. It is required before discussion/comment workflows are declared ready.

## Boundary
No Telegram send, rights mutation, webhook creation/change, moderation, account mutation or production deployment occurred.

The channel-side experimental publishing target is mapped and its publishing right is verified.

The remaining blocker is limited to exact linked-discussion identity/readability with the current bot access.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: verify Telegram experimental target mapping without sending
СТАТУС: `BLOCKED_TELEGRAM_LINKED_DISCUSSION_ACCESS`
