# KOO → SHD r0.4: Writer Gate only

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК r0.4
scope: WRITER_GATE_ONLY
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@80a816b1e834e00de7d54a3c0dcff130103626b7:
entities/koordinator/outbox/KOO__authorize-SHD-replacement-r04-writer-gate__OPERATOR.md

Exact initiation result:
puev5691/wellbeing-hq@7ebb342337657ddca712260f4cc2116e651b3d1d:
entities/shardovik/outbox/SHD__replacement-initiation-r04-result__OPERATOR-KOO.md
blob 5877273fd56b02dd4b92e00203f7f7fa72cf8ddc
terminal initiation_verified_waiting_writer_gate

Canonical recovery:
puev5691/wellbeing-entity-bootstrap@6a5b09807bb8a6b4525620a1cbd7d6a4561f0817:
entities/shd/recovery/versions/shd-recovery-r04

Freeze authority:
puev5691/wellbeing-hq@80fba20328fb9e01072aa9c1f247b0e8f652127f:
entities/archivarius/outbox/ARH__SHD-current-writer-handoff-freeze-r04__OPERATOR-SHD.md
blob d15afe3082970a8435454f353a693b8ba2470e1d

Perform only Writer Gate.

Required:
1. fresh HQ preflight;
2. verify initiation result exact identity/status;
3. verify freeze authority exact identity and predecessor disposition;
4. verify canonical recovery r0.4 identity/currentness;
5. verify no competing replacement SHD writer;
6. verify no superseding handoff/recovery/task terminal invalidates this gate;
7. if all pass, publish one authoritative current-writer artifact for SHD r0.4;
8. exact immutable readback;
9. return Writer Gate result to KOO/OPERATOR;
10. STOP.

Do NOT:
- execute File/Artifact Service review;
- resume Telegram or TERA/WBN;
- replay historical tasks;
- mutate hosts/source/genesis/DATA/DB;
- deploy;
- access credentials;
- execute memory-layering attempt 3.

Expected terminal:
PASS_SHD_REPLACEMENT_R04_WRITER_GATE

or exact BLOCKED_* / FAIL_*.
