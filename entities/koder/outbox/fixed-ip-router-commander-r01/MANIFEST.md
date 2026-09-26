# Fixed-IP router → Commander integration r0.1 manifest

status: CANDIDATE_NOT_DEPLOYED
scope: OPERATOR_ASSISTED_IMPLEMENTATION_PACKAGE_ONLY
project_time: omitted

Task: `puev5691/wellbeing-hq@4e2bade099a125462c1cbcb2aba268b80471a826:entities/koordinator/outbox/KOO__fixed-ip-router-commander-integration-r01__KOD.md`, blob `76dc5faeae715dd04a511c13277749de91088634`.

Authority: `puev5691/wellbeing-hq@08670d2c4b6322d461bf3744b9df43ac67323a90:entities/koordinator/outbox/KOO__authorize-KOD-fixed-ip-router-commander-integration-r01__OPERATOR.md`, blob `094123b1a70607152d73d2d632dd56e6a8bcdac9`.

KOO current state: `puev5691/wellbeing-hq@b3098eabccef13f86dc2c2686dc7102f89fd46f8:entities/koordinator/current/KOO__fixed-ip-router-current-state-r01.md`, blob `804c28f8052fbdeadbfb62cd2fe995a6e5d2c9e3`, `OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER`.

## Exact members

`integration.py`, `offline_cli.py`, `mapping.schema.json`, `mapping.current.json`, `fixtures/operator-selection.synthetic.json`, `test_integration.py`, `README.md`, `MANIFEST.md`, `SHA256SUMS.txt`.

`SHA256SUMS.txt` covers the actual bytes of the eight other members, excluding itself. Generated `__pycache__` is excluded. Git tree/blob identities and immutable readback are reported in the addressed KOD result.

## Verification and limits

`python -m unittest -v test_integration.py`: 14/14 PASS, 0 failures after correcting an offline test helper setup error. The correction did not alter mapping or production data. One synthetic offline CLI fixture returns `TASK_AUTHORITY_MISSING`. SHA-256 checks pass 8/8. All tests used local fixtures/mocks, no Commander/provider/host/DNS access.

Current availability of the three Commander devices and the trustworthiness of externally supplied inventory/route/authority evidence remain UNKNOWN to this package. It creates no authenticated Commander API connector and issues no host command. Independent SIS review must distinguish source-code selection from an operationally authorized control path. Deployment and host mutation were not performed.
