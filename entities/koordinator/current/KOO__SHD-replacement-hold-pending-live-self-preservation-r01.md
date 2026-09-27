# KOO current routing: SHD replacement hold pending live self-preservation r0.1

status: HOLD_EMERGENCY_REPLACEMENT_PENDING_LIVE_SELF_PRESERVATION
project_time: omitted

New OPERATOR evidence:
the current SHD chat is still responsive in browser while replacement preparation has begun.

Consequence:
the previous emergency-replacement assumption "old SHD unavailable for self-preservation" is no longer reliable enough to use as the preferred path.

Current routing:
1. allow the still-responsive authoritative SHD instance to complete fresh self-snapshot/self-preservation;
2. route that fresh package to ARH for independent preservation/readback;
3. only after preservation, establish exact freeze/handoff;
4. then initiate replacement SHD from the newest preserved recovery.

Until that chain completes:
- do not start replacement SHD from older r0.3 as the preferred path;
- do not execute new SHD profile work;
- preserve existing emergency-replacement artifacts as historical fallback evidence, not as the active preferred path.

This hold does not cancel preserved recovery r0.3.
It only prevents choosing stale emergency replacement while a fresher graceful handoff remains possible.

terminal:
PASS_KOO_SHD_REPLACEMENT_HOLD_PENDING_LIVE_SELF_PRESERVATION_R01
