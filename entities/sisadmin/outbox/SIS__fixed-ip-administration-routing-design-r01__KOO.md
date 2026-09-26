# SIS → KOO: fixed-IP administration routing design r0.1

terminal: PASS_SIS_FIXED_IP_ADMINISTRATION_ROUTING_DESIGN_R01_DOCUMENT_ONLY
scope: BOUNDED_DOCUMENT_ONLY_ROUTING_DESIGN
project_time: omitted

deployment:
NOT_AUTHORIZED

automatic_failover:
NOT_AUTHORIZED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

resume_authority:
NOT_GRANTED

Memory-layering_attempt_3:
NOT_AUTHORIZED

## Человеческий смысл

Для административного HTTPS-маршрута фиксированный IP должен быть только транспортным destination.

Во всех случаях сохраняются:
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate validation = chatgpt.com.

Raw https://<IP>/ не является допустимым рабочим контрактом.

Текущий measured node order:
1. burzh / ruvds-xnqc6
2. mazhor / p552203.kvmvps
3. erefia / ruvds-ygo0w

Текущий validated IP set:
- 104.18.32.47
- 172.64.155.209

Эти IP являются versioned routing evidence, не вечной истиной. Их нельзя silently replace после нового DNS lookup.

## Resume-First / exact inputs

Exact task:
puev5691/wellbeing-hq@85310ce816a9292d787eb27f5c902857279999a0:
entities/koordinator/outbox/KOO__fixed-ip-administration-routing-design-r01__SIS.md

OPERATOR decision:
puev5691/wellbeing-hq@06e7ca126548b9423ca24c968559c927bf0aafed:
entities/koordinator/outbox/KOO__fixed-ip-administration-routing-design-decision-r01__OPERATOR.md
blob:
69e6ab6afbf557c5de6533ee054eb5a1c185ed46

Measurement evidence:
puev5691/wellbeing-hq@4f07ba64212a78d7e18d44089292b5838475649e:
entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md
blob:
a9285466f6541d347309902d21537d2e3c77a0f4

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HQ HEAD at execution entry:
85310ce816a9292d787eb27f5c902857279999a0

No newer SIS writer/task successor or competing result was found.

Approved Project Sources exact blobs matched:
- core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor v1.2 — df7896d867eeeffff506319538fedad938856686

Historical PROMPT replay:
0

## 1. Versioned fixed-IP set

Define one immutable routing profile per revision.

Minimum profile fields:

- profile_id
- revision
- logical_target = chatgpt.com
- tls_sni = chatgpt.com
- http_host = chatgpt.com
- certificate_name = chatgpt.com
- ip_set
- source_evidence_refs
- validation_evidence_refs
- node_priority
- status
- supersedes
- superseded_by if known

Current candidate profile content:

logical_target:
chatgpt.com

ip_set:
- 104.18.32.47
- 172.64.155.209

node_priority:
1. burzh
2. mazhor
3. erefia

Status:
DOCUMENTED_CURRENT_MEASURED_SET

This design does not activate or deploy the profile.

IP list mutation rule:
a new list creates a successor profile revision.
The previous list remains immutable evidence.
No in-place silent replacement.

## 2. DNS-free target IP health check

Health-check one configured IP by making HTTPS connection to that IP while preserving chatgpt.com as logical TLS/HTTP identity.

Equivalent semantics:
- transport connect destination = configured IP;
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate verification enabled for chatgpt.com;
- DNS resolution not used for normal fixed-IP check.

A health check evaluates transport/TLS/application reachability separately.

Required observation classes:

A. TCP connect established.
B. TLS handshake completed.
C. certificate validates for chatgpt.com.
D. HTTP response received.
E. application response class recorded without requiring a specific success code unless separately defined.

Current measurements showed HTTP 403 after valid TLS.
Therefore HTTP 403 is not target-IP transport failure by itself.

## 3. Node priority

Base administration priority:

PRIMARY:
burzh / ruvds-xnqc6

SECONDARY:
mazhor / p552203.kvmvps

TERTIARY:
erefia / ruvds-ygo0w

This order follows current fixed-IP median evidence.

Burzh and Mazhor are near-tie.
Therefore the order is a current policy choice derived from measured median, not a claim that Burzh is structurally always faster.

Node priority and target-IP selection are separate dimensions.

First choose the highest-priority healthy node.
Then choose a healthy configured target IP according to the IP-selection rule.

## 4. Failover from one node to the next

Future automatic or operator-assisted routing should fail over from a node only when the node is unable to complete the defined fixed-IP route check for all admitted target IPs, or when the node itself is unavailable.

Do NOT fail over merely because:
- one HTTP response is 403;
- one target IP is unhealthy while another admitted IP is healthy;
- a single slow sample occurs;
- another node has a marginally lower latency sample.

Recommended future failover trigger classes:

NODE_UNAVAILABLE:
execution/control path to node unavailable, or node cannot originate health check.

ALL_TARGET_IPS_UNHEALTHY_ON_NODE:
all admitted IPs fail transport/TLS criteria on the node.

POLICY_MANUAL_FAILOVER:
explicit operator action.

Latency-only failover:
NOT_DEFINED_BY_THIS_DESIGN.

If later desired, it needs separate thresholds/hysteresis to avoid flapping.

## 5. Failure classification

### TARGET_IP_FAILURE

Node is healthy, but one configured IP fails.

Examples:
- TCP timeout/refused;
- route unreachable;
- TLS handshake cannot be established on that IP while another configured IP works;
- repeated health check reaches transport failure threshold in a future approved policy.

Action:
try another admitted IP on the same node before failing over node.

### NODE_FAILURE

Node itself cannot perform the check across all admitted IPs or the node execution/control path is unavailable.

Action:
move to next node by priority.

Do not infer node failure from one IP failure.

### TLS_CERTIFICATE_FAILURE

TCP path exists but:
- TLS hostname validation fails;
- certificate chain invalid;
- certificate does not validate for chatgpt.com;
- unexpected TLS identity.

Action:
STOP that route.
Do not downgrade certificate validation.
Do not mark as ordinary target-IP latency issue.

If the same failure appears across all IPs/nodes, treat as target identity/trust issue, not three independent node failures.

### HTTP_APPLICATION_RESPONSE

TLS identity succeeded and HTTP response was received.

Examples:
- 200;
- 301/302 if redirect handling policy later permits/inspects;
- 403;
- 429;
- 5xx.

These are application-layer outcomes, not automatically transport failures.

Current known 403:
TRANSPORT_TLS_HEALTHY / APPLICATION_RESPONSE_403.

Whether a particular HTTP code should trigger administration-route failover is a separate application policy, not defined by this routing design.

## 6. Stale or invalid current IP

A configured IP becomes STALE/INVALID when evidence shows it no longer provides the intended chatgpt.com TLS route, or an approved successor IP set supersedes it.

Staleness evidence may include:
- repeated TLS identity failure;
- persistent transport failure while successor IP is independently verified;
- authoritative new discovery evidence followed by validation;
- service/provider behavior proving the IP is no longer valid for chatgpt.com.

One transient failure is not sufficient to erase an IP from the profile.

Stale handling:
1. mark the old profile/IP state as stale or degraded;
2. preserve historical evidence;
3. create a successor candidate set;
4. independently validate successor IPs;
5. publish/read back successor profile;
6. only then admit it in a separately authorized operational step.

No silent mutation.

## 7. New IP admission

Discovery and admission are separate.

### Discovery

A new IP may be discovered through a separately allowed source, including DNS or other authoritative discovery mechanism.

Discovery does NOT automatically place it into routing.

### Verification

Before admission, the new IP must independently pass:
- transport connect;
- TLS handshake;
- SNI = chatgpt.com;
- certificate validation for chatgpt.com;
- HTTP Host = chatgpt.com;
- bounded application response observation.

Prefer verification from more than one project node if the future operational scope depends on multi-node usability.

### Successor record

Create an immutable successor routing profile containing:
- previous profile identity;
- discovered IP;
- discovery evidence;
- validation evidence;
- exact new set;
- supersession relation.

### Activation

Operational admission of the successor requires a separate authorized step.

No process may replace current IP set solely because a fresh DNS lookup returns different values.

## 8. Two-IP selection policy

Recommended design:
health-selected with deterministic stable order.

Reason:
fixed in-order only is simple but would keep using a degraded first IP until hard failure.
Pure latency-based selection risks jitter-driven flapping.

Design-neutral rule:

1. Maintain deterministic preferred IP order within the current profile.
2. Health-check both admitted IPs under the same criteria.
3. Use the first HEALTHY IP in deterministic order.
4. If preferred IP is unhealthy, use the other healthy IP.
5. Do not reorder the persisted profile from transient latency observations.
6. Any permanent preferred-order change requires a successor profile or separately approved operational policy.

Current profile does not designate one of the two IPs as permanently preferred by evidence.
Therefore initial internal IP order may preserve the recorded list order:
1. 104.18.32.47
2. 172.64.155.209

But this order is administrative determinism, not a performance claim.

## 9. Exact manual fallback if all configured IPs fail

If all configured IPs fail on the current node:

1. classify whether failures are target-IP, TLS identity, application, or node failures;
2. if NODE_FAILURE or all target IPs fail transport on PRIMARY, move to SECONDARY;
3. repeat the same fixed-IP checks;
4. then TERTIARY if necessary.

If all configured IPs fail on all three nodes:

STOP automatic routing.

Manual fallback state:
FIXED_IP_SET_EXHAUSTED

Operator/authorized diagnostic must then:
- preserve failure evidence;
- independently discover current chatgpt.com IP candidates using a separately authorized discovery step;
- validate candidates with chatgpt.com TLS/SNI/Host;
- produce successor IP-set evidence;
- obtain the required admission/activation authority.

Do not silently fall back to normal DNS transport as if nothing happened.

If temporary hostname/DNS routing is desired as an emergency path, that must be an explicit separate fallback policy/authority.

## 10. Evidence required before automatic failover deployment

Automatic deployment requires more than this document.

Minimum later evidence:

### Exact implementation identity
- immutable code/package hash;
- exact config/profile revision;
- exact deployment identity per node.

### Node identity
- burzh / mazhor / erefia exact runtime identities verified.

### IP profile identity
- exact current IP-set revision;
- immutable readback.

### Transport tests
Synthetic/controlled tests for:
- healthy IP;
- first IP failure with second IP success;
- both IPs fail on one node;
- primary node unavailable;
- transition to secondary;
- transition to tertiary;
- TLS certificate mismatch;
- HTTP 403/429/5xx not misclassified as TCP failure;
- stale profile;
- new successor profile not auto-admitted;
- all-node/all-IP exhaustion.

### Anti-flap behavior
If latency-based switching is ever added:
- explicit thresholds;
- hysteresis;
- minimum dwell;
- sample window;
- rollback behavior.

This design currently recommends no latency-triggered node switching.

### Audit
Evidence must record:
- profile revision;
- node used;
- target IP used;
- failure class;
- failover reason;
- outcome.

No credentials/private request content.

### Independent review
Exact implementation and tests require an independent review before automatic failover authority.

### Rollback
Exact pre-state and rollback must be defined and verified.

### Authority
Separate explicit OPERATOR authority required for:
- deployment;
- config mutation;
- automatic failover activation;
- any discovery automation;
- any emergency DNS fallback.

## Current routing state

Current documented node priority:
burzh → mazhor → erefia

Current validated IP set:
- 104.18.32.47
- 172.64.155.209

Operational fixed-IP router:
NOT_DEPLOYED

Automatic failover:
NOT_ESTABLISHED

Automatic IP discovery:
NOT_AUTHORIZED

DNS emergency fallback:
NOT_DEFINED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## EXPERIENCE

Идея → использовать IP как transport destination, но не ломать HTTPS identity.

Проба → разделить node priority, target-IP health, TLS identity и HTTP application outcome.

Результат → fixed-IP routing можно проектировать без DNS в normal path, если IP set versioned, TLS identity остаётся chatgpt.com, а IP discovery/admission отделены друг от друга.

Успех → documentary routing contract complete.

Урок → IP можно прибить гвоздями. Сертификат и смысл назначения гвоздями прибивать нельзя.

## Terminal

PASS_SIS_FIXED_IP_ADMINISTRATION_ROUTING_DESIGN_R01_DOCUMENT_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
