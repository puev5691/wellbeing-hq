# KOO → SHT: staged Entity Chat → Work migration process r0.1

status: `READY_FOR_PROFILE_WORK`
scope: `process_design_only`
implementation: `no`
production: `no`

## Purpose

Design a staged, failure-safe process for migrating project Entities from ordinary ChatGPT chats to Work mode without silently losing instance continuity, recovery boundaries or writer authority.

## Basis

- active recovery canon v1.4;
- reviewed candidate r0.4 for uniform Wake → Resume / Initiation → Writer Gate → Exact Task;
- current empirical pilot: VOL operates in Work mode;
- OPERATOR observation: WEB and ARH ordinary chats show increasing latency/depth while still functioning.

## Exact scope

1. Fresh GitHub-preflight `puev5691/wellbeing-hq`.
2. Treat a new Work chat as a **new instance unless continuity is independently proven**.
3. Define staged migration states and gates for one Entity at a time:
   - pre-migration preservation readiness;
   - creation/opening of Work instance;
   - initiation/recovery verification;
   - writer handoff where required;
   - exact task smoke test;
   - retirement of old chat only after verified replacement.
4. Define rollback/failure states if Work instance cannot recover tools/files/GitHub/task state.
5. Keep Work product mechanics separate from project authority: mode availability does not create writer/task authority.
6. Recommend a pilot order and minimal evidence to decide whether to continue migration.

Do not migrate any Entity, approve canon, choose paid-plan changes or claim unverified ChatGPT limits.

Required result:
`entities/shtabist/outbox/SHT__entity-chat-to-work-migration-process-r01__KOO.md`

Verdict: process-ready / exact blocker.

---
КТО: KOO
ДЛЯ ЧЕГО: превратить переход Chat → Work в проверяемую процедуру, а не массовое переселение с чемоданами
СТАТУС: ready_for_profile_work
