# KOO development direction: Telegram + four-model context engine r0.1

status: DEVELOPMENT_DIRECTION_RECORDED_NOT_ACTIVATED
entity: KOO / КООРДИНАТОР
project_time: omitted

## Человеческий смысл

ОПЕРАТОР поручил заложить в разработку общий контекстный двигатель для будущего Telegram-диалога, соединённого с несколькими нейронными провайдерами.

Цель не сводится к переключателю между API.

Нужен собственный orchestration/context layer, который:
- принимает человеческий Telegram-ввод;
- восстанавливает релевантный контекст и causal state;
- формализует задачу;
- выбирает модель/модели и роли;
- отделяет фактологию от гипотез;
- запускает критику/контрпроверку там, где она полезна;
- сохраняет мотивационный/человеческий слой отдельно от evidence;
- собирает согласованный итог;
- не теряет следующий причинный шаг;
- хранит проверяемую историю без превращения полного transcript в prompt;
- работает поверх провайдеров, не делая одного провайдера источником истины.

## Provider set for design

Initial intended provider set:

1. OpenAI
2. Anthropic
3. Google Gemini
4. DeepSeek

Provider inclusion here is a development target, not proof of live connector/API readiness or entitlement.

Existing project evidence for OpenAI/Anthropic and Telegram should be fresh-reconciled before implementation.
Gemini and DeepSeek require separate current capability/connector/API verification when their implementation turn arrives.

## Proposed architecture

### 1. Telegram ingress

Responsibilities:
- normalize inbound Telegram event;
- preserve user message identity/thread/conversation context where available;
- avoid storing unnecessary raw personal/audience data;
- separate transport receipt from semantic acceptance;
- pass normalized event to context engine.

### 2. Context engine

Core responsibility:
produce a bounded CONTEXT_PACKET for one reasoning cycle.

Possible layers:

A. Human input layer
- exact user message;
- reply/thread relation;
- attachments refs;
- language/style hints.

B. Current causal state
- exact current task/goal;
- last durable terminal;
- blockers;
- next allowed transition;
- authority/effectivity boundaries.

C. Relevant memory/recovery
- compact evidence-backed state;
- no full transcript by default;
- stale/unknown marked explicitly.

D. Knowledge/evidence bundle
- project Sources;
- exact task artifacts;
- fresh web/external sources when required;
- provenance labels.

E. Behavioral kernel
- fact-first;
- critique-before-completion;
- causal continuation;
- human explanation;
- no authority inference;
- no dead-end handoff.

F. Model-routing policy
- one-model fast path;
- multi-model parallel consultation;
- specialist critic;
- verifier;
- synthesis.

G. Output contract
- human answer;
- evidence/provenance;
- unresolved unknowns;
- next causal step;
- operator/user action if any.

## Model roles are dynamic, not permanently attached to brands

Do not hard-code:
OpenAI = thinker,
Anthropic = critic,
Gemini = search,
DeepSeek = coder.

Instead use provider capability profiles and task-level role assignment.

Candidate roles:
- PRIMARY_REASONER
- FACT_CHECKER
- CRITIC
- COUNTERARGUMENT
- CODE_SPECIALIST
- SOURCE_REVIEWER
- SUMMARIZER
- SYNTHESIZER
- SAFETY_BOUNDARY_CHECK
- HUMAN_INTERFACE_REVIEW

One provider may serve multiple roles; several providers may compete for the same role.

## Multi-model coordination modes

### FAST_SINGLE
One selected provider, minimal context.

### PRIMARY_PLUS_CRITIC
Primary answer + independent critic + corrected synthesis.

### PARALLEL_PANEL
2-4 independent responses over the same frozen context packet.

### FACT_THEN_SYNTHESIS
One or more evidence-oriented passes first, synthesis only after evidence normalization.

### ADVERSARIAL_REVIEW
Primary proposal + explicit counterexample/failure-mode review.

### CONSENSUS_WITH_DISSENT
Synthesis records:
- agreement;
- disagreements;
- unresolved evidence;
- minority objection when materially relevant.

No simple majority vote is treated as truth.

## Context packet invariants

Every model invocation should receive only the minimum necessary packet.

Packet should distinguish:

FACT
INFERENCE
USER_PREFERENCE
PROJECT_RULE
CANDIDATE
UNKNOWN
BLOCKER
AUTHORITY
TASK
TERMINAL
MEMORY_HINT

Memory/model output never self-promotes to FACT or AUTHORITY.

Provider response should return structured metadata sufficient to preserve:
- model/provider identity;
- requested role;
- evidence refs used;
- claims needing verification;
- confidence only as self-report, never as proof;
- suggested next step.

## Context engine decision loop

1. normalize user event;
2. classify intent/task;
3. resolve current project/user context;
4. establish authority/scope where applicable;
5. construct minimal context packet;
6. choose orchestration mode;
7. select provider(s);
8. invoke;
9. normalize provider outputs;
10. detect conflicts/unknowns;
11. optionally invoke critic/verifier;
12. synthesize human answer;
13. run continuity/pre-send check;
14. deliver;
15. persist only durable derived state/evidence needed for future continuation.

## Failure philosophy

Fail closed on:
- missing required authority;
- stale task identity;
- contradictory authoritative state;
- provider-origin mismatch;
- unverified external-send action;
- missing evidence required for factual claim;
- ambiguous next step where project action would follow.

Do not fail merely because providers disagree.
Disagreement becomes explicit evidence for review.

## Telegram-human layer

The Telegram participant should experience one coherent interlocutor, not four chatbots shouting into a bucket.

Default behavior:
- normal Russian prose;
- explain uncertainty;
- do not expose internal orchestration unless useful;
- ask fewer questions when context can safely resolve them;
- keep one next action;
- support lightweight chat and deep project mode separately.

## Future searchable/queryable request history

Context engine should support semantic indexing/classification of user requests without forcing the user to manually tag every message.

Candidate dimensions:
- topic;
- entity/project line;
- intent;
- task/decision/question/idea/result/blocker;
- causal parent;
- status;
- related artifacts;
- model/provider cycle;
- user-defined labels.

This enables future queries such as:
- "покажи мои решения по Telegram";
- "все мои идеи про память";
- "что я поручал SIS по p552203";
- "какие вопросы остались без ответа";
- "какие мои запросы породили task, но не terminal".

This indexing is a derived search layer, not authoritative task state.

## Relationship to Entity Operational Continuity

The context engine should reuse the continuity concepts currently under bounded candidate pilot:

- derived current-state capsule;
- causal/conveyor head;
- pre-send continuity validation;
- explicit WAIT/NONE basis;
- decision request != granted authority;
- dispatch != receipt;
- execution terminal != handoff quality.

Do not make the continuity candidate universally active merely by reusing its ideas in design.

## Development sequencing

This direction is added to development backlog without disturbing the current top-priority STP-C/P552203 causal line.

Future sequence, when activated:

1. fresh multi-provider/connector capability reconciliation:
   OpenAI / Anthropic / Gemini / DeepSeek;
2. Telegram ingress/current bridge reconciliation;
3. define canonical normalized event;
4. define CONTEXT_PACKET r0.1;
5. define provider capability profile schema;
6. define routing/orchestration policy;
7. define response normalization schema;
8. define critique/synthesis policy;
9. privacy/storage/logging review;
10. offline simulator with mock providers;
11. independent stress-review;
12. bounded Telegram sandbox pilot;
13. only then live multi-provider use.

## Explicit boundaries

This record does NOT:
- activate implementation now;
- change current task priority;
- wake KOD/SIS/SHD;
- call any provider;
- install credentials;
- change Telegram runtime;
- create automatic routing authority;
- activate Entity Operational Continuity candidate universally;
- mutate Project Sources/canons.

## Queue disposition

Development line:
MULTIMODEL_TELEGRAM_CONTEXT_ENGINE_R01

status:
PAUSED_BACKLOG_DIRECTION

Current priority remains governed by existing verified conveyor until OPERATOR separately changes it.

## Terminal

RECORDED_MULTIMODEL_TELEGRAM_CONTEXT_ENGINE_R01_DEVELOPMENT_DIRECTION
