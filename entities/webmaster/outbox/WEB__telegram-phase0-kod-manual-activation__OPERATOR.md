# WEB → OPERATOR: ручная активация KOD для Telegram Media Gateway Phase 0

## Требуемое действие

Открыть/активировать существующий чат KOD / КОДЕР и дать ему короткую команду:

`Продолжай работу. Обработай входящее KOO__telegram-media-phase0__KOD.md и выполни Telegram Media Gateway Phase 0 по exact WEB contract.`

Ручной перенос файлов не нужен.

## Почему это требуется

KOO уже открыл bounded Telegram media MVP Phase 0 и адресно выдал KOD задачу:

`entities/koordinator/outbox/KOO__telegram-media-phase0__KOD.md`
task_commit: `b994d9a5cc9806a95c321f5ef6bcaaac11ae75f1`
task_blob: `20caec6a6aeaa7c38262e472e3a9fd48d0cccbcf`

KOD inbox pointer:
`entities/koder/inbox/KOO__telegram-media-phase0__KOD.md`
inbox_commit: `81d07d460c232a588d42a57f525502bc943d5a11`
inbox_blob: `40f52fdcc5f91ac92f0c89f586529d47da200644`

Dispatch:
`routes/dispatch/KOO__telegram-media-phase0__KOD.md`
dispatch_commit: `1635a4c6af1952865ee2ff026ea667018e99ebb5`

Entity activation detector workflow run:
`34695954348`

Проверенные workflow logs:
- найден `entities/koder/inbox/KOO__telegram-media-phase0__KOD.md`;
- `activation_detector=PASS`;
- workflow сформировал activation state с `activation_requested: yes`;
- `activation_status: activation_failed`;
- `operator_manual_ping_required: yes`;
- причина соответствует известной границе: текущий workflow не умеет доказанно возобновлять конкретный существующий ChatGPT Entity-chat.

Отдельный activation record был создан внутри workflow run, но не появился в текущем `main`; поэтому этот файл не заявляет несуществующий locator как источник истины.

## Что должен выполнить KOD

Только Phase 0:

- credential-free;
- local/sandbox;
- fake Telegram adapter;
- без сети к Telegram;
- без bot token/webhook secret;
- без production/publication side effects.

Exact inputs:

Architecture:
`entities/webmaster/current/webmaster-library/TELEGRAM-MEDIA-MVP-ARCHITECTURE.md`
commit: `eb099857d473318b5e369d0e67a1c75e7c1d2353`

Phase 0 contract:
`entities/webmaster/current/webmaster-library/TELEGRAM-MVP-PHASE0-CONTRACT.md`
commit: `f548e269c3a4e1174e095f80d393baa675951155`
blob: `6aadfc98d2db63538a33acb30b85196ed8919d50`

## Ожидаемый результат

KOD должен вернуть KOO:
- immutable package locator + commit;
- manifest/checksums;
- exact dependency versions;
- test command;
- full test summary;
- safe receipt fixture;
- known limitations;
- cleanup/run instructions;
- explicit statement that no Telegram/network/credential side effect occurred.

## Stop conditions

Этот manual ping не разрешает:
- real Telegram network call;
- bot token;
- real channel/group id;
- webhook secret;
- MTProto;
- production publication;
- repository settings mutation.

---
created_by: WEB
to_entity: operator
document_type: manual-activation-dependency
status: action_required
purpose: снять подтверждённый exact-chat activation blocker KOD для уже выданного Telegram Media Gateway Phase 0 task
project_time: not_recorded_no_trusted_source