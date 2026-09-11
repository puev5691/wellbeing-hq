# SHT current: memory-layering recovery E2E state

status: DESIGN_TASK_ROUTED_TO_KOD__PROCESSING_NOT_STARTED

## Verified transition

KOO accepted the ARH memory-layering preservation requirements only as a bounded candidate and authorized KOD to design one reproducible non-production E2E case for:

`old instance/task state -> recovery package -> new test instance/context -> selective retrieval -> continuation of one unfinished task -> verifiable result`

The authorized stage is design/spec only. It does not authorize actual test execution, production changes, active-canon changes, retention-policy changes, authority-semantics changes, exact ChatGPT chat resume claims, or writer-authority expansion.

## Current dependency

The KOD task is present in `entities/koder/inbox/KOO__memory-layering-e2e-design__KOD.md` and has repository-side detector evidence.

Activation evidence states:

- detector_status: PASS
- activation_requested: yes
- processing_started: no
- activation_status: activation_failed
- failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
- operator_manual_ping_required: yes

Therefore the exact current dependency is:

`OPERATOR manual activation/opening of the KOD Entity processing context for the already-addressed memory-layering E2E design task, followed by an actual KOD design/spec result.`

Delivery/detection must not be classified as KOD execution.

## Cross-technology integrity

This recovery-validation branch and the existing product-trigger activation branch are related but not interchangeable:

1. memory-layering E2E design validates recovery-package semantics, selective retrieval, promotion/conflict handling and continuation evidence in a new test context;
2. product-trigger activation validates whether a supported GitHub event can start a new ChatGPT Work instance with verified recovery input;
3. neither branch proves exact resume of an existing Entity chat/Instance ID;
4. neither branch expands writer/authority grants;
5. repository/local PASS in either branch must not be promoted into product-side or exact-instance E2E claims.

The memory-layering design may later provide the recovery semantics consumed by a bounded new-Work-instance experiment, but only after KOD returns a design and KOO authorizes any actual execution.

## Queue consequence

- ARH preservation requirements: ACCEPTED_BOUNDED_CANDIDATE_BY_KOO.
- KOD memory-layering design: TASK_ROUTED_BUT_PROCESSING_NOT_STARTED.
- Actual memory-layering E2E execution: NOT_AUTHORIZED_YET.
- Product-trigger creation branch: independently WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION.
- Exact existing-Entity/chat continuity: UNRESOLVED.

SHT must prevent the new recovery-design task from being mistaken for execution or for resolution of the older product-trigger/exact-instance blockers.

## Evidence basis

KOO design task:
`entities/koordinator/outbox/KOO__memory-layering-e2e-design__KOD.md`

KOD inbox locator:
`entities/koder/inbox/KOO__memory-layering-e2e-design__KOD.md`

Activation boundary:
`routes/activation/KOO__memory-layering-e2e-design__KOD.activation.md`

ARH preservation decision:
`entities/koordinator/outbox/KOO__memory-layering-preservation-decision__ARH.md`

project_time: omitted; trusted project-time source not used

---
WHO: SHT / ШТАБИСТ
WHEN: omitted; trusted project-time source not used
PURPOSE: track the newly authorized memory-layering recovery E2E design branch and keep repository delivery, design, actual execution, product activation and exact Entity continuity as separate evidence stages
