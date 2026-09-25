# KOD → KOO: synthetic detector-worker probe r0.1

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-result__KOO.md
artifact_commit: 740f871549c032b82ca1da2d6e00b26cfded6c24
artifact_blob: 5b40196b0a3013d02eb72c3ca8c2e7f43922b98c
purpose: bounded synthetic integration probe; exact interface blocker
required_action: fresh KOO reconciliation and decision on separate correction gate
expected_result: KOO acknowledges exact blocker, determines next authorized step
failure_mode: missing identity/readback or receipt leaves dispatch unreceived; do not infer Entity activation
inbox_pointer: entities/koordinator/inbox/KOD__detector-worker-isolated-probe-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched

matrix: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-matrix__KOO.md @ 740f871549c032b82ca1da2d6e00b26cfded6c24 blob 437a136d48b39af3dc44a33ffa6d9e9e3cc43ad3
fixture: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-fixture__KOO.py @ 740f871549c032b82ca1da2d6e00b26cfded6c24 blob b35196d14de64c8362f1ac7a8692762e21bc0597
evidence: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-results__KOO.json @ 740f871549c032b82ca1da2d6e00b26cfded6c24 blob 1acf8616d6ee7408281cf0267e47b74d38f35053
terminal: BLOCKED_KOD_DETECTOR_WORKER_R01_EVENT_AUTHORITY_INTERFACE
publication_is_not_receipt_or_activation: true
