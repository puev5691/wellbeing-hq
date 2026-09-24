# КООРДИНАТОР: blocker согласования Project Instructions v3 metadata2

## Что произошло и что нужно решить

КООРДИНАТОР сверил новый точный кандидат v3 после отдельного Writer Gate v0.8. Инициация и право текущего writer подтверждены. KAN закрыл K5 по сохранённому исходному UI v2; прежние K1–K4/K6 остаются закрытыми в проверенном содержательном объёме.

ШТАБИСТ точно выполнил ограниченную правку двух строк, однако в следующей, третьей служебной строке того же раздела осталось утверждение, что прежний пробел блокирует полное сравнение с исходным UI и заявление об активации. Это противоречит двум новым строкам и KAN K5 PASS. Поэтому точный `metadata2` payload пока нельзя честно представить как внутренне согласованный предмет решения APPROVE / REJECT.

Минимальное решение ОПЕРАТОРА: разрешить отдельную правку третьей устаревшей служебной строки с новым immutable commit/blob, точным diff и readback либо оставить эту редакцию на паузе. Уже существующий файл с исправленными тремя строками не назначается автоматически новым target: у него иная identity и иной объём правки. После решения КОО заново сверит точную версию и подготовит gate утверждения. Текущий UI v2 и active Project Sources не меняются.

## Exact blocker

terminal: BLOCKED_KOO_PROJECT_INSTRUCTIONS_V3_METADATA2_INTERNAL_K5_CONTRADICTION
scope: Project Instructions v3 approval reconciliation only
fresh_hq_head_before_result: 33b552de8736419cff9e1c971446b3c77659635e
writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md
writer_establishment_commit: 9781aeff09d868ade3f3e1a28f28014d23512386
writer_blob: ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
prior_KOO_reconciliation: entities/koordinator/outbox/KOO__project-instructions-v3-resume-reconciliation-r01__OPERATOR.md@7835ba7a3fb96c3ab96ce1b6b6b7285f336cf3e3
prior_KOO_blob: 0fdef53a59de0a4a10d1cb6b31797bb16d73e3e6

target: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata2.md@848a035d9616f68d0f47eb6acca0333be3f948d1
target_blob: 66626473e7d08e2d5d71021c3c2159e929b1b0d0
diff: entities/shtabist/outbox/SHT__project-instructions-v3-r03-final-metadata2-exact-diff.md@33b552de8736419cff9e1c971446b3c77659635e
diff_blob: 0ef972461f572b552016aeb9e925582dab258ca5
base: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final.md@c87f17e6efb2469f46aca717d212cd22060818c8
base_blob: b55cd8d478be93012a295de8eb0cffd265b68429
KAN_K5: entities/kancelar/outbox/KAN__project-instructions-v3-k5-review__SHT-KOO.md@ceba72d839d5902265710eb167a08787a4fd50b5
KAN_K5_blob: 1b472a9d31a082f1bb21d7e607dbdb83c700f3a5
KAN_K5_terminal: PASS_KAN_V3_R03_K5_BASELINE_DIFF_REVIEW
KAN_prior_K1_K4_K6: entities/kancelar/outbox/KAN__project-instructions-v3-r03-rereview__SHT-KOO.md@26a1f9cec09da64605fdd29e6759eadf16c2c423
KAN_prior_blob: 5855007c7402bc00a3246a19312666a590375fea

Verified target lines 384–386:
`- exact UI Project Instructions v2 immutable export: AVAILABLE_AND_IMMUTABLY_CAPTURED`
`- preservation completeness versus UI predecessor: VERIFIED_BY_EXACT_BASELINE_DIFF`
`- this gap does not block candidate correction/re-review, but blocks complete predecessor diff/activation claim`

The third line is unchanged from the base, as the exact diff explicitly states. This is a present-tense contradiction inside the proposed payload, not a claim that KAN failed. An earlier distinct file `entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata-corrected.md`, blob `4f4a6eb352f9d1ab514e59df28f5b563dbd47c1e`, changed three lines and predates metadata2. It is evidence of a possible correction, not automatic approval target or supersession.

approval_gate: NOT_PREPARED
candidate_approval: NOT_GRANTED
ui_replacement: NOT_PERFORMED
active_project_sources_mutated: no
historical_prompt_replay: none
memory_layering_terminal: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION
memory_layering_attempt_3: NOT_AUTHORIZED

## Опыт

Идея: сравнить не только изменённые строки, но и весь служебный абзац, в котором они стоят. Проверка: immutable readback двух кандидатов и точное построчное сравнение. Результат: изменение двух строк подтверждено, третья противоречит новому состоянию K5. Урок: ограниченная правка может оставить ложную зависимость в соседней строке; точный diff и целостность не доказывают смысловую согласованность.

---
entity: KOO / КООРДИНАТОР
status: BLOCKED_KOO_PROJECT_INSTRUCTIONS_V3_METADATA2_INTERNAL_K5_CONTRADICTION
project_time: omitted
