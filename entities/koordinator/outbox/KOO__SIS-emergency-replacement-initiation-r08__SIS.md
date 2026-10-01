# KOO -> NEW SIS: emergency replacement cold-start initiation r0.8

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First is NOT available because this is a NEW replacement instance.

Perform emergency replacement cold-start initiation only.

## Explicit OPERATOR authority

OPERATOR has explicitly reported:

PREVIOUS_SIS_R07_TECHNICALLY_UNAVAILABLE = YES

Reason:
the previous SIS chat instance is exhausted/ended and cannot reliably continue or produce a fresh authoritative self-snapshot/handoff.

OPERATOR authorizes ONLY:
SIS emergency replacement cold-start initiation r0.8.

This authority does NOT:
- establish current-writer;
- authorize Writer Gate;
- resume any historical task;
- replay any historical PROMPT;
- authorize Telegram install/live;
- authorize host/DB/schema mutation;
- authorize service start;
- authorize Telegram/OpenAI calls.

## Exact authoritative predecessor writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

Predecessor disposition for this emergency initiation:
TECHNICALLY_UNAVAILABLE

Do not create a synthetic predecessor self-freeze.

## Last externally verified SIS recovery

External recovery delta:

puev5691/wellbeing-entity-bootstrap@faa13798292dd93617ef8d4c0e5e47ebaf5ce809:
entities/sis/recovery/versions/sis-planned-r07

RECOVERY-MANIFEST.md blob:
f206d6b66dd1697cea5566257a10dc8143c541b2

sha256sums.txt blob:
fc5aacd1d288e94def96d3ec4fe35931e520f5f2

Base recovery:

puev5691/wellbeing-entity-bootstrap@6ffb05a0a2fb018717ddd6e996d4ec1c7a41ef7:
entities/sis/recovery/versions/sis-emergency-r06

ARH preservation/readback result:

puev5691/wellbeing-hq@0061574c3aa4fcc3eeba341e63b9cc6c972dd9a3:
entities/archivarius/outbox/ARH__SIS-planned-replacement-r07-result__KOO-OPERATOR.md

blob:
df944eb4e2b7bf00935e7134c87e36811cd018c8

terminal:
PASS_ARH_SIS_PLANNED_REPLACEMENT_R07_EXTERNALLY_PRESERVED

Important:
this externally verified recovery predates later SIS r0.7 Telegram work.
Do not reconstruct later state into the recovery package.
Treat post-recovery GitHub evidence as a separate delta during initiation reconciliation.

## Approved Project Sources

Load and verify current approved common source-set before concluding initiation:

- Project Core v2.5
  blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33

- Entity Roles v2.4
  blob 1772339cb74dae8550bfbd2e33401c34a929e911

- Source Loading Policy v2.2
  blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf

- Recovery Canon v1.6
  blob 233117e1c9509d730e1f5ec532b1cabe3f786609

- File Work Canon v2.4
  blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2

- Task Conveyor Canon v1.2
  blob df7896d867eeeffff506319538fedad938856686

Fresh-check whether these remain current/compatible.
Do not assume supersession absence from this prompt alone.

## Latest verified post-recovery Telegram evidence

The latest exact verified SIS terminal before the still-open readiness task is:

puev5691/wellbeing-hq@29e3cfca5c5bf6231b0d05d36986404820db231c:
entities/sisadmin/outbox/SIS__telegram-conversation-root-r01-I1-rereview-result__KOO.md

blob:
7a92c9d8779ce6f3cdd4d0b199023abf9cbdbd1a

terminal:
PASS_SIS_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_REREVIEW

This evidence may be used as fresh GitHub delta evidence only.
It is not retroactively part of recovery r0.7.

## Last exact task issued to previous SIS

puev5691/wellbeing-hq@5f5902b71ad7509a4d11c7f6812f0ae5583a7542:
entities/koordinator/outbox/KOO__telegram-conversation-root-r01-install-verify-readiness__SIS.md

blob:
3f11c244f0d9b17964471e57131453ada879dc3e

Current KOO reconciliation found:
NO terminal result for this task in GitHub at emergency replacement time.

Therefore classify:

TASK_EXECUTION_STATUS:
UNKNOWN

TASK_REPLAY:
FORBIDDEN

Do NOT:
- assume completed;
- assume failed;
- continue from remembered chat text;
- execute the task during initiation.

If a terminal result appears during fresh initiation preflight:
record exact locator/blob and classify it as new delta evidence,
but still do not execute a next profile step during initiation.

## Initiation procedure

1. Fresh GitHub preflight of puev5691/wellbeing-hq.

2. Verify:
- exact predecessor current-writer identity;
- no newer SIS current-writer;
- no competing replacement;
- no superseding freeze/handoff/initiation;
- no cancelling OPERATOR decision;
- exact recovery locator/version;
- ARH preservation/readback result;
- approved source-set;
- post-recovery SIS delta;
- latest task/result state.

3. Read/verify external recovery r0.7 composition and checksums.

4. Preserve stale boundary:
recovery r0.7 is last externally verified recovery,
not a claim that it contains later Telegram work.

5. Build the new instance's initiation state from:
- verified recovery r0.7;
- exact current project sources;
- exact GitHub delta evidence;
without reconstructing missing self-state.

6. Explicitly classify:
- confirmed/current evidence;
- historical evidence;
- UNKNOWN pending task/result state;
- forbidden historical PROMPT replay.

7. Do NOT perform profile work.

8. Do NOT establish current-writer.

## Required output

Create one immutable initiation result under SIS outbox.

Required status on success:

initiation_verified_waiting_writer_gate

Required terminal:

PASS_SIS_EMERGENCY_REPLACEMENT_INITIATION_R08_WAITING_WRITER_GATE

The result must include:
- exact predecessor writer;
- PREVIOUS_SIS_R07_TECHNICALLY_UNAVAILABLE=YES;
- exact recovery r0.7/base identity and integrity;
- source-set verification;
- exact post-recovery delta boundary;
- exact latest known terminal;
- exact status of readiness task 5f5902...;
- explicit historical replay prohibition;
- profile_work=NOT_STARTED;
- current_writer=NOT_ESTABLISHED_FOR_R08;
- next gate=SEPARATE_OPERATOR_WRITER_GATE_DECISION_REQUIRED.

If recovery/version/source/supersession conflict exists:
return exact BLOCKED_/FAIL_ and STOP.

## Hard boundary

No:
- Writer Gate;
- authoritative SIS current-state mutation beyond own initiation result;
- Telegram profile task execution;
- install/migration;
- live host mutation;
- service start;
- Telegram/OpenAI call;
- credential mutation;
- historical task replay.

After initiation result:
STOP.
