# P552203 STP-C preservation package r0.1

status: PACKAGE_CANDIDATE_FOR_ATOMIC_PUBLICATION
project_time: omitted
source_device: 830038a0-232b-4d83-b52d-0e9973126165
source_hostname: p552203.kvmvps
payload_files: 13

## Scope

Fresh preservation copy only. Source data was not modified, moved or deleted. Historical unattached Git blobs are not treated as task progress or recovery state.

Fail-closed secret scan of the exact approved source roots returned no blocked file. The embedded archive was inspected without extraction and returned no blocked member.

## Payload

| source locator | package relative path | bytes | SHA-256 | source mode | uid:gid | Git blob |
|---|---|---:|---|---|---|---|
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/README.md` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/README.md` | 548 | `b45563fdccde8b5c2c023c09e42395e60be504d3f3d62ea48522acde2346fa24` | `0o664` | `1000:1000` | `76ff08dfafcd973923e5551f6da8f4faa197d15d` |
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/host-state.txt` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/host-state.txt` | 3728 | `5db43dee7350defbb97faeff529339ad01b4da8394723bd0acf418630d72ae78` | `0o664` | `1000:1000` | `d8f343c16ece22bb625ecfe953786540a7925b4c` |
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/lab-tree.txt` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/lab-tree.txt` | 4533 | `dd229b72c4160af2d2ab0a6c689624d65861d13c6fe67ce0ccd4382ac7081dd6` | `0o664` | `1000:1000` | `70706e79a53f081ed83ba87c2fa3405ba55a3466` |
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/lab-workfiles.tar.gz` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/lab-workfiles.tar.gz` | 920 | `a2854f299dd42cff0175d947a148b952861fbfbe9508c87e988e26cb496c880c` | `0o664` | `1000:1000` | `7a25672351cb2f298862468c4ea50efc83ffdb80` |
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/repo-state.txt` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/repo-state.txt` | 328 | `1b56890749458552db5eca68edb65e3d57bfe73e3cadc2fe6005f186fa71cdbb` | `0o664` | `1000:1000` | `262eb904bcfd92addea0d787cd3ad3cebbfb73bc` |
| `/data/wellbeing-lab/backups/shd-pre-reinit-v01/sha256sums.txt` | `source/data/wellbeing-lab/backups/shd-pre-reinit-v01/sha256sums.txt` | 404 | `9314c0b522fcf4511583c6dd9dd1221d6728846b4b7f2d40efefb2a8932d1a6f` | `0o664` | `1000:1000` | `d948350b7d67eadddd960555080e396ce873935d` |
| `/data/wellbeing-lab/reports/LAB01_MARKER.txt` | `source/data/wellbeing-lab/reports/LAB01_MARKER.txt` | 26 | `c1329555ed3e0341cbe3d37fed5e2739774f2195eb4916be0852f37a4f89d64e` | `0o664` | `1000:1000` | `75ea4b22e04b899bb2d2792b68036ae77dd09ee5` |
| `/data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md` | `source/data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md` | 756 | `5ad32dd091e3dbbac1b102fc2fcbd465d5844613e7bdf1491bd8bfbb3011cfb7` | `0o664` | `1000:1000` | `5f5b8ec64fb7371e42a034282949e6b588c0d304` |
| `/data/wellbeing-lab/reports/host_inventory.txt` | `source/data/wellbeing-lab/reports/host_inventory.txt` | 1236 | `cb1a5728287d23cf7e3d3fa484b6a44d5ef7a2e7937d45dd87d42320349797d3` | `0o664` | `1000:1000` | `cee787525aeb66c4560b28c097ed57c8dc928b4f` |
| `/opt/wb-shard-gateway/INVOCATION.json` | `source/opt/wb-shard-gateway/INVOCATION.json` | 737 | `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218` | `0o444` | `0:0` | `193e6cb2c220cb8ed0c0fd73c99e2c98926c12a4` |
| `/opt/wb-shard-gateway/audit_sink.py` | `source/opt/wb-shard-gateway/audit_sink.py` | 1425 | `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88` | `0o444` | `0:0` | `763d4ae4945e946878a52098ba87df379f4f6762` |
| `/opt/wb-shard-gateway/gateway.py` | `source/opt/wb-shard-gateway/gateway.py` | 17053 | `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881` | `0o444` | `0:0` | `d42e58060365c4b996bf87c81f3e3eb2ad684ceb` |
| `/opt/wb-shard-gateway/harness.py` | `source/opt/wb-shard-gateway/harness.py` | 6244 | `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465` | `0o444` | `0:0` | `07202ebb8006d0d6388c119cc6576acf62d4a48b` |

## Boundaries

- no source deletion/move/modification
- no cleanup/reset/reimage
- no STP-C proof-root creation
- no backend selection/install/run
- T01-T20 executed = 0
- CHECKPOINT_DURABLE = NOT_ESTABLISHED
- memory-layering attempt 3 not run

Git file mode in the preservation repository is storage metadata only; original source mode/ownership is recorded above.
