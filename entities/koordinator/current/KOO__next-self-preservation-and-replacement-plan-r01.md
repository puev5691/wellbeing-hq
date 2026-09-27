# KOO current plan: next self-preservation and replacement r0.1

status: KOO_SELF_PRESERVATION_NEXT_AFTER_SHD_HANDOFF
project_time: omitted

Reason:
current KOO r0.9 has accumulated substantial authoritative work after its existing recovery snapshot. Waiting for chat failure would risk losing the newest causal state and force reconstruction from GitHub history.

Sequence after SHD replacement handoff closes:
1. KOO fresh reconciliation;
2. KOO self-snapshot of current role, writer, active tasks, blockers, completed work, next causal steps and experience;
3. preservation package with exact source map/manifest/checksums;
4. ARH independent preservation and immutable external readback;
5. only after preservation, exact KOO handoff/freeze authority;
6. replacement KOO cold-start initiation;
7. separate Writer Gate;
8. resume only fresh current tasks, no historical replay.

Required preservation content must include at least:
- current operational-memory/shards recovered plan and current blockers;
- standing fixed-IP -> Commander transport state;
- File/Artifact Service r0.2 review chain and current SHD replacement state;
- EOM pilot / memory-layering attempt-3 prohibition;
- human-readable Entity response pattern;
- exact next allowed causal steps;
- relevant experience/anti-regression lessons.

No automatic replacement or freeze is executed by this plan.

terminal:
PASS_KOO_SELF_PRESERVATION_NEXT_AFTER_SHD_HANDOFF_R01
