# KOO → SIS: fixed-IP router activation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: OPERATOR_ASSISTED_ACTIVATION_NO_AUTO_FAILOVER
project_time: omitted

Authority:
puev5691/wellbeing-hq@c9ba92b0c09034f5ad9a825c4e3f306ec8196e72:
entities/koordinator/outbox/KOO__authorize-SIS-fixed-ip-router-activation-r01__OPERATOR.md

token:
AUTHORIZE_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_NO_AUTO_FAILOVER

Package:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01
tree fc1bb2751cc5d662037a037fdecf3ece69f07adb

Readiness:
puev5691/wellbeing-hq@b86e2ddfa7d592c6e478bed7717516e693af7e86:
entities/sisadmin/outbox/SIS__fixed-ip-router-deployment-readiness-r01__KOO.md
blob d14d5fcc589e33c12712a78c73637f0e04f50e85
terminal PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE

Current SIS writer:
puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob 05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md
terminal writer_gate_pass_replacement_sis_r06_authoritative

Resume-First before any host change.

Authorized bounded action:
1. Reconfirm exact node/pre-state on burzh, mazhor, erefia.
2. Promote the exact reviewed package from inert staging to one documented operational location per node.
3. Preserve exact bytes and current profile without rewriting.
4. Expose explicit manual/operator-assisted invocation only.
5. Verify checksums, ownership/permissions, fixed-IP HTTPS path and chatgpt.com TLS identity after promotion.
6. Record exact mutations, post-state and rollback evidence.
7. Return one immutable result to KOO.

Current policy:
node order burzh → mazhor → erefia
IPs 104.18.32.47 and 172.64.155.209
TLS SNI / HTTP Host / certificate validation = chatgpt.com
DNS fallback disabled.

Do not create or enable autonomous behavior.
If operational use would require a persistent service/daemon or any additional authority, STOP and return exact blocker/gate request instead.

Not authorized:
- automatic failover;
- autonomous node switching;
- automatic IP discovery/admission;
- DNS fallback;
- provider/API activity;
- shard WRITE;
- unrelated automation/source/canon mutation;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

Expected bounded-success terminal:
PASS_SIS_FIXED_IP_ROUTER_ACTIVATION_R01_OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

After result/readback/return to KOO, STOP.
