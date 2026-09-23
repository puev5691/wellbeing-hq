# KOO → OPERATOR: bind unconsumed ML-E2E-R01 MAIN authority to admitted p552203 runtime

status: WAITING_OPERATOR_HOST_BOUND_MAIN_DECISION
project_time: omitted

## Человеческий смысл

p552203.kvmvps прошёл exact runtime admission для ML-E2E-R01. MAIN ещё не запускался. Ранее выданная одноразовая authority AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION остаётся неизрасходованной, но была выдана до выбора этого host и не переносится на него автоматически.

Нужно отдельное решение ОПЕРАТОРА: разрешить использовать именно эту ранее неизрасходованную one-shot MAIN authority на exact admitted runtime p552203.

## Exact admitted runtime

SIS terminal:
PASS_SIS_MEMORY_LAYERING_E2E_R01_P552203_RUNTIME_ADMISSION

Admission JSON:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-p552203-runtime-admission.json
publication commit cccce6f58625716bd9ac765aadc6f24888f08703
blob 8d5a3ceaa63767957906e0b1df3fcfe108e725aa
host-file SHA-256 c9305e658da97c6852b9d4bcb6ce73a5f1053bdfe926efe796ffa43e242665fe

Host:
p552203.kvmvps
machine-id SHA-256 8c109d3a8fabdd5dae11510668967ba94ea2314b20374e8218cf76e1dbcba1f4

Immutable design/package remain:
design commit 9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca, blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0
preparation commit 5e03bfb59e763ba48e2ea982f31ae3fc33b69b23, subtree c3a4f352d5d65e363d569803bc726bac164bd086

## Existing authority state

AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION

main_attempts_started=0
main_authority_consumed=false
automatic_retries=0

The failed KOD runtime admission did not start MAIN and did not consume authority.

## Decision effect

If authorized, KOO may route the exact host-bound MAIN execution to SIS/KOD roles using only the admitted runtime and immutable package above.

All original MAIN bounds remain:
- exactly 1 main attempt;
- automatic retries=0;
- semantic reads <=32;
- semantic bytes <=262144;
- computation deadline <=5 s;
- provider calls=0;
- arbitrary worker network=0;
- production/project/current/writer/canon/retention mutation=0;
- oracle/checker-private supervisor-only;
- structural PASS + semantic restoration PASS required before continuation.

After the attempt, no retry is authorized regardless of PASS/FAIL/BLOCKED.

Independent post-result SHT review and ARH preservation/readback remain required.

Even PASS proves only bounded synthetic process recovery/selective-retrieval/continuation, not ChatGPT chat continuity or production Fast Memory.

## Decision token

AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_ON_ADMITTED_P552203

This token binds the already-unconsumed MAIN authority to the exact admitted p552203 runtime above. It does not create a second attempt or standing authority.

---
КТО: KOO / КООРДИНАТОР
КОМУ: OPERATOR / ОПЕРАТОР
СТАТУС: WAITING_OPERATOR_HOST_BOUND_MAIN_DECISION
