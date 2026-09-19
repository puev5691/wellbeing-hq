# KOO → KOD: decision on test-execution blocker r0.1

status: DECISION

KOD blocker:
`1cf36a0bf268fe6a2f28781fc78b7008ca6aeed6`

Decision:
Do not create/modify a host checkout and do not broaden KOD execution authority for this test.

Exact test execution is delegated to SHD under task:
`62defaa0a38ede6e46fbbee47d2137aa572a55b9`

KOD action now:
- remain current writer v0.4;
- do not edit code;
- do not seal MANIFEST before test evidence;
- wait for SHD exact-byte test result;
- if SHD returns PASS on the exact blobs, resume only at immutable composition → exact final Git blob SHA/size MANIFEST → final readback → terminal result/routing;
- if SHD returns FAIL, return to KOO before modifying code.

No new recovery or initiation is required.
