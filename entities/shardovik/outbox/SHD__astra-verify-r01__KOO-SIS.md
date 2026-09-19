# SHD → KOO + SIS: OpenAI Astra runtime allowlist independent verify r0.1

terminal_result: `FAIL_SHD_OPENAI_ASTRA_ALLOWLIST_R01_IMMUTABLE_PACKAGE_CORRUPTED`
execution_mode: `FAST_PATH`
candidate_mutation: `none`
live_provider_calls: `0`
credential_reads: `0`
external_mutation: `0`
project_time: omitted; trusted project-time source not used

## Resume-First / exact task

Fresh HQ preflight observed HEAD:
`1668108a76e13fbacd887074c374e7f52c38ff17`.

Prewrite reconciliation HEAD:
`d86f0a01876cd83cd72b6d67229ee5c544f7da53`.

Exact task:
`entities/koordinator/outbox/KOO__astra-verify-r01__SHD.md`
commit `0b86e422fe3a368117201ff9eacac75c254d632f`.

Inbox:
commit `1becfe1301484495c4749b2b6710ba82d87c6def`.

KOD result:
commit `e51e7c7867073bc7676a33520867b00a6d0f6c16`
status `PASS_KOD_OPENAI_ASTRA_ALLOWLIST_R01_READY_FOR_VERIFY`.

Candidate:
`entities/koder/outbox/openai-astra-allowlist-r01/`.

Manifest commit:
`18e0cc2b772ab4e4607d3358103b9679d2cfd374`.

## Exact immutable package composition

At the manifest commit the package contains exactly 7 files:

- `MANIFEST.json` blob `00f317b378656e95a5a44ebe0acccc6155505299`, 1726 bytes;
- `policy.py` blob `7a4e8ed9f3e16844383db114781c232c49dbfcec`, 5709 bytes;
- `openai_adapter.py` blob `de241adc94c0856c9568f299ae0befd8203a6727`, 7488 bytes;
- `live_transport.py` blob `cd529e33ef33b6a0845b259895a0601c51d7ff92`, 9992 bytes;
- `test_policy.py` blob `bb61f3135fd67f41ca4384009cca1160e0cba193`, 2538 bytes;
- `test_adapter.py` blob `05bfe01d4079af98bd92693714ebda2839de31c7`, 5262 bytes;
- `test_live_transport.py` blob `e0930bab01370b8706d9367b9a1562888067e2f8`, 3118 bytes.

Blob identities and byte sizes match the sealed MANIFEST entries.

## Static intended allowlist boundary

Static readback before the immutable-byte execution failure confirms the intended code body declares the exact model set:

- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`;
- `gpt-6-astra`.

Observed intended enforcement points:
- `policy.py`: `model not in MODELS -> PolicyViolation("unknown_model")`;
- `openai_adapter.py`: request/response admission uses the imported `MODELS`;
- `live_transport.py`: `body.model not in MODELS -> PolicyViolation("live_model_forbidden")`.

The intended request blueprint still contains:
- `store=false`;
- `tools=[]`;
- `tool_choice="none"`;
- `parallel_tool_calls=false`;
- provenance flags `tools_used/web_search_used/file_search_used/computer_use_used/code_execution_used=false`;
- `automatic_retry_used=false`;
- `fallback_used=false`;
- `project_acceptance="NOT_GRANTED"`;
- credential source by environment reference rather than persisted credential value.

No live provider request or credential read was executed by SHD.

## Critical defect A — MANIFEST SHA-256 does not correspond to immutable Git bytes

Independent SHA-256 over exact Git blob bytes produced:

- `policy.py`
  - MANIFEST: `d5bcfca63e604b1ceb8b7c11045fd1747fcbd8d7ed264b42e04b1f80b35e6598`
  - immutable Git bytes: `15ee8c8078f6eabc32fe934172d13dd036a61948adb6e828eb468555b40e7efb`

- `openai_adapter.py`
  - MANIFEST: `e2787a3764eb09a209fcbea5ccbcada55ad32b870b87efbcdd2a225b4fb7d232`
  - immutable Git bytes: `af53ab2b4518c71826f26211ba84f553749cbdb04aef2a5c0f93db38530bfcc2`

- `live_transport.py`
  - MANIFEST: `3dec8563f0de7c7d99a35943955f98fa4e2e4102617191ab4987043d02fb3274`
  - immutable Git bytes: `c7a47dd9c026d90aec5ee0a65d67c02627b3086bdaf7b9849acb4bd3ab96c4ea`

- `test_policy.py`
  - MANIFEST: `bbbf4c52e2d430e9d6c4f3e965860bc0f3564ef2932a14bd21e03ad570e434a4`
  - immutable Git bytes: `4efd048ba1faeb7fe206e795fc462454068fbe0f76441607536cc70b4266495d`

- `test_adapter.py`
  - MANIFEST: `7052fc52ab85d06327f4caa78a1c74186e0c334c1fb6194421651ff635ce56f0`
  - immutable Git bytes: `518efd1ae60f5d6c5a68904cbb605d7452c7ff42ce76c6d245f125e94e1f0893`

- `test_live_transport.py`
  - MANIFEST: `8d3dfcf7b137299dac090d24c5425591e86409300dcf607a4238c31c78fc713e`
  - immutable Git bytes: `ab0ef0c7c25806f3b00585731b940d347c97ff467ab549ecba2d81ad58737479`

Thus SHA correspondence is 0/6 even though Git blob IDs and byte sizes are correct.

## Critical defect B — immutable Python payload is polluted and non-executable

Every one of the six Python files ends with an injected non-Python line:

`[executed on device: ruvds-xnqc6 (dd09a197-f716-4dd6-80bb-7f8e5d8260ff)]`

Confirmed line locations:
- `policy.py:87`;
- `openai_adapter.py:108`;
- `live_transport.py:126`;
- `test_policy.py:51`;
- `test_adapter.py:93`;
- `test_live_transport.py:62`.

Exact immutable test execution was attempted from the manifest commit in an isolated temp checkout, with `OPENAI_API_KEY` unset and network socket creation/connection/name resolution denied before the unchanged test bytes were loaded.

Observed results:
- `test_policy.py`: exit 1, `SyntaxError: invalid decimal literal` at injected device line;
- `test_adapter.py`: exit 1, same syntax error;
- `test_live_transport.py`: exit 1, same syntax error.

Therefore the exact immutable candidate cannot execute its own test suite and cannot be used as the verified runtime correction package.

The source-level KOD claim of 9 + 13 + 6 = 28 PASS tests may describe pre-publication/local bytes, but it is not valid evidence for the exact immutable Git payload at `18e0cc2b...`.

## Diagnostic correlation

For the three runtime modules, removing exactly the injected device annotation from the immutable Git bytes yields SHA-256 values equal to the MANIFEST values:
- policy -> `d5bcfca6...`;
- adapter -> `e2787a37...`;
- live transport -> `3dec8563...`.

This strongly localizes the runtime-module SHA mismatch to post-hash annotation contamination. The test files also contain the annotation, but their stripped SHA-256 values still do not equal the sealed MANIFEST values, so they additionally require exact resealing from final bytes.

## Boundary status

Because the immutable payload is syntactically invalid, SHD cannot truthfully certify:
- executable exact candidate tests;
- preserved Luna/Terra/Sol behavior on the exact immutable package;
- Astra runtime admission on the exact immutable package.

Static intended code shows the requested four-model set and preserved no-tools/no-fallback/no-storage boundaries, but static intent cannot substitute for executable immutable-byte verification.

No live provider call was made.
No credential was read.
No candidate byte was modified by SHD.
No external state was mutated.

## Exact minimum correction

KOD should create a clean immutable successor package that:
1. removes all execution-tool annotation text from source/test file bytes;
2. republishes exact clean Python bytes;
3. regenerates MANIFEST blob/size/SHA-256 from the final Git-published bytes;
4. reruns the exact 9/13/6 tests against those final bytes;
5. returns the new immutable package for SHD re-verification.

## Terminal result

`FAIL_SHD_OPENAI_ASTRA_ALLOWLIST_R01_IMMUTABLE_PACKAGE_CORRUPTED`
