# KOO → OPERATOR: OpenResearch / ШТАБ LOCAL preservation r0.1

status: CANDIDATE_PRESERVED_NOT_ACTIVE
project_time: omitted

## Смысл

По прямому решению ОПЕРАТОРА материал OpenResearch сохраняется для будущего изучения идеи и её практической реализации при появлении подходящего локального железа.

Эта фиксация НЕ запускает внедрение, не утверждает OpenResearch как production runtime и не меняет действующие governance/recovery/current-writer/source/file/task-conveyor правила ШТАБА.

## OPERATOR candidate basis

ОПЕРАТОР сформулировал архитектурное направление «ШТАБ LOCAL»:

- локальный ШТАБ хранит устойчивое состояние Сущностей, полномочия, recovery, current-writer, задачи, инструменты и историю;
- LLM рассматривается как заменяемый вычислительный компонент;
- Сущность не должна быть тождественна одной LLM-сессии или одному облачному чату;
- предпочтительна гибридная модель local LLM + внешние модели через разрешённый gateway;
- внешние системы доступны только через authority/policy gate и профильные инструменты;
- OpenResearch рассматривается как кандидат на отдельные механизмы исполнительного слоя, а не как замена governance ШТАБА.

Статус направления:
CANDIDATE / NOT ACTIVE.

Практическое изучение/реализация откладывается до появления подходящего локального оборудования.

## External source lock

Repository:
alphaXiv/OpenResearch

Requested branch:
main

Pinned commit for this preservation record:
27cb34200fe82957d33d37c143adf086408281d0

Pinned README:
alphaXiv/OpenResearch@27cb34200fe82957d33d37c143adf086408281d0:README.md

README blob:
6a91c2664192d3dcbf9b2d3e1bd99cfe65d52d20

Pinned LICENSE:
alphaXiv/OpenResearch@27cb34200fe82957d33d37c143adf086408281d0:LICENSE

LICENSE blob:
9797032ba850015adf4eed913c8cf879c20f2617

License observed:
MIT License

Future study must start from this immutable locator, then separately compare with the then-current upstream version. Do not silently replace this evidence with a newer main.

## Why it is relevant to ШТАБ LOCAL

Verified from the pinned README, OpenResearch currently presents:

- local-first workspace for research agents/autoresearch;
- independent agent sessions with isolated git worktrees;
- git-native experiment lineage;
- run/experiment evidence tied to code state and artifacts;
- local ownership of projects, conversations, experiments, runs, logs, code and artifacts;
- selectable agent/model backend;
- local-model support via LM Studio, oMLX, Ollama or custom endpoint with OpenCode;
- execution locally or on external compute;
- remote execution support including SSH and several cluster/compute backends;
- local dashboard and local SQLite storage by default.

These mechanisms are relevant as candidates for:
- isolated execution workspace;
- parallel bounded agent runs;
- experiment/run lineage;
- code-state binding;
- logs/artifact preservation;
- local/external model backend selection.

They are NOT accepted as replacements for:
- KOO routing authority;
- Project Sources;
- recovery;
- current-writer / Writer Gate;
- task authority;
- approval;
- delivery/receipt/acceptance semantics;
- secrets policy;
- automatic activation policy.

## Important security/architecture note for future study

Pinned README states that remote mode can run the workspace next to remote compute over SSH and that the remote service binds to loopback, but has no application-level authentication.

Therefore any future adoption must independently examine:
- authentication boundary;
- SSH/control-path trust;
- secrets isolation;
- per-Entity authority enforcement;
- audit/evidence model;
- multi-user host exposure;
- model/tool sandboxing;
- rollback/recovery;
- compatibility with current ШТАБ governance.

No conclusion is made here that the upstream defaults are safe enough for production ШТАБ use.

## Future trigger

Study may be resumed when OPERATOR declares suitable local hardware available.

At that point the first allowed architectural task should compare:
1. pinned OpenResearch commit above;
2. then-current upstream successor;
3. exact ШТАБ LOCAL requirements.

Expected study topics:
- runtime Сущности;
- persistent state;
- recovery/current-writer;
- model gateway;
- local LLM serving;
- tool/API gateway;
- secrets boundary;
- Git/GitHub information field;
- event/task queue;
- evidence/logging;
- backup/recovery;
- local vs external API boundary;
- exact OpenResearch components worth reusing vs rejecting.

## Current boundary

No hardware purchase authorized by this record.
No OpenResearch installation authorized.
No production use authorized.
No runtime migration authorized.
No automatic activation authorized.
No Project Source/canon mutation.
No current-writer change.
No task replay.

This is long-term preserved architecture material only.

## Terminal

PASS_KOO_OPENRESEARCH_SHTAB_LOCAL_CANDIDATE_PRESERVED_R01
