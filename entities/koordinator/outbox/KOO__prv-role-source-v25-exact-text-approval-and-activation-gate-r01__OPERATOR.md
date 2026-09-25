# КОО → ОПЕРАТОР: утверждение точного текста роли PRV и отдельный gate активации источника

terminal: PASS_KOO_PRV_ROLE_SOURCE_V25_EXACT_TEXT_APPROVED_ACTIVATION_PENDING
scope: EXACT_SOURCE_TEXT_APPROVAL_AND_ACTIVATION_PREPARATION_ONLY
project_time: omitted

## Решение ОПЕРАТОРА

ОПЕРАТОР в адресном чате КОО ответил на exact карточку решения единственной строкой:

APPROVE_PRV_ROLE_SOURCE_V25_EXACT_TEXT_ONLY

Это approval содержания только указанного ниже immutable кандидата. Это не approval новых байтов, не активация Project Source и не утверждение посетительского runtime. Действующий источник ролей v2.4 остаётся ACTIVE до отдельного PASS source-set activation barrier.

## Fresh reconciliation

Fresh HQ HEAD до фиксации: 35f68cd067fb54e3b847d3be129c491821b3d1a6. Последние изменения после decision gate 79f634d87718857b85791c6f4d6e278fb94b708f касаются отдельной линии KOD Telegram read-only Bot API bridge и записи об activation boundary; не заменяют кандидата/решение PRV. В проверенной линии не найден конкурирующий successor/approval/current-writer.

KOO current-writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md; Git blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd; WRITER_ESTABLISHED.

Действующие шесть approved Project Sources из приложенного source set вновь прочитаны и сверены по Git blob: recovery 233117e1c9509d730e1f5ec532b1cabe3f786609; roles v2.4 1772339cb74dae8550bfbd2e33401c34a929e911; source-loading 69eb657f260a019f76e8e707c880ea88c1dfa0bf; file-work e9c29d62057f34e4f771d6057a36d9b7f72e74c2; task-conveyor df7896d867eeeffff506319538fedad938856686; core a42f7dca6a7469a54fa2da24aae0da4e549c9d33. Source-set r0.7 activation result remains blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99; roles v2.4 was not replaced.

Exact approved text: puev5691/wellbeing-hq@456db508377fc7eab5411176377c0f7889e8acdc:entities/koordinator/outbox/KOO__entity-roles-short-v25-prv-candidate-r01__OPERATOR.md; blob b7efcb983cd45c9b098ef9d937b897224a838aa8.

Decision gate read: puev5691/wellbeing-hq@79f634d87718857b85791c6f4d6e278fb94b708f:entities/koordinator/outbox/KOO__prv-role-source-v25-operator-decision-gate-r01__OPERATOR.md; blob b0847a581408490d69577ef812a645e09b21b7be.

Independent KAN review: puev5691/wellbeing-hq@f9f3a5f049e0175aea156be45927698fdbc61dad:entities/kancelar/outbox/KAN__prv-role-candidate-r01-independent-review__KOO.md; blob a6b2ca84a027eaf8e117feb6e19faf6110cb1f85; PASS_WITH_BOUNDARIES. Exact predecessor diff: blob 1ba83cc7c554b78b5e225568709f270e098fc965, 144 → 156 lines, three hunks +25/-13, reconstruction PASS. The KAN review concerns precisely candidate blob b7ef... and does not review future modified approved-source metadata.

## Concrete next gate (not executed)

To include this text in active Project Sources, a separate source-set activation step must:
1. Fresh-check HEAD, KOO writer, competing approval/supersession and six active source identities.
2. Prepare a versioned approved-source successor from the approved candidate. Distinguish exact approved substantive role text from any necessary service metadata changes (title, status, version, source, approval decision, changed_sections); publish and check exact metadata-only delta against approved candidate. If any substantive role wording changes, stop and request new review/decision for changed bytes.
3. Check activation barrier for single-source replacement: all required source files available/consistent, exact blobs and readbacks, no competing activation, predecessor roles v2.4 explicitly superseded only after barrier PASS. Record approved successor source path, Git blob and source-set activation terminal with postwrite readback.
4. Update active attached Project Source in UI only under separate explicit instruction or a demonstrated authorized mechanism; GitHub publication by itself cannot prove an active UI Project Source changed. Until UI/source-set effectivity is verified, record ACTIVATION_PENDING, not ACTIVE.

Next exact permission requested if ОПЕРАТОР wants activation work:
AUTHORIZE_PRV_ROLE_SOURCE_V25_SOURCE_SET_ACTIVATION_R01

Meaning: authorize a bounded source-set activation procedure for the already approved role text, including exact metadata transformation and verification of applicable source-set and UI effectivity gates. Do not infer permission for PRV physical instance/recovery/Writer Gate, visitor data handling, Telegram bot response, provider/host work or automation. If active UI source replacement requires the ОПЕРАТОР, return the exact prepared file and one concrete manual action; do not claim UI activation until verified.

Until this separate permission: approved_text = YES, role_source_active = NO, PRV_writer_runtime = NOT_ESTABLISHED. Publication/dispatch/inbox != activation or processing_started. Historical PROMPT replay: none. Memory-layering attempt 3: NOT_AUTHORIZED.

---
КТО: KOO / КООРДИНАТОР
КОМУ: ОПЕРАТОР
СТАТУС: PASS_KOO_PRV_ROLE_SOURCE_V25_EXACT_TEXT_APPROVED_ACTIVATION_PENDING
