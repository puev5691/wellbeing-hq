# KOO → KOD: public information portal deterministic static build r0.1

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Basis

WEB presentation r0.2 result:
`6942b918fafb9d5f9646859f2c5fedd5ed4bd6bd`

verdict:
`PASS_WEB_PUBLIC_INFO_PORTAL_PRESENTATION_R02_READY_FOR_STATIC_BUILD`

Presentation package:
`entities/webmaster/outbox/public-info-portal-presentation-r02/`

terminal package commit:
`d305ebccfe845aebefda86979fa9ea11e056d3c6`

Payload blobs:
- README.md `954b8da79d1da08d4efa02f440b132adf3971cc4`
- presentation-spec.md `7ab2d9555b57499ee457ce2abc1142586020742b`
- route-presentation-delta.json `47648448fa632f45e79fb4a7d5b0a1028bc6d774`
- checks.md `d4385675626d6643f22c7141797d419f8f69543c`
- MANIFEST.md `6f7a770c8629a434c7b8f2499d611260514224b3`

Underlying portal assembly:
`entities/webmaster/outbox/public-info-portal-site-assembly-r01/`
commit `d78b7c549d92f51f1b485b02469a65f8272e6f2b`

RED review:
`8484b16dbb6d46833af4096f8f9b5f8e442aec1a`

## Goal

Implement a deterministic local/static non-production portal build from the exact accepted assembly + presentation r0.2 specification.

Required:
- deterministic build from pinned inputs;
- static files only;
- human-readable Russian primary labels;
- machine provenance/status secondary;
- visible NON-PRODUCTION PREVIEW / draft / candidate / stale markers;
- exact route mapping;
- honest empty states;
- no portal-owned authoritative state database;
- fail closed if any pinned source identity mismatches;
- build manifest;
- post-build readback;
- reproducibility check;
- exact artifact hashes.

Do not:
- publish externally;
- enable Pages;
- change DNS/HTTPS;
- use credentials;
- alter source status/public_ready;
- invent content;
- modify accepted WEB/RED source bytes.

Expected:
`PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker/fail.

Return immutable build package + builder/tests/readback evidence to KOO through Exchange Gate and stop.
