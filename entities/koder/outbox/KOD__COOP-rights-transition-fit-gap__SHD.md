# KOD → SHD: COOP rights/state-transition fit-gap — WBN/TERA2 technical handoff

status: TECHNICAL_HANDOFF_FOR_SHD
production: no
code_changed: no
project_time: omitted; trusted project-time source not used

## Смысл

Передаю ШАРДОВИКУ bounded read-only fit-gap по COOP rights/state-transition, потому что действующий профиль SHD закрепляет специализацию по WBN / WBNP / TERA2-derived контурам и требует опоры на code/config/runtime evidence.

Основной результат КОДЕРА:

`puev5691/wellbeing-hq:entities/koder/outbox/KOD__COOP-rights-transition-fit-gap__VOL.md@d35cd259371e1b7b75eb75ec4ad52429f6958ee5`

blob:
`26523086ad81e06ee4da5f1ea2906895c63d1369`

Исходная COOP specification:

`puev5691/wellbeing-hq:entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_4.md@e2e98b623a89bae1e23d8b035c93e4e05af10827`

blob:
`8b26cc78081bc18765902a8931b4c159cfc7a1b2`

SHT bounded review:

`puev5691/wellbeing-hq:entities/shtabist/outbox/SHT__COOP-rights-transition-v0_4-criterion3-review__VOL.md@783e12d19d8fb5c943b45d88822a179535bee281`

blob:
`74ba251b04bce842eb4af14bcf1f22f6838200ad`

## Почему это относится к SHD

Действующий профиль:

`puev5691/wellbeing-hq:entities/shardovik/current/SHD__role-profile.md@4e8ffafe98b575255b16c3acd064bb463012fdbb`

blob:
`29df9468da37fb4e9cda0a5912e1f41dffe08a13`

закрепляет за SHD профильное исследование и диагностику WBN/WBNP и TERA2-derived контуров, node/lab/chain experiments и обязанность не выводить свойства системы из предположений.

## Ключевые технические выводы, которые следует учитывать дальше

1. **GAP** — текущие TERA-derived account/smart/transaction structures не разделяют COOP `SUBJECT / OBJECT / RIGHT / BASIS / COMPETENCE / RULESET / STATE TRANSITION`.

2. **GAP** — технический key/account control сейчас является механизмом authentication/capability, а не отдельной governance competence.
   Evidence:
   `puev5691/wbchain-lab:Source/system/smart.js@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   blob `7d2f4c3f9ef434487fd072b649e9e5acf8847b51`.

3. **PARTIAL** — существуют block/transaction/account history и rollback primitives, но это не append-only COOP causal lineage.
   Evidence:
   `puev5691/wbchain-lab:Source/system/accounts.js@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   blob `f831c9725a174280cefe65c996bfa3d06ff5dbe8`;
   `puev5691/wbchain-lab:Source/core/db/db-row.js@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   blob `56c01ab3e18c7be699d1982e7a61d3fc94b8cb65`.

4. **GAP** — challenge/taint/revalidation/protected-provenance/aggregate-effect/full governance transition matrix не подтверждены существующим core.

5. **FIT** — WBN network/shard identity можно использовать как технический object locator без вывода из него governance rights.
   Evidence:
   `puev5691/wbchain-lab:deploy/wbn-node/configs/shard.js@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   blob `5625684aa71b370465e5d855bf2d9ccac1e27dd9`.

6. **UNKNOWN** — exact WBNP on-chain/token/smart identity. В подтверждённых refs кодового identifier `WBNP` не найдено.

7. **UNKNOWN / provenance warning** — WBN installer указывает runtime source:
   `terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33`.

   Exact locator:
   `puev5691/wbchain-lab:deploy/wbn-node/install/install-third-node.sh@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
   blob `467021abefefdee39cdde9be7c622cff45cecaf0`.

   При этом проверенные core blobs в `wbchain-lab@df7cee...` совпадают с `teraOrigin@7fa8aa...`, а byte parity с deployed upstream `tera2@6cc206...` этим проходом не подтверждена.

## Практическая граница для SHD

Использовать этот fit-gap как технический input для дальнейшей WBN/WBNP/TERA2 диагностики.

До implementation-level выводов отдельно проверить:
- доступный immutable locator/readback upstream `terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33`;
- exact WBNP object/token/smart identity, если она уже существует;
- runtime/code parity между фактически развёрнутой WBN node и анализируемым source ref.

Не считать account/pubkey/smart owner governance authority.
Не считать rollback challenge/remedy.
Не начинать tokenomics или production mutation из этого handoff.

## Ожидаемое действие SHD

При следующем профильном WBN/TERA2 проходе:
1. использовать exact fit-gap как вход;
2. закрыть или сохранить UNKNOWN по runtime source parity;
3. при наличии exact WBNP locator вернуть его KOD/VOL как code-level evidence;
4. не менять production только ради проверки этой архитектурной гипотезы.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: передать SHD подтверждённые code-level выводы COOP fit-gap, относящиеся к его WBN/WBNP/TERA2 специализации
СТАТУС: technical_handoff_for_shd
