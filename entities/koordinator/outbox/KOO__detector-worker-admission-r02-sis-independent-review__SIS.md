# КОО → СИСАДМИН: независимая изолированная проверка detector-worker admission r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
scope: INDEPENDENT_DOCUMENT_AND_OFFLINE_SYNTHETIC_VERIFICATION_ONLY
fresh_HQ_HEAD_before_write: 9f81fe75a90b1f11e10abb5062062b9472b8be37
project_time: omitted

## Основание и приём

ОПЕРАТОР прямо поручил КООРДИНАТОРУ после результата КОДЕРА определить отдельный gate независимой проверки кандидата, включая происхождение event envelope и границу доверия supervisor profile. KOO выбирает одну bounded проверку СИСАДМИНОМ в пределах SIS runtime/admission профиля. Это не разрешение внедрения.

КООРДИНАТОР непосредственно прочитал exact KOD result, matrix, candidate, diff и evidence, а также адресный inbox и dispatch. Receipt exact KOD объектов VERIFIED_BY_DIRECT_READ; publication/inbox/dispatch сами по себе receipt, activation или processing_started не доказывали.

Exact result:
puev5691/wellbeing-hq@19d387a8c9044647c6c119f1cf2bf2e2858f9f30:entities/koder/outbox/KOD__detector-worker-admission-r02-result__KOO.md
blob 6bb3e38623e591f4102f1b3ea8d73066ba531593
terminal PASS_KOD_DETECTOR_WORKER_EVENT_AUTHORITY_ADMISSION_R02_ISOLATED_READY_FOR_INDEPENDENT_VERIFY.

В том же commit:
- isolated successor `entities/koder/outbox/KOD__activation-worker-v03-isolated__KOO.py`, blob `fb08da8617871b670e26de9dee1e0f5ec81bd04a`;
- tests `entities/koder/outbox/KOD__detector-worker-admission-r02-tests__KOO.py`, blob `1d508ff4e1cd712878512de0be97221a42bea084`;
- matrix `entities/koder/outbox/KOD__detector-worker-admission-r02-matrix__KOO.md`, blob `f051c4ca5c5343e3a594a644c4330216ea14dd1a`;
- evidence `entities/koder/outbox/KOD__detector-worker-admission-r02-evidence__KOO.json`, blob `00ed17ef8e1272fb856540193e320df9dfa12d7a`;
- exact diff `entities/koder/outbox/KOD__detector-worker-admission-r02-exact-diff__KOO.patch`, blob `b60b99fe9cc49cb68c2786f70797b8ed2ac9b21a`.
Historical unchanged worker v0.2 blob `c680878806fd2fb6d20df8b6e8938d3f3ead5053`.

KOO проверил exact blob identities и JSON evidence: ровно 25 case objects с `executed=true`, `verdict=PASS`; это readback собственных тестов КОДЕРА, не независимый engine/runtime PASS. Адресные KOO inbox blob `1f4f46d6f5a89d884f57178082406e435fec496c`, dispatch blob `f40df9342256bb28c3dd0a6429f8e7866851f6ca`. После publication результата до prewrite HEAD только dispatch и workflow activation boundary, competing successor/terminal scope не найден.

KOO current writer v0.8 blob `ca7ed0ed4e539dcdbe783e122cea409a77ab10cd`. Перед собственной профильной работой SIS обязан независимо проверить свой exact current-writer и task authority; current catalog содержит исторические r0.2/r0.5 и r0.6 establishment candidate, не выбирать по имени/времени.
Шесть approved Project Sources проверены по Git blobs: recovery `233117e1c9509d730e1f5ec532b1cabe3f786609`, roles `1772339cb74dae8550bfbd2e33401c34a929e911`, loading `69eb657f260a019f76e8e707c880ea88c1dfa0bf`, file-work `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`, conveyor `df7896d867eeeffff506319538fedad938856686`, core `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`.

## Точное поручение СИСАДМИНУ

1. Fresh GitHub preflight; загрузи действующие approved Sources; независимо установи свою writer/task admission boundary, supersession и competing result. Если writer не подтверждён, верни диагностический BLOCKED без профильного результата.
2. Независимо проверь точную реконструкцию v0.2 baseline → patch → isolated successor, отсутствие collateral changes, immutable identities и возможность воспроизвести заявленные 25 локальных исходов без доступа к реальным хостам/сервисам. Если безопасная локальная воспроизводимость недоступна, укажи DOCUMENT_ONLY и UNKNOWN без утверждения выполненных независимых тестов.
3. Проверь fail-closed semantics до handler: event/inbox/artifact/dispatch binding, authority/source/recovery/current-writer, duplicate ID/digest, unknown reservation, handler nonzero exit и отсутствие ложного real processing_started.
4. Отдельно исследуй границу происхождения: реальный GitHub workflow сейчас пишет activation_failed и не вызывает worker; кто создаёт event envelope, как external supervisor удостоверяет его источник и неизменность, и возможно ли сформировать валидный envelope без доверенного detector. Digest, вычисленный из доступных полей, сам по себе не является свидетельством происхождения.
5. Отдельно исследуй supervisor trust profile: кто утверждает применимый approved source set и task authority, как подтверждаются актуальность/несуперседированность и writer state, кто хранит/выдаёт profile, не может ли инициатор/handler самостоятельно его подменить. Synthetic fixtures под `fixtures/` не равны реальным approved Sources или действующей authority. Оцени поведение при profile mismatch, partial write, corruption, outage и uncertain crash semantics; локальный fsync не доказывает F2 durability.
6. Верни независимое ограниченное заключение с матрицей: фактически проверено / только design / UNKNOWN / BLOCKED; точный defect, если найден, и один минимальный следующий gate. Не объявляй KOD 25/25 собственных проверок независимым 25/25 автоматически.

Результат: один SIS outbox document с PASS_WITH_BOUNDARIES / FAIL / BLOCKED, immutable readback и адресным dispatch KOO; укажи exact candidate/commit/blob и что было фактически исполнено. После terminal result остановись.

## Запреты

Никакого production deployment, реального GitHub workflow-to-worker transport, real Entity activation, host/shard access или WRITE, provider call, secrets, Project Sources/canon/current-writer mutation, automation change, memory-layering attempt 3 либо исторического PROMPT replay. Прежние Exchange Gate defects не объявлять устранёнными. KOD result не даёт production admission или substantive acceptance. Локальный worker marker не является processing_started реальной Сущности. F2 domain HOLD сохраняется.

Передача другой Entity-чату остаётся ручной до отдельного доказательства automatic activation точного scope. Publication этого файла не является receipt/activation/processing_started.

---
КТО: КООРДИНАТОР / KOO v0.8
АДРЕСАТ: СИСАДМИН / SIS
СТАТУС: AWAITING_MANUAL_CHAT_ACTIVATION
