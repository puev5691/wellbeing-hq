# SIS → KOO: Telegram facilitator semantic-input independent verify r0.1

verdict: `PASS_SIS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01`
production: `no`
telegram_api_calls: `0`
live_provider_calls: `0`
credentials_used: `0`
db_systemd_runtime_deployment: `0`
project_time: omitted; trusted project-time source not used

## Resume-First
fresh_HQ_HEAD: `d78b7c549d92f51f1b485b02469a65f8272e6f2b`
prewrite_reconciliation_HEAD: `104d66b92dd2f6d8bff7ec93f7df0319f80b5b5b`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__telegram-facilitator-semantic-input-independent-verify-r01__SIS.md`
commit `5c0e408893b9111dd9c12a0910ec5c2199d969ca`.

Inbox placement commit:
`28d950eaa58c28d99ac8e8713d295790719fa29a`.

KOD report:
commit `8cd295606cc4f8bad5336de66fa7506008eea920`
verdict `PASS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01_READY_FOR_INDEPENDENT_VERIFY`.

## Exact immutable candidate
Package:
`entities/koder/outbox/telegram-facilitator-semantic-input-contract-r01/`
commit `5d3db12bb4311e8d2d225882b2fbd7a947e09005`
tree `475ccfa91ba6f354a09a64946d33850e46f9d545`.

Exact composition is seven files:
- MANIFEST.json
- README.md
- fixtures.py
- semantic_input.py
- test.stderr.txt
- test.stdout.json
- test_semantic.py

Independent SHA-256 readback:
- MANIFEST.json `e46e873e5fa26dd9babbaba1a600903cbb050bf377905f96e3167162a5e27f07`;
- README.md `0d4e743e367919b46a8a0bd749afc2f08d388b86089ae9aa686439d75ebee84b`;
- fixtures.py `44c6a4d3b975dfe143b6140374e312c4b0f12314d856f65d739c9dfa9dfd7b79`;
- semantic_input.py `dab4746b25a62d07b7d84d5ee933bfb978d420593079a98c99552c485acf73f9`;
- test.stderr.txt `0cea82967c53a0f4d5d6a440bbc337210e710a38487c53eff58c65ed2267af28`;
- test.stdout.json `24fa5eabc324e9cee112ff7ff08264cd6896a7c965e17ca9719de5488e563577`;
- test_semantic.py `521c84dd6eb4e8a8b6edba5c45fac4a804fe595aa81cd4a492278ce1c2a2e483`.

Post-test hashes remained identical.

## Exact accepted dependency
The only application dependency is accepted facilitator_core.py:
- source commit `0020dff62785a5fd0048b0696728b3518812dcd1`;
- Git blob `ad980b0de8a00c1d134823cebc49059a0811f3fa`;
- SHA-256 `33f280e9cc56534996d0706de7e3605c0247ff1af8b71ea985fdd7613d47b64a`.

No dependency bytes were modified.

## Independent execution
The exact candidate and exact facilitator core were copied from immutable Git commits into a temporary test-only directory.

Executed:
`python3 -I -B candidate/test_semantic.py --core deps/facilitator_core.py`.

Observed:
- test methods: `39`;
- failures: `0`;
- errors: `0`;
- skipped: `0`;
- fixture semantic inputs: `13`;
- network attempts: `0`;
- process attempts: `0`;
- write attempts: `0`;
- database open attempts: `0`;
- provider calls: `0`;
- Telegram API calls: `0`;
- credentials used: `false`.

## Declared-only semantic boundary
The candidate accepts only analysis policy mode `declared_only`.
Semantic category must be explicitly declared and allowed by policy.
Automatic inference from excerpt/claim text is not implemented and unsupported modes fail closed.
No provider/LLM dependency or call exists in this contract.

## Bounded semantic content
Independent tests confirmed:
- excerpt is literal and UTF-8 bounded;
- structured claim is literal subject/predicate/object with local per-field bounds;
- total input size is bounded;
- unsupported/unknown fields and malformed input fail closed;
- raw Telegram update shapes are rejected;
- undeclared Telegram user_id/username or action/identity fields are rejected.

These are local candidate bounds, not claims about Telegram platform limits.

## Optional participant boundary
Optional participant uses a discussion-scoped pseudonym only.
It requires:
- policy allow_participant;
- exact matching discussion scope;
- bounded pseudonym identity and expiry;
- explicit AdmissionProof confirmation.

The participant itself is not exported downstream in the core NormalizedEvent/SemanticResult.
The candidate does not claim the pseudonym is intrinsically anonymous or unrelated to a real Telegram identity; that remains an upstream privacy-gate responsibility.

## AdmissionProof / AdmissionCheck
Independent tests and source readback confirm the admission check binds:
- exact semantic input identity;
- exact authority/task/writer/privacy_gate;
- analysis-policy digest;
- category and source/provenance;
- participant digest when present;
- discussion scope;
- privacy/retention/expiry state.

AdmissionProof must match the exact AdmissionCheck hash and bounded timing/retention conditions.
Missing, forged, stale, expired or malformed proof fails closed.
Input fields are not self-authorizing.

## Privacy / retention / provenance
Output inherits the strictest privacy/retention constraints and nearest expiry from semantic input, all sources and optional participant.
For minimized input the output remains minimized_derived/memory_only.
Expiry is checked again against current logical tick.
SourceRefs remain exact and semantic input adds its own version-bound source identity.
Changed content requires changed source identity and a fresh admission.

No persistent raw storage is required by the library; it performs no DB/file/log persistence. This does not claim physical erasure of process memory or external copies.

## Candidate task / authority boundary
Independent end-to-end tests against the accepted core confirm:
- generated task remains `candidate_only`;
- `executable=false`;
- `approved_for_execution=false`;
- approve/reject/defer review records do not create execution authority.

The semantic-input library itself does not call apply_event, synthesize, record_decision or dispatch. It produces a bounded SemanticResult/NormalizedEvent only.

## Protected upstream boundary
This independent verification used only temporary copies.
Existing Phase1B, aggregate bridge and accepted facilitator-core bytes were not modified.
No runtime, DB, service or production mutation occurred.

## Conclusion
The exact immutable candidate independently satisfies the bounded semantic-input contract required by the exact KOO task.

This PASS does not authorize real Telegram ingestion, upstream privacy-gate implementation, provider/LLM use, credential handling, DB/systemd deployment, automatic approval or production integration.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: independently verify exact facilitator semantic-input contract and privacy/authority boundaries
СТАТУС: `PASS_SIS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01`
