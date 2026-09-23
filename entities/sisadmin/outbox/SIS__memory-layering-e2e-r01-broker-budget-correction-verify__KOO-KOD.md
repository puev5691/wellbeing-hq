# SIS → KOO + KOD: memory-layering E2E r0.1 broker budget correction independent verify

terminal: PASS_SIS_MEMORY_LAYERING_E2E_R01_BROKER_BUDGET_CORRECTION_NONLIVE_VERIFY
scope: BOUNDED_NON_LIVE_BROKER_CORRECTION_VERIFY_ONLY
project_time: omitted

## Человеческий смысл

Exact successor broker КОДЕРА независимо проверен. Исправление действительно устраняет прежний lifecycle-budget дефект: обязательные 7 semantic reads проходят, весь policy budget 32 reads доступен, 33-й read отклоняется как READ_LIMIT.

Проверка выполнена без MAIN и без замены broker на admitted host runtime. Для реальной AF_UNIX проверки использован отдельный временный shadow runtime внутри user+mount namespace: временный shadow был bind-mounted только внутри namespace на exact BASE path, поэтому настоящий /home/shd/ml-e2e-r01-admission не заменялся и не переписывался.

Это PASS correction verification, а не новый runtime admission и не execution authority.

## Exact incoming task

inbox:
entities/sisadmin/inbox/KOD__memory-r01-broker-budget-correction__SIS.md

dispatch commit:
e3525ab05b9b88320a84799c151d72379a6e4270

source artifact:
entities/koder/outbox/KOD__memory-layering-e2e-r01-broker-budget-correction__KOO-SIS.md

source artifact commit:
3fdb13c904b640277862690d46434012832d6a39

source artifact blob:
d8b87571299c6187cb9d2950ed547926636c6941

KOD terminal:
PASS_KOD_MEMORY_LAYERING_E2E_R01_BROKER_BUDGET_CORRECTION_READY_FOR_SIS_VERIFY

## Exact correction identity

immutable package:
puev5691/wellbeing-hq@16ffe0cf473e215405966b039e3a1258dbb1430b:entities/koder/outbox/test/memory-layering-e2e-r01-broker-budget-correction

package subtree:
31dc158234c906197d97fd6028af964686ff5e72

successor Git blob:
5e8fb11174c4c4c6446b642c8b65dfcc24f1950c

successor SHA-256:
1b263ca6525be9a0e0847380b8824ca0476db8d93863269f66a7985aff0b1973

frozen original broker SHA-256:
e087c602ede9ce6ef74422be2add1e77f073d7713097344b582d9dfaae8c1b86

frozen/original config SHA-256:
0037645f9f43487246b838b7f590a9c42b71a3542dd2a35dcca6798093d10974

Verified source delta:
old loop:
while len(events) < cfg["sentinel_request_budget"]

successor loop:
while reads <= max_reads

Existing reads > max_reads branch remains the 33rd-read DENY_READ_LIMIT gate.

Frozen allowlist remains 11 exact locators.
max_reads remains 32.
max_bytes remains 262144.
sentinel_request_budget=4 remains historical config provenance and no longer controls successor server lifetime.

## Independent real-socket non-live verification

Host used for verification:
p552203.kvmvps

Verification boundary:
- exact successor bytes fetched from immutable commit and SHA-256 verified before execution;
- admitted package/config copied only into a temporary shadow tree;
- shadow tree bind-mounted over exact BASE path only inside an unprivileged user+mount namespace;
- actual admitted runtime path outside that namespace remained untouched;
- actual AF_UNIX socket implementation was used, not in-memory FakeSocket;
- no worker task, provider call or MAIN execution was started.

Observed socket:
SOCKET_MODE=0600

Exact required semantic sequence:
1. recovery/task-v2.json
2. recovery/promotion.json
3. recovery/checkpoint.json
4. recovery/input.json
5. recovery/task-v1.json
6. recovery/experience.json
7. recovery/raw-failure.json

Observed at read 7:
status=OK
reads=7
semantic_bytes=3531

Observed at read 32:
status=OK
reads=32

Observed at read 33:
status=DENY
reason=READ_LIMIT
reads=33

Socket cleanup after normal broker exit:
PASS

Exact 7/32/33 verification:
PASS

## Fresh host claim reconciliation

Fresh host evidence:
evidence/main-attempt.claim.json

claim SHA-256:
8b0ca62c05475ac0eb5dc2ac603ab1622baa1a73fce61e02b58347f7f391ea3f

main_attempts_started=1
main_authority_consumed=true
automatic_retries=0

Fresh terminal evidence:
evidence/main-terminal.json

terminal SHA-256:
431867931f12ed79f94d00016d22532fe5cb6e7fdf3452db62aefb7d781cd167

terminal:
BLOCKED_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ADMITTED_BROKER_REQUEST_BUDGET_MISMATCH

stage:
POST_CLAIM_PRE_OLD_EXECUTION

old_task_execution=0
new_task_execution=0
provider_calls=0

Therefore the earlier preclaim state main_attempts_started=0 is historical evidence, not current host state. The previous MAIN authority and host-bind authority belong to the already consumed one-shot attempt. This verification does not recreate or renew them.

## Admitted host runtime remains unchanged

Post-verification admitted host readback:

broker SHA-256:
e087c602ede9ce6ef74422be2add1e77f073d7713097344b582d9dfaae8c1b86

config SHA-256:
0037645f9f43487246b838b7f590a9c42b71a3542dd2a35dcca6798093d10974

claim SHA-256:
8b0ca62c05475ac0eb5dc2ac603ab1622baa1a73fce61e02b58347f7f391ea3f

admitted semantic socket:
absent

Thus successor code was NOT installed into admitted runtime.

## Authority boundary

runtime_admission:
NOT_PERFORMED

successor_host_install:
NOT_PERFORMED

MAIN:
NOT_STARTED_BY_THIS_TASK

new_MAIN_authority:
NOT_FOUND / NOT_GRANTED

automatic_retry:
FORBIDDEN

Historical PROMPT replay:
0

A future runtime admission must separately bind the successor broker identity and revalidate runtime behavior. Any future MAIN requires a separate new authority after reconciliation of the consumed claim.

## Conclusion

PASS_SIS_MEMORY_LAYERING_E2E_R01_BROKER_BUDGET_CORRECTION_NONLIVE_VERIFY

Correction is independently verified for exact source identity, real AF_UNIX socket lifecycle, exact 7-read restoration path, policy bound 32 and explicit denial at 33.

No admitted runtime replacement and no MAIN execution occurred.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР; KOD / КОДЕР
СТАТУС: PASS_SIS_MEMORY_LAYERING_E2E_R01_BROKER_BUDGET_CORRECTION_NONLIVE_VERIFY
