# КООРДИНАТОР → СИСАДМИН: текущий приоритет SIS — инфраструктурный доступ к эРэФии

status: `READY_FOR_ADDRESS_DELIVERY`
production_mutation: `no`
project_time: omitted; trusted project-time source not used

## Решение по очереди SIS

Текущий SIS current-writer выполняет одну профильную полосу за раз.

До отдельного решения Telegram Phase1B resume gate r0.4 переводится в `PAUSED_BY_HIGHER_CURRENT_PRIORITY`. Старый Phase1B task не отменяется и не закрывается, но сейчас не исполняется.

Текущий приоритет: инфраструктурно восстановить управляемый доступ к exact host эРэФия для продолжения bounded SHD WBN/TERA work.

## Exact входы

Основной SHD input:
`entities/sisadmin/inbox/SHD__erefia-host-access-restore__SIS.md`

Исправление SSH endpoint:
`entities/sisadmin/inbox/SHD__erefia-ssh2222-correction__SIS.md`

Точный текущий SSH endpoint:
`194.87.107.135:2222`

Порт `22` не использовать как текущий SSH endpoint.

## Разрешённый объём

Выполнить fresh Resume-First и только инфраструктурную проверку/восстановление доступа, необходимого для дальнейшего read-only inventory SHD.

Цель:
- подтвердить доступность SSH `194.87.107.135:2222`;
- вернуть/подтвердить Remote Desktop Commander на exact host, если это можно сделать в рамках уже существующей инфраструктуры и полномочий;
- не менять TERA/WBN runtime;
- вернуть SHD и KOO проверяемый результат либо точный blocker.

Если требуется отдельное действие ОПЕРАТОРА, вернуть одну точную человеческую операцию и остановиться в `WAITING_OPERATOR_EXACT_HUMAN_ACTION`.

## Запрещено

- менять TERA/WBN service, chain identity, DB, genesis/reward logic;
- менять nginx/Xray/UFW/DNS без отдельной задачи;
- публиковать credentials;
- destructive cleanup;
- параллельно исполнять Telegram Phase1B r0.4;
- считать входящий файл или activation request доказательством processing.

## Ожидаемый результат

Вернуть через Exchange Gate файл:
`entities/sisadmin/outbox/SIS__erefia-access-readiness__KOO.md`

В нём указать:
- fresh HQ boundary;
- exact host/port;
- что реально проверено;
- Commander state;
- TERA/WBN mutation: yes/no;
- следующий допустимый шаг или точный blocker.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: сериализовать текущую SIS очередь и поставить инфраструктурный blocker эРэФии выше Telegram Phase1B
СТАТУС: ready_for_address_delivery
