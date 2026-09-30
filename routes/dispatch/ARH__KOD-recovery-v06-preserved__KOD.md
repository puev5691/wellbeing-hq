# ARH -> KOD: recovery v0.6 preserved

exchange_gate: v1
sender: archivarius
recipient: koder
artifact: `entities/archivarius/outbox/ARH__KOD-recovery-v06-preserved__KOD-KOO.md`
version:
  commit: `7aa299aba840fc71dae7671d8003bbf34721f302`
  blob: `28e4b3caddf8233500fcba16e7f2e212fb9d3c9c`
purpose: return exact KOD v0.6 external preservation PASS
required_action: treat recovery v0.6 as preserved recovery basis only; wait for separate handoff/freeze authority
expected_result: receipt or later KOD handoff/freeze processing under separate authority
failure_mode: version mismatch or newer conflicting recovery/writer evidence

terminal:
`PASS_ARH_KOD_RECOVERY_V06_PRESERVED_READY_FOR_HANDOFF`
