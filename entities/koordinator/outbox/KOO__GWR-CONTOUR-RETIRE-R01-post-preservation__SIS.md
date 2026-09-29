# KOO -> SIS: NEW GWR-CONTOUR-RETIRE-R01 post-preservation retirement

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact retirement authority:

puev5691/wellbeing-hq@7e7f4e410a78bba4eea62e89dba84f3a113acdfb:
entities/koordinator/outbox/KOO__GWR-CONTOUR-RETIRE-R01-authority__SIS.md

Exact ARH preservation PASS:

puev5691/wellbeing-hq@3d7e9cca497ee0d559acfaa46899b477e038665c:
entities/archivarius/outbox/ARH__GWR-CONTOUR-RETIRE-R01-exact-bytes-preserved__KOO.md

blob:
422273700508783484b2ee1649cfd3348b6d30ca

terminal:
PASS_ARH_GWR_CONTOUR_RETIRE_R01_EXACT_BYTES_PRESERVED

Exact private preservation locator:

host:
p552203.kvmvps

path:
/data/wellbeing-lab/private-preservation/gwr-contour-retire-r01/v01

Git commit:
63001e9fba2166ffc25f2c89a35e150c2a3f7fbb

Git tree:
f503454de4699e5388a92e6cfb67fae7180f79e7

Preserved object identities:
request.json SHA-256 e07c7a5e7220b8d8a6c144997fa3798c130c689c3b12466e08f16cd709cf0b39
audit.jsonl SHA-256 da15f7cc35535273498cab6741c6daf4b77f9f9ff8dd606e53efc8a10cdb3901
unit SHA-256 b044ebdb2ad0e7d03e0723d19eef7160d437b6c8b9bb9dd0be5cb37879bd2eac

Previous SIS execution:
CONSUMED / NON_REPLAYABLE

Do NOT replay:
puev5691/wellbeing-hq@3e3cc7dd34d5bd99d13eee34150479209df25e6c:
entities/koordinator/outbox/KOO__GWR-CONTOUR-RETIRE-R01__SIS.md

Exact host:
p552203.kvmvps

Legacy contour:
wellbeing-shard-gateway

Task:

Run one NEW exact retirement execution instance under GWR-CONTOUR-RETIRE-R01 after preservation gate PASS.

Before any mutation, fresh-verify:
- current SIS writer;
- exact task/authority identities;
- no superseding GWR task/result/authority;
- exact host identity p552203.kvmvps;
- preservation locator remains readable and exact commit/tree identities still match;
- current exact contents/objects in the approved gateway contour;
- current service/unit state;
- no active process/open-file/socket/current consumer;
- no SECRET_OR_SENSITIVE / UNKNOWN / OUT_OF_SCOPE object;
- no symlink/mount/path escape;
- every object to be removed remains inside exact allowlist;
- every DURABLE_STATE_OR_DATA / AUDIT_EVIDENCE object to be removed is covered by the exact ARH preservation PASS;
- object identity is revalidated immediately before mutation.

If any check fails, changed object requires reclassification, or any required fact is UNKNOWN:
STOP before affected mutation and return exact blocker.

Allowed mutation paths only:
- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- /run/wb-shard-gateway
- /var/lib/wellbeing/shard-gateway
- /var/log/wb-shard-gateway

Recursive/container cleanup only if every removed descendant is fresh-inspected, classified, covered by preservation where required, admitted and reverified.

Then:
- retire only admitted exact legacy objects;
- daemon-reload only if causally required after unit removal;
- perform exact post-mutation verification;
- record actual mutations, not intended ones.

Hard exclusions:
- do not mutate /data/wellbeing-lab preservation source;
- no proof roots;
- no backend select/install/run;
- no T01-T20;
- no CHECKPOINT_DURABLE;
- no memory-layering attempt 3;
- no Telegram/provider/credential work;
- no Project Sources/canons mutation;
- no unrelated host/service cleanup;
- no historical PROMPT/task replay.

Expected result:
PASS_SIS_GWR_CONTOUR_RETIRE_R01_RETIREMENT_COMPLETE_CONSUMED

or exact BLOCKED/FAIL result.

Mandatory RETURN KOO:
- exact task ref;
- terminal;
- immutable result locator;
- preservation locator used;
- actual mutations;
- post-mutation verification;
- remaining residue;
- final authority/contour state.

If whole legacy contour is verified retired:
RETIREMENT_COMPLETE_CONSUMED

After immutable result/readback and RETURN KOO, STOP.
