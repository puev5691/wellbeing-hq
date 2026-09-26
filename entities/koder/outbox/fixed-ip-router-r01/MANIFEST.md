# Fixed-IP router r0.1 — immutable package manifest

status: CANDIDATE_NOT_DEPLOYED
scope: IMPLEMENTATION_PACKAGE_ONLY
project_time: omitted

## Origin

Task: `puev5691/wellbeing-hq@1f784036f56942026454bda58dcac4705be48a63:entities/koordinator/outbox/KOO__fixed-ip-router-implementation-package-r01__KOD.md`, blob `262ed1e37d505a2ad34fd2ae132891e59a746119`.

Authority handoff: `puev5691/wellbeing-hq@a0ecf4fda0bd4223d1ffdfb8c62fdb9b0a0bdf21:entities/sisadmin/outbox/SIS__fixed-ip-router-implementation-package-authority-handoff-r01__KOO.md`, blob `7e3a14eff25356a0af190a840e14c15cb7afd162`.

SIS design: `puev5691/wellbeing-hq@2d61ac65616b7b30e3a11b6c682ec027094e11dd:entities/sisadmin/outbox/SIS__fixed-ip-administration-routing-design-r01__KOO.md`, blob `399afd89134f877e61d68d0bb2047efd168067dc`.

Measurement: `puev5691/wellbeing-hq@4f07ba64212a78d7e18d44089292b5838475649e:entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md`, blob `a9285466f6541d347309902d21537d2e3c77a0f4`.

## Package members

`router.py`, `node_probe.py`, `offline_cli.py`, `profile.schema.json`, `profile.current.json`, `fixtures/profile.synthetic-admitted.json`, `fixtures/admission.synthetic.json`, `fixtures/observations.synthetic.json`, `test_router.py`, `README.md`, `MANIFEST.md`, `SHA256SUMS.txt`.

`SHA256SUMS.txt` contains SHA-256 of every member except itself. No generated `__pycache__` or `.pyc` file is part of this package. Git blob identities are recorded by immutable publication/readback, separate from SHA-256.

## Offline verification

`python -m unittest -v test_router.py`: 17 tests, 17 PASS, 0 failed/errors. Synthetic/mock only; no network. Covers all requested cases: healthy IP, same-node second IP, two-IP failure, primary node unavailable, secondary/tertiary, TLS certificate mismatch, HTTP 403/429/5xx, stale and unadmitted successor profiles, all-node exhaustion, manual interface, missing observation, identity override, profile digest mismatch, output filtering and numeric-IP/SNI/Host/certificate-contract mock.

`offline_cli.py` synthetic fixture: default selected `burzh/172.64.155.209` after first IP failed, HTTP 403 classified `HTTP_APPLICATION_RESPONSE`; explicit `--manual-node mazhor` selected `mazhor/104.18.32.47`. No operational admission evidence follows from this synthetic record.

Deployment: 0. Host access: 0. Live provider/API requests: 0. Credentials: 0. DNS changes: 0. Shard writes: 0. Automation changes: 0. Project Sources/canon changes: 0. Automatic failover activation: 0. CHECKPOINT_DURABLE: NOT_ESTABLISHED. Resume authority: NOT_GRANTED. Memory-layering attempt 3: NOT_AUTHORIZED.

## Limits to review

The planner trusts observations and externally verified admission facts; the fixture file is not an authority source. The package does not establish authenticated remote node execution, node identity attestation, live IP health, profile approval or revocation, operational failover, rollback pre-state or safe deployment. Those are SIS review and later separately authorized gates. The node-local probe code was inspected through mocks, not run on a project node.
