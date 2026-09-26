# SIS → KOO: fixed-IP router deployment-readiness r0.1

terminal: PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE
scope: BOUNDED_DEPLOYMENT_READINESS_NO_AUTO_ACTIVATION
project_time: omitted

## Человеческий результат

Bounded deployment-readiness for the exact reviewed fixed-IP router package completed on all three exact nodes.

The exact package was staged only in inert per-user staging directories.
No production path, service, listener, DNS setting, provider/API, credentials, shard state, automation or Project Source was changed.

On each node:
- exact 12-member package staged;
- package checksums/readback passed;
- local Python synthetic suite passed 17/17;
- both exact fixed IPv4 live HTTPS probes completed through the staged reviewed node_probe;
- TLS identity/certificate validation for chatgpt.com passed;
- HTTP 403 was observed as application-layer response, not transport failure;
- test-generated __pycache__ was removed;
- staged exact reviewed bytes remain inert;
- no related process/service/listener was left active.

Result:
READY_FOR_SEPARATE_ACTIVATION_DECISION_GATE only.

No activation authority is created by this PASS.

## Resume-First / authority

Exact task:
puev5691/wellbeing-hq@ee727dbf3674dbb9af4a870b9d13c958e2c3a1aa:
entities/koordinator/outbox/KOO__fixed-ip-router-deployment-readiness-r01__SIS.md

task blob:
cfaf5ea6abe0911ecc30b1cf69760a816799022d

Exact authority:
puev5691/wellbeing-hq@3325856954f2d323fe0a9fbfca75b1c6fa80b9b4:
entities/koordinator/outbox/KOO__authorize-SIS-fixed-ip-router-deployment-readiness-r01__OPERATOR.md

authority token:
AUTHORIZE_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_BOUNDED_NO_AUTO_ACTIVATION

Exact reviewed package:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01

tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

Independent review:
puev5691/wellbeing-hq@d4b2afc3bd9fa05ddade9d2e8a273d18a69badd4:
entities/sisadmin/outbox/SIS__fixed-ip-router-independent-package-review-r01__KOO.md

blob:
63ff89a3116e377ecb68c56a181a86ff94308f6e

terminal:
PASS_SIS_FIXED_IP_ROUTER_INDEPENDENT_PACKAGE_REVIEW_R01_READY_FOR_DEPLOYMENT_GATE

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HQ HEAD at final reconciliation:
648dab5bd5a58fb156ff1ed90f352dae99a398e4

No newer competing SIS deployment-readiness result or exact task successor found before publication.

## Node identities and pre-state

### burzh

Expected:
burzh / ruvds-xnqc6

Observed:
hostname = ruvds-xnqc6
execution user = pev5691
uid = 1000
HOME = /home/pev5691

Staging path:
 /home/pev5691/.local/share/wbnp-fixed-ip-router/staging/fc1bb2751cc5d662037a037fdecf3ece69f07adb

Pre-state:
- staging path absent;
- no related fixed-ip-router/wbnp-fixed-ip service unit found;
- no related fixed-ip-router/wbnp-fixed-ip active listener found;
- no pre-existing package-related process found beyond the read-only inspection command itself.

Runtime:
Python 3.12.3
OpenSSL 3.0.13
default verify paths present
default SSL context:
check_hostname = true
verify_mode = CERT_REQUIRED

Note:
Remote Desktop shell emitted inherited getcwd warnings because its prior working directory no longer existed. Commands used explicit absolute paths/cd for staging and verification. No package/readiness failure followed from this shell condition.

### mazhor

Expected:
mazhor / p552203.kvmvps

Observed:
hostname = p552203.kvmvps
execution user = shd
uid = 1000
HOME = /home/shd

Staging path:
 /home/shd/.local/share/wbnp-fixed-ip-router/staging/fc1bb2751cc5d662037a037fdecf3ece69f07adb

Pre-state:
- staging path absent;
- no related service unit found;
- no related listener found;
- no pre-existing package-related process found beyond inspection command.

Runtime:
Python 3.12.3
OpenSSL 3.0.13
default verify paths present
default SSL context requires hostname verification and CERT_REQUIRED.

Important correction:
the first read-only pre-state candidate used /home/pev5691 by pattern and found it absent.
Before any mutation SIS checked the actual execution identity/HOME and used /home/shd for all staging.
No write was made to /home/pev5691 on mazhor.

### erefia

Expected:
erefia / ruvds-ygo0w

Observed:
hostname = ruvds-ygo0w
execution user = pev5691
uid = 1000
HOME = /home/pev5691

Staging path:
 /home/pev5691/.local/share/wbnp-fixed-ip-router/staging/fc1bb2751cc5d662037a037fdecf3ece69f07adb

Pre-state:
- staging path absent;
- no related service unit found;
- no related listener found;
- no pre-existing package-related process found beyond inspection command.

Runtime:
Python 3.12.3
OpenSSL 3.0.13
default verify paths present
default SSL context requires hostname verification and CERT_REQUIRED.

## Non-active staging

Mutation performed on each node only:
create inert per-user staging directories and write the exact reviewed 12 package members.

No:
- production location replacement;
- PATH mutation;
- cron;
- systemd unit;
- service enable/start/reload;
- automatic execution;
- credential file;
- DNS setting;
- provider/API integration.

Package members on each node after staging:

MANIFEST.md
README.md
SHA256SUMS.txt
fixtures/admission.synthetic.json
fixtures/observations.synthetic.json
fixtures/profile.synthetic-admitted.json
node_probe.py
offline_cli.py
profile.current.json
profile.schema.json
router.py
test_router.py

Exact member count:
12 on burzh
12 on mazhor
12 on erefia

## Checksum / readback

On every node:
sha256sum -c SHA256SUMS.txt
= 11/11 OK
exit = 0

SHA256SUMS.txt self-hash on every node:
1efd68b1052bb156b8f262312ba759c4112b0b7af4fd1dd3aa0d7d10e3d11d0c

This equals the SHA256SUMS.txt hash independently established during package review.

Therefore exact staged byte identity is established for all 12 members on all three nodes.

## Local synthetic tests

Exact command on each node from exact staging directory:
python3 -m unittest -v test_router.py

burzh:
Ran 17 tests
OK
TEST_EXIT=0

mazhor:
Ran 17 tests
OK
TEST_EXIT=0

erefia:
Ran 17 tests
OK
TEST_EXIT=0

Local-node result:
17/17 PASS on each node
51/51 test executions PASS total

This is new node-local readiness evidence and is distinct from the earlier KOD package test report.

## Bounded live fixed-IP HTTPS probe

Exact staged node_probe.py was invoked only for:

104.18.32.47
172.64.155.209

The reviewed probe contract:
- accepts canonical numeric IPv4 only;
- socket transport destination = numeric IPv4:443;
- ssl.create_default_context();
- check_hostname = True;
- verify_mode = ssl.CERT_REQUIRED;
- server_hostname/SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- no DNS fallback.

### burzh / ruvds-xnqc6

104.18.32.47:
HTTP_APPLICATION_RESPONSE
HTTP status 403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
HTTP status 403

Result:
transport PASS
TLS handshake PASS
certificate validation for chatgpt.com PASS
HTTP application layer reachable PASS
DNS fallback NOT USED

### mazhor / p552203.kvmvps

104.18.32.47:
HTTP_APPLICATION_RESPONSE
HTTP status 403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
HTTP status 403

Result:
transport PASS
TLS handshake PASS
certificate validation for chatgpt.com PASS
HTTP application layer reachable PASS
DNS fallback NOT USED

### erefia / ruvds-ygo0w

104.18.32.47:
HTTP_APPLICATION_RESPONSE
HTTP status 403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
HTTP status 403

Result:
transport PASS
TLS handshake PASS
certificate validation for chatgpt.com PASS
HTTP application layer reachable PASS
DNS fallback NOT USED

Aggregate:
6/6 node×IP live probes reached valid TLS/application response.

HTTP 403 is recorded as HTTP_APPLICATION_RESPONSE and is not treated as transport/TLS failure.

## Rollback / post-state evidence

Synthetic test execution generated Python __pycache__ directories only inside inert staging.

SIS removed only those test-generated __pycache__ directories.

The reviewed staging package itself is intentionally preserved inert for a potential separately authorized activation gate.

Post-state on every node:

- exact stage directory remains;
- exactly 12 reviewed members remain;
- SHA256SUMS 11/11 PASS;
- SHA256SUMS.txt self-hash exact PASS;
- no related fixed-ip-router/wbnp-fixed-ip process active;
- no related service unit created/enabled/started/reloaded;
- no related listener active;
- no production path changed;
- no DNS setting/fallback changed;
- no provider/API or credentials used.

Rollback boundary proven by this task:
the only persistent mutation is the separately identified inert staging directory containing exact reviewed bytes.
It can later be removed as one bounded staging artifact if a separately authorized gate chooses rollback/removal.

Not proven:
production deployment rollback, because no production deployment occurred.

## Blockers

None for bounded deployment-readiness.

## Activation gate statement

A separate activation decision gate can now be opened.

This result does NOT open it automatically and does NOT authorize activation.

The following remain NOT AUTHORIZED:
- automatic failover activation;
- production-path replacement;
- production service enable/start/reload;
- provider/API;
- credentials/secrets;
- DNS changes or DNS fallback;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

## EXPERIENCE

Идея → доказать не только корректность package bytes, но и совместимость exact reviewed package с тремя реальными runtime/trust/network environments без включения production route.

Проба → pre-state → inert per-user staging → exact checksum/readback → 17 local synthetic tests per node → two numeric-IP HTTPS probes per node → cleanup generated cache → post-state/readback.

Результат → exact package passes on all three nodes; 51/51 synthetic test executions PASS; 6/6 fixed-IP TLS probes PASS to application response; no production route or service activated.

Успех → bounded deployment-readiness PASS.

Урок → staging path must follow the actual execution identity, not a remembered username. Mazhor reminded us that even boring details like $HOME can still ambush an otherwise respectable deployment plan.

## Terminal

PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
