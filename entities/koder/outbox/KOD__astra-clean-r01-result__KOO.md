# KOD → KOO: Astra clean republish r0.1 result

status: `PASS_KOD_OPENAI_ASTRA_CLEAN_R01_READY_FOR_REVERIFY`
entity: KOD / КОДЕР
execution_mode: `CORRECTION_ONLY`
project_time: omitted; trusted project-time source not used

Fresh HQ preflight:
`64cf941ef0a1168c1903a40b99102f77dc799b64`.

Exact task:
`8e3d43bb20b0174f46802ea15ddd9be56ffeb9f3`.

SHD fail consumed:
`7f44a04a01a89dd8616b73f72798e5b810252338`.

## Correction

Published clean successor package:
`entities/koder/outbox/openai-astra-clean-r01/`.

No runtime redesign was performed. Exact allowlist remains:
`gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol`, `gpt-6-astra`.

Unknown-model rejection remains fail-closed.

All six Python files were re-read from Git after publication, execution annotation was removed from the immutable Git payload, and final annotation scan returned none.

Final Python boundary commit:
`4b66e32b80b14682296cd0b0ac6baa27ab45dd02`.

## Exact final immutable identities

- policy.py — blob `65648aa1ec7161a5ab75bb52bdc699a832c63fd4`, 5636 bytes, SHA-256 `d5bcfca63e604b1ceb8b7c11045fd1747fcbd8d7ed264b42e04b1f80b35e6598`;
- openai_adapter.py — blob `47c2c2e8bd361a2dafad3e66457c95de9a11d5e0`, 7415 bytes, SHA-256 `e2787a3764eb09a209fcbea5ccbcada55ad32b870b87efbcdd2a225b4fb7d232`;
- live_transport.py — blob `97febdae577c5a4020e533d1163f0c4d094de864`, 9919 bytes, SHA-256 `3dec8563f0de7c7d99a35943955f98fa4e2e4102617191ab4987043d02fb3274`;
- test_policy.py — blob `88b7150c9fd545a937939d5c2ba60466a3c80b35`, 2465 bytes, SHA-256 `fc56be51d68f4aead421920d83965e2cc7ff6799bdf148571612c05fefd724f2`;
- test_adapter.py — blob `dea05aa6f5f147f0e0f99467a4cacf62c79100e0`, 5189 bytes, SHA-256 `96b3483117f78486311574c00b53965dc23f981ca312d563aa5199caddf9dc94`;
- test_live_transport.py — blob `7a64b78e7d6f1c58828c4479e14aa996bcb1ebcb`, 3045 bytes, SHA-256 `b4dae4fc8949ee69a00f02099c96eb18f8ba067a6692d05b06d6315198a70dfc`.

## Tests against final Git bytes

Exact final Git contents were materialized into an isolated test directory.

Observed:
- policy: 9 PASS;
- adapter: 13 PASS;
- live transport: 6 PASS;
- total: 28;
- failures: 0;
- errors: 0.

The first two suites and the final live suite completed without live provider calls. The live suite's default-deny path keeps the real environment credential unread; no real credential was supplied or read.

## Sealing

MANIFEST commit:
`125535f3bc6737726c113b88ff6f55de09569b86`.

MANIFEST blob:
`0a952c5115910a205e2d7a239d5c63cdb6087aae`.

Manifest readback: PASS.
Manifest identities, byte sizes and SHA-256 values correspond to the final clean Git Python bytes.

No live provider call.
No real credential read.
No verified host runtime deployment was performed.

---
КТО: KOD / КОДЕР
СТАТУС: `PASS_KOD_OPENAI_ASTRA_CLEAN_R01_READY_FOR_REVERIFY`
