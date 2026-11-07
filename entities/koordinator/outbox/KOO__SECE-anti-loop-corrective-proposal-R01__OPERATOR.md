# KOO SECE anti-loop corrective proposal R01

status: PROPOSAL_FOR_OPERATOR_REVIEW
entity: KOO / КООРДИНАТОР r1.4
scope: ONE_SECE_WORK_CYCLE_PILOT_ONLY
project_time: omitted

## Operator task authority

Current chat OPERATOR instruction:

"Поручаю КООРДИНАТОРУ подготовить один конкретный anti-loop corrective proposal для SECE: убрать повторные gates без новых оснований и вернуть цепочку к SHD rereview R02. Не переписывать каноны глобально до проверки этого решения на реальном рабочем цикле."

This authorizes preparation of one proposal only. It does not authorize canon mutation, activation, G4/G5/G6, real sandbox effects, or automatic downstream continuation.

## Human summary

The KOD R02 correction is recorded as PASS and ready for independent rereview. The next intended specialist is SHD. The existing SHD self-snapshot handoff contains a stale frontier reference: its PROMPT records frontier blob b16894c2119bbac96f8a49e607ad25b28d950fc0, while the currently fetched frontier file is blob 81082bc94bf8db76196139626291409bef853f7c. This is a narrow evidence-reference mismatch, not evidence that the whole SECE state or KOO writer must be reinitialized.

The proposal is to reconcile only this exact reference, then continue the existing SHD handoff with the minimum required gates. The mismatch must not be “fixed” by assuming the old or new frontier is correct without immutable readback.

## Corrective rule proposed for this pilot

### 1. Event-triggered gate reuse

For this single SECE cycle, treat a gate result as reusable only within its recorded scope and exact immutable inputs.

- If the exact writer blob, source-set identity, task authority, candidate/result blobs, and relevant registry/frontier identities are unchanged, reuse the prior verified gate evidence.
- Do not rerun initiation, Writer Gate, recovery integrity, source-set checks, or queue reconciliation merely because a new chat turn or handoff is occurring.
- Revalidate only the dependency whose evidence changed or whose required validity is explicitly event/phase-bound.
- A changed immutable identity, superseding writer/task, conflicting result, missing required evidence, or actual boundary transition invalidates the affected gate and triggers that gate only.
- A gate result is not promoted to broader authority. Passing a preservation gate does not authorize review; passing review does not authorize sandbox execution or G4/G5/G6.

### 2. Minimum evidence at the next handoff

For SHD R02 rereview handoff, perform only:
1. Resume-First against the exact SHD current-writer/recovery basis already established; rerun initiation/writer gates only if continuity/writer/recovery evidence actually changed.
2. Readback and reconcile the exact SHD snapshot authority, registry, and frontier; resolve the stale frontier blob by confirming the exact current commit/path/blob and accepted state.
3. Confirm the immutable KOD R02 result and package tree, plus KOD recovery v09 identity, remain the exact review inputs.
4. Confirm no competing SHD snapshot/review result or superseding authority exists.
5. Confirm candidate remains NOT_ACTIVATED, real sandbox effect NOT_EXECUTED, target UNKNOWN/NOT_SELECTED, G4/G5/G6 NOT_CREATED.
6. If these checks pass, continue to the separately authorized SHD R02 review task. Do not create review authority from this proposal alone.

Do not re-run unrelated SECE/R04 proofs, historical queue scans, global source-set activation, or full recovery integrity checks when their exact evidence remains unchanged and the applicable canon does not require them at this phase.

### 3. Frontier discrepancy handling

Current PROMPT frontier blob (stale reference candidate):
b16894c2119bbac96f8a49e607ad25b28d950fc0

Fetched current frontier file blob:
81082bc94bf8db76196139626291409bef853f7c

Required disposition:
- Freshly fetch the exact frontier file and its containing commit.
- Verify authority/registry bindings and accepted_state.
- If the current frontier is the accepted successor and authority/registry remain consistent, update/reissue only the SHD self-snapshot handoff reference to the exact current frontier.
- If it is a competing or incompatible frontier, STOP with that exact mismatch; do not reset the whole SECE chain.

## Pilot acceptance criteria

The anti-loop pilot is PASS only if:
- SHD reaches its authorized independent R02 rereview without unnecessary repeat initiation/Writer Gate/source-set/recovery rituals;
- all reused gates are tied to exact unchanged evidence;
- changed evidence causes only the affected gate to rerun;
- no stale frontier is silently accepted;
- no authority boundary is widened;
- SHD returns a review verdict with evidence and KOO records one concise reconciliation.

Pilot FAIL if any mandatory gate is skipped despite changed/missing evidence, or if the workflow still demands a full repeated gate sequence without a concrete changed input or canon-required trigger.

## Boundaries

- No global Recovery Canon, Writer Gate, Task Conveyor Canon, Project Sources, or SECE canon rewrite.
- No retroactive approval of earlier artifacts.
- No SHD R02 review authority created by this proposal.
- No G4/G5/G6 authority, activation, deployment, or real sandbox effect.
- No automatic continuation.
- Historical prompts/queues are navigation evidence only, not replay authority.

## Proposed next action

Operator reviews this single pilot proposal. If accepted, KOO fresh-reconciles the exact SHD frontier/authority/registry identities and issues one corrected, bounded SHD handoff for the already intended R02 rereview. No global canon change is made until the pilot result is observed and reviewed.

terminal:
PROPOSAL_READY_FOR_OPERATOR_REVIEW
