# КООРДИНАТОР: решение ОПЕРАТОРА по точной версии Project Instructions v3

## Предмет решения

Сверка завершена. ШТАБИСТ исправил последнюю противоречащую строку в служебном блоке о UI v2. Проверка КАН K5 подтвердила сохранение исходного UI v2 и сравнение с финальным кандидатом. Ранее закрытые K1–K4/K6 остаются на проверенном содержательном основании. Новая версия меняет относительно metadata2 ровно одну служебную строку; содержательные разделы кандидата не менялись.

ОПЕРАТОР решает только, принимать ли **точный immutable текст** как утверждённый кандидат для будущей замены Project Instructions в UI. Ни это предложение, ни возможное «APPROVE» не выполняют фактическую замену UI, не активируют новые Project Sources и не разрешают работы по memory-layering.

**Точный payload решения:**
`puev5691/wellbeing-hq@8582e9205cecf43ba53a2eed652fa5e9aea861c8:entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata3.md`
Git blob: `79ddc8890d2fb4110b4edd287980ab57c66c2728`.
Читать полный текст именно по этому commit, а не по изменяемому `main`.

Этот текст вводит при утверждении обязательный сценарий terminal dialogue и предлагаемые правила orchestrator за пределами уже действующих инвариантов. Семантика BRIDGE применяется только в пределах отдельно утверждённого профильного contract; детали memory/Booster не повышаются до нормы. Действующие approved Project Sources кандидат не отменяет. КАН отметил: сохранность защитных правил v2 подтверждена по совокупности кандидата и действующих Sources, но не каждая редакционная формулировка v2 перенесена дословно.

## Отдельное решение

- **APPROVE:** ОПЕРАТОР явно утверждает указанный exact commit/blob как текст v3 для отдельного будущего шага UI replacement. Это не свидетельство установки и не полномочие автоматически заменить UI.
- **REJECT:** указанный exact commit/blob не утверждается; дальнейшее действие зависит от причины отклонения и отдельного решения.

До прямого ответа ОПЕРАТОРА статус `WAITING_OPERATOR_EXACT_APPROVAL_DECISION`. Если к моменту решения текущий UI-текст изменился или обнаружится новый competing/superseding result, решение по старому baseline останавливается на новой сверке.

## Проверка и provenance

repository: puev5691/wellbeing-hq
fresh_preflight_head: db2f633a24bb08624e52cdb8e91c5ad97f4714a5
current_writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md
current_writer_commit: 9781aeff09d868ade3f3e1a28f28014d23512386
current_writer_blob: ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
newer_competing_KOO_writer: not_found_in_fresh_tree
newer_competing_v3_terminal_or_candidate: not_found_in_fresh_tree

addressed_SHT_inbox: entities/koordinator/inbox/SHT__project-instructions-v3-metadata3-result__KOO.md
addressed_inbox_blob: c3f7d03ed2c6ad708ce045c831b357653beef455
SHT_terminal: entities/shtabist/outbox/SHT__project-instructions-v3-metadata3-result__KOO.md@a44e0dd89905dbb1400c48c35bdb065bc21f7816
SHT_terminal_blob: a9b1dacd67e831baeb677437e4077b803398b418
SHT_status: PASS_SHT_PROJECT_INSTRUCTIONS_V3_METADATA3_EXACT_ONE_LINE_CORRECTION
base: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata2.md@848a035d9616f68d0f47eb6acca0333be3f948d1
base_blob: 66626473e7d08e2d5d71021c3c2159e929b1b0d0
exact_diff: entities/shtabist/outbox/SHT__project-instructions-v3-metadata2-to-metadata3-exact-diff.md@31c61c60f45d4e1347ae530e895b49c9dda88169
exact_diff_blob: 0283182d61d535b59eeb8ee27c403a8f1dc9073f
independent_line_comparison: 395_to_395; changed_lines=1; line_386_only
old_line: `- this gap does not block candidate correction/re-review, but blocks complete predecessor diff/activation claim`
new_line: `- predecessor baseline gap: CLOSED_BY_OPERATOR_CAPTURE_AND_KAN_K5_PASS; candidate approval and UI activation remain separate explicit gates`
prior_KOO_blocker: entities/koordinator/outbox/KOO__project-instructions-v3-metadata2-blocker-r01__OPERATOR.md@2fe755aaa9034521785d1bb0cd7bc6f84785212f
prior_KOO_blocker_blob: 0c65610842273ccaa3289145ad1d0d967fed54b8
prior_blocker_disposition: RESOLVED_FOR_EXACT_METADATA3
KAN_K5: entities/kancelar/outbox/KAN__project-instructions-v3-k5-review__SHT-KOO.md@ceba72d839d5902265710eb167a08787a4fd50b5
KAN_K5_blob: 1b472a9d31a082f1bb21d7e607dbdb83c700f3a5
KAN_K5_terminal: PASS_KAN_V3_R03_K5_BASELINE_DIFF_REVIEW
KAN_prior_K1_K4_K6: entities/kancelar/outbox/KAN__project-instructions-v3-r03-rereview__SHT-KOO.md@26a1f9cec09da64605fdd29e6759eadf16c2c423
KAN_prior_blob: 5855007c7402bc00a3246a19312666a590375fea
UI_v2_baseline: entities/shtabist/outbox/SHT__ui-project-instructions-v2-baseline-operator-capture.md@21043ccd7d21175479876cb50ba5f3abdbcb6223
UI_v2_baseline_blob: 98586e84fb7fa43108b4040a8e7a5e312ee3670c

approval: NOT_GRANTED
ui_replacement: NOT_PERFORMED
active_project_sources_mutated: no
historical_PROMPT_replay: none
memory_layering_terminal: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION
memory_layering_attempt_3: NOT_AUTHORIZED

## Опыт

Идея: оценивать точный кандидат после исправления соседнего смыслового блока. Проба: readback по immutable commit и независимое построчное сравнение, затем сверка с KAN K5 и предыдущим blocker. Результат: внутреннее противоречие устранено одной строкой, содержательная нормативная проверка не переписывалась. Урок: approval относится к exact bytes; даже служебная корректировка требует отдельной immutable identity, тогда как установка UI остаётся следующим самостоятельным фактом.

---
entity: KOO / КООРДИНАТОР
status: WAITING_OPERATOR_EXACT_APPROVAL_DECISION
project_time: omitted
