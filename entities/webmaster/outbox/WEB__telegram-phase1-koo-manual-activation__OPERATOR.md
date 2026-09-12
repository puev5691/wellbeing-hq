# WEB → OPERATOR: единая ручная активация KOO по Telegram Phase 0/1

## Требуемое действие

Открыть/активировать существующий чат KOO / КООРДИНАТОР и дать одну команду:

`Продолжай работу. Обработай два входящих WEB: WEB__telegram-phase0-verify-phase1-mapping__KOO.md и WEB__telegram-experimental-surface-public-readback__KOO.md. Зафиксируй Phase 0 review/acceptance или defect и выдай следующий bounded Phase 1 шаг.`

Файлы вручную переносить не нужно.

## Почему это требуется

Оба адресных входящих доставлены в KOO inbox и обнаружены activation detector.

### Input 1

`entities/koordinator/inbox/WEB__telegram-phase0-verify-phase1-mapping__KOO.md`

Activation record:
`routes/activation/WEB__telegram-phase0-verify-phase1-mapping__KOO.activation.md`

State:
- `detector_status: PASS`;
- `activation_requested: yes`;
- `processing_started: no`;
- `activation_status: activation_failed`;
- `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`;
- `operator_manual_ping_required: yes`.

### Input 2

`entities/koordinator/inbox/WEB__telegram-experimental-surface-public-readback__KOO.md`

Activation record:
`routes/activation/WEB__telegram-experimental-surface-public-readback__KOO.activation.md`

State identical:
- detector PASS;
- processing not started;
- exact KOO chat resume unsupported;
- manual ping required.

## What KOO will find

### Independent Phase 0 verification

WEB independently reran exact KOD package:

`entities/koder/outbox/telegram-media-phase0-v01/`
package_commit: `df287f89410adb1b935e5123ec7abd9ddb37795c`

Result:
- `14/14 PASS`;
- exit code `0`;
- manifest blob ids/sizes match;
- no Telegram credential/network dependency required by Phase 0.

WEB verdict:
`PASS_REPRODUCED_BY_WEB`

### Phase 1 conditions

Real send remains blocked on:
- KOD real Telegram adapter/config;
- SIS runtime/secrets/webhook;
- KAN privacy/comment-retention;
- verified Telegram admin/channel/discussion mapping.

### Experimental target readback

Target:
`https://t.me/wbnp_pev5691_15042026`

WEB verified:
- HTTP 200;
- public `/s/` preview exists;
- title `Медиа Благополучие`;
- public posts visible;
- channel public state = `PUBLIC_VERIFIED`.

Still unknown:
- numeric chat id;
- admin control;
- linked discussion state/id;
- bot state/rights.

## Expected KOO action

1. Review/accept/revise WEB independent Phase 0 result.
2. Do not infer unknown Telegram-side admin facts.
3. Open bounded Phase 1 preparation only if Phase 0 review passes.
4. Assign exact next profile tasks for KOD/SIS/KAN/WEB as required.
5. Keep first real send synthetic/experimental and readback-verified.

## Stop conditions

This manual activation does not authorize:
- unattended production publication;
- bot token in GitHub;
- MTProto user session;
- raw audience data export;
- destructive moderation;
- claim of linked discussion before Telegram-side evidence.

---
created_by: WEB
to_entity: operator
document_type: combined-manual-activation-dependency
status: action_required
purpose: activate KOO once for both delivered Telegram Phase 0 verification and experimental-surface readback inputs
project_time: not_recorded_no_trusted_source