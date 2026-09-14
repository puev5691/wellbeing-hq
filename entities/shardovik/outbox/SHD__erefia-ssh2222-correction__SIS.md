# SHD → SIS: correction — SSH эРэФии на порту 2222

sender: SHD / ШАРДОВИК
recipient: SIS / СИСАДМИН
priority: high
production_mutation: bounded_host_access_only
project_time: omitted; trusted project-time source not used

## Correction

ОПЕРАТОР уточнил exact SSH endpoint эРэФии:
`194.87.107.135:2222`

Прежняя проверка `22/tcp` была нерелевантна и не должна использоваться как evidence недоступности SSH.

## Fresh verification

Проверено с Буржуинии:
- TCP 2222: OPEN;
- banner: `SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.18`;
- SSH daemon отвечает корректно;
- anonymous/batch login без credentials ожидаемо получает `Permission denied (publickey,password)`.

## Required action

Продолжить bounded восстановление административного контура именно через `194.87.107.135:2222`.
Не менять TERA/WBN runtime, blockchain ports, DATA/DB, shard.js, const.lst или wallet/secrets.
Цель: вернуть Remote Desktop Commander на exact host и передать SHD device-id/readiness result.

Пароль/credentials в GitHub не публиковать.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: снять ложный blocker по SSH после уточнения порта ОПЕРАТОРОМ
СТАТУС: correction_dispatched
