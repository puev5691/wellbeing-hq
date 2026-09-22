# KOO → OPERATOR: memory-layering E2E r0.1 execution-preparation decision gate

status: WAITING_OPERATOR_EXECUTION_PREPARATION_DECISION
project_time: omitted

## Что произошло

Design первого bounded synthetic E2E Fast Memory прошёл обе независимые профильные проверки:

- SHT: PASS_SHT_MEMORY_LAYERING_E2E_DESIGN_R01_BOUNDARY_REVIEW
- ARH: PASS_ARH_MEMORY_LAYERING_E2E_DESIGN_R01_PRESERVATION_REVIEW

Это означает только: проект эксперимента достаточно согласован по authority/inter-stage и preservation/experience границам, чтобы отдельно решить вопрос подготовки исполнения.

Fast Memory ещё не доказана. Fixtures не материализованы. Main E2E не запускался.

## Immutable design

puev5691/wellbeing-hq@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca:
entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md
blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0
scenario ML-E2E-DESIGN-R01.

## Proposed execution-preparation scope

Если ОПЕРАТОР разрешает следующий этап, разрешить только PREPARATION, не main execution.

Executor/preparer:
KOD v0.5 — материализация synthetic fixtures и deterministic harness candidate.

Checker:
отдельный deterministic verifier/oracle, доступ к oracle имеет checker, но не NEW-01 worker. До main execution exact checker package должен пройти independent SHT/SIS-style bounded review; KOD self-test не заменяет independent verification.

Isolated environment:
новый временный non-production workspace/process namespace MLTEST; OLD-01 и NEW-01 — отдельные процессы, без inherited task variables/cache/transcript; worker без arbitrary network/provider/tools/project writer capability.

External test locator:
отдельный immutable GitHub test-package locator в puev5691/wellbeing-hq under KOD outbox/test namespace. Он не является production recovery registry/current state. Exact commit/tree/blob/checksums должны быть закреплены до execution admission.

Permitted writes during preparation:
только новые synthetic fixture/harness/test-package artifacts, KOD result, Exchange Gate routing, RED journal-source и ARH experience candidate/provenance. Не изменять approved Project Sources, production recovery/current, writer state, retention policy или реальные Entity task states.

Attempt/read/byte/time bounds inherited from reviewed design:
- main execution in this gate: 0;
- preparation/self-tests only;
- future main attempt: exactly 1, no automatic retry;
- semantic reads future main: max 32;
- semantic payload future main: max 256 KiB;
- computation deadline future main: 5 s;
- provider calls: 0;
- worker arbitrary network: 0;
- production writes: 0.
Mandatory approved-source bootstrap is separately metered; if it cannot fit agreed bootstrap boundary, preparation returns BLOCKED rather than silently shrinking sources.

Independent preservation owner:
ARH. KOD may create self-check evidence but MUST NOT impersonate ARH preservation PASS. Before future main execution, exact materialized recovery package requires ARH independent preservation/readback receipt if preparation result says package is ready.

Product-side boundary:
this r0.1 preparation and any later synthetic process execution do NOT claim exact ChatGPT chat/Work continuity. No product-side ChatGPT activation is required for the synthetic process test itself. Any later claim/test involving actual ChatGPT Work/new chat/existing Entity chat requires a separate product-side gate and supported activation/context boundary.

## Stop after preparation

Preparation may produce only:
- exact synthetic fixtures;
- harness/checker candidate;
- manifest/checksums;
- isolation contract;
- expected evidence schema;
- deterministic offline self-tests;
- proposed immutable package locator;
- exact independent-review/preservation inputs.

After that KOD stops.

No OLD-01→NEW-01 main E2E attempt may run until:
1. preparation package exists and readback passes;
2. checker/harness is independently verified;
3. ARH preservation/readback requirement is satisfied;
4. KOO reconciles those results;
5. OPERATOR separately authorizes MAIN E2E EXECUTION.

## Decision token

To authorize only this bounded preparation stage:

AUTHORIZE_MEMORY_LAYERING_E2E_R01_EXECUTION_PREPARATION

This token does NOT authorize main E2E execution, production changes, canon/retention changes, writer-authority changes, real ChatGPT chat resume, or project acceptance.

---
КТО: KOO / КООРДИНАТОР
КОМУ: OPERATOR / ОПЕРАТОР
СТАТУС: WAITING_OPERATOR_EXECUTION_PREPARATION_DECISION
