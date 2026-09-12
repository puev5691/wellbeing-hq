# WEB → OPERATOR: ручная активация KOO для Telegram media MVP

## Что требуется

Не переносить файлы и не пересылать содержимое.

Нужно только открыть/активировать существующий чат KOO / КООРДИНАТОРА и дать ему короткую команду обработать уже лежащее адресное задание:

`entities/koordinator/inbox/WEB__telegram-media-mvp-launch__KOO.md`

Рекомендуемая короткая команда в чате KOO:

`Продолжай работу. Обработай входящее WEB__telegram-media-mvp-launch__KOO.md и запусти bounded Telegram media MVP implementation cycle.`

## Почему это нужно

Activation record:
`routes/activation/WEB__telegram-media-mvp-launch__KOO.activation.md`

Current verified state:
- `detector_status: PASS`;
- `activation_requested: yes`;
- `processing_started: no`;
- `activation_status: activation_failed`;
- `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`;
- `operator_manual_ping_required: yes`.

То есть GitHub-доставка произошла, detector задачу увидел, но текущий adapter не умеет доказанно возобновить конкретный существующий KOO Entity-chat.

## Что уже готово и не требует ручной переноски

Architecture:
`entities/webmaster/current/webmaster-library/TELEGRAM-MEDIA-MVP-ARCHITECTURE.md`
commit: `eb099857d473318b5e369d0e67a1c75e7c1d2353`
blob: `062088db227fcd58f769bbca9dd18b6979e57a54`

Phase 0 exact test contract:
`entities/webmaster/current/webmaster-library/TELEGRAM-MVP-PHASE0-CONTRACT.md`
commit: `f548e269c3a4e1174e095f80d393baa675951155`

Launch request:
`entities/webmaster/outbox/WEB__telegram-media-mvp-launch__KOO.md`
commit: `741f5ea8e752cb9d62cd232c122f02bafb7cbb2d`
blob: `67a82d7d160f20b0b0cf808245ef9c03d135ac7a`

Stage B information-entry synthesis уже принят KOO, а bounded info-entry pilot r1 уже принят и передан SHD на cross-layer review. Поэтому Telegram ветка сейчас имеет достаточный подготовительный контекст для отдельного bounded implementation-cycle.

## Что KOO должен сделать после активации

1. Прочитать launch request и architecture/test-contract.
2. Выдать bounded KOD task на credential-free media-gateway Phase 0.
3. Выдать SIS task на Phase 1 runtime/webhook/secrets boundary.
4. Выдать KAN task на Telegram privacy/data-retention/moderation boundary.
5. Связать RED derivative/discussion policy с текущим editorial lifecycle.
6. При необходимости включить SHD как cross-layer verifier, не как замену KOD/SIS.
7. Вернуть exact acceptance/blockers/bootstrap decision.

## Stop conditions

Этот manual ping не разрешает:
- production Telegram publication;
- bot token в GitHub;
- создание MTProto user session;
- autonomous moderation/bans;
- создание public channel/group без отдельного решения;
- production site/settings mutation.

---
created_by: WEB
to_entity: operator
document_type: manual-activation-dependency
status: action_required
purpose: снять единственный подтверждённый activation blocker Telegram media MVP ветки без ручной транспортировки файлов
project_time: not_recorded_no_trusted_source