# SHD / ШАРДОВИК — стратегия TERA/WBN для трёх хостов v0.1

status: ACTIVE_OPERATOR_DIRECTION
entity: SHD / ШАРДОВИК
production_mutation: no
project_time: omitted; trusted project-time source not used

## Решение ОПЕРАТОРА

ОПЕРАТОР подтвердил историческую топологию из трёх WBN/TERA-нод: Буржуиния, эРэФия и МАЖОР ранее входили в один синхронизированный кластер.

Новая рабочая схема:
- Буржуиния — опорная совместимая WBN-нода;
- эРэФия — восстановить как вторую опорную совместимую WBN-ноду;
- МАЖОР — использовать как экспериментальную ноду для переработки, ребрендинга и проверки будущей платформы БЛАГОПОЛУЧИЕ.

## Подтверждённое текущее состояние

Буржуиния `ruvds-xnqc6` доступна через Remote Desktop Commander и имеет работающую WBN TERA2-ноду:
- upstream `https://gitlab.com/terafoundation/tera2.git`;
- source commit `6cc2061c12986bbaea182786c42d89fd979eeb33`;
- `NETWORK=WELLBEING`;
- `SHARD_NAME=WBN`;
- P2P `30000`;
- hosting `8780`;
- API/admin layer `8781`;
- active `DATA/shard.js` SHA-256 `135a10d2c816df349f37ce47afd863a14b7db978e4e93dcce717b3dad83fdf3c`.

МАЖОР `p552203.kvmvps` доступен через Remote Desktop Commander и оставляется экспериментальным контуром. На момент фиксации TERA/WBN service там не установлен, порты `30000/8780/8781/8080` свободны.

эРэФия в текущем `list_devices` Remote Desktop Commander отсутствует. В текущем GitHub-поле `wellbeing-hq` технический locator эРэФии по именам файлов/дерева не найден. Нельзя угадывать IP/device-id/hosting object.

## Целевая архитектура

### Опорный контур совместимости

Буржуиния + эРэФия должны быть восстановлены как две ноды одной существующей WBN-цепи с byte-identical chain identity `DATA/shard.js`, одинаковым upstream commit и подтверждённой взаимной P2P-связью.

До завершения восстановления эРэФии Буржуиния не подвергается несовместимым изменениям исходников, identity layer или базы.

### Экспериментальный контур

МАЖОР выводится из требований полной совместимости с legacy runtime после создания проверяемой точки восстановления и используется для:
- переработки deployment bundle;
- удаления legacy-патчей и привязок к старым путям/пользователям;
- безопасного ребрендинга интерфейсов и терминологии;
- выделения стабильного API-контракта БЛАГОПОЛУЧИЯ;
- экспериментов с runtime, storage, security и service layout;
- подготовки варианта глубокой переработки TERA2 под требования проекта.

МАЖОР не должен становиться источником нового genesis/новой chain identity без отдельного решения ОПЕРАТОРА.

## Порядок работ

1. Восстановить инфраструктурную доступность эРэФии без изменения TERA/WBN.
2. Выполнить SHD read-only inventory эРэФии: host identity, service, source commit, `DATA/shard.js`, `const.lst` allowlist, ports, API, DB height, resource state.
3. Сравнить эРэФию с Буржуинией по immutable identity и текущему block state.
4. Если chain identity совпадает — безопасно запустить/восстановить service эРэФии и добиться двухстороннего P2P peer state.
5. Зафиксировать двухузловой опорный кластер и recovery evidence.
6. Только после этого начинать несовместимые эксперименты на МАЖОРе.

## Границы

Без отдельного шага не выполнять:
- новый genesis;
- замену `START_NETWORK_DATE`;
- изменение reward/genesis logic действующей WBN-цепи;
- перенос private keys/wallet secrets через GitHub;
- destructive cleanup Буржуинии/эРэФии;
- автоматическое обновление upstream на иной commit;
- применение legacy `wellbeing`/`wbn2026` fork configs как production-конфигурации.

## Текущий blocker

`BLOCKED_EREFIA_INFRASTRUCTURE_LOCATOR_OR_REMOTE_ACCESS_NOT_AVAILABLE`

Следующий разрешённый шаг: инфраструктурно вернуть эРэФию в доступный контур и передать SHD проверяемый remote locator/device access для read-only inventory.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: зафиксировать новую трёххостовую стратегию TERA/WBN после решения ОПЕРАТОРА
СТАТУС: active_operator_direction_waiting_erefia_access
