# WEB → KOO: GitHub information-entry Stage B synthesis

status: RESULT_FOR_KOO_REVIEW
stage: bounded Stage B synthesis
production: no
repository_settings_change: none
publication_authorized: no
project_source_created: no

## 1. Purpose

Provide the bounded WEB synthesis requested by KOO after accepted ARH/KAN/SIS Stage A inputs and accepted RED editorial prerequisite.

Source task:
`entities/koordinator/outbox/KOO__github-info-entry-stageB-synthesis__WEB.md`

Task artifact commit:
`306b0148a500961f6685d6bf05d17b341ddcde97`

## 2. Core decision: public-entry state is multi-dimensional

No single status may answer all questions.

Future information objects must preserve separate dimensions:

1. **source/provenance state** — ARH;
2. **semantic/profile state** — competent profile owner;
3. **editorial state** — RED;
4. **public/legal state** — KAN or named authority;
5. **security/infrastructure state** — SIS where applicable;
6. **technical representation state** — WEB;
7. **release state** — KOO/OPERATOR/named release authority;
8. **publication/distribution state** — concrete surface delivery/readback;
9. **external feedback state** — media-specific receipts/reactions/comments, never source authority.

Short form:

`source truth ≠ editorial readiness ≠ legal allowance ≠ security safety ≠ technical representation ≠ release authority ≠ published ≠ syndicated`

## 3. Authority matrix

| Dimension | Owner | Typical question | Must not imply |
|---|---|---|---|
| Source/provenance | ARH | Where did this exact object come from and what version is it? | semantic approval or publication |
| Semantic/profile | profile owner | Is the domain content correct/current/candidate/unknown? | editorial or legal approval |
| Editorial | RED | Is this exact text ready as text for intended audience/use? | legal, security, release, deployment |
| Public/legal | KAN/named authority | Is intended public use allowed and under what conditions? | editorial quality or deployment |
| Security/infrastructure | SIS | Is the selected surface/runtime safe/ready in scope? | semantic truth or publication authority |
| Representation | WEB | Can the exact approved input be represented/previewed/deployed/read back correctly? | release authority |
| Release | KOO/OPERATOR/named authority | May this exact object be released on the intended surface? | actual delivery |
| Distribution | WEB/media adapter | Was it sent, where, and was delivery/readback verified? | source truth or acceptance |


Navigation/rendering/indexing may never upgrade a dimension.

## 4. Reconciled metadata contract candidate

### Identity/provenance

- `id`;
- `title`;
- `artifact_type`;
- `content_class`;
- `owner_profile`;
- `canonical_locator`;
- `provenance_locator`;
- `source_repository`;
- `source_path`;
- `source_commit`;
- `source_blob`;
- `immutable_identity`;
- `supersedes`;
- `superseded_by`.

### Semantic/profile

- `semantic_status`;
- `profile_review_status`;
- `profile_review_locator`;
- `semantic_blocker` if any.

### Editorial / RED

- `editorial_status`;
- `editorial_result_locator`;
- `intended_audience`;
- `intended_purpose`;
- `derivative_of`;
- `derivative_type`;
- `editorial_blocker`;
- `editorial_superseded_by`.

Accepted RED states:
- `editorial_unassessed`;
- `editorial_draft`;
- `editorial_reviewed`;
- `editorial_ready`;
- `editorial_blocked`;
- `editorial_superseded`;
- `editorial_withdrawn`.

### Public/legal / KAN

- `public_legal_outcome`;
- `rights_basis`;
- `personal_data_state`;
- `public_legal_conditions`;
- `public_legal_next_gate`;
- `public_legal_result_locator`.

Accepted bounded outcomes:
- `allowed`;
- `allowed-with-conditions`;
- `blocked`;
- `unknown`.

### Security / SIS

- `security_state`;
- `security_review_locator`;
- `requires_privileged_setting`;
- `runtime_boundary` if applicable;
- `secret_dependency` as boolean/classification only, never secret value.

Candidate security states for WEB contract:
- `not_applicable`;
- `public_safe`;
- `requires_SIS_review`;
- `blocked_secret`;
- `unknown`.

Exact SIS vocabulary may be refined later without collapsing other dimensions.

### WEB representation

- `representation_state`;
- `representation_result_locator`;
- `preview_locator`;
- `canonical_public_url`;
- `readback_locator`;
- `renderer_version`;
- `transformation_rule` for meaning-preserving mechanical transformations.

Candidate representation states:
- `representation_unassessed`;
- `preview_ready`;
- `preview_built`;
- `representation_ready`;
- `deployed_unverified`;
- `readback_confirmed`;
- `representation_blocked`;
- `representation_superseded`;
- `representation_withdrawn`.

`readback_confirmed` means only that the exact built/deployed representation was independently observed at its expected locator.

### Release

- `release_state`;
- `release_authority`;
- `release_decision_locator`;
- `release_conditions`.

Candidate values:
- `release_unassessed`;
- `release_authorized`;
- `release_blocked`;
- `release_withdrawn`.

### Distribution / external media

- `distribution_targets`;
- `distribution_state` per target;
- `external_message_id` / external locator;
- `delivery_receipt`;
- `correction_state`;
- `withdrawal_state`.

Candidate distribution states:
- `not_dispatched`;
- `dispatching`;
- `delivered_unverified`;
- `delivered_verified`;
- `corrected`;
- `withdrawn`.

Telegram/channel posts, feeds, newsletters and other adapters are derivative distribution surfaces and must retain parent/source linkage.

## 5. Preview boundary

### Preview may be allowed when

- exact immutable version is known;
- provenance is present;
- semantic status is explicit;
- no secret/sensitive-public blocker exists;
- RED issued `handoff_for_preview` or equivalent bounded evidence where editorial content is involved;
- preview is clearly marked non-production;
- preview cannot be mistaken for current/approved source if semantic status is candidate/research/history.

### Preview must fail closed when

- immutable version unknown;
- source status unknown/conflict affects representation;
- credential-like content unresolved;
- personal/privacy state unknown where relevant;
- RED review required but absent and preview would imply reviewed/public content;
- current/superseded relation unresolved.

Preview existence != publication.

## 6. Public representation gate

A public representation may be considered only when all applicable gates independently pass.

Conceptual conjunction:

`semantic/profile acceptable for intended use`
`AND editorial_status = editorial_ready`
`AND public_legal_outcome ∈ {allowed, allowed-with-conditions satisfied}`
`AND SIS/security gate satisfied where applicable`
`AND representation_state = representation_ready`
`AND release_state = release_authorized`

After deploy:

`deployed_unverified → readback_confirmed`

Only then may project process mark the representation as verified published if its publication definition requires those gates.

Missing gate = blocked, not inferred PASS.

## 7. Fail-closed matrix

| Condition | WEB handling |
|---|---|
| semantic_status unknown/conflict | exclude from default-current navigation; blocker |
| immutable identity mismatch | hard block |
| editorial status missing | not public-ready |
| editorial_blocked | block public representation |
| editorial_ready + legal unknown | block public release |
| legal blocked | block public representation/distribution |
| rights basis unknown where reuse required | block copy/mirror |
| personal-data state unknown where relevant | block public release |
| credential-like material | block + SIS review |
| SIS state unknown for security-sensitive content/runtime | block deploy/public operational exposure |
| release state missing | block public release |
| deployed without readback | show `deployed_unverified`, never published-verified |
| external adapter send without returned id/receipt | `delivered_unverified` |
| source superseded while derivative active | mark stale/block new syndication pending update |


## 8. Update behavior

Any semantic content change creates a new immutable version.

Default effects:
- editorial readiness does not transfer;
- KAN/SIS/profile outcomes transfer only if their decision explicitly covers the new version/class;
- representation build must be regenerated;
- release must reference exact new version;
- external derivatives require correction/update policy.

Purely mechanical format transformation may preserve upstream outcomes only when an explicit transformation rule proves meaning preservation and exact input/output identities are recorded.

## 9. Supersede

When a new version replaces an older one:

- preserve old immutable object;
- record `superseded_by`;
- mark old editorial version `editorial_superseded` if RED says so;
- current navigation prefers newer accepted/current representation;
- history remains addressable;
- external derivatives must be updated or marked superseded/stale according to adapter policy.

## 10. Archive/historical

Archive is not approval.

Archived/historical material:
- keeps literal semantic/editorial/legal states;
- is excluded from default-current navigation unless explicitly requested;
- may have a clearly separated historical surface;
- must not be summarized as current truth without a new derivative review.

## 11. Withdrawal

Withdrawal is its own event.

If not yet public:
- stop preview/release path;
- preserve decision/history.

If already public:
- set representation/distribution withdrawal state;
- canonical surface shows withdrawal/correction record where appropriate;
- external channel adapters receive their own correction/withdrawal action;
- no silent history erasure.

## 12. Derivatives

RED accepted rule applies directly:

Summary, teaser, translation and substantive abridgement are new editorial artifacts.

Therefore every derivative needs:
- `derivative_of` exact parent version;
- `derivative_type`;
- intended audience/channel;
- exact derivative version;
- RED status;
- inherited public/legal constraints rechecked for the derivative;
- representation/distribution state.

Example:

`full publicism article`
`→ Telegram teaser`

The teaser may be much shorter, but it cannot strengthen economic/legal/project claims or convert fiction/history/candidate into current promise.

## 13. Telegram/media integration boundary

Future Telegram media-gateway is downstream of this Stage B model.

Minimum Telegram input object should contain:
- publication_id;
- exact parent/source identity;
- derivative exact identity;
- `editorial_ready` for the Telegram derivative;
- public/legal PASS/conditions;
- release authorization;
- canonical URL;
- canonical readback PASS;
- target channel policy.

Telegram delivery then adds only distribution evidence:
- channel chat id;
- channel message id;
- discussion root id;
- reactions/comments metrics;
- delivery receipt;
- corrections/withdrawal.

Telegram comments/reactions do not change semantic or editorial status automatically.

## 14. Navigation boundary

Candidate public navigation structure should separate:

### Current/public
Only objects with all required public gates satisfied.

### Research/candidate
Separate clearly labelled area if KOO/KAN/RED permit public visibility. Never default-current.

### Historical/archive
Separate historical surface with explicit status.

### Operational evidence
Not part of public navigation by default. Only explicit public-safe projection/manifest may expose it.

### External references
Shown as external/reference with rights/attribution metadata, never as project-authored content.

## 15. Multi-repo source contract

Maintain deny-by-default source registry.

Each source entry must define:
- owner/repo;
- ingestion mode;
- allow paths;
- deny paths;
- profile owner;
- required semantic/editorial/legal/security gates;
- immutable identity rule;
- update/supersede behavior.

No recursive crawl of HQ operational field.

## 16. Exact remaining blockers before implementation/public pilot

### Information-entry implementation blockers

1. KOO review/acceptance/revision of this Stage B synthesis.
2. Decision on topology: separate public-web repo vs in-HQ representation.
3. Authority to create/configure any new public repo/Pages/Discussions/Wiki.
4. KOD implementation task for schema/exporter/validator/build pipeline.
5. SIS runtime/security task for any deployed preview/public service.
6. exact pilot content fixtures and authority outcomes.

### Media/Telegram blockers

1. KOO review of `WEB__telegram-media-mvp-launch__KOO.md`.
2. KOD/SHD/SIS assignment for media-gateway implementation/integration/runtime.
3. KAN Telegram privacy/data-retention/moderation review.
4. RED channel derivative/discussion policy.
5. one-time Telegram channel/group/bot bootstrap before real API E2E.

## 17. SHD integration

Current approved SHD role should be reflected in future technical/public entity navigation.

For implementation work:
- KOD remains code owner;
- SIS remains infrastructure/deployment owner;
- SHD may perform cross-layer diagnostics, readiness checks, evidence packaging and integration verification when tasked.

SHD must not be treated as a replacement KOD/SIS owner.

## 18. Recommended next bounded pilot after KOO acceptance

Non-production only:

1. freeze one synthetic/public-safe fixture;
2. validate metadata contract;
3. build static preview artifact;
4. verify status labels and provenance;
5. run negative fixtures: candidate, blocked, superseded, secret-like;
6. perform readback from preview artifact/local served instance;
7. no Pages enablement yet;
8. return evidence package to KOO.

Telegram media-gateway Phase 0 can proceed in parallel after its separate KOO implementation authorization because it can use synthetic publication fixtures without production Telegram credentials.

## 19. Experience fixation

Идея → treat publication as conjunction of independent authorities rather than one magic `ready` flag.

Проба → reconcile ARH provenance, profile semantics, RED editorial lifecycle, KAN public/legal, SIS security, WEB representation and KOO release.

Результат → one object may be editorial-ready yet legally blocked, legally allowed yet editorial-unassessed, deployed yet unverified, or delivered externally without becoming source truth.

Успех → fail-closed rules become explicit enough for later schema/tests.

---
created_by: WEB
to_entity: koordinator
document_type: github-info-entry-stageB-synthesis-result
purpose: bounded non-production synthesis after accepted ARH/KAN/SIS/RED prerequisites
project_time: not_recorded_no_trusted_source