# SHT: анализ Project Instructions и актуализация

status: REVIEW_COMPLETE_UPDATE_REQUIRED
target: ChatGPT Project Instructions — ШТАБ БЛАГОПОЛУЧИЯ v2
proposed_successor: SHT__project-instructions-v3-candidate.md
authority_effect: none_until_operator_activation
project_time: omitted

## Человеческий вывод

Текущая Project Instructions v2 сохраняет правильный фундамент: подтверждённые источники, fail-closed достоверность, file-first, адресную доставку, recovery, минимальную загрузку контекста и запрет молча разрешать конфликт норм.

Но она отстала от active Project Core v2.5 и от разработок по memory-layering, Booster, activation lineage и orchestrator. Главный дефект — не ошибочные старые правила, а отсутствие новых общих границ. Из-за этого их приходится восстанавливать из отдельных результатов.

Нужен successor именно Project Instructions, а не новая версия Project Core.

## Оставить

- sources of truth и статусность;
- достоверность прежде исполнения;
- профильный owner/result/check;
- file-first;
- human-readable документы;
- locator delivery;
- minimal source loading;
- recovery по действующему канону;
- fail-closed при конфликте approved rules.

## Добавить/уточнить

1. Human-first для каждого human-facing ответа: что произошло → почему важно → где мы → что дальше.
2. Resume-First: fresh information-field/task/writer/recovery reconciliation до профильной работы; historical replay запрещён.
3. Serial cycle как default, но безопасные независимые parallel lanes допустимы; shared downstream decision требует reconciliation.
4. Memory boundary: integrity != semantic restoration != continuation != acceptance; raw/log/digest не authority; unknown сохраняется; selective retrieval.
5. Experience: reusable lesson + provenance/applicability/anti-regression; не плодить новый memory subsystem.
6. Booster: вспомогательный ресурс, не authority-bearing Entity; output = candidate/evidence до профильной проверки.
7. Orchestrator: materializes только уже разрешённый causal next step; не создаёт task/writer/approval/production authority.
8. Activation lineage: publication != dispatch != inbox != receipt != acceptance != activation_attempt != processing_started.
9. Manual и automatic activation используют одну causal/state model; stale/superseded work не replay.
10. OPERATOR после orchestrator не является ручным диспетчером/переносчиком файлов/сборщиком PROMPT.
11. Lightweight experience: идея → проба → результат → успех/неудача → фиксация; significant lesson → ARH, journal candidate → RED.
12. Memory/orchestrator/Booster не могут создавать authority друг для друга.

## Не переносить в Project Instructions

Не включать конкретные L0–L5 каталоги, provider/model Booster, реализацию orchestrator, JSON schemas, тестовые лимиты ML-E2E, серверы, расписания automations или полный task-conveyor/recovery алгоритм. Это профильные источники и implementation details.

## Рекомендация

Подготовить v3 candidate, затем:
KOO reconciliation → KAN bounded normative review → при необходимости ARH recovery impact → explicit OPERATOR approval → ручная замена Project Instructions.

Ни этот анализ, ни candidate не меняют active Project Sources и не утверждают новую норму.

---
КТО: SHT / ШТАБИСТ
СТАТУС: REVIEW_COMPLETE_UPDATE_REQUIRED
