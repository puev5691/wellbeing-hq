# KOO → OPERATOR: fixed-IP router → Commander live control-path decision gate r0.1

status: WAITING_OPERATOR_LIVE_CONTROL_PATH_DECISION
project_time: omitted

## Human meaning

The integration package and current external Commander facts are independently verified enough for one bounded live proof.

No real Commander host command has yet been authorized by this line.

## Exact review basis

puev5691/wellbeing-hq@c3ce11348b3f8583ea3df7571c56b34d4bef1a3c:
entities/sisadmin/outbox/SIS__fixed-ip-router-commander-independent-review-r01__KOO.md

blob:
8759157bb30a94587e2a28fbcb789a15932e3d91

terminal:
PASS_SIS_FIXED_IP_ROUTER_COMMANDER_INDEPENDENT_REVIEW_R01_READY_FOR_LIVE_CONTROL_PATH_GATE

## Proposed first live proof

Logical node:
burzh

Commander device:
dd09a197-f716-4dd6-80bb-7f8e5d8260ff

Device name:
ruvds-xnqc6

Action ID:
FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ

Exact harmless/read-only command:
hostname && id -un

Purpose:
prove end-to-end binding:
current route evidence -> selected logical node -> exact Commander device -> exact task authority -> explicit OPERATOR confirmation -> actual read-only host execution -> bounded returned evidence.

Expected output semantics:
- hostname must equal ruvds-xnqc6;
- user is reported as observed evidence, not pre-assumed authority;
- no mutation is permitted.

## Required fresh checks immediately before execution

SIS must independently establish:
1. current fixed-IP route evidence/provenance/currentness for burzh;
2. exact router tree fc1bb2751cc5d662037a037fdecf3ece69f07adb;
3. exact profile SHA-256 b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac;
4. fresh Commander device identity and AVAILABLE state;
5. exact action authority locator and action_id;
6. exact node/device binding;
7. explicit OPERATOR confirmation.

Any mismatch -> STOP.

## Authority boundary if approved

Authorized:
- one Commander execution only;
- exact device above;
- exact command above;
- read-only result capture;
- immutable result/readback back to KOO.

Not authorized:
- any second command;
- shell expansion into other diagnostics;
- file reads beyond command-internal system identity output;
- host mutation;
- deployment;
- service/config/network changes;
- automatic failover/node switching;
- credentials/provider operations;
- DNS fallback;
- shard WRITE;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

## Exact OPERATOR choices

A.
AUTHORIZE_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY

B.
DEFER_FIXED_IP_COMMANDER_LIVE_PROOF_R01

## Terminal

PASS_KOO_FIXED_IP_COMMANDER_LIVE_CONTROL_PATH_GATE_R01_WAITING_OPERATOR
