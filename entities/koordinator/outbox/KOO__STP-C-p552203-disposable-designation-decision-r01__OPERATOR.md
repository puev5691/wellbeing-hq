# KOO → OPERATOR: STP-C p552203 disposable designation decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Exact SIS inventory:
puev5691/wellbeing-hq@3b3337126d99f7ee1571d08b6f5585275b31ab4d:
entities/sisadmin/outbox/SIS__STP-C-disposable-proof-environment-inventory-r01__KOO.md
blob 72a6ac44a9dd0da8ebf6dee74465fd8b5046725e

Current blocker:
M5 = BLOCKED / NO_VERIFIED_DISPOSABLE_ENVIRONMENT
M6 = BLOCKED / ROOT_NOT_CREATED_AND_NO_ISOLATED_STORAGE_BOUNDARY

Candidate VM:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Verified existing material includes:
- /data/wellbeing-lab
- repos
- backups
- secrets
- logs
- /opt/wb-shard-gateway
All observed persistent storage is on the same /dev/sda1 ext4 root filesystem.

No live backend/project listener was observed in the bounded inventory, but no proof yet establishes that existing data may be discarded or that no project dependency relies on the VM.

## Option D1 — conditional disposable designation with preservation-first rule

Return token:

DESIGNATE_P552203_STPC_DISPOSABLE_CONDITIONAL_PRESERVATION_FIRST

Meaning:
- OPERATOR designates this exact VM as the intended future STP-C disposable proof environment;
- designation is CONDITIONAL and does not yet permit reset, erase, root creation or backend installation;
- all currently existing /data/wellbeing-lab and /opt/wb-shard-gateway material must be inventoried and dispositioned before destructive mutation;
- anything required for project/recovery/history must be preserved to a separately verified safe locator/version before deletion;
- secrets must not be copied into public/project artifacts;
- live dependency absence must be verified;
- only after preservation + dependency verification may KOO request a separate bounded mutation authority for proof-root creation/reset.

## Option D2 — do not designate this VM

Return token:

DO_NOT_DESIGNATE_P552203_STPC_DISPOSABLE

Meaning:
- p552203 remains non-disposable;
- M5/M6 stay blocked;
- KOO must search/design another disposable environment.

## Option D3 — defer

Return token:

DEFER_P552203_STPC_DISPOSABLE_DECISION

No execution or mutation follows from defer.

Hard boundary for all options:
- no erase/reset;
- no root creation;
- no backend install/run;
- no T01-T20;
- no CHECKPOINT_DURABLE;
- no live WRITE/CAS.
