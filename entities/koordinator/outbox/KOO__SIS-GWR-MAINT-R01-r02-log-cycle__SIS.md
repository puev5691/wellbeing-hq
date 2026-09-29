# KOO -> SIS: NEW GWR r0.2 log-residue cycle

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Authority:
puev5691/wellbeing-hq@83ad1d2ccac592bbffeb731d4077bd6bcba7c519:
entities/koordinator/outbox/KOO__approve-SIS-GWR-MAINT-R01-r02-standing-authority__OPERATOR.md

Candidate:
puev5691/wellbeing-hq@7dc9c475ea166ae3170ae9af2cbc111c0da0cc5e:
entities/shtabist/outbox/SHT__SIS-GWR-MAINT-R01-r02-candidate__OPERATOR-KOO.md
blob 782c4d7595aac7daeef8b09212e965753f351cc1

Current SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Causal blocker:
puev5691/wellbeing-hq@1cbbb48c6eb1cbef9f39e7d4dff963d773a53e26
BLOCKED_SIS_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02_LOG_DIR_NONEMPTY

Exact scope:
/var/log/wb-shard-gateway

Action:
execute one NEW exact SIS-GWR-MAINT-R01 r0.2 cycle under the approved standing authority.

Use exact r0.2 sequence and gates:
Resume-First -> preservation prerequisite -> INSPECT -> CLASSIFY -> OBJECT_RETIREMENT_ADMISSION -> pre-mutation reverify -> RETIRE admitted objects only -> VERIFY.

Apply every fail-closed STOP and exclusion from exact r0.2.

No historical PROMPT replay.
No automatic activation.

Mandatory finish:
publish immutable result and return exact locator/terminal to KOO.
Then STOP.
