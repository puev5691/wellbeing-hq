# KOO current state: fixed-IP router r0.1

status: OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER
project_time: omitted

## Human meaning

The exact reviewed fixed-IP router is operationally available on all three verified nodes in manual/operator-assisted mode only.

Current node policy:
1. burzh / ruvds-xnqc6
2. mazhor / p552203.kvmvps
3. erefia / ruvds-ygo0w

Current fixed IP set:
- 104.18.32.47
- 172.64.155.209

Per-node IP policy:
- try 104.18.32.47 first;
- only after explicit TARGET_IP_FAILURE may operator manually try 172.64.155.209 on the same node;
- node transition remains explicit operator action;
- TLS_CERTIFICATE_FAILURE = STOP;
- HTTP_APPLICATION_RESPONSE including 403/429/5xx is not transport failure.

HTTPS identity:
- transport destination = numeric IPv4;
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate validation = chatgpt.com;
- DNS fallback disabled.

## Exact operational paths

burzh:
/home/pev5691/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

mazhor:
/home/shd/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

erefia:
/home/pev5691/.local/opt/wbnp-fixed-ip-router/fc1bb2751cc5d662037a037fdecf3ece69f07adb

Exact reviewed package tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

Per SIS activation evidence on all nodes:
- exact 12 members;
- SHA256SUMS 11/11 PASS;
- profile bytes preserved;
- files 0644;
- directories 0755;
- no daemon;
- no service;
- no listener;
- no cron/autostart;
- no automatic failover.

Post-activation fixed-IP verification:
6/6 node×IP probes PASS to valid TLS/application response.

## Authority boundary

Active:
manual/operator-assisted invocation only.

Not active / not authorized:
- automatic failover;
- autonomous node switching;
- automatic IP discovery/admission;
- DNS fallback;
- provider/API use;
- credential/secret mutation;
- shard WRITE;
- unrelated automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

Any persistent daemon/service or autonomous switching requires a new explicit authority and new exact task.

## Provenance

Activation result:
puev5691/wellbeing-hq@67b41196a9bf96b15e28622e62ed4098d0a3e28d:
entities/sisadmin/outbox/SIS__fixed-ip-router-activation-r01__KOO.md
blob 06866aea4402a956d8aff6a36862f7121a27ea88
terminal PASS_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

Package:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01
tree fc1bb2751cc5d662037a037fdecf3ece69f07adb

No newer competing current-state/successor/automatic-failover authority was found in fresh reconciliation before publication.

## Terminal

PASS_KOO_FIXED_IP_ROUTER_CURRENT_STATE_R01_OPERATOR_ASSISTED_ACTIVE
