# WEB: Telegram media gateway MVP architecture

status: working-architecture
implementation_status: not_started_by_WEB
scope: Telegram channel + linked discussion group + automated publication + feedback/metrics
production_changed: false
repository_settings_changed: false

## 1. Решение верхнего уровня

Для первого рабочего медиаконтура достаточно трёх компонентов:

1. Telegram-канал проекта;
2. связанная discussion-supergroup, которая даёт комментарии к постам;
3. Media Gateway — серверный сервис с Telegram Bot API, webhook, локальной БД и publication registry.

Смысловая схема:

`approved publication object`
`→ WEB canonical representation/readback`
`→ media event`
`→ Media Gateway`
`→ Telegram Bot API`
`→ channel post`
`→ Telegram auto-forward to linked discussion group`
`→ comments/reactions webhook`
`→ private metrics/feedback store`
`→ aggregated metrics + selected feedback back into project`

Сайт/public-web остаётся candidate canonical presentation hub. Telegram является derivative/distribution surface, а не самостоятельным source-of-truth.

## 2. Что Telegram даёт штатно

### Канал и discussion group

Telegram позволяет связать broadcast channel с discussion group. Каждый пост канала автоматически пересылается в связанную supergroup и становится корнем отдельного comment thread.

Официальная документация:
`https://core.telegram.org/api/discussion`

Для автоматического forward Bot API Message содержит:
- `is_automatic_forward=true`;
- `forward_origin`;
- для origin type `channel`: исходный channel chat + original `message_id`.

Это позволяет надёжно связать:

`channel_message_id ↔ discussion_root_message_id`.

### Публикация ботом

Bot API `sendMessage`, `sendPhoto`, `sendDocument`, `sendVideo` и другие методы принимают channel `@username` или numeric chat id.

Reference:
`https://core.telegram.org/bots/api#sendmessage`

### Редактирование и удаление

Bot API поддерживает edit methods для уже отправленных сообщений.

Удаление возможно в пределах прав/ограничений Bot API; для channel bot с `can_post_messages` можно удалять собственные outgoing channel posts, а право `can_delete_messages` расширяет управление.

References:
`https://core.telegram.org/bots/api#editmessagetext`
`https://core.telegram.org/bots/api#deletemessage`

### Реакции

Bot API может получать:
- `message_reaction`;
- `message_reaction_count`.

Для этого bot должен быть administrator и эти update types надо явно добавить в `allowed_updates`.

### Комментарии

Bot administrator in a group receives all group messages. Комментарии к channel post являются обычными replies/thread messages в linked discussion supergroup.

Reference:
`https://core.telegram.org/bots/features#privacy-mode`

### Member counts

`getChatMemberCount` возвращает количество участников channel/supergroup.

## 3. Важная граница статистики

### Что можно собрать через Bot API в MVP

- publication delivery success;
- channel message id;
- linked discussion root id;
- reaction events/counts;
- comments/replies;
- edit/delete events, доступные bot updates;
- channel subscriber count snapshots;
- discussion group member count snapshots;
- comment count;
- unique commenters count, если KAN разрешает хранение/псевдонимизацию user ids;
- moderation actions;
- publication correction/withdrawal state.

### Что Bot API не даёт

В текущем Bot API Message отсутствует post view counter.

Поэтому **просмотры постов не входят в Bot API MVP**.

### Advanced stats, отдельный второй контур

Полная Telegram channel statistics доступна через MTProto API, например:

`stats.getBroadcastStats`

Она включает follower dynamics, views per post, shares per post, reactions per post и graphs.

Официальная документация прямо указывает:
`stats.getBroadcastStats` — only users can use this method.

Кроме того, detailed stats доступны только администраторам channel определённого сервером размера через `can_view_stats`.

Reference:
`https://core.telegram.org/api/stats`
`https://core.telegram.org/method/stats.getBroadcastStats`

Следовательно, advanced views/stats collector нельзя прятать внутрь обычного bot publisher.

Правильная граница:

`Bot API media-gateway = MVP mandatory`
`MTProto user-session stats collector = optional Stage 2 after SIS+KAN review`

## 4. Bootstrap Telegram surface

### Recommended MVP bootstrap

Одноразово через обычный Telegram client под владельцем проекта:

1. создать или подтвердить project channel;
2. создать или подтвердить discussion supergroup;
3. связать discussion group с channel;
4. создать publisher bot через @BotFather;
5. добавить bot administrator в channel;
6. добавить bot administrator в discussion group;
7. передать bot token только SIS-controlled runtime secret store;
8. сохранить channel/group numeric IDs и usernames в private runtime config.

Bot token не попадает в GitHub.

### Почему это одноразовый human bootstrap

Bot API не предоставляет обычному bot методы создания channel/group и связывания discussion group.

Raw Telegram client API имеет `channels.createChannel` и `channels.setDiscussionGroup`, но это уже MTProto user-account automation с phone login/session credentials.

Для первого запуска такая автоматизация дороже и опаснее, чем одноразовая UI-настройка.

Позже, если будет реальная необходимость массово создавать media surfaces, KOD/SIS/KAN могут отдельно оценить MTProto provisioning tool.

## 5. Минимальные bot permissions

### Channel

Required candidate rights:
- `can_post_messages`;
- `can_edit_messages` — если gateway должен исправлять published derivative;

Optional:
- `can_delete_messages` — только если approved withdrawal/moderation policy требует deletion.

Не давать:
- promote admins;
- change info;
- invite users;
- stories;
- прочие права без задачи.

### Discussion supergroup

Bot должен быть administrator, чтобы получать все messages независимо от group privacy mode.

Required:
- receive all messages as admin;

Optional only for moderation:
- `can_delete_messages`;
- `can_restrict_members`.

Для первого MVP auto-ban не нужен.

## 6. Webhook

Media Gateway exposes:
`POST /telegram/webhook`

Telegram `setWebhook` должен использовать HTTPS и `secret_token`.

Каждый request проверяется по:
`X-Telegram-Bot-Api-Secret-Token`.

Recommended `allowed_updates`:

```json
[
  "channel_post",
  "edited_channel_post",
  "message",
  "edited_message",
  "message_reaction",
  "message_reaction_count",
  "my_chat_member",
  "chat_member"
]
```

`chat_member` можно исключить, если MVP считает только periodic member-count snapshots.

Gateway обязан deduplicate updates по `update_id`.

Reference:
`https://core.telegram.org/bots/api#setwebhook`

## 7. Publication flow

### Input contract

Gateway принимает только publication object, уже прошедший upstream gates.

Минимум:

- `publication_id`;
- `content_layer`;
- exact source commit/blob;
- canonical URL;
- canonical readback PASS;
- KOO release/routing locator;
- target channel;
- renderer/version;
- derivative payload;
- correction policy;
- status `approved_for_distribution` или эквивалент, определённый RED/KOO.

### Event

Candidate event:
`publication.published`

Событие создаётся только после canonical WEB deploy + readback.

### Delivery

Gateway:

1. validates idempotency key `publication_id + target_channel`;
2. stores job as `prepared`;
3. renders Telegram derivative;
4. sends via Bot API;
5. stores returned channel `message_id`;
6. waits for channel_post/webhook echo where applicable;
7. maps auto-forwarded discussion root;
8. marks channel delivery `verified`; 
9. emits delivery receipt back into project-controlled storage.

Deploy/send without saved Telegram message id != verified delivery.

## 8. Discussion mapping

When linked discussion is configured, channel post is automatically forwarded to supergroup.

Webhook receives the group message with:
- `is_automatic_forward=true`;
- `forward_origin.type=channel`;
- `forward_origin.chat.id = channel id`;
- `forward_origin.message_id = original channel message id`.

Gateway stores:

`publication_id`
`channel_chat_id`
`channel_message_id`
`discussion_chat_id`
`discussion_root_message_id`

All replies with matching thread/root map back to the same `publication_id`.

## 9. Comments and discussion operation

### MVP policy

Discussions stay native Telegram threads.

Bot does NOT try to replace Telegram UI with its own comment system.

Gateway roles:
- observe;
- count;
- classify technical metadata;
- provide moderation hooks;
- preserve selected feedback when explicitly promoted;
- build digests.

### Important separation

`comment in Telegram` != `project source`.

A comment becomes a project feedback object only after explicit moderator/profile capture.

Candidate moderator command:
`/capture` as reply to a comment.

Alternative later:
inline moderator button in private/admin UI.

Captured feedback object should contain:
- publication_id;
- Telegram chat/message locator;
- exact text or approved extract;
- capture reason;
- capturing moderator;
- privacy state;
- destination profile;
- immutable local record id.

Raw audience comments must never be pushed automatically to public GitHub.

## 10. Moderation

### MVP

Human-first moderation.

Bot may:
- detect obvious flood/rate anomalies;
- flag suspicious links/duplicate spam;
- produce moderator queue;
- delete only after explicit moderator action unless a future KAN/RED moderation policy defines safe automatic classes.

No autonomous semantic moderation or account bans in v0.1.

### Discussion rules

RED/KAN should produce short public rules covering:
- topic relevance;
- abuse/harassment;
- spam;
- personal data;
- illegal content;
- promotion/advertising;
- corrections;
- use of comments as possible project feedback.

## 11. Statistics model

### Per publication

Store:
- channel message id;
- publish timestamp from Telegram event;
- current reaction counts by emoji/type;
- total comments;
- unique commenters if privacy policy allows;
- first/last comment time;
- moderation counts;
- corrections/edits;
- discussion root;
- delivery/readback status.

### Per channel/day

Store:
- channel member count snapshot;
- discussion group member count snapshot;
- publications count;
- comments count;
- reactions count;
- active discussion threads;
- captured feedback count.

### Not in MVP

- post views;
- shares;
- detailed audience geography/language;
- Telegram native graph analytics.

Those require MTProto user statistics and separate authority/security.

## 12. Data storage

### Private runtime database

Recommended MVP:
SQLite for one-instance sandbox; PostgreSQL if KOD/SIS expect multiple workers/high availability.

Core tables candidate:

`publications`
`telegram_deliveries`
`discussion_threads`
`reaction_snapshots`
`comment_events`
`member_snapshots`
`moderation_events`
`feedback_captures`
`webhook_updates_dedupe`

### Public GitHub storage

Only aggregated/public-safe artifacts:
- publication receipt;
- external message URL/id;
- counts without personal identities;
- approved captured feedback summaries;
- health/status reports.

Never:
- bot token;
- Telegram session;
- raw private user identifiers;
- raw comment database;
- webhook secret.

## 13. Retention/privacy

Exact raw-comment retention requires KAN decision.

Safe candidate until KAN decides:
- raw comments remain in private runtime only;
- do not export usernames/user ids to public repo;
- permanent project preservation only for explicitly captured/approved feedback;
- aggregate metrics may be retained longer;
- deletion request handling must be specified before production.

## 14. Corrections and withdrawal

### Correction

Canonical source changes only through normal RED/KOO/publication lifecycle.

After new canonical readback:
- gateway edits Telegram derivative when technically/semantically safe;
- stores previous payload hash/version;
- writes correction receipt.

### Withdrawal

Withdrawal should prefer explicit status/correction notice over silent deletion when possible.

Actual deletion requires KOO/RED/KAN policy and Bot API rights/time-window constraints.

## 15. Reliability

Required:
- queue/outbox;
- idempotency;
- exponential retry;
- webhook update dedupe;
- health endpoint;
- structured logs without secrets;
- backup of runtime DB;
- startup recovery;
- dead-letter queue;
- delivery state machine;
- periodic `getWebhookInfo` health check;
- periodic `getChatMemberCount` snapshots.

## 16. Proposed service endpoints

Internal candidate API:

`POST /v1/publications` — enqueue approved publication derivative;
`GET /v1/publications/{id}` — delivery state;
`POST /v1/publications/{id}/correct` — approved correction;
`POST /v1/publications/{id}/withdraw` — approved withdrawal request;
`POST /telegram/webhook` — Telegram updates;
`GET /healthz` — service health;
`GET /metrics` — operational metrics, protected/private.

Project automation may later call this API from GitHub Action using a separate signed gateway credential.

Bot token stays server-side and is never placed in GitHub Actions.

## 17. MVP phases

### Phase 0 — code without Telegram credentials

KOD builds:
- publication registry;
- renderer;
- delivery state machine;
- Telegram API adapter interface;
- webhook parser;
- automatic-forward mapping;
- comments/reactions aggregator;
- fake Telegram adapter and fixtures;
- tests.

PASS does not require external Telegram yet.

### Phase 1 — private Telegram sandbox

One-time bootstrap creates:
- private test channel;
- linked discussion group;
- test publisher bot.

SIS deploys gateway with real token/webhook.

Test sequence:
1. synthetic approved publication;
2. bot publishes;
3. auto-forward appears in discussion;
4. human makes comments;
5. human reactions are added;
6. gateway records thread/reactions/comments;
7. correction test;
8. restart recovery test;
9. duplicate event test;
10. export safe receipt/metrics artifact.

### Phase 2 — project production media surface

Only after KOO acceptance of Phase 1 and RED/KAN/SIS boundaries:
- confirm/create real project channel;
- confirm/create linked discussion group;
- production bot or promoted sandbox bot;
- public rules;
- canonical public-web event integration;
- first real publication.

### Phase 3 — advanced analytics

Optional MTProto user-session stats collector for:
- views;
- shares;
- native Telegram stats graphs.

Requires separate SIS/KAN review because it stores user-account session credentials and uses user-only API methods.

## 18. MVP acceptance

PASS only if:

1. exact publication id maps to exact channel message id;
2. linked discussion root maps back to same publication;
3. comments are received and counted;
4. reactions are received/countable;
5. member snapshots work;
6. duplicate publication event does not create duplicate Telegram post;
7. bot token/webhook secret absent from GitHub/logs;
8. restart does not lose delivery state;
9. correction produces verifiable state/version;
10. public artifact contains no audience personal data;
11. delivery receipt can be read back independently;
12. no production publication is claimed from sandbox.

## 19. What remains profile-owned

RED:
- publication object;
- derivative length/style;
- discussion/editorial rules;
- correction language.

KAN:
- privacy/data retention;
- Telegram platform/legal review;
- audience comment preservation boundaries;
- moderation legal boundary.

SIS:
- runtime;
- HTTPS/webhook;
- secret storage;
- monitoring/backups;
- network/TLS;
- later MTProto stats security.

KOD:
- Media Gateway implementation;
- DB;
- Bot API adapter;
- webhook parser;
- state machine;
- tests;
- GitHub/publication event adapter.

WEB:
- canonical URL/readback;
- channel derivative renderer requirements;
- publication/message mapping;
- media routing and visible status;
- cross-channel consistency.

KOO:
- sequence/acceptance;
- cross-profile conflicts;
- authorization of sandbox → production transition.

## 20. Current evidence and references

Telegram official:
- https://core.telegram.org/bots/api
- https://core.telegram.org/bots/features
- https://core.telegram.org/api/discussion
- https://core.telegram.org/api/stats
- https://core.telegram.org/method/stats.getBroadcastStats

Project:
- `entities/webmaster/current/webmaster-library/MEDIA-CONTOUR.md`;
- `entities/webmaster/current/webmaster-library/PUBLICATION-AUTOMATION.md`;
- `entities/webmaster/current/webmaster-library/PUBLICATION-FIXTURE-001.md`;
- `entities/webmaster/outbox/WEB__media-contour-structure-routing__KOO.md`;
- `entities/webmaster/outbox/WEB__media-contour-historical-evidence__KOO.md`.

## 21. Короткая фиксация опыта

Идея → не считать Telegram «ещё одним местом, куда копируем текст», а сделать технически трассируемый publication/feedback transport.

Проба → сверены official Bot API, linked discussion behavior, reactions, webhook security and MTProto statistics boundary.

Результат → Bot API покрывает publishing/comments/reactions/member snapshots; post views and native detailed stats требуют отдельного user-session MTProto layer.

Решение-кандидат → запускать два уровня: Bot API MVP сейчас, advanced MTProto stats later only if justified.

---
created_by: WEB
document_type: telegram-media-gateway-mvp-architecture
purpose: technical working architecture for Telegram channel/discussion automation and measurable feedback
project_time: not_recorded_no_trusted_source