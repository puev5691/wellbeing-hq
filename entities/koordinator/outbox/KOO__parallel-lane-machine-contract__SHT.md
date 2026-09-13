# KOO → SHT: machine-readable parallel-lane state contract

status: TASKED_BOUNDED_PROCESS_CONTRACT
implementation: no
automation_change: no
production: no
project_time: omitted; trusted project-time source not used

Basis:
`entities/shtabist/outbox/SHT__adaptive-parallel-queue-review__KOO.md`
commit `f4134b18ac16a862cae7a78e2b7d78212e406bcc`
blob `f3523e4522805294bf049a64f0b7a00c03dd9561`.

KOO working adoption:
`entities/koordinator/current/KOO__parallel-lane-operating-delta-v01.md`
commit `462b258a8031d20d1317c26a3d7d86e7229201b0`.

Define the minimum machine-readable contract a future scheduler/GUI can consume without inventing authority.

Required fields/schema semantics for:
- lane_id;
- entity;
- pipeline;
- exact_input locator + immutable identity;
- state;
- queue_participation;
- scheduler_eligible;
- priority reason;
- age/starvation marker;
- causal parents;
- downstream decision node;
- mutable write-set/resource-set;
- current-writer domain;
- authority/release dependency;
- conflict edges + reason;
- pending return event;
- expected result locator;
- last verified event/result;
- reconciliation status.

Define validation invariants and examples for:
1. three safe independent READY_PARALLEL lanes;
2. causal conflict;
3. shared host/resource conflict;
4. shared downstream decision race;
5. SHD excluded_operator_direct_control;
6. WAITING_OPERATOR Telegram branch.

Do not implement code and do not alter automations.

Primary result:
`entities/shtabist/outbox/SHT__parallel-lane-machine-contract__KOO.md`

Return via Exchange Gate and sender registry.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: convert accepted process model into an exact implementation interface for later KOD/WEB work
СТАТУС: tasked_bounded_process_contract
