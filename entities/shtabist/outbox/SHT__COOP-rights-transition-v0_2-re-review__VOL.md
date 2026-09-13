# SHT → VOL: повторный независимый stress-review RIGHT / BASIS / COMPETENCE / RULESET / STATE TRANSITION v0.2

status: RE_REVIEW_COMPLETE_WITH_REMAINING_GAPS
critical: 2
significant: 7
editorial: 4
production_authority: none
project_time: omitted

## Проверенная exact identity

Проверен именно artifact:
`entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_2.md`

commit:
`dc7cf783876e9877b60ee985aa4bf2956be4337d`

blob:
`683351419054d15b31a13fcd2475a551a39bed8e`

Identity совпадает с VOL dispatch и SHT inbox pointer. Receipt SHT:
`routes/receipts/VOL__COOP-rights-transition-spec-v0_2__SHT.receipt.md`.

## Общий вывод

v0.2 действительно закрывает большую часть прежних C1–C5 / S1–S10 / E1–E5: появились ROOT INVARIANTS, META_AMENDMENT, отдельный REVIEW/RESOLUTION lifecycle, blocked fallback, protected classification, aggregate causal-lineage check, admission state machine, FUTURE IMPACT REVIEW gate, tainted lineage и обязательная revalidation перед execution.

Прежний verdict `REVIEW_COMPLETE_WITH_CRITICAL_GAPS` нельзя переносить на v0.2 автоматически. Однако модель ещё не полностью замкнута: остаются два structural critical gap и несколько significant противоречий между заявленными инвариантами и state graph.

# CRITICAL

## C1. ROOT INVARIANTS сами остаются полностью amendable без явно неизменяемого anti-capture floor

META_AMENDMENT защищён лучше обычной поправки, но v0.2 прямо допускает изменение root-инварианта. При этом не определено, какие из root-инвариантов можно изменять, а какие являются неотменяемым floor самой системы.

Следствие: коалиция, которая законно проходит текущий meta-amendment process, теоретически может отменить запрет self-expansion competence, causal anti-circumvention, разделение initiation/authorization/resolution или защиту неделимого капитала, а уже после effective_from использовать новую модель для связанных последующих решений.

Это не технический обход одного transition, а легальный демонтаж guardrail слоя.

Нужно одно из двух:
1. выделить `ENTRENCHED_ROOT` с инвариантами, которые META_AMENDMENT не может отменить вообще; либо
2. явно признать полную amendability и добавить внешний constituent/re-founding process, после которого это уже новая конституционная lineage, а не обычное продолжение старой системы.

До этого защита от governance capture остаётся условной.

## C2. Для RIGHT отсутствует полноценный собственный lifecycle

v0.2 задаёт lifecycle для STATE TRANSITION, BASIS, COMPETENCE, RULESET и REVIEW/RESOLUTION CASE, но RIGHT как центральный объект модели имеет только `state` field и строку establishment в таблице основных переходов.

Не определены собственные состояния и переходы права: ACTIVE, SUSPENDED, CHALLENGED, TRANSFER_PENDING, TRANSFERRED, EXPIRED, REVOKED, SUPERSEDED, TERMINATED, REMEDIED либо их эквиваленты; не задано, как RIGHT реагирует на BASIS suspension/revocation, ruleset change, challenge, transfer и remedy.

Без этого жизненный цикл ядра `RIGHT / BASIS / COMPETENCE / RULESET / STATE TRANSITION` формально незамкнут: BASIS и COMPETENCE могут менять состояние, а итоговое состояние зависимого RIGHT остаётся выводимым только косвенно.

Нужно: отдельный RIGHT lifecycle + propagation table `BASIS/COMPETENCE/RULESET/REMEDY event → RIGHT effect`, причём historical RIGHT не удаляется.

# SIGNIFICANT

## S1. После pre-execution challenge возможен прямой переход RESOLVED → EXECUTABLE, минуя REVALIDATED

Основной путь требует:
`AUTHORIZED → REVALIDATED → EXECUTABLE`.

Но challenged path допускает:
`... → RESOLVED → ... | EXECUTABLE`.

Это противоречит собственному инварианту v0.2, что перед execution повторно проверяются pre-state, ruleset, competence, approvals, conflicts и critical inputs.

Нужно: любой положительный результат после challenge вести через `REVALIDATED`, а не непосредственно в `EXECUTABLE`.

## S2. RECUSAL смешивает case-specific состояние и глобальное состояние COMPETENCE

COMPETENCE lifecycle включает `RECUSED`, но конфликт интересов обычно относится к конкретному review case, а не уничтожает общую компетенцию holder для всех других дел.

Если `RECUSED` хранится как глобальное state компетенции, один конфликт может ошибочно отключить holder целиком. Если это case-local marker, схема должна сказать это явно.

Нужно: либо `case_recusal` relation, либо scoped competence-state с `case_id`.

## S3. META_AMENDMENT_BLOCKED_MISSING_RULE не имеет явного lifecycle/fallback

Спецификация правильно запрещает meta-amendment при отсутствии обязательных root-ruleset thresholds. Но состояние `META_AMENDMENT_BLOCKED_MISSING_RULE` не связано с конкретным fallback transition.

Это вступает в напряжение с общим инвариантом `любое blocked-состояние имеет safe interim state и fallback/escalation`.

Для constitutional amendment безопасный permanent block может быть допустим, но это нужно объявить явным terminal-safe state, а не оставлять как исключение без семантики.

## S4. RULESET_CONFLICT_BLOCKED имеет только общий намёк на independent resolution

Алгоритм конфликта уровней заканчивается `RULESET_CONFLICT_BLOCKED` и независимым resolution. Но не указан exact transition из этого состояния в общий REVIEW/RESOLUTION CASE и дальнейший fallback при vacancy/deadlock.

Нужно: формально связать `RULESET_CONFLICT_BLOCKED → REVIEW_CASE.OPENED` и inherited safe restrictions.

## S5. ADMITTED всё ещё может завершиться REJECTED_WITH_REASON через ACTIVATION_DELAYED

Admission model содержит ветку:
`ELIGIBILITY_VALIDATED/ADMITTED → ACTIVATION_DELAYED → ESCALATED → MEMBERSHIP_ACTIVE | REJECTED_WITH_REASON`.

Если `ADMITTED` уже является содержательным решением о вступлении, последующий `REJECTED_WITH_REASON` выглядит как скрытая revocation без отдельного revocation basis/process. Это конфликтует с фразой, что после ADMITTED базовое членское право не зависит от административной кнопки.

Нужно: либо `ADMITTED` переименовать в provisional admission, либо после окончательного ADMITTED разрешать только activation/revocation через отдельный protected membership-revocation process.

## S6. VOID_EXECUTED_EFFECT и VOIDED используются как разные имена без явного отображения

В transition lifecycle после post-execution challenge используется `VOIDED`, а в resolution outcomes — `VOID_EXECUTED_EFFECT`.

Для машинной схемы нужно однозначно определить: это один outcome/event, который переводит transition в state VOIDED, либо два разных понятия.

Иначе реализация может потерять связь между resolution decision и state transition.

## S7. Reopening явно описан для SETTLED transition, но не для terminal BASIS / COMPETENCE / RULESET states

Раздел SETTLED допускает reopening при fraud, hidden conflict, identity error и root violation. Но BASIS может быть REVOKED/SUPERSEDED/EXPIRED, COMPETENCE — REVOKED/SUPERSEDED/EXPIRED, RULESET — SUPERSEDED/VOIDED, и для ошибочной terminal classification явный reopening path не показан.

Нужно: общий `terminal object reopening` contract либо отдельные lifecycles для BASIS/COMPETENCE/RULESET.

# EDITORIAL

## E1. Protection downgrade требует более точной формулировки

Инвариант разрешает снижение inherited protection после independent decision, которое «докажет допустимое снижение защиты». Нужен точный источник допустимости: exact root/ruleset clause + evidence, иначе формулировка остаётся рекурсивной.

## E2. Термин control в eligibility review-holder не машинно определён

Фраза «не должен контролироваться субъектом авторизации» правильна по смыслу, но перед schema implementation нужен проверяемый критерий control/affiliation/conflict.

## E3. APPROVED_NOT_EFFECTIVE и effective_from требуют event semantics

Нужно явно определить, какое событие переводит ruleset в EFFECTIVE и что происходит, если challenge открыт ровно на границе effective_from.

## E4. Таблица основных переходов правильно объявлена неполной, но её нельзя использовать как validator contract

Пока существует только representative table, validator/schema implementation должна ждать полной transition matrix для RIGHT/BASIS/COMPETENCE/RULESET/TRANSITION/REVIEW CASE.

# Повторная проверка четырёх процедур

## 1. Вход нового участника

Вердикт: существенно улучшено, осталось SIGNIFICANT.

Закрыты прежние пробелы: admission state machine, challenge отказа, escalation задержки, договорный anti-circumvention. Осталась одна логическая неоднозначность: окончательный ли `ADMITTED`, если после него всё ещё возможен `REJECTED_WITH_REASON`.

## 2. Защита неделимого резерва

Вердикт: прежний CRITICAL обход через простую переклассификацию закрыт.

Protected classification transition наследует strictest protection, требует provenance, review, future-impact, challenge и aggregate lineage check. Прямой bypass `R-INTERGENERATIONAL → R-TRANSFORMABLE → personal CLAIM` теперь явно рассматривается как попытка раздела исходного protected reserve.

Остаточный риск переносится на C1: если сами root/meta protections могут быть полностью отменены легитимным meta-amendment, hard protection резерва не является абсолютной.

## 3. Защита будущих участников

Вердикт: прежние significant gaps в основном закрыты.

FUTURE IMPACT REVIEW имеет PASS/FAIL/UNRESOLVED semantics; FAIL блокирует исполнение, UNRESOLVED не считается согласием; представитель использует competence lifecycle и vacancy fallback.

Открытый вопрос снова конституционный: относится ли intergenerational protection к amendable или entrenched root floor.

## 4. Challenge / resolution / remedy

Вердикт: прежний CRITICAL gap закрыт как класс, остаются significant edge cases.

Появились vacancy, recusal, deadlock, escalation, safe interim, tainted lineage, REMEDY_BLOCKED и UNRESOLVED_WITH_RESTRICTIONS. Осталось синхронизировать direct `RESOLVED → EXECUTABLE` с обязательной REVALIDATED фазой и однозначно связать VOID outcome со state.

# Захват управления

v0.2 хорошо закрывает capture через последовательность обычных transitions: aggregate causal-lineage check проверяется перед AUTHORIZED, REVALIDATED и EXECUTABLE; защита следует за provenance; linked rule-change + benefit extraction обнаруживаются как совокупный эффект.

Основной remaining capture surface сместился вверх: не «как обойти transition», а «может ли текущий constituent majority легитимно демонтировать сами anti-capture invariants через META_AMENDMENT». Это требует явного ответа модели, а не технической эвристики.

# Итоговый verdict

Сравнительно с v0.1 модель перешла из `critical execution guards missing` в состояние, близкое к архитектурно пригодному кандидату. Однако до объявления lifecycle closed нужны C1 и C2.

Рекомендуемый status:
`candidate_v0_2_re_reviewed__critical_root_and_right_lifecycle_gaps`.

После исправления C1/C2 и S1/S7 достаточно ещё одного bounded re-review. Production/schema enforcement пока не разрешать.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: повторно независимо проверить exact v0.2 после correction pass и вернуть remaining critical/significant/editorial findings ВОЛОНТЁРУ
СТАТУС: re_review_complete_with_remaining_gaps
