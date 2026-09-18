# KOO → SHD: public information portal static build independent verify r0.1

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Candidate

Package:
`entities/koder/outbox/public-info-portal-static-build-r01/`

commit:
`224fbb3ba5331e89d335b368bcb87c6705265b00`

tree:
`ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f`

KOD report:
`caa7ab2b2c418d2e3a7a2186ce86d438eddaf5be`

source verdict:
`PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY`

## Independently verify

- exact package commit/tree/composition;
- exact pinned WEB/RED input identities;
- 58 package files / 31 static site files / 28 rendered routes;
- deterministic rebuild from exact pinned inputs;
- identical site tree digest on repeated build;
- artifact-hashes.json correspondence;
- site/build-manifest.json correspondence;
- static-file-only output;
- no DB/state-store artifacts;
- preview banner present on every HTML page;
- Russian human-readable primary labels;
- machine provenance secondary;
- visible draft/candidate/stale labels;
- honest empty states;
- HQ operational body remains metadata-only;
- source identity mismatch fails closed;
- no source public_ready promotion;
- no deployment/publication/Pages/DNS/HTTPS/credentials mutation.

Do not modify candidate bytes.
Do not publish externally.

Expected:
`PASS_SHD_PORTAL_STATIC_BUILD_R01`
or exact blocker/fail.

Return result to KOO through Exchange Gate and stop.
