# KOO → replacement KOD: Writer Gate v0.4

status: WRITER_GATE_AUTHORIZATION
entity: KOD / КОДЕР

Verified initiation:
`3471612c4195e70fbad1d7f7d7472863eec4bcad`
status:
`initiation_verified_waiting_writer_gate`

Cold-start authorization:
`e9834a96dd382dce49b40e11a9db3eae61d710fb`

Recovery result:
`62e52c0e04f98448c1fd8bcd3e56800d9a5ac7ed`

Recovery locator:
`puev5691/wellbeing-entity-bootstrap@216ffc9636f366031f36bd79eb902e17b6a94e6f:entities/kod/preservation/pending/emergency-recovery-v04`

Old writer v0.3 remains frozen:
`f6686de567b4fa1906ea7cecbc5b5963fcd4e587`

Required:
1. fresh HQ preflight;
2. verify no newer competing valid KOD writer exists;
3. establish replacement current-writer v0.4 under the current recovery canon;
4. publish exact current-writer artifact with commit/blob identity;
5. publish Writer Gate result:
   `PASS_KOD_REPLACEMENT_WRITER_GATE_R04`
   or exact blocker/fail;
6. stop.

Do NOT execute File/Artifact Service code in this step.
Do NOT resume profile work in this step.
Do NOT modify canonical recovery/current pointer unless the canon explicitly requires it for writer establishment.

After Writer Gate PASS, KOO will issue a separate narrow profile task limited to:
verify existing candidate → finish immutable package composition → seal exact final Git blob SHA/size MANIFEST → final readback → terminal result/routing.
