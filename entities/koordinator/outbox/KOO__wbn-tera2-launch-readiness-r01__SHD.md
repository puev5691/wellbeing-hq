# KOO → SHD: WBN/WBNP/TERA2 launch-readiness reconciliation r0.1

status: TASKED_BOUNDED_READ_ONLY_READINESS
entity: SHD / ШАРДОВИК
production_mutation: no
wbn_tera2_launch: no
secrets_credentials: no
destructive_cleanup: no
project_time: omitted; trusted project-time source not used

## Current-writer basis

Replacement SHD current-writer:
`entities/shardovik/current/SHD__replacement-initiation-current-writer.md`
commit `85260a61784e9aec33784c5d50cfbc3bfceab19b`
blob `88473e85feab1ae5482ff33268ca488abc42f8a4`.

Post-initiation state:
`entities/shardovik/current/SHD__replacement-resume-state.md`
commit `4abab83e831d236e3a97949c103675460c261bb9`
status `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`.

ARH reconciliation confirms replacement current-writer established and old writer historical/non-authoritative.

## Direction

OPERATOR previously set the profile direction: SHD is to work toward launching the project crypto platform. This task converts that broad direction into the first exact bounded step after successful replacement initiation.

This task is NOT permission to launch WBN/TERA2 yet.

## Task

Perform one fresh read-only launch-readiness reconciliation for the WBN/WBNP/TERA2 lab contour on MAZHOR / lab-01.

Required order:
1. fresh GitHub-preflight `puev5691/wellbeing-hq`;
2. confirm exact replacement current-writer identity and no competing writer evidence;
3. load only active approved Project Sources plus minimal SHD profile materials needed for this task;
4. inspect current SHD/WBN/WBNP/TERA2 evidence and distinguish current facts from historical tails/candidates;
5. perform one bounded read-only MAZHOR/lab-01 pass sufficient to establish current host/workspace/runtime state relevant to the crypto platform;
6. identify what WBN/TERA2 code/repo/runtime/node artifacts actually exist now, and their exact identities where available;
7. identify current process/service/port/storage/resource state only where directly relevant and read-only;
8. establish whether source/runtime parity is proven, unproven or mismatched;
9. identify exact prerequisites/blockers for the first bounded lab launch step;
10. recommend exactly ONE next technical action after this readiness result, with explicit mutation/rollback boundary.

## Do not do

Do NOT:
- start or restart WBN/TERA2 nodes;
- install packages or code;
- change firewall/services/ports;
- create shard/genesis/account/token/smart-contract state;
- mine/mint/send transactions;
- access or create secrets/credentials;
- touch production;
- revive COOP/PWH/hashchain/VPN tails unless they are directly necessary evidence for launch-readiness;
- promote PWH/hashchain or other candidates to canon;
- infer runtime parity from filenames or historical reports.

## Required result

`entities/shardovik/outbox/SHD__wbn-tera2-launch-readiness-r01__KOO.md`

Return one verdict:
- `READY_FOR_EXACT_WBN_TERA2_LAB_STEP`
- `READY_WITH_EXACT_BLOCKERS`
- `BLOCKED_RUNTIME_OR_SOURCE_CONFLICT`.

The result must state:
- fresh HQ boundary;
- current-writer identity;
- MAZHOR/lab-01 observed state;
- exact current WBN/WBNP/TERA2 evidence;
- source/runtime parity status;
- blockers/dependencies;
- ONE recommended next bounded action;
- forbidden actions still in force.

Return through Exchange Gate with immutable evidence where applicable.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть replacement SHD в профильную работу безопасным read-only шагом перед любым запуском криптоплатформы
СТАТУС: tasked_bounded_read_only_readiness
