# Inbox pointer: SHD → KOO

Кратко: SHD завершил independent semantic/chain-policy review immutable TERA2 root-profile candidate r0.2 и возвращает terminal blocker КООРДИНАТОРУ.

## Locator

artifact: `entities/shardovik/outbox/SHD__tera2-root-profile-r02-review__KOO.md`
artifact_commit: `bcdbe6dfc744ee1ff581ca78bd1f3eeaf001323c`
artifact_blob: `7091f6ebb88b8130602eadf67be27fbefa68904f`
source_task: `entities/koordinator/outbox/KOO__tera2-root-profile-r02-review__SHD.md`
source_task_commit: `dbbf5950a1657d92c683287905d11a1980d282a7`
source_task_blob: `dddc8dd9f4d7d02d27b709b835de80ccae6cbe5e`

## Terminal verdict

`BLOCKED_TERA2_ROOT_PROFILE_R02_COMMON_IDENTITY_CONTRACT`

## Blockers

1. `MODE_RUN` выбирает common root profile, но помещён в `node-local.example.json` как будто это только per-node operational field; verifier не требует его точного совпадения с common `root-profile.mode_run`.
2. static verifier не доказывает полное соответствие machine-readable chain-policy profile фактически применяемому tracked source patch; ряд consensus/update/reward/genesis policy fields может drift без fail-closed rejection.

Текущие r0.2 naming/economic choices сами по себе этим verdict не отклонены; они остаются KOD candidate choices, требующими KOO/OPERATOR policy acceptance до launch.

## Smallest next bounded action

Открыть KOD correction-only task: исправить common-vs-node-local `MODE_RUN` contract и расширить fail-closed profile↔patch/source identity verification; никаких node/genesis launch, DATA/DB или credentials. После immutable correction вернуть SHD на один read-only re-review.

## Boundary

Node/genesis не запускались. DATA/DB не создавались и не менялись. Credentials/miner keys не использовались. Candidate package SHD не переписывал.

status: `incoming-dispatched`
project_time: omitted; trusted project-time source not used
