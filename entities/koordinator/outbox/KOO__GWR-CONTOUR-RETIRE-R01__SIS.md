# KOO -> SIS: NEW GWR-CONTOUR-RETIRE-R01 execution

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Authority:
puev5691/wellbeing-hq@7e7f4e410a78bba4eea62e89dba84f3a113acdfb:
entities/koordinator/outbox/KOO__GWR-CONTOUR-RETIRE-R01-authority__SIS.md

Exact host:
p552203.kvmvps

Legacy contour:
wellbeing-shard-gateway

Current SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Current standing maintenance authority:
puev5691/wellbeing-hq@cb568cdb982367d34e79f19cdc27346ff4a3194d:
entities/sisadmin/current/SIS__GWR-MAINT-R01-r03-approved.md
blob 820ac3e67a1a687594c76c4df85ae50732184481

Fresh causal basis:
puev5691/wellbeing-hq@0ab967c34799890ae70023e630485e20a5d7f2f5:
entities/sisadmin/outbox/SIS__GWR-MAINT-R01-r03-log-state-cycle-result__KOO.md
blob 78f7295012ab468804a4ae034642ca662bf8a0f8

Task:
execute one NEW exact bounded retirement instance for the entire legacy wellbeing-shard-gateway contour under GWR-CONTOUR-RETIRE-R01.

Before any mutation:
- verify current SIS writer and host;
- verify authority/task freshness and no supersession;
- freshly inspect the entire exact allowlist;
- classify every object that would be removed;
- preserve every DURABLE_STATE_OR_DATA / AUDIT_EVIDENCE object exactly, with locator + immutable identity + integrity/readback + rollback/recoverability evidence;
- establish no active/current consumer;
- establish no secret/sensitive/unknown/out-of-scope object;
- establish no symlink/mount/path escape;
- admit each exact object;
- pre-mutation reverify each exact object or atomic bounded group.

Then retire only admitted objects and verify actual post-mutation state.

Allowed mutation paths only:
- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- /run/wb-shard-gateway
- /var/lib/wellbeing/shard-gateway
- /var/log/wb-shard-gateway

Recursive/container cleanup:
only if every descendant is individually covered by valid classification/preservation/admission and fresh reverify.

daemon-reload allowed only if causally required after unit removal.

Fail closed on any authority boundary from GWR-CONTOUR-RETIRE-R01.

Do not:
- replay historical tasks/PROMPT;
- touch /data/wellbeing-lab;
- create proof roots;
- run/select backend;
- run T01-T20;
- claim CHECKPOINT_DURABLE;
- run memory-layering attempt 3;
- touch Telegram/provider/credentials;
- mutate Project Sources/canons;
- touch unrelated hosts/services.

Mandatory finish:
publish immutable result/readback addressed to KOO with:
- terminal;
- actual mutations;
- preservation locators;
- verification;
- remaining residue;
- final contour state.

If whole legacy contour is verified retired:
RETIREMENT_COMPLETE_CONSUMED

Then STOP.
