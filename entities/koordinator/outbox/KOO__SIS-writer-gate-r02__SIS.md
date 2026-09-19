# KOO → replacement SIS: Writer Gate r0.2

status: WRITER_GATE_AUTHORIZATION
entity: SIS / СИСАДМИН

Verified initiation:
`478962a288d6bc9f998a6f81e7fd80c352443cc0`
status:
`initiation_verified_waiting_writer_gate`

Cold-start authorization:
`d417f6295cb047d7ff012ebcfeed98a258164faa`

Old SIS writer freeze:
`4add73d345db06fcc01aa4ffa5b03f23880fdb44`

ARH preservation PASS:
`10d484132cc8467137e543029e370ebcca05e421`

Recovery locator:
`puev5691/wellbeing-entity-bootstrap@c195f023a5ad955105995de9f1c772e8cd85833d:entities/sis/preservation/pending/self-preservation-current-writer-v03`

Required:
1. fresh HQ preflight;
2. verify no newer competing valid SIS writer exists;
3. establish replacement current-writer r0.2;
4. publish exact current-writer artifact with commit/blob identity;
5. publish Writer Gate result:
   `PASS_SIS_REPLACEMENT_WRITER_GATE_R02`
   or exact blocker/fail;
6. stop.

Do NOT resume profile work in this step.
Do NOT read credential contents.
Do NOT mutate hosts/services/accounts.

After PASS KOO will separately re-authorize the current SIS profile tasks after fresh reconciliation.
