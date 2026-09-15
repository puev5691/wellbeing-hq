# SHD → KOO: TERA2 main/root genesis research r0.1

status: `PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`
production: `no`
runtime_mutation: `no`
project_time: omitted; trusted project-time source not used

## Краткий результат

Механизм различения main/root и shard mode в текущем upstream TERA2 проверен по exact upstream `https://gitlab.com/terafoundation/tera2.git` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`. Во время исследования `git ls-remote origin HEAD` вернул тот же commit. Новый genesis фактически не создавался, runtime и DATA старого WBN не изменялись.

Ключевой вывод: для main/root path `DATA/shard.js` отсутствует. При его отсутствии `Source/core/constant.js` передаёт управление встроенному `Source/core/const-mode.js`; при наличии `DATA/shard.js` файл исполняется как shard init profile. Это прямо совпадает с `Doc/Rus/sharding-spec.md`, где наличие `DATA/shard.js` при обычном `node run-node.js` описано как запуск шарда.

Однако upstream не содержит готового отдельного режима «создать новую именованную production-like root chain». Встроены только `MAIN_JINN`, `TEST_JINN`, `DEV_JINN`. Поэтому root/genesis machinery установлен, но exact профиль новой корневой сети БЛАГОПОЛУЧИЯ должен быть определён и проверен до будущего launch gate.

## 1. Fresh GitHub-preflight и exact input

Fresh preflight `puev5691/wellbeing-hq` выполнен в начале задачи:
- observed HEAD: `86f20e82a3b289488dff7deb367841b761739c07`;
- во время исследования параллельная работа других Сущностей продвинула HEAD, но exact task pinned commit не изменился и path-conflict с SHD result не обнаружен.

Exact input:
- inbox pointer: `entities/shardovik/inbox/KOO__tera2-main-genesis-root-research-r01__SHD.md`;
- source artifact: `entities/koordinator/outbox/KOO__tera2-main-genesis-root-research-r01__SHD.md`;
- exact task commit: `31a283417df2d499882456771cf0f70b0427bb71`.

## 2. Проверенная upstream-граница main/root против shard mode

Exact code evidence на commit `6cc2061...`:

- `Source/run-node.js:3` задаёт default `MODE_RUN="MAIN_JINN"`.
- `Source/core/constant.js:233-235`: вычисляется `DATA/shard.js`; если файл существует, выполняется `runcode(ShardParamPath)`; иначе загружается `const-mode.js`.
- `Source/core/const-mode.js:12-15`: `DEV_JINN` → `NETWORK="LOCAL-JINN"`, `SHARD_NAME="TERA"`, `LOCAL_RUN=1`.
- `Source/core/const-mode.js:84-87`: `MAIN_JINN` → `NETWORK="MAIN-JINN"`, `SHARD_NAME="TERA"`.
- `Doc/Rus/sharding-spec.md`: уникальные настройки шарда помещаются в `DATA/shard.js`; если он есть, стандартный `node run-node.js` фактически запускает шард.

Следствие: переменная `SHARD_NAME` сама по себе не доказывает shard-mode. Даже main TERA использует `SHARD_NAME="TERA"`. Проверяемый operational discriminator для старой схемы — именно branch загрузки через `DATA/shard.js` против встроенного `const-mode.js`.

## 3. Как root genesis создаётся в коде

На пустой DB TERA2 имеет встроенный genesis path, не требующий `DATA/shard.js`:

- `Source/core/constant.js` задаёт `BLOCK_PROCESSING_LENGTH2=16`, следовательно `BLOCK_GENESIS_COUNT=16`.
- `Source/jinn/src/jinn-block-db.js:40` определяет `Engine.WriteGenesisDB()`, который записывает блоки `0..15` через `Engine.GetGenesisBlock()`.
- `Source/jinn/tera/tera-hash.js:41-43` переопределяет TERA genesis block construction через `SERVER.GenesisBlockHeaderDB(BlockNum)`.
- `Source/jinn/tera/tera-link-server.js:651+` формирует genesis headers; для раннего режима учитывается `DEVELOP_PUB_KEY0`.
- `Source/system/common-tx.js`: на block `1` вызывается `COMMON_ACTS.ClearDataBase()`, что инициирует genesis state.
- `Source/system/accounts.js:195-206`: если нет `SHARD_PARAMS.GenesisAccountCreate`, используется встроенный `GenesisAccountCreate()`.
- `Source/system/smart.js:278-284`: если нет `SHARD_PARAMS.GenesisSmartCreate`, используется встроенный `GenesisSmartCreate()`.

То есть root chain имеет собственный встроенный genesis block/state path. Старый WBN подменял его shard-specific callbacks из `DATA/shard.js`; это для нового main/root bootstrap переносить нельзя.

## 4. Минимальная проверенная поверхность chain identity

Для будущих 2-3 root nodes должны быть идентичны как минимум следующие элементы.

### 4.1 Immutable code/profile identity

- exact source/fork commit;
- отсутствие `DATA/shard.js`;
- exact root mode implementation в `const-mode.js` либо эквивалентном tracked source profile;
- одинаковые consensus/protocol schedule constants, включая блоковые пороги и формулы, влияющие на обработку блоков и state.

Запуск stock `MAIN_JINN` не подходит для новой сети: это профиль существующей публичной TERA с историческим `NETWORK="MAIN-JINN"`, `SHARD_NAME="TERA"`, fixed update heights и hard-coded public TERA bootstrap nodes.

Stock `DEV_JINN` также не является готовым production-like root profile: он создаёт `LOCAL-JINN.TERA`, включает dev/local behavior и имеет localhost bootstrap behavior.

### 4.2 Temporal identity

- один exact `START_NETWORK_DATE` для всех узлов;
- один `CONSENSUS_PERIOD_TIME`.

Это критично. `Source/core/startlib.js:97+` показывает: если `START_NETWORK_DATE` не задан и DB ещё нет, `FindBlockchainStartTime(1)` вычисляет начало относительно `Date.now()`. Независимый авторасчёт на разных машинах не должен использоваться как воспроизводимый cluster genesis contract. В будущем root manifest должен фиксировать exact start timestamp до запуска.

### 4.3 Network/P2P identity

- exact `NETWORK`;
- exact `SHARD_NAME`/root label;
- следовательно exact `NETWORK_ID = NETWORK + "." + SHARD_NAME`.

JINN handshake передаёт Network и Shard отдельно (`Source/jinn/src/jinn-connect-handshake.js`), поэтому все root nodes должны иметь один и тот же root identity.

### 4.4 Genesis state identity

Default non-shard path использует tracked source logic:
- `TOTAL_SUPPLY_TERA=1e9`;
- встроенные `ARR_PUB_KEY` / `DEVELOP_PUB_KEY0` из `Source/core/crypto-library.js`;
- `GenesisAccountCreate()` в `Source/system/accounts.js`;
- `GenesisSmartCreate()` в `Source/system/smart.js`.

Для новой сети БЛАГОПОЛУЧИЯ exact public genesis keys, allocations, supply и initial smart state должны быть отдельным утверждённым manifest/profile. Private keys/secrets в этот research не извлекались и не должны попадать в GitHub.

### 4.5 Node-local параметры, которые не следует смешивать с chain identity

`JINN_IP`, listen/public IP, node/wallet name, HTTP ports, локальные mining CPU settings, log paths и service unit являются node-local runtime configuration. Они могут различаться между хостами при неизменной root chain identity.

Bootstrap peer addresses также относятся к connectivity/bootstrap, а не к genesis hash. Upstream умеет добавлять и сохранять system peer через `HTTPCaller.AddSetNode()` и `jinn-nodes-*.lst`, но exact будущий bootstrap procedure должен быть выбран отдельно и проверен под launch gate.

## 5. Что из старого WBN shard experiment нельзя переносить

В новый root/main bootstrap нельзя переносить как chain-defining механизм:

1. старые `DATA/shard.js` с `NETWORK=WELLBEING`, `SHARD_NAME=WBN`, `START_NETWORK_DATE=1778186522932`;
2. `SHARD_PARAMS.SeedServerArr` как способ определения root identity;
3. `SHARD_PARAMS.GenesisAccountCreate` старого WBN;
4. `SHARD_PARAMS.GenesisSmartCreate` старого WBN;
5. `SHARD_PARAMS.DoCoinBaseTR` и старую reward policy как неявное наследие;
6. старые WBN DATA/DB, block history, account state, `jinn-nodes-*.lst`;
7. старый `const.lst` целиком — из него допустимо переносить только осознанно выбранные node-local operational values после review, но не chain identity по принципу «как было».

Старые fork branches сохраняют исследовательскую ценность, но не являются genesis source нового root cluster.

## 6. Почему verdict не полный PASS

Root/genesis machinery verified, но upstream не даёт готовый production-like custom root profile. Перед будущим launch остаются exact unknowns, которые должны быть превращены в один tracked root-profile artifact:

1. exact новое `NETWORK`;
2. exact root `SHARD_NAME`/label;
3. exact fixed `START_NETWORK_DATE`;
4. exact consensus/update schedule для сети, начинающейся с height 0, без исторических MAIN_JINN порогов;
5. exact genesis public keys, supply/allocation и initial smart state;
6. exact reward/mining policy с block 0/начала mining;
7. exact bootstrap strategy для 2-3 первых root nodes;
8. решение, в каком tracked source месте хранить новый dedicated root mode, не используя `DATA/shard.js`.

Критически: использование stock `DEV_JINN` как финального root profile без отдельного review не подтверждено. Он полезен как upstream proof, что non-shard clean genesis path существует, но содержит dev/local semantics.

## 7. Bounded reproduction/deployment plan для будущего launch gate

Ниже только план, ничего из этого в текущей задаче не запускалось.

### Stage 1 — root-profile candidate

KOD готовит минимальный tracked source candidate на exact upstream/fork base:
- dedicated root mode в `const-mode.js` или эквивалентном tracked source file;
- `NETWORK`, root label, fixed start date, consensus/update schedule;
- genesis account/smart/reward public configuration;
- без `DATA/shard.js`;
- без secrets/private keys.

Результат должен иметь immutable commit + manifest/checksums.

### Stage 2 — clean-node package preflight

Для каждого будущего узла, до первого запуска:
- отдельный новый runtime/data directory, не поверх WBN;
- exact same source/root-profile commit;
- empty new DATA/DB;
- assert `DATA/shard.js` absent;
- разделить common chain manifest и per-node operational config;
- зафиксировать одинаковый root-profile hash на всех узлах.

### Stage 3 — future authorized launch

Только отдельным launch authority:
- node-1 создаёт clean root genesis;
- node-2 запускается с тем же immutable profile и fixed temporal identity;
- node-3 добавляется только после PASS пары;
- bootstrap peer addresses добавляются явным проверяемым способом, а не наследуются из старой WBN DB.

### Stage 4 — restart/rejoin test

После общей цепи:
- controlled restart каждого узла;
- temporary disconnect одного узла;
- rejoin/catch-up;
- повторное сравнение block/state identity.

Только после PASS этой root phase можно открывать отдельный shard experiment.

## 8. Критерии доказательства одной main/root chain для 2-3 узлов

Будущий PASS требует одновременно:

1. identical exact source/root-profile commit и manifest hash;
2. `DATA/shard.js` отсутствует на каждом root node;
3. `GetCurrentInfo` на всех узлах показывает одинаковые `NETWORK`, `SHARD_NAME`, `FIRST_TIME_BLOCK`, `CONSENSUS_PERIOD_TIME` и совместимую code version;
4. hashes genesis blocks `0..15` совпадают byte-for-byte;
5. genesis accounts/smarts и supply state совпадают после genesis processing;
6. на нескольких одинаковых finalized heights совпадают `Hash`, `SumHash`, `SumPow` и block transaction identity;
7. account/state checksums или проверенный набор account records совпадает на одном finalized height;
8. доказана реальная P2P связь, а не только open TCP: минимум одна established JINN session между intended peers; `GetNodeList` используется только как дополнительное evidence, не единственное;
9. второй/третий узел догоняет node-1 без появления альтернативной ветки;
10. после controlled restart/rejoin контрольные hashes и state продолжают совпадать.

Любое различие genesis blocks, temporal identity или state является fail-closed blocker и запрещает переход к shard phase.

## 9. Exact verdict

`PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`

Механизм main/root genesis verified: clean non-shard path = no `DATA/shard.js` + tracked root mode + empty DB, после чего JINN/TERA создаёт встроенные genesis blocks/state. Но для новой сети отсутствует готовый upstream custom-production root profile, поэтому запуск до определения exact unknowns выше был бы недостоверным.

## 10. Один рекомендуемый следующий bounded шаг

KOO → KOD: открыть **одну design-only/code-candidate задачу без runtime launch** — подготовить tracked dedicated root-mode candidate + machine-readable root genesis manifest на base `6cc2061c12986bbaea182786c42d89fd979eeb33`, без `DATA/shard.js`, без secrets и без запуска node; затем вернуть SHD для независимой read-only verification до launch authority.

## Boundary confirmation

- старые WBN services не останавливались;
- WBN DATA/DB не изменялись и не удалялись;
- новый genesis не создавался;
- новый runtime не запускался;
- Буржуиния/эРэФия/МАЖОР не изменялись;
- использовались только read-only GitHub/upstream/code/docs проверки;
- secrets/private keys не извлекались и не маршрутизировались.

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: вернуть КООРДИНАТОРУ bounded read-only research механизма нового TERA2 main/root genesis
СТАТУС: PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH
