# ARH: event-lineage смены модели активации Сущностей

## Назначение

Зафиксировать проверяемую смену причинной модели активации Сущностей, не превращая исследовательские кандидаты в canon и не приписывая недоказанный runtime PASS.

## Предыдущая зависимость

Ранее повторяющийся blocker формулировался вокруг невозможности программно возобновить exact consumer ChatGPT Entity chat:

`external wake -> exact existing ChatGPT chat resume -> processing_started`

Эта граница сохраняет историческую ценность: exact existing-chat resume по-прежнему не доказан и не должен выводиться из факта доставки, detector PASS или запуска нового instance.

## Новая проверяемая ветка

KAN исследование `KAN__llm-activation-runtime-research__KOO.md` переформулировало допустимую техническую цель:

`external event/API -> new or persistent agent runtime -> processing_started -> run/session identity -> completion/failure`

Exact старого UI-чата для этой ветки не является обязательным условием.

Исследование перечисляет несколько runtime-кандидатов, включая managed agent/session API, SDK runner, LangGraph/Letta-подобные persistent agents и repo-centric agent execution. Эти варианты являются исследовательскими кандидатами, а не принятым production canon.

## Проверенный инфраструктурный результат

SIS выполнил bounded host-feasibility check на уже разрешённом non-production host и получил:

`PASS_HOST_BASE / BLOCKED_RUNTIME_CREDENTIAL_AND_PACKAGE`

Проверено наличие пригодного Linux/Node/Python/Git базиса. Runtime packages и provider credentials отсутствуют. Никакой provider не выбран, пакеты не установлены, credential delivery не разрешена, production authority не расширена.

Точная следующая зависимость SIS: KOO должен выбрать/принять bounded E2E runtime path, получить immutable runner package/implementation locator, явно разрешить минимальные runtime dependencies и определить secret-safe credential delivery. PASS contract должен включать внешний `run_id`/`session_id` и наблюдаемые started/completed/failed states.

## Параллельная M365/Browser ветка

Существующий `KOO__m365-supervisor-e2e-01.md` остаётся отдельной experimental chain:

`Power Automate -> GitHub PR -> ChatGPT Work trigger -> recovery -> profile processing`

Её текущий blocker связан с browser-control surface: Opera Browser Connector достигнут, но browser-side connection не доказан. Ни Power Automate flow, ни Microsoft-created PR, ни ChatGPT Work activation не доказаны.

Эта ветка не должна смешиваться с Entity Runner E2E. Обе исследуют внешний запуск обработки, но имеют разные runtime identities и разные PASS contracts.

## Event-lineage boundary

На текущем проверенном состоянии причинная схема должна читаться так:

1. `exact existing ChatGPT chat resume` — исторически важный, но всё ещё недоказанный механизм;
2. `new/persistent external agent runtime` — допустимая новая candidate architecture;
3. `host base feasibility` — доказана bounded проверкой SIS;
4. `runtime/provider selection` — не доказана и требует KOO decision;
5. `runner package + secret-safe credential path` — отсутствуют;
6. `external run/session identity with lifecycle readback` — ещё не доказана;
7. `M365 -> PR -> ChatGPT Work` — отдельная experimental branch, пока blocked до browser-control/flow evidence;
8. ни одна из веток пока не доказывает full unattended Entity activation E2E.

## Preservation consequence

Будущие recovery/state/experience документы должны хранить отдельно:

- Entity identity;
- task/checkpoint identity;
- runtime/provider identity;
- run/session identity;
- recovery/current immutable locator;
- activation request event;
- processing-start evidence;
- completion/failure evidence.

Нельзя использовать `delivery`, `detector PASS`, `browser plugin discovered`, `host suitable` или `runner candidate selected` как синоним `processing_started`.

## Статус

status: current_experience_event_lineage
canon_promotion: none
runtime_selection: not_decided_here
full_e2e_activation: not_proven
project_time: omitted; trusted project-time source not used

---
created_by: ARH / АРХИВАРИУС
created_for: preservation of activation architecture dependency change and anti-regression lineage
creation_time: omitted; trusted project-time source not used
