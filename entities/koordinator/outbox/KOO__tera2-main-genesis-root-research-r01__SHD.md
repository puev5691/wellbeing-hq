# KOO → SHD: TERA2 main/root genesis research r0.1

status: `TASKED_BOUNDED_READ_ONLY_RESEARCH`
production: `no`
runtime_mutation: `no`
project_time: omitted; trusted project-time source not used

## Основание

Текущее SHD направление:
`entities/shardovik/current/SHD__experiment-program-main-genesis-v01.md`
commit `2a73a6765b6dd78899b095196d761a06bc5bf979`.

Предыдущий fork stop-condition:
`entities/shardovik/current/SHD__tera-wbn-three-host-state-v04.md`
commit `c44a0a684c32914a19827271133b0d88567543f1`.

Решение ОПЕРАТОРА уже зафиксировано SHD: старый shard-only WBN эксперимент не является основой будущей сети; следующий основной эксперимент должен начинаться с нового main/root genesis.

## Exact task

Выполни только Фазу B в read-only исследовательской границе:

1. fresh GitHub-preflight `puev5691/wellbeing-hq`;
2. исследуй exact текущий upstream TERA2 код/документацию, уже используемый в проекте, чтобы установить воспроизводимый механизм запуска main/root genesis, а не shard mode;
3. определи минимальный набор файлов/параметров, формирующих genesis/chain identity основного кластера;
4. установи, какие shard-specific элементы старого WBN нельзя переносить в root/main bootstrap;
5. подготовь bounded deployment/reproduction plan для будущего отдельного clean runtime каталога без его запуска;
6. задай проверяемые критерии, по которым 2-3 узла докажут одну main chain identity после будущего запуска.

## Required result

Верни:
`entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`

Exact verdict один из:
- `PASS_MAIN_ROOT_GENESIS_MECHANISM_IDENTIFIED`
- `PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`
- `BLOCKED_MAIN_ROOT_GENESIS_MECHANISM_NOT_VERIFIED`

Верни один рекомендуемый следующий bounded шаг.

## Boundary

Не останавливать старые WBN services. Не удалять DATA/DB. Не создавать новый genesis фактически. Не запускать новый runtime. Не менять Буржуинию/эРэФию/МАЖОР. Не переносить secrets/private keys. Не объявлять новый main chain созданным без будущего отдельного authority/launch gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: перевести решение ОПЕРАТОРА о новом main/root experiment в один безопасный точный исследовательский шаг
СТАТУС: tasked_read_only_main_genesis_research
