# KOO → OPERATOR: fresh reconciliation of fixed-IP administration routing design r0.1

status: DESIGN_COMPLETE_IMPLEMENTATION_AUTHORITY_REQUIRED
project_time: omitted

## Human meaning

SIS completed the bounded fixed-IP routing design.

The design is coherent with the current OPERATOR decision:
- fixed IP transport destination;
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate validation for chatgpt.com;
- DNS excluded from normal fixed-IP transport path.

Current node priority:
1. burzh / ruvds-xnqc6
2. mazhor / p552203.kvmvps
3. erefia / ruvds-ygo0w

Current validated IP set:
- 104.18.32.47
- 172.64.155.209

## Design accepted as documentary basis

The design correctly separates:
- target-IP failure from node failure;
- transport/TLS failure from HTTP application response;
- IP discovery from IP admission;
- fixed-IP profile versioning from silent replacement;
- node failover from single-IP failover;
- TLS certificate failure from ordinary route degradation.

If all admitted IPs fail on all three nodes:
FIXED_IP_SET_EXHAUSTED
and STOP.

DNS emergency fallback remains NOT_DEFINED.

## Current state

Operational fixed-IP router:
NOT_DEPLOYED

Automatic failover:
NOT_AUTHORIZED

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

## Supersession / currentness

No newer competing routing design or OPERATOR decision was found in the checked HQ chain after the SIS result.

The completed design task authority is consumed.

No already-authorized implementation/deployment task exists for this routing design.

## Next causal gate

If OPERATOR wants to proceed toward real use, a separate bounded implementation-preparation step is required.

Recommended next step:
prepare an implementation package/specification only, without deployment.

Scope should define:
- exact router script/service behavior;
- immutable config/profile format;
- current node/IP profile;
- health-check state machine;
- failure classifications;
- manual failover command;
- logging/audit fields;
- rollback;
- test fixtures for IP/node/TLS/HTTP failure cases;
- exact deployment prerequisites.

This step must NOT:
- deploy to hosts;
- enable automatic failover;
- mutate production config;
- enable automatic IP discovery;
- enable DNS fallback;
- grant shard WRITE;
- grant resume authority.

Required separate OPERATOR authority token:

AUTHORIZE_SIS_FIXED_IP_ADMINISTRATION_ROUTER_IMPLEMENTATION_PREP_R01_DOCUMENT_ONLY

## Terminal

PASS_KOO_FIXED_IP_ROUTING_DESIGN_RECONCILED_IMPLEMENTATION_PREP_GATE_REQUIRED_R01
