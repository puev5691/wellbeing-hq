# KOO → RED: literary project journal implementation preparation

status: TASK
execution_mode: BOUNDED_EDITORIAL_IMPLEMENTATION_DESIGN
journal_activation_authority: no
project_source_mutation_authority: no
automation_authority: no
project_time: omitted; trusted project-time source not used

## OPERATOR decision

Decision:
`APPROVE_HUMAN_INTERFACE_CORE_V24_AND_JOURNAL_IMPLEMENTATION_PREP`

Decision record:
`entities/koordinator/current/KOO__human-interface-journal-operator-decision.md`

commit:
`550e7be8ae773f318e2b18dce8c4997313475450`

## Reviewed basis

KAN proposal:
`entities/kancelar/outbox/KAN__project-literary-journal-proposal__KOO-RED.md`
commit `dfeddadb591a87218d5d594bc6841779f369bf4f`

RED review:
`entities/redaktor/outbox/RED__human-interface-and-journal-review-r01__KAN-KOO.md`
commit `94e579cbc2abd1ba75607502311b60788fe8a81e`
verdict `PASS_RED_HUMAN_INTERFACE_AND_JOURNAL_REVIEW_R01`

## Task

Prepare one minimal implementation-design candidate for a literary project journal.

The journal must remain:
- non-authoritative;
- non-Project-Source;
- non-technical-log;
- non-transcript;
- non-per-task;
- non-automated in this task.

Design only what is needed for practical editorial use.

## Required output

Create one candidate package or one concise candidate file that defines:

1. recommended storage location/layout;
2. simplest durable journal structure;
3. minimal form of one entry;
4. how significant events are selected;
5. how material can be accumulated episodically/periodically;
6. how RED can use it later for Telegram, portal and book/history work;
7. how technical evidence is referenced without copying machine noise;
8. how direct quotes are distinguished from paraphrases;
9. privacy/publication boundary;
10. how ARH/KOO may assist without changing ownership;
11. explicit rule that journal is not source of technical truth.

Avoid:
- per-task logging;
- mandatory entry after every terminal result;
- heavy schemas;
- automatic cron/workflow;
- new Entity roles;
- Project Source activation;
- publication authority.

## Expected terminal result

Return exactly one:

`PASS_RED_LITERARY_JOURNAL_IMPLEMENTATION_CANDIDATE_READY_FOR_OPERATOR`

or

`BLOCKED_RED_LITERARY_JOURNAL_IMPLEMENTATION: <exact blocker>`

or exact FAIL.

Address result to KOO.
Stop after terminal result.
