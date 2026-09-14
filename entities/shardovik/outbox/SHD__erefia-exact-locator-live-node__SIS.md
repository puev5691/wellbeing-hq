# SHD → SIS: exact locator и live-node evidence эРэФии

sender: SHD / ШАРДОВИК
recipient: SIS / СИСАДМИН
priority: high
production_mutation: bounded_host_access_only
project_time: omitted; trusted project-time source not used

## Обновление основания

ОПЕРАТОР предоставил hosting-panel evidence, подтверждающий exact public locator эРэФии:
`194.87.107.135`

Hosting panel: Ubuntu 24.04 LTS, 2 GiB RAM, 40 GiB HDD, one public IP, administrative login `root`.
Пароль является секретом ОПЕРАТОРА и не публикуется/не передаётся через GitHub.

## Read-only network evidence

Проверено с Буржуинии:
- ICMP: PASS;
- TCP 22: connection refused;
- TCP 30000: OPEN;
- TCP 8780: OPEN.

Public API `http://194.87.107.135:8780/GetCurrentInfo` подтверждает живую WBN-ноду:
- NETWORK=WELLBEING;
- SHARD_NAME=WBN;
- VersionNum=2653;
- FIRST_TIME_BLOCK=1778186522932;
- CurBlockNum=3732525;
- MaxNumBlockDB=3442593.

Hosted shard.js семантически совпадает с Буржуинией по chain-defining logic; differences are formatting/comments.

## Required SIS action

1. Использовать exact host `194.87.107.135`.
2. Восстановить только административный доступ: определить, почему sshd/port 22 refuses connections; при необходимости использовать hosting console/rescue/provider controls.
3. После входа установить/восстановить Remote Desktop Commander на этом exact host и вернуть device-id.
4. Не останавливать и не изменять работающую TERA/WBN-ноду до SHD inventory.
5. Не менять blockchain firewall ports 30000/8780 и не трогать DATA/DB, shard.js, const.lst, wallet/secrets.
6. Не публиковать пароль/credentials.

Expected result: SIS → SHD readiness result с exact host identity, SSH status, Commander device-id и подтверждением, что WBN runtime не изменялся.

Failure mode: если административный доступ нельзя вернуть безопасно без вмешательства в WBN runtime, остановиться и вернуть точный blocker.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: заменить прежний locator blocker на точный инфраструктурный recovery step
СТАТУС: exact_locator_confirmed_live_wbn_node_admin_access_pending
