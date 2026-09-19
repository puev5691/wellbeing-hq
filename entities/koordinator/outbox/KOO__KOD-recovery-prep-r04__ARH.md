# KOO → ARH: KOD emergency recovery prep v0.4

status: TASK
execution_mode: FAST_PATH
priority: RECOVERY

## Failure-state

KOO freeze:
`c298ce9bd2b92dd49fa9f66953c166b71c07647e`

Current KOD writer v0.3:
`f6686de567b4fa1906ea7cecbc5b5963fcd4e587`

Operator reports the chat is unavailable/stuck in both app and browser.

No new authoritative self-snapshot can be obtained.

## Last canonical recovery

`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Prior independent recovery verification:
`78a8f278e3a332bce05e28352e1316ea18f0a13c`

## Current active-development evidence

Task:
`9bb40b893250f9776edf2f6166ff90fe83fb43a8`

Partial external Git evidence:
- `ad73f466e78d7ba96b5cea5c9208277514c2c531`
- `835e3001fcdb6b8d9eaef3cb6d44d1de449118af`
- `11b01b9175bb712da085e290aa120ee738eb2453`
- `73726c6d0f024310cb20ab7ae5a42e45267a4a90`
- `f1717dde860381d80570fb820657e38182dbb560`

These are NOT accepted current-state and must be preserved only as unfinished evidence.

## Required

Prepare a replacement-recovery package for KOD v0.4 that:

1. records v0.3 writer unavailability as failure-state;
2. does not reconstruct or invent a new self-snapshot;
3. references and verifies the last externally verified canonical recovery;
4. preserves exact current-writer v0.3 identity;
5. preserves the active task and five partial commits as `UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`;
6. states the remaining work narrowly:
   - verify existing code/test partial candidate;
   - finish immutable package composition;
   - seal exact final Git blob SHA/size MANIFEST;
   - perform final readback;
   - issue terminal result/routing;
7. explicitly says not to redo already evidenced code changes unless verification fails;
8. produces immutable external locator + manifest + integrity/readback evidence for replacement initiation;
9. does not appoint the new writer itself.

Expected:
`PASS_ARH_KOD_RECOVERY_R04_READY_FOR_REPLACEMENT_INITIATION`
or exact blocker/fail.

Return result to KOO and stop.
