# KOO — операторская доска всех рабочих конвейеров ШТАБА

status: CURRENT_OPERATOR_DISPATCH_BOARD
scope: all verified active HQ task pipelines
source_boundary: wellbeing-hq main scanned through `96a538408c596e32cc4b51fb27c8334c3bab20df`
project_time: omitted; trusted project-time source not used

## 1. Правило диспетчеризации

Пятифазный цикл `KOD → KOO → SIS → SHT → ARH` является дежурным polling/resume контуром, но не описывает все рабочие цепочки ШТАБА.

ОПЕРАТОР ведёт одновременно несколько причинных конвейеров. Чтобы один технический эпизод не вытеснял остальные, ручной режим работает round-robin:

`одна Сущность → один bounded профильный проход → проверяемый результат/blocker → маршрутизация → переход к следующей независимой цепочке`.

Если конкретная causal dependency требует возврата предыдущей Сущности, зависимость имеет приоритет над формальным порядком запуска.

## 2. Текущие проверенные конвейеры

### P1 — Telegram Media Phase 1B

Цепочка:
`KAN → KOO → KOD → KOO → SIS → KOO → далее WEB/KAN/KOD по фактическому verdict`.

Текущее состояние:
- KAN privacy gate: bounded/conditional;
- KOD privacy-fix accepted KOO только как technical basis;
- exact package: `entities/koder/outbox/telegram-media-phase1b-privacy-v01/` @ `cd81bbd98a4be334388f95ea948427d91fa82a05`;
- KOO independent SHA-256: 9/9 PASS;
- live send: NOT AUTHORIZED.

Текущий владелец действия:
`SIS`.

Exact inbox:
`entities/sisadmin/inbox/KOO__telegram-phase1b-runtime-privacy-readiness-r2__SIS.md`
commit: `ca4da476e4b3d0aa72649e867714335e39e4dd99`.

После SIS:
вернуть результат KOO; KOO решает следующий gate. Не перескакивать сразу к live Telegram.

### P2 — GitHub Information Entry

Цепочка:
`KAN/RED/SIS inputs → WEB synthesis → KOD pilot r1 → SHD defect → KOD r2 → KOO review → SHD re-verification → KOO`.

Текущее состояние:
KOD вернул strict-type-validation r2.

Exact KOO inbox:
`entities/koordinator/inbox/KOD__github-info-entry-pilot-r2-result__KOO.md`.

Package:
`entities/koder/outbox/github-info-entry-pilot-v01-r2/`
commit: `04753a229afc24ecf724f583e6df3dabed6bfba3`.

Текущий владелец действия:
`KOO`.

Следующий допустимый этап:
KOO technical review; при PASS — новая exact task ШАРДОВИКУ на cross-layer re-verification. Public-ready promotion до этого blocked.

### P3 — COOP rights-transition

Цепочка:
`VOL → SHT → VOL → при необходимости KOO/другая профильная Сущность`.

Текущее состояние:
VOL опубликовал v0.4 после предыдущего bounded review.

Exact SHT inbox:
`entities/shtabist/inbox/VOL__COOP-rights-transition-spec-v0_4__SHT.md`.

Exact artifact:
`entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_4.md`
commit: `e2e98b623a89bae1e23d8b035c93e4e05af10827`.

Текущий владелец действия:
`SHT`.

Требуемый проход:
последний single-criterion re-review только criterion 3 section 18; вернуть VOL bounded PASS либо exact remaining critical defect.

### P4 — литературная публикация «Сначала она была выдумана»

Цепочка:
`RED → KOO → KAN → KOO → RED/OPERATOR`.

Exact RED candidate:
`entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana-v03__KOO.md`
commit: `1d81c994b212ea8a00e6441136d39dd5364c6b32`.

Текущий gate:
short bounded KAN delta-review.

Exact KAN inbox:
`entities/kancelar/inbox/KOO__snachala-ona-byla-vydumana-v03-delta-review__KAN.md`.

Текущий владелец действия:
`KAN`.

Publication authorized: no.

После KAN:
результат → KOO → только затем RED revision/acceptance path либо OPERATOR decision.

### P5 — Source Loading Policy v2.1

Цепочка:
`KAN → KOO → OPERATOR`.

Candidate:
`entities/kancelar/outbox/source-loading-policy-v2_1-candidate.md`
commit: `59ae5c036151460ca63a0e2ccd37d4aa53c88aaf`.

KOO inbox:
`entities/koordinator/inbox/KAN__source-loading-policy-harmonization__KOO.md`.

Current boundary:
candidate is NOT an active Project Source.

Текущий владелец решения:
`OPERATOR`, после KOO exact review/presentation.

Запрещено молча считать v2.1 approved.

### P6 — ARH preservation/recovery

Цепочка:
`current-writer self-state → independent verification → ARH canonical publication/readback/registry → practical initiation only when actually required`.

Текущее состояние:
ARH recovery v03 canonical preservation PASS.

Canonical locator:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`.

Текущая работа:
routine monitoring/preservation only. Practical replacement ARH не выполнен и не требуется без нового trigger/evidence.

ARH остаётся обязательным конечным preservation звеном после значимых state-changing циклов.

### P7 — VPN / client experience / SHD integration

Цепочка:
`SHD diagnostics → SIS review/acceptance → KOO where policy/registry decision is needed → ARH preservation as needed`.

В SIS inbox уже находятся SHD результаты:
- `SHD__vpn-v2rayng-hiddify-resolution__SIS.md`;
- `SHD__vpn-client-experience-candidate__SIS.md`;
- `SHD__android-vpn-diagnostics-runbook__SIS.md`.

Текущий владелец следующего содержательного решения:
`SIS`, но после более приоритетного P1 runtime/privacy gate.

SHD не должен плодить новые версии, пока нет SIS/KOO response или новой технической проблемы.

### P8 — публичная cooperation speech

RED exact candidate:
`entities/redaktor/outbox/RED__wellbeing-cooperation-speech-v02__KOO.md`
commit: `30214bc36f48d4804ffff9fc60c3a7aedb0438c1`.

KOO state:
`ACCEPTED_AS_BOUNDED_PUBLIC_SPEECH_CANDIDATE`.

Exact candidate уже routed OPERATOR.

Текущий владелец решения:
`OPERATOR`.

До OPERATOR acceptance/revision RED не должен переписывать текст по инерции.

### P9 — Entity runner / activation / continuity

У KOD, SIS, KAN, SHT и ARH существует отдельная многозвенная линия entity-runner/activation/continuity.

Она не закрыта тем фактом, что отдельные activation records умеют детектировать GitHub push. Проверенный текущий системный предел остаётся: detector может зафиксировать event, но exact existing Entity-chat resume текущим adapter не доказан.

Эта линия сохраняется в backlog и должна подниматься Resume-First по свежим inbox/current/receipts. Она не должна вытеснять профильные live blockers P1–P4, но и не должна исчезать из операторской доски.

### P10 — WEB / publication surface

WEB участвует минимум в двух текущих ветках:
- Telegram experimental/public surface;
- GitHub Information Entry Stage B.

Сейчас самостоятельного следующего WEB mutation без upstream verdict не требуется:
- Telegram ждёт SIS/KOO pre-live gate;
- Information Entry ждёт KOO review r2 + SHD re-verification.

WEB запускать сразу, когда KOO создаёт exact downstream task, а не ради пустого polling.

## 3. Сущности без текущего профильного запуска

По свежему HQ inbox/current scan отдельной новой профильной работы сейчас не подтверждено для:
- KON / КОНСУЛЬТАНТ;
- SHKOLA / ШКОЛА как HQ entity;
- PROVODNIK.

Это не означает, что роли отменены. Их режим — event-driven: запускать при exact task/dependency, а не производить документы ради видимости занятости.

VOL используется в существующих COOP routes; active approved role source v2.3 отдельно предупреждает, что дополнительные полномочия VOL из одного имени выводить нельзя.

## 4. Рекомендуемый ручной round-robin ОПЕРАТОРА сейчас

Чтобы не заморить одну ветку вниманием и не забыть остальные:

1. SIS — P1 Telegram runtime/privacy r2.
2. KAN — P4 literary v0.3 delta-review.
3. SHT — P3 COOP rights-transition v0.4 criterion-3 review.
4. KOO — обработать результаты предыдущих проходов + P2 info-entry r2.
5. SHD — только после exact KOO r2 re-verification task.
6. VOL — после результата SHT по v0.4.
7. RED — после KAN/KOO decision по literary branch либо OPERATOR decision по speech.
8. WEB — после KOO unlock по Telegram или info-entry.
9. ARH — preservation pass после значимого изменения состояния/закрытия цепочки.
10. KOD — при exact defect/next implementation task; не будить ради повторения уже отданных candidates.

Это round-robin приоритеты текущего verified state, а не вечный нормативный порядок. Каждый запуск начинается fresh GitHub-preflight и Resume-First.

## 5. Automation boundary

На последней инструментальной проверке:
- KOO GitHub Work: ON, :24;
- ARH GitHub Work: ON, :00;
- KOD GitHub Work: OFF;
- SIS GitHub Work: OFF;
- SHT GitHub Work: OFF;
- KAN GitHub Watch: OFF.

Automation state не заменяет task state. Перед включением каждой выключенной automation нужно сверить её prompt с текущей causal chain, чтобы не воскресить старую задачу как вечный приоритет.

## 6. Правило для КООРДИНАТОРА

Каждый KOO проход обязан проверять не только собственный текущий technical chain, но и минимум следующие классы:

1. technical/runtime: KOD/SIS/SHD;
2. organizational/process: SHT/VOL;
3. policy/legal/semantic: KAN;
4. editorial/media/publication: RED/WEB;
5. preservation/recovery: ARH;
6. OPERATOR-required decisions.

Если одна ветка активна много проходов подряд, KOO обязан проверить, не голодают ли независимые pipelines.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ и replacement KOO единую проверяемую карту всех параллельных рабочих конвейеров ШТАБА
СТАТУС: current_operator_dispatch_board
