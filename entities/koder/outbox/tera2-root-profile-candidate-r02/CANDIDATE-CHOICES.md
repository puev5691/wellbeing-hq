# TERA2 root-profile r0.2 — project candidate choices

Ниже не upstream-факты, а review-only выбор KOD для materialized candidate.

- `MODE_RUN=WBN_ROOT` как отдельный tracked root mode.
- `NETWORK=WELLBEING`, `SHARD_NAME=ROOT`, `NETWORK_ID=WELLBEING.ROOT`.
- `START_NETWORK_DATE=1800000000000` фиксирован намеренно и не получен из текущего времени. Если отдельный launch gate наступит после этого значения, profile должен быть переиздан.
- `CONSENSUS_PERIOD_TIME=3000` сохраняет проверенный upstream период.
- исторические MAIN_JINN update heights не наследуются; candidate schedule стартует от height 0/1 с explicit zero/one thresholds.
- genesis accounts: 100% `TOTAL_SUPPLY_TERA=1e9` в system reserve account 0; accounts 1..15 имеют zero initial balance; founder/developer preallocation отсутствует.
- built-in upstream `GenesisSmartCreate()` сохраняется без custom shard callback.
- reward policy включается начиная с block 16, то есть после 16 genesis blocks; runtime mining execution (`USE_MINING`) profile не включает.
- coinbase formula constants фиксируются в candidate как `KTERA=3`, без referral window (`REF_PERIOD_END=0`).

Нерешённые launch-зависимости:
- public bootstrap peers для первых 2–3 root nodes;
- future miner account creation/selection;
- SIS host/runtime preflight;
- SHD review block/state identity criteria;
- OPERATOR authority на clean genesis launch;
- отдельное решение о наименовании/экономике, если `WELLBEING.ROOT` или supply/reward policy будут изменены.
