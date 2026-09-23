# Project Instructions v3 r0.3 — delta map

status: CANDIDATE_DELTA_MAP
candidate: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r03.md
predecessor_candidate: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r02.md@da770ca7dede1a21c415c7fd6b1912f97b5482c4
norm_review: entities/kancelar/outbox/KAN__project-instructions-v3-r02-norm-review__SHT-KOO.md@0377df0c76950b80020f0cf157c3fa72b45d1bed
active_sources_mutated: no
ui_mutated: no

## A. Действующие нормы, которые candidate только отражает/сводит

| Тема | Действующее основание | Статус в r0.3 |
|---|---|---|
| Human-first: сначала смысл, затем machine evidence | Project Core v2.5, «Человекочитаемый интерфейс проекта» | retained/organized |
| Capability != authority | Project Core v2.5, «Границы Сущности, полномочий…» | retained |
| Entity != chat instance | Project Core v2.5 | retained |
| Wake → Resume / Initiation → Writer Gate → Exact Task | Recovery v1.6 | K1 restored explicitly |
| Significant result must be standalone file/package | File-work v2.4, главный принцип/§3 | K2 restored explicitly |
| Publication/delivery/receipt/acceptance distinct | Project Core v2.5 + File-work/Task-conveyor | retained |
| Manual handoff while automatic scope not authorized+verified | Project Core v2.5 + Task-conveyor v1.2 §10 | K3/K4 restored explicitly |
| Historical PROMPT != current execution authority | Task-conveyor v1.2 §12 | retained |
| Minimal source loading / approved baseline | Source-loading v2.2 | retained |
| JOURNAL_CANDIDATE is optional and not auto-publication | Task-conveyor v1.2 | retained |
| Conflict/unknown fail-closed | Core v2.5 + recovery/source-loading | retained |

## B. Новые предлагаемые общепроектные нормы, требующие решения ОПЕРАТОРА

1. Обязательный единый terminal-dialogue scenario:
   human story → experience → technological fixation → next Entity/handoff → explicit Operator action.
2. Один рабочий эпизод как три согласованные проекции: exact evidence / reusable experience / literary-media narrative.
3. Верхнеуровневая граница Booster как bounded auxiliary resource, а не authority-bearing Entity.
4. Верхнеуровневая модель orchestrator как materializer уже разрешённого causal next step.
5. Целевая роль ОПЕРАТОРА: не постоянный ручной диспетчер при наличии разрешённой проверенной automation.
6. Общий anti-bureaucracy rule для terminal artifact/experience/journal/handoff.

Эти пункты не объявлены active до explicit OPERATOR approval и фактической UI replacement.

## C. Профильные/implementation contracts, которые candidate не повышает до общей нормы

- конкретная memory-layering L0–L5 архитектура;
- конкретные ML-E2E limits/runtime;
- Booster provider/model/API/billing/data permissions;
- orchestrator implementation/schema/scheduler/runtime;
- specific activation-lineage event/BRIDGE schema;
- server/host topology;
- automation schedule.

§11 r0.3 прямо ограничивает BRIDGE semantics отдельно подключённым approved activation-lineage contract.

## D. K1–K6 disposition

- K1: FIXED — continuity check precedes Resume/Initiation.
- K2: FIXED — significant result file-first restored without “reusable/if task requires” weakening.
- K3: FIXED — automatic branch requires BOTH standing/explicit automation authority AND verified mechanism.
- K4: FIXED — transitional manual mode + KOO reconciliation fallback restored.
- K5: EVIDENCE_GAP — exact immutable UI Project Instructions v2 predecessor export not found in verified project evidence.
- K6: FIXED — active invariants / new proposed policies / profile contracts explicitly separated.

## E. K5 exact evidence gap

Known:
- current project conversation exposes a Project Instructions v2 text to the runtime;
- active Project Core v2.5 is separately verified in GitHub;
- no exact immutable export/identity of the predecessor **UI Project Instructions v2** was found in verified project evidence used for this review.

Therefore:
- do not substitute Project Core v2.5 for UI Project Instructions v2;
- do not claim complete predecessor preservation;
- do not claim exact v2→v3 UI diff;
- do not block K1–K4/K6 correction or KAN re-review.

Minimal OPERATOR action before approval/activation:
**provide/export the exact current UI Project Instructions v2 text as a file or otherwise create a verifiable immutable snapshot of that exact UI text.**

After that snapshot:
1. bind immutable identity;
2. compare it to r0.3;
3. record conscious deletions/additions;
4. only then make approval/replacement decision;
5. after UI replacement, read back the installed exact revision.

---
КТО: SHT / ШТАБИСТ
СТАТУС: CANDIDATE_DELTA_MAP
