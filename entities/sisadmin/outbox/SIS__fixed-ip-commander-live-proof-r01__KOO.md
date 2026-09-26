# SIS → KOO: fixed-IP Commander live proof r0.1 — burzh identity read-only

terminal: PASS_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY
scope: EXACT_ONE_COMMAND_READ_ONLY_LIVE_PROOF
project_time: omitted

## Human result

One exact Remote Desktop Commander host action was executed against the exact authorized burzh device.

Exact command:
hostname && id -un

Attempt count:
1

Exit status:
0

Observed stdout:
ruvds-xnqc6
pev5691

Hostname match expected ruvds-xnqc6:
YES

Observed username:
pev5691

No second host command was executed.
No fallback was attempted.
No mutation was performed by the authorized command.

## Resume-First / exact authority

Exact task:
puev5691/wellbeing-hq@b4015780f05aafda69a278937870eabe005fdab2:
entities/koordinator/outbox/KOO__fixed-ip-commander-live-proof-r01__SIS.md

task blob:
9b289d084a04f51fd8d931697dfd74ba25107e00

Exact authority:
puev5691/wellbeing-hq@52a3ae55a7a999bc171b6a6d877d43180797e152:
entities/koordinator/outbox/KOO__authorize-SIS-fixed-ip-commander-live-proof-r01__OPERATOR.md

authority token:
AUTHORIZE_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY

Authorized action binding:
- node: burzh
- device_id: dd09a197-f716-4dd6-80bb-7f8e5d8260ff
- device_name: ruvds-xnqc6
- action_id: FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ
- exact command: hostname && id -un

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

writer blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HQ HEAD before action:
b4015780f05aafda69a278937870eabe005fdab2

No newer competing SIS live-proof task/result or successor/supersession was found before action.

## Current route evidence verified before action

Current KOO fixed-IP router state:
entities/koordinator/current/KOO__fixed-ip-router-current-state-r01.md

blob:
804c28f8052fbdeadbfb62cd2fe995a6e5d2c9e3

status:
OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

Exact router tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

Fresh exact tree read:
PASS

Exact profile.current.json:
puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01/profile.current.json

Fresh independently recalculated profile SHA-256:
b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac

Expected profile SHA-256:
b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac

Profile digest match:
PASS

Current route policy confirmed:
- burzh first
- fixed-IP set 104.18.32.47 / 172.64.155.209
- operator-assisted only
- no automatic failover
- TLS_CERTIFICATE_FAILURE = STOP
- HTTP_APPLICATION_RESPONSE after valid TLS is not route failure
- DNS fallback disabled

## Fresh Commander identity / availability before action

Fresh read-only Commander inventory:

device_name:
ruvds-xnqc6

device_id:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

status:
online

auth_token:
valid

availability:
AVAILABLE

Expected binding:
burzh → ruvds-xnqc6 → dd09a197-f716-4dd6-80bb-7f8e5d8260ff

Binding:
PASS

Independent review basis:
puev5691/wellbeing-hq@c3ce11348b3f8583ea3df7571c56b34d4bef1a3c:
entities/sisadmin/outbox/SIS__fixed-ip-router-commander-independent-review-r01__KOO.md

blob:
8759157bb30a94587e2a28fbcb789a15932e3d91

terminal:
PASS_SIS_FIXED_IP_ROUTER_COMMANDER_INDEPENDENT_REVIEW_R01_READY_FOR_LIVE_CONTROL_PATH_GATE

## Action execution

Exact Commander target:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

Exact action_id:
FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ

Exact command:
hostname && id -un

attempt_count:
1

Process result:
exit code 0

stdout:
ruvds-xnqc6
pev5691

Required comparison:
hostname == ruvds-xnqc6:
PASS

Observed username:
pev5691

## Environment warning

Remote Desktop Commander emitted inherited shell/getcwd warnings before stdout because its prior working directory no longer existed.

These warnings did not alter:
- exact command identity;
- exact device identity;
- hostname result;
- username result;
- exit status.

No diagnostic or repair command was executed because the authority explicitly prohibited any second command.

## Mutation / command count boundary

Host commands executed:
1

Second host command:
0

Fallback command:
0

Additional diagnosis:
0

Host mutation:
0

Deployment:
0

Automatic failover:
0

Credentials/provider operation:
0

DNS fallback:
0

Shard WRITE:
0

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## Meaning

This proof establishes only that the separately authorized live Commander control path can:
- bind the exact burzh logical target to the exact Commander device;
- execute the exact one-shot read-only action;
- return the expected host identity and execution username.

It does not establish generic host-command authority, mutation authority, automatic failover, or standing execution permission.

## EXPERIENCE

Идея → доказать реальный control path одной безвредной exact-командой, не превращая успешный selector в общий remote shell authority.

Проба → fresh route/device/authority gate, затем ровно один execution: hostname && id -un.

Результат → exact burzh device returned ruvds-xnqc6 / pev5691, exit 0.

Успех → one-shot live proof PASS.

Урок → control path становится доказанным не тогда, когда есть красивый mapping, а когда exact authority, exact device и exact action сходятся в одном проверяемом исполнении. И да, одна команда действительно может остаться одной командой, если человечество очень постарается.

## Terminal

PASS_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
