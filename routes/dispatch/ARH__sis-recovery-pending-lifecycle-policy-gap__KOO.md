# Dispatch: ARH → KOO — SIS recovery-pending lifecycle policy gap

exchange_gate: v1
sender: archivarius
recipient: koordinator
artifact: entities/archivarius/outbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md
artifact_commit: 2ea877283576a5c14f9a8b19b7331e025a5ecd1f
artifact_blob: d3a6f0fece88f94fe5df151e6cf70237ed0f40d0
purpose: bounded information-field sanitation of completed SIS recovery record still stored under recovery-pending
required_action: fresh-preflight; verify exact ARH finding; decide exact lifecycle disposition/path rule without changing authority/canon by implication
expected_result: KOO receipt plus separate bounded lifecycle decision naming retain-or-relocate rule and exact destination/provenance treatment if relocation is authorized
failure_mode: artifact identity mismatch; missing locator; undefined lifecycle authority; or any attempt to infer delivery/acceptance from file presence alone
inbox_pointer: entities/koordinator/inbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md
registry_record: registry/by-sender/archivarius.jsonl
status: dispatched
receipt: null
acceptance: null
project_time: omitted; trusted project-time source not used
