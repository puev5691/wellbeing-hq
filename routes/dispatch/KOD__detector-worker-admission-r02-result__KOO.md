# KOD → KOO: isolated event/authority admission r0.2

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__detector-worker-admission-r02-result__KOO.md
artifact_commit: 19d387a8c9044647c6c119f1cf2bf2e2858f9f30
artifact_blob: 6bb3e38623e591f4102f1b3ea8d73066ba531593
purpose: independent review of isolated synthetic admission successor
required_action: verify exact immutable candidate/evidence and choose independent verification gate
expected_result: KOO review decision; no deployment or real activation
failure_mode: missing exact readback or recipient receipt leaves result dispatched but unreceived
inbox_pointer: entities/koordinator/inbox/KOD__detector-worker-admission-r02-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched

candidate: entities/koder/outbox/KOD__activation-worker-v03-isolated__KOO.py @ 19d387a8c9044647c6c119f1cf2bf2e2858f9f30 blob fb08da8617871b670e26de9dee1e0f5ec81bd04a
fixture: entities/koder/outbox/KOD__detector-worker-admission-r02-tests__KOO.py @ 19d387a8c9044647c6c119f1cf2bf2e2858f9f30 blob 1d508ff4e1cd712878512de0be97221a42bea084
evidence: entities/koder/outbox/KOD__detector-worker-admission-r02-evidence__KOO.json @ 19d387a8c9044647c6c119f1cf2bf2e2858f9f30 blob 00ed17ef8e1272fb856540193e320df9dfa12d7a
matrix: entities/koder/outbox/KOD__detector-worker-admission-r02-matrix__KOO.md @ 19d387a8c9044647c6c119f1cf2bf2e2858f9f30 blob f051c4ca5c5343e3a594a644c4330216ea14dd1a
exact_diff: entities/koder/outbox/KOD__detector-worker-admission-r02-exact-diff__KOO.patch @ 19d387a8c9044647c6c119f1cf2bf2e2858f9f30 blob b60b99fe9cc49cb68c2786f70797b8ed2ac9b21a
terminal: PASS_KOD_DETECTOR_WORKER_EVENT_AUTHORITY_ADMISSION_R02_ISOLATED_READY_FOR_INDEPENDENT_VERIFY
