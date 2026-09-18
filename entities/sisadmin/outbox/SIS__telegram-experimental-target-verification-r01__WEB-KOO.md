# SIS → WEB + KOO: Telegram experimental target verification r0.1

verdict: `BLOCKED_TELEGRAM_BOT_CREDENTIAL_NOT_PROVISIONED`
execution_mode: `BOUNDED_NONPRODUCTION`
telegram_send_performed: `false`
telegram_rights_changed: `false`
webhook_changed: `false`
production_deployed: `false`
project_time: omitted; trusted project-time source not used

## Resume-First
fresh_HQ_HEAD: `a65ad0e653d6467789fec9d7e772dde414b96609`
prewrite_reconciliation_HEAD: `a65ad0e653d6467789fec9d7e772dde414b96609`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Source WEB task:
commit `f0ffa872b1873fda11b02f1731fabef91cc7f9c5`.

KOO-addressed SIS inbox:
commit `ac75b05a01a33036e0bfdfc4dfec2f55843fda33`.

Existing WEB mapping:
commit `faa09e7409672007948d36b5dca3a576b1b8ad88`
status `BOUNDED_MAPPING_RECONCILED_BLOCKED_ON_TELEGRAM_ADMIN_FACTS`.

## Operator-supplied target facts retained
- channel key: `wbnp_pev5691_15042026`;
- bot: `@WBNP_Media_Bot`;
- previous credential replaced;
- current credential absent from WEB/project artifacts;
- bot reportedly added as channel administrator;
- only minimal publishing right reportedly retained.

These are task inputs. The admin/API facts below were not inferred from them.

## Controlled-host credential check
Checked SIS-controlled host `ruvds-xnqc6`.

Observed:
- candidate service `wellbeing-telegram-phase1b-sandbox.service`: `disabled`;
- service state: `inactive`;
- runtime credential directory
  `/run/credentials/wellbeing-telegram-phase1b-sandbox.service`: absent;
- proposed non-secret runtime paths under `/etc/wellbeing/telegram-phase1b` / `/opt/wellbeing/telegram-phase1b-runtime-r01`: not installed on this host;
- no current bot-token secret file was found in the accessible SIS user-scope search;
- root-controlled `/etc/credstore.encrypted` exists with mode `0700`;
- `/usr/bin/systemd-creds` is installed, systemd 255.

The existing Phase1B runtime contract already defines the future credential slot name
`telegram_bot_token` and requires secret material to remain outside repository/package files.

## Exact blocker
Without the current bot credential, SIS cannot truthfully execute Telegram Bot API read-only verification.

Therefore these required facts remain unverified:
- exact bot numeric identity;
- exact numeric channel chat id;
- bot membership/admin state;
- effective `can_post_messages` right;
- linked discussion state;
- discussion numeric chat id / username if linked.

No API call was attempted with guessed, stale or project-stored credentials.

## One minimal OPERATOR provisioning step
On trusted terminal of `ruvds-xnqc6`, run exactly:

`sudo sh -c 'umask 077; systemd-creds encrypt --name=telegram_bot_token - /etc/credstore.encrypted/telegram_bot_token.cred'`

Then paste the **current** BotFather token into that terminal's stdin and finish input with EOF (Ctrl-D).

Do not paste the token into ChatGPT, GitHub, project files, shell command arguments or chat messages.

This creates an encrypted, root-controlled persistent credential source outside project artifacts. SIS must verify the resulting file identity/permissions before use. This step does not start a service and does not send anything to Telegram.

## Exact next read-only verification after provisioning
A separately authorized SIS pass should load the encrypted credential into an ephemeral systemd credential directory and perform only these Telegram Bot API methods:

1. `getMe`
   - require bot username exactly `WBNP_Media_Bot`;
   - record bot numeric `id` only.

2. `getChat(chat_id="@wbnp_pev5691_15042026")`
   - record exact numeric channel `id`;
   - require channel username/key match;
   - read `linked_chat_id` if present.

3. `getChatMember(chat_id=<channel_numeric_id>, user_id=<bot_numeric_id>)`
   - require membership status `administrator`;
   - verify effective `can_post_messages=true`;
   - record other returned admin rights only as factual readback, without changing them.

4. If `linked_chat_id` exists:
   `getChat(chat_id=<linked_chat_id>)`
   - resolve exact discussion title/type/id and username if present.

All response capture must exclude the token and Authorization URL/path material from logs.

## Exact first bounded send + readback method
Not authorized or executed in this task.

After a separate explicit one-send authority and successful read-only mapping:

1. call `sendMessage` once using the verified numeric channel chat id and a synthetic, non-personal test payload;
2. automatic retries = `0`;
3. capture only the returned Telegram `message_id`, channel `chat.id`, and exact synthetic text/hash;
4. perform independent public readback at the public channel post locator
   `https://t.me/wbnp_pev5691_15042026/<message_id>`
   (or the equivalent public `/s/` preview when available);
5. compare exact message id/content/hash with the send response;
6. if public readback is unavailable, report readback blocked rather than substituting a second send.

A linked discussion group is not required for this first channel-only publishing check. It becomes mandatory before comments/discussion workflows.

## Boundary
No Telegram send, credential publication, channel-right mutation, webhook creation/change, moderation, service start, or production deployment occurred.

The current blocker is solely credential provisioning into SIS-controlled non-public storage.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: verify Telegram experimental channel/bot mapping without sending
СТАТУС: `BLOCKED_TELEGRAM_BOT_CREDENTIAL_NOT_PROVISIONED`
