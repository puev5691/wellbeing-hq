# KOO → KOD: clean republish Astra runtime package r0.1

status: TASK
execution_mode: CORRECTION_ONLY
priority: TOP_INFRASTRUCTURE

SHD fail:
`7f44a04a01a89dd8616b73f72798e5b810252338`

KOD source candidate:
`e51e7c7867073bc7676a33520867b00a6d0f6c16`

## Exact defect

The intended four-model logic is acceptable, but immutable Git Python bytes were polluted by an injected execution annotation line and became non-executable. MANIFEST SHA-256 also does not match final immutable bytes.

## Correct only publication/sealing

1. start from the intended clean source/test bytes from the Astra candidate;
2. remove all execution-tool annotation text from source/test payloads;
3. do not redesign policy/adapter/live behavior;
4. preserve exact allowlist:
   - `gpt-5.6-luna`
   - `gpt-5.6-terra`
   - `gpt-5.6-sol`
   - `gpt-6-astra`;
5. preserve unknown-model fail-closed behavior;
6. publish clean immutable Python bytes;
7. recompute byte sizes + SHA-256 from exact final Git-published bytes;
8. generate/seal MANIFEST from those exact final bytes;
9. run exact 9/13/6 tests against the final immutable bytes, not pre-publication/local variants;
10. verify no annotation/pollution exists in any Python payload;
11. return exact commit/tree/blob/SHA identities.

Preserve:
- retries=0;
- fallback=none;
- no tools/web/files/computer/code capability;
- hidden credential/no-persistence contract;
- no live provider call;
- no real credential read.

Expected:
`PASS_KOD_OPENAI_ASTRA_CLEAN_R01_READY_FOR_REVERIFY`
or exact blocker/fail.

Return result to KOO and stop.
