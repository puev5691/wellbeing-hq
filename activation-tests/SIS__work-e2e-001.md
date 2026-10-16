# SIS bounded Work E2E activation manifest

test_class: SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT
task_id: SIS-WORK-E2E-001
entity_id: SIS-E2E-NONPROD-001
environment: non-production
writer_authority: none
production_current_state_mutation: forbidden

## Immutable source locators

authorization_artifact: entities/koordinator/outbox/KOO__activation-product-path-decision__SIS.md
authorization_commit: ba2548d767c0babc4d6a56946d3fa33bfde83f32
authorization_blob: b641fc8b62399d1c42550c195a1494dea6c79178

recovery_current_locator: entities/sisadmin/current/EXCHANGE-GATE.md
recovery_current_commit: 1176d3946586c8928339cc70c41e8423fbacafc6
recovery_current_blob: cfe0ee89f68ab483b9ce05859dcc4d5c00674d18

## Work-side required behavior

1. Treat the pull-request event only as an activation signal, never as writer authority.
2. Read this manifest from the PR head and report PR number/event type, task_id and entity_id.
3. Resolve each immutable locator above against GitHub and verify the expected blob identity.
4. If any path/commit/blob mismatch occurs, return FAIL_CLOSED_LOCATOR_MISMATCH and perform no profile work.
5. On successful verification, report VERIFIED_RECOVERY_INPUT and generate a fresh processing instance identifier scoped only to this test run.
6. Do not claim resume of any pre-existing Entity chat or continuity of an old Instance ID.
7. Do not mutate entities/*/current/, production state, grants, deployments, or writer authority.
8. Result is test evidence only and must be correlated by KOO with the GitHub PR event and product-side Work result.

## Acceptance target

PASS only if a supported GitHub PR event starts Work without an OPERATOR chat message and the resulting Work execution reports this Task ID plus successful immutable-locator verification.

A repository-side PR without independently visible Work execution is NOT PASS.

from_entity: SIS
to_entity: KOO
document_type: non-production activation-test manifest
status: repository-side-test-input
project_time: omitted; trusted project-time source not used
