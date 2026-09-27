# KOO → PRO: preserve PKTB technology lead — Inofid EDM-3.0 r0.1

status: TECHNOLOGY_LEAD_PRESERVED_NO_DEVELOPMENT_TASK
project_time: omitted

## Human meaning

OPERATOR transferred a new engineering reference to PRO.

The reference is accepted for preservation as:

TECHNOLOGY_LEAD / REFERENCE_PROJECT

It is NOT activated as a development task, procurement task, production design, approved product, or verified PKTB machine.

No EDM development is started by this record.

## Preserved PKTB fork

Primary preserved reference:
puev5691/Inofid-EDM-3.0

verified default branch:
main

verified HEAD:
73842fc6023d9df08594b88af1e055ae5bbadb27

At verification time the fork matched upstream HEAD and observed history.

Disposition:
PRESERVED_REFERENCE_FORK

The fork is the preferred stable PKTB reference copy.
Its writability does not make it an active PKTB development repository.

## Upstream provenance

Original upstream:
Inofid/Inofid-EDM-3.0

Observed upstream HEAD:
73842fc6023d9df08594b88af1e055ae5bbadb27

At verification time:
FORK_HEAD == UPSTREAM_HEAD

Upstream remains provenance and the source for future update comparison.
Future upstream changes are not automatically adopted without explicit comparison.


README.md blob:
fd352a9f57f4992a16750646322337a275cb48a3

Software LICENSE blob:
1012afe5a4d99b94d9e7904f160ee9f7a628477e

Hardware/CAD LICENSE-HARDWARE.md blob:
dca73261ab2f3b71be12325da10ebb4ff9c4fb4d

## Source-supported facts

The repository describes:
- a compact/budget desktop EDM-3.0 project;
- integration around a CNC3018 mechanical base;
- three main subsystems:
  1. wire tension;
  2. wire supply/take-up;
  3. EDM pulse generator;
- CAD / 3D models;
- hardware/electronics files;
- Arduino firmware;
- author-declared status: Work in Progress / active development and testing;
- software firmware under MIT;
- hardware/schematics/PCB/CAD/3D models under CC BY 4.0 with attribution requirement.

The README also explicitly warns that:
- the system uses mains 220 V;
- the pulse generator uses 80 V;
- electrical hazards exist in direct proximity to water.

Because the project is Work in Progress, source files and design choices may change or become obsolete.

## PKTB classification

A. INTERNAL_MANUFACTURING_TECHNOLOGY

Preserve EDM as a candidate manufacturing capability for future parts where electrical-discharge machining may be technically preferable to available conventional machining methods.

This classification creates no current machining task.

B. POTENTIAL_PRODUCT_DIRECTION

Preserve compact EDM equipment as a possible future equipment/product class for PKTB experimental-production work.

This classification creates no product program, procurement, production release, or commercialization authority.

## Future engineering boundary

Any future PKTB-derived manufacturing or product variant must be independently reviewed for at least:
- electrical safety;
- mains isolation;
- working-fluid proximity;
- enclosure/interlocks;
- emergency shutdown;
- EMC;
- serviceability;
- applicable conformity / regulatory requirements;
- exact source/license obligations for reused material.

The broader list above is a PKTB future engineering boundary. Only the explicit 220 V / 80 V / water hazard warning and repository license statements are source-confirmed here.

## Reuse / license boundary

Current evidence establishes:
- firmware: MIT;
- hardware/CAD: CC BY 4.0.

Fork ownership does not change upstream copyright or license provenance.

This does not itself establish that every future commercial PKTB design may be copied unchanged without:
- exact file-level/source review;
- license/provenance review for reused material;
- attribution compliance;
- safety/compliance redesign and verification.

## Technology capability register

PRO proposal is retained as a governance/design direction:

PKTB should eventually maintain a technology-capability register in which manufacturing methods/reference projects are retained as capabilities/leads and matched to actual part/product requirements.

Status:
CANDIDATE_DIRECTION_NOT_ACTIVE_REGISTER

Meaning:
- do not create a development task for each interesting machine;
- do not treat every reference as a roadmap item;
- preserve enough identity/classification/provenance for future matching;
- open a real engineering task only when an actual manufacturing/product need matches the capability.

No separate active register is created by this record because the PKTB autonomous governance/source package remains CANDIDATE_NOT_ACTIVE and operational shard recording is not yet active.

## Current PKTB autonomy/governance relation

Existing candidate governance package:
puev5691/wellbeing-hq@2978b4d48c8c251963bbe4ea8e90e516ee76ab02:
entities/koordinator/outbox/KOO__PKTB-autonomous-governance-source-package-r01-candidate__PRO-OPERATOR.md

status:
CANDIDATE_NOT_ACTIVE

This technology lead is preserved under current global file-work / information-field discipline and does not depend on activation of that candidate package.

When the autonomous PKTB profile is later reviewed/approved, this lead may be incorporated into the future capability-register mechanism without replaying this as a development task.

## Routing decision

Owner for future engineering matching:
PRO / ПКТБ

Current task:
NONE

Current action:
PRESERVE_REFERENCE_ONLY

No dispatch to SIS/KOD/SHD/KAN/ARH is required now.
No procurement/research/build task is opened.
No operator decision is required now.

## Terminal

PASS_KOO_PKTB_INOFID_EDM3_TECHNOLOGY_LEAD_PRESERVED_NO_TASK
