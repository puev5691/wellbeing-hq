# Failure cases коллективного субъекта — wave 2 / v0.1

## Назначение

Второй проход проверяет пять узких мест из предыдущей матрицы: псевдоучастие и концентрацию фактической власти; воспроизводство участника через обучение и onboarding; федеративную взаимопомощь после отказа локального узла; масштабирование, при котором ownership и decision rights перестают совпадать; границы входа/членства/выхода.

Этот документ не доказывает универсальную причинность. Он фиксирует наблюдаемые связи, границы утверждений и переменные-кандидаты для будущей модели организационной динамики.

## CASE-04 — Platform cooperatives: формальное право голоса не устраняет participation elite

### Наблюдение

Эмпирическое исследование четырёх итальянских platform worker cooperatives, survey `n=418`, обнаружило неравномерность участия в принятии решений. Участники с меньшей affective commitment и меньшим social capital среди других членов участвовали реже. Авторы прямо выделяют participation elite из более вовлечённых и лучше связанных членов. При этом размер кооператива и human capital в этой выборке эффекта не показали.

Следовательно, наличие общего собрания, `one member / one vote`, онлайн-опросов и формальной доступности процедур ещё не означает равномерного фактического влияния.

### Механизмы

- `M04` участие в изменении правил и решений;
- `M10` обучение/включение участника;
- `M11` членство и фактическая включённость.

### Failure pattern

**Право участия ≠ способность и вероятность им воспользоваться.** Формально демократическая система может устойчиво производить ядро активных участников и периферию номинальных членов.

### Модельный вывод

Недостаточно считать `voting_right=true`. Нужны как минимум:

`participation_rate_by_member`, `participation_concentration`, `decision_influence_concentration`, `member_social_connectivity`, `member_commitment_proxy`, `consultation_to_decision_conversion`.

### Evidence

- *Silicon law of oligarchy: patterns of member participation in the decision-making of platform cooperatives*, Socio-Economic Review 22(3), 1335–1367. Oxford Academic locator: `https://academic.oup.com/ser/article/22/3/1335/7300933`.

Status: `SOURCE_SUPPORTED_PARTICIPATION_CASE`.

## CASE-05 — Cooperative reproduction: onboarding является governance-механизмом, а не кадровой мелочью

### Наблюдение

Современная литература по cooperative governance отдельно выделяет internal worker reproduction: способность привлекать, удерживать и заменять работников/членов, пригодных для participatory culture. В этот контур входят recruitment, hiring, onboarding, education, development, turnover и succession.

Наблюдение поддерживается и эмпирическими описаниями кооперативов Emilia-Romagna: в исследованных организациях высокий уровень участия поддерживается не только формальными органами, но и регулярными каналами двустороннего обмена информацией; в Cefla членам предоставляется обучение, помогающее понимать финансовую отчётность и бюджеты.

Это не доказывает, что обучение автоматически создаёт демократию. Оно показывает более узкую вещь: реальное участие требует компетенции понимать объект решения и воспроизводить практику после смены людей.

### Механизмы

- `M08` институциональная память;
- `M10` обучение как воспроизводимость;
- `M04` содержательное участие в решениях.

### Failure pattern

**Формально равные права при неравной способности понимать и продолжать процесс создают скрытую зависимость от компетентного меньшинства.** Тогда уход носителя знания может разрушить процесс либо усилить управленческую концентрацию.

### Модельный вывод

Кандидатные поля:

`onboarding_completion`, `decision_literacy`, `handover_success`, `successor_independence`, `knowledge_holder_concentration`, `time_to_autonomous_action`, `external_prompt_count_after_handover`.

### Evidence

- McMahon, C.; Novkovic, S. *Humanistic governance in worker cooperatives: Unlocking collective capacities*, Economic and Industrial Democracy, 2026.
- *Cooperative Governance in Context*, Springer chapter, DOI family `10.1007/978-3-031-17403-2`.

Status: `SOURCE_SUPPORTED_REPRODUCTION_CASE`.

## CASE-06 — Fagor after collapse: федерация не спасла локальную организацию, но смягчила потерю участниками функции труда

### Наблюдение

Официальная хронология MONDRAGON фиксирует, что в 2013 году собственные усилия Fagor Electrodomésticos и солидарная поддержка других кооперативов не предотвратили прекращение деятельности. После коллапса были активированы корпоративные механизмы солидарности для решения проблемы примерно 2 000 избыточных рабочих мест.

В записи за 2014 год MONDRAGON сообщает, что благодаря координации кооперативов решение по занятости было найдено для 90% из 1 900 затронутых членов.

Это важное различие уровней результата: федеративная система **не обеспечила survival локального предприятия**, но, по собственным данным MONDRAGON, существенно повысила способность системы перераспределить последствия для членов.

### Механизмы

- `M09` вложенные/федеративные уровни;
- `M05` связь участника с общей ресурсной системой;
- `M08` способность системы продолжить функцию после отказа узла.

### Failure / resilience pattern

**Resilience системы нельзя измерять только выживанием каждого узла.** Иногда локальный failure остаётся failure, но надсистема сохраняет людей, компетенции или функции через relocation/reallocation.

Одновременно это предупреждение против красивой подмены: успешная релокация не превращает банкротство Fagor в успех.

### Модельный вывод

Нужны разные метрики:

`local_node_survival`, `member_function_recovery`, `cross_node_absorption_capacity`, `time_to_relocation`, `federation_support_attempt`, `support_prevented_failure`, `support_mitigated_consequence`.

### Evidence

- MONDRAGON official timeline, 2013: `https://www.mondragon-corporation.com/timeline/2013/`.
- MONDRAGON official timeline, 2014: `https://www.mondragon-corporation.com/en/timeline/2014/`.

Status: `PRIMARY_SOURCE_RESILIENCE_CASE`; 90% figure is MONDRAGON self-report and should retain that provenance.

## CASE-07 — Internationalisation: cooperative ownership at the core can coexist with non-member periphery

### Наблюдение

Longitudinal qualitative case study одной multinational worker cooperative группы MONDRAGON фиксирует противоречия internationalisation: усиление managerial control относительно worker-member participation и создание capitalist subsidiaries, работники которых исключены из ownership и decision-making.

Это прямой boundary case для масштабирования. Организация может сохранять cooperative identity и democratic core, одновременно расширяя деятельность через единицы, где права работников принципиально иные.

### Механизмы

- `M03` распределение полномочий;
- `M04` участие;
- `M05` ownership/result rights;
- `M09` уровни и масштабирование;
- `M11` границы членства.

### Failure pattern

**Масштабирование способно разорвать соответствие `contribution → membership → ownership → decision rights`.** Тогда агрегированная метрика по всей организации скрывает разные режимы субъектности внутри разных узлов.

### Модельный вывод

Нужны node-level attributes, а не только system average:

`node_membership_regime`, `worker_owner_share`, `worker_vote_share`, `subsidiary_governance_type`, `rights_asymmetry_between_nodes`, `core_periphery_gap`.

### Evidence

- Bretos, I. et al. *Ownership, governance, and the diffusion of HRM practices in multinational worker cooperatives: Case-study evidence from the Mondragon group*, Human Resource Management Journal. DOI `10.1111/1748-8583.12165`.

Status: `SOURCE_SUPPORTED_SCALING_BOUNDARY_CASE`.

## CASE-08 — Membership and exit: юридическое членство не гарантирует равенство прав внутри кооператива

### Наблюдение

Исследование farmer cooperatives Zhejiang Province рассматривает democratic decision-making, participation, member exit и profit allocation. Эмпирический результат: ownership rights, decision rights и income rights были существенно смещены к небольшой доле членов; ряд governance practices не соответствовал требованиям закона.

Этот case полезен не как универсальное описание китайских кооперативов, а как демонстрация разрыва между формой членства и фактическим распределением прав.

### Механизмы

- `M04` участие;
- `M05` ownership/income rights;
- `M11` членство и выход.

### Failure pattern

**Граница членства недостаточна без карты прав.** Два формально одинаковых member records могут соответствовать существенно разной способности принимать решения, получать результат и безопасно выйти.

### Модельный вывод

Кандидатные поля:

`member_ownership_right`, `member_decision_right`, `member_income_right`, `rights_concentration`, `exit_rule`, `exit_cost`, `unsettled_obligation_on_exit`, `formal_actual_rights_gap`.

### Evidence

- Liang, Q.; Hendrikse, G.; Huang, Z.; Xu, X. *Governance Structure of Chinese Farmer Cooperatives: Evidence From Zhejiang Province*, Agribusiness 31(2), 198–214. DOI `10.1002/agr.21400`.

Status: `SOURCE_SUPPORTED_RIGHTS_DISTRIBUTION_CASE`.

## Синтез wave 2

После второго прохода становится недостаточно моделировать участника как единицу `member=true/false`.

Рабочая структура усложняется:

`формальное членство → фактические права → способность понимать решение → вероятность участия → реальное влияние → вклад/результат → способность передать функцию → последствия выхода`.

Для федеративного уровня аналогично:

`локальный узел → локальная устойчивость → межузловая помощь → способность поглощать отказ → сохранение участников/функций → здоровье надсистемы`.

Особенно важны три новых различения:

1. `formal right` и `exercised right`;
2. `local survival` и `system resilience`;
3. `membership` и реальный bundle прав `ownership / decision / income / exit`.

## Что теперь должно войти в концепцию движка

К уже выделенным переменным следует добавить четыре группы:

- participation distribution: `participation_concentration`, `decision_influence_concentration`, `consultation_to_decision_conversion`;
- reproduction: `decision_literacy`, `handover_success`, `successor_independence`, `knowledge_holder_concentration`;
- federation resilience: `cross_node_absorption_capacity`, `member_function_recovery`, `support_prevented_failure`, `support_mitigated_consequence`;
- rights topology: `node_membership_regime`, `worker_owner_share`, `rights_asymmetry_between_nodes`, `formal_actual_rights_gap`, `exit_cost`.

Это всё ещё candidate model layer. Поля не становятся валидными метриками только потому, что получили приличные английские имена. Для каждого нужны definition, unit/scale, provenance, falsification case и data availability.

## Следующий цикл

Следующий исследовательский проход должен перестать просто добавлять cases и начать строить **операциональные определения** ключевых переменных. Приоритет: `participation_concentration`, `decision_latency`, `handover_success`, `knowledge_holder_concentration`, `cross_node_absorption_capacity`, `formal_actual_rights_gap`.

Для каждой переменной нужны: наблюдаемый объект; формула/шкала; минимальные события; способ ложного измерения; тест на историческом или проектном case.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: второй evidence-backed проход failure/resilience cases и выделение переменных для модели организационной динамики.
Статус: candidate research artifact; не Project Source и не задание КОДЕРУ.
Время: не указано; разрешённый проверяемый источник проектного времени не использовался.
