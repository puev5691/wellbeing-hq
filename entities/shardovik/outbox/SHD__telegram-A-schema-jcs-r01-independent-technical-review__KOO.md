# SHD → KOO: Telegram A closed schema + JCS vectors independent technical review r0.1

terminal_result: `PASS_WITH_BOUNDARIES`
terminal_code: `PASS_SHD_TELEGRAM_A_SCHEMA_JCS_R01_WITH_BOUNDARIES`
scope: `BOUNDED_INDEPENDENT_NON_LIVE_TECHNICAL_DOCUMENT_REVIEW`
candidate_mutation: `none`
A_issued: `NO`
B_issued: `NO`
token_to_bot_binding: `UNKNOWN`
host_access: `0`
credential_access: `0`
Bot_API_calls: `0`
Telegram_mutation: `0`
implementation_changes: `0`
memory_layering_attempt_3: `NOT_AUTHORIZED`
project_time: omitted; trusted project-time source not used

## Human summary

The KAN candidate is technically coherent as a **closed documentary schema candidate** for future A payload bytes.

Independent review confirms:
- 21 top-level fields are consistently specified;
- required/optional/null policy is internally coherent;
- nested object shapes are closed;
- numeric identifiers/generations are intentionally strings, not JSON numbers;
- decoded duplicate keys are required to fail before a map loses the duplicate;
- immutable REF format is closed and requires commit+blob+path correspondence;
- arrays that affect digest semantics have explicit deterministic order requirements;
- current payload digest, readback, current-A approval, effective/current/revoked state and B are correctly kept outside the payload to avoid direct self-reference;
- educational V1–V4 byte lengths and SHA-256 values independently reproduce exactly.

The candidate is **not ready for A issuance**. It remains CANDIDATE_NOT_ACTIVE.

Two pre-issuance semantic rules should be made explicit before an implementation/validator is accepted:
1. `SHA256(bytes resolved by executable_identity.artifact_ref) == executable_identity.sha256`;
2. `issuer.authority_ref` must be a pre-existing independently valid authority artifact and MUST NOT depend on the digest/approval/effectivity of the same A payload.

These are bounded fail-closed clarifications, not a contradiction requiring redesign.

## Resume-First / exact authority

Fresh HQ preflight before processing:
`cb1e6f11e119fa640266bdcd40856f05eb52705d`.

Prewrite reconciliation later observed:
`1d62a2fa545c06439f6b43423659f78d937bcb8c`,
a staged KOO pre-replacement checksum artifact only.

Current KOO writer remained:
`entities/koordinator/current/KOO__replacement-current-writer-v08.md`
blob `ca7ed0ed4e539dcdbe783e122cea409a77ab10cd`
status `WRITER_ESTABLISHED`.

No established v09 current-writer or superseding exact task was found at prewrite.
The exact task blob on current main remained unchanged.

Current SHD writer:
`entities/shardovik/current/SHD__replacement-initiation-current-writer.md`
establishment commit `85260a61784e9aec33784c5d50cfbc3bfceab19b`
blob `88473e85feab1ae5482ff33268ca488abc42f8a4`
state `replacement_current_writer_established`.

Approved SHD operational profile:
`entities/shardovik/current/SHD__role-profile.md`
blob `29df9468da37fb4e9cda0a5912e1f41dffe08a13`.

It permits bounded cross-layer evidence/technical review and local no-side-effect verification under an exact task. It does not grant A/B issuance, canon, host/secrets, implementation or runtime acceptance.

Exact task:
`entities/koordinator/outbox/KOO__telegram-A-schema-jcs-r01-shd-independent-technical-review__SHD.md`
commit `2fcb9d1b2e0714841d573b1237d088ed3e976f6a`
blob `eaa04ca08a88b5a0d4f3b7101eefbf6fd814ab2e`.

Addressed inbox was created by KOO at commit
`ad9179d82ca0e0c836fa4066cb149751798149d8`.

Automatic activation record
`5c12e77416ed08f9beb89412a0b25bc13dd5a64f`
states:
- `processing_started: no`;
- `activation_status: activation_failed`;
- `operator_manual_ping_required: yes`.

The present OPERATOR message is therefore the manual activation of this exact task; it does not expand authority.

## Active approved Project Sources

The six attached active Project Sources were locally read and independently Git-hash checked:

- recovery v1.6 -> `233117e1c9509d730e1f5ec532b1cabe3f786609`;
- roles v2.4 -> `1772339cb74dae8550bfbd2e33401c34a929e911`;
- source-loading v2.2 -> `69eb657f260a019f76e8e707c880ea88c1dfa0bf`;
- file-work v2.4 -> `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`;
- task-conveyor v1.2 -> `df7896d867eeeffff506319538fedad938856686`;
- project core v2.5 -> `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`.

Relevant active rules reconfirmed:
- exact task authority is distinct from inbox/dispatch/activation;
- current-writer does not expand role authority;
- competing writers are not resolved by last-write-wins;
- significant artifacts require immutable identity/readback;
- publication/dispatch do not prove receipt/acceptance.

Prepared PRV role v2.5 remains outside this review because active UI replacement was not verified.

## Exact candidate identity / supersession

Candidate:
`entities/kancelar/outbox/KAN__telegram-bridge-A-closed-schema-jcs-vectors-r01-candidate__KOO.md`
commit `bde5e6caf988b255e52aaa191de41e1f6b354572`
blob `a0fa6d972dc26aa009c55318f03347515bbb7982`
status `CANDIDATE_NOT_ACTIVE`.

Exact predecessor/governance locators stated by KAN were independently re-read and matched:

- six-governance DESIGN_ONLY decision:
  commit `58ab882b8e80b3ff321ac3dd4fac59b138c4c57a`
  blob `666b5c36d5cac571f97cb2baccbb97be81e20146`;

- prior SHD A+B review:
  commit `c641965b9b9d1a3492c191042b5431a48bc2d702`
  blob `17f3dba23a08968b186a23dcfa5d7db56e2924d1`;

- KOO SHD-review governance gate:
  commit `41ea8744f5d356b82ac94c67aac2bcfe6d48ae58`
  blob `863d4d1fdb4df4ea6961ad048b61d9c6e49be17e`;

- KOD A+B predecessor design:
  commit `871cb4e411a537ac2b9657a4b32710f88839d7b7`
  blob `575d5f03159f09de57d91c60fd99078c050f89d8`.

Fresh recent-commit reconciliation showed the KAN candidate, its dispatch/activation boundary, current SHD review task/inbox/dispatch and unrelated later work. No later competing A-schema/JCS terminal or superseding schema candidate was found.

## Closed top-level schema

PASS_AS_DESIGN.

Exactly 21 top-level fields are defined:

1. schema_id
2. profile_id
3. generation
4. bot_id
5. bot_username_hint
6. channel_id
7. credential_slot_ref
8. slot_generation
9. host_identity
10. caller_identity
11. executable_identity
12. operations
13. fixed_parameters
14. issuer
15. trust_anchor_id
16. trust_anchor_ref
17. validity_policy_ref
18. currentness_policy_ref
19. revocation_policy_ref
20. supersedes
21. source_evidence

20 are required.
Only `bot_username_hint` is optional.

Unknown top-level fields are rejected rather than ignored.
No extension/metadata escape hatch exists.

## Types / required / null

PASS_AS_DESIGN.

The candidate consistently defines:
- `ID`: restricted non-empty ASCII string;
- `DEC`: positive decimal ASCII string without sign/leading zero/exponent;
- `SHA256`: exact 64 lowercase hex;
- `REF`: exact four-field immutable Git locator;
- no JSON numbers or booleans in A payload;
- only object / array / string / one specifically permitted null.

Null policy is unambiguous:
- only `supersedes` may be null;
- null is only valid for generation `"1"` with independently verified genesis;
- missing `supersedes` is invalid;
- `bot_username_hint` is absent-or-valid-string, never null/empty.

UNKNOWN is correctly kept outside an actual payload rather than serialized as placeholder text/null/zero/fake hash.

## Closed nested shapes

PASS_AS_DESIGN.

### executable_identity
Exactly:
- `sha256`;
- `artifact_ref`.

### fixed_parameters
Exactly:
- `getWebhookInfo: {}`;
- `getChatMember: {chat_id,user_id}`.

Cross-field equality:
- getChatMember.chat_id == channel_id;
- getChatMember.user_id == bot_id.

### issuer
Exactly:
- `role="KAN"`;
- `principal_id`;
- `authority_ref`.

### supersedes
Either null for verified genesis or exact:
- `profile_id`;
- `generation`;
- `profile_digest`.

Successor generation must equal predecessor generation+1.

### source_evidence item
Exactly:
- `field`;
- `value`;
- `claim_type`;
- `ref`;
- `verifier_principal_id`;
- `verification_ref`.

The array must cover exactly one item for each declared provenance field, except absent optional username hint.

With username hint present the required evidence-field set has 12 entries.
With hint absent it has 11.

V2 has only one entry and therefore intentionally fails this rule.

## Duplicate keys

PASS_AS_DESIGN.

The requirement to detect duplicates by **decoded property name before map construction** is technically necessary and correctly stated.

Independent isolated parser demonstration confirmed that raw keys:
- `bot_id`
- `bot_\u0069d`

decode to the same property name and can be rejected as a duplicate before ordinary object construction would overwrite/lose one value.

No implementation acceptance is implied because no candidate parser exists in this task.

## REF immutable identity

PASS_WITH_BOUNDARIES.

REF has exactly:
- repository;
- path;
- 40-lowercase-hex commit;
- 40-lowercase-hex blob.

The grammar rejects:
- branch/main/latest;
- abbreviated SHA;
- absolute/path traversal/dot segments;
- backslash;
- URL/query/fragment forms.

The document additionally requires the exact repository/path at the exact commit to resolve to the exact blob.
Regex shape alone is explicitly not treated as existence/trust proof.

Independent review of the real project locators used by this candidate found the expected exact blobs.

Synthetic `example/fixture` refs in V2 are not real provenance and are not treated as such.

### Required pre-issuance clarification 1: executable artifact binding

The field description states that `executable_identity.sha256` is the hash of actual executable bytes and `artifact_ref` is their immutable locator.

For fail-closed validator semantics this relationship should be made an explicit cross-field rule:

`SHA256(REF_RESOLVED_BYTES(executable_identity.artifact_ref)) == executable_identity.sha256`.

REF existence plus a separately stated sha256 does not, by itself, prove the two identify the same bytes unless this comparison is mandatory.

This is a bounded schema clarification before issuance/implementation acceptance.

## Deterministic arrays

PASS_AS_DESIGN.

- `operations` must be exactly
  `["getWebhookInfo","getChatMember"]`
  in that order;
- no duplicate/third operation;
- JCS does not reorder arrays;
- `source_evidence` has an explicit UTF-16-code-unit order by its `field` value and wrong order is rejected rather than silently sorted.

This removes digest ambiguity from semantically equivalent but differently ordered arrays.

## Independent vector recomputation

Computation was performed locally on public synthetic values only, without project host/network/credential/Telegram access.

For the schema-relevant vectors the independent serializer used:
- recursive object-key sorting;
- compact JSON separators;
- UTF-8;
- no trailing LF;
- array order unchanged;
- no JSON numbers/booleans.

### V1

Canonical text:
`{"bot_id":"8866633840","channel_id":"-1003606547591"}`

Independent result:
- bytes: `53`;
- hex:
  `7b22626f745f6964223a2238383636363333383430222c226368616e6e656c5f6964223a222d31303033363036353437353931227d`;
- SHA-256:
  `f24e21c83112b798b26107ddacbbd5ad8c7c134e8c168373aa58e0fb98df0f4f`.

MATCH candidate: PASS.

V1 remains standalone-invalid:
`REJECT_MISSING_FIELDS`.

### V2

The full source fixture from the candidate was independently reconstructed field-for-field and serialized.

Independent result:
- canonical UTF-8 bytes length: `2211`;
- SHA-256:
  `06b05384a53dcc6ab9fc9c6da62a55936d3f1d39ad7686c0b737441778e66b32`;
- first ten bytes:
  `7b 22 62 6f 74 5f 69 64 22 3a`;
- last byte:
  `7d`;
- no trailing LF.

MATCH candidate: PASS.

But V2 is **not** a positive schema/provenance/admission vector:
- username hint is present, so complete source_evidence requires 12 field entries;
- V2 provides only 1;
- every REF/principal/hash is explicitly synthetic;
- trust/currentness/revocation/issuance approval are not established.

Therefore:
`V2 -> REJECT_PROVENANCE_COVERAGE / NOT_EFFECTIVE_A`.

Canonicalization success is not provenance success.

Production admission must not take the educational V2 digest as a valid profile digest.

### V3

`{"supersedes":null}`
- bytes: `19`;
- hex:
  `7b2273757065727365646573223a6e756c6c7d`;
- SHA-256:
  `549fec5f27071a2c99fb30d8706716e235d33c1f503992f804b465afcb08465e`.

`{}`
- bytes: `2`;
- hex: `7b7d`;
- SHA-256:
  `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`.

MATCH candidate: PASS.

This correctly demonstrates missing != null.
It does not make either fragment a full valid A.

### V4

Single U+00E9:
`{"value":"é"}`
- bytes: `14`;
- hex:
  `7b2276616c7565223a22c3a9227d`;
- SHA-256:
  `69e46f3f0688000ab7eeb9e40e6a516a254268cd644a24f4f69cf7ad063cf479`.

U+0065 + U+0301:
`{"value":"é"}`
- bytes: `15`;
- hex:
  `7b2276616c7565223a2265cc81227d`;
- SHA-256:
  `1b986c631da83257beca64c93ff3e5174908d558af7bb9dfb36b25a6198f7c38`.

MATCH candidate: PASS.

The two visually similar strings remain byte-distinct.
No implicit Unicode normalization occurs.

The `value` property is not part of A schema; V4 is only a JCS micro-vector.

## RFC 8785 verification boundary

Official RFC 8785 was independently checked at the RFC Editor during this review.

Relevant requirements confirmed:
- JCS input is constrained to I-JSON;
- duplicate object property names are not allowed;
- Unicode string data is preserved as-is rather than normalized;
- invalid Unicode such as lone surrogates must cause failure;
- object property names are recursively sorted by UTF-16 code units;
- array element order is not changed;
- final canonical output is UTF-8.

The candidate is consistent with those points.

However:
`FULL_RFC_8785_IMPLEMENTATION_CONFORMANCE = UNKNOWN`.

This review did not execute the RFC full conformance corpus or certify a general-purpose canonicalizer.

Not independently covered as a full implementation suite:
- IEEE-754 number serialization;
- all ECMAScript string escaping cases;
- supplementary-plane/non-ASCII property-name sorting;
- every RFC test vector;
- duplicate-preserving parser implementation;
- runtime admission implementation.

For this exact proposed A schema, all property names and admitted identity/reference strings are tightly restricted, and JSON numbers/booleans are not used. Therefore the independently reproduced V1–V4 subset is sufficient to verify the **documented educational bytes**, not to certify arbitrary RFC 8785 software.

The candidate's rejection of Unicode noncharacters is an additional A-schema restriction; it should not be represented as a general RFC 8785 requirement.

## Provenance coverage

PASS_WITH_BOUNDARIES.

The source_evidence design correctly distinguishes:
- intended project identity claims for bot/channel/optional username;
- anchored assignments for profile/generation/slot/host/caller/executable hash/issuer principal/trust anchor.

A verification record does not become live Telegram truth.
A document hash does not establish token→bot binding.

REF and verification_ref are required to be immutable documentary evidence.
Independent currentness/trust/effectivity still remain separate gates.

### Executable provenance boundary

As stated above, explicit byte-to-hash comparison between executable `artifact_ref` and `sha256` should be added before issuance/implementation acceptance.

## Digest / approval / trust-root cycle analysis

PASS_WITH_BOUNDARIES.

The candidate correctly excludes from current A payload:
- current `profile_digest`;
- current A Git readback locator;
- signature;
- current exact approval;
- effective/current/revoked state;
- B;
- B evidence that already depends on current A.

The intended sequence is acyclic:

1. pre-existing trust/policy/assignment/source-verification artifacts;
2. build and validate payload;
3. JCS canonical bytes;
4. SHA-256 profile digest;
5. immutable readback of payload bytes;
6. detached exact-digest OPERATOR approval;
7. detached effectivity/currentness/revocation evidence;
8. later B references A digest.

`supersedes.profile_digest` references only a pre-existing predecessor A and is not self-reference.

### Required pre-issuance clarification 2: issuer.authority_ref

Because `issuer.authority_ref` is itself inside the hashed payload, the validator/spec should explicitly require:

- the referenced issuer authority already exists before the current payload digest is computed;
- it independently authorizes the exact issuer principal/schema/scope;
- it does not depend on the current A digest, current-A approval, effectivity or readback.

Without this explicit sequencing rule an implementation could accidentally construct:
`A payload -> issuer authority/approval -> A digest`
while the authority itself depends on that digest.

The design prose strongly implies pre-existing separate authority, but the no-cycle condition should be stated normatively for this field just as it is already stated for policy and verification refs.

### Trust root

No self-bootstrap was found in the candidate.

`trust_anchor_ref`, validity/currentness/revocation policy refs and source verification refs are explicitly required to be predecessor evidence.

Actual trust-anchor implementation/effectivity remains UNKNOWN and is not supplied by the hash itself.

## Known / UNKNOWN after review

Verified document facts:
- intended bot_id: `"8866633840"`;
- intended channel_id: `"-1003606547591"`;
- documentary username hint: `"@WBNP_Media_Bot"`;
- diagnostic operation set remains exactly two methods;
- KAN candidate exact commit/blob exists;
- educational vector calculations match.

UNKNOWN / not created:
- live current username;
- token→bot binding;
- current protected credential slot reference/generation;
- real A profile_id/generation/genesis;
- actual host/caller/executable assignment;
- actual executable bytes;
- real issuer principal/issuance authority;
- implemented OPERATOR trust-root anchor;
- effective validity/currentness/revocation contracts and resolver evidence;
- exact A digest approval/readback/effectivity;
- B;
- secure protected credential transfer;
- runtime/admission implementation.

Existing SIS Bot API diagnostic blocker remains active.

## Defect classification

No design contradiction was found in the 21-field closed schema or V1–V4 vectors.

Two bounded pre-issuance specification clarifications are required:

### BOUNDARY-CORRECTION-01
Add explicit cross-field rule:
`SHA256(REF_RESOLVED_BYTES(executable_identity.artifact_ref)) == executable_identity.sha256`.

### BOUNDARY-CORRECTION-02
Make `issuer.authority_ref` explicitly predecessor/pre-digest evidence and prohibit dependence on the current A digest/approval/effectivity/readback.

If either is omitted by a future validator, that validator must not receive implementation/security acceptance.

Neither correction requires changing V1–V4 expected bytes because those rules concern admission/provenance semantics, not JCS serialization.

## V2 disposition

`V2_SERIALIZATION = PASS`
`V2_SCHEMA_PROVENANCE_GATE = REJECT`
`V2_EFFECTIVE_A = NO`.

The fixture's exact 2211-byte serialization and matching digest do **not** prove:
- complete source_evidence;
- REF existence/trust;
- issuer authority;
- trust root;
- currentness/revocation;
- OPERATOR exact-digest approval;
- token→bot binding.

## Authority boundary preserved

This review:
- did not issue A;
- did not issue B;
- did not contact a project host;
- did not access token/credential content;
- did not call Bot API/Telegram;
- did not change implementation;
- did not change Project Sources/canon;
- did not claim runtime safety;
- did not authorize memory-layering attempt 3.

## Terminal

`PASS_WITH_BOUNDARIES`

Exact machine terminal:
`PASS_SHD_TELEGRAM_A_SCHEMA_JCS_R01_WITH_BOUNDARIES`.

Candidate remains:
`CANDIDATE_NOT_ACTIVE`.

Smallest next correction before issuance:
- KAN/KOO may incorporate only BOUNDARY-CORRECTION-01 and -02 into the next documentary schema revision or explicit normative addendum;
- then exact immutable successor bytes require fresh independent review before any A issuance.

No live or implementation step follows automatically.
