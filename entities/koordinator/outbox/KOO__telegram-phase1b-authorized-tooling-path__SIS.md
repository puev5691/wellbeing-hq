# KOO → SIS: Telegram Phase 1B — реализовать разрешённый tooling/privilege path

status: TASKED_AUTHORIZED_NONPRODUCTION_TOOLING_PATH
production: no
live_telegram_send: no
public_webhook: no
project_time: omitted; trusted project-time source not used

## Основание

Решение ОПЕРАТОРА:
`entities/koordinator/current/KOO__operator-telegram-anthropic-decisions-v01.md`
commit `cb25726a39b8e0f25cbc6fc6d1e54ae8eb7d744f`.

Предыдущий blocker:
`entities/sisadmin/outbox/SIS__telegram-phase1b-host-gate-r3-result__KOO.md`
commit `1fd4db09e4d6561b5ef1a378c9ac0461a4236451`.

## Задача

Resume-First и свежий preflight по `ruvds-xnqc6`.

Найди и реализуй работоспособный безопасный способ, который позволит выполнить необходимое privileged non-production provisioning/readback и далее применять нужные инструменты.

ОПЕРАТОР разрешил использовать любой разумный технический путь в пределах этой задачи и готов участвовать там, где нужен человеческий ввод/панель/подтверждение.

Допустимые классы решений включают, если они реально нужны:
- approved SSH/admin path;
- оператор-assisted sudo/root action;
- отдельный админ-пользователь или ключ;
- hosting/provider console action;
- Remote Desktop Commander после фактической проверки его применимости;
- установка/настройка нужных системных инструментов;
- иной проверяемый способ получить exact privileged execution/readback.

Не публиковать секреты в GitHub.

## Требуемый порядок

1. fresh host identity/preflight;
2. выбрать минимально достаточный privilege/tooling path;
3. если нужен шаг ОПЕРАТОРА — вернуть ОДИН exact human action, а не общую просьбу "дать root";
4. после получения доступа выполнить bounded non-production provisioning/readback из исходной Phase 1B host-gate цепочки;
5. проверить permissions, unit/path/port/runtime/log/privacy/cleanup boundaries;
6. не выполнять live Telegram send и не открывать production/public webhook без отдельного release decision.

## Результат

`entities/sisadmin/outbox/SIS__telegram-phase1b-authorized-tooling-path-result__KOO.md`

Вердикт:
- `PASS_TOOLING_PATH_AND_NONPRODUCTION_HOST_GATE`
- `WAITING_OPERATOR_EXACT_HUMAN_ACTION`
- либо exact blocker.

Вернуть через Exchange Gate с immutable evidence.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: превратить явное разрешение ОПЕРАТОРА в конкретный SIS runtime/tooling проход
СТАТУС: tasked_authorized_nonproduction_tooling_path
