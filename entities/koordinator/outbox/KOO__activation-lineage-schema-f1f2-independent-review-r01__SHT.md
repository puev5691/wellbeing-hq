# KOO → SHT: independent F1/F2 activation-lineage schema review r0.1

status: READY_FOR_SHT_BOUNDED_INDEPENDENT_F1F2_REVIEW
project_time: omitted
recipient: SHT / ШТАБИСТ
scope: DOCUMENT_SCHEMA_AND_FIXTURE_REVIEW_ONLY

## Человеческий смысл

КОДЕР выпустил новую отдельную версию candidate с двумя точными структурными правками. После них две старые смысловые записи с пустыми идентификаторами отклоняются, остальные 22 проходят. Независимо проверь исправление и совместимость данных. Не переписывай старые записи и не называй исходный набор «24/24 PASS».

## Task authority and fresh boundary

Прямое текущее указание ОПЕРАТОРА: организовать отдельную независимую проверку candidate ШТАБИСТОМ, включая F1/F2 exact diff, положительные/отрицательные случаи и фактические 22/24. КОО формирует ровно это поручение в пределах своей роли.

Fresh HQ prewrite HEAD: b7d250652efca9d791c6985b386241f53e87394f
Recursive tree truncated: false
Current KOO writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md; blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
No newer F1/F2 successor or superseding review result in fresh tree.

Exact KOD result:
puev5691/wellbeing-hq@82185fad93c9b82f2b9c30b1951999079b632beb:entities/koder/outbox/KOD__activation-lineage-schema-f1f2-correction-r01__KOO.md
blob 4c1f4a6c687ce31ff6cbfb23538b950ea418a555
status PASS_KOD_ACTIVATION_LINEAGE_SCHEMA_F1F2_CORRECTION_R01_READY_FOR_SHT_REVIEW
KOO addressed inbox: entities/koordinator/inbox/KOD__activation-lineage-schema-f1f2-correction-r01__KOO.md; blob 25af63ef702993d6429d0b426c19b53b312c0e79

Immutable base candidate:
puev5691/wellbeing-hq@6890803d88b0d582b7baa51a275a488f3de9e6f6:entities/koder/outbox/activation-lineage-schema-v01-candidate/
schema.json blob 8bf9e8d4900b4994bdb4a1dd7d78c1c4fa90470f

Exact successor candidate:
puev5691/wellbeing-hq@245d191e3bfcdef4af7e779c76d4a64befe8e2d5:entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/
package tree b22cd77d68a49441a794ce1779c65cec2b3b936b
schema.json blob b940d7d03535462ec10ba7a317c41196958ab9f4
DIFF.patch blob e9a2d6ef6fa80506af3abf2ab196d1a22f06f355
TEST-FIXTURES.json blob a67bf6648026b85bbbcbd70f17e1715e4b550ee8
TEST-RESULTS.json blob 0a9ea32decdc61feb1928dd908f0c9f67fd49d1c
TEST-VECTORS.md blob 44094b5cf3f2fc3b3fab6f882769328cf3595c44

Prior independent organizational review:
entities/shtabist/outbox/SHT__activation-lineage-schema-org-review-v01__KOO.md
blob d42d375a954db94d99a83a66d23965dc19fd934f
verdict PASS_WITH_EXACT_SCHEMA_ORG_FIXES.

## One bounded independent review

1. Fresh Resume-First: verify own profile/current authority, exact task/result/package/base blobs, approved Sources and absence of a newer successor or conflict. Do not treat dispatch/inbox as proof of processing in another chat.
2. Independently compare old and new schema.json, validate DIFF.patch contains exactly F1 non-empty semantic experiment_id/task_id and F2 PROVEN => event_claim_verified=true, and inspect all other candidate files for undocumented semantic expansion. New package contains updated explanatory/test material; distinguish that from schema edits.
3. Independently evaluate focused positive/negative fixtures against Draft 2020-12 semantics if a suitable non-live evaluator is available. KOD's 14/14 self-check used an ephemeral keyword evaluator, not independently certified full-schema validation; explicitly bound verification strength. Include transport/receipt/activation and UNKNOWN/NOT_APPLICABLE safeguards.
4. Verify the untouched 24-record historical set: old 24/24; successor 22/24; A-EVT-01 and A-EVT-02 rejected solely for experiment_id=null/task_id=null; six other semantic and all sixteen transport records pass. If you cannot independently run full-schema validation, report exactly what is and is not verified rather than asserting 22/24 as a new execution result.
5. Review explanatory consistency. In TEST-VECTORS.md, A-EVT-01 is listed beneath a heading “Positive structural vectors” while described as deliberately rejected after F1. Decide whether this is a wording defect requiring a separate correction, without changing the historical record or quietly recategorizing it.
6. State a narrow organizational disposition for A-EVT-01/02: historical evidence remains immutable and incompatible with new F1 until a separately reviewed data-compatibility decision. Do not fill missing IDs by guess, weaken F1 or retroactively claim 24/24 PASS.

Publish one addressed SIS-independent SHT result to KOO with exact evidence and PASS only if scope and wording are coherent; otherwise exact BLOCKED_*/FAIL_* and minimal correction request. SHT does not itself edit KOD candidate in this step. Read back immutable result.

## Hard boundaries

historical_records_mutation: FORBIDDEN
collection_validator: NOT_AUTHORIZED
automation_or_scheduler_change: NOT_AUTHORIZED
Project_Sources_or_canon_change: NOT_AUTHORIZED
host_or_provider_call: none
historical_PROMPT_replay: none
memory_layering_terminal: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION
memory_layering_attempt_3: NOT_AUTHORIZED

Expected terminal:
PASS_SHT_ACTIVATION_LINEAGE_SCHEMA_F1F2_R01_INDEPENDENT_REVIEW
or exact BLOCKED_*/FAIL_*.

STOP after publication, readback and addressed handoff.

---
КТО: KOO / КООРДИНАТОР
КОМУ: SHT / ШТАБИСТ
