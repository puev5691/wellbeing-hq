# KOO → SIS: P552203 request.json + gateway retirement r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.7
scope: BOUNDED_OPERATOR_ASSISTED_RETIREMENT_R02
project_time: omitted

Resume-First.

## Current KOO writer

puev5691/wellbeing-hq@9c5e330719fa4410eca76e91a128bfcc29d56c45:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

## Intended SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

SIS must fresh-verify writer continuity, supersession and exact task/authority before any mutation.

## Exact authority

puev5691/wellbeing-hq@7391f4eaa8ba17b0ffbb5d90eb041459c138f5ab:
entities/koordinator/outbox/KOO__authorize-P552203-request-json-and-gateway-retirement-r02__OPERATOR.md

blob:
b9d380c20f53df9a1d5ba212e365febd4920b484

decision:
AUTHORIZE_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02

## Exact classification basis

puev5691/wellbeing-hq@3b6c83751de929af53daa6ca41a88494673d5c13:
entities/sisadmin/outbox/SIS__P552203-run-wb-shard-gateway-read-only-classification-r01__KOO.md

blob:
e899990f4dc3cbfde8d743c3aef9f295dc4b5660

terminal:
PASS_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01

Classified stale candidate:
/run/wb-shard-gateway/request.json

## Exact host

expected hostname:
p552203.kvmvps

Fresh-verify host identity before any mutation.

## Task

Perform only the exact bounded operator-assisted retirement r0.2.

Phase 1 — fresh reconciliation/prechecks:
- current SIS writer;
- exact authority/task identities;
- no superseding task/result/authority;
- exact host identity;
- service still inactive/dead;
- unit still disabled;
- no reverse dependencies;
- no enable symlinks;
- no related active units;
- no current project runtime consumer;
- /run/wb-shard-gateway contains exactly one expected entry request.json;
- request.json remains regular file at exact path and no current use is observed;
- /var/lib/wellbeing/shard-gateway empty/unreferenced;
- /var/log/wb-shard-gateway empty/unreferenced;
- exact preservation package still readable.

If any check fails or is UNKNOWN:
STOP before mutation and return exact blocker.

Phase 2 — if direct privileged execution is unavailable, prepare one self-contained privileged command block for OPERATOR.

The block may only:
1. repeat necessary fail-closed prechecks;
2. remove /run/wb-shard-gateway/request.json;
3. verify /run/wb-shard-gateway is then empty;
4. remove /etc/systemd/system/wellbeing-shard-gateway-verify.service;
5. remove /opt/wb-shard-gateway;
6. remove /var/lib/wellbeing/shard-gateway only if empty/unreferenced;
7. remove /run/wb-shard-gateway only if empty/unreferenced;
8. remove /var/log/wb-shard-gateway only if empty/unreferenced;
9. run systemd daemon-reload only if required;
10. print exact post-mutation evidence.

The block must:
- identify host;
- stop on first unexpected condition;
- not suppress proof-relevant errors;
- touch no unrelated paths;
- print sufficient evidence for immutable result verification.

OPERATOR returns complete output to SIS.

Phase 3 — verify output/results:
- do not infer omitted evidence;
- if all prechecks and postchecks are proven, publish immutable PASS result;
- otherwise publish exact BLOCKED_/FAIL_ result with no extra mutation attempt.

## Not authorized

- unrelated path mutation;
- /data/wellbeing-lab mutation;
- reset/reimage;
- proof-root creation;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay.

## Expected terminal

PASS_SIS_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02_COMPLETE

or exact BLOCKED_*/FAIL_*.

After immutable result/readback and addressed return to KOO, STOP.
