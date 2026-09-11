# Bounded Work E2E current state

entity_id: `ent:KOD-E2E-WORK-01`
task_id: `task:activation-work-e2e-01`
state_role: immutable current-state seed
state: `READY_FOR_PRODUCT_TRIGGER_TEST`
production: false

## Required next action

A GitHub PR-triggered Work run may use this state only as bounded test input. Before profile work it must verify all manifest locators exactly, create a fresh Instance ID, and emit evidence sufficient to correlate the PR event, Work execution result, Task ID, Entity ID, fresh Instance ID, and verified repository provenance.

## Prohibited inference

This state does not authorize production mutation, writer-grant expansion, exact Entity/chat resume claims, or reuse of an old Instance ID.

Expected state token: `WB-HQ-KOD-E2E-STATE-01`

Project time omitted; trusted project-time source not used.
