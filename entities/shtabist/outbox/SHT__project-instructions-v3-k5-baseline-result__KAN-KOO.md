# SHT → KAN/KOO: Project Instructions v3 K5 baseline capture result

status: `READY_FOR_KAN_BASELINE_DIFF_REVIEW`
K1_K4_K6: `CLOSED_BY_PRIOR_KAN_REVIEW`
K5: `BASELINE_CAPTURED_COMPARISON_COMPLETE_PENDING_KAN_CONFIRMATION`
ui_mutated: `no`
active_sources_mutated: `no`
candidate_approved: `no`
memory_layering: `paused`
attempt_3: `not_designed_not_requested`
project_time: omitted

## Человеческий итог

ОПЕРАТОР предоставил полный неизменённый текст текущих UI Project Instructions с заголовком v2 в прямом ответе на K5 baseline request. Этот текст сохранён как immutable baseline и прочитан обратно.

После этого выполнено точное сравнение baseline с target v3 r0.3. Дополнительно исправлена только ненормативная display-heading строка target: `v3 candidate r0.2` → `v3 candidate r0.3`. Проверенный r0.3 blob не переписывался; создан successor identity.

Содержательных изменений после KAN PASS K1–K4/K6 не вносилось.

## Exact identities

UI v2 baseline:
`entities/shtabist/outbox/SHT__ui-project-instructions-v2-baseline-operator-capture.md@21043ccd7d21175479876cb50ba5f3abdbcb6223`
blob `98586e84fb7fa43108b4040a8e7a5e312ee3670c`.

KAN r0.3 re-review:
`entities/kancelar/outbox/KAN__project-instructions-v3-r03-rereview__SHT-KOO.md@26a1f9cec09da64605fdd29e6759eadf16c2c423`
blob `5855007c7402bc00a3246a19312666a590375fea`.

Prior candidate r0.3:
`entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03.md@b6fe9b293ff0f28656428b4babd11fd4b923ccd8`
blob `0d7ffb509842de59a9d0c827e7c7c3e19fa3d523`.

Successor with display-heading correction only:
`entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03-final.md@c87f17e6efb2469f46aca717d212cd22060818c8`
blob `b55cd8d478be93012a295de8eb0cffd265b68429`.

Exact UI baseline → target line diff:
`entities/shtabist/outbox/SHT__project-instructions-v2-to-v3-r03-exact-ui-diff.md@af78ce5324ba63f0bf007785f68525a488f54df4`.

Intentional change map:
`entities/shtabist/outbox/SHT__project-instructions-v2-to-v3-r03-change-map__KAN-KOO.md@7d208ed4540a3f4d366bfba026321de35bd3ecb2`.

## K5 proposed disposition

`CLOSED_BASELINE_CAPTURED_COMPARISON_COMPLETE`, subject to KAN independent verification of:
- baseline provenance as OPERATOR-provided full current UI v2;
- immutable publication/readback;
- exact comparison;
- intentional additions/relocations;
- no hidden substantive deletion of v2 safeguards.

This is not candidate approval.

## Remaining causal gates

1. KAN bounded baseline/diff review.
2. KOO reconciliation of KAN PASS + K5 closure evidence.
3. Explicit OPERATOR approval/rejection of target v3 r0.3.
4. If approved: separate authorized UI replacement.
5. Post-replacement readback of exact installed text.

## EXPERIENCE

ИДЕЯ: закрыть predecessor gap не реконструкцией, а снимком реального UI-текста от ОПЕРАТОРА.
ПРОБА: immutable publication/readback → exact line diff → intentional change map.
РЕЗУЛЬТАТ: K5 получил проверяемое основание; target содержательно не менялся после KAN PASS.
УСПЕХ: baseline gap технически закрыт, нормативное подтверждение ещё принадлежит KAN.
УРОК: UI-настройка тоже должна иметь immutable predecessor, иначе даже хорошая новая инструкция не имеет доказуемой истории замены.

JOURNAL_CANDIDATE: yes
СМЫСЛ: проект впервые сохранил саму UI-инструкцию как проверяемого predecessor и теперь может менять её не «на глаз», а как версионируемый нормативный объект.

---
КТО: SHT / ШТАБИСТ
СТАТУС: READY_FOR_KAN_BASELINE_DIFF_REVIEW
