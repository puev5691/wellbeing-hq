# KOO → KOD: Telegram Media Gateway Phase 1A

status: TASK
scope: REAL_ADAPTER_AND_CONFIG_PREPARATION_ONLY
production: no
telegram_network_calls: forbidden
real_credentials: forbidden

## Goal

Prepare a new immutable Phase 1A package that removes Phase 0 fixture assumptions and introduces a real-adapter/configuration boundary suitable for later SIS/KAN-controlled sandbox integration.

This task does NOT perform a real Telegram send.

## Basis

Phase 0 decision:
`entities/koordinator/outbox/KOO__telegram-media-phase0-review__KOD.md`
commit: `5570c78beb0b304a078c2ea7de20ed104cca319d`
blob: `b3d100c960c4c502748ff8c61e9f1db4b1ed2830`

WEB mapping result:
`entities/webmaster/outbox/WEB__telegram-phase0-verify-phase1-mapping__KOO.md`
commit: `4c8bb86d32a191b0cec3604faf7c152e5e7c2cee`

Verified experimental target:
`https://t.me/wbnp_pev5691_15042026`

Public facts:
- `public_state = PUBLIC_VERIFIED`;
- `public_title = Медиа Благополучие`.

Still UNKNOWN and must remain fail-closed:
- channel numeric chat id;
- admin control;
- linked discussion;
- discussion numeric chat id;
- publisher bot;
- bot rights;
- webhook configuration.

## Required Phase 1A changes

### 1. Runtime configuration

Remove real-path dependence on synthetic IDs.

Introduce explicit runtime config schema for:
- channel username/key;
- verified channel chat id;
- discussion linked state;
- verified discussion chat id;
- bot identity metadata without secret value;
- webhook endpoint metadata without secret;
- environment/sandbox marker.

No synthetic Phase 0 chat id may be a default for a real adapter.

### 2. Composite external identity

Replace any real-path lookup by bare `message_id` with at least:

`(chat_id, message_id)`.

Delivery identity must support:

`publication_id + distribution_target + external_chat_id + external_message_id`.

### 3. Auto-forward validation

Real adapter mapping must require:
- `forward_origin.type == channel`;
- `forward_origin.chat.id == configured channel_chat_id`;
- `forward_origin.message_id == stored channel_message_id`.

No discussion binding by message id alone.

### 4. Delivery verification

Replace synthetic blind `verify_echo(publication_id)` semantics on the real path.

Real-path `delivered_verified` requires evidence matching:
- configured channel chat id;
- returned Telegram message id;
- expected publication/delivery record.

The fake adapter path may remain for tests.

### 5. Multi-target-safe schema

Do not assume one global discussion mapping per publication.

Schema must permit more than one distribution target for the same canonical publication.

### 6. Real adapter interface

Implement a Telegram Bot API adapter boundary/interface with:
- send;
- edit;
- member-count query;
- webhook/update ingestion contract;
- configuration validation.

For this task the real adapter must be testable using a fake HTTP transport or injected client.

No live Telegram request is allowed.

### 7. Privacy fail-closed boundary

Because KAN has not yet approved real audience-data retention:
- real comment ingestion mode must be disabled by default OR configured to discard/minimize identity beyond immediate processing;
- raw user ids/names/comments must not be exported publicly;
- package must make the KAN dependency explicit.

Do not invent the final retention policy.

### 8. Canon-complete package manifest

The new Phase 1A immutable package must correct the Phase 0 manifest metadata defect.

Manifest must explicitly include:
- package_id;
- source_location;
- generated_files;
- recipients;
- copied_to;
- integrity/immutable identity information;
- operator_action;
- unresolved_questions;
- status;
- service footer.

Do not rewrite the old Phase 0 package.

## Required tests

At minimum add tests proving:
- real-path config rejects UNKNOWN/missing channel chat id;
- synthetic Phase 0 IDs cannot silently enter real config;
- same message_id in two chats does not collide;
- auto-forward with wrong origin chat is rejected;
- auto-forward with wrong origin message is rejected;
- delivery verification cannot flip state on mismatched chat/message;
- multiple targets for one publication remain distinct;
- real adapter uses injected fake transport and makes zero live network calls;
- privacy default does not publicly export audience identity;
- old Phase 0 positive behavior remains reproducible where compatible.

## Required result

Return:
- one new immutable Phase 1A package commit;
- canon-complete manifest;
- exact dependency versions;
- exact test command and summary;
- explicit zero-live-network evidence;
- explicit zero-real-credential evidence;
- known limitations;
- exact external dependencies for later Phase 1B real sandbox.

Route:
`KOD outbox → KOO inbox pointer → dispatch → readback`.

Do not claim Phase 1 PASS or real Telegram readiness.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подготовить безопасный real-adapter/config слой до SIS/KAN и первого реального Telegram sandbox send
СТАТУС: assigned
