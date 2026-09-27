# KOO: human-readable Entity response pattern r0.1

status: OPERATOR_APPROVED_RESPONSE_PATTERN
project_time: omitted

## Purpose

This document records the OPERATOR-approved human-facing response pattern for all project Entities.

It is a communication/output pattern only.
It does not replace Project Sources, role definitions, recovery, task, file, routing, approval, delivery or authority canons.

## Core rule

Chat is the human interface.

Technical detail belongs in the project information field:
- GitHub now;
- operational shards / memory layers where separately approved in the future.

Do not dump internal technical bookkeeping into the human chat unless the OPERATOR needs it for a decision or verification.

## Default terminal response structure

A normal Entity result to OPERATOR should contain only:

1. Human meaning
   - what happened;
   - what it means;
   - what is blocked or complete;
   - what happens next.

2. Next recipient
   - exact Entity name/callsign.

3. One complete copy-paste PROMPT block for that Entity
   - enough exact locator/version/authority information for Resume-First;
   - no requirement for OPERATOR to assemble instructions from multiple places;
   - do not repeat unnecessary project history already available by exact locator.

4. One exact OPERATOR action
   - usually: send the block to the named Entity;
   - or: approve/reject one exact decision;
   - or: provide one specific missing fact;
   - or: do nothing.

## Technical-detail boundary

Keep out of the human-facing explanation by default:
- long commit/blob/tree inventories;
- package member lists;
- full verification matrices;
- internal counters/logs;
- repetitive PASS tables;
- detailed routing mechanics;
- implementation trace;
- machine-only audit detail.

These remain in the project information field and are referenced by locator when needed.

Surface technical identifiers in chat only when:
- the OPERATOR must copy them into the next Entity prompt;
- they are needed to verify a decision;
- they are the subject of the decision itself;
- a blocker cannot be understood without them.

## Example

Human meaning:

The architecture review passed except for one blocked pilot lineage. The EOM pilot cannot run because it causally overlaps unauthorized memory-layering attempt 3. The independent File/Artifact Service correction remains allowed and is the next causal step.

Next recipient:

KOD / КОДЕР

Copy-paste prompt:

```text
Resume-First.

Take the already prepared exact task:

<exact task locator>

Use the exact authority and inputs referenced there.

Perform only the bounded correction scope.
Do not execute the blocked pilot or any unrelated mutation.

Return the immutable result to KOO and STOP.
```

OPERATOR action:

Send this block to KOD.

## Additional rule

If there is no next Entity action, do not manufacture a prompt.
End with the one real OPERATOR action, including "nothing to do" when that is actually correct.

## Status

This is the OPERATOR-approved response pattern for all Entities.
It is not itself a Project Source/canon mutation.

terminal:
PASS_KOO_HUMAN_READABLE_ENTITY_RESPONSE_PATTERN_R01_RECORDED
