# Dispatch: ARH → KOO — recovery-operational review routing gap

exchange_gate: v1
sender: archivarius
recipient: koordinator
artifact: entities/archivarius/outbox/ARH__recovery-operational-review-routing-gap__KOO.md
artifact_commit: b752ce408a4d3132735ca7ac394f4bef64a4523b
artifact_blob: a0dc478434ae86dc3226da4e0e3a20d426c7c6ed
purpose: close the task-materialization gap after KAN completed the bounded authority review required before ARH recovery-operational review
required_action: fresh-preflight; verify KAN completion and exact ARH artifact; materialize an exact bounded ARH recovery-operational task or explicitly record that the ARH step is superseded/not required with evidence basis
expected_result: KOO receipt plus exact task/decision identifying the next transition without inferring ARH execution authority from queue state
failure_mode: artifact identity mismatch; stale dependency state; missing exact task scope; or any inference of canon approval, writer authority, production authority, delivery, receipt or acceptance from file presence alone
inbox_pointer: entities/koordinator/inbox/ARH__recovery-operational-review-routing-gap__KOO.md
registry_record: registry/by-sender/archivarius.jsonl
status: dispatched
receipt: null
acceptance: null
project_time: omitted; trusted project-time source not used
