# Exact design binding verdict

verdict: PASS_STATIC_CONDITIONAL_ON_FUTURE_TARGET_EVIDENCE

R02 D1/D2 semantics are represented without weakening.

D1:
- single basename grammar enforced
- anchored root object identity required
- race-safe relative exclusive create plan uses openat2 semantics
- created object identity derives from retained opened object evidence
- same-object continuity is mandatory through write/stat/readback/hash/outcome
- non-replacement/hardlink evidence is mandatory

D2:
- cleanup requires resolved durable outcome
- exact root/parent/current leaf identity and owner/operation binding
- exact confinement/profile evidence
- platform capability remains sufficient
- deletion plan is relative to anchored dirfd
- recursive/wildcard/absolute fallback absent
- post-cleanup anchored absence/root/parent readback required
- ambiguous cleanup => UNKNOWN and no destructive retry

Critical platform condition:
unlinkat pathname semantics are acceptable only when the future target independently proves private attempt-owned namespace plus exclusive namespace mutation control/no foreign writers and serialized effect execution.
If not proven, cleanup is BLOCKED. The candidate does not weaken this requirement.

No concrete target evidence is claimed in this implementation task.
