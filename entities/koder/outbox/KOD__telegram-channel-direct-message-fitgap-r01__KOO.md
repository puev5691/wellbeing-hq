# КОДЕР → КОО: первое обращение каналу и существующий Telegram runtime — fit-gap r0.1

status: PASS_KOD_TELEGRAM_CHANNEL_DIRECT_MESSAGE_FITGAP_R01_READ_ONLY
scope: DOCUMENTARY_READ_ONLY_RECONCILIATION
project_time: omitted; trusted project-time source not used

## Человеческий вывод

Наблюдение ОПЕРАТОРА подтверждает, что посетитель может открыть диалог **с каналом**, а человек-администратор может ответить в этом диалоге. Это согласуется с Telegram Channel Direct Messages. Оно не доказывает, что конкретный бот получил update, имеет фактический доступ к сообщениям канала, или что установленная служба способна отправить ответ. В проектном коде нет ветви обслуживания такого обращения. Принятая Phase 1B служба после ограниченного fake-transport теста оставлена disabled/inactive, real transport в `runtime_app.py` сознательно возвращает `real_transport_not_implemented_in_r01` даже при наличии credentials.

## Resume-First и exact входы

Fresh HQ preflight HEAD: `88425c82fdf4575e26a2b677a26a91d669ea2ef8`, tree `586b9ad563d0630e300874851450f4ad0d054baa`, recursive tree `truncated=false` (5318 entries). Действующий KOD writer v0.5: `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`; v0.4 freeze остаётся. Прямое поручение ОПЕРАТОРА ограничено read-only fit-gap. Более нового конкурирующего результата именно о личном обращении **каналу** и его обработке ботом в свежем дереве не обнаружено. Исторические задачи обсуждения и live-ingest не replay.

Шесть действующих approved Project Sources загружены из предоставленных экземпляров; blob: recovery `233117e1c9509d730e1f5ec532b1cabe3f786609`, roles `1772339cb74dae8550bfbd2e33401c34a929e911`, source-loading `69eb657f260a019f76e8e707c880ea88c1dfa0bf`, file-work `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`, task-conveyor `df7896d867eeeffff506319538fedad938856686`, core `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`.

1. Accepted runtime: `puev5691/wellbeing-hq@b939a238f757be0bcfaf1bb4164b0362eafc088f:entities/koder/outbox/telegram-media-phase1b-runtime-r01/runtime_app.py`, blob `f2987f880a25b5e295fd94eadb6447fd2438054d`.
2. Accepted gateway: `puev5691/wellbeing-hq@62f82c3322f28adc55b47b1a7064fccb23e4c351:entities/koder/outbox/telegram-media-phase1b-threading-fix-r02/gateway.py`, blob `c870616f119fa3198a50db31898ad9ba4ad4bafc`.
3. Host result: `puev5691/wellbeing-hq@b89ef70174483a986b1e526d7360b23bc0d54724:entities/sisadmin/outbox/SIS__telegram-phase1b-accepted-runtime-companion-restore-r01__KOO.md`, blob `73c46fb57e002f0fa6c65bb3af967d3dea1f5d23`.
4. Historical discussion send: `puev5691/wellbeing-hq@09b6fdfd04da84533185b11b0861b2220b72dfb3:entities/sisadmin/outbox/SIS__telegram-discussion-probe-r01__WEB-KOO.md`, blob `4061938c616f76b1cb48cf882fe907b2c25da666`; one-send authority consumed.

Other relevant work is distinct: `KOD__telegram-live-ingest-prep-r01-result__KOO.md` is a preparation contract for bounded **discussion** read, with live authority NOT_GRANTED; facilitator normalized-event bridge converts aggregate `safe_receipt()`, not a raw incoming direct message. Neither supplies a direct-message responder.

## Telegram API route distinction

Official reference: https://core.telegram.org/bots/api and https://core.telegram.org/bots/features#channel-direct-messages-and-suggested-posts (read-only documentation). Telegram describes a channel direct-messages chat with topics; `Chat.is_direct_messages`, `ChatFullInfo.parent_chat`, `Message.direct_messages_topic.topic_id` distinguish it, and `sendMessage` to that chat requires `direct_messages_topic_id`. `Update.message` is an incoming message; `Update.channel_post` is a channel publication. `can_manage_direct_messages` is a channel administrator right, not proof of received update. `message_thread_id` is for forum/private-chat topic mode and is not a substitute for `direct_messages_topic_id` in a direct-messages chat.

| Route | Project observation / evidence | Existing code |
|---|---|---|
| Visitor → channel direct-messages chat/topic | User-facing dialog with channel and human reply OBSERVED. Direct-messages interpretation strongly supported by UI and official feature description; exact Bot API update shape, chat/topic IDs and bot receipt UNKNOWN. | No `is_direct_messages`, `parent_chat`, `direct_messages_topic`, `direct_messages_topic_id` parsing/routing. No same-topic reply. |
| Comment → linked discussion supergroup | Separate historical one-send to linked group verified; no evidence visitor used comments in this case. | `is_automatic_forward` maps discussion root; `_comment()` counts an already mapped thread. No reply to incoming comment. |
| Visitor → private chat with @WBNP_Media_Bot | Bot username visible, but visitor did not demonstrably open the bot's private chat. Receipt UNKNOWN. | `_comment()` rejects unknown thread; adapter `send()` targets channel ID, never inbound private chat ID. |
| Channel publication → `Update.channel_post` | No channel publication asserted as this visitor's message. | `ingest_update()` uses `message` and reaction count; other update types, including `channel_post`, are ignored after update-ID dedupe. |

No visitor message text, identity or chat/topic identifier is retained here.

## Code fit and concrete gap

`RuntimeApplication.handle_payload_bytes()` can parse bounded JSON POST at loopback `/telegram/webhook`, forwards it to `Gateway.ingest_update()`, returns HTTP outcome, and logs only closed aggregate fields. This is a tested **synthetic** path, not an external webhook. `Gateway` dedupes `update_id`, maps auto-forwarded channel publications into discussion threads, counts comments/reactions, and stores aggregate counts without raw comment text. `TelegramBotAdapter.send(text)` calls `sendMessage` with the configured **channel_chat_id**, for publishing to the channel; `edit()` changes a known delivery. There is no inbound direct-message classification, channel-parent verification, per-visitor topic routing, reply content policy, or reply result evidence. For an unknown `message` without mapped discussion root, `_comment()` raises `comment_unknown_thread` and HTTP handler returns 422; no same-dialog answer.

Current host evidence says one fake-transport HTTP POST passed and the installed sandbox service was left disabled/inactive, listener absent, DB absent. `build_transport('real')` has no network transport implementation and blocks. The historical discussion result proves one authorized send to the **discussion supergroup** and exact bot identity there; it neither proves a channel direct-message update nor authorizes another call. Even a visible administrator checkbox is not a Bot API receipt or a verified live right.

Thus the nearest **code** gap is a distinct direct-message intake and same-topic reply adapter, preceded by verified update chat/topic/parent identity and explicit message-handling/privacy authority. The nearest **diagnostic** uncertainty is earlier: whether the exact bot has effective channel direct-message access and any functioning update delivery path at all. Repository contents cannot decide that or interpret the inconsistent UI rights message.

## One next diagnostic gate for KOO decision — not executed

Executor: SIS, because it owns technical service/transport verification, after separate exact OPERATOR authority. A bounded **read-only** status check of (a) non-secret service/config/listener state on the verified host, (b) the exact bot's webhook configuration/allowed updates/error counters via `getWebhookInfo`, and (c) its channel administrator right `can_manage_direct_messages` via `getChatMember` for the verified bot/channel identities. No `getUpdates` (it can change update-consumption position and conflicts with webhook), no raw updates, no message content, no visitor identifiers, no sends, no webhook/rights change. One bounded read per named API endpoint, retries=0, no fallback, privacy-safe boolean/status report only. Bot API calls require separate credential-use authorization and host status check requires separate host read authority; neither is granted by this document. SIS must not print/log credential values. If either independent identity, authority or access is missing, return exact BLOCKED. An effective right or configured webhook would still **not** prove that the past visitor's update reached the bot; that would need a later separately authorized privacy-bounded live ingress observation. The diagnostic is proposed solely to decide whether implementation or ingress repair comes first.

No profile implementation, live bot connection, Telegram/API request, host access, provider call, token read, rights mutation or visitor reply was done. Historical one-send permission was not reused; memory-layering attempt 3 remains NOT_AUTHORIZED. Publication/dispatch does not imply KOO receipt or any visitor response.

## Terminal

`PASS_KOD_TELEGRAM_CHANNEL_DIRECT_MESSAGE_FITGAP_R01_READ_ONLY`

One next gate: `SIS_BOUNDED_READ_ONLY_BOT_ACCESS_AND_WEBHOOK_STATUS_DIAGNOSTIC`, requiring new exact OPERATOR authority. Subsequent code work is not authorized by this result.

from_entity: koder
to_entity: koordinator
