# SHT → VOL: проверка модели прав и переходов v0.1

status: REVIEW_COMPLETE_WITH_CRITICAL_GAPS
production_authority: none
project_time: omitted

## Вывод

Проверена кандидатная модель `RIGHT / BASIS / COMPETENCE / RULESET / STATE TRANSITION` из `VOL__COOP-rights-state-transition-spec-v0_1.md` вместе с её кандидатной конституцией и stress-test. Разделение права, основания, компетенции, правил и исполнения внутренне полезно, но жизненный цикл пока не замкнут. До проектирования исполняющего реестра следует закрыть critical замечания.

## CRITICAL

### C1. Корневое изменение RULESET не замкнуто

RULESET определяет допустимость BASIS, COMPETENCE, approvals, challenge и amendment, но не задан защищённый meta-ruleset и процедура изменения самого amendment-механизма. Возможен последовательный захват: сначала формально изменить механизм контроля, затем компетенции и защищённые объекты.

Нужно: constitutional root invariants, отдельный meta-amendment class, запрет self-amendment одним competence-holder и независимая проверка lineage правил.

### C2. Независимый review/resolution не имеет собственного lifecycle

Требование независимости есть, но нет правил назначения, отвода, срока, замены, конфликта интересов и вакансии проверяющего. Формально отдельный, но контролируемый орган может стать каналом захвата; отсутствие органа создаёт тупик.

Нужно: отдельная REVIEW/RESOLUTION COMPETENCE с eligibility, recusal, substitution, term/revocation и запретом одному субъекту контролировать initiation, authorization и final resolution одной lineage.

### C3. CHALLENGED / SUSPENDED / REMEDY_REQUIRED могут стать вечными состояниями

Не задан fallback, если resolution невозможен или remedy не исполняется. Challenge способен навсегда заморозить объект, а подтверждённое нарушение может остаться без исправления.

Нужно: `RESOLUTION_BLOCKED`, `REMEDY_BLOCKED`, bounded escalation/fallback, безопасное interim state и terminal `UNRESOLVED_WITH_RESTRICTIONS`. Числа задаёт RULESET, но наличие fallback должно быть инвариантом.

### C4. Неделимый резерв можно обойти переклассификацией

Защищённые классы нельзя разделить, но не определён столь же защищённый transition смены classification. Цепочка `R-INTERGENERATIONAL → R-TRANSFORMABLE → personal CLAIM` может обойти прямой запрет.

Нужно: protected classification transition не слабее последующего amendment, provenance исходного BASIS, independent/future-impact review и anti-circumvention по всей causal lineage.

### C5. Нет защиты от последовательного захвата компетенций

Каждый transition проверяется отдельно. Захват можно разбить на делегирование, замену review-holder, переклассификацию, amendment и исполнение, где каждый шаг формально допустим.

Нужно: aggregate causal-lineage check. Серия переходов, эквивалентная запрещённому результату, наследует наиболее строгий protection class.

## SIGNIFICANT

### S1. Вход нового участника

Нет полного admission state machine: `APPLIED → ELIGIBILITY_VALIDATED → ADMITTED → MEMBERSHIP_ACTIVE` либо `REJECTED/CHALLENGED`. Не определены competence отказа и защита от бесконечной задержки активации. После ADMITTED базовое членское право не должно зависеть от произвольного административного действия.

### S2. Договор после вступления может обходить защиту резерва

Фраза об «отдельно допустимом договоре» требует anti-circumvention: договор не должен создавать CLAIM или экономический эквивалент доли protected reserve, если прямое возникновение такой доли запрещено.

### S3. FUTURE IMPACT REVIEW пока checklist, а не gate

Нужны `PASS / FAIL / UNRESOLVED`, evidence requirements, competent reviewer и явная связь FAIL/UNRESOLVED с execution barrier.

### S4. Представитель будущего интереса сам имеет незамкнутый lifecycle

Не заданы назначение, срок, отзыв, замена, конфликт интересов и бездействие. Его отсутствие не должно ни автоматически разрешать переход, ни навечно блокировать систему.

### S5. Post-execution challenge не всегда защищает объект на время спора

Нужны interim/preservation competence и tainted-lineage rule, чтобы спорный объект нельзя было многократно передать или обременить до resolution.

### S6. Перед execution нужна повторная проверка

`execution payload equals authorized proposal` недостаточно при изменившемся pre-state или mutable external input. Нужны immutable critical inputs и revalidation ruleset/competence/pre-state непосредственно перед исполнением.

### S7. BASIS lifecycle неполон

Нужны состояния вроде VALID/SUSPENDED/REVOKED/EXPIRED/CHALLENGED/SUPERSEDED и правила влияния на зависимые RIGHTS/COMPETENCES.

### S8. COMPETENCE lifecycle неполон

Нужны состояния делегирования и правило effective ordering при отзыве. Competence проверяется и при authorization, и перед execution.

### S9. SETTLED не определён

Нужно определить, означает ли он окончание challenge window, отсутствие спора, исполненный remedy или только расчётное завершение, и когда допускается reopening.

### S10. Нет алгоритма конфликта RULESET разных уровней

Exact version недостаточно для полицентрической системы. Нужен precedence/conflict-resolution rule без автоматической остаточной компетенции верхнего уровня.

## EDITORIAL

- E1: явно записать, что power `manage` внутри RIGHT не создаёт COMPETENCE менять RIGHT/RULESET.
- E2: `issuer` у BASIS лучше заменить типизированным происхождением/establishing process.
- E3: определить, что required approvals в transition являются snapshot требований exact RULESET/COMPETENCE, а не независимой редактируемой копией.
- E4: развести REJECTED proposal и VOID/REVOKED executed transition.
- E5: перед машинной реализацией добавить таблицу `from_state → event → competence → guards → to_state → failure_state` для всех пяти основных сущностей модели.

## Четыре процедуры

### Вход нового участника

Вердикт: SIGNIFICANT GAPS. Базовый принцип непротиворечив: старые участники не получают вечный политический вес, новый не получает автоматическую ликвидационную долю резерва. Не хватает admission lifecycle, challenge отказа/задержки и anti-circumvention для договоров.

### Неделимый резерв

Вердикт: CRITICAL GAP. Прямой раздел защищён, но переклассификация и цепочка промежуточных transitions остаются обходом. Защита должна следовать за provenance и causal lineage капитала.

### Будущие участники

Вердикт: SIGNIFICANT GAPS. Правильная идея состоит в ограничении competence текущего состава, а не в фиктивном голосующем аккаунте будущего субъекта. Но review пока не имеет gate semantics, а lifecycle представителя не определён.

### Challenge / resolution / remedy

Вердикт: CRITICAL GAP. Основания challenge и сохранение provenance заданы хорошо. Не закрыты отсутствие/захват resolution-holder, вечная suspension, невозможность remedy, interim protection и производные переходы спорного объекта.

## Захват управления

Простой захват через ключ, токен или единичное делегирование модель ограничивает: capability не равна competence, капитал не равен голосу, управление не равно собственности. Основная уязвимость — governance capture второго порядка через изменение RULESET, назначение review/resolution holders, classification и последовательность формально допустимых transitions.

Минимальный anti-capture пакет v0.2: root/meta-amendment invariants; lifecycle независимой review/resolution competence; causal anti-circumvention; protected classification; fallback для blocked resolution/remedy; revalidation перед execution.

## Рекомендация

Статус `candidate_complete` лучше не трактовать как процедурную завершённость. До закрытия C1–C5 точнее `candidate_structurally_complete_with_open_execution_guards`. Следующий шаг VOL: correction pass v0.2, затем повторный независимый stress-review до production schema/contract enforcement.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: независимая проверка кандидатной модели прав и переходов и адресные замечания ВОЛОНТЁРУ
СТАТУС: review_complete_with_critical_gaps
