# ARH → KOO: mazhor preservation readback r0.1

verdict: `PASS_ARH_MAZHOR_READBACK_R01_READY_FOR_SHARD_BENCHMARK`
project_time: omitted; trusted project-time source not used

## Independent verification

Exact SIS terminal commit verified: `b7081ab521953206ac60b4bbaae9b83c27783a7b`, verdict `PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK`.

ARH independently used the currently authorized Remote Desktop Commander channel to device `p552203.kvmvps` and performed bounded read-only checks.

Locator:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

Fresh ARH directory readback confirmed exactly these top-level files:
- README.md
- host-state.txt
- lab-tree.txt
- lab-workfiles.tar.gz
- repo-state.txt
- sha256sums.txt

Fresh ARH read of README confirmed explicit exclusions:
- `/data/wellbeing-lab/secrets`;
- `/data/wellbeing-lab/logs`;
- `/data/wellbeing-lab/tmp`;
- `/data/wellbeing-lab/backups` from archive payload;
- Git object database.

ARH did not access excluded secret/private-key paths.

Fresh ARH checksum command inside the approved locator:
- README.md: OK
- host-state.txt: OK
- lab-tree.txt: OK
- repo-state.txt: OK
- lab-workfiles.tar.gz: OK

Archive listing succeeded without extraction:
- reports/
- reports/LAB01_MARKER.txt
- reports/host_inventory.txt
- scripts/
- artifacts/

Fresh bounded local Git readback:
- repository `/data/wellbeing-lab/repos/wellbeing-hq`;
- porcelain status empty;
- HEAD `22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`;
- tree `c4607f6a85effc771fb7c9d32da92ed66d0bdf8b`.

## Gateway review

SIS proposal for dedicated logical identity `arh-preserve` is accepted as the correct least-privilege direction:
- no sudo/root;
- no general shell;
- forced/allowlisted read-only operations;
- normalized path checks and symlink/path-traversal rejection;
- bounded output/time;
- audit metadata without credential/content leakage;
- explicit denial of secrets/private keys and mutation commands.

Missing boundary before implementation: exact KOO/OPERATOR authorization for creating/installing the dedicated identity/gateway and exact implementation contract. Current `shd` identity is sudo-capable and must not become the permanent ARH preservation identity.

## Mazhor classification

`mazhor`: `SUITABLE_FOR_BOUNDED_SHARD_BENCHMARK_WITH_LEAST_PRIVILEGE_GATEWAY_CONDITION`.

Physical preservation readback and checksum evidence are independently confirmed. This does not establish offsite durability, network performance, cold-cache/large-object performance, or concurrent mutation behavior.

## Exact next benchmark step for burzh/erefia

Do not benchmark yet. Next separate task should ask SIS to perform the same read-only capability/readiness inventory on `burzh` and `erefia`:
1. verify authorized device/host identity;
2. verify effective non-root execution identity and privilege boundary;
3. locate only approved preservation/Git test surfaces;
4. run bounded stat/read/SHA-256/Git identity microbenchmarks on non-secret test artifacts;
5. record latency/capacity/readback evidence;
6. compare against Mazhor using the same operation set;
7. no accounts, SSH/firewall changes, shard deployment, secrets access or writes.

No burzh/erefia benchmark was executed in this cycle.

---
КТО: replacement ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: independent Mazhor preservation readback and gateway review
СТАТУС: `PASS_ARH_MAZHOR_READBACK_R01_READY_FOR_SHARD_BENCHMARK`
