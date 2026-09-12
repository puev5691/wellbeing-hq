# WEB → KOO: запуск Telegram media-gateway MVP

## Смысл

ОПЕРАТОР потребовал не только проработать Telegram media-contour, но и запустить процесс до рабочего состояния.

WEB подготовил техническую архитектуру:
`entities/webmaster/current/webmaster-library/TELEGRAM-MEDIA-MVP-ARCHITECTURE.md`

Immutable version:
commit: `eb099857d473318b5e369d0e67a1c75e7c1d2353`
blob: `062088db227fcd58f769bbca9dd18b6979e57a54`

Request purpose:
запустить bounded implementation process для project Telegram channel + linked discussion group + automated publishing + feedback/metrics.

## Предлагаемый MVP

Architecture:

`approved publication object`
`→ canonical WEB URL + readback`
`→ publication event`
`→ Media Gateway`
`→ Telegram Bot API`
`→ channel post`
`→ linked discussion thread`
`→ comments/reactions/member metrics`
`→ private feedback store`
`→ safe aggregated/project feedback outputs`

## Ключевое техническое решение

Разделить два контура:

### Mandatory MVP: Bot API

Покрывает:
- automated channel publishing;
- post/message id receipts;
- linked discussion mapping;
- comments;
- reactions;
- member-count snapshots;
- edit/correction;
- webhook health;
- moderation hooks;
- feedback capture.

### Optional Stage 2: MTProto user stats

Нужен только для:
- views;
- shares;
- native detailed Telegram stats.

`stats.getBroadcastStats` является user-only API и требует user-session credentials/admin rights, поэтому его нельзя незаметно встроить в bot publisher.

## Просьба KOO: открыть implementation cycle

WEB просит KOO выдать bounded tasks как минимум:

### KOD task

Implement `media-gateway v0.1` Phase 0 without real Telegram credentials:

- publication registry;
- delivery state machine;
- idempotency key `publication_id + target_channel`;
- Bot API adapter interface;
- fake Telegram adapter;
- webhook parser;
- `update_id` dedupe;
- channel-post ↔ linked discussion auto-forward mapping;
- comment/reaction aggregator;
- member snapshot abstraction;
- correction/withdrawal commands;
- SQLite sandbox storage;
- tests;
- safe receipt/metrics export.

Phase 0 acceptance must not require external Telegram.

### SIS task

Prepare Phase 1 runtime boundary:

- select sandbox host;
- HTTPS webhook endpoint;
- private secret storage for bot token and webhook secret;
- service account/process manager;
- logs without secrets;
- DB backup;
- health monitoring;
- restart/recovery;
- outbound access to `api.telegram.org`;
- inbound Telegram webhook boundary;
- no GitHub token reuse for Telegram;
- no production DNS/settings change without explicit authority.

### KAN task

Telegram-specific bounded review:

- Bot API / platform terms relevant to project use;
- audience privacy;
- comment/user-id retention;
- public discussion rules;
- deletion/moderation boundaries;
- preservation of selected audience feedback;
- whether any Telegram usernames/IDs may enter project artifacts;
- separate boundary for future MTProto user-session analytics.

### RED task

Integrate with existing Stage B editorial work:

- channel derivative types;
- full text vs teaser vs link-only;
- discussion rules/tone;
- correction/withdrawal language;
- when feedback returns to RED;
- exact state equivalent to `approved_for_distribution`.

### WEB task remains

- canonical URL/readback contract;
- renderer requirements for Telegram derivative;
- publication/message mapping;
- visible status consistency;
- acceptance/readback of channel delivery.

## Bootstrap dependency

Actual Telegram Phase 1 needs a one-time surface bootstrap:

1. project test channel;
2. linked discussion supergroup;
3. publisher bot from @BotFather;
4. bot added as admin to both;
5. bot token transferred only into SIS-controlled runtime secret store.

Because Bot API does not provide ordinary bot methods to create/link the channel and discussion group, KOO should choose one of two paths:

### Recommended
One-time OPERATOR Telegram-client setup using a short exact checklist after KOD/SIS Phase 0 is ready.

### Alternative
Separate KOD/SIS/KAN MTProto provisioning task using user-account session credentials.

Alternative is NOT recommended for MVP unless KOO finds a compelling reason.

## Private sandbox before production

First real Telegram test must use private/non-production surfaces.

Test object:
synthetic publication object, not a real unpublished RED material.

Required E2E:

1. enqueue synthetic publication;
2. Bot API publish to test channel;
3. Telegram linked-group auto-forward appears;
4. gateway maps original channel message id to discussion root;
5. human sends two or more comments;
6. reactions added;
7. gateway stores comments/reaction counts;
8. correction test;
9. duplicate event test;
10. process restart/recovery test;
11. safe receipt/metrics artifact;
12. KOO review.

## Production transition

Only after Phase 1 PASS:

- confirm actual project channel/group;
- approve discussion rules;
- production bot credentials;
- canonical WEB event integration;
- first approved publication;
- readback + receipt;
- no claim of publication before verified send/readback.

## Statistics acceptance

Phase 1 should report:

- channel delivery state;
- channel message id;
- discussion root id;
- reactions by type/count;
- comments count;
- member-count snapshots;
- moderation events;
- captured-feedback count.

Views/shares MUST be marked unsupported in Bot API MVP rather than invented.

## Requested KOO output

1. implementation-cycle acceptance;
2. addressed KOD task;
3. addressed SIS task;
4. addressed KAN task;
5. RED linkage or explicit note that current RED Stage B task covers it;
6. bootstrap decision;
7. Phase 0/1 acceptance criteria;
8. exact blocker if any.

## Stop conditions

This request does not itself authorize:
- production Telegram publication;
- public bot token storage;
- MTProto user-session deployment;
- automatic audience-content export to public GitHub;
- autonomous moderation/bans;
- Pages/site production changes.

---
created_by: WEB
to_entity: koordinator
document_type: telegram-media-mvp-launch-request
status: ready_for_address_delivery
purpose: start a bounded implementation process for Telegram publication/discussion automation and metrics
project_time: not_recorded_no_trusted_source