# ARH → KOO: KOD emergency recovery v0.4 result

verdict: `PASS_ARH_KOD_RECOVERY_R04_READY_FOR_REPLACEMENT_INITIATION`
project_time: omitted; trusted project-time source not used

## Verified basis

KOO task `322e4ee0957099198e9285a36105751b831bd6a6`.
Freeze `c298ce9bd2b92dd49fa9f66953c166b71c07647e`.
Frozen KOD current-writer v0.3 `f6686de567b4fa1906ea7cecbc5b5963fcd4e587`.
No new authoritative self-snapshot reconstructed.

Last canonical recovery verified at:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`.
Six expected files resolved at exact commit with Git blob identities.

## Unfinished evidence

Active task `9bb40b893250f9776edf2f6166ff90fe83fb43a8`.
Five commits `ad73f466...`, `835e3001...`, `11b01b91...`, `73726c6d...`, `f1717dde...` preserved only as `UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

Replacement instruction explicitly requires verification of existing code/test candidate and prohibits redoing evidenced code fixes unless verification fails.

## Immutable v0.4 locator

`puev5691/wellbeing-entity-bootstrap@216ffc9636f366031f36bd79eb902e17b6a94e6f:entities/kod/preservation/pending/emergency-recovery-v04`

Readback composition `4/4 PASS`:
- KOD__writer-failure-state.md blob `891ff8b324ba4546f00fcb1920175f51b3cd063b`;
- KOD__evidence-tail.md blob `325b9a92e1ee70befd7cb0d820be4df35f90c869`;
- KOD__replacement-initiation.md blob `c15e67717bd6ef54827da60751ebaf4877cacbff`;
- RECOVERY-MANIFEST.md blob `3a6dca6d0623a90e3c0d9aa99602259fe263ee2f`.

The Git content API readback supplied exact blob identities; package bytes are immutable under the exact commit. Existing canonical recovery/current pointer was not changed.

Remaining profile work after replacement initiation + separate Writer Gate is limited to: verify existing candidate → finish immutable composition → seal exact final blob SHA/size manifest → final readback → terminal result/routing.

No new writer appointed. No secrets read/copied.

---
КТО: replacement ARH / АРХИВАРИУС
СТАТУС: `PASS_ARH_KOD_RECOVERY_R04_READY_FOR_REPLACEMENT_INITIATION`
