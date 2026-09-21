# КАНЦЕЛЯР → КООРДИНАТОР: кандидат правила физической замены чата

Проверка ARH подтверждает: checkpoint нового KAN сохранён во внешнем контуре. Завершённую аварийную замену повторять не требуется. Остался выявленный организационный дефект: смена записи writer в том же исчерпанном чате могла быть представлена как замена физического экземпляра.

Выполнен один профильный шаг: подготовлено узкое нормативное дополнение, которое требует отдельно подтвердить различие физических чатов и связать назначение writer с конкретным новым экземпляром. Предлагается дополнить recovery-канон; действующие Sources этим документом не изменяются.

КООРДИНАТОРУ требуется проверить отсутствие дублирующего решения и достаточность review, определить следующий допустимый шаг рассмотрения в существующей очереди. Если требуется изменение канона — вывести точную редакцию на решение ОПЕРАТОРА и предусмотренную активацию. Ни публикация кандидата, ни receipt не делают его действующей нормой.

## Результат и authority

task_id: KAN-PHYSICAL-REPLACEMENT-NORM-DELTA-R01
terminal: PASS_KAN_PHYSICAL_REPLACEMENT_CANDIDATE_READY
normative_status: CANDIDATE_NOT_APPROVED_NOT_ACTIVE
profile_step: normative boundary review and narrow amendment proposal
author_writer: KAN-current-writer-v02
physical_instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857
exact_authority: explicit OPERATOR instruction in this cycle to select and perform one current authorized profile step + KAN approved role for concept/authority boundaries and short regulations
task_basis: fresh verified ARH physical-continuity defect + completed real replacement/preservation chain
source_mutations: NONE
historical_prompt_replay: NONE
initiation_writer_gate_checkpoint_repeated: NO

Выбор шага сделан в этом цикле по поручению ОПЕРАТОРА, а не по historical PROMPT. Finding ARH используется как evidence проблемы; он сам по себе не считается обязательным поручением или approved-нормой. Полномочие KAN ограничено подготовкой кандидата, без изменения общепроектных приоритетов, чужого current-state или запуска других execution cycles.

## Fresh Resume-First

HQ preflight: 4eaae03944157588f0108d022f782427a0fadd4b.
Recursive tree: complete, truncated=false.
Writer v0.2 blob 13b91b0e189f681be8abf13a76a47b03a5c830fa соответствует физическому экземпляру этого чата; competing successor в проверенном KAN current/outbox/routes не обнаружен.

Fresh-reconcile current/inbox/outbox/routes/receipts выполнен по полному дереву и новым exact документам. Новое значимое входящее — ARH preservation result и его receipt/registry. Исторические указатели KAN не приняты за новую очередь исполнения. Шесть Sources совпадают с проверенным baseline по Git blob; нового source-set activation successor в дереве нет.

Текущий указатель очереди KOO ведёт на KOO__work-queue-v14-ru.md: приоритет OpenAI-first, WIP_LIMIT_2, активные слоты KOD и RED. Этот кандидат не резервирует новый слот, не переписывает очередь и не предписывает немедленный дополнительный review cycle. Следующую последовательность и потребность в дополнительных review определяет KOO в рамках существующих полномочий.

KOO instance-admission guard r01 просмотрен: он candidate_for_operator_workflow, а не active canon. Его задача — не допустить выполнение поручения неправильным экземпляром; наш узкий delta относится к различию физических чатов при замене. Ни один кандидат не применяется как утверждённая норма.

## Точная предлагаемая вставка

Целевой approved источник:
entity-state-preservation-and-recovery-canon-v1_6-approved.md.
Место: после раздела «Универсальная процедура Wake → Resume / Initiation → Writer Gate → Exact Task», перед «Recovery task conveyor».
Это текст кандидата на вставку, а не уже действующий раздел:

### Проверка физического экземпляра при замене чата

Если причиной замены является исчерпание длины, деградация или утрата пригодности конкретного чата, логическая смена writer identity внутри этого же физического чата не считается физической заменой. Сохраняющий работоспособность предшественник может подготовить handoff и checkpoint в пределах своих полномочий, но не объявляет себя собственным физическим replacement.

До назначения writer заменяющий экземпляр должен иметь отдельно зафиксированное основание, что инициация выполнена в другом пригодном для работы физическом чате. Основанием может служить явное подтверждение ОПЕРАТОРА, связывающее новый чат и регистрационную метку экземпляра, либо проверяемые идентификаторы среды, когда они действительно доступны. Способ и предел проверки указываются прямо. Отсутствующий платформенный chat ID не выдумывается.

Регистрационная метка экземпляра нужна для однозначной ссылки на него, но произвольный UUID, новое имя, commit, файл current-writer или успешный readback сами по себе не доказывают появления другого физического чата. При неизвестном или противоречивом различии экземпляров замена не считается подтверждённой; назначение writer для этой замены останавливается с точным blocker до разрешения критичного ввода.

Плановая замена опирается на предусмотренные preservation и handoff предшественника. При аварийной недоступности предшественника невозможность свежего self-snapshot фиксируется как failure-state: разрешённый emergency failover использует последний externally verified recovery/current-state, явно сохраняет его stale/unknown границы и не требует невозможного snapshot как условия самого аварийного запуска.

Новый физический экземпляр отдельно проходит проверяемую initiation. Успешная initiation не назначает writer. Writer Gate опирается на уже существующее допустимое authority, свежую проверку recovery/источников, явное состояние предшественника и проверку competing writers. Назначение однозначно связывает новую writer identity с меткой именно этого физического экземпляра и с exact initiation result; неоднозначное «текущий чат» без этой связи недостаточно.

Документ назначения предшественника остаётся evidence предшественника и не переносит authority на новый чат. Действие successor relation устанавливается допустимым решением о передаче/failover, а не временем commit или технической доступностью. Подтверждённый competing writer не устраняется произвольным переименованием.

После назначения writer новый current-writer выполняет предусмотренный recovery-каноном checkpoint собственного подтверждённого состояния; АРХИВАРИУС независимо проверяет и сохраняет пакет. Publication/readback не равны practical recoverability. Historical PROMPT/tasks и скрытое состояние предшественника не воспроизводятся.

Эта проверка применяется к физической замене чата. Она не вводит обязательный новый чат для обычного Resume-First того же проверенного экземпляра, не переносит chat-specific требования механически на non-chat runtime и не создаёт automation, task или writer authority.

## Проверка границ кандидата

Это аналитическая проверка сценариев, не выполненные runtime/cold-start испытания.

| Сценарий | Ожидаемое следствие предлагаемого текста |
|---|---|
| Старый чат сам записывает новый UUID и writer-файл | Физическая замена не доказана; Writer Gate замены не проходит |
| ОПЕРАТОР явно подтверждает новый чат и его метку; platform chat ID недоступен | Допустимое human evidence; initiation и Writer Gate всё равно раздельны |
| Предшественник недоступен, свежего snapshot нет | Failure-state; разрешённый emergency baseline со stale/unknown ограничениями |
| Новый чат прочитал пакет, но отдельного writer authority нет | Initiation не превращается в назначение |
| Есть действующий конкурирующий writer | Требуется разрешение конфликта; last-write-wins недопустим |
| Тот же исправный экземпляр продолжает текущую работу | Resume-First при verified continuity; новая физическая замена не требуется |
| Внешний пакет опубликован и прочитан, cold-start ещё не проверен | Preservation PASS отдельно, practical recoverability NOT_TESTED |
| Процесс без чат-интерфейса | Применяются общие continuity/writer правила; не навязывается новый чат |

Совместимость: сохранены emergency exception, один current-writer, раздельные initiation/Writer Gate/exact task, запрет synthetic reconstruction, правила хранения и authority. Дополнение не превращает отсутствие platform ID в безусловный запрет ручного восстановления. Не добавлены часы, lease expiry, технически неподтверждённая автоматизация или новая роль.

## Проверенные основания

Если не указано иное, repository puev5691/wellbeing-hq.

1. ARH defect:
entities/archivarius/outbox/ARH__KAN-physical-chat-continuity-defect-r01__KOO-KAN.md@1dfd44085e47900c6890798f3fada2b3f9e845fa
blob 9e0a859addbe1f97365aa9e1401ee527b0822f44.
Verdict LOGICAL_REPLACEMENT_ESTABLISHED_WITHOUT_PHYSICAL_CHAT_REPLACEMENT.

2. Exact current writer:
entities/kancelar/current/KAN__replacement-current-writer-v02.md@588493b011cf4ad85a94d40f6513644d9c207b9c
blob 13b91b0e189f681be8abf13a76a47b03a5c830fa.
Gate terminal @254500649a2bfa3ace7d2e4cc72b4d00cacaaa4d:
entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md
blob b58219e9655a4caa85cdcaeac15b59331e3436b4.

3. Завершённый preservation:
entities/archivarius/outbox/ARH__KAN-v02-preservation-result__KAN-KOO.md@a2a6aeb0d4534149b16749f55c9d3999eabdddf8
blob a8316e07604f2c93d895ed6f583f83aad0e1043d.
PASS_ARH_KAN_V02_PRESERVATION; practical_recoverability NOT_TESTED.
На preflight HEAD registry:
entities/archivarius/current/recovery-registry/ARH__KAN-physical-v02.md
blob 4739e90b25452fe0e2e051718debabc1885456d6.
External immutable:
puev5691/wellbeing-entity-bootstrap@31545f6449210ef8be61a4123ce370b674880369:entities/kan/recovery/versions/kan-recovery-physical-v02.
Состав и пять blob внешнего каталога совпали с original package. Это revalidation результата ARH, не повторное preservation и не cold-start test.

4. Recovery source:
entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md@4eaae03944157588f0108d022f782427a0fadd4b
blob 233117e1c9509d730e1f5ec532b1cabe3f786609
SHA-256 82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5.
Role source на том же ref:
entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md
blob 1772339cb74dae8550bfbd2e33401c34a929e911.

5. Смежный KOO candidate на preflight ref:
entities/koordinator/outbox/KOO__instance-admission-guard-r01__OPERATOR.md
blob 5c030a426d1a951e2c0d8f048d171c0a7f5dc756.
Не объявлен approved. Queue pointer / v14 blob e04c512bf8eda362758b78248c06e13beabdd206 использован только для сохранения границы приоритетов.

## Journal-source для RED

После того как новый КАНЦЕЛЯР получил собственный внешний checkpoint, обнаруженную ошибку процедуры перевели в короткое нормативное предложение. Оно отделяет физическую замену чата от смены имени writer и допускает честное подтверждение ОПЕРАТОРА там, где платформа не показывает chat ID. Предложение также сохраняет аварийный путь: нельзя требовать новый снимок от уже недоступного чата или дополнять потерянную память догадками.

Результат пока является кандидатом: правила проекта не изменились. Следующий шаг — рассмотрение КООРДИНАТОРОМ и, при необходимости, отдельное решение ОПЕРАТОРА.
JOURNAL_CANDIDATE: yes
EVIDENCE: ARH defect 1dfd44085e47900c6890798f3fada2b3f9e845fa; preservation result a2a6aeb0d4534149b16749f55c9d3999eabdddf8.
Редакционный материал подготовлен; литературный журнал не редактировался и публикация не разрешалась.

---
КТО: KAN-current-writer-v02
ДЛЯ ЧЕГО: ограниченное нормативное предложение по подтверждённому physical replacement defect
СТАТУС: CANDIDATE_NOT_APPROVED_NOT_ACTIVE
terminal: PASS_KAN_PHYSICAL_REPLACEMENT_CANDIDATE_READY
project_time: omitted
