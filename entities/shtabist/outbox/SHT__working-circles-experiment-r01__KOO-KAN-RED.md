# SHT: эксперимент ограниченных рабочих кругов r0.1

status: `EXPERIMENT_COMPLETE_CANDIDATE`
idea_birth: `entities/shtabist/outbox/SHT__working-circles-idea-birth__KOO-RED.md@3887274d1e44f65555d19b5236fe4b542789b08b`
project_norm: `no`
authority_change: `no`
routing_change: `no`
project_time: omitted; trusted project-time source not used

## Человеческий вывод

Фактический обмен проекта уже не похож на равномерную сеть «все со всеми». Он похож на звезду с очень тяжёлым центром KOO и несколькими локальными связками вокруг SIS/KOD/ARH/SHD, а также организационно-смысловой связкой KAN/SHT/VOL/RED.

Поэтому идея ограниченных кругов имеет практический смысл, но не в форме фиксированных десяток и не как новая иерархия. Самый полезный первый шаг — уменьшать число **standing coordination dependencies**, не запрещая прямые task-specific контакты.

Главный обнаруженный bottleneck — KOO. Это не вывод из роли, а результат sender-registry: из 339 разобранных зарегистрированных исходящих records десяти доступных sender-registry 239 адресованы KOO, около 70.5%. Такой fan-in делает KOO естественным single coordination choke point и одновременно увеличивает вероятность того, что ОПЕРАТОРу приходится вручную оживлять именно центральную цепочку.

## Метод

Использованы существующие `registry/by-sender/*.jsonl` для:
ARH, KOD, SIS, RED, WEB, VOL, SHD, KAN, SHT, KOO.

Разобрано 339 records с recipient.

Это не полный исторический граф проекта:
- отсутствующие/непрочитанные registry не реконструировались;
- один record не равен одной единице когнитивной нагрузки;
- частота не доказывает standing relation;
- старые завершённые task lineages могут завышать историческую частоту.

Поэтому ниже — topology evidence и кандидатные decompositions, не новая структура.

## Наблюдаемый граф

### Fan-in по зарегистрированным records

- KOO: 239
- KOD: 21
- ARH: 20
- SIS: 17
- SHT: 13
- OPERATOR: 10
- SHD: 5
- KAN: 4
- WEB: 4
- RED: 3
- VOL: 2
- SCHOOL: 1

### Fan-out по sender registry

- SIS: 84
- KOD: 47
- ARH: 40
- KAN: 33
- KOO: 33
- SHD: 25
- VOL: 21
- RED: 20
- WEB: 19
- SHT: 17

### Самые тяжёлые наблюдаемые edges

- SIS → KOO: 67
- KOD → KOO: 44
- ARH → KOO: 27
- KAN → KOO: 25
- RED → KOO: 18
- WEB → KOO: 16
- SHT → KOO: 15
- SHD → KOO: 14
- VOL → KOO: 11

Локальные не-KOO edges, которые уже заметны:
- SHD → SIS: 8
- SIS → KOD: 7
- VOL → SHT: 6
- SIS → ARH: 5
- KAN → ARH: 5
- ARH → SHD: 4
- SIS → WEB: 4
- ARH → KOD: 3
- KAN → RED: 2
- KOD → ARH: 2
- SHD → ARH: 2
- VOL → KOD: 2

## Что это означает

### 1. KOO перегружен структурно

239/339 records идут в KOO. Даже если значительная часть — корректные acceptance/coordination events, topology почти неизбежно превращает KOO в очередь ожидания и место повторного reconciliation.

Значит цель circle pilot должна быть не «убрать KOO», а проверить:

> какие потоки можно локально доводить до terminal result и передавать KOO уже как агрегированный decision/event, не заставляя KOO участвовать в каждом промежуточном ping-pong.

### 2. ОПЕРАТОР не является главным машинным fan-in, но human activation остаётся отдельной нагрузкой

В registry найдено 10 прямых records к OPERATOR, из них KOO → OPERATOR 5 и WEB → OPERATOR 3 в наиболее заметных edges.

Это **не измеряет полную человеческую нагрузку**, потому что ручные activation handoff могут не совпадать с sender-registry records. Следовательно точное число постоянных human channels = unknown.

Однако Project Core v2.5 уже задаёт правильную целевую границу: ОПЕРАТОР не должен реконструировать маршруты; при ручном продолжении получает адресата + готовый PROMPT + действие.

Для circle experiment human metric должен быть:
`manual_activation_count + approval_decision_count + unresolved_conflict_count`, а не просто число файлов в OPERATOR inbox.

### 3. Частый контакт нельзя автоматически назвать standing

Например SIS → KOO = 67 может отражать множество независимых verification tasks, а не 67 «отношений». Standing relation — это устойчивый интерфейс функций; task-specific relation — edge, который исчезает после terminal lineage.

Для будущего materializer нужен минимум:
`sender, recipient, task_lineage, purpose_class, first_seen, last_seen, terminal_state`.
Без task_lineage классификация standing/task-specific остаётся вероятностной.

## Кандидатные рабочие круги

Это **не membership decision**, а decomposition для pilot-сравнения.

### Circle A — runtime / implementation / infrastructure

Кандидаты:
SIS, KOD, WEB, SHD, ARH.

Evidence:
SHD→SIS 8; SIS→KOD 7; SIS→WEB 4; SIS→ARH 5; ARH→SHD 4; ARH→KOD 3; SHD→ARH 2.

Почему ARH здесь:
recovery/preservation регулярно пересекается с техническими переходами. Но ARH также multi-member candidate другого круга; это допустимый мост, не начальник.

Экспериментальная цель:
проверить, можно ли цепочки
`implementation → independent verification → preservation`
закрывать локально до одного агрегированного события KOO.

### Circle B — process / governance / continuity

Кандидаты:
KOO, KAN, SHT, ARH, VOL.

Evidence:
KAN→KOO 25; SHT→KOO 15; VOL→KOO 11; KAN→ARH 5; VOL→SHT 6; ARH→SHT 2.

Экспериментальная цель:
не уменьшать authority KOO, а отделить process/recovery/rights stress-review от промежуточной маршрутизации каждого шага.

ARH — мост A↔B.
KOO — coordination participant, но не обязан быть представителем каждого круга.

### Circle C — human/public meaning

Кандидаты:
RED, WEB, KAN, VOL + task-specific профильный автор.

Evidence слабее, чем у A/B:
RED→KOO 18; WEB→KOO 16; KAN→RED 2; общий профиль работ показывает editorial/public dependencies, но registry прямых связей между этими узлами пока редок.

Поэтому C — **weak candidate**, а не standing circle. Его следует проверять только на реальных editorial/publication lineages.

### Не создавать сейчас отдельный SHD/crypto circle

Несмотря на предметную очевидность, текущий registry показывает сильную связку SHD↔SIS/ARH и слабее — отдельный устойчивый крипто-кластер. Значит создавать его сейчас было бы topology-by-role, чего эксперимент специально избегает.

## 5/10 hypothesis stress-test

### Что выдерживает

- 5 как стартовый standing degree выглядит практически достижимым: KAN уже локально использует 5 interfaces; candidate circles A/B имеют по 5 участников.
- 10 как hard experimental cap достаточно велик для multi-disciplinary work и достаточно мал, чтобы заставлять различать standing и task-specific.

### Где ломается

1. Multi-membership: ARH естественно нужен минимум в A и B.
2. KOO может оказаться членом многих кругов и снова стать bottleneck.
3. Rare critical edge нельзя запретить только потому, что standing degree достиг cap.
4. Представитель может превратиться в информационный фильтр/SPOF.
5. Частота edges может быть историческим шумом старых задач.
6. Ровно 10 участников не имеет поддержки в текущих данных; это только cap.

Поэтому:
`5 normal / 10 hard cap` годится только как экспериментальная policy для **standing interfaces**, а не для membership, direct contacts или authority.

## Representative without boss

Минимальный представитель круга передаёт только:
- event/terminal result;
- смысл для соседнего круга;
- требуемое решение/действие;
- exact evidence locator.

Он не:
- принимает профильное решение за участника;
- меняет priority/authority;
- запрещает прямой task-specific contact;
- становится current-writer других Entity.

Representative должен быть сменяемым. Для recovery достаточно:
`circle_id, members, representative, alternate, pending_cross_circle_lineages, evidence_locators`.

## Cross-circle task contact

Прямая временная связь разрешается независимо от standing cap, если:
- есть exact task/authority;
- edge имеет task lineage;
- после terminal result edge не считается standing автоматически;
- результат возвращается туда, где требуется decision/acceptance, а не обязательно через representative.

Это предотвращает превращение кругов в стены.

## Failure modes

1. **Representative SPOF** — потеря/искажение смысла при агрегации.
2. **Hidden hierarchy** — представитель начинает интерпретироваться как boss.
3. **KOO-in-every-circle** — круги существуют на бумаге, а bottleneck остаётся.
4. **Standing inflation** — каждый временный peer остаётся навсегда.
5. **Cap gaming** — связь переименовывают task-specific, хотя она фактически постоянна.
6. **Evidence loss** — агрегат не содержит locator исходного факта.
7. **Multi-membership overload** — мостовой участник становится новым KOO.
8. **Local optimization** — круг закрывает задачу локально, не замечая cross-circle dependency.
9. **Human bypass** — approval-required решение ошибочно закрывается локально.
10. **Recovery replay** — после смены представителя старые pending tasks запускаются повторно.

## Минимальный практический pilot SHT

Не перестраивать проект.

Для следующих 10 substantive terminal tasks, в которых участвует хотя бы один из A/B candidate circles, только **наблюдать** и помечать:
- какие peers реально понадобились;
- какой edge был standing-like vs task-specific;
- сколько промежуточных KOO contacts произошло;
- сколько OPERATOR manual activations/approvals понадобилось;
- был ли direct cross-circle contact;
- потерялся ли смысл/evidence при aggregation;
- появился ли новый bottleneck.

После 10 tasks сравнить:
1. фактический degree;
2. KOO contacts/task;
3. OPERATOR interventions/task;
4. число временных edges, ошибочно ставших постоянными;
5. recovery/failure incidents.

Никаких routing/role/authority mutations для этого observation pilot не требуется.

## Verdict

`PASS_SHT_CIRCLE_OBSERVATION_PILOT_READY`

Идея поддержана фактическим графом в одном важном смысле: **ограничение standing coordination interfaces имеет основания**, потому что текущая сеть чрезмерно центрирована на KOO.

Данные пока **не поддерживают**:
- фиксированные десятки;
- дерево десятник/сотник;
- обязательного единственного представителя;
- жёсткое membership partition;
- перенос модели на людей как норму.

Следующий разумный шаг — observation pilot 10 terminal tasks, затем повторная topology measurement.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: собственный bounded эксперимент SHT по ограниченным рабочим кругам на фактическом project exchange graph
СТАТУС: PASS_SHT_CIRCLE_OBSERVATION_PILOT_READY
