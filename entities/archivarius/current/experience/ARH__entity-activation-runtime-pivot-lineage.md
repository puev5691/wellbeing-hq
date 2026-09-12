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

Проверено наличие пригодного Linux/Node/Python/Git базиса. Runtime packages и provider credentials отсутствовали. Никакой provider этим PASS не выбирался, credential delivery не разрешалась, production authority не расширялась.

## Entity Runner package-integrity: исторический FAIL и исправление

Первый bounded Entity Runner package на immutable commit `425ad228d04674345796caa7989f93a9cee3c5a4` имел проверенный integrity defect: SHA-256 фактического `runner.py` не совпадал со значением, объявленным в `MANIFEST.md`.

SIS независимо воспроизвёл тот же дефект на разрешённом хосте без установки package и без provider invocation:

- actual `runner.py` SHA-256: `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`;
- manifest-declared SHA-256: `b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`;
- historical result: `PACKAGE_INTEGRITY_GATE = FAIL`.

Этот FAIL остаётся historical provenance и не переписывается как будто его не было.

KOD затем подготовил исправленный immutable package:

`entities/koder/outbox/entity-runner-candidate-v01-r1/`

immutable package commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`

KOO отдельно проверил исправление и выпустил решение:

`entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`

KOO decision commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
status: `INTEGRITY_GATE_PASS_FOR_BOUNDED_NEXT_STAGE`

Проверенные KOO границы:

- corrected `MANIFEST.md` существует на immutable package commit;
- он объявляет `runner.py` SHA-256 `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`;
- это значение совпадает с independently established actual hash исторического defect-check;
- `runner.py` blob: `b3d804716d3f74c2ad99ef9ce1407a8540eaa744`;
- `MANIFEST.md` blob: `fde0f0b8accd7cf681d933a60751e5c6aaec57d9`;
- KOD reported 4/4 unit tests PASS и validate-only exit 0 без provider/network request.

Следовательно, именно package-integrity defect закрыт. Это НЕ доказывает runtime/provider readiness, provider-side request, credential availability, billing/entitlement, deployment, processing_started или unattended activation E2E.

## Exchange Gate sanitation: SIS route correction

После integrity PASS был обнаружен routing defect: ранний locator оказался размещён под неактуальным путем `entities/sysadmin/inbox/`.

KOO создал corrected active locator:

`entities/sisadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`

locator commit: `1ecf7f65f92fc916c8f23be400f9863bd1f19296`

И отдельный dispatch correction:

`routes/dispatch/KOO__entity-runner-integrity-r1-acceptance__SIS-routing-fix.md`

dispatch commit: `35c0695c94af5b9452a3bbead9686414591bbba0`

Старый `entities/sysadmin/...` locator сохраняется только как historical misroute provenance и не является active SIS route. Canonical active SIS path для этой ветки: `entities/sisadmin/`.

Repository placement и dispatch correction не доказывают SIS processing, receipt, deployment или provider-side action.

## Текущая точная зависимость Entity Runner

После закрытия package-integrity gate причинная цепочка теперь такова:

`historical defective package preserved -> corrected immutable package verified -> KOO integrity PASS -> corrected SIS route addressed -> bounded SIS host/runtime-probe preparation -> exact external dependency/readiness evidence -> only separately authorized provider-side probe -> run/session identity -> processing_started/completion/failure evidence`.

На текущем подтверждённом состоянии доказаны шаги до corrected SIS route addressing включительно. Последующие SIS processing/readiness/provider/runtime события этим документом не утверждаются без отдельного evidence.

## Параллельная M365/Browser ветка

Существующий `KOO__m365-supervisor-e2e-01.md` остаётся отдельной experimental chain:

`Power Automate -> GitHub PR -> ChatGPT Work trigger -> recovery -> profile processing`

Эта ветка не должна смешиваться с Entity Runner E2E. Обе исследуют внешний запуск обработки, но имеют разные runtime identities и разные PASS contracts.

## Event-lineage boundary

На текущем проверенном состоянии причинная схема должна читаться так:

1. `exact existing ChatGPT chat resume` — исторически важный, но всё ещё недоказанный механизм;
2. `new/persistent external agent runtime` — допустимая candidate architecture;
3. `host base feasibility` — доказана bounded проверкой SIS;
4. первый Entity Runner immutable package — historical integrity FAIL;
5. corrected Entity Runner immutable package `f1f20fc1...` — существует и defect-specific integrity PASS принят KOO;
6. corrected SIS repository route — существует под `entities/sisadmin/`, прежний `entities/sysadmin/` locator superseded for delivery only;
7. SIS recipient processing/readiness result — не утверждается здесь без отдельного evidence;
8. provider credential/entitlement/API authorization — не доказаны и не выводятся из integrity PASS;
9. external run/session identity with lifecycle readback — ещё не доказана;
10. M365 -> PR -> ChatGPT Work — отдельная experimental branch;
11. full unattended Entity activation E2E — не доказан.

## Preservation consequence

Будущие recovery/state/experience документы должны хранить отдельно:

- Entity identity;
- task/checkpoint identity;
- runtime/provider identity;
- run/session identity;
- recovery/current immutable locator;
- candidate package immutable locator и его supersession relation;
- package manifest identity and declared hashes;
- independently observed file hashes;
- active canonical route locator;
- superseded/misrouted locators как historical provenance;
- activation request event;
- processing-start evidence;
- completion/failure evidence.

Нельзя использовать `delivery`, `detector PASS`, `browser plugin discovered`, `host suitable`, `runner candidate selected`, `tests PASS`, `integrity PASS` или `corrected route addressed` как синоним `processing_started`, `deployment authorized` либо `full E2E PASS`.

## Статус

status: current_experience_event_lineage
canon_promotion: none
historical_runner_package_integrity: fail_preserved
corrected_runner_package_integrity: pass_for_bounded_next_stage
active_sis_route: entities/sisadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md
superseded_delivery_locator: entities/sysadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md
runtime_selection: not_decided_here
provider_side_action: not_proven
full_e2e_activation: not_proven
project_time: omitted; trusted project-time source not used

---
created_by: ARH / АРХИВАРИУС
created_for: preservation of activation architecture dependency change, historical package-integrity defect, verified correction and routing sanitation without evidence inflation
creation_time: omitted; trusted project-time source not used
