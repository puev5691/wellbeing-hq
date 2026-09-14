# SHD / ШАРДОВИК — состояние TERA/WBN трёх хостов v0.3

status: ACTIVE_OPERATOR_DIRECTION
entity: SHD / ШАРДОВИК
production_mutation: no
project_time: omitted; trusted project-time source not used

## Исправление SSH-границы эРэФии

ОПЕРАТОР уточнил, что SSH эРэФии работает на порту `2222`, а не `22`.

Проверено с Буржуинии для exact host `194.87.107.135`:
- TCP `2222`: OPEN;
- SSH banner: `OpenSSH_9.6p1 Ubuntu-3ubuntu13.18`;
- batch login без credentials ожидаемо отвергнут `Permission denied (publickey,password)`;
- это подтверждает живой SSH daemon и корректный административный endpoint.

Прежний вывод `SSH_PORT_22_REFUSED` был следствием проверки неверного порта и больше не является blocker.

## Текущее подтверждённое состояние эРэФии

- host: `194.87.107.135`;
- Ubuntu 24.04 LTS;
- SSH: `194.87.107.135:2222`;
- WBN P2P `30000/tcp`: OPEN;
- WBN hosting `8780/tcp`: OPEN;
- `NETWORK=WELLBEING`;
- `SHARD_NAME=WBN`;
- `VersionNum=2653`;
- `FIRST_TIME_BLOCK=1778186522932`;
- current block height совпадает с Буржуинией;
- local DB height отстаёт примерно на 290k блоков на момент проверки;
- hosted `shard.js` семантически совпадает с Буржуинией по chain-defining logic, различия — комментарии/форматирование.

## Следующий шаг

Инфраструктурный blocker теперь сводится не к отсутствию SSH, а к необходимости вернуть Remote Desktop Commander на exact host и провести локальный read-only inventory без вмешательства в работающую WBN-ноду.

После появления Commander SHD проверяет локально service, source commit, const.lst allowlist, DATA/DB и P2P state, затем восстанавливает опорную пару Буржуиния ↔ эРэФия.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: исправить неверную SSH-границу эРэФии после уточнения ОПЕРАТОРА
СТАТУС: ssh_2222_verified_admin_endpoint_live
