# KOO → OPERATOR: fixed-IP router activation decision gate r0.1

status: WAITING_OPERATOR_ACTIVATION_DECISION
project_time: omitted

## Human meaning

The exact reviewed package has now passed:
1. KOD implementation and package publication;
2. KOD 17/17 local synthetic tests;
3. independent SIS package review;
4. SIS deployment-readiness on all three actual nodes;
5. 51/51 node-local synthetic test executions;
6. 6/6 fixed-IP live HTTPS probes with chatgpt.com TLS identity.

The exact package remains staged inert on:
- burzh / ruvds-xnqc6;
- mazhor / p552203.kvmvps;
- erefia / ruvds-ygo0w.

No production route/service is active.

## Exact readiness result

puev5691/wellbeing-hq@b86e2ddfa7d592c6e478bed7717516e693af7e86:
entities/sisadmin/outbox/SIS__fixed-ip-router-deployment-readiness-r01__KOO.md

blob:
d14d5fcc589e33c12712a78c73637f0e04f50e85

terminal:
PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE

## Fresh reconciliation

No newer activation authority, activation task, or competing fixed-IP router activation result was found after the readiness result.

Therefore activation remains blocked on OPERATOR decision.

## Recommended bounded activation model

The first operational activation should be OPERATOR-assisted/manual, not automatic failover.

If authorized, SIS may:
- install/promote the exact reviewed bytes/profile from inert staging into one explicitly defined operational location per node;
- preserve exact pre-state and rollback;
- expose an explicit manual invocation/control path;
- perform one bounded post-install verification;
- keep node priority burzh → mazhor → erefia;
- keep same-node alternate-IP retry logic;
- preserve TLS SNI/HTTP Host/certificate validation = chatgpt.com;
- keep DNS fallback disabled;
- record closed audit evidence.

This first activation does NOT authorize autonomous switching between nodes or autonomous IP discovery/admission.

## Still separately prohibited unless later authorized

- automatic failover activation;
- automatic node switching without explicit operator action;
- automatic IP discovery/admission;
- DNS fallback;
- provider/API calls;
- credential/secret changes;
- shard WRITE;
- unrelated automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE claim;
- resume authority;
- Memory-layering attempt 3.

## Exact OPERATOR choices

A.
AUTHORIZE_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_NO_AUTO_FAILOVER

Meaning:
authorize bounded operational installation/promotion of the exact reviewed package on the three verified nodes, explicit manual/operator-assisted invocation only, one bounded post-install verification, exact rollback evidence, and no autonomous failover/discovery/DNS fallback.

B.
DEFER_FIXED_IP_ROUTER_ACTIVATION_R01_KEEP_INERT_STAGED

Meaning:
leave the exact reviewed package staged inert on all three nodes and stop before production activation.

## Terminal

PASS_KOO_FIXED_IP_ROUTER_ACTIVATION_DECISION_GATE_R01_WAITING_OPERATOR
