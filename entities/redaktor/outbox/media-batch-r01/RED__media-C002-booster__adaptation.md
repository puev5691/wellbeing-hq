# RED media adaptation — C002

content_id: `C002`
title: `Booster: почему работающий канал ещё не означает полезный инструмент`
publication_status: `CANDIDATE_ONLY`
PUBLICATION_AUTHORITY: `NONE`
EXTERNAL_PUBLICATION: `NOT_PERFORMED`
project_time: omitted

## Telegram adaptation

### Booster заработал. И это ещё ничего не доказало

Сначала мы проверяли простую вещь: способен ли внешний ответ пройти через систему так, чтобы служебный reasoning не превратился в «готовый результат», а одноразовое разрешение нельзя было незаметно повторить.

Первый живой вызов вернулся с HTTP 200, но система остановилась: форма ответа оказалась сложнее ожидаемой. Вместо красивого отчёта получилось полезное «нет»: результат не был выдуман.

После узкой коррекции весь технический тракт прошёл полностью.

И тут возник более неприятный вопрос:

**а Booster вообще помогает работать быстрее или лучше?**

Первый utility-опыт с маленьким лимитом ответа не дал пользовательского текста. Причина, связанная с лимитом токенов, осталась гипотезой: нужной диагностики тогда ещё не сохраняли.

Во втором опыте изменили только один существенный параметр: лимит 64 → 1024. Ответ уже появился. Но его отверг наш собственный checker, который оказался строже исходного задания.

Checker исправили отдельно. Исходный FAIL не переписали. На тех же байтах и baseline, и candidate потом прошли 8/8 тестов.

И ещё одна неприятность: на этой маленькой задаче ускорения не наблюдалось.

**Вывод:** технический PASS, правильный ответ и практическая польза — три разных доказательства. Если смешать их в одно слово «работает», эксперимент превращается в рекламу самому себе.

## Portal mapping

### Intended longform structure
1. Зачем Booster вообще строился: bounded external assistance.
2. Wiring gap: проверенные компоненты ещё не система.
3. Первый live response и fail-closed на reasoning container.
4. Узкая normalizer correction и первый full-path PASS.
5. Переход от технического PASS к utility question.
6. r0.1: limit 64, reasoning-only, candidate отсутствует.
7. Observability gap и failure-metadata correction.
8. r0.2: единственное намеренное изменение 64 → 1024.
9. Candidate появился, но checker не соответствовал specification.
10. Original `needs_rework` остаётся историческим фактом.
11. Post-hoc 8/8 на неизменных байтах.
12. Измерения: на маленькой задаче speedup не наблюдался.
13. Что пока неизвестно: applicability across task classes.

### Source / provenance
Primary RED synthesis:
- `puev5691/wellbeing-hq@7d856fe18075af40515d1ff0843882896ccad6aa:entities/redaktor/current/literary-journal/RED__project-literary-journal.md`
- journal blob after consolidation: `37bf61e6cdb58a31a0afb2a914792c83634b5f30`

Underlying evidence refs retained in that chapter include:
- SIS/KOD full-path and reasoning-correction lineage;
- `entities/sisadmin/outbox/SIS__booster-utility-pilot-r01-one-shot-live-terminal__KOO.md`;
- `entities/koder/outbox/KOD__booster-utility-pilot-r01-no-assistant-text-diagnosis__KOO.md`;
- `entities/koder/outbox/KOD__booster-failure-diagnostic-metadata-r01-result__KOO-SIS.md`;
- `entities/koder/outbox/KOD__booster-utility-pilot-r02-max1024-precall-result__KOO-SIS.md`;
- `entities/koder/outbox/KOD__booster-utility-pilot-r02-requester-decision__KOO-SIS.md`;
- `entities/sisadmin/outbox/SIS__booster-utility-r02-checker-spec-alignment-r01-independent-verify__KOO.md`.

### Factual / non-claim boundaries
- token-budget causality for r0.1 remains unconfirmed;
- 64→1024 is an observed experimental change, not proven cause of r0.2 success;
- original requester decision `needs_rework` is not rewritten;
- post-hoc 8/8 is not retroactive original-gate PASS;
- no general claim that Booster improves or worsens productivity;
- N=1/N=2 does not support universal conclusions;
- technical PASS does not imply product/business value;
- no production/standing-use claim.

### Dependencies before publication
- RED public copyedit and terminology simplification;
- KAN review of external-provider/model naming and public technical boundary;
- KOO release decision;
- explicit OPERATOR release;
- WEB exact publication task after release.

portal_production_deployment_claim: `none`
