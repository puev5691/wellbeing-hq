# KOO → RED: activate literary project journal r0.1

status: TASK
execution_mode: BOUNDED_EDITORIAL_ACTIVATION
automation_authority: no
project_source_authority: no
publication_authority: no
project_time: omitted; trusted project-time source not used

## OPERATOR authority

Decision:
`ACTIVATE_RED_LITERARY_JOURNAL_R01`

Decision record:
`entities/koordinator/current/KOO__literary-journal-r01-operator-decision.md`

decision commit:
`37494f65f859fda1c0bca95c30458feea2046644`.

## Exact implementation basis

RED candidate:
`entities/redaktor/outbox/RED__literary-journal-implementation-candidate-r01__KOO.md`

commit:
`cef6220d4225a0892cdc1e25438b5d793d7eec37`

blob:
`1f51413b592ea44329d2f93e1d9dfde3819e9875`

verdict:
`PASS_RED_LITERARY_JOURNAL_IMPLEMENTATION_CANDIDATE_READY_FOR_OPERATOR`.

KAN proposal:
`entities/kancelar/outbox/KAN__project-literary-journal-proposal__KOO-RED.md`
commit `dfeddadb591a87218d5d594bc6841779f369bf4f`.

## Required action

Perform one bounded activation step only.

1. Create:
`entities/redaktor/current/literary-journal/`

2. Create one main journal:
`entities/redaktor/current/literary-journal/RED__project-literary-journal.md`

3. At the top state clearly:
- purpose: human/editorial memory of significant project events;
- not technical log;
- not full transcript;
- not authoritative current-state;
- not Project Source;
- internal by default;
- publication requires separate editorial/public authority;
- direct quote requires verifiable exact source;
- paraphrase must not be presented as verbatim quote.

4. Seed only a small number of already verifiable significant episodes if exact evidence is readily available.
Do not create filler entries merely to make the journal look populated.

Suitable seed candidates may include:
- adoption of human-facing interface rule;
- successful bounded mazhor shard gateway acceptance;
- the OPERATOR-interface lesson that humans must not be used as manual file/API couriers;
but include only what can be supported by exact available evidence.

5. Each entry should remain readable and may use a compact structure:
- what happened;
- why it mattered;
- human detail;
- consequence;
- evidence only when useful.

Do not force all headings if a natural paragraph is better.

6. Do not copy hashes/paths/route history into prose unless needed to support the episode.
Technical evidence belongs primarily in the information field.

7. Perform exact readback of the created journal artifact.

8. Record current journal locator/identity so the next RED preservation/recovery snapshot can retain continuity.

## Explicitly forbidden

- automation;
- cron/workflow;
- mandatory entry after each task;
- Project Source mutation;
- new role creation;
- publication to Telegram/portal/book;
- use of journal as technical authority;
- full transcript ingestion;
- secret/credential inclusion;
- invented quotations;
- reconstruction of unavailable dialogue as verbatim speech.

## Terminal criterion

Return exactly one:

`PASS_RED_LITERARY_JOURNAL_R01_ACTIVATED`

or

`BLOCKED_RED_LITERARY_JOURNAL_R01_ACTIVATION: <exact blocker>`

or exact FAIL.

Terminal result should state in human language:
- whether the journal was created;
- whether seed entries were added;
- whether it remains internal/non-authoritative/non-automated;
- whether any further OPERATOR action is required.

Address terminal result to KOO.
Stop after terminal result.
