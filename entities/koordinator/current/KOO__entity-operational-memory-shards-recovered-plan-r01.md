# KOO current plan: Entity operational memory + shards r0.1

status: RECOVERED_PLAN_ACTIVE
project_time: omitted

## Главная цель

ОПЕРАТОР не должен при замене или новом экземпляре Сущности вручную пересказывать:
- чем Сущность занималась;
- что уже сделано;
- какие решения приняты;
- где остановилась причинная цепочка;
- какие факты, опыт и зависимости уже накоплены;
- какой следующий шаг разрешён.

Новый экземпляр должен восстановить это из проверяемого внешнего состояния и продолжить работу без потери причинной цепочки.

## Архитектурный смысл

GitHub остаётся каноническим внешним слоем доказательств и значимых решений.

GitHub НЕ должен использоваться как оперативная память для каждого промежуточного чтения/записи.

Целевая причинная цепочка:

Entity
-> operational memory / shard
-> File/Artifact Service
-> seal / verify / checkpoint
-> GitHub canonical publish/readback только для значимых результатов
-> recovery/bootstrap нового экземпляра
-> selective retrieval
-> continuation exact task

## Требуемые слои памяти

1. Governance / identity
   - role
   - authority
   - current-writer / Writer Gate
   - active exact task

2. Operational working memory
   - промежуточные факты;
   - рабочие гипотезы;
   - краткоживущее состояние шага;
   - текущий cursor/causal chain;
   - промежуточные locators/results.

3. Current state / checkpoint
   - проверенное состояние задачи;
   - незавершённые зависимости;
   - последний подтверждённый результат;
   - следующий разрешённый шаг;
   - stop conditions.

4. Experience
   - проверяемые повторяемые уроки/anti-regression facts;
   - не подменяет current state или authority.

5. Library / durable knowledge
   - устойчивые материалы, источники, технические знания и внешние locators;
   - загружаются выборочно, не весь архив.

6. Canonical GitHub evidence
   - решения;
   - accepted/current state;
   - значимые checkpoints;
   - immutable package/result identities;
   - не мелкая оперативная телеметрия.

## Уже существующие компоненты

### Git operational shards direction

puev5691/wellbeing-hq@87c278e5d99f102b9c148104a56e5009ab49a005:
entities/koordinator/outbox/KOO__git-operational-shards-priority-r01__OPERATOR.md

Target:
Entity -> fast local/host file service -> batch/seal/check -> GitHub canonical publish/readback

### File/Artifact Service direction

puev5691/wellbeing-hq@b62896ff271ab0480a4ff1fcecef386a7c65b1b6:
entities/koordinator/outbox/KOO__file-artifact-git-shards-r01__PROJECT.md

Existing MVP failed independent verification at:

puev5691/wellbeing-hq@b6849cd2aa9d45fea823b06f05d45053d968d2cb:
entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md

Exact known defects:
1. committed bytes did not match package MANIFEST for 11/12 records;
2. reserved generated MANIFEST.json target collision accepted;
3. prior_manifest_path could escape source_root;
4. create_archive type contract was not fail-closed.

Concept was not rejected; correction-only successor was the stated minimal next action.

### Shard gateway

Mazhor current verified runtime evidence:

puev5691/wellbeing-hq@19c360d694f2274236942b9e8f4b792003a13bcd:
entities/sisadmin/outbox/SIS__mazhor-shard-gateway-option-a-current-state__KOO.md

State:
- successor runtime r0.3 installed;
- verify unit succeeds;
- no listener;
- WRITE not enabled;
- no credential access;
- no production acceptance.

### Memory-layering

Isolated runtime feasibility:

puev5691/wellbeing-hq@930e90b32dddb33aad133d8303ecaa6b49348f42:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-isolated-runtime-feasibility__KOO-SHT.md

Feasible host:
mazhor / p552203.kvmvps

Attempt 2 terminal:

puev5691/wellbeing-hq@7cfcfb611dd9e1a66fcb5dd2ff4e460fb8003a86:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-result__KOO.md

terminal:
FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION

Meaning:
scenario itself was NOT tested.
Execution stopped before OLD-01 because verifier import created __pycache__ inside immutable package.
Attempt 2 consumed.
Attempt 3 remains NOT_AUTHORIZED.

Required harness lesson:
immutable package verification must be physically non-mutating, e.g. python -B / PYTHONDONTWRITEBYTECODE=1 and preferably read-only projection.

### Reusable host transport

Standing fixed-IP -> Commander transport current state:

puev5691/wellbeing-hq@59848480752f5096d07866e747bf894c3559270a:
entities/koordinator/current/KOO__fixed-ip-commander-standing-transport-current-r01.md

status:
STANDING_TRANSPORT_ACTIVE_PER_ACTION_AUTHORITY_REQUIRED

This solves reusable node/device transport selection.
It does not grant host-command authority.

## Acceptance criterion for the whole program

A replacement Entity passes only if, without OPERATOR retelling prior work, it can:

1. establish role and governance boundary;
2. establish current-writer state;
3. locate the active exact task;
4. load only the required current/checkpoint memory;
5. selectively retrieve supporting operational/library/experience records;
6. state the last verified result;
7. reconstruct the unfinished causal chain;
8. state the next already-authorized step;
9. continue the task without replaying completed prefix work;
10. preserve authority/supersession boundaries;
11. avoid using GitHub for high-frequency scratch operations;
12. publish to GitHub only bounded significant state/results/checkpoints;
13. survive shard failure without silently changing canonical project truth.

Human success criterion:
OPERATOR does not have to explain the history of the work to the replacement Entity.

## Performance criterion

The pilot must count and compare:
- operational shard reads/writes;
- GitHub reads/writes;
- bytes transferred;
- number of canonical GitHub publications;
- replacement recovery latency;
- missing-context corrections requested from OPERATOR.

Target direction:
many operational memory operations may occur in shard/local service;
GitHub publications remain sparse and significant.

No numeric performance target is asserted yet.

## Current next step

Do not launch memory-layering attempt 3.

First produce a convergence design from the existing exact artifacts:
- corrected File/Artifact Service boundary;
- existing shard gateway r0.3;
- operational memory record/checkpoint model;
- selective retrieval contract;
- replacement bootstrap/continuation contract;
- GitHub batching/canonical publication contract;
- exact smallest synthetic E2E pilot;
- explicit measurement plan.

Then independently review that design before any new live execution authority.

## Preserved boundaries

GitHub remains canonical evidence.
Shard state alone is not authoritative.
No hidden authority in memory/shard.
No automatic current-writer transfer.
No attempt 3 authority.
No generic host mutation authority.
No Project Sources/canon mutation by this plan.
No CHECKPOINT_DURABLE claim.

## Terminal

PASS_KOO_ENTITY_OPERATIONAL_MEMORY_SHARDS_RECOVERED_PLAN_R01
