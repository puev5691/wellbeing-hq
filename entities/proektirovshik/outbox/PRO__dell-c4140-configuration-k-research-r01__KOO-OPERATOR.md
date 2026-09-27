# PRO: Dell PowerEdge C4140 Configuration K research r0.1

status: VERIFIED_ENGINEERING_RESEARCH_RESULT
scope: READ_ONLY_RESEARCH
project_time: omitted

## Human conclusion

Dell PowerEdge C4140 Configuration K is verified as a factory 1U Dell platform for two Intel Xeon Scalable CPUs and four SXM2 GPUs with NVLink2. Dell officially supports V100 32 GB NVLink and Dell's own performance paper tested Configuration K with 4× V100 32 GB SXM2. Therefore 128 GB aggregate HBM2 is a factory-supported/tested configuration.

Configuration K has a major architectural tradeoff: GPU-to-GPU traffic uses NVLink2, while the four-GPU complex reaches the host through one PCIe Gen3 x16 path and an internal 96-lane PCIe Gen3 switch, with all GPUs attached to one CPU side. This is narrower for host↔GPU traffic than Configuration M.

C4140 K is not an NVSwitch system. Dell documents an NVLink board plus a PCIe switch. NVIDIA documents V100 NVSwitch systems separately as DGX-2/HGX-2.

The dominant local-use limitation is physical: four 300 W GPUs, dual CPUs, eight required fans, 2000/2400 W PSUs and datacenter acoustics. Dell explicitly describes C4140 as acoustically intended for an unattended data center.

Volta remains usable but is legacy-bound: compute capability 7.0; CUDA 12.x is the last toolkit family supporting Volta; R580 is NVIDIA's last driver branch for Volta.

Engineering suitability: CONDITIONALLY_SUITABLE as a dedicated local CUDA/LLM compute node if noise/heat are isolated and the exact used unit passes acceptance tests. Not verified suitable as a quiet desk-side workstation.

## Verified architecture

FACT:
- 1U dual-socket server.
- K = 2 CPUs + 4 SXM2 GPUs + NVLink2.
- 24 DDR4 DIMM slots.
- 8 cooling fans required with two CPUs.
- Config K maximum weight 24 kg.
- chassis depth approximately 886 mm body / 924 mm maximum.
- basic display is provided by Matrox G200eW3.

CPU/RAM FACT:
- two 2nd Generation Intel Xeon Scalable processors; current Dell specs list up to 26 cores/CPU;
- both CPUs populated and same type/model;
- 24 DIMMs, six memory channels/CPU;
- RDIMM/LRDIMM;
- up to 2933 MT/s in supported configurations;
- up to 1.5 TB documented memory capacity.

## 4× V100 32 GB feasibility

VERIFIED_RESULT:
Dell lists V100 32 GB PCIe/NVLink as supported and K as four-GPU NVLINK2.

Dell performance paper explicitly tested Configuration K with:
- 4× V100 32 GB SXM2;
- dual Xeon Gold 6148;
- 384 GB RAM;
- dual 2000 W PSU.

CALCULATION:
4 × 32 GB = 128 GB aggregate HBM2.
This is not one hardware-coherent 128 GB GPU.

## Topology

FACT:
Dell system overview gives Configuration K one x16 processor↔GPU-complex PCIe link.
Dell Technical Guide says B/G/K use an internal 96-lane PCIe Gen3 switch.
Dell performance paper says K uses NVLink GPU↔GPU and all four GPUs connect to a single CPU.

Verified high-level topology:

2 CPUs linked by UPI
→ one PCIe Gen3 x16 host path
→ internal 96-lane PCIe Gen3 switch
→ 4× V100 SXM2
↔ NVLink2 GPU fabric.

V100 SXM2 FACT:
- max power 300 W;
- HBM2 bandwidth 900 GB/s;
- SXM2 NVLink specification up to 300 GB/s aggregate bidirectional.

NVSwitch VERIFIED_RESULT:
ABSENT from documented C4140 K architecture.

UNKNOWN:
exact live pairwise NVLink matrix/link health on any used unit. Physical acceptance must collect:
nvidia-smi topo -m
nvidia-smi nvlink --status
and preferably DCGM topology/link diagnostics.

## Power / cooling / acoustics

CALCULATION:
GPU-only ceiling = 4 × 300 W = 1200 W.
Whole-system wall power remains UNKNOWN until exact configuration is measured.

FACT:
Dell offers 2000 W and 2400 W PSUs and dual redundancy.

For K at 4×300 W GPU full concurrent load, Dell's recommended ambient ceiling falls as CPU TDP rises: about 25°C at 2×70 W CPU, 22°C at 2×105 W, 21°C at 2×125 W, and 18°C at 2×150/165 W.

FACT:
Dell calls the acoustic target an unattended data center and notes hearing-protection/monitoring may be expected in such environments.

Implication:
human-adjacent use needs an acoustic/thermal placement solution.

## Serviceability / management / lifecycle

FACT:
Dell service documentation covers SXM2 GPUs, NVLink shroud/board area, fans, PSUs and cabling.
iDRAC9/Lifecycle Controller provides out-of-band management.
Dell still publishes C4140 support/firmware guidance in 2026.
Dell states 14G iDRAC9 feature development ended 2023-06-30 and software maintenance continues until 2027-02-01.

UNKNOWN:
exact BIOS/iDRAC/GPU-board firmware state of a used unit; must be checked from Service Tag/inventory. No flashing is authorized.

## CUDA / local LLM suitability

FACT:
V100 = Volta, compute capability 7.0.
CUDA 12.x = last toolkit family for Volta.
R580 = last driver branch for Volta.

ASSESSMENT:
Multi-GPU LLM runtimes can use aggregate memory through model partitioning, but 128 GB aggregate is not one 128 GB VRAM device. KV cache, temporary buffers, quantization and runtime topology matter.

K's NVLink is favorable for GPU peer traffic. Its single PCIe Gen3 x16 host uplink may limit CPU↔GPU streaming compared with M. For GPU-resident steady-state inference this may be acceptable but must be benchmarked.

UNKNOWN:
tokens/s for project workloads.

V100 is a compute accelerator, not a modern CAD/display GPU. It can serve CUDA engineering workloads but does not replace a workstation graphics adapter for interactive CAD.

## Fact / unknown summary

- C4140 K 1U / dual CPU / 4×SXM2 NVLink2 — FACT.
- V100 32 GB NVLink supported — FACT.
- 4×V100 32GB SXM2 tested in K — VERIFIED_RESULT.
- 128 GB aggregate HBM2 — CALCULATION.
- one PCIe Gen3 x16 host path — FACT.
- internal 96-lane PCIe Gen3 switch — FACT.
- GPU↔GPU NVLink2 — FACT.
- NVSwitch — VERIFIED_RESULT: ABSENT.
- live NVLink matrix/health — UNKNOWN.
- whole-system wall power — UNKNOWN.
- GPU-only ceiling 1200 W — CALCULATION.
- exact LLM performance — UNKNOWN.
- used-unit health — UNKNOWN.

## Current market evidence, separate from technical facts

September 2026 search confirms active used/open-box C4140 supply. Listings range from roughly USD 2.5k for used four-V100 systems whose titles do not prove 32 GB capacity, to much higher explicit 4×V100-32GB configurations. Market listings prove availability only; exact GPU part numbers, K topology, firmware and health remain seller claims until acceptance evidence.

No purchase recommendation is made.

## Next engineering step

If this branch continues, create an acceptance-evidence checklist for one exact used C4140 K unit before price comparison or procurement decision.

Required candidate-unit evidence:
1. Service Tag/factory inventory.
2. exact 4× V100 SXM2 32 GB part numbers.
3. nvidia-smi -q.
4. nvidia-smi topo -m.
5. nvidia-smi nvlink --status.
6. DCGM diagnostics if available.
7. BIOS/iDRAC versions and hardware health logs.
8. PSU model/wattage.
9. fan/thermal status under load.
10. measured wall power and placement/noise constraints.
11. bounded LLM/CUDA benchmark for intended runtime.

## Source map

S01 Dell C4140 Technical Guide — official Dell.
S02 Dell C4140 Installation and Service Manual — official Dell.
S03 Dell C4140 Technical Specifications — official Dell.
S04 Dell "New NVIDIA V100 32GB GPUs Initial performance results" — official Dell.
S05 NVIDIA Tesla V100 Data Sheet — official NVIDIA.
S06 NVIDIA CUDA Toolkit/Driver/Architecture Matrix — official NVIDIA.
S07 NVIDIA Fabric Manager/NVSwitch platform documentation — official NVIDIA.
S08 Dell current 14G BIOS/iDRAC guidance — official Dell.
S09 Dell iDRAC9 lifecycle/support — official Dell.
Current eBay results were used only as market evidence.

## Task provenance

authority:
wellbeing-hq@08d7031e24b56aad27ce5f83b741637c04ec6b20
KOO__authorize-PRO-dell-c4140-config-k-research-r01__OPERATOR.md

task:
wellbeing-hq@56ce32be267cb2e496b64f3676d94b913e54f87d
KOO__PRO-dell-c4140-config-k-research-r01__PRO.md

current-writer:
wellbeing-hq@f61f1ab5288738a0f4fff7294545134042cd31ad
PRO__first-current-writer-r01.md

canonical recovery:
wellbeing-entity-bootstrap@b34dd2cda94c2f61acc59a5f066c38bd24fdae0c
entities/pro/recovery/versions/pro-recovery-r01

terminal:
PASS_PRO_DELL_C4140_CONFIGURATION_K_RESEARCH_R01
