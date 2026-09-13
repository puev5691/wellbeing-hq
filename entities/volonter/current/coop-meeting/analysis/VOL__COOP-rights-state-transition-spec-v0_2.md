# Политэкономия совладения: спецификация прав и переходов состояния v0.2

## Смысл и требуемое действие

Версия v0.2 исправляет критические и существенные пробелы, выявленные независимой проверкой ШТАБИСТА. Модель дополнена защищённым конституционным корнем, процедурой мета-поправок, жизненными циклами оснований, компетенций и независимого рассмотрения, защитой всей причинной цепочки от обхода, тупиковыми состояниями и повторной проверкой непосредственно перед исполнением.

Документ остаётся исследовательским кандидатом. Он не является утверждённой нормой, токеномикой WBN/WBNP, программной схемой или разрешением на production-разработку.

Требуемое действие: повторный независимый stress-review ШТАБИСТА. До его результата документ нельзя передавать в реализацию как замкнутую исполнимую модель.

## Проверяемая база

- v0.1: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_1.md`, commit `9ef56621b8b600bb5f5c159b9eaee619bd820c36`, blob `e3e8ec3f22febb65eb24fd941c8fa6a02aafe77c`;
- review ШТАБИСТА: `entities/shtabist/outbox/SHT__COOP-rights-transition-review__VOL.md`, commit `95e8a42706eeed9e5deca16f7bb109adb8d427a4`, blob `e7c94bda4eda1b03729830aed5464d1c41afbd61`;
- результат review: `REVIEW_COMPLETE_WITH_CRITICAL_GAPS`;
- принятые замечания: C1–C5, S1–S10, E1–E5.

## 1. Состав модели

### SUBJECT — субъект

Носитель права или компетенции: человек, участник, продолжающийся коллектив, локальный Союз, федерация, общественный или природный контур. Технический аккаунт, ключ и программа являются средствами действия, но не заменяют субъекта и не создают право или компетенцию.

Минимальные поля: `subject_id`, `subject_type`, `status`, `representation`, `conflict_disclosures`, `provenance`.

### OBJECT — объект

То, к чему относится право: результат труда, требование, резерв, инфраструктура, ресурс, поток, решение, правило или компетенция.

Минимальные поля: `object_id`, `object_type`, `classification`, `current_state`, `protection_class`, `causal_lineage`, `provenance`.

### RIGHT — право

Связь субъекта с объектом. Право хранится отдельно от баланса и от компетенции изменять право.

Минимальные поля:

- `right_id`, `subject_id`, `object_id`;
- `right_type`: personal, membership, public_common, natural;
- `powers`: use, income, manage, inform, vote, amend, alienate, exit, challenge;
- `scope`, `start_condition`, `end_condition`;
- `transferability`: transferable, conditionally_transferable, nontransferable;
- `basis_id`, `ruleset_id`, `state`, `protection_class`, `provenance`.

Наличие power `manage` внутри `RIGHT` не создаёт `COMPETENCE` менять это право, чужое право или `RULESET`.

### BASIS — основание

Проверяемая причина возникновения, изменения или прекращения права: вклад, членство, общественный режим капитала, природный базис, договор, делегирование, решение или remedy.

Минимальные поля: `basis_id`, `basis_type`, `establishing_process`, `evidence_refs`, `valid_from`, `valid_until`, `ruleset_id`, `state`, `dependent_objects`, `provenance`.

`establishing_process` указывает не абстрактного «эмитента», а компетентную процедуру, доказательства и решение, которыми основание установлено.

### COMPETENCE — компетенция

Право принимать конкретный класс решений по конкретному объекту и функции. Компетенция отделена от собственности, управленческого power и технической capability.

Минимальные поля: `competence_id`, `holder`, `action_class`, `object_scope`, `source`, `limits`, `required_approvals`, `term`, `review`, `recusal`, `substitution`, `revocation`, `ruleset_id`, `state`, `provenance`.

### RULESET — набор правил

Версионированный набор условий допустимости. Каждое решение и переход ссылаются на точную действовавшую версию. Изменение `RULESET` является защищённым классом события.

Минимальные поля: `ruleset_id`, `version_identity`, `scope`, `level`, `effective_from`, `supersedes`, `root_lineage`, `amendment_class`, `approval_evidence`, `conflict_rule`, `state`, `provenance`.

### STATE TRANSITION — переход состояния

Предложенное или выполненное изменение объекта, права, основания, компетенции или набора правил.

Минимальные поля:

- `transition_id`, `transition_type`, `initiator`;
- `pre_state_ref`, `proposed_post_state`;
- `affected_rights`, `basis_id`, `competence_id`, `ruleset_id`;
- `requirements_snapshot`, `approval_evidence`;
- `reversibility_class`, `protection_class`, `challenge_barrier`;
- `causal_parents`, `aggregate_effect`, `status`;
- `execution_ref`, `provenance`.

`requirements_snapshot` является immutable-снимком требований exact `RULESET/COMPETENCE` на момент авторизации, а не второй редактируемой копией правил.

## 2. Конституционный корень

### ROOT INVARIANTS

Корневые инварианты ограничивают не только обычные решения, но и изменение механизма изменения правил:

1. техническая capability не создаёт authority;
2. управление не создаёт собственность;
3. капитал не создаёт политический голос;
4. членство, базовый голос, информация, выход и challenge не продаются как экономический актив;
5. неделимый общественный капитал не является суммой долей текущего состава;
6. субъект не может единолично расширить собственную компетенцию или снять собственный контроль;
7. один субъект не контролирует initiation, authorization и final resolution одной causal lineage;
8. запрещённый результат нельзя легализовать разбиением на цепочку формально допустимых действий;
9. защита объекта следует за его provenance при переклассификации, преобразовании и передаче;
10. исправление сохраняет историю и не превращается в новое присвоение;
11. уровень правил не получает остаточную верховную компетенцию только из-за своего положения выше;
12. отсутствие review/resolution-holder не означает автоматического разрешения перехода.

### META-AMENDMENT — изменение механизма поправок

Изменение root-инварианта, amendment-процедуры, состава независимого контроля или правил causal-lineage относится к `META_AMENDMENT`.

Для него обязательны:

- отдельное предложение с явным перечнем затронутых ограничений;
- immutable до-состояние и полный lineage правил;
- раскрытие выгодоприобретателей и конфликтов интересов;
- независимая проверка вне competence-holder, чья власть меняется;
- проверка меньшинства, общественного капитала и будущего интереса;
- повышенный барьер, отличный от обычного управления;
- challenge до исполнения;
- невозможность одним решением одновременно изменить процедуру и применить новую процедуру к связанному распределению/назначению;
- отложенное вступление в силу либо иной барьер против одномоментного захвата;
- повторная проверка causal effect перед вступлением в силу.

Точные кворумы, пороги и сроки задаёт утверждённый root-ruleset. Их отсутствие не разрешает переход: это `META_AMENDMENT_BLOCKED_MISSING_RULE`.

## 3. Общие инварианты допустимости

1. Нет действующего права без субъекта, объекта, действующего основания и exact ruleset.
2. Нет действия без компетенции, охватывающей action class, object scope и текущую фазу.
3. Отзыв или приостановка `BASIS/COMPETENCE` влияет на зависимые объекты по заранее установленному propagation rule.
4. Делегат не изменяет источник, предел или контроль собственной компетенции.
5. Экономический договор не создаёт эквивалент запрещённого членского или резервного права.
6. Переклассификация наследует наиболее строгую защиту причинных родителей, пока компетентное независимое решение не докажет допустимое снижение защиты.
7. Серия переходов, эквивалентная запрещённому прямому переходу, запрещена или наследует его protection class.
8. `R2/R3` и конституционные переходы требуют review до исполнения.
9. Перед исполнением повторно проверяются pre-state, ruleset, competence, approvals, conflict state и критические входы.
10. После challenge спорный объект получает interim protection и не очищается последующими передачами.
11. Любое blocked-состояние имеет безопасный interim state и маршрут fallback/escalation.
12. Терминальность не препятствует reopening при доказательстве ошибки, мошенничества, скрытого конфликта или несовпадения исполнения с авторизацией.

## 4. Жизненные циклы

### 4.1. STATE TRANSITION

Основной путь:

`DRAFT → PROPOSED → VALIDATED → AUTHORIZED → REVALIDATED → EXECUTABLE → EXECUTED → SETTLED`

До исполнения:

`PROPOSED/VALIDATED/AUTHORIZED → CHALLENGED → SUSPENDED → RESOLVED → REJECTED | MODIFIED_FOR_REVALIDATION | EXECUTABLE`

После исполнения:

`EXECUTED/SETTLED → CHALLENGED → TAINTED_UNDER_REVIEW → RESOLVED → UPHELD | VOIDED | REMEDY_REQUIRED → REMEDIED | REMEDY_BLOCKED`

Тупиковая ветка:

`CHALLENGED/SUSPENDED → RESOLUTION_BLOCKED → ESCALATED → RESOLVED | UNRESOLVED_WITH_RESTRICTIONS`

`REJECTED` относится к неисполненному предложению. `VOIDED/REVOKED` относится к уже исполненному переходу и не удаляет его историческую запись.

### 4.2. BASIS

`PROPOSED → VALIDATED → VALID → SUSPENDED | EXPIRED | REVOKED | SUPERSEDED`

Дополнительная ветка:

`VALID/SUSPENDED → CHALLENGED → UPHELD | REVOKED | MODIFIED | UNRESOLVED_WITH_RESTRICTIONS`

При `SUSPENDED/REVOKED/EXPIRED` система применяет `dependency_effect`: pause, freeze_new_actions, preserve_existing_claim, recalculate, challenge_required или иной exact rule. Молчаливое уничтожение зависимых прав запрещено.

### 4.3. COMPETENCE

`NOMINATED → ELIGIBILITY_VALIDATED → ACTIVE → SUSPENDED | RECUSED | EXPIRED | REVOKED | SUPERSEDED`

При конфликте интересов используется `RECUSED`, после чего назначается допустимый substitute. Отзыв действует по зафиксированному ordering: переход не считается авторизованным, если компетенция была недействительна в момент авторизации; перед исполнением её действительность проверяется снова.

### 4.4. RULESET

`DRAFT → REVIEWED → APPROVED_NOT_EFFECTIVE → EFFECTIVE → SUPERSEDED | SUSPENDED | VOIDED`

Обычная поправка и `META_AMENDMENT` имеют разные action classes. Новый ruleset не применяется к связанному переходу до `effective_from` и завершения обязательного challenge barrier.

### 4.5. REVIEW / RESOLUTION CASE

`OPENED → ELIGIBILITY_CHECK → ASSIGNED → EVIDENCE_COMPLETE → DELIBERATION → DECIDED → IMPLEMENTATION_TRACKED → CLOSED`

Ветки:

- `ASSIGNED → RECUSED → REASSIGNMENT`;
- `OPENED/REASSIGNMENT → VACANT → SUBSTITUTION_OR_ESCALATION`;
- `EVIDENCE_COMPLETE/DELIBERATION → DEADLOCK → ESCALATED`;
- `DECIDED → REMEDY_REQUIRED → REMEDIED | REMEDY_BLOCKED`.

## 5. Независимая REVIEW / RESOLUTION COMPETENCE

Независимость является проверяемым свойством конкретного дела, а не названием органа.

### Eligibility

Review/resolution-holder не должен:

- быть инициатором или непосредственным выгодоприобретателем;
- контролироваться субъектом авторизации;
- участвовать в создании спорного evidence как ответственная сторона;
- иметь нераскрытый материальный или управленческий конфликт;
- одновременно контролировать назначение собственного substitute и итог дела.

### Назначение и срок

Ruleset задаёт способ назначения, срок, ротацию, основания отвода, отзыв за нарушение, пул substitute и fallback-уровень. Отзыв не может применяться как наказание за неблагоприятное решение без отдельной проверки.

### Recusal и vacancy

При конфликте holder обязан отвестись. Если допустимый substitute отсутствует, дело переходит в `RESOLUTION_BLOCKED`, а объект — в заранее определённое безопасное interim state. Vacancy не даёт инициатору права назначить удобного арбитра ad hoc.

### Разделение контроля

Один субъект или фактически контролируемая группа не может одновременно контролировать три стадии одной causal lineage:

`initiation → authorization → final resolution`.

Если независимость невозможно подтвердить, положительное решение не становится `EXECUTABLE`.

## 6. Causal-lineage и anti-circumvention

Каждый переход хранит причинных родителей и вычисляемый совокупный эффект.

### Aggregate causal-lineage check

Перед `AUTHORIZED`, `REVALIDATED` и `EXECUTABLE` проверяется:

- не изменились ли за рассматриваемую цепочку holder, competence, reviewer или ruleset;
- не снизилась ли защита объекта через последовательные классификации;
- не возник ли экономический эквивалент запрещённого права;
- не получил ли один субъект совокупный контроль, отсутствующий в каждом отдельном шаге;
- не соединены ли связанные поправка правил и извлечение выгоды;
- не были ли промежуточные действия заранее согласованными частями одного результата.

Если совокупный результат эквивалентен запрещённому прямому переходу, вся цепочка отклоняется либо наследует наиболее строгий protection class.

### Tainted lineage

После challenge спорный статус следует за объектом, его производными, обеспечением и преобразованными требованиями. Передача третьему лицу не очищает provenance. Допустимый ruleset определяет защиту добросовестной стороны, но не может удалять исходный спор.

## 7. Классы обратимости и безопасные состояния

- `R0 reversible`: отменяется без существенного вреда;
- `R1 compensable`: полный возврат невозможен, но допустима проверяемая компенсация;
- `R2 hard_to_reverse`: восстановление дорого, медленно или затрагивает третьих лиц;
- `R3 irreversible`: восстановление объекта невозможно.

Для `R2/R3` обязательны расширенное раскрытие, future-impact review, challenge до исполнения, независимая проверка и повышенный барьер.

При споре safe interim state может включать: запрет отчуждения, ограничение новых обязательств, сохранение минимальной эксплуатации, escrow, разделение бесспорной и спорной части либо временное управление без права менять титул. Конкретный режим задаётся ruleset по классу объекта.

## 8. Вход нового участника

### Admission state machine

`APPLIED → ELIGIBILITY_VALIDATED → ADMITTED → MEMBERSHIP_ACTIVE`

Альтернативы:

- `APPLIED/ELIGIBILITY_VALIDATED → REJECTED → CHALLENGED → UPHELD | ADMITTED`;
- `ELIGIBILITY_VALIDATED/ADMITTED → ACTIVATION_DELAYED → ESCALATED → MEMBERSHIP_ACTIVE | REJECTED_WITH_REASON`.

Компетенции допуска, отказа и активации разделены либо контролируются независимым review. После `ADMITTED` базовое членское право не зависит от произвольной административной кнопки. Задержка требует exact basis, ограниченного срока и escalation/fallback.

### Права и накопленный капитал

Вступление создаёт членские права с установленного момента, но не создаёт ретроактивное личное требование на ранее накопленный капитал. Участник получает право совместного использования и управления общественным капиталом без автоматической ликвидационной доли.

Отсрочка отдельных экономических преимуществ должна быть общей, заранее известной, ограниченной и оспоримой. Она не затрагивает базовый голос и право информации после активации членства.

### Договорный anti-circumvention

Договор после вступления не может создавать `CLAIM`, обеспечение, опцион, гарантированный поток или иной экономический эквивалент доли protected reserve, если прямое возникновение такой доли запрещено.

## 9. Неделимый резерв

### Классы

- `R-CONTINUITY`: непрерывность деятельности;
- `R-INFRASTRUCTURE`: долгоживущая инфраструктура;
- `R-INTERGENERATIONAL`: капитал будущих участников;
- `R-OBLIGATION`: обеспечение обязательств;
- `R-TRANSFORMABLE`: изменение режима возможно только конституционной процедурой.

### Управление и раздел

Обычное большинство управляет использованием в пределах назначения, но не превращает резерв в личные требования. Самораздел `R-CONTINUITY`, `R-INFRASTRUCTURE`, `R-INTERGENERATIONAL`, `R-OBLIGATION` запрещён. `R-TRANSFORMABLE` требует защищённой поправки.

### Protected classification transition

Смена classification является переходом не слабее последующего действия с объектом. Она требует:

- исходного BASIS и полного provenance;
- сохранения наиболее строгого protection class причинных родителей;
- независимого review;
- future-impact review, если затронут долгосрочный базис;
- aggregate causal-lineage check;
- challenge до исполнения;
- запрета связанной переклассификации и личного распределения одним пакетом решений.

Цепочка `R-INTERGENERATIONAL → R-TRANSFORMABLE → personal CLAIM` рассматривается как попытка раздела исходного `R-INTERGENERATIONAL`, пока независимое решение не докажет иной допустимый совокупный эффект.

## 10. Будущие участники и поколения

Будущий субъект представляется ограничением компетенции текущего состава, а не фиктивным голосующим аккаунтом.

### FUTURE IMPACT REVIEW как gate

Результаты: `PASS`, `FAIL`, `UNRESOLVED`.

Обязательные evidence:

- горизонт и затронутый базис;
- необратимость и класс перехода;
- минимальный сохраняемый уровень капитала/ресурса;
- текущие выгодоприобретатели и отложенные носители риска;
- альтернативы;
- восстановительное или компенсационное обязательство;
- uncertainty и отсутствующие данные.

`FAIL` запрещает исполнение. `UNRESOLVED` переводит переход в `SUSPENDED` или `UNRESOLVED_WITH_RESTRICTIONS`; он не трактуется как молчаливое согласие.

### Lifecycle представителя будущего интереса

Используется общий lifecycle `COMPETENCE`: nomination, eligibility, term, conflict disclosure, recusal, substitution, review, revocation. Представитель не становится собственником капитала, не извлекает личную выгоду и не получает неограниченного veto.

При vacancy включается предусмотренный substitute/escalation. Отсутствие представителя не разрешает переход автоматически и не замораживает систему без fallback.

## 11. Challenge, resolution и remedy

### Кто может оспаривать

Носитель затронутого права; участник с правом контроля; уполномоченный защитник общественного, природного или будущего интереса; сторона, чья компетенция обойдена.

### Основания

- недействительное `BASIS`;
- выход за `COMPETENCE`;
- неверный `RULESET`;
- нарушение root-инварианта;
- скрытые данные, согласия или конфликт;
- обход через classification, договор или causal lineage;
- несовпадение исполнения с авторизацией;
- ошибочный класс обратимости/защиты;
- утрата независимости review/resolution.

### Interim protection

После допустимого challenge спорный объект, производные требования и ещё не исполненный переход получают tainted status и безопасное interim state. Interim competence ограничена сохранением объекта и не позволяет переписать право или правила.

### Resolution outcomes

`UPHOLD`, `REJECT`, `MODIFY_BEFORE_EXECUTION`, `VOID_EXECUTED_EFFECT`, `REMEDY_REQUIRED`, `ESCALATE_RULE_CONFLICT`, `UNRESOLVED_WITH_RESTRICTIONS`.

### Remedy

Новая запись связывается с нарушением; старая не удаляется. Возможны обратный переход, восстановление права, компенсация, заморозка, отзыв делегирования, исправление классификации, смена ключей или конституционная эскалация.

Remedy ограничен устранением подтверждённого нарушения. При `R3` фиксируются невозможность полного восстановления, остаточный ущерб и обязательства по его снижению.

### Blocked fallback

Если решение или remedy невозможно:

1. фиксируется `RESOLUTION_BLOCKED` либо `REMEDY_BLOCKED` с exact dependency;
2. применяется safe interim state;
3. запускается заранее определённая substitution/escalation;
4. по истечении установленного ruleset предела дело получает `UNRESOLVED_WITH_RESTRICTIONS`, а не исчезает и не разрешается автоматически;
5. новые действия с tainted object ограничены до появления допустимого resolution/remedy.

## 12. Revalidation непосредственно перед execution

`AUTHORIZED` не гарантирует будущую исполнимость. Перед каждым execution система повторно проверяет:

- совпадает ли фактический pre-state;
- действует ли exact ruleset;
- активна ли competence и не отозвана ли она;
- действуют ли approvals;
- завершён ли challenge barrier;
- не появился ли challenge, conflict, tainted parent или новое обязательное evidence;
- неизменны ли critical external inputs либо заново ли они валидированы;
- совпадает ли payload с авторизованным предложением;
- не изменился ли aggregate causal effect.

Провал проверки даёт `REVALIDATION_FAILED` и возвращает переход в `SUSPENDED/MODIFIED_FOR_REVALIDATION`; молчаливое исполнение запрещено.

## 13. Конфликт RULESET разных уровней

Полицентрическая система не предполагает автоматического приоритета верхнего уровня.

Порядок проверки:

1. определить объект и функцию конфликта;
2. установить explicit delegation и её пределы;
3. проверить exclusive/shared/local competence;
4. применить special rule к конкретному объекту, если он создан компетентным уровнем и не нарушает root-инварианты;
5. при действительном shared scope применить заранее установленную coordination/conflict procedure;
6. при неустранимом конфликте — `RULESET_CONFLICT_BLOCKED` и независимый resolution, а не остаточная власть федерации.

## 14. Таблица основных переходов

| Объект | Из состояния | Событие | Компетенция | Guards | В состояние | Failure state |
|---|---|---|---|---|---|---|
| RIGHT | PROPOSED | establish | establish-right | BASIS valid, ruleset exact, approvals | ACTIVE | REJECTED/SUSPENDED |
| BASIS | VALIDATED | activate | establish-basis | evidence, establishing process, no conflict | VALID | REJECTED |
| COMPETENCE | ELIGIBILITY_VALIDATED | appoint | appoint-competence | term, limits, conflict check | ACTIVE | VACANT/REJECTED |
| RULESET | APPROVED_NOT_EFFECTIVE | activate | ruleset-amend | root/meta guards, challenge complete | EFFECTIVE | BLOCKED/VOIDED |
| STATE TRANSITION | AUTHORIZED | execute | execute-transition | revalidation, lineage, payload match | EXECUTED | REVALIDATION_FAILED |
| REVIEW CASE | ASSIGNED | decide | resolution | independence, evidence complete | DECIDED | DEADLOCK/RESOLUTION_BLOCKED |
| RESERVE | PROTECTED | reclassify | constitutional-classification | provenance, strictest protection, future review | RECLASSIFIED_PROTECTED | REJECTED/SUSPENDED |
| MEMBERSHIP | ADMITTED | activate | membership-activation | admission final, no arbitrary delay | ACTIVE | ACTIVATION_DELAYED/ESCALATED |

Полная машинная таблица должна быть отдельным schema-артефактом только после успешного повторного review; эта таблица проверяет замыкание основных путей, но не притворяется готовым контрактом.

## 15. Значение SETTLED и reopening

`SETTLED` означает: переход исполнен, обязательный обычный challenge window завершён, открытого спора нет, а требуемый remedy исполнен либо отсутствует.

`SETTLED` не означает неоспоримость навсегда. Reopening допускается по отдельной competence при новом доказательстве мошенничества, скрытого конфликта, ошибки идентичности, несовпадения исполнения с решением или нарушении root-инварианта. Reopening создаёт новую lineage и не удаляет settled-запись.

## 16. Машинно-проверяемая допустимость

Переход становится `EXECUTABLE`, только если:

`subject and object exist`

`AND pre-state matches`

`AND basis is VALID under exact effective ruleset`

`AND competence is ACTIVE and covers phase/action/object`

`AND requirements_snapshot matches authorized rules`

`AND approvals remain valid`

`AND root invariants hold`

`AND aggregate causal-lineage check passes`

`AND required reviews PASS`

`AND challenge barrier is satisfied`

`AND critical inputs are immutable or revalidated`

`AND execution payload equals authorized proposal`.

Формальный PASS необходим, но не заменяет challenge и независимое resolution для содержательного конфликта.

## 17. Минимальный event-log

Сохраняются предложение, автор, до-/после-состояние, затронутые права, основание, компетенция, exact ruleset, requirements snapshot, approvals, reversible/protection class, causal parents, aggregate effect, conflicts, challenge, review eligibility, решение, исполнение, remedy, blocked dependency, residual harm и полный provenance.

Ни supersede, ни void, ни remedy не удаляют прежние события.

## 18. Граница WBN/WBNP

Из модели выводятся требования к реестру, но не эмиссия, цена, распределение или политические права WBN/WBNP. Монета, токен, членство, голос, `CLAIM`, `RESERVE`, `COMPETENCE` и природное право остаются разными типами объектов.

Владение WBN/WBNP не создаёт членство, голос, компетенцию или долю неделимого капитала без отдельного допустимого права и основания.

## 19. Матрица закрытия замечаний SHT

| Замечание | Исправление v0.2 |
|---|---|
| C1 | ROOT INVARIANTS, META_AMENDMENT, lineage правил |
| C2 | REVIEW/RESOLUTION lifecycle, eligibility, recusal, vacancy, substitution |
| C3 | RESOLUTION_BLOCKED, REMEDY_BLOCKED, escalation, safe interim, UNRESOLVED_WITH_RESTRICTIONS |
| C4 | protected classification transition и наследование защиты provenance |
| C5 | aggregate causal-lineage check и strictest protection inheritance |
| S1–S2 | admission state machine и договорный anti-circumvention |
| S3–S4 | FUTURE IMPACT REVIEW gate и lifecycle представителя |
| S5–S6 | tainted lineage, interim protection, execution revalidation |
| S7–S9 | BASIS/COMPETENCE lifecycle, SETTLED и reopening |
| S10 | object/function/delegation conflict algorithm без автоматического верховенства |
| E1–E5 | разведение manage/competence, establishing process, requirements snapshot, proposal/executed outcomes, transition table |

Матрица подтверждает наличие ответа в тексте, но не доказывает достаточность исправления. Это предмет повторного независимого review.

## 20. Критерии повторной проверки

ШТАБИСТУ следует проверить:

1. можно ли изменить root/meta-amendment через обходную последовательность;
2. можно ли фактически контролировать независимый review через назначение, отзыв, vacancy или substitute;
3. существует ли путь из каждого challenge/blocked/remedy state;
4. следует ли защита за резервом и производными объектами;
5. обнаруживается ли совокупный захват управления;
6. можно ли необоснованно задержать или купить членство;
7. блокирует ли `FAIL/UNRESOLVED` future-impact review исполнение;
8. предотвращает ли revalidation исполнение устаревшего решения;
9. не создаёт ли conflict algorithm скрытую остаточную власть верхнего уровня;
10. какие пробелы остаются `critical / significant / editorial`.

## Статус

specification_status: candidate_v0_2_pending_independent_re_review
previous_status: candidate_structurally_complete_with_open_execution_guards
review_findings_addressed_in_text: C1-C5_S1-S10_E1-E5
independent_re_review: pending
wbn_wbnp_bridge: registry_requirements_only
production_authority: none

---

КТО: VOL / ВОЛОНТЁР
КОГДА: метка времени не ставилась; доверенный проектный источник времени не использовался
ДЛЯ ЧЕГО: исправить кандидатную спецификацию прав и переходов по результатам независимой проверки ШТАБИСТА и вернуть её на повторный stress-review
СТАТУС: candidate_v0_2_pending_independent_re_review
