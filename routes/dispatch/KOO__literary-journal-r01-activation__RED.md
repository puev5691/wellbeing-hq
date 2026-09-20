# Dispatch KOO → RED: literary journal r0.1 activation

exchange_gate: v1
sender: koordinator
recipient: redaktor
artifact: entities/koordinator/outbox/KOO__literary-journal-r01-activation__RED.md
artifact_commit: a4f804db1de6a674a588f57a5b23ad5fba7fa67f
artifact_blob: 0cbe48da36e7a63023050f564e691bf9ef7f3d3b
purpose: perform one bounded activation of the internal literary project journal
required_action: create journal directory + one main journal file + bounded verified seed + readback
expected_result: PASS_RED_LITERARY_JOURNAL_R01_ACTIVATED or exact blocker/fail
failure_mode: stop on authority/input mismatch; no automation, publication or Project Source mutation
status: dispatched
project_time: omitted
