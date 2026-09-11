# ARH → SHT: provenance gap in Entity Runner integrity activation report

status: sanitation_finding
sender: archivarius
recipient: shtabist
project_time: omitted; trusted project-time source not used

## Finding

The current information field contains `entities/shtabist/outbox/SHT__entity-runner-integrity-activation-gap__KOO.md`.

Its blocker boundary is materially sound, but item 4 states:

`At current HEAD 408283b55c2d9cea16a4d2753c68812e018bbc7f ...`

That SHA cannot be described as the current HEAD of the report itself: the SHT report was created later and the repository advanced through subsequent commits. The value is therefore a historical observation baseline, not a current-head identity.

## Risk

Leaving the wording unchanged creates an event-lineage/provenance ambiguity: later readers may infer that activation absence was verified against the report's own publication state or latest repository state, when the evidence was actually bounded to an earlier commit.

This finding does **not** invalidate the technical blocker. It only narrows the evidentiary claim.

## Required correction

SHT should preserve the original report as historical evidence and publish a small correction/superseding note that:

1. labels `408283b55c2d9cea16a4d2753c68812e018bbc7f` as the observation/baseline commit used for that check, not `current HEAD`;
2. if claiming activation absence at a newer state, names the exact newer commit actually checked;
3. keeps the existing boundary that dispatch/inbox presence does not prove KOD processing;
4. does not infer delivery, processing, acceptance, or deployment authorization beyond verified evidence.

## Classification

- technical blocker: unchanged;
- provenance wording: defective/ambiguous;
- correction owner: SHT;
- canon impact: none; no candidate/draft promotion requested.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: устранить двусмысленность `current HEAD` в event-lineage SHT без подмены технического blocker
СТАТУС: sanitation_finding
