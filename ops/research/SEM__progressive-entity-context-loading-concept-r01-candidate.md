# Semantic Engine: progressive entity context loading r0.1

status: CANDIDATE_CONCEPT_R01
activation: NOT_AUTHORIZED
production_use: NO
project_time: omitted
subject: semantic routing / progressive context loading / Entity continuity
candidate_profile_owner: KOD / КОДЕР
candidate_preservation_owner: ARH / АРХИВАРИУС
candidate_process_owner: SHT / ШТАБИСТ

## 1. Смысл

Семантический двигатель не должен быть просто поиском по архиву и не должен заранее загружать в каждый instance всю долговременную память Сущности.

Его функция:

1. определить, какая профильная Сущность нужна для события/задачи;
2. дать ей минимальное обязательное «рефлекторное ядро»;
3. восстановить ситуативную осведомлённость;
4. по мере работы выявлять недостающие смысловые области;
5. выборочно распаковывать релевантную память, опыт, эпизоды и evidence;
6. если подтверждённой информации всё ещё недостаточно — инициировать точный запрос к следующему источнику;
7. после результата вернуть новый проверенный опыт в долговременный контур.

Это progressive semantic bootstrap долговечной Entity поверх сменяемых processing instances.

## 2. Связь с уже существующей архитектурой

Концепция НЕ заменяет существующие линии:

- Entity Continuity / Task Persistence;
- L0–L5 layered memory;
- selective retrieval;
- recovery/current-writer gates;
- experience extraction;
- reflective learning.

Она добавляет отсутствующий control plane:

> какой слой и какой фрагмент памяти надо загрузить сейчас, почему именно его и когда остановить дальнейшее раскрытие контекста.

Existing memory model:

- L0 Raw event/evidence;
- L1 Operational state;
- L2 Episode / causal chain;
- L3 Experience memory;
- L4 Durable concepts/procedures;
- L5 high-density digest.

Navigation remains selective, but Semantic Engine becomes the policy/mechanism deciding the next disclosure step.

## 3. Аналогия с нервной системой

Аналогия используется только как инженерная модель.

### 3.1. «Спинной мозг» — Reflex Kernel

Загружается всегда и сразу.

Содержит только то, без чего Entity не имеет права начинать осмысленную работу:

- Entity identity / role;
- current approved project core;
- recovery/initiation rules;
- Writer Gate boundary;
- source-loading rules;
- task-conveyor rules;
- stop conditions;
- authority invariants;
- no-historical-replay rule;
- unknown stays unknown;
- memory does not create authority;
- tool does not expand role;
- minimal locator/provenance rules.

Reflex Kernel должен быть малым, стабильным и жёстко versioned.

Он не является «памятью обо всём». Это набор рефлексов, ограничителей и базовых схем восприятия.

## 4. «Датчики» — Situational Awareness Layer

Сразу после Reflex Kernel подгружается краткий текущий снимок ситуации.

Минимальные поля:

- exact current task / Task ID;
- current-writer state;
- instance state;
- supersession/revocation status;
- current dependencies;
- open blockers;
- safe next step;
- active external conditions;
- latest relevant receipts/results;
- environment/runtime facts needed for this task;
- what changed since last preserved state.

Это в основном L1 + минимально нужные L0 facts.

Ключевой принцип:

> Reflex Kernel отвечает «как вообще можно действовать», Situational Awareness отвечает «что происходит прямо сейчас».

## 5. Profile Pack — специализированная «кора»

После определения профильной Сущности загружается её role-specific pack:

- профильные approved sources;
- профильные процедуры;
- known invariants;
- anti-regression rules;
- durable concepts;
- типовые checks/preflight;
- capability boundaries;
- reusable domain vocabulary.

Это главным образом L4 + approved source profile.

Разные Entity получают разные Profile Pack при одном и том же Project Core.

## 6. Working Experience — релевантный опыт

После определения конкретной задачи Semantic Engine формирует semantic query не «по всей памяти», а по потребностям текущей Task.

Из L3 извлекаются только experience cards, у которых проверены:

- relevance;
- evidence refs;
- applicability boundary;
- freshness;
- confidence/status;
- supersedes/conflict;
- prohibited_repeat / next_time_behavior.

Старая карточка без applicability/freshness не должна автоматически попадать в рабочий контекст.

## 7. Episode / Evidence expansion

L2/L0 раскрываются только когда нужен ответ на конкретный вопрос:

- почему принято прошлое решение;
- где возникла ошибка;
- какое evidence подтверждало вывод;
- что именно произошло в предыдущей попытке;
- почему сработал anti-regression;
- не потерялась ли существенная причинная связь.

То есть обычный путь:

L5/L1 -> L4 -> L3 -> L2 -> L0

но не обязательно проходить все уровни.

Если L4/L3 уже достаточно для действия и provenance проверяем, raw episode не грузится.

## 8. Semantic Need Vector

Semantic Engine на каждом meaningful step формирует компактное описание дефицита контекста:

- entity_role;
- task_type;
- current_stage;
- risk_class;
- unresolved_claims;
- missing_decisions;
- missing_evidence;
- contradictions;
- confidence_gap;
- required_freshness;
- retrieval_budget;
- permitted_sources.

Пример:

NEED:
- domain = Telegram Bot API delivery
- unresolved = human sender provenance
- known = owner anonymous false, webhook absent
- missing = one post-boundary direct-human Update
- acceptable evidence = exact Bot API fields
- irrelevant = historical channel posts, usernames, display names

Так запрос становится не «дай всё про Telegram», а точным semantic retrieval contract.

## 9. Progressive Disclosure Loop

Рабочий цикл:

1. Bootstrap Reflex Kernel.
2. Load Situational Awareness.
3. Select Profile Pack.
4. Parse exact Task into required semantic slots.
5. Fill slots from current state / L4 / L3.
6. Check confidence and contradictions.
7. If sufficient -> work.
8. If insufficient -> request exact L2/L0 evidence.
9. Re-evaluate.
10. If still insufficient -> ask a targeted external/source/user question.
11. Before consequential action -> authority/input/version recheck.
12. Execute one permitted step.
13. Capture result/evidence.
14. Consolidate new episode/experience candidates.
15. Update digest/current state only through authorized owner.

Это не one-shot RAG. Это iterative semantic hydration.

## 10. Когда двигатель обязан запросить ещё память

Triggers:

- UNKNOWN required for next action;
- contradiction between current and retrieved state;
- missing immutable version;
- stale experience outside applicability;
- low confidence on high-risk decision;
- new stage of Task;
- failed attempt;
- unexpected result;
- before irreversible/external action;
- evidence requested by verifier;
- suspected supersession;
- new relation between formerly distant episodes.

## 11. Когда двигатель обязан остановить раскрытие

Stop retrieval if:

- all semantic slots needed for current bounded step are satisfied;
- next step is authorized and inputs exact;
- additional archive material would not change the current decision;
- retrieval budget reached and remaining gaps are non-material;
- source boundary prohibits deeper retrieval.

Hard STOP instead of guessing if:

- authority missing;
- required version cannot be proven;
- conflict unresolved;
- mandatory evidence absent;
- two current-writer claims conflict;
- recovery identity unclear.

## 12. Retrieval object / Context Manifest

Каждый loaded item получает metadata:

- locator;
- immutable version/hash;
- layer;
- normative_status;
- reason_loaded;
- query/need_id;
- applicability;
- freshness;
- confidence/status;
- supersedes/conflicts;
- bytes/tokens loaded;
- source owner;
- loaded_at_stage;
- context_loaded = true/false.

Это позволяет отличать:

- artifact was available;
- artifact was read;
- artifact entered semantic context;
- artifact influenced decision.

## 13. Authority Firewall

Semantic Engine никогда не должен выводить authority из релевантности.

Даже идеально релевантная память:

- не создаёт task;
- не устанавливает writer;
- не делает candidate active;
- не превращает old PROMPT в новое поручение;
- не делает receipt approval;
- не разрешает production action.

Semantic relevance и governance authority — независимые оси.

## 14. Memory Promotion

Новый опыт не попадает напрямую в «рефлексы».

Путь:

L0 event
-> L2 episode
-> L3 experience candidate
-> review/dedup/evidence check
-> confirmed/bounded/rejected
-> при повторяемости и достаточной проверке L4 concept/procedure
-> только отдельным governance решением часть L4 может стать approved Reflex Kernel rule/source.

Это защищает систему от превращения одной неудачи в вечный рефлекс.

## 15. Reflective Learning

Периодический или event-triggered reflective cycle:

- ищет повторы;
- сравнивает удалённые эпизоды;
- ищет одинаковую структуру проблемы при разных предметных областях;
- формирует candidate pattern;
- требует проверку;
- после подтверждения предлагает L3/L4 update.

Пример текущего события:

наблюдение:
несколько попыток Telegram verification ломались не из-за предметной логики, а из-за wall-clock window, process lifetime, concurrent observers и human timing.

semantic abstraction:
локальный wall-clock / краткое окно — системный источник хрупкости повторяемых distributed workflows.

transfer hypothesis:
общий deterministic event sequence может быть лучше локального времени как trigger basis.

candidate concept:
WBN block height as logical conveyor clock.

Именно такой перенос между эпизодом и новой архитектурой Semantic Engine должен уметь поддерживать.

## 16. Выбор профильной Entity

Semantic Engine может участвовать в routing, но не единолично назначать authority.

Pipeline candidate:

incoming event
-> classify semantic domain
-> determine candidate Entity role
-> load that Entity Reflex Kernel/Profile Pack
-> verify exact task routing/authority
-> if routing evidence insufficient, return to KOO
-> only then begin profile work.

То есть semantic classifier может сказать:
«это похоже на SIS/KOD/SHD»,
но фактическое назначение задачи остаётся у разрешённого routing/governance contour.

## 17. Cold Start target

Новый instance должен сначала получить очень маленький пакет:

A. Reflex Kernel
B. Entity identity/profile pointer
C. current-writer/recovery proof
D. exact active Task
E. L5 digest
F. L1 state
G. semantic need vector

После этого память раскрывается по demand.

Это уменьшает:
- token cost;
- stale-context risk;
- случайное смешение старых задач;
- вероятность last-write-wins мышления;
- cold-start latency.

## 18. Failure modes

Нужно отдельно тестировать:

- over-retrieval;
- under-retrieval;
- stale experience chosen over fresh state;
- candidate treated as canon;
- digest treated as truth;
- memory treated as authority;
- cross-Entity leakage;
- raw event promoted without verification;
- conflicting experience silently merged;
- semantic query too broad;
- retrieval loop without stop condition;
- relevant evidence available but not loaded;
- irrelevant archive dominating context.

## 19. Minimal E2E experiment

Одна synthetic Entity, одна unfinished Task.

Cold start получает только:
- Reflex Kernel;
- L5;
- L1;
- exact Task.

Task специально требует факта, отсутствующего в bootstrap.

Expected behavior:

1. Semantic Engine detects missing slot.
2. Generates exact Need Vector.
3. Retrieves one relevant L3 card.
4. Card references exact L2 evidence.
5. L2 evidence resolves the missing slot.
6. Irrelevant L0 archive remains unloaded.
7. Task continues.
8. New result creates one candidate experience.
9. A second instance repeats cold start and uses the promoted lesson without full archive.

PASS:
- correct Entity selected;
- mandatory reflexes always loaded;
- no unauthorized work;
- relevant memory retrieved;
- irrelevant archive not loaded;
- missing evidence causes exact request, not guess;
- stale/conflicting item causes blocker;
- semantic context smaller than full corpus;
- task outcome equals independent oracle;
- provenance trace explains every loaded item.

## 20. Relation to Block Clock

Block Clock and Semantic Engine are complementary.

Block Clock answers:
WHEN should an already permitted check/activation be considered?

Semantic Engine answers:
WHO is the candidate specialist and WHAT context does it need now?

Task Conveyor/Governance answers:
IS this activation/task actually authorized?

Combined:

block/event trigger
-> semantic classification
-> governance/routing verification
-> Entity bootstrap
-> progressive context loading
-> bounded work
-> receipt
-> experience extraction
-> future semantic routing.

## 21. Suggested implementation split

KOD:
- semantic need vector schema;
- retrieval policy;
- context manifest;
- progressive loader;
- retrieval trace;
- bounded E2E harness.

ARH:
- memory layer storage/preservation;
- experience review/dedup;
- provenance/freshness/applicability;
- semantic recovery verification;
- reflective-learning corpus boundaries.

SHT:
- process/governance implications;
- cross-Entity routing boundary;
- candidate plan/reconciliation.

KOO:
- exact task routing;
- authority verification;
- next-step decisions.

## 22. Status and next profile result

This is a candidate extension of existing memory-layering architecture.

Not a new Project Source.
Not production-authorized.
Not an automatic routing authority.

Candidate next result after separate exact authorization:

KOD__semantic-progressive-context-loader-feasibility-r01.md

Expected:
- exact boot layers;
- Need Vector schema;
- retrieval precedence;
- stop/escalation rules;
- Context Manifest schema;
- one synthetic E2E;
- token/byte metrics;
- anti-regression cases;
- ARH preservation interface;
- no production activation.

---

КТО: SIS / concept synthesis по прямому обсуждению с ОПЕРАТОРОМ
ДЛЯ ЧЕГО: встроить предложенную модель «рефлексы + ситуативная осведомлённость + progressive memory disclosure» в уже существующую Entity Continuity / L0-L5 архитектуру
СТАТУС: CANDIDATE_NOT_ACTIVE
source_basis:
- puev5691/wellbeing-hq:entities/koder/current/concepts/automation/entity-continuity-task-persistence.md blob cd9a0761969f0e41a7a6c7a19d4303c6198e2d99
- puev5691/wellbeing-hq:entities/koder/outbox/KOD__entity-layered-memory-event-lineage__ALL.md blob 0ec0b1553c8bbe3fbaf6e2436213772670b53ea7
- puev5691/wellbeing-hq:entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0
- OPERATOR semantic-engine proposal in current discussion
approval_status: NOT_APPROVED_FOR_EXECUTION
responsibility_boundary: concept/preservation only; no routing authority, no writer change, no source promotion, no production loader
