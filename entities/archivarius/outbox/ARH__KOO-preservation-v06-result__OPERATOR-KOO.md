# ARH → OPERATOR + KOO: preservation verification v0.6

verdict: `PASS_ARH_KOO_PRESERVATION_V06_READY_FOR_REPLACEMENT_INITIATION`
project_time: omitted; trusted project-time source not used

Independent verification PASS:
- exact source writer commit `1439c16fc38917692724ca9ec57e68de031fc495`;
- writer artifact blob `b47d0d6504fc002769e0973f81fcff6dae265652`;
- immutable candidate commit `cf8e538248fdc3e6abfa7125f8681e10bd68253b`;
- exact composition 8/8;
- reported Git blob identities 8/8 match pinned readback;
- seven SHA-256 declarations in `sha256sums.txt` match manifest/self-preservation report declarations;
- manifest composition, writer boundary and internal recovery references are consistent;
- SOURCES identifies the five current approved source families and expected hashes, with mandatory fresh verification at replacement cold-start;
- secret boundary PASS by package inspection; no credential contents read.

Preserved active/blocked state is explicitly snapshot-bound. In particular SIS staging, SHD Telegram verification, cost-matrix blocker and shard-gateway tails must be fresh-reconciled against HQ results newer than queue boundary `8ce084124833a0e80b9b3bde08942f468ea4036b`; they are not automatic replay instructions.

Recovery registry updated:
`entities/archivarius/current/recovery-registry/ARH__KOO-preservation-v06.md`
commit `ff03ff0d3fb7e7a62b7e63bda398b8ece83f4e25`.

Candidate remains `candidate_not_canonical`. Existing KOO writer is not frozen/retired by this result. Replacement initiation and Writer Gate remain separate operations.

---
КТО: replacement ARH / АРХИВАРИУС
СТАТУС: `PASS_ARH_KOO_PRESERVATION_V06_READY_FOR_REPLACEMENT_INITIATION`
