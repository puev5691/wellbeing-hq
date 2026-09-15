# КООРДИНАТОР — рабочая очередь v0.9

Статус: текущая операторская очередь после полного обхода Сущностей и fresh GitHub-preflight.
Это рабочий документ KOO, не канон проекта.
Проектное время не указывается.

## Главное изменение

Предыдущая волна в основном завершена:
- WEB Static Preview v0.3 E1 recheck: PASS и принят KOO;
- ARH recovery candidate r0.4: PASS, ready for OPERATOR gate;
- SHD main/root genesis research: принят, дальнейший root-profile требует KOD;
- SHT recovery-record lifecycle convention: принят;
- VOL P5 protocol: принят;
- SIS Telegram Phase1B: точный blocker `BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`, следующий owner KOD.

WEB и ARH остаются функциональны, но OPERATOR наблюдает рост задержки/глубины. Поэтому их следующий профильный шаг — сохранение continuity до возможной замены чата.

## Операторское окно: 4 текущих действия

### 1. KOD — human writer gate

Новый KOD уже `initiation_verified`, но старый verified current-writer формально не retired.

ОПЕРАТОР в новом KOD-чате даёт явное решение:

> Предыдущий verified KOD current-writer прекращает дальнейшую профильную работу и считается retired для новых KOD mutations. Новому `initiation_verified` KOD instance разрешаю выполнить fresh competing-writer check и, если нового конфликта нет, установить replacement current-writer с immutable publication/readback и post-publication reconciliation. После writer establishment остановись и верни KOO результат; профильные задачи автоматически не начинай.

Основание:
`entities/koordinator/outbox/KOO__KOD-replacement-writer-decision-gate__OPERATOR.md`
commit `a0c8f70cbe3edd9031ee4881d189639f5a166d98`.

После PASS KOO dispatch'ит уже подготовленный, но пока заблокированный Telegram threading-fix:
`entities/koordinator/outbox/KOO__telegram-phase1b-threading-fix-r01__KOD.md`
commit `5553e1857936755ee4cc511eb5d5f1d8a0b4c092`.

Следующий KOD lane после него:
`KOO__tera2-root-profile-candidate-r01__KOD.md`
commit `9c6972681ae8b058cbe99c5ae4a3674a5cd1d3eb`.

### 2. ARH — pre-replacement self-preservation

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай exact input `KOO__ARH-pre-replacement-self-preservation-r01__ARH.md` из своего inbox. Только self-preservation candidate до возможной замены чата: не инициируй replacement, не меняй writer и не смешивай sanitation-хвосты. Верни KOO exact result через Exchange Gate.

Task commit: `65eb351c2b428e4ec3ee38bbfd5e0a1644b421dc`.

Цель: получить свежий immutable external preservation candidate до того, как текущий глубокий ARH-чат начнёт реально ломаться.

### 3. WEB — continuity preservation candidate

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай exact input `KOO__WEB-continuity-preservation-candidate-r01__WEB.md` из своего inbox. Только candidate-only continuity capture; не объявляй canonical recovery, initiation_verified или current-writer. Верни KOO exact result через Exchange Gate.

Task commit: `4ee6182f069e023ac2a33ffbb9db2348730d99ec`.

Цель: сохранить проверяемое состояние WEB до замены, поскольку formal canonical WEB recovery/current-writer basis пока не подтверждена.

### 4. VOL — Work-mode pilot observation

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай exact input `KOO__work-mode-pilot-observation-r01__VOL.md` из своего inbox. Зафиксируй только реально наблюдавшееся поведение Work-mode; отделяй observed от not-proven и не делай выводов о лимитах тарифа. Верни KOO exact result через Exchange Gate.

Task commit: `88021fe9f2baa6beabf5d93a530629816c2b6b2e`.

## Горячий резерв: SHT

После освобождения первого слота:

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай exact input `KOO__entity-chat-to-work-migration-process-r01__SHT.md` из своего inbox. Только process design staged Chat→Work migration; никого фактически не мигрируй и не расширяй authority. Верни KOO exact result через Exchange Gate.

Task commit: `df3cdcd429f8673a12ede9eceb8b0cb47a54fa15`.

## Сейчас не будить

- SIS: ждёт новый immutable KOD runtime candidate; повтор sudo/старого host gate запрещён.
- SHD: ждёт KOD root-profile candidate после Telegram fix.
- KAN: текущая authority-проверка закрыта; следующий профильный review пока не материализован.
- RED: текущая редакционная ветка не блокирует технический процесс; новая задача появится после накопления новых утверждаемых фактов.

## Готовый OPERATOR gate recovery-canon v1.5

Candidate r0.4 прошёл SHT → KAN → ARH и готов к человеческому решению.

Gate artifact:
`entities/koordinator/outbox/KOO__entity-recovery-canon-v1_5-operator-gate__OPERATOR.md`
commit `17190f729eef6537f0404af387253c9c11eb3a21`.

Допустимые решения:
- `APPROVE_V1_5_WAKE_INITIATION_RESUME_AMENDMENT`
- `RETURN_V1_5_FOR_FIXES: <точный дефект>`
- `REJECT_V1_5`

Это решение не требуется для запуска текущей четырёхполосной волны.

## Health / replacement note

ARH: replacement preparation now justified. Current external recovery exists, but current HQ state advanced through layered delta; self-preservation refresh is scheduled before any initiation.

WEB: replacement preparation justified, but canonical recovery/current-writer basis not proven. Therefore only continuity candidate is allowed first.

Neither chat is declared failed or retired at this time.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ следующую применимую очередь и одновременно подготовить WEB/ARH к безопасной замене
СТАТУС: current_operator_queue_v0_9
