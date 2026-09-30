# KAN → KOO: нормативная проверка Semantic Bootstrap Profile r0.1

Кандидат требует трёх точечных исправлений: отделить semantic test от admission/инициации и не запрещать необходимое проверочное чтение; разделить общие нормативные слоты seed и ссылки на состояние конкретной роли; сделать критерии результата проверки однозначными. Это review текста, а не запуск bootstrap или изменение действующих процедур.

terminal: NEEDS_REWORK_KAN_ENTITY_SEMANTIC_BOOTSTRAP_PROFILE_R01
candidate_status: DESIGN_RESULT_AND_PROFILE_CANDIDATE_NOT_ACTIVE
review_scope: independent normative/document review only
sender: KAN / КАНЦЕЛЯР
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Exact basis / Resume-First

Repository: puev5691/wellbeing-hq.
Fresh preflight HEAD: b1b6784e720813831fac1acaf389dab02eda073e.
Recursive tree: complete, truncated=false.

Task at that commit:
entities/koordinator/outbox/KOO__entity-semantic-bootstrap-profile-r01-normative-review__KAN.md
blob 50000be2a3015f233e540ef0e2a783fbae586614.
Task authority: текущая явная активация ОПЕРАТОРОМ exact independent review + установленная профильная роль KAN. Task-file/inbox сами authority не создают.

Exact reviewed result/candidate:
46f04e4f2d89fae93cedcaee0b21b3529d5c68e9:
entities/shtabist/outbox/SHT__entity-operational-semantics-bootstrap-gap-r01__KOO.md
blob 9849752526f971c0730ae2222e227f5c8149438a.
Candidate находится внутри этого единственного SHT artifact, §§2–14; отдельный профиль не выдумывался.
Task и candidate прочитаны по exact commits; Git blob независимо пересчитан по UTF-8 bytes с Git header: 2/2 PASS. На preflight HEAD candidate не изменён.

Writer:
588493b011cf4ad85a94d40f6513644d9c207b9c:
entities/kancelar/current/KAN__replacement-current-writer-v02.md
blob 13b91b0e189f681be8abf13a76a47b03a5c830fa.
writer_identity: KAN-current-writer-v02
physical_instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857.
Проектная регистрационная метка продолжающегося экземпляра, не platform-attested chat ID.
Fresh current writer bytes и Writer Gate result blob b58219e9655a4caa85cdcaeac15b59331e3436b4 подтверждены; terminal PASS_KAN_PHYSICAL_V02_WRITER_GATE. Нового writer/handoff либо competing review/superseding semantic-bootstrap task/result в проверенном current/handoff и релевантных outbox/inbox/routes не обнаружено. v01 — historical predecessor only.

Fresh-loaded active Sources на preflight HEAD:
- Project Core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33;
- Entity Roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911;
- Source Loading Policy v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf;
- Recovery Canon v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609;
- File Work Canon v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2;
- Task Conveyor Canon v1.2 — df7896d867eeeffff506319538fedad938856686.
Computed blobs и локальные приложенные Sources: 6/6 MATCH.
Source-set-r07 activation result: entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md, blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99.
KOO gap reconciliation прочитан как design evidence, blob 240d840abcc92537c40a62cb76fb73b8ee224574; он не принят за новую approved норму.

## D1 — неоднозначный admission и запрет необходимой загрузки

Места: «Человеческий итог» (only then contour/profile/task semantic loading); §8 (referenced by initiation after recovery/source verification); §9 («Only PASS admits profile semantic loading/work»); §§10–12; §14.

Дефект: §14 сохраняет будущий effectivity gate, но §9 описывает PASS как допускающий loading/work. Разрешение дальнейшего чтения смешано с разрешением профильного исполнения. Для самой initiation/проверки нужны профильный initiation/recovery, exact task и иногда role profile: Source Loading §4 требует их чтения; Recovery v1.6 отдельно проверяет continuity, writer и exact task. Запрет всей профильной загрузки до PASS создаёт циклическую зависимость. Кроме того, текст не устанавливает явно, что semantic FAIL (включая формат human-facing ответа) не меняет уже подтверждённые initiation/writer/recovery facts. Общая оговорка «complements» эту границу не определяет.

Точная минимальная замена admission-предложения §9:

> SEMANTIC_BOOTSTRAP_PASS фиксирует только успешное выполнение exact semantic evaluation в объявленном scope. Он не создаёт task, writer, authority, approval, source activation/effectivity, processing_started или production authority и не допускает работу самостоятельно. Проверка является предварительным условием только тех переходов, для которых отдельное явное approved effectivity decision установит её применимость. До такого решения данный candidate нового gate не вводит.

Добавить к §8/§12 одну общую boundary, сослаться на неё из вступления и §10 вместо повторения полного алгоритма:

> Чтение минимально необходимых active Sources, initiation/recovery, role/profile и exact task/evidence для проверки, диагностики или исправления допускается по уже существующим полномочиям и Source Loading Policy до semantic PASS; чтение не означает исполнение задачи или активацию источника. Bootstrap не заменяет предусмотренные Recovery Canon проверки и не изменяет их outcomes. Semantic FAIL/UNKNOWN/SOURCE_CONFLICT фиксируются отдельно: они не отменяют подтверждённую identity, writer appointment, integrity/readback или factual terminal result. Ограничивается только зависимый переход в установленном применимом scope. Emergency recovery и отдельно допустимые worker/read-only/recovery-diagnostic действия остаются под Recovery Canon, без нового запрета или исключения из bootstrap.

Уточнить §14:

> Введение обязательного semantic prerequisite, scope для новых/существующих instances, retest и effectivity требуют отдельного решения. Если выбранная интеграция меняет смысл обязательной процедуры Recovery Canon, нужна отдельная явная canon amendment/activation; ссылка «complements» её не заменяет.

Это не разрешает такую amendment текущей задачей.

## D2 — seed смешивает нормативную композицию и instance binding

Места: §4 ROLE («role identity/ref», «stable purpose», «role boundary»), SOURCE_SET и «PROVENANCE per slot ... section where available»; §5.3 («Populate active seed only from active approved sources»); §10, где Entity role/profile загружается только после global bootstrap.

Дефект: общие значения правил и конкретная привязка роли/instance не разделены. Одни только global approved Sources не обязаны содержать exact identity/profile каждой Сущности и её current binding. §5.3 либо не позволяет заполнить эти слоты из допустимого профильного/current evidence, либо подталкивает принять такое evidence за active normative truth. §10 дополнительно откладывает требуемый источник до завершения seed. Из перечня полей пока нельзя однозначно определить, что относится к universal invariant, а что — к instance reference.

Точный correction scope: не расширять словарь seed, а классифицировать существующие слоты двумя типами и заменить §5.3 соответствующей формулировкой:

> NORMATIVE_INVARIANT — представление уже действующей применимой нормы. Для каждого обязательного слота указываются exact source locator/version, normative status и точное semantic basis (раздел либо однозначный фрагмент). Слот не получает нормативную силу от seed и не заполняется candidate-нормой.
>
> INSTANCE_BINDING — ссылка на exact проверенную role/profile/instance/current-state dependency с её собственными status, scope и provenance. Такая ссылка не является новой общей нормой; task/profile/current evidence не становится global Project Source. Binding читается при необходимости по Source Loading Policy, включая проверочную загрузку до PASS. Отсутствующее binding остаётся UNKNOWN; произвольное значение из общей роли или памяти не подставляется.

Указать прямо, что ROLE identity/ref и конкретные current-state refs — INSTANCE_BINDING, а различения Entity/instance, role/task, authority/capability — NORMATIVE_INVARIANT. Для отсутствующей необязательной/applicability-зависимой привязки фиксировать reason, не выдумывать всеобщую обязательность.

Для заявленной deterministic composition добавить компактную slot→source-section mapping существующих нормативных слотов; не копировать canons. Заменить «where available» для обязательного нормативного слота на требование проверяемого semantic basis; если basis установить нельзя, слот UNKNOWN и соответствующий evaluation не PASS. Это документальная таблица существующих зависимостей, не loader implementation.

Сохранить уже имеющиеся правила: construction order не override precedence; active conflict не решается timestamp/order; fresh verified current evidence применяется только в доказанном exact scope и не разрешает synthetic recovery/state reconstruction.

## D3 — неоднозначность outcome и недостаточно ограниченный claim self-test

Места: §6 («human-facing machine dump ... failure»); §9 («persistent metadata-first», UNKNOWN только при недоступности source); §12 («UNKNOWN or FAIL depending on exact mismatch»); §8 S9 и §4 HUMAN_INTERFACE.

Дефект: однократный metadata-first объявлен failure в §6, но в §9 добавлено неопределённое persistent; mismatch может стать UNKNOWN либо FAIL без критерия. Не определён исход, когда source доступен, но evaluation не выполнен или ответ не позволяет установить соблюдение инварианта. Это не позволяет воспроизводимо присвоить заявленный deterministic PASS. Кроме того, правильный порядок текста не доказывает понимание вообще и не заменяет обязательное evidence.

Точная минимальная outcome-оговорка:

> Для каждого применимого S1–S12 evaluation сохраняет exact scenario/input, проверяемый ответ/результат, source-basis и scenario outcome в одном evaluation artifact или его ссылках; отдельный файл на сценарий не требуется. PASS возможен только при проверенных успешных результатах всех применимых обязательных сценариев на exact seed/source versions. Пропущенная проверка, недоступный обязательный input или недостаточность evaluation evidence дают UNKNOWN, а не PASS. Доказанный неверный переход или ответ, нарушающий обязательный инвариант, дают FAIL. Доказанное противоречие применимых active approved Sources даёт SOURCE_CONFLICT и не разрешается агрегатором. При сочетании проблем сохраняются все scenario outcomes; общий результат выбирается SOURCE_CONFLICT, иначе FAIL, иначе UNKNOWN, иначе PASS. Это порядок отчётных outcomes, не precedence нормативных источников.

Удалить неопределённое «persistent» из критерия S9/§9 либо заменить ссылкой на явный exact test criterion; минимальный вариант — один проверяемый S9 ответ. Для source/seed mismatch разграничить: недостаточно evidence для сравнения → UNKNOWN; установленная неверная композиция относительно проверенного источника → FAIL; конфликт самих active норм → SOURCE_CONFLICT.

Дополнить S9:

> Связный русский смысл идёт первым; необходимое exact evidence сохраняется и остаётся проверяемым. Хорошее изложение без обязательного evidence не даёт PASS. Ошибка human-interface требует исправления/повторной проверки только затронутого scenario/evaluation; она сама по себе не аннулирует factual result, recovery или writer. PASS подтверждает только продемонстрированное применение перечисленных инвариантов в exact evaluation, а не универсальную безошибочность экземпляра.

Не добавлять runtime tester, numeric retry policy или новый журнал.

## Correction boundary / RETURN KOO

Проверены вопросы N1–N10 exact задачи; substantive вывод ограничен D1–D3. Новый полный канон не требуется для этих исправлений: исправляется composition/validation contract, а не исходные нормы. Отсутствие отдельного обязательного self-test в active Sources само по себе не означает, что действующие initiation результаты недействительны.

Вернуть КОО для fresh reconciliation и выбора уже авторизованного correction-only successor либо точного missing-authority gate. Текущая проверка не назначает SHT correction и не активирует ARH review. Переход к ARH нельзя объявлять открытым по PASS KAN: PASS здесь не выдан.

Не менять остальные различения S1–S12 и разделение bootstrap / loader / dialogue engine / governance / recovery. Исправление только D1–D3, с exact successor/diff и сохранением CANDIDATE_NOT_ACTIVE.

Project Sources/canons, writer/recovery, loader/engine/runtime: NOT_CHANGED.
Entities created: NO.
PKTB D1-D2 lineage: UNTOUCHED.
Source activation/effectivity/approval: NOT_GRANTED.
Historical PROMPT replay: NONE.
Memory-layering attempt 3: NOT_AUTHORIZED.
Publication/dispatch/inbox не являются receipt/acceptance/processing_started адресата.

Journal-source для RED, без отдельного editorial запуска: проверка проекта Semantic Bootstrap обнаружила, что проверку понимания нужно точнее отделить от разрешения на работу и от подтверждения восстановления. Требуемая доработка касается допуска, происхождения полей seed и проверяемости результатов теста; действующие каноны и назначения Сущностей сохранены.

STOP after immutable result, exact readback and RETURN KOO.
