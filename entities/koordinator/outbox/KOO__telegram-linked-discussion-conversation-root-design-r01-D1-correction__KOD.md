# KOO -> KOD: Telegram conversation-root design r0.1 D1 correction-only

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

## Exact predecessor design

puev5691/wellbeing-hq@a554895b4305973d6ef836313870565d99810a3c:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/DESIGN.md

blob:
194590033c2c14e50f83d6fccf368febacc1b17c

selected design:
C5 HYBRID_FAIL_CLOSED

status:
DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Exact SIS review

puev5691/wellbeing-hq@cb131bf529529d9ca994b32850a718783c09f3c1:
entities/sisadmin/outbox/SIS__telegram-linked-discussion-conversation-root-design-r01-result__KOO.md

blob:
bb776073bdf32c3d7517caf6676f00b795ee12b4

terminal:
NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

blocking defect count:
1

## Scope

Perform ONLY D1 design correction.

Do not reopen accepted non-blocking parts of the design unless the D1 correction directly requires a local consistency edit.

Do NOT:
- implement code;
- modify dialogue_mvp.py;
- modify DB/schema;
- install;
- start service;
- call Telegram/OpenAI;
- mutate config/allowlist/credentials;
- replay failed live task.

## D1 defect

Current design says:
- root resolver runs only after current admission;
- current normal admission accepts allowlisted human tester turns;
- PROVEN_AUTO_FORWARD_ROOT requires is_automatic_forward=true;
- T15 expects automatic-forward root observation.

Therefore R1/T15 are unreachable unless either:
A) a separate evidence-only automatic-forward observation path exists;
or
B) executable auto-forward root capture is removed from r0.1.

Normal human admission MUST NOT be widened to admit automatic-forward events into provider/history/send flow.

## Required decision

Choose exactly ONE bounded correction model:

### OPTION A — evidence-only automatic-forward observation path

If selected, DESIGN successor must define:

1. a separate non-dialogue root-evidence path;
2. it runs before/alongside normal human-turn admission;
3. exact configured linked discussion only;
4. requires is_automatic_forward=true;
5. may validate linked-channel sender/chat projection only if official/current evidence supports it;
6. NEVER enters provider/history/send flow;
7. NEVER counts as accepted tester turn;
8. NEVER widens tester allowlist/admission;
9. persists only bounded root evidence needed for later human-turn root resolution;
10. replay/idempotency/fail-closed behavior explicit;
11. no raw Update/full Message/user identity persistence;
12. resolver ordering updated;
13. R1 PROVEN_AUTO_FORWARD_ROOT updated;
14. metadata/storage boundary updated;
15. T15 updated to prove:
    - evidence captured;
    - provider calls = 0;
    - send effects = 0;
    - tester admission count unchanged;
    - replay/idempotency safe.

If evidence-only path itself becomes ambiguous or unsafe:
fail closed, no dialogue effect.

### OPTION B — remove executable auto-forward root capture from r0.1

If selected:

1. remove PROVEN_AUTO_FORWARD_ROOT from executable r0.1 derivation classes;
2. remove/replace T15;
3. retain official auto-forward semantics only as protocol context/future design input;
4. r0.1 root model relies on:
   - OBSERVED_LINKED_THREAD_ANCHOR;
   - PROVEN_OUTBOUND_LINEAGE;
   - SAME_ROOT_OBSERVATION;
   - ISOLATED_UNRESOLVED;
5. no automatic-forward evidence is required for r0.1 implementation;
6. future auto-forward capture requires separate design/authority.

## Selection criteria

Choose A or B based on minimality, safety and necessity for the CURRENT bounded visitor-dialogue objective.

Do not choose A merely because it is richer.
Do not choose B merely because it is simpler if the current root model would be materially incomplete without auto-forward evidence.

Explain:
- why the selected option is sufficient;
- why the rejected option is unnecessary or riskier for r0.1.

## Preserve accepted design findings

Unless D1 requires local consistency edits, preserve unchanged:

- C5 HYBRID_FAIL_CLOSED as selected high-level model;
- no semantic inference from numeric coincidence 112==112;
- PROVEN_OUTBOUND_LINEAGE guards;
- OBSERVED_LINKED_THREAD_ANCHOR not canonical MTProto top root;
- one-hop reply_to_message bounded lineage;
- no cross-chat/direct-topic merge;
- ambiguity/legacy fail-closed;
- historical tg-dialogue-r02 conversation_key immutability;
- no synthetic legacy backfill;
- versioned root-r01 future semantics;
- privacy-minimal scalar metadata;
- OUTCOME_UNKNOWN / no-blind-resend;
- root derivation before history/provider;
- T1-T14 and T16 unless directly renumbered by correction.

## Output

Create one immutable corrected design successor.

Recommended locator:

entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/

Must include:
- exact predecessor identity;
- exact SIS NEEDS_REWORK identity;
- chosen option A or B;
- exact D1 diff;
- corrected DESIGN.md;
- statement all other accepted design findings remain unchanged except local consistency edits;
- status DESIGN_CANDIDATE_NOT_IMPLEMENTED.

## Expected terminal

PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_CORRECTION_READY_FOR_SIS_RECHECK

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- chosen option;
- rationale;
- exact corrected design locator/blob;
- exact D1 diff;
- unchanged accepted findings;
- DESIGN_CANDIDATE_NOT_IMPLEMENTED;
- exact next gate:
  SIS bounded D1 re-review only.

Then STOP.
