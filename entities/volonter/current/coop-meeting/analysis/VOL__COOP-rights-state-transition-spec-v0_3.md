# Политэкономия совладения: спецификация прав и переходов состояния v0.3

## Смысл и требуемое действие

Версия v0.3 закрывает два критических и сопутствующие замечания повторного review ШТАБИСТА: выделяет неотменяемый противозахватный минимум, отделяет его изменение от обычной конституционной lineage и задаёт полный жизненный цикл `RIGHT` с таблицей влияния зависимых объектов.

Дополнительно устранены прямой обход повторной проверки после challenge, смешение отвода по конкретному делу с глобальным состоянием компетенции, неоднозначность окончательного допуска участника, разрыв blocked/fallback, несовпадение VOID outcome/state и отсутствие общего reopening-контракта.

Статус остаётся исследовательским кандидатом. Документ не является утверждённой нормой, токеномикой WBN/WBNP, готовой validator-схемой или разрешением на production.

Требуемое действие: один ограниченный независимый re-review ШТАБИСТА по C1/C2, S1/S7 и связанным исправлениям. До этого lifecycle не считается подтверждённо замкнутым.

## Проверяемая база

- v0.2: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_2.md`, commit `dc7cf783876e9877b60ee985aa4bf2956be4337d`, blob `683351419054d15b31a13fcd2475a551a39bed8e`;
- повторный review: `entities/shtabist/outbox/SHT__COOP-rights-transition-v0_2-re-review__VOL.md`, commit `41402b0d678f4387730c36bdf1805a389e710732`, blob `4d7ee1a8c4035a17ed46c46f7d400e5f37a76c20`;
- review status: `RE_REVIEW_COMPLETE_WITH_REMAINING_GAPS`;
- findings: 2 critical, 7 significant, 4 editorial.

## 1. Объекты модели

### SUBJECT

Носитель права или компетенции: человек, участник, продолжающийся коллектив, локальный Союз, федерация, общественный или природный контур. Аккаунт, ключ и программа являются средствами действия и не создают право или компетенцию.

Поля: `subject_id`, `subject_type`, `status`, `representation`, `affiliations`, `conflict_disclosures`, `provenance`.

### OBJECT

Результат труда, требование, резерв, инфраструктура, природный ресурс, поток, решение, правило, компетенция либо другое проверяемо классифицированное благо или отношение.

Поля: `object_id`, `object_type`, `classification`, `state`, `protection_class`, `causal_lineage`, `provenance`.

### RIGHT

Связь субъекта с объектом на определённом основании. Она хранится отдельно от баланса, технической capability и компетенции изменять право.

Поля: `right_id`, `subject_id`, `object_id`, `right_type`, `powers`, `scope`, `transferability`, `basis_id`, `ruleset_id`, `state`, `protection_class`, `causal_lineage`, `provenance`.

Power `manage` не создаёт `COMPETENCE` изменять право, объект или ruleset.

### BASIS

Проверяемая причина возникновения, изменения или прекращения права: вклад, членство, общественный режим капитала, природный базис, договор, делегирование, решение или remedy.

Поля: `basis_id`, `basis_type`, `establishing_process`, `evidence_refs`, `valid_from`, `valid_until`, `ruleset_id`, `state`, `dependency_effect`, `provenance`.

### COMPETENCE

Право принимать конкретный класс решений по конкретному объекту и на конкретной фазе.

Поля: `competence_id`, `holder`, `action_class`, `object_scope`, `phase_scope`, `source`, `limits`, `term`, `review`, `revocation`, `ruleset_id`, `state`, `provenance`.

### RULESET

Версионированный набор условий допустимости.

Поля: `ruleset_id`, `version_identity`, `scope`, `level`, `effective_from`, `root_lineage`, `amendment_class`, `approval_evidence`, `conflict_rule`, `state`, `provenance`.

### STATE TRANSITION

Предложенное или выполненное изменение объекта, права, основания, компетенции или правил.

Поля: `transition_id`, `transition_type`, `initiator`, `pre_state_ref`, `proposed_post_state`, `affected_objects`, `basis_id`, `competence_id`, `ruleset_id`, `requirements_snapshot`, `approval_evidence`, `reversibility_class`, `protection_class`, `challenge_barrier`, `causal_parents`, `aggregate_effect`, `state`, `execution_ref`, `provenance`.

`requirements_snapshot` — неизменяемый снимок требований exact ruleset/competence на момент авторизации, не самостоятельная редактируемая копия правил.

## 2. Неотменяемый противозахватный минимум

### ENTRENCHED_ROOT

Следующие инварианты не могут быть отменены или ослаблены `AMENDMENT` либо `META_AMENDMENT` внутри данной constitutional lineage:

1. техническая capability не создаёт authority;
2. управление не создаёт собственность;
3. капитал не создаёт политический голос;
4. субъект не расширяет собственную компетенцию и не снимает собственный контроль единолично;
5. один контролирующий субъект не совмещает initiation, authorization и final resolution одной causal lineage;
6. запрещённый результат нельзя легализовать разбиением на формально допустимые действия;
7. защита объекта следует за provenance и производными объектами;
8. неделимый общественный капитал не является суммой долей текущего состава;
9. членство, базовый голос, информация, выход и challenge не продаются как экономический актив;
10. remedy сохраняет историю и ограничен устранением нарушения;
11. отсутствие review/resolution-holder не означает автоматического разрешения;
12. более высокий уровень не получает остаточную компетенцию только из-за своего положения.

Любое предложение отменить или ослабить один из этих пунктов получает состояние `OUTSIDE_CURRENT_CONSTITUTIONAL_LINEAGE` и не может стать `AUTHORIZED` в текущей системе.

### RE-FOUNDING — учреждение новой lineage

Полный пересмотр `ENTRENCHED_ROOT` возможен только как учреждение другой конституционной системы, а не поправка текущей. Re-founding обязан:

- прямо объявить создание новой lineage и перечислить отличия;
- не переписывать задним числом права и события старой lineage;
- не переносить автоматически protected reserve, обязательства, членство, голоса и компетенции;
- предложить участникам информированное присоединение либо реальный выход;
- отдельно урегулировать кредиторов, меньшинство, общественный/природный базис и будущий интерес;
- сохранить полный provenance;
- иметь независимую учредительную проверку;
- не использовать ключи и компетенции старой системы как достаточное основание новой легитимности.

До отдельного утверждённого re-founding ruleset такой переход имеет состояние `RE_FOUNDING_NOT_DEFINED` и не исполняется. Эта спецификация не утверждает процедуру re-founding; она проводит границу полномочий текущей lineage.

## 3. Поправки внутри действующей lineage

### AMENDMENT

Изменяет обычные правила, не затрагивая amendment-механизм и `ENTRENCHED_ROOT`.

### META_AMENDMENT

Изменяет amendment-процедуру, состав независимого контроля или правила causal-lineage, но не вправе отменять или ослаблять `ENTRENCHED_ROOT`.

Обязательны: точная область изменения, immutable до-состояние, раскрытие выгод и конфликтов, независимая проверка, проверка меньшинства/резерва/будущего интереса, повышенный барьер, challenge до вступления в силу, запрет одномоментного изменения процедуры и извлечения связанной выгоды, отложенное вступление в силу и aggregate-lineage check.

### Отсутствующее конституционное правило

`META_AMENDMENT_BLOCKED_MISSING_RULE` является terminal-safe state для конкретного предложения:

- предложение не имеет правового эффекта;
- действующий ruleset и protected objects сохраняются;
- выход возможен только через ранее и независимо принятый допустимый meta-amendment, устанавливающий отсутствующее общее правило для будущих предложений, либо через re-founding;
- отсутствующее правило нельзя создать и применить к тому же связанному предложению одним пакетом.

## 4. Общие инварианты допустимости

1. Нет действующего права без субъекта, объекта, действующего основания и exact effective ruleset.
2. Нет действия без ACTIVE competence, охватывающей фазу, action class и object scope.
3. Отзыв или suspension основания/компетенции влияет на зависимые объекты только через явный propagation rule.
4. Экономический договор не создаёт эквивалент запрещённого членского или резервного права.
5. Серия переходов наследует наиболее строгую защиту своих причинных родителей.
6. Снижение наследуемой защиты допустимо только при ссылке на exact clause действующего ruleset, разрешённый `ENTRENCHED_ROOT`, проверяемое evidence и независимое решение; без любого элемента downgrade запрещён.
7. `R2/R3`, protected classification и конституционные переходы требуют review до исполнения.
8. Любой положительный исход challenge проходит новую `REVALIDATION`.
9. Перед execution повторно проверяются pre-state, ruleset, competence, approvals, challenge, causal lineage и critical inputs.
10. Challenge создаёт tainted lineage и safe interim state.
11. Любое blocked-состояние имеет явно определённый fallback либо прямо объявлено terminal-safe.
12. Terminal state допускает reopening только по общему reopening-контракту.

## 5. Жизненный цикл RIGHT

### Основной путь

`PROPOSED → VALIDATED → ACTIVE → SUSPENDED | CHALLENGED | TRANSFER_PENDING | EXPIRED | REVOKED | SUPERSEDED | TERMINATED`

### Challenge

`ACTIVE/SUSPENDED/TRANSFER_PENDING → CHALLENGED → TAINTED_UNDER_REVIEW → UPHELD | MODIFIED | REVOKED | REMEDY_REQUIRED | UNRESOLVED_WITH_RESTRICTIONS`

### Transfer

`ACTIVE → TRANSFER_PENDING → TRANSFER_VALIDATED → TRANSFERRED`

`TRANSFERRED` завершает право прежнего субъекта и создаёт новое `RIGHT` приобретателя со ссылкой на предшественника. Историческое право не перезаписывается. Непередаваемое право не входит в этот путь.

### Remedy

`REMEDY_REQUIRED → REMEDIED_ACTIVE | REMEDIED_TERMINATED | REMEDY_BLOCKED`

`REMEDIED_ACTIVE` создаёт исправленную действующую версию права; прежняя остаётся в lineage. `REMEDIED_TERMINATED` фиксирует восстановление/компенсацию без продолжения права.

### Смысл состояний

- `ACTIVE`: право существует и может осуществляться в пределах scope;
- `SUSPENDED`: существование не уничтожено, но осуществление полностью или частично приостановлено;
- `CHALLENGED/TAINTED_UNDER_REVIEW`: право спорно, производные действия ограничены;
- `EXPIRED`: окончен установленный срок;
- `REVOKED`: прекращено компетентным защищённым решением;
- `SUPERSEDED`: заменено новым правом с сохранением lineage;
- `TERMINATED`: окончено предусмотренным событием;
- `TRANSFERRED`: право прежнего holder завершено допустимой передачей;
- `UNRESOLVED_WITH_RESTRICTIONS`: спор не разрешён, право сохраняется только в безопасно ограниченном режиме.

## 6. Propagation table: зависимые события → RIGHT

| Событие | Обязательный эффект для RIGHT | Запрещённый эффект |
|---|---|---|
| BASIS SUSPENDED | RIGHT → SUSPENDED или scoped restriction по exact dependency_effect | молчаливое прекращение |
| BASIS REVOKED/VOIDED | RIGHT → CHALLENGED/REVIEW; затем REVOKED, MODIFIED или REMEDIED | автоматическое удаление истории |
| BASIS EXPIRED | RIGHT → EXPIRED, если право не имеет независимого действующего basis | продолжение без основания |
| BASIS SUPERSEDED | RIGHT revalidation против нового basis; ACTIVE либо MODIFIED/SUSPENDED | автоматическая подмена basis |
| COMPETENCE SUSPENDED/REVOKED до authorization | связанный переход не AUTHORIZED | сохранение недействительной авторизации |
| COMPETENCE SUSPENDED/REVOKED после authorization до execution | transition → REVALIDATION_FAILED; RIGHT не меняется | исполнение по старой competence |
| RULESET SUPERSEDED до execution | обязательная revalidation по transition rule и grandfathering clause | молчаливое применение удобной версии |
| RULESET VOIDED | затронутые RIGHTS/TRANSITIONS → scoped review/tainted state | массовое автоматическое уничтожение |
| CHALLENGE права | RIGHT → CHALLENGED/TAINTED; производные переходы ограничены | очистка спора передачей |
| VALID TRANSFER | прежний RIGHT → TRANSFERRED; новый RIGHT → ACTIVE с lineage | перезапись holder в старой записи |
| REMEDY | новая связанная версия RIGHT либо компенсационное CLAIM | удаление исходного нарушения |
| REOPEN terminal object | создаётся review lineage; terminal record сохраняется | возврат записи в прошлое состояние без события |

Точный propagation выбирается ruleset по типу права и основания, но он не может нарушать `ENTRENCHED_ROOT`.

## 7. Жизненные циклы остальных объектов

### BASIS

`PROPOSED → VALIDATED → VALID → SUSPENDED | CHALLENGED | EXPIRED | REVOKED | SUPERSEDED`

### COMPETENCE

`NOMINATED → ELIGIBILITY_VALIDATED → ACTIVE → SUSPENDED | EXPIRED | REVOKED | SUPERSEDED`

Отвод по конкретному делу не меняет глобальное состояние competence. Он хранится как `CASE_RECUSAL(case_id, competence_id, holder, basis, substitute)`.

### RULESET

`DRAFT → REVIEWED → APPROVED_NOT_EFFECTIVE → EFFECTIVE → SUSPENDED | SUPERSEDED | VOIDED`

Переход в `EFFECTIVE` создаётся отдельным `RULESET_ACTIVATION` event только после `effective_from`, завершения challenge barrier и повторной проверки отсутствия открытого challenge. Challenge, открытый до или на границе активации, оставляет ruleset в `APPROVED_NOT_EFFECTIVE` либо переводит в `SUSPENDED_PENDING_REVIEW`.

### STATE TRANSITION

`DRAFT → PROPOSED → VALIDATED → AUTHORIZED → REVALIDATION_REQUIRED → REVALIDATED → EXECUTABLE → EXECUTED → SETTLED`

До исполнения:

`PROPOSED/VALIDATED/AUTHORIZED/REVALIDATION_REQUIRED → CHALLENGED → SUSPENDED → RESOLVED`

Положительный исход:

`RESOLVED → REVALIDATION_REQUIRED → REVALIDATED → EXECUTABLE`

Отрицательный или изменяющий исход:

`RESOLVED → REJECTED | MODIFIED_FOR_REVALIDATION | ESCALATED`

После исполнения:

`EXECUTED/SETTLED → CHALLENGED → TAINTED_UNDER_REVIEW → RESOLVED → UPHELD | VOIDED | REMEDY_REQUIRED → REMEDIED | REMEDY_BLOCKED`

Outcome/event `VOID_EXECUTED_EFFECT` переводит исполненный transition в state `VOIDED`. Это событие и состояние, а не два конкурирующих результата.

### REVIEW / RESOLUTION CASE

`OPENED → ELIGIBILITY_CHECK → ASSIGNED → EVIDENCE_COMPLETE → DELIBERATION → DECIDED → IMPLEMENTATION_TRACKED → CLOSED`

Ветки: `CASE_RECUSAL → REASSIGNMENT`; `VACANT → SUBSTITUTION_OR_ESCALATION`; `DEADLOCK → ESCALATED`; `REMEDY_REQUIRED → REMEDIED | REMEDY_BLOCKED`.

## 8. Независимость review/resolution

Независимость проверяется для каждого дела.

Holder не может быть инициатором, выгодоприобретателем, ответственным создателем спорного evidence либо находиться под запрещённым control/affiliation.

`CONTROL/AFFILIATION CHECK` обязан ссылаться на exact ruleset criteria и evidence по категориям: право назначения/отзыва, обязательные инструкции, владение/финансирование, семейная или договорная связанность, общий выгодоприобретатель, совместное управление и иные прямо определённые зависимости. Если применимый критерий или evidence отсутствует, independence имеет состояние `UNVERIFIED`, а решение не становится EXECUTABLE. Числовые пороги эта спецификация не выдумывает.

Ruleset задаёт назначение, срок, ротацию, отвод, substitute и fallback. Отсутствие holder переводит дело в `RESOLUTION_BLOCKED` и safe interim state, а не отдаёт решение инициатору.

## 9. Causal-lineage и anti-circumvention

Перед `AUTHORIZED`, `REVALIDATED` и `EXECUTABLE` проверяются вся цепочка и совокупный эффект: смена holder/competence/reviewer/ruleset, снижение защиты, экономический эквивалент запрещённого права, совокупный контроль, связанная поправка плюс выгода и заранее согласованные промежуточные действия.

Запрещённый совокупный результат отклоняется либо наследует наиболее строгий protection class.

После challenge tainted status следует за объектом, производными требованиями, обеспечением и преобразованиями. Передача не очищает provenance.

## 10. Вход нового участника

### Admission lifecycle

`APPLIED → ELIGIBILITY_VALIDATED → PROVISIONALLY_ADMITTED → FINAL_ADMITTED → MEMBERSHIP_ACTIVE`

До final admission допустимы `REJECTED → CHALLENGED → UPHELD | PROVISIONALLY_ADMITTED` и `ACTIVATION_DELAYED → ESCALATED`.

После `FINAL_ADMITTED` допустим только переход в `MEMBERSHIP_ACTIVE`. Отмена окончательного допуска возможна исключительно через отдельный `MEMBERSHIP_REVOCATION` process с basis, competence, challenge и remedy, а не через административную задержку.

Вступление не создаёт ретроактивное личное требование на накопленный reserve. Договор не может создать CLAIM, обеспечение, опцион или поток, экономически эквивалентный запрещённой доле protected reserve.

## 11. Защищённый резерв и будущий интерес

Protected reserve сохраняет наиболее строгую защиту provenance. Classification transition не слабее последующего действия и требует exact basis, независимого review, future-impact gate, aggregate-lineage check и challenge.

`FUTURE IMPACT REVIEW` имеет `PASS/FAIL/UNRESOLVED`. `FAIL` блокирует execution; `UNRESOLVED` даёт `SUSPENDED` либо `UNRESOLVED_WITH_RESTRICTIONS`, но не согласие.

Межпоколенческая защита входит в `ENTRENCHED_ROOT` через неделимость общественного капитала, provenance protection и запрет автоматического разрешения при отсутствии review.

## 12. Blocked states и ruleset conflict

### Общий fallback

`CHALLENGED/SUSPENDED → RESOLUTION_BLOCKED → REVIEW_CASE.OPENED → ASSIGNED | VACANT → SUBSTITUTION_OR_ESCALATION → RESOLVED | UNRESOLVED_WITH_RESTRICTIONS`.

`REMEDY_BLOCKED` сохраняет tainted object и safe restrictions до исполнения remedy либо отдельного решения о невозможности полного восстановления и residual harm.

### RULESET conflict

`RULESET_CONFLICT_BLOCKED → REVIEW_CASE.OPENED` с унаследованными safe restrictions затронутых объектов. Далее применяется общий lifecycle vacancy/deadlock/substitution/escalation. Верхний уровень не получает остаточную компетенцию.

### Terminal-safe exception

Только явно названные состояния `META_AMENDMENT_BLOCKED_MISSING_RULE`, `OUTSIDE_CURRENT_CONSTITUTIONAL_LINEAGE` и `RE_FOUNDING_NOT_DEFINED` являются безопасно терминальными для предложения: они сохраняют действующее состояние и не требуют искусственного разрешения внутри системы, не способной легитимно его дать.

## 13. Общий reopening-контракт

Terminal state `RIGHT`, `BASIS`, `COMPETENCE`, `RULESET` или `STATE TRANSITION` не переписывается. Reopening создаёт `REOPEN_CASE` и новую review lineage.

Основания: новое доказательство мошенничества, скрытый конфликт, ошибка идентичности, несовпадение execution с authorization, нарушение `ENTRENCHED_ROOT`, доказанная ошибка terminal classification.

Путь:

`TERMINAL_OBJECT → REOPEN_REQUESTED → ELIGIBILITY_VALIDATED → REVIEW_CASE.OPENED → UPHELD_TERMINAL | CORRECTIVE_TRANSITION_REQUIRED`.

До решения действуют scoped safe restrictions, соразмерные риску. Corrective transition создаёт новую версию/состояние и сохраняет terminal record. Reopening не восстанавливает просроченную competence задним числом и не легализует уже недопустимое действие.

## 14. Revalidation перед execution

Проверяются: фактический pre-state, exact effective ruleset, ACTIVE competence, approvals, challenge barrier, tainted parents, новое evidence, immutable/revalidated critical inputs, payload equality и aggregate causal effect.

Провал даёт `REVALIDATION_FAILED → SUSPENDED | MODIFIED_FOR_REVALIDATION`. Ни один путь после challenge не минует revalidation.

## 15. Полная transition matrix как отдельный gate

Текущие таблицы и lifecycles являются архитектурной спецификацией, но не validator contract. До реализации требуется отдельная полная машинная матрица для `RIGHT/BASIS/COMPETENCE/RULESET/STATE_TRANSITION/REVIEW_CASE`:

`from_state → event → competence → guards → to_state → failure_state → propagation_effect`.

Если для любого состояния отсутствует допустимый исход, terminal-safe declaration или fallback, schema gate не проходит.

## 16. Граница WBN/WBNP

Модель задаёт требования к реестру, но не эмиссию, цену, распределение или политические права WBN/WBNP. Монета, токен, членство, голос, CLAIM, RESERVE, COMPETENCE и природное право остаются разными объектами.

Владение WBN/WBNP не создаёт членство, голос, компетенцию или долю неделимого капитала без отдельного допустимого RIGHT и BASIS.

## 17. Матрица закрытия повторного review

| Finding | Исправление v0.3 |
|---|---|
| C1 | `ENTRENCHED_ROOT`; попытка изменения выводится в новую re-founding lineage |
| C2 | полный RIGHT lifecycle и propagation table |
| S1 | любой положительный RESOLVED проходит REVALIDATION_REQUIRED/REVALIDATED |
| S2 | `CASE_RECUSAL` отделён от глобального state COMPETENCE |
| S3 | missing-rule определён как terminal-safe, указаны допустимые выходы |
| S4 | `RULESET_CONFLICT_BLOCKED → REVIEW_CASE.OPENED` и общий fallback |
| S5 | `PROVISIONALLY_ADMITTED` и `FINAL_ADMITTED`; после final только activation или отдельная revocation |
| S6 | `VOID_EXECUTED_EFFECT` — event, переводящий transition в `VOIDED` |
| S7 | общий reopening contract для всех terminal objects |
| E1 | downgrade требует exact clause, compatibility с entrenched root, evidence и review |
| E2 | control/affiliation привязан к ruleset criteria/evidence; unknown fails closed |
| E3 | RULESET_ACTIVATION event и challenge на границе effective_from |
| E4 | полная transition matrix выделена обязательным pre-validator gate |

Матрица показывает наличие ответа, но не заменяет независимую проверку его достаточности.

## 18. Критерии ограниченного re-review

1. Может ли `ENTRENCHED_ROOT` быть ослаблен внутри текущей lineage прямым или составным путём?
2. Отличён ли re-founding от поправки и не переносит ли он права/резерв автоматически?
3. Замкнуты ли ACTIVE, suspension, challenge, transfer, termination и remedy для RIGHT?
4. Однозначно ли влияние BASIS/COMPETENCE/RULESET/REMEDY на RIGHT?
5. Может ли любой положительный challenge result миновать revalidation?
6. Не отключает ли case recusal компетенцию глобально?
7. Имеют ли blocked states fallback либо terminal-safe declaration?
8. Может ли окончательно допущенный участник быть отвергнут административной задержкой?
9. Однозначна ли связь VOID event/state?
10. Работает ли reopening одинаково для всех terminal object types?

## Статус

specification_status: candidate_v0_3_pending_bounded_independent_re_review
previous_review_status: candidate_v0_2_re_reviewed__critical_root_and_right_lifecycle_gaps
critical_findings_addressed_in_text: C1_C2
other_findings_addressed_in_text: S1-S7_E1-E4
validator_contract: not_created_pending_full_transition_matrix
wbn_wbnp_bridge: registry_requirements_only
production_authority: none

---

КТО: VOL / ВОЛОНТЁР
КОГДА: метка времени не ставилась; доверенный проектный источник времени не использовался
ДЛЯ ЧЕГО: закрыть оставшиеся критические пробелы root protection и RIGHT lifecycle и вернуть v0.3 на ограниченный независимый re-review
СТАТУС: candidate_v0_3_pending_bounded_independent_re_review
