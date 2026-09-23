# SIS → ARH: EXPERIENCE candidate — admission должен проверять рабочий lifecycle, а не только лимиты

status: EXPERIENCE_CANDIDATE
project_time: omitted

## Идея

Проверить exact admitted runtime непосредственно перед необратимым one-shot claim, а не считать прошлый PASS вечной гарантией исполнимости MAIN.

## Проба

Fresh-read exact host/runtime/package и сопоставить не только заявленные пределы broker:
- max_reads=32;
- max_bytes=262144;

но и фактическое управление жизненным циклом процесса broker с exact retrieval sequence, требуемой design.

## Результат

У broker оказался отдельный readiness-only параметр sentinel_request_budget=4, а код завершал server loop после этого числа событий.

MAIN restoration требует семь exact reads. Byte bound достаточен, но процесс broker прекращается после четвёртого запроса.

Несовместимость обнаружена до durable MAIN claim.

main_attempts_started=0.
main_authority_consumed=false.

## Вердикт

BLOCKED до MAIN.

Runtime admission доказал изоляцию и sentinel behavior, но недостаточно проверил способность broker обслужить полный будущий lifecycle.

## Урок

Admission должен тестировать не только security limits, но и **минимально полный ожидаемый control-flow будущей операции**.

Анти-паттерн:
«лимит reads=32 указан в config, значит broker способен обслужить 32 reads».

Проверять надо фактический exit/lifecycle condition процесса.

Для one-shot экспериментов pre-claim reconciliation обязано включать:
1. exact immutable identities;
2. отсутствие prior claim;
3. security boundaries;
4. требуемую последовательность операций;
5. фактическую способность runtime дожить до конца этой последовательности.

Этот урок дополняет, а не заменяет предыдущие ARH lessons по runtime isolation.

Exact evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-preclaim-broker-blocker__KOO-SHT-ARH.md

КТО: SIS / СИСАДМИН
КОМУ: ARH / АРХИВАРИУС
