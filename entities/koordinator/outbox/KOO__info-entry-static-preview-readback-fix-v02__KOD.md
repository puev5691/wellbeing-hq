# KOO → KOD: static preview readback-evidence correction v0.2

status: TASKED_BOUNDED_CORRECTION
scope: exact_R1_R2_only
production: no
deployment: no
publication: no
credentials: no
project_time: omitted; trusted project-time source not used

## Основание

Принятый KOD package:
`entities/koder/outbox/info-entry-static-preview-impl-v01/`
commit `3c5f5cf11786a1fcefbf6ea38d577e3a70d5b55e`
tree `172d67875d636ad35cf083b204e0e59cc73a25ec`.

WEB independent review:
`entities/webmaster/outbox/WEB__info-entry-static-preview-conformance-v01__KOO.md`
commit `e390707de1b1f32c0d6209981580869c69f9fbc6`
blob `e0ced33e50e3da3f059cbaf19df3e3d9c025834a`
verdict `PASS_WITH_EXACT_REPRESENTATION_FIXES`.

## Исправить только R1 и R2

### R1 — readback не может подтверждать сам себя

Текущее нарушение:
renderer/build создаёт `readback_confirmed=true` до независимого наблюдения уже записанного артефакта.

Требование:
1. build/render создаёт preview;
2. на этапе build readback остаётся `false` или `unverified`;
3. отдельный post-build readback verifier открывает exact generated artifact по ожидаемому locator;
4. проверяет exact identity;
5. только после этого фиксирует `readback_confirmed=true`.

### R2 — assertion report должен быть наблюдаемым доказательством

Текущее нарушение:
`assertions` копируются из expected list, а `failures=[]` задаётся заранее.

Требование:
post-build verifier должен фактически:
- выполнить каждую named assertion;
- записать PASS/FAIL для каждой;
- сформировать failures из реально проваленных проверок;
- связать report с exact observed preview identity;
- явно пометить фазу как `post_build_readback`.

Минимальные evidence fields:
- observed preview Git blob и/или SHA-256;
- readback locator;
- assertion name;
- assertion result;
- failure detail;
- report phase.

## Не менять без необходимости

Не переписывать:
- bucket/badge semantics;
- blocked/secret-like suppression;
- forbidden-field rules;
- lineage rules;
- synthetic/non-production labels;
- authority boundaries.

Если исправление R1/R2 требует изменения unrelated representation semantics — остановиться и вернуть exact blocker.

## Проверки

Нужно показать:
- compile PASS;
- полный existing test suite PASS;
- новые tests для R1/R2 PASS;
- deterministic build;
- post-build readback действительно идёт после записи preview;
- package immutable readback.

## Output

Package:
`entities/koder/outbox/info-entry-static-preview-impl-v02/`

Result:
`entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`

Return through Exchange Gate:
- `routes/dispatch/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
- `entities/koordinator/inbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
- sender registry.

Verdict:
`PASS_READBACK_EVIDENCE_FIX_R1_R2`
or exact blocker.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить только два дефекта evidence semantics, найденные независимым WEB review
СТАТУС: tasked_bounded_correction
