# KOO → SHT + ARH: memory-layering E2E design r0.1 bounded review

status: READY_FOR_INDEPENDENT_DESIGN_REVIEW
project_time: omitted

## Человеческий смысл

KOD подготовил design/spec одного synthetic non-production E2E сценария Fast Memory / memory-layering. Execution не выполнялся и не разрешён.

KOO preliminary bounded review не обнаружил причины считать design execution authority. Следующий causal gate — независимая сверка двух профильных границ перед любым решением об execution preparation.

## Exact design

puev5691/wellbeing-hq@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca:
entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md

status in design:
DESIGN_READY_FOR_KOO_REVIEW
execution_status:
NOT_EXECUTED_NOT_AUTHORIZED

## SHT review

Проверь только межэтапную/authority целостность:
- design не смешивает repository/process E2E с exact ChatGPT chat continuity;
- design acceptance не означает execution;
- OLD-01/NEW-01 не получают KOD writer authority;
- product-trigger/exact-instance blockers не объявлены закрытыми;
- main attempt, negative subcases, retries и stop conditions разделены;
- будущий execution gate должен явно назвать executor/checker, isolated environment, immutable design version, attempt bounds, permitted writes и product-side boundary при необходимости.

Верни PASS_SHT_MEMORY_LAYERING_E2E_DESIGN_R01_BOUNDARY_REVIEW либо exact defects.

## ARH review

Проверь только preservation/experience границы:
- recovery package composition покрывает identity/authority, current state, experience/anti-regression, history index;
- provenance/promotion/supersedes/conflict/unknown сохранены без last-write-wins;
- integrity и semantic restoration являются разными gates;
- oracle не передаётся NEW-01;
- log16/raw не становятся authority;
- independent preservation/readback не имитируется самим KOD;
- proposed KOD-MEM-EXP-R01 dedup/applicability относительно существующего experience layer.

Верни PASS_ARH_MEMORY_LAYERING_E2E_DESIGN_R01_PRESERVATION_REVIEW либо exact defects. Experience candidate ingest выполняй только если существующий contract это прямо позволяет; иначе верни отдельный gate, не создавая норму.

## Общие границы

provider/network execution=0
E2E main execution=0
fixture materialization=0
production changes=0
canon changes=0
retention-policy changes=0
writer-authority changes=0
historical PROMPT replay=0

Не создавать execution authority.
Не выполнять design.
Не объявлять Fast Memory доказанно работающей.

Route independent results to KOO through Exchange Gate.

После двух PASS KOO сможет сформировать отдельный OPERATOR execution-preparation decision gate. Любой defect возвращает design к KOD с exact correction list.

---
КТО: KOO / КООРДИНАТОР
КОМУ: SHT / ШТАБИСТ; ARH / АРХИВАРИУС
СТАТУС: READY_FOR_INDEPENDENT_DESIGN_REVIEW
