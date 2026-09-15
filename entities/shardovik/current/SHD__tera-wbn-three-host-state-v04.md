# SHD / ШАРДОВИК — состояние TERA/WBN трёх хостов v0.4

status: BLOCKED_CANONICAL_BRANCH_DECISION
entity: SHD / ШАРДОВИК
production_mutation: no
project_time: omitted; trusted project-time source not used
preflight_commit: bc5f801b55995bd2ab8f96e92aff0b70cf8535ff

## Что проверено

эРэФия `ruvds-ygo0w` восстановлена в Remote Desktop Commander как отдельное устройство `c55d5659-f2c8-416d-8b40-9bac8c80c30d`; после detach от SSH/tmux отвечает прямым DC `ping`.

Локальный WBN service на эРэФии:
- `wbn-tera2-node.service`: active + enabled;
- `/usr/bin/node`: `v18.19.1`;
- `ExecStart=/usr/bin/node run-node.js NOPSWD NOAUTOUPDATE`;
- source: `/home/pev5691/wbn-tera2-lab/tera2`;
- upstream commit: `6cc2061c12986bbaea182786c42d89fd979eeb33`;
- ports `30000`, `8780`, `8781`: LISTEN;
- `DATA/shard.js`: 2176 bytes, sha256 `efba585a002fb6917dd72a1da82ba4e1de54d85d193c7480dff566694b449a91`;
- `DATA/const.lst`: 1561 bytes, sha256 `31f444e9388e2fcd8a98a84790a42f2da34069da21d42a845c6d33985529996d`;
- identity: `NETWORK=WELLBEING`, `SHARD_NAME=WBN`, `START_NETWORK_DATE=1778186522932`;
- `JINN_IP=194.87.107.135`, `JINN_PORT=30000`, `NODES_NAME=EREFIA`, `MINING_ACCOUNT=9`.

На момент проверки локальная DB эРэФии уже догнала текущую высоту. `GetNodeList` на обеих нодах возвращает пустой `arr=[]`. TCP `30000` открыт в обе стороны между Буржуинией и эРэФией. Следовательно, текущая проблема не является простым сетевым firewall-blocker.

## Критический результат: обнаружен fork

Буржуиния и эРэФия имеют одну историю только до блока `2984033` включительно.

Последний общий блок:
- height: `2984033`;
- hash: `ece8a1f293b9e84818fa48864c1da6265260b3b70ebdcf93ada0424a6dbb9e1e`;
- Miner `9`, Power `14`, SumPow `40632303`.

Первый различающийся блок `2984034`:
- Буржуиния: hash `795051c9b25717aef1dff607877e1a4cab6a1ba48118add5010beb1af7aa6f97`, Miner `0`, Power `0`, SumPow `40632303`;
- эРэФия: hash `ee5f4833c90f74248351976fa4aaaf7b8b2dcf19141bc34f024e091b2bb4d063`, Miner `9`, Power `13`, SumPow `40632316`.

На контрольной высоте `3757200` ветки по-прежнему различаются. Там cumulative work уже выше у Буржуинии:
- Буржуиния SumPow `49175696`;
- эРэФия SumPow `46800713`.

## Состояние счетов также разошлось

Различия подтверждены текущим `GetAccountList`, поэтому fork затрагивает не только block headers / PoW.

Примеры `SumCOIN`:
- account 0 `WBN System`: Буржуиния `985329438`, эРэФия `985891624`;
- account 1 `WBN Genesis`: Буржуиния `3778122`, эРэФия `3778130`;
- account 2: Буржуиния `6296114`, эРэФия `4333274`;
- account 9: Буржуиния `4153404`, эРэФия `5554050`.

## Стоп-условие

Нельзя безопасно просто соединить две ноды или сбросить одну из DB: это может уничтожить одну из реально существующих веток и её состояние счетов.

До решения ОПЕРАТОРА никакие production/data mutations, reset DB, history replace, service restart ради reorg или изменение chain identity не выполняются.

Технический кандидат на canonical branch: Буржуиния, потому что она является configured seed и на проверенной современной высоте имеет существенно больший cumulative SumPow. Это рекомендация, не утверждённое решение.

## Требуемое решение ОПЕРАТОРА

Выбрать политику сохранения истории:
1. принять ветку Буржуинии как canonical WBN и сохранить эРэФию как архивную копию перед синхронизацией;
2. принять ветку эРэФии как canonical WBN;
3. сначала сохранить полные immutable snapshots обеих DATA/DB и провести дополнительный сравнительный аудит транзакций/наград после fork, затем выбрать canonical branch.

Рекомендуемый безопасный вариант: `3`, затем при отсутствии содержательных пользовательских транзакций после fork — canonical Буржуиния.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: зафиксировать verified fork и остановить разрушительное автоматическое восстановление кластера
СТАТУС: BLOCKED_CANONICAL_BRANCH_DECISION
