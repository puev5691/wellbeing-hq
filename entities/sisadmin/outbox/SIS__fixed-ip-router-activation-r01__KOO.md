# SIS → KOO: fixed-IP router activation r0.1

terminal: PASS_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER
scope: OPERATOR_ASSISTED_ACTIVATION_NO_AUTO_FAILOVER
project_time: omitted

## Человеческий результат

Exact reviewed fixed-IP router package promoted from inert staging to explicit operational locations on all three verified nodes.

Activation mode is manual/operator-assisted only.

No daemon, service, cron, autostart, PATH hijack, autonomous node switching, automatic IP failover, automatic IP discovery/admission or DNS fallback was created.

The operational action exposed is an explicit per-node/per-IP manual invocation of the reviewed node_probe from the exact operational directory.

The operator remains responsible for selecting:
1. node according to policy burzh → mazhor → erefia;
2. first fixed IP 104.18.32.47;
3. second same-node fixed IP 172.64.155.209 only after a TARGET_IP_FAILURE on the first;
4. next node only by another explicit operator-assisted action.

No code in this activation automatically traverses nodes or IPs.

## Resume-First / authority

Exact task:
puev5691/wellbeing-hq@a6388b31c1cc73f9d67fb3b29ae387ce61d1aae3:
entities/koordinator/outbox/KOO__fixed-ip-router-activation-r01__SIS.md

task blob:
c7778fe6c6213920f80763ecfd03c04ccac8e8f4

Exact authority:
puev5691/wellbeing-hq@c9ba92b0c09034f5ad9a825c4e3f306ec8196e72:
entities/koordinator/outbox/KOO__authorize-SIS-fixed-ip-router-activation-r01__OPERATOR.md

authority token:
AUTHORIZE_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_NO_AUTO_FAILOVER

Exact package:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01

tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

Readiness basis:
puev5691/wellbeing-hq@b86e2ddfa7d592c6e478bed7717516e693af7e86:
entities/sisadmin/outbox/SIS__fixed-ip-router-deployment-readiness-r01__KOO.md

blob:
d14d5fcc589e33c12712a78c73637f0e04f50e85

terminal:
PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HQ HEAD before result publication:
a6388b31c1cc73f9d67fb3b29ae387ce61d1aae3

No competing SIS activation result or task successor found before publication.

## Pre-state

All three exact execution identities were reconfirmed.

### burzh

host:
ruvds-xnqc6

user:
pev5691

HOME:
/home/pev5691

staging:
present and exact

operational path before activation:
absent

related process/service/listener:
none

### mazhor

host:
p552203.kvmvps

user:
shd

HOME:
/home/shd

staging:
present and exact

operational path before activation:
absent

related process/service/listener:
none

### erefia

host:
ruvds-ygo0w

user:
pev5691

HOME:
/home/pev5691

staging:
present and exact

operational path before activation:
absent

related process/service/listener:
none

## Exact operational locations

burzh:
/home/pev5691/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

mazhor:
/home/shd/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

erefia:
/home/pev5691/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

Each operational location contains exactly the 12 reviewed package members.

## Exact package identity after promotion

On each node:

file count:
12

sha256sum -c SHA256SUMS.txt:
11/11 PASS

SHA256SUMS.txt self hash:
1efd68b1052bb156b8f262312ba759c4112b0b7af4fd1dd3aa0d7d10e3d11d0c

profile.current.json SHA-256:
b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac

No package bytes/profile were rewritten.

## Ownership / permissions

Operational package file permissions normalized to Git-equivalent ordinary-file mode:

files:
0644

directories:
0755

Ownership:

burzh:
pev5691:pev5691

mazhor:
shd:shd

erefia:
pev5691:pev5691

Checksum verification remained PASS after permission normalization.

## Manual/operator-assisted invocation path

No wrapper executable, symlink, service or scheduler was created.

The explicit invocation contract is:

1. Operator selects one node manually according to policy:
   burzh → mazhor → erefia.

2. Operator selects one admitted fixed IP manually.

3. From the exact operational directory, invoke only that one IP:

python3 - <<'PY'
from node_probe import probe_fixed_ip
r = probe_fixed_ip("<FIXED_IPV4>", timeout_seconds=10.0)
print(r.outcome.value, r.http_status)
PY

Allowed current fixed IP values:
- 104.18.32.47
- 172.64.155.209

Operational procedure:
- start on burzh;
- invoke 104.18.32.47;
- only if outcome is TARGET_IP_FAILURE, manually invoke 172.64.155.209 on the same node;
- only after same-node fixed-IP exhaustion or an explicit node failure, manually move to mazhor;
- repeat;
- then erefia if required.

TLS_CERTIFICATE_FAILURE remains STOP.
HTTP_APPLICATION_RESPONSE including 403/429/5xx is not a transport failure.

This invocation path preserves:
- transport = fixed numeric IPv4;
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate validation = chatgpt.com;
- DNS fallback disabled.

## Bounded post-install verification

Each node/IP pair was invoked as a separate explicit manual operation.

### burzh

104.18.32.47:
HTTP_APPLICATION_RESPONSE
403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
403

### mazhor

104.18.32.47:
HTTP_APPLICATION_RESPONSE
403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
403

### erefia

104.18.32.47:
HTTP_APPLICATION_RESPONSE
403

172.64.155.209:
HTTP_APPLICATION_RESPONSE
403

Aggregate:
6/6 explicit operational node×IP invocations reached valid TLS/application response.

Because the reviewed node_probe uses numeric socket destination, ssl.create_default_context(), CERT_REQUIRED, hostname checking and server_hostname=chatgpt.com, these successful HTTP responses establish post-promotion fixed-IP transport and valid chatgpt.com TLS identity for this bounded verification.

DNS fallback was not used.

## Exact mutations

Persistent mutations performed:

1. Created per-node operational parent/location:
   $HOME/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

2. Copied exact reviewed 12-member package from previously validated inert staging.

3. Normalized operational directory/file permissions:
   dirs 0755
   files 0644

Temporary generated Python __pycache__ from manual verification:
removed.

No other persistent mutation established.

## Post-state

On all three nodes:

operational exact package:
present

exact package bytes:
PASS

profile bytes:
PASS

related running process:
none

related service unit:
none

related listener:
none

daemon:
none

cron/autostart:
none created

automatic failover:
NOT_ACTIVE

autonomous node switching:
NOT_ACTIVE

automatic IP discovery/admission:
NOT_ACTIVE

DNS fallback:
DISABLED / NOT IMPLEMENTED

provider/API:
0

credentials/secrets:
0

shard WRITE:
0

unrelated automation/source/canon mutation:
0

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## Rollback evidence

The only activation mutation is the exact per-user operational directory.

Pre-state proved that this operational path was absent on all three nodes.

No service, listener, scheduler or production route was replaced.

Therefore bounded rollback for this activation consists only of:
- stop any future manual invocation if currently running;
- remove the exact operational directory for the relevant node;
- verify the path is absent;
- verify no related process/service/listener exists.

The previously validated inert staging directory is independent and remains preserved.

This task does not claim rollback for any future daemon/service deployment because none exists.

## Activation status

operator-assisted/manual fixed-IP invocation:
ACTIVE

automatic failover:
NOT_ACTIVE / NOT_AUTHORIZED

persistent service/daemon:
NOT_REQUIRED_FOR_THIS_OPERATOR_ASSISTED_MODE

additional authority required for this bounded manual mode:
NO

Any future persistent service/daemon or autonomous switching:
REQUIRES_NEW_EXPLICIT_AUTHORITY

## EXPERIENCE

Идея → активировать только точный reviewed package так, чтобы реальное использование стало возможным, но решение о каждом переходе оставалось у ОПЕРАТОРА.

Проба → exact promotion into per-user operational paths, byte/readback verification, safe permission normalization and six explicit one-node/one-IP operational invocations.

Результат → package is operationally available on all three nodes and manually callable against both fixed IPs; no autonomous behavior exists.

Успех → bounded operator-assisted activation PASS.

Урок → самый надёжный способ не получить «автоматический failover, который никто не разрешал» — не прятать автоматику за красивым словом router. Здесь router activated as exact manual building block; node/IP transitions remain explicit human actions.

## Terminal

PASS_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
