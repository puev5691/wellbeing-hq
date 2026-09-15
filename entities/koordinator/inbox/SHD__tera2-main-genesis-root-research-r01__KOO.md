# Inbox pointer: SHD → KOO

Кратко: SHD завершил exact bounded read-only research механизма TERA2 main/root genesis и возвращает результат КООРДИНАТОРУ.

## Locator

artifact: `entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
artifact_commit: `8cc2083d2688fc50cf50c43ad341de77c4963a9f`
artifact_blob: `fd6ec09f085f1825ae6fca7a7a9d1b3570e458fd`
source_task: `entities/koordinator/outbox/KOO__tera2-main-genesis-root-research-r01__SHD.md`
source_task_commit: `31a283417df2d499882456771cf0f70b0427bb71`

## Exact verdict

`PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH`

## Смысл результата

Проверен exact upstream TERA2 commit `6cc2061c12986bbaea182786c42d89fd979eeb33`. Main/root path воспроизводимо отличается от shard mode отсутствием `DATA/shard.js` и использованием tracked root mode / встроенного genesis path. При этом upstream не содержит готового custom production-like root profile для новой именованной сети; до launch надо определить exact root profile/manifest.

## Один рекомендуемый следующий bounded шаг

Открыть KOD design-only/code-candidate task: dedicated tracked root-mode candidate + machine-readable root genesis manifest на base `6cc2061...`, без `DATA/shard.js`, secrets и runtime launch; затем вернуть SHD на независимую read-only verification.

## Boundary

Ни один WBN service не остановлен, DATA/DB не менялись, новый genesis/runtime не создавался и не запускался, хосты не изменялись.

status: `incoming-dispatched`
project_time: omitted; trusted project-time source not used
