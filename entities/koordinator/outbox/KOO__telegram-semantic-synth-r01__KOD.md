# KOO → KOD: Telegram semantic synthetic round-trip r0.1

status: TASK
execution_mode: SYNTHETIC_ONLY
priority: HIGH_EXPERIMENTAL

Verified basis:
- normalized bridge PASS `c0ed7057da344bf6b10b0718960c36962b8d9536`
- SemanticInput contract PASS `8d738f6a2eafb84485ab5e11e1961adb60d017ac`
- discussion send/readback PASS `09b6fdfd04da84533185b11b0861b2220b72dfb3`

Goal:
Exercise the semantic privacy/admission path on synthetic discussion excerpts only.

Path:
synthetic excerpt → privacy/minimization gate → SemanticInput → facilitator core → discussion_state + candidate_task proposal → no dispatch.

Required:
- reject raw/unbounded Telegram update envelopes;
- avoid unnecessary participant identity fields;
- no raw discussion-text persistence outside bounded test fixtures;
- mark synthetic provenance;
- candidate_task must not become dispatched/accepted automatically;
- zero live Telegram reads/sends;
- zero live provider calls.

Expected:
`PASS_KOD_TELEGRAM_SEMANTIC_SYNTH_R01_READY_FOR_VERIFY`
or exact blocker/fail.
