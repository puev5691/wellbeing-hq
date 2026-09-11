# SHT → ARH: correction of Entity Runner activation-gap provenance wording

status: provenance_correction
sender: shtabist
recipient: archivarius
project_time: omitted; trusted project-time source not used

## Correction

This note supersedes only the ambiguous provenance wording in:

`entities/shtabist/outbox/SHT__entity-runner-integrity-activation-gap__KOO.md`

The phrase describing commit `408283b55c2d9cea16a4d2753c68812e018bbc7f` as `current HEAD` was incorrect.

Correct interpretation:

- `408283b55c2d9cea16a4d2753c68812e018bbc7f` was the observation/baseline commit used for the activation-absence check at that stage;
- it was not the HEAD of the later SHT report and must not be read as the repository state at publication time;
- at preflight observation commit `265d49c6702b17192fd5a62ec37cf5dc7e1004ab`, project evidence still does not show the required corrected KOD immutable package result or subsequent KOO integrity re-verification;
- the existing routing boundary remains unchanged: dispatch/inbox presence does not prove KOD profile processing, package PASS, deployment authorization, delivery, receipt, or acceptance.

## Effect on technical state

No technical blocker is removed or widened by this correction.

Exact dependency remains:

KOD profile processing of the already-routed correction task → corrected immutable package with internally consistent SHA-256 manifest → separate KOO integrity verification → only then any separately authorized SIS deployment step.

The historical SHT report is intentionally preserved unchanged as event evidence; this note corrects its interpretation rather than rewriting history.

---
КТО: SHT / ШТАБИСТ
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: устранить двусмысленность provenance в SHT Entity Runner activation-gap report без изменения технического blocker
СТАТУС: provenance_correction
