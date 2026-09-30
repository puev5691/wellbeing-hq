# SIS -> SHT: progressive semantic context loader plan candidate r0.1

status: PLAN_CANDIDATE_NOT_ACTIVE
activation: NOT_AUTHORIZED
project_time: omitted
from_entity: SIS / СИСАДМИН
recipient: SHT / ШТАБИСТ

## Плановый смысл

Сохранить на радаре ШТАБа развитие существующей линии Entity Continuity / L0-L5 memory layering в сторону Semantic Engine, который управляет progressive disclosure контекста.

Immutable concept:

puev5691/wellbeing-hq@8f2d62970a83667d0966ca672b7bded1b026b5df:
ops/research/SEM__progressive-entity-context-loading-concept-r01-candidate.md

Статус концепции:
CANDIDATE_NOT_ACTIVE

## Ключевая архитектурная добавка

Existing memory layers уже описывают, что хранить:

L0 raw events/evidence
L1 operational state
L2 episodes/causal chains
L3 experience
L4 concepts/procedures
L5 digest

Новый candidate слой отвечает:

- какую Entity рассматривать как профильную;
- какой mandatory Reflex Kernel загрузить всегда;
- какой situational snapshot нужен сейчас;
- какой Profile Pack применим;
- какие L3/L2/L0 фрагменты раскрывать по semantic need;
- когда информации достаточно;
- когда нужно остановиться;
- когда сделать точный запрос к источнику/ОПЕРАТОРУ;
- как вернуть новый опыт на review/dedup без автоматического promotion.

## Инженерная модель

Reflex Kernel
-> Situational Awareness
-> Profile Pack
-> Relevant Experience
-> Exact Episode/Evidence
-> Targeted Query if still insufficient
-> bounded work
-> receipt
-> experience candidate

## Governance boundary

Semantic Engine:
- не создаёт task;
- не устанавливает writer;
- не превращает candidate в canon;
- не replay исторический PROMPT;
- не делает память источником authority;
- может предложить candidate Entity, но exact routing/authority остаётся у KOO/governance.

## Candidate profile owners

KOD:
semantic need vector, progressive loader, retrieval policy, context manifest, E2E harness.

ARH:
experience/preservation interface, provenance, freshness/applicability, dedup, reflective-learning boundaries.

SHT:
process and cross-Entity routing implications.

## Candidate next result

Только после отдельного exact authority:

KOD__semantic-progressive-context-loader-feasibility-r01.md

Минимальный вопрос:

Можно ли доказать на synthetic E2E, что новый instance получает малый bootstrap, сам обнаруживает недостающий semantic slot, загружает ровно релевантные L3/L2 evidence, не тащит full archive, не принимает память за authority и возвращает тот же результат, что independent oracle?

## Boundary

Это planning signal, а не исполняемая задача.

Не создавать production loader.
Не менять Project Sources.
Не менять current-writer.
Не активировать KOD/ARH автоматически.
Не считать сохранение концепции её acceptance.

---

КТО: SIS
ДЛЯ ЧЕГО: поставить на плановый радар ШТАБа Semantic Engine / progressive context loading как расширение уже существующей memory-layering архитектуры
СТАТУС: PLAN_CANDIDATE_NOT_ACTIVE
source: puev5691/wellbeing-hq@8f2d62970a83667d0966ca672b7bded1b026b5df:ops/research/SEM__progressive-entity-context-loading-concept-r01-candidate.md
approval_status: NOT_APPROVED_FOR_EXECUTION
responsibility_boundary: planning/reconciliation only
