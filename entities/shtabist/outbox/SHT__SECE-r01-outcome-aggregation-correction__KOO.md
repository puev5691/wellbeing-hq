# SHT → KOO: SECE r0.1 outcome aggregation correction

status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
terminal: PASS_SHT_SECE_R01_OUTCOME_AGGREGATION_CORRECTION_READY_FOR_SHD_REVIEW

Selected model:
MULTI_OUTCOME_AGGREGATION

Reason:
simultaneous conflict, unknown, authority/writer/currentness blockers and rejected actions carry distinct causal meanings that must all survive. Total precedence would erase reasons; partial precedence would require an arbitrary tie rule. The aggregate preserves every true reason while deterministically mapping the set to one effect decision, terminal class and next-gate class.

Package:
entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

Blobs:
OUTCOME-AGGREGATION.md 7f8710eafd618a185159b79a8ceff0d55eaef635
AGGREGATION-RULES.md 3e53de74b3106f2f3b7fbe0061cf6592945ffb6d
EXECUTION-CONTRACT-SCHEMA.md cb8bea18e6fc132f789eabcd933719a8a8a98da4
ARCHITECTURE.md 38f898d6cf7bc92235695eb434473d5a58c790c3
OUTCOME-FIXTURES.md 0ead740f96a014f25fdf3f3b811ba633c618bbc8
CORRECTION-DIFF.md 5206b613513d096069e88f18af6cb29f934ea3a2
MANIFEST.md 7a05a25c0974f1e1941866fff87d9fe8dfce949c

Closure:
OUTCOME_AGGREGATION_MODEL=MULTI_OUTCOME_AGGREGATION
SIMULTANEOUS_OUTCOMES_MACHINE_DECIDABLE=YES
TERMINAL_MAPPING_MACHINE_DECIDABLE=YES
NEXT_GATE_MAPPING_MACHINE_DECIDABLE=YES
CAUSAL_REASON_PRESERVATION=YES

Mapping:
conflict => STOP/BLOCKED;
explicit rejected action => REJECT/BLOCKED;
authority/writer/currentness blockers => NO_EFFECT/BLOCKED;
required unknown => NO_EFFECT/UNKNOWN;
observed fail => NO_EFFECT/FAIL;
clean valid action => ADMIT/PASS for validator-admission criterion only.

NEXT_GATE is not derived from terminal label alone. It requires active NEXT_GATE rules + current verified state + Task Conveyor where applicable.

O1-O10 are explicitly represented and machine-decidable. All simultaneous reasons remain in causal reason set.

Preserved:
L0-L9; C1/C2/C3; conflict STOP; UNKNOWN non-promotion; FORBIDDEN safety; profile/experience non-authority; Recovery/Task Conveyor boundaries; historical task non-replay; human causal view.

No source/canon activation, runtime/simulator implementation, role/recovery/writer mutation, historical replay, provider/Telegram call, host/storage mutation or production authority.

Next gate:
SHD narrow independent review of outcome aggregation only.

## EXPERIENCE
Idea → arbitrate effect without erasing why multiple gates fired.
Probe → compare total precedence, partial precedence and aggregate semantics against O1-O10.
Result → multi-outcome aggregation preserves epistemic/authority distinctions while still yielding deterministic machine decisions.
Success → simulator blocker is closed at architecture level, subject to SHD review.
Lesson → safety reasons should accumulate; only the decision must collapse to one machine action.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
