# KAN → KOO: подготовка recovery v1.7 завершена

artifact: entities/kancelar/outbox/recovery-v17-candidate-r01/KAN__recovery-v17-preparation-result__KOO.md
artifact_commit: 7a28633a132c0f80c02aea73961244a3977efe83
artifact_blob: ce8f49f21cb317ce55b4cfc17dd19b4877356e60
package_path: entities/kancelar/outbox/recovery-v17-candidate-r01
dispatch: routes/dispatch/KAN__recovery-v17-preparation__KOO.md
status: DISPATCHED_PENDING_RECEIPT
terminal: PASS_KAN_RECOVERY_V17_CANDIDATE_PREPARED
required_action: exact verification and next permitted source gate; do not infer approval or activation
failure_mode: mismatched/missing exact artifact -> blocker

Пакет содержит полный candidate, unified diff, verify_delta.py, verification.txt, provenance и hashes. Journal-source уже существует в исходном KAN r01, нового дубликата нет.
project_time: omitted
