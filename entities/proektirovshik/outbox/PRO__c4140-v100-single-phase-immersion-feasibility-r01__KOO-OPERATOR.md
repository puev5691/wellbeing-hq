# PRO: C4140 / 4×V100 SXM2 single-phase immersion feasibility r0.1

status: ENGINEERING_FEASIBILITY_RESULT
scope: BOUNDED_ENGINEERING_FEASIBILITY_STUDY
project_time: omitted

## Human conclusion

Single-phase dielectric immersion for the Dell C4140 / 4×V100 SXM2 compute complex is technically plausible, but generic immersion practice does not prove material compatibility for this exact Dell/V100 assembly.

Architecture outcomes:
- A — broad/whole compute-system immersion: CONDITIONALLY_FEASIBLE.
- B — donor compute extraction into a purpose-built bath, with PSU/storage/network predominantly dry-side: FEASIBLE_CANDIDATE.
- C — GPU/NVLink-section-only immersion: CONDITIONALLY_FEASIBLE, with extra power/interconnect complexity and no proven advantage over B.

The strongest candidate is B because it removes the stock 1U high-speed fan requirement from the immersed compute section while avoiding unnecessary immersion of serviceable power/storage/network components.

This is not a production-ready design and not procurement authority.

## Thermal model

FACT from verified source result:
4× V100 SXM2 at 300 W each = 1200 W GPU ceiling.

ASSUMPTION/CALCULATION:
A preliminary total compute thermal design envelope of roughly 1.5–1.8 kW is reasonable for feasibility only after adding CPUs, memory, PCIe switching and board losses. Actual whole-system power remains UNKNOWN until measured on an exact configuration.

DESIGN_CANDIDATE:
Heat-rejection equipment in the approximate 2.5–3 kW class would provide engineering margin over the preliminary compute envelope. This is not selected equipment.

Illustrative flow calculation at 2 kW, assuming single-phase dielectric fluid specific heat near 2 kJ/(kg·K) and density near 0.8–0.9 kg/L:
- ΔT 10 K: about 0.10 kg/s, roughly 6–7.5 L/min depending on density.
- ΔT 5 K: about 0.20 kg/s, roughly 12–15 L/min.

These are sizing illustrations only. Exact flow depends on selected fluid properties, local component heat transfer, pressure drop and allowed component temperatures.

## Compatibility map

V100 SXM2 modules — CONDITIONALLY_FEASIBLE / UNKNOWN long-term exact-fluid compatibility.
NVLink board/carrier/interposer — CONDITIONALLY_FEASIBLE / exact materials and fluid compatibility UNKNOWN.
System motherboard/CPU/RAM/PCIe switch — CONDITIONALLY_FEASIBLE; electronics are plausible immersion candidates but exact connectors, plastics, labels, adhesives and TIM must be checked.
Connectors/cabling — UNKNOWN until exact materials + fluid vendor compatibility evidence.
Thermal interface materials — UNKNOWN; swelling/leaching/softening risk must be checked.
Fans — should not be relied upon submerged; candidate architecture removes/avoids their cooling function. Firmware reaction to absent/stalled fans is UNKNOWN.
PSUs — dry-side preferred candidate. Whole-PSU immersion not justified by current evidence.
Storage/BOSS/SSDs — dry-side preferred; no benefit established from immersion.
Network/management interfaces — dry-side termination preferred where practical.
Labels/adhesives/elastomers/plastics — UNKNOWN and fluid-specific.

## Noise / heat rejection

FACT:
stock C4140 uses datacenter-class forced-air cooling and eight fans in dual-CPU configuration.

HYPOTHESIS supported by immersion architecture:
removing the need for stock 1U airflow can eliminate the dominant server fan noise.

Remaining acoustic sources:
- circulation pump;
- dry-cooler/radiator fans;
- any dry-side PSU fans;
- auxiliary equipment.

DESIGN_CANDIDATE:
pump and heat rejection can be physically separated from the occupied workspace; large low-speed fans or an externally located dry cooler can reduce human-adjacent noise.

Heat is not removed by immersion itself; approximately the same electrical power ultimately becomes heat and must be rejected elsewhere.

## Electrical / fire / material boundary

Required fluid properties before design:
- documented dielectric use for electronics immersion;
- flash/fire behavior suitable for intended installation;
- viscosity and thermal-property data over operating range;
- material-compatibility guidance;
- aging/oxidation/moisture handling guidance;
- vendor guidance on connectors, elastomers, plastics and TIM where available.

Grounding/protective-earth requirements do not disappear because electronics are immersed.

Leak/spill containment, fluid handling, fire classification, emergency isolation and maintenance procedures remain required engineering subjects.

No physical experiment is justified from generic immersion compatibility alone.

## Serviceability

Whole-system immersion increases cleaning/draining/handling burden and contaminates otherwise dry-replaceable components.

Donor-compute architecture improves service boundary:
immersed compute assembly + dry PSU/storage/network.

UNKNOWN:
long-term service effects on used Dell connectors, board labels, thermal pads, cable jackets and replacement workflow for exact selected fluid.

## Candidate block architecture

Dry side:
AC input
→ PSU(s)
→ storage / BOSS
→ network / management termination
→ protected power/data penetrations

Immersion bath:
C4140 donor motherboard / CPU / RAM
→ PCIe switch / NVLink board
→ 4× V100 SXM2

Thermal loop:
bath
→ low-noise circulation pump
→ liquid/liquid heat exchanger or liquid/air radiator
→ external/remote dry cooler where useful
→ bath

## Risk / UNKNOWN table

- exact immersion fluid: UNKNOWN.
- V100/Dell board material compatibility with exact fluid: UNKNOWN.
- connector/cable/TIM/plastic/elastomer compatibility: UNKNOWN.
- iDRAC/BIOS behavior when stock fans are removed/stalled: UNKNOWN.
- thermal behavior of low-power components formerly dependent on directed airflow: UNKNOWN.
- actual total heat load: UNKNOWN until measurement.
- exact hydraulic pressure drop/flow distribution: UNKNOWN until mechanical design.
- long-term fluid aging/contamination: fluid-specific UNKNOWN.
- whole-system immersion: CONDITIONALLY_FEASIBLE.
- donor compute extraction: FEASIBLE_CANDIDATE.
- GPU-only immersion: CONDITIONALLY_FEASIBLE.
- production readiness: NO.

## Evidence required before any physical design/experiment

1. Select candidate industrial single-phase immersion fluid families.
2. Obtain official fluid technical/safety data.
3. Obtain vendor material-compatibility evidence for relevant PCB materials, connector plastics, cable jackets, elastomers, adhesives and TIM.
4. Identify exact C4140 donor components/part numbers.
5. Establish whether iDRAC/BIOS permits operation without stock fan feedback or requires a controlled workaround; no workaround is authorized here.
6. Obtain exact power/thermal measurements from a representative C4140 K configuration or conservative component inventory.
7. Establish component maximum temperatures and sensing coverage.
8. Define electrical isolation, PE grounding, containment, leak/spill and fire boundary.
9. Only after those evidence gaps close, size bath, pump, heat exchanger and heat rejection system.

## Exact next engineering step candidate

Build an evidence-based compatibility matrix for 2–3 industrial single-phase immersion-fluid families against the exact C4140/V100 component/material set.

This step is NOT started or authorized by this result.

## Provenance

Source task:
puev5691/wellbeing-hq@291f332912637398ee4d72c34149867857876126:
entities/koordinator/outbox/KOO__PRO-c4140-v100-single-phase-immersion-feasibility-r01__PRO.md
blob b881b404f6d5f82c7ee9b5be1c48de9045690d3f

Authority:
puev5691/wellbeing-hq@7b40dbf9cac602089ef44d26d2823e267af688ab:
entities/koordinator/outbox/KOO__authorize-PRO-c4140-v100-single-phase-immersion-feasibility-r01__OPERATOR.md
blob a3020e4fd85b79e3eb8e6dc56f359be6c870f238

Verified source engineering result:
puev5691/wellbeing-hq@dd4fa82d039fa0f57706b80442cc34f48dd4f896:
entities/proektirovshik/outbox/PRO__dell-c4140-configuration-k-research-r01__KOO-OPERATOR.md
blob 17f46b95242fae413ea74db1cae585c0e4fc541b

terminal:
PASS_PRO_C4140_V100_SINGLE_PHASE_IMMERSION_FEASIBILITY_R01
