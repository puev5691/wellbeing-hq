# KOO → SIS: independent fixed-IP router → Commander integration review r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: INDEPENDENT_PACKAGE_AND_CONTROL_PATH_EVIDENCE_REVIEW_NO_DEPLOYMENT
project_time: omitted

## Purpose

Independently verify the exact KOD integration package and the external control-path facts it depends on.

This is NOT deployment and NOT authorization to execute host commands.

## Exact KOD result

puev5691/wellbeing-hq@25cb49462f4d0ff04c49c5c10ab30ff667bb85af:
entities/koder/outbox/KOD__fixed-ip-router-commander-integration-r01-result__KOO.md

blob:
b902f3c0d5ee4f2ab9a14152bea9bc0ad69196f9

terminal:
PASS_KOD_FIXED_IP_ROUTER_COMMANDER_INTEGRATION_R01_READY_FOR_SIS_REVIEW

## Exact package

puev5691/wellbeing-hq@c177b506543ae367727d02600d753530f194c3e6:
entities/koder/outbox/fixed-ip-router-commander-r01

tree:
40cea4a800a2cd9c1bf625b582b6f0c95ca6becc

KOD-reported integrity/tests:
- SHA256SUMS 8/8 PASS;
- immutable package readback 9/9 PASS;
- unit tests 14/14 PASS;
- Commander calls 0;
- host commands 0;
- deployment 0.

Do not adopt these PASS claims without independent review of the immutable package.

## Current fixed-IP router state

puev5691/wellbeing-hq@b3098eabccef13f86dc2c2686dc7102f89fd46f8:
entities/koordinator/current/KOO__fixed-ip-router-current-state-r01.md

blob:
804c28f8052fbdeadbfb62cd2fe995a6e5d2c9e3

status:
OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER

## Current SIS writer basis

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

terminal:
writer_gate_pass_replacement_sis_r06_authoritative

## Required independent checks

### 1. Package identity/integrity

Verify exact tree, member list, manifest, checksums and absence of undeclared executable/deployment/credential artifacts.

### 2. Exact Commander device identities

Independently verify current project mapping:

- burzh / ruvds-xnqc6
- mazhor / p552203.kvmvps
- erefia / ruvds-ygo0w

Expected IDs from KOD evidence, to be independently checked:

- burzh: dd09a197-f716-4dd6-80bb-7f8e5d8260ff
- mazhor: 830038a0-232b-4d83-b52d-0e9973126165
- erefia: c55d5659-f2c8-416d-8b40-9bac8c80c30d

Do not infer identity from hostname alone if current Commander evidence can verify device identity.

### 3. Fresh Commander availability

Perform only a bounded read-only Commander inventory/status check sufficient to establish whether each exact device is currently available/online.

No host command execution is authorized by this review.

Return per-device current availability:
- AVAILABLE
- UNAVAILABLE
- UNKNOWN

with evidence.

### 4. Route evidence trust/currentness

Verify that any route-health input admitted by the integration can be tied to:

- exact fixed-IP router tree:
  fc1bb2751cc5d662037a037fdecf3ece69f07adb
- exact current profile digest:
  b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac
- explicit manual selected node;
- fixed-IP trace;
- no DNS fallback;
- TLS_CERTIFICATE_FAILURE = STOP;
- HTTP application response after valid TLS does not imply route failure.

Check whether KOD package merely accepts a caller claim such as verified_by_supervisor without authenticating it. If so, classify the missing trust root exactly and do not promote placeholder fields to trusted evidence.

### 5. Task authority boundary

Verify that package cannot turn node/device selection into command authority.

Required:
- action/task authority is separate;
- node and device binding are checked against authority;
- operator/manual confirmation is explicit;
- missing/mismatched authority blocks execution readiness;
- package does not contain or infer arbitrary host-command authority.

Assess what exact external authority evidence would be required before a real Commander action can be executed.

### 6. No automatic fallback/authority expansion

Verify:
- no automatic fallback to another Commander device;
- no automatic node switching;
- no automatic failover;
- no automatic IP discovery/admission;
- no DNS fallback;
- no credential acquisition/readout;
- no provider/API behavior;
- no hidden host command execution;
- no deployment side effect.

### 7. Test review

Independently inspect the 14 tests and confirm their claimed coverage.

A bounded local/non-host rerun is optional only if exact bytes can be executed safely without Commander/network/host side effects.

Do NOT perform Commander calls from the package.

## Required result

Return one immutable SIS result addressed to KOO.

Full bounded PASS terminal:

PASS_SIS_FIXED_IP_ROUTER_COMMANDER_INDEPENDENT_REVIEW_R01_READY_FOR_LIVE_CONTROL_PATH_GATE

PASS means only:
the package and current external identities/evidence are coherent enough to reach a separate live control-path decision gate.

PASS does NOT authorize:
- deployment;
- host mutation;
- Commander host command execution;
- automatic failover;
- autonomous switching;
- credential/provider operations;
- DNS fallback;
- shard WRITE;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

If exact current device identity/availability or evidence trust cannot be established, return exact BLOCKED_* with the smallest missing fact.

After immutable result + readback + addressed return to KOO, STOP.
