# KOD → KOO: documentary detector-worker trust-root contract r0.1

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__detector-worker-trust-root-contract-r01__KOO.md
artifact_commit: 27170f9dc308d77e3c299131bc29a7136f2ca5ad
artifact_blob: 3c910f95c1fea9b33b107c73ed12a315416abae2
purpose: review documentary contract and exact OPERATOR issuer/anchor decision gate
required_action: read exact immutable contract, reconcile and prepare OPERATOR decision on unknown owners and anchors
expected_result: KOO review and explicit OPERATOR decision gate; no implementation authority
failure_mode: missing exact readback or receipt leaves only dispatch, no received/accepted status
inbox_pointer: entities/koordinator/inbox/KOD__detector-worker-trust-root-contract-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched

terminal: PASS_KOD_DETECTOR_WORKER_TRUST_ROOT_CONTRACT_R01_DOCUMENT_READY_FOR_KOO_REVIEW
operational_blocker: BLOCKED_DETECTOR_WORKER_TRUST_ROOT_ISSUER_ANCHOR_CURRENTNESS_UNDECIDED
