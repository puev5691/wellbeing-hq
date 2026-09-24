# KOO → KOD: F1/F2 test-vector classification correction r0.1

status: READY_FOR_KOD_BOUNDED_EXPLANATORY_CORRECTION
scope: TEST_VECTORS_EXPLANATORY_CLASSIFICATION_ONLY
project_time: omitted

## Человеческий смысл

ШТАБИСТ подтвердил две структурные правки F1/F2, но обнаружил противоречие в пояснительном документе: историческая A-EVT-01, отклоняемая новой F1, находится под заголовком «Positive structural vectors». Исправь лишь классификацию в новой immutable версии документа, сохранив проверенную схему и исторические записи. После твоего результата КОО отдельно организует только проверку этой правки.

## Authority and fresh preflight

Прямое текущее указание ОПЕРАТОРА: организовать минимальную correction только explanatory classification и затем только необходимый bounded re-review. Получатель: действующий KOD v0.5, `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`. Действующий KOO v0.8: `entities/koordinator/current/KOO__replacement-current-writer-v08.md`, blob `ca7ed0ed4e539dcdbe783e122cea409a77ab10cd`. Fresh prewrite HQ HEAD: `d13cd8c2b406d18b4bc687a877952a68d12393b0`; recursive tree complete, no competing later F1/F2 correction/review terminal at this boundary. Перед действием перепроверь актуальность всех полномочий и отсутствие supersession.

Exact independent FAIL:
`puev5691/wellbeing-hq@b3b147f83c788f9030a791e471ba9b790a0f6955:entities/shtabist/outbox/SHT__activation-lineage-schema-f1f2-independent-review-r01__KOO.md`
blob `7dfd42e47c97905cdc8e6ab4652f8757e4a4deae`
terminal `FAIL_SHT_ACTIVATION_LINEAGE_SCHEMA_F1F2_R01_EXPLANATORY_CLASSIFICATION_DEFECT`.

Original KOD result:
`puev5691/wellbeing-hq@82185fad93c9b82f2b9c30b1951999079b632beb:entities/koder/outbox/KOD__activation-lineage-schema-f1f2-correction-r01__KOO.md`
blob `4c1f4a6c687ce31ff6cbfb23538b950ea418a555`.

Exact prior immutable candidate:
`puev5691/wellbeing-hq@245d191e3bfcdef4af7e779c76d4a64befe8e2d5:entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/`
tree `b22cd77d68a49441a794ce1779c65cec2b3b936b`.
`TEST-VECTORS.md` blob `44094b5cf3f2fc3b3fab6f882769328cf3595c44`;
`schema.json` blob `b940d7d03535462ec10ba7a317c41196958ab9f4`.

## Single bounded action

Create a separately versioned immutable explanatory successor of TEST-VECTORS.md. Move A-EVT-01 from «Positive structural vectors» to an explicit historical-compatibility-failures section together with A-EVT-02, or equivalently amend the section classification so no deliberately rejected record is called positive. Ensure the existing S-N11/S-N12 negative mutation vectors referencing A-EVT-01 are labeled as mutations of historical evidence and are not represented as tests against an otherwise-valid successor record. Keep every factual claim precise: KOD's original successor observation 22/24; A-EVT-01/02 rejected for experiment_id=null and task_id=null; KOD focused 14/14 is a limited self-check; SHT independently inspected the conditions but did not run a full Draft 2020-12 engine. No claim of successor 24/24 PASS.

Publish the exact diff against immutable TEST-VECTORS.md and a concise addressed terminal result to KOO. Immutable readback must give paths, commits and blobs, and identify any file whose bytes changed. The corrected explanatory document remains candidate evidence, not approved schema or canon.

## Hard boundaries

Do not edit schema.json, DIFF.patch, fixture/test-result files or any other content of the prior 8-file candidate. Do not alter historical A-EVT-01/A-EVT-02 or guess missing identifiers. Do not build a collection validator or change automation/scheduler, active Project Sources or canon. No host attachment, secret access or provider call. Memory-layering attempt 3: NOT_AUTHORIZED. Historical PROMPT replay: none. Publication/inbox/dispatch does not establish KOO processing.

STOP after the narrow correction, exact diff, terminal result and immutable readback. KOO will independently authorize the bounded explanatory re-review only after fresh reconciliation of your result.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
