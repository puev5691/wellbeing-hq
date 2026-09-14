# ОПЕРАТОРУ — запуск нового SIS / СИСАДМИНА

status: PREPARED_WAITING_KOO_INDEPENDENT_VERIFICATION
production_mutation: no
current_writer_transfer: not_performed
project_time: omitted; trusted project-time source not used

## Смысл

Новый чат SIS нельзя запускать как authoritative current-writer только по старому recovery или по памяти старого чата.

Подготовлена двухслойная recovery-схема:

1. Принятый SIS self-recovery:
`puev5691/wellbeing-entity-bootstrap@861645789d206db19e5135a6771564660d99158f:entities/sis/recovery/current`

2. Свежий ARH replacement overlay:
`puev5691/wellbeing-entity-bootstrap@1f4f3467deb4b2364ff5c9f3b25c6585e1d4e97c:entities/sis/preservation/pending/replacement-initiation-v01`

Launcher:
`SIS__emergency-initiation-master.md`

До KOO independent PASS новый чат допускается только как read-only recovery reader, но не как current-writer.

## Перед открытием нового чата

1. Получить KOO PASS/FAIL по:
`entities/koordinator/inbox/ARH__SIS-replacement-initiation-v01__KOO.md`.

2. При FAIL нового authoritative SIS не запускать; вернуть blocker ARH.

3. При PASS открыть новый чат SIS и передать ему стартовый промпт ниже.

## Стартовый промпт новому SIS

Проведи replacement initiation SIS / СИСАДМИНА по recovery-канону.

Основной launcher:
`puev5691/wellbeing-entity-bootstrap@1f4f3467deb4b2364ff5c9f3b25c6585e1d4e97c:entities/sis/preservation/pending/replacement-initiation-v01/SIS__emergency-initiation-master.md`

Accepted base recovery:
`puev5691/wellbeing-entity-bootstrap@861645789d206db19e5135a6771564660d99158f:entities/sis/recovery/current`

Выполни launcher полностью и строго по порядку.

Сначала:
- загрузи только active approved Project Sources;
- независимо проверь base recovery и KOO acceptance;
- независимо проверь replacement overlay composition/checksums по exact immutable commit;
- сделай fresh GitHub-preflight `puev5691/wellbeing-hq`;
- проверь SIS inbox/outbox/current, dispatch/receipts, sender registry, ARH recovery registry и current-writer/activation evidence.

Не продолжай старую задачу автоматически.

Особенно не запускай автоматически исторический Telegram Phase1B sudo step. Recovery фиксирует его только как внешний dependency в состоянии `WAITING_OPERATOR_EXACT_HUMAN_ACTION_RECEIVED`; выполнение этого шага в recovery не доказано.

До подтверждённого writer handoff работай только read-only.

Если KOO PASS + решение ОПЕРАТОРА о replacement + отсутствие competing writer подтверждены, создай отдельный SIS-owned current-writer initiation artifact, сделай immutable readback и только затем переходи к Resume-First.

В первом отчёте верни:
- `initiation_status`;
- base recovery locator + verification state;
- overlay locator + raw-byte checksum result;
- KOO verification artifact/commit/verdict;
- fresh HQ HEAD;
- Telegram Phase1B current state;
- Entity Runner current state;
- VPN/Hiddify current state;
- competing-writer state;
- current-writer state;
- unresolved OPERATOR/authority dependencies;
- forbidden boundaries.

Допустимый initiation status:
`initiation_verified | initiation_loaded_external_unverified | initiation_failed`.

Запрещено во время initiation:
- production/server/network mutation;
- live Telegram send/public webhook;
- повтор старого sudo шага без fresh exact authorization;
- provider-side API execution;
- создание/публикация credentials;
- изменение nginx/Xray/TERA2/UFW/DNS;
- destructive cleanup;
- восстановление секретов из snapshot;
- объявление receipt/acceptance/writer authority по одному наличию файла.

## После успешной инициации

1. Старый SIS-чат больше не использовать для authoritative profile work.
2. Новый SIS выполняет fresh Resume-First и выбирает только всё ещё актуальный exact addressed task.
3. `SIS GitHub Work` включать только после подтверждённого current-writer handoff и проверки отсутствия recovery/writer conflict. Не создавать дубль.
4. Если exact профильной задачи нет — остановиться в `WAITING_KOO_OR_OPERATOR_EXACT_PROFILE_DIRECTION`.

## Что считать успешной инициацией

Недостаточно сообщения «готов».

Нужны:
- KOO independent PASS;
- base recovery verification;
- overlay raw-byte checksum PASS;
- fresh HQ reconciliation;
- отсутствие competing replacement writer;
- отдельный SIS-owned initiation/current-writer artifact;
- immutable readback этого artifact;
- отсутствие запрещённой mutation в ходе startup.

Только после этого practical replacement SIS считается завершённым.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: операторская инструкция холодного старта нового СИСАДМИНА
СТАТУС: prepared_waiting_koo_independent_verification