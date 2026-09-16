# КООРДИНАТОР — рабочая очередь v0.11

Статус: `CURRENT_OPERATOR_QUEUE`
Режим: `WIP_LIMIT_2`
Проектное время не указывается.

## Текущее фактическое состояние

### ACTIVE SLOT 1 — KOD / OpenAI Responses API D0 adapter r0.1

Текущая exact task:
`entities/koordinator/outbox/KOO__openai-responses-d0-adapter-r01__KOD.md`
commit `73a7ccbc2a3728f69c123a3790129343325c4277`
blob `0472f621324885bc0bc6a8c02b69b45c8761def3`.

Последняя зафиксированная KOD-работа:
commit `4c55e0886f77cc46f012be335a09d62c962d6faf`
message `KOD: stage OpenAI Responses D0 policy r01`.

Terminal result, complete immutable package/readback и return-routing KOO после этого commit в свежем HQ не подтверждены.

Текущий статус:
`CURRENT_TASK_INCOMPLETE_AT_RESULT_PUBLICATION_STAGE`.

Следующее действие: KOD должен продолжить именно эту task, не начинать новую, завершить недостающие части и вернуть terminal result:
`PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`
либо exact `BLOCKED_* / FAIL_*`.

### SLOT 2 — FREE / SIS WAITING

SIS завершил host/runtime gate r0.1 exact blocker:
`entities/sisadmin/outbox/SIS__telegram-phase1b-host-runtime-gate-r01__KOO.md`
commit `a49040d2e9b4ecceeb4827d9e224e0a5e1eee952`
blob `34eff69659a6bd4a73d67321deb42af509ebcad4`.

Verdict:
`BLOCKED_PRIVILEGE_REQUIRED`.

Runtime contract восстановлен однозначно. Blocker не в коде и не в paths: accepted `/opt`, `/etc`, `/var/lib` runtime boundary требует privilege/provisioning, а exact task запрещала sudo/root/privileged mutation.

SIS сейчас:
`WAITING_OPERATOR_KOO_PRIVILEGE_PATH_DECISION`.

Не повторять historical sudo gate и не подменять accepted paths на `/tmp`.

Новый SIS runtime attempt допустим только после отдельного exact privilege/provisioning решения.

## Следующие зависимости

### OpenAI live D0 gate

Не запускать до terminal PASS текущей KOD adapter task.
После PASS дополнительно потребуются:
- OPERATOR API billing readiness;
- OPERATOR-created API key;
- secret-safe runtime injection;
- выбранный Unix-host preflight;
- отдельное разрешение ровно на один D0 synthetic live call.

### Telegram Phase1B privilege/provisioning gate

Не запускать автоматически.
Требуется отдельное решение, разрешающее exact privileged restoration/provisioning принятого runtime boundary без silent replay старой sudo-процедуры.

### TERA2 / SHD

Остаётся после освобождения KOD slot:
`entities/koordinator/outbox/KOO__tera2-root-profile-candidate-r01__KOD.md`
commit `9c6972681ae8b058cbe99c5ae4a3674a5cd1d3eb`.

Пока KOD current task не закрыта, TERA2 не запускать.

### Recovery canon v1.5

Готовый OPERATOR gate остаётся отдельным неблокирующим решением:
`entities/koordinator/outbox/KOO__entity-recovery-canon-v1_5-operator-gate__OPERATOR.md`
commit `17190f729eef6537f0404af387253c9c11eb3a21`.

## Background

### Retired Entity lifecycle study

v0.1 заменяется v0.2 с `CAPTURE_FIRST` и `EXTERNAL_COLLECTOR`.
Retired instance не обязан иметь GitHub write.
Исследование не занимает WIP-slot активной профильной работы.

Первая агрегация только после накопления примерно 10–20 пригодных samples.

### Chat → Work migration

Process design готов. Массовый migration не запускать. API/entity-runner остаётся более высоким приоритетом.

### ARH / WEB replacement

Preservation candidates готовы. Replacement только по эксплуатационной необходимости/отдельному gate.

## WIP interpretation

WIP считается по незакрытым проектным execution cycles, а не по тому, печатает ли чат сейчас ответ.

`active` = task имеет authority/input и не имеет terminal result/blocker/waiting.

`blocked/waiting` освобождает execution slot, но dependency остаётся в очереди.

Исторический или промежуточный commit не является terminal completion.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: синхронизировать очередь с фактическим KOD incomplete-cycle и SIS privilege blocker
СТАТУС: `CURRENT_OPERATOR_QUEUE_V11`
