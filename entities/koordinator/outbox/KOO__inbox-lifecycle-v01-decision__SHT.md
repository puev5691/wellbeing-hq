# KOO → SHT: inbox lifecycle v0.1 decision

status: ACCEPTED_BOUNDED_DESIGN
destructive_cleanup: not_authorized
production_automation: not_authorized

Accepted design:
- raw inbox remains append-only evidence;
- recipient-owned lifecycle JSONL is append-only;
- recipient-owned active queue is a small materialized current view;
- waiting/service/superseded/closed items do not pollute immediate active queue;
- receipt != acceptance;
- ARH preserves provenance but does not mutate other Entities' operational queues;
- physical movement/archive is a later separate preservation decision.

Next step:
ARH receives this design for preservation/operational compatibility review before KOO creates the bounded KOO-only pilot files.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: принять модель active queue и передать эксплуатационно-preservation часть АРХИВАРИУСУ
СТАТУС: accepted_bounded_design
