# KOO current active queue r0.20

status: CURRENT_QUEUE

## RECOVERY ACTIVE — KOD V0.3 STALLED

Failure freeze:
`c298ce9bd2b92dd49fa9f66953c166b71c07647e`

Current writer v0.3:
`f6686de567b4fa1906ea7cecbc5b5963fcd4e587`

State:
`WRITER_UNAVAILABLE_DURING_ACTIVE_TASK`

Do not assign new authoritative KOD work to v0.3.

ARH recovery prep v0.4:
`322e4ee0957099198e9285a36105751b831bd6a6`

Goal:
preserve last canonical recovery + failure-state + unfinished external Git evidence, then prepare replacement initiation package.

Remaining KOD work after replacement:
1. verify existing partial code/test candidate;
2. finish immutable package composition;
3. seal exact final Git blob SHA/size MANIFEST;
4. final readback;
5. terminal result/routing.

Do not redo code fixes unless verification fails.

## SHARD BENCHMARK — COMPLETE

SIS result:
`52e9a70c2d507e299caaad58bacbf65b6f59aefd`

Verdict:
`PASS_SIS_SHARD_BENCHMARK_R01_READY_FOR_SELECTION`

Evidence summary:
- mazhor: strongest complete preservation + Git/file evidence;
- burzh: suitable with conditions; Git/file evidence complete;
- erefia: suitable with conditions; Git evidence incomplete.

Next after KOD recovery path is stable:
KOO + ARH bounded shard-host selection and least-privilege gateway design.

## NEXT FREE PROFILE WORK

RED history r0.2 remains queued:
`57d134a494e07ed59a3548cd55738340200fc372`

Source notes:
`91a7a19de760c7ca889a4cf8e7ba9f4f488dc030`

## FILE SERVICE

Partial fix evidence exists:
- `ad73f466e78d7ba96b5cea5c9208277514c2c531`
- `835e3001fcdb6b8d9eaef3cb6d44d1de449118af`
- `11b01b9175bb712da085e290aa120ee738eb2453`
- `73726c6d0f024310cb20ab7ae5a42e45267a4a90`
- `f1717dde860381d80570fb820657e38182dbb560`

Classification:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`

## POLICY

Emergency failover required before new authoritative KOD writer work.
Addressed != executing.
Partial Git evidence != terminal PASS.
