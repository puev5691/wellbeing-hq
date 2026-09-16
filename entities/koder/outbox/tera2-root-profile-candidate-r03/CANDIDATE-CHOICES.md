# TERA2 root-profile r0.3 — correction-only candidate

Эта версия исправляет только два SHD blocker-а r0.2.

## Сохранённые policy choices

Без изменений относительно immutable r0.2:
- `MODE_RUN=WBN_ROOT` как common tracked selector;
- `NETWORK=WELLBEING`, `SHARD_NAME=ROOT`, `NETWORK_ID=WELLBEING.ROOT`;
- fixed review-only `START_NETWORK_DATE=1800000000000` и reissue policy;
- `CONSENSUS_PERIOD_TIME=3000` и существующий r0.2 schedule;
- 100% `TOTAL_SUPPLY_TERA=1e9` в system reserve account 0, accounts 1..15 zero;
- founder/developer preallocation = 0;
- upstream built-in `GenesisSmartCreate()` retained;
- reward policy r0.2, включая `START_MINING=16`, `NEW_FORMULA_KTERA=3`, `NEW_FORMULA_JINN_KTERA=3`.

## Correction A — common selector

`MODE_RUN` удалён из свободного node-local config. Node-local example содержит только ссылку `root-profile.json#mode_run`; verifier запрещает `MODE_RUN` в node-local слое и negative fixture доказывает fail-closed поведение.

## Correction B — full policy proof

`POLICY-MAP.json` машинно классифицирует каждый leaf common-policy field. Verifier требует exact leaf coverage и доказывает source assignments, derived identity, upstream constants, genesis accounts 0..15, patch invariants, policy-only boundaries, pinned source identities и declared post-patch identities.

Никакой launch authority эта коррекция не создаёт.
