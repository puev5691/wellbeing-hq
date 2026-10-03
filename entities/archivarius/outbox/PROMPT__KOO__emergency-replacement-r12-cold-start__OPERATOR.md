# PROMPT — emergency replacement KOO r1.2 cold-start initiation

АДРЕСАТ: НОВЫЙ КООРДИНАТОР / KOO

Emergency replacement / Initiation-required.

ОПЕРАТОР подтверждает:

PREVIOUS_KOO_R11_TECHNICALLY_UNAVAILABLE = YES

Предыдущий authoritative KOO r1.1 полностью выработан и технически не способен продолжать работу.

ОПЕРАТОР явно разрешает только emergency replacement Initiation Gate нового KOO r1.2.

Это разрешение:
- не устанавливает current-writer;
- не выполняет Writer Gate;
- не разрешает profile work;
- не разрешает replay historical PROMPT/tasks/queues;
- не разрешает Project Source/canon mutation;
- не разрешает Telegram/OpenAI/provider/runtime/host/shard mutation.

## Predecessor current writer

puev5691/wellbeing-hq:
entities/koordinator/current/KOO__replacement-current-writer-r11.md

blob:
d0e74b6a22ddd1880f725786a313d067aaace2c2

status:
WRITER_ESTABLISHED

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R11

Do NOT invent predecessor freeze/handoff if exact artifact is absent.

## External recovery lineage

BASE:

puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:
entities/koo/recovery/versions/koo-recovery-r09

DELTA:

puev5691/wellbeing-entity-bootstrap@e07047dfce0684638e2164d1712dee06ac313cfc:
entities/koo/recovery/versions/koo-recovery-r10

SUCCESSOR:

puev5691/wellbeing-entity-bootstrap@f478b936e4cba58c8a81490463541b6ecd76a4c1:
entities/koo/recovery/versions/koo-recovery-r11

EMERGENCY SUCCESSOR:

puev5691/wellbeing-entity-bootstrap@122fcd2172781cc87e2cc15afc46f715193f63db:
entities/koo/recovery/versions/koo-recovery-r12

package tree:
aee471b4388224842b1d052e6e9951eeb1090eac

composition:
5/5 PASS

## r12 exact composition

1. KOO__predecessor-current-writer-r11.md
blob:
d0e74b6a22ddd1880f725786a313d067aaace2c2

2. KOO__human-interface-contract-r02.md
blob:
fdea31034c370220dfb961993059500716ccfe20

3. KOO__emergency-recovery-delta-r12.md
blob:
4939ffadd581dd9ef49a015441420e005f64324a

4. KOO__emergency-replacement-initiation-draft-r12.md
blob:
aca5b0172d156fe96bd452a9050017ff674d968c

5. RECOVERY-MANIFEST.md
blob:
4fc6f31aaa9a1f3705bb023c6d8b4fa2536aa3cb

## Missing-state boundary

Fresh predecessor self-snapshot r1.2:
NOT_FOUND

Chat-local state after the last durable KOO action:
UNKNOWN

Disposition:
DO NOT_RECONSTRUCT
DO_NOT_REPLAY

Do not infer current task from:
- historical active queues;
- model memory;
- inbox presence;
- dispatch presence;
- activation records;
- priority lists;
- the last durable task merely because it is last.

## Last proven durable KOO action

puev5691/wellbeing-hq@5774baafa3a1b39f6064facec6d89a5acfae2361:
entities/koordinator/outbox/SIS_SECE_D1D2_publicfetch_exec_r03_prompt.md

blob:
6f2efa24959a90b3477019fdada1c2bab9deec73

Its own attempt state:
AWAITING_OPERATOR_TRANSFER

This proves only KOO materialized the task.

It does NOT prove:
- OPERATOR transfer;
- SIS receipt;
- SIS processing_started;
- SIS completion.

Fresh downstream reconciliation is required after Writer Gate.

## Mandatory Human Interface Gate

Load exact:

entities/koo/recovery/versions/koo-recovery-r12/KOO__human-interface-contract-r02.md

blob:
fdea31034c370220dfb961993059500716ccfe20

Explicitly verify H1-H8.

If any H1-H8 cannot be verified:
return HUMAN_INTERFACE_GATE_NOT_VERIFIED and STOP.

## Required Initiation Gate

Fresh-preflight wellbeing-hq and verify:

1. exact predecessor KOO r1.1 identity/status;
2. OPERATOR failure-state PREVIOUS_KOO_R11_TECHNICALLY_UNAVAILABLE = YES;
3. recovery lineage r09+r10+r11+r12;
4. r12 package composition 5/5 and exact blob identities;
5. absence of newer valid KOO current-writer;
6. absence of competing r1.2 replacement/initiation;
7. current approved Project Sources;
8. Human Interface Gate H1-H8;
9. missing self-snapshot r1.2 = NOT_FOUND;
10. chat-local predecessor tail = UNKNOWN;
11. last durable KOO action exact locator/blob;
12. no historical task/queue replay authority;
13. no superseding OPERATOR decision.

Do not merge:
- externally verified recovery state;
- fresher durable repository evidence;
- UNKNOWN chat-local state

into synthetic self-state.

## Allowed outcomes

If all required identity/integrity/currentness checks pass:

initiation_verified_waiting_writer_gate

If recovery can be read but integrity/version cannot be fully verified:

initiation_loaded_external_unverified

If required package/version/composition fails:

initiation_failed

If H1-H8 fail:

HUMAN_INTERFACE_GATE_NOT_VERIFIED

## Required result

Publish one standalone immutable initiation-result in KOO outbox containing at minimum:

instance:
emergency replacement KOO r1.2

predecessor:
KOO r1.1

PREVIOUS_KOO_R11_TECHNICALLY_UNAVAILABLE:
YES

recovery lineage:
r09 + r10 + r11 + r12

r12 package:
5/5 verified or exact blocker

fresh predecessor self-snapshot r1.2:
NOT_FOUND

chat-local predecessor tail:
UNKNOWN / DO_NOT_RECONSTRUCT / DO_NOT_REPLAY

last proven durable KOO action:
5774baafa3a1b39f6064facec6d89a5acfae2361
entities/koordinator/outbox/SIS_SECE_D1D2_publicfetch_exec_r03_prompt.md
blob 6f2efa24959a90b3477019fdada1c2bab9deec73

historical replay:
NONE

profile work:
NOT_STARTED

Writer Gate:
NOT_PERFORMED

Human Interface Gate:
H1-H8 explicit result

Perform immutable readback.

Then STOP before Writer Gate.

Do NOT create current-writer artifact in this step.
