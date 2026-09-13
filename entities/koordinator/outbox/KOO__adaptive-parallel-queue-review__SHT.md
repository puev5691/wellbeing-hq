# KOO → SHT: adaptive parallel queue bounded review

status: TASKED_PROCESS_REVIEW
scope: queue_concurrency_and_dependency_safety
production_mutation: no
automation_change: no
project_time: omitted; trusted project-time source not used

## Context

KOO working algorithm:
`entities/koordinator/current/KOO__dynamic-next-route-algorithm.md`
commit: `8db0d5a8231256bc01d9b49fd7afcfac48d8d6b6`.

All-pipelines board:
`entities/koordinator/outbox/KOO__operator-all-pipelines-board__OPERATOR.md`
commit: `4a3a2f8fd61adfd70b6dff0354bc42ac51f35b19`.

Current OPERATOR direction: do not force all work through one serial adaptive queue when independent profile tasks exist. SHD is temporarily excluded from the adaptive queue while working under direct OPERATOR control on MAZHOR.

## Problem

A single serial READY selection causes avoidable waiting:
- independent pipelines wait behind unrelated long-running work;
- one WAITING_OPERATOR / WAITING_SHD branch can reduce throughput;
- manual Entity activation is currently the scarce control layer.

Need a bounded process review for safe **parallel lanes** without weakening exact dependency, current-writer, authority, Exchange Gate or immutable-result rules.

## Required review

Produce a process candidate that defines:

1. when two or more tasks are safe to run concurrently;
2. hard conflict conditions that prohibit parallel launch:
   - same exact artifact mutable write target;
   - same Entity/current-writer conflict;
   - causal dependency;
   - same privileged/runtime resource where concurrent mutation is unsafe;
   - shared release/authority decision;
3. operational classes for each lane:
   `READY_PARALLEL`, `RUNNING`, `WAITING_EXTERNAL`, `WAITING_ENTITY`, `WAITING_OPERATOR`, `CLOSED`, `CONFLICT`;
4. how KOO reconciles several returned results without losing causal order;
5. starvation prevention across independent pipelines;
6. whether a bounded maximum parallel lane count is needed now, and on what evidence;
7. how manual OPERATOR activation maps to future automatic scheduler/supervisor;
8. exact failure mode when two results race to affect the same downstream decision;
9. how SHD direct-control exclusion is represented without losing its pending return event;
10. minimal update to the dynamic-next-route algorithm if SHT recommends one.

Do not invent new authority for SHT, KOO or any Entity. Do not modify automations or production.

## Output

Primary result:
`entities/shtabist/outbox/SHT__adaptive-parallel-queue-review__KOO.md`

Return through Exchange Gate:
- `routes/dispatch/SHT__adaptive-parallel-queue-review__KOO.md`
- `entities/koordinator/inbox/SHT__adaptive-parallel-queue-review__KOO.md`
- sender registry `registry/by-sender/shtabist.jsonl`

Verdict:
- `BOUNDED_PASS_WITH_PARALLEL_LANE_MODEL`, or
- exact process blockers/contradictions.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: получить независимый process review безопасной параллельной адаптивной очереди
СТАТУС: tasked_process_review
