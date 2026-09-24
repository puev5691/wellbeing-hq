# Решение ОПЕРАТОРА: текст Project Instructions v3 одобрен

## Что решено

ОПЕРАТОР прочитал предоставленный файл с полным текстом кандидата и прямо сообщил КООРДИНАТОРУ: «Текст Project instructions v3 - одобряю, готов перенести его для замены существующей инструкции проекта ШТАБ БЛАГОПОЛУЧИЯ».

Это явное утверждение точного текста `metadata3` для ручной замены существующей UI Project Instructions. ОПЕРАТОР заявил готовность самостоятельно перенести его. Фактическая установка в UI этим сообщением и настоящей записью не доказана.

Следующий единственный ручной шаг: ОПЕРАТОР вставляет полный текст утверждённого файла в поле инструкций проекта «ШТАБ БЛАГОПОЛУЧИЯ» и сохраняет. После этого требуется отдельный readback именно сохранённого UI-текста и сравнение с immutable утверждённой версией. До readback нельзя объявлять UI activation PASS.

## Точная версия и основание

repository: puev5691/wellbeing-hq
fresh_preflight_head_before_record: a8c10f36dcb97986abc80a939fd3842374683f88
current_KOO_writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md
current_KOO_writer_commit: 9781aeff09d868ade3f3e1a28f28014d23512386
current_KOO_writer_blob: ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
approval_gate: entities/koordinator/outbox/KOO__project-instructions-v3-metadata3-approval-gate-r01__OPERATOR.md@a8c10f36dcb97986abc80a939fd3842374683f88
approval_gate_blob: b7f3d8653bc6f818bb61f2b79b0a4f25cc64c20e

approved_target: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata3.md
approved_target_commit: 8582e9205cecf43ba53a2eed652fa5e9aea861c8
approved_target_blob: 79ddc8890d2fb4110b4edd287980ab57c66c2728
approved_target_locator: puev5691/wellbeing-hq@8582e9205cecf43ba53a2eed652fa5e9aea861c8:entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final-metadata3.md
approval_authority: direct OPERATOR decision in current KOO conversation after delivery of exact full-text download and approval gate

## Раздельные состояния

exact_text_approval: APPROVED_BY_OPERATOR
manual_ui_replacement: OPERATOR_READY_NOT_YET_VERIFIED
post_replacement_ui_readback: NOT_PERFORMED
ui_activation: NOT_VERIFIED
active_project_sources_mutated: no
historical_prompt_replay: none
memory_layering_terminal: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION
memory_layering_attempt_3: NOT_AUTHORIZED

Не подменять UI readback ссылкой на GitHub или фактом скачивания файла. При ошибке вставки, обрезании текста или несовпадении сохранённого UI вернуться к точной диагностике без ложного activation PASS.

---
entity: KOO / КООРДИНАТОР
status: APPROVED_OPERATOR_V3_METADATA3_PENDING_MANUAL_UI_REPLACEMENT_AND_READBACK
project_time: omitted
