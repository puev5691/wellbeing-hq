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

## Entity Runner package-integrity evidence

После появления bounded Entity Runner candidate техническая ветка не перешла в deployment/runtime probe. KOO ранее обнаружил immutable-package identity defect на package commit `425ad228d04674345796caa7989f93a9cee3c5a4`: SHA-256 фактического `runner.py` не совпадает со значением, объявленным в `MANIFEST.md`.

SIS независимо воспроизвёл тот же дефект на разрешённом хосте `ruvds-xnqc6`, без установки package и без provider invocation:

- actual `runner.py` SHA-256: `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`;
- manifest-declared SHA-256: `b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`;
- result: `PACKAGE_INTEGRITY_GATE = FAIL`.

Это усиливает доказательность blocker, но не меняет его класс. Независимая воспроизводимость FAIL не является package PASS, deployment authorization или runtime evidence.

Текущая точная зависимость этой ветки:

`KOD processing of existing return-for-fix -> new immutable package commit -> regenerated manifest from exact final bytes -> SHA-256 verification -> unit tests + validate-only rerun -> KOO separate integrity verification/acceptance -> only then bounded SIS deployment/runtime probe if authorized`.

Дефектный immutable locator должен сохраняться как historical provenance и не переосмысливаться как исправленный package.

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
4. `Entity Runner implementation/test evidence` — локальная bounded evidence, не пересекающая package-integrity gate;
5. `Entity Runner package integrity` — FAIL, независимо воспроизведён KOO и SIS на одном immutable package locator;
6. `corrected immutable runner package` — не доказан и зависит от KOD processing существующего return-for-fix;
7. `KOO re-verification/acceptance` — не доказана;
8. `runtime/provider selection` — не утверждается этим документом;
9. `external run/session identity with lifecycle readback` — ещё не доказана;
10. `M365 -> PR -> ChatGPT Work` — отдельная experimental branch, пока blocked до browser-control/flow evidence;
11. ни одна из веток пока не доказывает full unattended Entity activation E2E.

## Preservation consequence

Будущие recovery/state/experience документы должны хранить отдельно:

- Entity identity;
- task/checkpoint identity;
- runtime/provider identity;
- run/session identity;
- recovery/current immutable locator;
- candidate package immutable locator;
- package manifest identity and declared hashes;
- independently observed file hashes;
- activation request event;
- processing-start evidence;
- completion/failure evidence.

Нельзя использовать `delivery`, `detector PASS`, `browser plugin discovered`, `host suitable`, `runner candidate selected`, `tests PASS` или `independently reproducible FAIL` как синоним `processing_started`, `package PASS` либо `deployment authorized`.

## Статус

status: current_experience_event_lineage
canon_promotion: none
runner_package_integrity: fail_independently_reproduced
runner_correction_dependency: KOD_existing_return_for_fix
runtime_selection: not_decided_here
full_e2e_activation: not_proven
project_time: omitted; trusted project-time source not used

---
created_by: ARH / АРХИВАРИУС
created_for: preservation of activation architecture dependency change, package-integrity causal boundary and anti-regression lineage
creation_time: omitted; trusted project-time source not used
