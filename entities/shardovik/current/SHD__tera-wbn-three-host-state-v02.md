# SHD / ШАРДОВИК — состояние TERA/WBN трёх хостов v0.2

status: ACTIVE_OPERATOR_DIRECTION
entity: SHD / ШАРДОВИК
production_mutation: no
project_time: omitted; trusted project-time source not used

## Подтверждённая топология

ОПЕРАТОР подтвердил исторический кластер из трёх WBN/TERA-нод: Буржуиния, эРэФия и МАЖОР.

Текущая рабочая архитектура:
- Буржуиния — опорная совместимая WBN-нода;
- эРэФия — восстановить как вторую опорную совместимую WBN-ноду;
- МАЖОР — экспериментальная нода для переработки и ребрендинга платформы под БЛАГОПОЛУЧИЕ.

## Буржуиния

Remote Desktop Commander: online.
Host: `ruvds-xnqc6`.
WBN service: active/enabled.
Source commit: `6cc2061c12986bbaea182786c42d89fd979eeb33`.
NETWORK: `WELLBEING`.
SHARD_NAME: `WBN`.
START_NETWORK_DATE: `1778186522932`.
Active DATA/shard.js SHA-256: `135a10d2c816df349f37ce47afd863a14b7db978e4e93dcce717b3dad83fdf3c`.
Current API check: `MaxNumBlockDB=3732522`, `CurBlockNum=3732525`, VersionNum `2653`.
GetNodeList: empty at check boundary.

## эРэФия

Exact public locator confirmed by OPERATOR screenshot: `194.87.107.135`.
Hosting panel identifies Ubuntu 24.04 LTS, 2 GiB RAM, 40 GiB HDD, one public IP; administrative login exists. Password is secret and is not stored in GitHub.

Read-only network verification from Буржуиния:
- ICMP: PASS;
- TCP/22: connection refused;
- TCP/30000: OPEN;
- TCP/8780: OPEN;
- TCP/8781: unavailable at check boundary;
- TCP/8080: unavailable at check boundary.

Public WBN API on `194.87.107.135:8780` confirms:
- NETWORK=`WELLBEING`;
- SHARD_NAME=`WBN`;
- VersionNum=`2653`;
- FIRST_TIME_BLOCK=`1778186522932`;
- CONSENSUS_PERIOD_TIME=`3000`;
- MaxAccID=`22`;
- MaxDappsID=`4`;
- CurBlockNum=`3732525`;
- MaxNumBlockDB=`3442593`.

Thus the node is live but its persisted blockchain DB is about 290k blocks behind Буржуиния at this check boundary.
GetNodeList is empty.

Hosted `/shard.js` on эРэФия:
- size 2176 bytes;
- SHA-256 `efba585a002fb6917dd72a1da82ba4e1de54d85d193c7480dff566694b449a91`.

Semantic diff against Буржуиния shows the same chain-defining logic: identical NETWORK, SHARD_NAME, START_NETWORK_DATE, CONSENSUS_PERIOD_TIME, START_HISTORY, START_MINING, seed `185.39.19.240:30000`, genesis account logic, genesis smart, WBN development/miner rewards, PRICE_DAO and development public key. Differences observed are comments and formatting only.

## МАЖОР

Remote Desktop Commander: online.
Host: `p552203.kvmvps`.
Ubuntu 24.04.1 LTS, 1 vCPU, ~1.9 GiB RAM, 30 GiB disk, no swap at preflight.
TERA/WBN service absent; ports 30000/8780/8781/8080 free at preflight.
Role: experimental node. It must not become source of a new genesis/chain identity without separate OPERATOR decision.

## Operational conclusion

The historical WBN chain is positively identified on both Буржуиния and эРэФия.
The immediate blocker is no longer host identity: эРэФия is reachable and its WBN node is live. The remaining infrastructure blocker is administrative access: SSH port 22 refuses connections and Remote Desktop Commander is not registered/online on эРэФия.

Before incompatible experiments on МАЖОР:
1. restore administrative access to эРэФия without altering WBN runtime;
2. perform local read-only inventory of service/source/DATA/const.lst;
3. restore peer connectivity Буржуиния ↔ эРэФия;
4. let эРэФия catch up to Буржуиния and verify equal chain state;
5. preserve recovery evidence for both compatibility nodes;
6. then move incompatible development to МАЖОР.

## Safety boundary

Do not publish credentials/private keys/wallet secrets. Do not replace START_NETWORK_DATE, genesis/reward logic, DATA/DB or shard identity on either compatibility node before recovery evidence exists. Do not auto-update upstream beyond exact verified source commit during cluster recovery.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: зафиксировать подтверждённое состояние трёххостового WBN/TERA контура после обнаружения живой эРэФии
СТАТУС: active_operator_direction_erefia_live_admin_access_pending
