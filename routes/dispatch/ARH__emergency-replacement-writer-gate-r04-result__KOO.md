# ARH → KOO: emergency replacement Writer Gate r0.4

exchange_gate: v1
sender: archivarius
recipient: koordinator
artifact: `entities/archivarius/outbox/ARH__emergency-replacement-writer-gate-r04-result__OPERATOR-KOO.md`
version:
  commit: `5cb16a39878947361e4df37563427ece8b8a7b8b`
  blob: `e1a0dd6653912e69fbf37f304d0d84de94960c12`
purpose: notify KOO of established replacement ARH current-writer and preserve exact Writer Gate boundary
required_action: when KOO is again validly initiated/current-writer, read exact artifact and treat it as evidence for fresh reconciliation only; do not replay historical ARH tasks
expected_result: receipt or later KOO reconciliation result under valid KOO authority
failure_mode: commit/blob mismatch, stale locator, or KOO writer/recovery not verified

terminal carried by artifact:
`WRITER_ESTABLISHED`

This dispatch does not prove receipt, acceptance or processing.
