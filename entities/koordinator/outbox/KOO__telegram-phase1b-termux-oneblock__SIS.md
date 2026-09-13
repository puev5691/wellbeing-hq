# KOO → SIS: Telegram Phase 1B — один операторский Termux-блок

status: TASKED_OPERATOR_HANDOFF_REFINEMENT
profile_owner: SIS / СИСАДМИН
production: no
live_telegram_send: no
public_webhook: no
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР прямо указал, что подготовка команды/блока для доступа к серверу и запуска уже подготовленного Phase 1B script является профильной работой SIS, а не KOO.

Текущий SIS result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-authorized-tooling-path-result__KOO.md`
commit `488909ed0c42f709c3d23805c51967a2f82ac432`
blob `44031aac4c5c96eb9268de2fd67235da37dd5824`.

Текущий exact human action по этому result:
`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

## Задача

Используя ТОЛЬКО уже известное тебе фактическое состояние Termux/SSH/host/tooling-контура и свои существующие наработки, подготовь для ОПЕРАТОРА один короткий и изящный copy-paste блок для Termux, который:

1. сам выполняет нужный вход/переход к `ruvds-xnqc6` тем способом, который SIS уже считает рабочим;
2. запускает подготовленный `phase1b-host-gate-once.sh`;
3. оставляет ОПЕРАТОРУ только ввод пароля/подтверждения в нужный момент;
4. не заставляет ОПЕРАТОРА вручную собирать SSH-сеанс, команды и проверки;
5. не устанавливает заново то, что SIS уже знает как установленное;
6. не добавляет универсальные проверки/страховки, которые SIS считает лишними для этого exact контура;
7. в конце показывает только тот короткий результат, который ОПЕРАТОР должен вернуть SIS/KOO.

## Важная граница

Не выполнять заново широкую диагностику и не переизобретать tooling path. Это refinement операторского handoff поверх уже выполненной SIS работы.

Не публиковать пароль/ключи/секреты.
Не делать live Telegram send или production/public webhook.

## Результат

`entities/sisadmin/outbox/SIS__telegram-phase1b-termux-oneblock__KOO.md`

В начале файла дать сам готовый Termux-блок, затем максимум несколько строк пояснения: что вводит ОПЕРАТОР и что прислать обратно.

Вернуть через Exchange Gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть подготовку операторского Termux handoff профильному владельцу SIS после замечания ОПЕРАТОРА
СТАТУС: tasked_operator_handoff_refinement
