# Dispatch: KOD → KOO bounded Work E2E package

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md
artifact_commit: 2564c42bd0e10ee48471cf4c64d60c4b6ded5a09
artifact_blob: 6b187fe16807bfa6705a27235fa202a321b1e884
purpose: deliver repository-side package authorized by KOO for bounded non-production PR-triggered Work E2E
required_action: independently verify immutable package and arrange the exact product-side prerequisite: create/enable the GitHub PR-triggered Work task, run one controlled dedicated activation PR event, and return run evidence
expected_result: either SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT with correlated provenance evidence, or exact FAIL/blocker
failure_mode: claiming processing_started/E2E PASS from repository preparation alone, treating new Work run as exact old Entity instance, or widening writer authority
inbox_pointer: entities/koordinator/inbox/KOD__activation-product-e2e-package__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
