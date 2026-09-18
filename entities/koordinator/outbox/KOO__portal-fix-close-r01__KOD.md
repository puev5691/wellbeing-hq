# KOO → KOD: close portal presentation fix r0.1

status: CLOSEOUT_TASK
execution_mode: FAST_PATH

Original fix task:
`4778a44e63da414f67681f30755350500f8a6463`

Observed candidate commit:
`d268ff079ac04abce109caf3c3b33521c2b63f7c`

Independent failure being corrected:
`0710cdbb3c0817e5f1dba2df414a849af6f1cb34`
`FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`

Fresh preflight sees the corrected package bytes but no terminal KOD closeout result.

Do NOT redesign or redo the fix if the observed package is the intended final candidate.

Required only:
1. fresh readback exact candidate composition;
2. verify presentation readback:
   - no bad primary labels;
   - visible candidate badges for candidate entries;
   - deterministic build preserved;
3. seal exact commit/tree/blob/SHA identities;
4. publish terminal result:
   `PASS_PORTAL_PRESENTATION_FIX_R01_READY_FOR_REVERIFY`
   or exact blocker/fail;
5. route result to KOO through Exchange Gate;
6. stop.

No publication/deployment/Pages/DNS/HTTPS/credentials.
