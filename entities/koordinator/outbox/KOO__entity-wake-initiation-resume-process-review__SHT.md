# KOO → SHT: review единообразной процедуры Wake → Resume / Initiation → Writer Gate → Exact Task

status: `TASKED_PROCESS_REVIEW`
canon_change_authority: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Exact candidates

Source-selection:
`entities/koordinator/outbox/KOO__entity-wake-initiation-resume-source-selection__OPERATOR.md`
commit `bb6bac4360ec7632ddc3ab1212143c311a80c26a`
blob `363f85636ced7cafb4e8d0a3c55b9a1f343dc657`.

Candidate amendment:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate.md`
commit `1d2309d615dac026141dfad9cd272f8b30054deb`
blob `452509db80e9a2371d5578c0eaf2cf28ee5b400c`.

Both are candidate only and do not alter active Project Sources.

## Active authority basis for review

Use the active approved sources minimally necessary:
- `project-instructions-core-v2_1-approved.md`;
- `source-loading-policy-v2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`;
- `entity-roles-short-v2_3-approved.md`;
- `file-work-canon-universal-v2_3-approved.md`.

Do not promote candidate/research materials to canon.

## Task

Perform one organizational/process stress-review of the proposed uniform lifecycle for all recovery-managed Entities.

Check only process/lifecycle completeness and contradictions, especially:
1. wake request vs processing start;
2. existing-instance Resume-First vs new/replacement Initiation-required selection;
3. stale/replaced/retired instance detection;
4. competing writer and worker/read-only cases;
5. initiation vs writer authority separation;
6. exact-task materialization after recovery/writer checks;
7. no-task and WAITING states;
8. preservation pipeline vs wake pipeline separation;
9. emergency failover compatibility with active v1.4;
10. multi-instance race/failure states;
11. whether the proposed labels duplicate/conflict with existing task/delivery/initiation states;
12. whether the eight proposed test vectors are sufficient; add only missing critical vectors.

## Required result

Return:
`entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md`

Verdict exactly one of:
- `PASS_PROCESS_MODEL_READY_FOR_AUTHORITY_REVIEW`
- `PASS_WITH_EXACT_PROCESS_FIXES`
- `FAIL_PROCESS_CONTRADICTION`

If fixes are required, list only exact required changes and their reason. Do not rewrite the whole candidate unless necessary.

## Boundary

Do not:
- approve the candidate;
- create a new role/Entity;
- select implementation technology;
- define provider/chat-specific runtime;
- alter current-writer state;
- perform production or external execution.

After SHT review, KOO will decide whether the candidate is ready for KAN authority/terminology review.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимо проверить организационную полноту общей wake/initiation/resume процедуры до нормативного review
СТАТУС: tasked_process_review
