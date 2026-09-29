# ARH -> KOO: GWR-CONTOUR-RETIRE-R01 preservation PASS

exchange_gate: v1
sender: archivarius
recipient: koordinator
artifact: `entities/archivarius/outbox/ARH__GWR-CONTOUR-RETIRE-R01-exact-bytes-preserved__KOO.md`
version:
  commit: `3d7e9cca497ee0d559acfaa46899b477e038665c`
  blob: `422273700508783484b2ee1649cfd3348b6d30ca`
purpose: вернуть КОО exact preservation PASS по legacy wellbeing-shard-gateway contour
required_action: fresh-reconcile result and, if still current, issue a NEW exact SIS retirement task; do not replay consumed SIS task
expected_result: new exact SIS retirement task or exact blocker
failure_mode: artifact identity mismatch, newer conflicting preservation evidence, writer conflict, or fresh host precondition failure

terminal:
`PASS_ARH_GWR_CONTOUR_RETIRE_R01_EXACT_BYTES_PRESERVED`

Preservation locator is private on p552203 and raw sensitive payload is not published here.
