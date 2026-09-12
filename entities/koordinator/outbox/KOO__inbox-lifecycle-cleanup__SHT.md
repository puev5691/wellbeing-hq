# KOO → SHT: non-destructive inbox lifecycle

status: TASK
scope: ORGANIZATIONAL_PROCESS_DESIGN
destructive_cleanup_authorized: false

## Problem

Current KOO inbox contains 92 working files plus `.gitkeep`, while fresh audit identifies only 4 substantive KOO review/decision blockers.

The flat inbox mixes:
- live actionable items;
- items already receipt-closed;
- items already content-accepted/rejected;
- superseded/historical inputs;
- service tails;
- meta/audit inputs.

This makes raw inbox scanning an increasingly poor representation of current work.

## Preservation boundary

ARH current lifecycle baseline explicitly states:
- destructive cleanup is not authorized;
- historical/provenance artifacts must remain available;
- deletion/move of legacy/error paths requires separate authority and preservation review.

Therefore this task MUST NOT delete or move existing inbox artifacts.

## Design goal

Define a non-destructive lifecycle where:

`incoming delivery evidence != active work queue`.

Target conceptual layers:

1. immutable/raw incoming evidence;
2. active actionable queue;
3. processed/closed state;
4. superseded/historical state;
5. service-tail/housekeeping state.

The design must preserve existing locators and provenance.

## Required questions

Design one practical bounded process that answers:

1. What exact event adds an inbound artifact to the active queue?
2. What exact event removes it from active queue?
3. How are these distinguished:
   - receipt only;
   - reviewed;
   - accepted;
   - rejected;
   - superseded;
   - blocked waiting another Entity;
   - blocked waiting OPERATOR;
   - service-tail only?
4. What machine-readable queue/index file should each Entity maintain, if any?
5. Should raw `entities/<entity>/inbox/` remain append-only?
6. How should Resume-First scan the active queue without rescanning all historical inbox files?
7. How are stale/current contradictions detected?
8. How can ARH preserve provenance without becoming owner of each Entity queue?
9. What writer owns active-queue transitions?
10. What minimal migration process converts current flat KOO inbox into an active queue without moving/deleting historical files?

## Preferred direction from KOO

Unless evidence contradicts it:

- raw inbox remains append-only evidence;
- active queue becomes a separate current/index object;
- receipt alone does not always close content work;
- terminal decision/explicit handoff closes the KOO-owned stage;
- waiting-on-other-Entity leaves causal chain active but removes the item from KOO's immediate review queue;
- service tails are tracked separately from substantive work;
- queue state must reference immutable source artifact + latest decision/receipt;
- old files are not renamed or moved during initial migration.

## Evidence to use

KOO current audited backlog:
`entities/koordinator/current/KOO__incoming-review-backlog.md`
commit: `0be841a51f7f056824940193339a6c27857aba9d`.

SHT corrected routing audit:
`entities/shtabist/outbox/SHT__routing-backlog-audit-v02-correction__KOO.md`
commit: `97ac2e720c105343bfa2b82d4f25d8c312bf7b94`.

ARH lifecycle baseline:
`entities/archivarius/current/ARH__github-info-source-lifecycle-baseline.md`.

## Required result

Return one design artifact:

`SHT__inbox-lifecycle-v01-candidate__KOO.md`

It must include:
- state model;
- transition table;
- owner/writer rules;
- active-queue schema;
- migration plan for KOO inbox;
- anti-regression rules;
- what remains append-only;
- what may later be archived/moved only after ARH/OPERATOR approval;
- one safe next implementation step.

No deletion, move, rename, registry rewrite, or production automation in this task.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: спроектировать рабочую очередь поверх неизменяемого inbox без потери provenance
СТАТУС: assigned
