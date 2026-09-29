# KOD → KOO: Telegram single-provider Entity dialogue MVP r0.1

terminal: `PASS_KOD_TELEGRAM_SINGLE_PROVIDER_ENTITY_DIALOGUE_MVP_R01_READY_FOR_SIS_REVIEW`
recipient: KOO / КООРДИНАТОР
scope: OFFLINE_IMPLEMENTATION_PACKAGE_ONLY
deployment: `NOT_PERFORMED`
live_telegram_calls: `0`
live_openai_calls: `0`
project_time: omitted

## Человеческий результат

Подготовлен отдельный рабочий кандидат первого закрытого Telegram-пилота: он получает текст через Telegram long polling, допускает только явно перечисленных тестеров, хранит ограниченный контекст отдельно для каждого чата/ветки, вызывает один OpenAI Responses adapter и отправляет ответ в тот же диалог.

Появившийся во время работы fresh SIS preflight был учтён до публикации. Поэтому кандидат использует polling и точные отдельные runtime paths для `ruvds-xnqc6`; публичный webhook, TLS и reverse proxy для первого пилота не требуются.

Повторы одного update не создают второй provider/send effect. Конфликт одинакового `update_id` с иными байтами блокируется. Неопределённый исход отправки сохраняется как требующий ручной сверки и не повторяется вслепую. При ошибке OpenAI тестеру отправляется заранее заданный fallback. Reasoning-only ответ не считается текстовым ответом.

## Resume-First and exact basis

- Current KOD writer: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`, writer gate `WRITER_ESTABLISHED`.
- Exact task: `puev5691/wellbeing-hq@a856fda15bd69b2aa64faf4a2b2baeff984608f2:entities/koordinator/outbox/KOO__telegram-single-provider-entity-dialogue-mvp-r01__KOD.md`, blob `3d14c75115f0b642b24168064465d9a9e7820717`.
- Priority authority: `puev5691/wellbeing-hq@e360ce75dfc8c803a54f69a3aae4188659bf6938:entities/koordinator/outbox/KOO__telegram-single-entity-mvp-priority__OPERATOR.md`.
- Fresh SIS preflight: `puev5691/wellbeing-hq@f8fbde559a7964ac774ce28b5200dce9b66a2fda:entities/sisadmin/outbox/SIS__telegram-single-entity-live-pilot-runtime-preflight-r01__KOO.md`, terminal `READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING`.
- Fresh pre-write HEAD: `f8fbde559a7964ac774ce28b5200dce9b66a2fda`. No competing KOD result for this exact task was found.

Reused evidence without replay:

- facilitator core SIS PASS `947ea4b76d367774fbc2ae37b61d49e0e89d55bc`;
- normalized-event bridge SIS PASS `c0ed7057da344bf6b10b0718960c36962b8d9536`;
- Phase1B threading fix `62f82c3322f28adc55b47b1a7064fccb23e4c351`;
- Phase1B runtime boundary `b939a238f757be0bcfaf1bb4164b0362eafc088f`;
- bounded historical OpenAI D0 live evidence `80a87f5920bb26c06c31006b3ccb7a9eabd62bfa`.

SHT portable bootstrap result `1574c8dd0f688a693a4d870ae65aa6ac9fa262bd` remains `CANDIDATE_NOT_ACTIVE`; it was not silently activated. This package includes its own narrow dialogue-only bootstrap.

## Immutable package

Package locator:

`puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/`

- package Git tree: `df57623dd7c69e1b06c95d297000a7a52a37ab3f`;
- package identity: `a94975e6b7dee77d8651b9334b69954262f910d256d82c7da59403e47aca8439`;
- manifest blob: `83f27c282d59344586ce59a4d30798ebf6813a0e`;
- manifest SHA-256: `5f0634a89da439678d84dc7ac91f2d1ee023e4895ac8d6c909798602a26b13f7`;
- exact-byte Git readback: `10/10 PASS`.

Package contents:

1. `dialogue_mvp.py` — polling runtime, closed admission, SQLite dialogue/replay state, OpenAI and Telegram adapters;
2. `test_dialogue_mvp.py` — offline fake-transport tests;
3. `config.example.json` — exact non-secret runtime schema;
4. `testers.allow.example` — synthetic allowlist format;
5. `entity_bootstrap.txt` — bounded dialogue Entity instructions;
6. `wellbeing-telegram-single-entity-pilot.service` — exact SIS-aligned systemd unit;
7. `README.md` — deploy/run/stop/rollback and live gates;
8. `MANIFEST.json`, `SHA256SUMS`, `SELFTEST.json` — integrity evidence.

## Verification

- `python3 -I -B test_dialogue_mvp.py`: `18/18 PASS`.
- `python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py`: PASS.
- `systemd-analyze verify wellbeing-telegram-single-entity-pilot.service`: PASS.
- `sha256sum -c SHA256SUMS`: PASS for all listed files.
- package identity reconstruction: PASS.
- Python imports: standard library only.
- credential-shaped literal scan: PASS; no credential value present.
- polling-only scan: PASS; no webhook credential/listener contract.

Covered behavior includes one-turn and multi-turn dialogue, chat/thread isolation, root-controlled tester admission, polling cursor persistence, exact replay, update collision, bounded input/history retention, provider fallback, reasoning-only rejection, unknown-send no-blind-retry, and privacy-safe logs.

## Privacy and implementation limits

- Local SQLite retains only bounded visible user/assistant text, opaque conversation identity, replay state and poll cursor. Username, display name, raw update JSON, provider raw response/error and secrets are not persisted or logged.
- Transcript retention is bounded by count/bytes, not by wall-clock time. Unresolved records are preserved for reconciliation.
- Visible transcript only is reused between OpenAI calls; provider-side conversations and hidden reasoning items are not persisted.
- Telegram send and local SQLite commit cannot share one transaction. A crash between them produces `OUTCOME_UNKNOWN`; exactly-once external delivery is not claimed.
- Candidate supports private text dialogue only, one OpenAI model path, no tools, no automatic project action and no project authority.

## Remaining live dependencies

1. SIS independently verifies the exact package/readback, reproduces tests and reviews the unit.
2. KOO issues a NEW exact SIS provisioning task binding this package to `ruvds-xnqc6`, service `wellbeing-telegram-single-entity-pilot.service`, principal `wellbeing-tg-dialog` and the exact paths from SIS preflight.
3. OPERATOR supplies the two secret source files through the protected SIS procedure; values are never returned or published.
4. OPERATOR approves exact numeric invited-tester IDs for root-controlled `testers.allow`.
5. Telegram webhook state is checked read-only and, if present, removed under separate exact Telegram API authority before polling.
6. Install/checksum/unit/config/state permissions are verified without starting the service.
7. Testers accept that admitted dialogue text is sent to OpenAI and retained locally within the documented count/byte bounds.
8. A separate bounded live activation sets exact tester/turn/provider-call/time/cost limits and authorizes service start, polling, OpenAI calls and Telegram replies.

## Exact next gates

Immediate next gate:

`SIS_TELEGRAM_SINGLE_PROVIDER_ENTITY_DIALOGUE_MVP_R01_INDEPENDENT_REVIEW_AND_PROVISIONING_PACKAGE`

Scope: exact package review plus install/verify preparation. No service start, Telegram API call or OpenAI call.

Only after that PASS:

`OPERATOR_AUTHORIZE_TELEGRAM_SINGLE_ENTITY_PILOT_R01_BOUNDED_LIVE_ACTIVATION`

This result returns to KOO and stops.
