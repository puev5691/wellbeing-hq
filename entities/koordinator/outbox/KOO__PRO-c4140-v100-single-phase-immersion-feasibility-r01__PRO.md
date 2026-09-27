# KOO → ПРОЕКТИРОВЩИК / PRO: C4140 / 4xV100 single-phase immersion feasibility r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: ПРОЕКТИРОВЩИК / PRO
scope: BOUNDED_ENGINEERING_FEASIBILITY_STUDY
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@7b40dbf9cac602089ef44d26d2823e267af688ab:
entities/koordinator/outbox/KOO__authorize-PRO-c4140-v100-single-phase-immersion-feasibility-r01__OPERATOR.md

Current writer:
puev5691/wellbeing-hq@f61f1ab5288738a0f4fff7294545134042cd31ad:
entities/proektirovshik/current/PRO__first-current-writer-r01.md
blob 0b2bf27d643cc28e7350913b5da89bf846d1eae0

Source engineering result:
puev5691/wellbeing-hq@dd4fa82d039fa0f57706b80442cc34f48dd4f896:
entities/proektirovshik/outbox/PRO__dell-c4140-configuration-k-research-r01__KOO-OPERATOR.md
blob 17f46b95242fae413ea74db1cae585c0e4fc541b

New design lead classification:
HYPOTHESIS / DESIGN_CANDIDATE

Concept:
C4140 compute hardware / 4x V100 SXM2
→ dielectric immersion bath
→ circulation
→ heat exchanger
→ large low-noise or remotely located heat rejection system.

Potential architectural consequence:
use C4140 as donor compute architecture rather than preserving the stock 1U air-cooled chassis.

## Required feasibility questions

1. Boundary of immersion
- Which exact compute components are candidates for immersion?
- What must remain dry/non-immersed?
- Is whole-system immersion technically plausible, or is donor extraction more realistic?

2. Material/component compatibility
- V100 SXM2 modules;
- NVLink board/interposer/carrier;
- system board/connectors/cabling;
- PSU strategy;
- storage/network devices;
- plastics/elastomers/labels/adhesives;
- fans and moving parts;
- serviceability implications.

3. Thermal feasibility
- heat load from 4x300 W GPUs plus CPUs/memory/switching;
- approximate coolant flow / heat exchanger duty;
- fluid-temperature and component-temperature constraints;
- whether single-phase immersion can plausibly remove the expected load without datacenter fan noise.

4. Electrical/safety boundary
- dielectric-fluid requirements;
- leakage/fire/material hazards;
- grounding/isolation/PSU considerations;
- what evidence would be required before any physical experiment.

5. Mechanical architecture
Compare at least:
A. whole C4140 internals immersed with major dry-side support retained;
B. donor compute assembly removed from 1U chassis into custom immersion tank;
C. hybrid approach where only GPU/NVLink compute section is immersed, if technically plausible.

6. Noise/heat rejection
- what noise sources disappear;
- which pumps/fans remain;
- radiator/dry-cooler/external heat rejection options;
- possibility of moving heat rejection outside occupied space.

7. Serviceability/reliability
- maintenance burden;
- fluid contamination/handling;
- connector access;
- replacement workflow;
- leak/spill risk;
- long-term unknowns for ex-datacenter hardware.

8. Evidence and UNKNOWN
For every important point distinguish:
FACT / CALCULATION / ASSUMPTION / HYPOTHESIS / UNKNOWN / VERIFIED_RESULT.

Do not infer compatibility merely because a generic immersion system exists.

## Sources

Priority:
1. Dell official C4140 documentation;
2. NVIDIA official V100/SXM2 documentation;
3. reputable immersion-cooling vendor/material compatibility documentation;
4. standards/manufacturer guidance for dielectric fluids and electrical equipment;
5. independent technical evidence only to close gaps.

Historical chat content is only candidate lead.

## Result

Produce one standalone feasibility artifact for KOO/OPERATOR:
- human conclusion;
- feasible / infeasible / conditionally feasible verdict by architecture option;
- heat-load and thermal calculations;
- component compatibility map;
- risk/UNKNOWN table;
- candidate system block diagram in text;
- evidence needed before any physical design/experiment;
- exact next engineering step if warranted.

Do NOT:
- buy;
- disassemble;
- immerse;
- fabricate;
- deploy;
- mutate hosts;
- approve procurement;
- claim production-ready design.

Expected terminal:
PASS_PRO_C4140_V100_SINGLE_PHASE_IMMERSION_FEASIBILITY_R01

or exact BLOCKED_* / FAIL_*.

After immutable result + readback + return KOO/OPERATOR, STOP.
