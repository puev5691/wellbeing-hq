# KOO record: OPERATOR authorizes bounded fixed-IP router deployment-readiness r0.1

status: OPERATOR_AUTHORITY_RECORDED
project_time: omitted

Exact OPERATOR authority token:

AUTHORIZE_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_BOUNDED_NO_AUTO_ACTIVATION

Authority meaning:
allow SIS to perform only bounded deployment-readiness work for the exact reviewed fixed-IP router package.

Authorized:
- fresh Resume-First and writer/current-task/supersession checks;
- exact pre-state capture on burzh, mazhor, erefia;
- non-active staging of the exact reviewed package;
- exact checksum/readback verification;
- local synthetic test execution on each node;
- bounded live HTTPS probe to the admitted fixed IP set while preserving chatgpt.com TLS identity;
- rollback/readback evidence;
- node-by-node readiness result back to KOO.

Not authorized:
- automatic failover activation;
- replacing existing production paths;
- daemon/service enablement for production use;
- provider/API calls;
- credentials/secrets;
- DNS changes or DNS fallback;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE claim;
- resume authority;
- Memory-layering attempt 3.

Exact package:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01
tree fc1bb2751cc5d662037a037fdecf3ece69f07adb

Independent SIS review:
puev5691/wellbeing-hq@d4b2afc3bd9fa05ddade9d2e8a273d18a69badd4:
entities/sisadmin/outbox/SIS__fixed-ip-router-independent-package-review-r01__KOO.md
blob 63ff89a3116e377ecb68c56a181a86ff94308f6e
terminal PASS_SIS_FIXED_IP_ROUTER_INDEPENDENT_PACKAGE_REVIEW_R01_READY_FOR_DEPLOYMENT_GATE
