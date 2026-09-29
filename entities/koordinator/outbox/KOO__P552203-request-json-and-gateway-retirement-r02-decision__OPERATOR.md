# KOO → OPERATOR: bounded retirement decision for stale /run/wb-shard-gateway/request.json and gateway contour

status: WAITING_OPERATOR_DECISION
entity: KOO / КООРДИНАТОР
project_time: omitted

## Human meaning

SIS r0.7 completed a bounded root-level read-only classification of the unexpected runtime residue.

Exact stale candidate:
/run/wb-shard-gateway/request.json

Observed:
- regular file;
- 302 bytes;
- owner/group arh-preserve:arh-preserve;
- mode 600;
- current open-file references NONE OBSERVED;
- socket references NONE OBSERVED;
- process references NONE OBSERVED;
- only systemd reference is old wellbeing-shard-gateway-verify.service;
- service inactive/dead and disabled;
- current consumer NONE OBSERVED;
- active dependency NOT PROVEN;
- creator UNKNOWN.

Classification:
STALE_RETIRABLE_CANDIDATE

No mutation has occurred.

## Exact evidence

SIS classification:

puev5691/wellbeing-hq@3b6c83751de929af53daa6ca41a88494673d5c13:
entities/sisadmin/outbox/SIS__P552203-run-wb-shard-gateway-read-only-classification-r01__KOO.md

blob:
e899990f4dc3cbfde8d743c3aef9f295dc4b5660

terminal:
PASS_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01

## Existing retirement lineage

Prior OPERATOR retirement decision:

puev5691/wellbeing-hq@74c92d0c745e35ee4393e22b6db36a286b0f9bae:
entities/koordinator/outbox/KOO__P552203-gateway-retirement-approved-r01__OPERATOR.md

decision:
APPROVE_P552203_GATEWAY_RETIREMENT_R01

Prior operator-assisted path authority:

puev5691/wellbeing-hq@eb631f2d42b6c0ea16baaaa8cc02595095e6d896:
entities/koordinator/outbox/KOO__authorize-P552203-gateway-retirement-r01-operator-assisted-privileged-path__OPERATOR.md

decision:
AUTHORIZE_P552203_GATEWAY_RETIREMENT_R01_OPERATOR_ASSISTED_PRIVILEGED_PATH

That authority did not permit deletion of unexpected non-empty runtime content.

## Exact decision requested

AUTHORIZE_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02

Meaning:

Authorize SIS r0.7 to supervise one bounded operator-assisted privileged retirement attempt on exact host p552203.kvmvps.

Before any mutation SIS must fresh-verify:
- current SIS writer and task/authority;
- host identity;
- service still inactive/dead;
- unit still disabled;
- no reverse dependencies;
- no enable symlinks;
- no related active units;
- no current project runtime consumer;
- /run/wb-shard-gateway contains exactly one entry:
  /run/wb-shard-gateway/request.json
- request.json still matches the classified object sufficiently for safe retirement:
  regular file, expected path, no observed current use;
- /var/lib/wellbeing/shard-gateway and /var/log/wb-shard-gateway remain empty/unreferenced as required by the existing retirement scope;
- exact preservation package remains readable;
- no superseding task/result/authority exists.

If any condition changed or is UNKNOWN:
STOP before mutation and return exact blocker.

If all prechecks PASS, authorize removal only of:

1. /run/wb-shard-gateway/request.json
2. /etc/systemd/system/wellbeing-shard-gateway-verify.service
3. /opt/wb-shard-gateway
4. /var/lib/wellbeing/shard-gateway, only if empty and unreferenced
5. /run/wb-shard-gateway, only after request.json removal and only if then empty/unreferenced
6. /var/log/wb-shard-gateway, only if empty and unreferenced

Then:
- run systemd daemon-reload only if required after unit removal;
- perform exact post-mutation verification;
- return immutable SIS result to KOO.

## Hard boundaries

This decision does NOT authorize:
- deletion/mutation of any unrelated path;
- /data/wellbeing-lab mutation;
- reset/reimage;
- proof-root creation;
- backend selection/install/run;
- T01-T20 execution;
- CHECKPOINT_DURABLE claim;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay.

## Alternatives

OPERATOR may instead choose:

HOLD_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02

which leaves all current objects unchanged and requires a later separate decision.

## Decision required

Choose exactly one:

AUTHORIZE_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02

or

HOLD_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02
