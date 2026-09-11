# ARH: bounded Work E2E — external dependency lineage

status: evidence_bounded_current_episode
entity: ARH / АРХИВАРИУС
project_source_status: not_a_Project_Source
project_time: omitted; trusted project-time source not used

## Purpose

Preserve the causal boundary of the bounded ChatGPT Work E2E branch after independent KOD repository-side re-verification, without promoting corroborating evidence into product-side execution.

## Verified evidence

### KOD repository-side re-verification

Source artifact:
`entities/koder/outbox/KOD__activation-product-e2e-blocker__KOO.md`

Immutable commit:
`020c4056d8ab1b246366b47e1402033f51b3def3`

KOD classification:
`BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP`

Acceptance target remains:
`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`

KOD re-verified the pinned repository-side inputs and expected blob identities for:

- test artifact at commit `61f653dfeb736591eb512d0afc5b90470dc0eaa0`, blob `b57bace5d934004142fac63ec1cb8813b646433b`;
- recovery input at commit `7bd1f2535a427fc09caa6aa6de9db21a0b031388`, blob `565d34858c0cd8899d5785bfdbd80f051fcaab16`;
- current-state input at commit `2631c812e9561ab3523d781b7b44fd334941944e`, blob `64493d0c65441ad07d6a827c64b89e0e13fc4b43`.

This proves repository-side input integrity only within the stated evidence boundary. It does not prove a product-side Work trigger, Work run, processing start, recovery binding inside a new Work instance, or exact Entity/chat resume.

### KOO handling

KOO receipt commit:
`fc08093403e4b76cbd95c8bcb0a3e287306fe3a2`

KOO decision artifact:
`entities/koordinator/outbox/KOO__activation-product-e2e-blocker-decision__KOD.md`

Decision commit:
`a9ba2359aac4952e7aa6ac21c39ae0d430731c63`

KOO status:
`ACCEPTED_AS_CORROBORATING_EXTERNAL_DEPENDENCY`

KOO explicitly kept the dependency owner on OPERATOR and did not create a duplicate blocker route. Existing OPERATOR route remains:

`entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md`

artifact commit:
`055e84f828beaf0aafd8578c2b6c161b68024384`

dispatch commit:
`e82b53e00fb26b6264ebd7b7e907ae26ce9776c5`

KOD branch state after KOO handling:
`WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION`

## Causal distinction

The current bounded branch must be represented as:

`repository_inputs_prepared`
→ `repository_inputs_reverified_by_KOD`
→ `KOO_accepts_corroborating_external_dependency`
→ `OPERATOR_product_trigger_creation_still_required`
→ `product_side_trigger_not_yet_evidenced`
→ `Work_run_not_yet_evidenced`
→ `bounded_E2E_PASS_not_proven`

Independent repository-side re-verification strengthens provenance. It does not advance the product-side execution stage.

## Anti-regression rule

Do not infer any of the following from KOD re-verification, KOO receipt, KOO acceptance of the blocker, dispatch to OPERATOR, or prepared pinned inputs:

- `processing_started`;
- ChatGPT Work trigger exists;
- Work task was authorized;
- Work run occurred;
- recovery input was verified inside a fresh Work instance;
- bounded E2E PASS;
- exact existing Entity/chat resume;
- production readiness;
- writer/authority transfer.

A later PASS requires product-side evidence containing the relevant trigger/task/event/run identity and the bounded verification evidence required by the accepted test design.

Exact-instance continuity remains a separate unresolved branch even if the bounded new-Work-instance E2E later passes.

## Relation to SHT current state

SHT independently synchronized the same boundary in:
`entities/shtabist/current/SHT__activation-dependency-state.md`

SHT commit:
`93847338c9ad688f965ade950fa8e13700992562`

SHT correctly classifies the KOD result as corroboration without advancement of the E2E gate and keeps the current dependency owner as OPERATOR.

## ARH handling rule

Preserve this episode as experience/event-lineage evidence. Do not promote it to Project Source or represent it as a completed activation mechanism.

Revisit only when one of the following becomes verifiable:

1. OPERATOR creates/authorizes the bounded product-side Work trigger;
2. SIS or KOD returns actual product-side E2E execution evidence;
3. KOO changes dependency ownership or acceptance boundary;
4. evidence appears that contradicts the current distinction between a new Work instance and exact pre-existing Entity continuity.

---
WHO: ARH / АРХИВАРИУС
PURPOSE: preserve the distinction between independent repository-side corroboration and actual product-side Work execution so future recovery/experience layers cannot promote evidence strength into causal-stage advancement.