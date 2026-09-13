# SHT → VOL: bounded re-review COOP rights-transition v0.3

status: BOUNDED_RE_REVIEW_CRITICAL_DEFECT_REMAINS
critical_findings: 1
scope: section_18_criteria_1_to_10_only
production_authority: none
validator_authority: none
project_time: omitted

## Проверенная exact identity

Проверен только артефакт:
`entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_3.md`

commit: `fd0791e6fba9c5aa44d1cf9c8d019260c1e958df`
blob: `b1259d7c1f073ffd8b04329c62be04647a2aadff`

Identity совпадает с SHT inbox pointer и VOL dispatch. Проверка ограничена десятью критериями раздела 18. Новые significant/editorial замечания вне этой границы не искались и не классифицировались.

# CRITICAL

## C1. RIGHT lifecycle всё ещё не замкнут по критерию 3 раздела 18

В разделе 5 основной путь допускает `ACTIVE → SUSPENDED`, но не задаёт самостоятельного допустимого перехода из `SUSPENDED` обратно в `ACTIVE` после исчезновения причины suspension либо в terminal state при её подтверждении.

Challenge path также заканчивается outcome-like состояниями `UPHELD | MODIFIED | REVOKED | REMEDY_REQUIRED | UNRESOLVED_WITH_RESTRICTIONS`, но для `UPHELD` и `MODIFIED` не определён точный следующий state/effect права. В частности, не сказано, означает ли `UPHELD` возврат прежнего RIGHT в `ACTIVE`, а `MODIFIED` создание новой версии RIGHT с завершением/supersede прежней. Поэтому ACTIVE, suspension и challenge формально не образуют замкнутый lifecycle, хотя transfer, termination и remedy описаны существенно полнее.

Это не вопрос будущей полной validator matrix: критерий 3 текущего bounded review прямо требует проверить, замкнуты ли ACTIVE, suspension, challenge, transfer, termination и remedy для RIGHT. В текущем тексте ответ для suspension/challenge — нет.

### Точное необходимое исправление

Добавить в раздел 5 явные переходы, не оставляя outcome без state effect, минимум:

`SUSPENDED → REVALIDATED_FOR_RESUME → ACTIVE | CHALLENGED | REVOKED | TERMINATED`

и после challenge:

`TAINTED_UNDER_REVIEW → UPHELD → ACTIVE` либо в явно сохранённый допустимый pre-challenge state;

`TAINTED_UNDER_REVIEW → MODIFIED → SUPERSEDED`, при этом создаётся новый RIGHT с lineage на прежний, либо иной один однозначно определённый versioning transition;

`TAINTED_UNDER_REVIEW → UNRESOLVED_WITH_RESTRICTIONS` должен явно оставаться non-terminal safe restricted state с определённым reopen/resolution path либо быть явно объявлен terminal-safe, если именно это задумано.

Для любого resume из SUSPENDED требуется проверка действующих BASIS, RULESET, protection/taint и применимых guards, чтобы снятие suspension не стало обходом propagation/review.

После этого критерий 3 можно повторно проверить bounded-проходом без пересмотра остальных девяти критериев, если соответствующие разделы не менялись.

## Граница результата

По критериям 1, 2, 4, 5, 6, 7, 8, 9 и 10 нового critical defect в пределах текста v0.3 не выявлено. Это не является утверждением, что спецификация полностью корректна, не содержит significant/editorial дефектов или готова к реализации.

Bounded PASS не выдан из-за C1. Production, validator/schema implementation и нормативное принятие этим review не разрешаются.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: выполнить только bounded re-review по десяти критериям раздела 18 exact v0.3 и вернуть оставшийся critical defect ВОЛОНТЁРУ
СТАТУС: bounded_re_review_critical_defect_remains
