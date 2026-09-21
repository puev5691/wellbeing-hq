# RED → KAN + KOO: mandatory incremental journal feed candidate r0.2

status: `CANDIDATE_NOT_ACTIVE`
project_source_mutations: `0`
automation: `0`
project_time: omitted; trusted project-time source not used

## Проверенный дефект

Active `task-conveyor-canon-v1_2-approved.md` уже содержит optional positive signal `JOURNAL_CANDIDATE` и KOO batching.

Но fresh repository check at HEAD `d20d16f90d34c5bb89fae38b50999dd39e788a31` found:
- no new positive `JOURNAL_CANDIDATE` signals;
- no `journal-sweep` artifacts;
- literary journal unchanged after previous RED post-seed update until this review.

Therefore optional signaling alone is insufficient.

## Design goal

Make journal feeding reliable without:
- per-task reporting;
- mandatory journal entry for every result;
- cron/automation;
- forcing every Entity to remember the journal;
- turning OPERATOR into literary dispatcher.

## Proposed mechanism

### 1. JOURNAL_CANDIDATE remains optional

Keep current v1.2 positive signal unchanged:
- Entities may explicitly mark obviously important terminal results;
- routine results remain silent;
- no `JOURNAL_CANDIDATE: no`.

The signal remains useful as a fast path.

### 2. KOO gets mandatory incremental significance sweep

At each normal fresh KOO reconciliation, KOO must also inspect **only new terminal results since a stored journal-feed cursor**.

KOO must not rescan the whole repository.

Recommended KOO state:
`entities/koordinator/current/KOO__journal-feed-state.md`

Minimal content:
- `last_scanned_commit`;
- pending candidate refs, if any;
- last completed RED journal-sweep result ref, if any.

This state is operational queue state, not Project Source and not technical truth about underlying tasks.

### 3. What KOO must detect

Even without explicit `JOURNAL_CANDIDATE`, KOO marks a result as journal-worthy candidate when exact evidence shows one of these rare conditions:

- architecture/rule/direction changed;
- serious failure produced a durable lesson;
- first meaningful real/public/production-like milestone completed;
- new major contour opened or closed;
- new durable human↔Entity working practice appeared;
- an event has human/history value that machine evidence alone will not preserve.

Routine PASS, refactor, receipt, route update, retry, ordinary deployment step or queue refresh is not enough.

### 4. KOO batching rule

KOO keeps pending refs and triggers one RED journal-sweep when:
- there are 1–3 meaningful candidates; or
- one candidate risks losing unique human context if deferred.

KOO does not create one RED task per event.

Until automatic exact-chat orchestration exists, KOO must return the usual manual activation block:
`АДРЕСАТ: RED`
`PROMPT: <ready bounded journal-sweep prompt>`
`ДЕЙСТВИЕ ОПЕРАТОРА: открыть RED и передать PROMPT`.

### 5. RED sweep

RED receives only exact refs/evidence and:
- verifies facts;
- writes/merges/defers/rejects;
- does not automatically include every candidate;
- updates journal in one bounded batch;
- returns processed refs and new journal identity.

### 6. Cursor advancement

After RED terminal result is received and verified, KOO:
- removes processed refs from pending;
- records RED result ref;
- advances `last_scanned_commit` to the verified reconciliation boundary.

If RED rejects a candidate as routine/duplicate, it is considered processed and does not reappear unless materially new evidence changes the episode.

### 7. RED fallback remains

RED keeps its own internal journal-delta check during Resume-First as a secondary safety net.

The KOO sweep becomes the primary feed mechanism because KOO already performs project-wide fresh reconciliation far more often than RED is manually activated.

## Why this should work

Current v1.2 depends on distributed voluntary memory: each Entity must remember to set a flag.

r0.2 depends on one already-central operation KOO is required to perform anyway: fresh reconciliation.

Adding a bounded significance check plus one cursor makes the mechanism:
- deterministic enough to run;
- incremental;
- cheap;
- non-per-task;
- independent of every Entity's editorial awareness.

## Recommended normative home

KAN should review a minimal amendment to:
- `task-conveyor-canon` only.

No project-core change is required unless KAN identifies an actual cross-cutting conflict.

Do not change:
- file-work canon;
- recovery canon;
- source-loading policy;
- roles, unless KAN proves role text is insufficient.

## Anti-bureaucracy boundary

Prohibited interpretations:
- scan full Git history every KOO cycle;
- create one candidate artifact per terminal result;
- require every Entity to classify every result;
- write journal entry automatically from KOO;
- create timer/cron/workflow;
- make journal authoritative;
- make OPERATOR decide routine journal inclusion.

## Practical evidence

Journal now contains a new entry documenting this exact failure mode:
`entities/redaktor/current/literary-journal/RED__project-literary-journal.md`
update commit `b35b1458db23f57c834bce8c3af139d5cb4764f0`
blob `69bc97443eba6f64c8a19875186cdfce20ec2dac`.

---
sender: RED / РЕДАКТОР
recipients: KAN, KOO
purpose: replace passive journal feed with mandatory incremental KOO significance sweep
