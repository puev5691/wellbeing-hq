# TERA2 root-profile r0.2 — upstream evidence

Основание исследования: `SHD__tera2-main-genesis-root-research-r01__KOO.md`, commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`, verdict `PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`.

Exact upstream: `https://gitlab.com/terafoundation/tera2.git` commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.
В текущей candidate-работе `git ls-remote origin HEAD` также вернул этот commit.

Проверенные upstream-факты:
- root/main path не требует `DATA/shard.js`; наличие `DATA/shard.js` переключает на shard profile;
- default mode — `MAIN_JINN`; upstream также имеет `TEST_JINN` и `DEV_JINN`, но не готовый custom production-like root mode;
- `BLOCK_GENESIS_COUNT = BLOCK_PROCESSING_LENGTH2 = 16`;
- `TOTAL_SUPPLY_TERA = 1e9`;
- пустая DB вызывает встроенный root genesis block/state path;
- встроенный `GenesisAccountCreate()` по умолчанию распределяет 95% system account и 5% founder account;
- встроенный coinbase использует `START_MINING` и формульные constants из `constant.js`/`const-mode.js`;
- node-local IP/ports/mining execution не должны становиться общей chain identity.
