# RED → KOO: GitHub information-entry editorial lifecycle/readiness

status: BOUNDED_RED_RESULT
stage: Stage B prerequisite
entity: RED / РЕДАКТОР
production_change_authorized: false
repository_settings_change_authorized: false
publication_authorized: false
project_source_created: no
project_time: omitted

## 1. Purpose

This result defines only the RED editorial lifecycle/readiness layer needed before WEB Stage B synthesis.

It does **not** replace:
- ARH source/provenance status;
- profile-owner semantic authority;
- KAN public/legal outcome;
- SIS security/infrastructure boundary;
- WEB representation/deployment checks;
- KOO/OPERATOR release authority where such authority is required.

The key rule is dimensional:

> **editorial-ready ≠ legal-allowed ≠ technically-publishable ≠ approved/current source-of-truth ≠ published.**

No single field should collapse these meanings.

## 2. Required status dimensions

A future public-entry object should preserve separate fields or equivalent evidence for at least:

1. **semantic/source status** — literal status from competent source/profile authority, e.g. approved/current, candidate/working, operational evidence, legacy/superseded, archive/historical, unknown/conflict;
2. **editorial status** — RED state defined below;
3. **public/legal outcome** — KAN or other competent authority outcome where required: allowed / allowed-with-conditions / blocked / unknown;
4. **technical publication state** — WEB/SIS layer, e.g. representable/previewable/deployed/readback-confirmed, using their competent vocabulary;
5. **release/acceptance state** — KOO/OPERATOR or named authority where a separate release decision is required.

Navigation, rendering or indexing must not upgrade any of these dimensions.

## 3. RED editorial states

### `editorial_unassessed`

RED has not evaluated the exact immutable version.

Meaning:
- no claim of editorial quality/readiness;
- may still be indexed as metadata if other authorities allow, but not represented as RED-reviewed content.

### `editorial_draft`

A text is under active editorial transformation.

Meaning:
- wording, structure, audience fit or claim framing may still change;
- public release is not implied;
- exact source/provenance must remain traceable.

### `editorial_reviewed`

RED has completed a substantive editorial pass on the exact version.

Meaning:
- readability, structure, terminology, claim framing and audience fit were checked;
- there may still be named editorial or non-editorial blockers;
- this is **not** yet a readiness claim.

### `editorial_ready`

RED has no remaining editorial blocker for the exact immutable version **within the stated intended use/audience**.

Required meaning:
- exact version identity is fixed;
- intended audience/purpose is known;
- source/provenance and literal semantic status are preserved;
- factual/project claims are traceable to available evidence or explicitly framed as opinion, hypothesis, fiction, candidate or uncertainty;
- wording does not silently upgrade candidate/research/history into current truth;
- known contradictions relevant to the public text are either resolved by competent authority or explicitly represented;
- terminology/readability/structure have passed the RED quality gate;
- required profile/content-owner review evidence is present when semantic subject-matter authority is needed;
- derivative restrictions or special handling are recorded when applicable.

`editorial_ready` means only: **RED would hand this exact version onward without another editorial pass being required by RED itself.**

It does not mean:
- legal/public use allowed;
- security-safe;
- technically deployable;
- approved as Project Source;
- publication/release authorized;
- actually published.

### `editorial_blocked`

RED cannot declare the exact version editorial-ready because a named blocker exists.

Typical blockers:
- unclear/conflicting source status affecting wording;
- missing intended audience/purpose;
- material factual claim unsupported by available source/evidence;
- unresolved conflict between current authority and proposed public wording;
- required profile review missing;
- identity/privacy/economic/legal ambiguity that changes wording and has not yet been bounded by competent input;
- exact version mismatch.

Blocker must be explicit and locator-based where possible. Do not replace uncertainty with plausible prose.

### `editorial_superseded`

This exact editorial version remains historical evidence but is replaced for current editorial use by a named newer version.

Required:
- `superseded_by` locator/version;
- old immutable artifact remains unchanged.

### `editorial_withdrawn`

The material is intentionally removed from active publication consideration.

Required:
- withdrawal reason or decision locator when available;
- prior publication/history is not erased;
- if already published, external withdrawal/correction is a separate media/WEB event.

## 4. Profile review and RED review are different

RED must not manufacture semantic/profile approval.

A profile owner may establish:
- factual correctness in its domain;
- current technical/project state;
- semantic authority over its own result.

RED establishes:
- clarity;
- faithful framing of that status;
- audience suitability;
- consistency of claims with supplied evidence;
- publication-text structure and language.

Recommended evidence fields:
- `profile_review_status`;
- `profile_review_locator`;
- `editorial_status`;
- `editorial_result_locator`.

If profile review is required but absent, RED fails closed rather than using fluency as a substitute for authority.

## 5. Editorial quality gate before WEB handoff

For `editorial_ready`, RED checks at minimum:

1. exact immutable content identity is known;
2. intended audience and purpose are explicit enough to edit against;
3. source/provenance locator exists or absence is explicitly classified;
4. literal source/project status is preserved;
5. fact / interpretation / hypothesis / fiction / candidate / unknown are not silently merged;
6. no unsupported upgrade such as draft → official position or test → success;
7. title, lead and summary do not overclaim beyond the body;
8. terminology is understandable for intended audience; unavoidable technical terms are explained at first use when needed;
9. structure supports reading and does not bury the required action/meaning under metadata;
10. obvious language/copy defects are resolved to the chosen quality level;
11. known privacy, rights, financial/economic, security or authority sensitivities are represented as explicit downstream gates, not silently assumed solved;
12. current version has not been superseded during review.

Failure of items 1–6 or 12 blocks readiness. Items 7–10 are editorial defects to correct. Item 11 may allow RED to reach `editorial_ready` only if the exact downstream gate is explicitly preserved; it still blocks public release until the competent gate is satisfied.

## 6. RED → WEB handoff

A RED handoff to WEB must identify the exact artifact and must not rely on a mutable "latest" notion.

Minimum handoff evidence:
- canonical/content locator;
- immutable commit/blob or equivalent version identity;
- title / content class;
- intended audience/purpose;
- literal semantic/source status;
- RED editorial status;
- RED review/result locator;
- profile review locator/status when required;
- known KAN/SIS/authority outcomes or `unknown`;
- derivative/syndication restrictions when applicable;
- supersedes/superseded_by relation when applicable.

### Handoff classes

#### `handoff_for_preview`
WEB may create non-production representation/preview if its own boundaries allow.

This does not imply public release.

#### `handoff_for_public_representation`
RED may issue this only when:
- exact artifact is `editorial_ready`;
- all named non-editorial release gates required for that object have verified outcomes allowing the intended public representation;
- no known conflict/version mismatch exists.

Even then, WEB/SIS must apply their own technical/security checks and the actual release authority remains separate if project process requires one.

## 7. Update / supersede / archive / withdrawal

### Ordinary update

Any semantic text change creates a new version identity.

Editorial readiness does **not** automatically transfer to the new version.

A new version begins at least as `editorial_draft` or `editorial_unassessed`, except for purely mechanical byte/format operations that RED/WEB can verify as meaning-preserving under an explicit transformation rule.

### Supersede

When a newer editorial version replaces an older one:
- preserve both immutable versions;
- set old → `editorial_superseded`;
- record `superseded_by`;
- current navigation should prefer the newer accepted/current representation without hiding history.

### Archive

Archive is primarily a preservation/navigation class, not an editorial approval.

Archived material retains its literal editorial status plus archive/historical source status. Archive must never be rendered as current merely because it is readable.

### Withdrawal

Withdrawal stops active release/use of that version.

If already externally published:
- canonical/public representation requires WEB/media correction or withdrawal record;
- syndication targets require their own correction/withdrawal handling;
- history remains preserved.

## 8. Derivative text rules

Summaries, teasers, translations and substantive abridgements are **new editorial artifacts** linked to a parent source.

They do not automatically inherit `editorial_ready`.

Required for each derivative:
- parent locator and parent immutable version;
- derivative type;
- intended channel/audience;
- exact derivative version;
- RED status.

### Summary

Must preserve:
- source status;
- uncertainty;
- blockers;
- scope limits;
- claim strength.

A summary that turns "candidate", "test", "planned" or "unknown" into "is", "works" or "approved" fails editorial review.

### Teaser

May compress aggressively, but cannot:
- make a stronger factual/economic/legal claim than the source;
- use a risky fragment detached from its limiting context;
- present a historical/fictional passage as current project promise.

### Translation

Translation is a semantic derivative, not a neutral transport.

It requires editorial review sufficient to confirm that:
- status vocabulary remains correct;
- authority/legal/economic qualifiers survive;
- technical terms do not acquire stronger meaning.

Machine translation starts as `editorial_draft` until reviewed.

### Exact excerpt

Even verbatim excerpts require context check if isolation could reverse or strengthen meaning. Exact quotation does not guarantee safe representation.

## 9. Distinction among three commonly confused outcomes

### Editorial-ready

Owner: RED.

Question answered:
> Is this exact text sufficiently clear, faithful and properly framed for its intended presentation?

### Legal-allowed

Owner: KAN / competent legal-public authority.

Question answered:
> May this material be publicly used in the intended way under the current bounded legal/privacy/rights/economic rules?

### Technically-publishable / represented

Owner: WEB/SIS within their scopes.

Question answered:
> Can this exact approved input be built/deployed/rendered/read back safely on the selected surface?

These outcomes must remain independently visible.

A public release path requires the conjunction of all **applicable** gates, not substitution of one for another.

## 10. Fail-closed rules

RED does not declare `editorial_ready` when:
- source/current status relevant to wording is unknown or conflicting;
- exact artifact/version cannot be established;
- required profile review is missing;
- a material claim cannot be traced or honestly framed as uncertain;
- supplied sources contradict each other on a point necessary to the public text and no competent resolution exists.

If RED is editorial-ready but KAN/SIS/release authority is unknown, the object may retain `editorial_ready` **but public release remains blocked**.

WEB must not interpret missing editorial status as ready.

Suggested representation for missing/conflicted editorial state:
- `editorial_status: unknown` or `editorial_blocked`;
- `public_representation: blocked` until RED or competent authority resolves it.

## 11. What RED explicitly does not authorize

This result does not authorize RED or WEB to:
- promote candidate/draft/research to approved/current;
- create or modify Project Sources;
- make legal/privacy/licensing determinations;
- certify security safety;
- enable Pages/Discussions;
- initialize Wiki;
- create a public-web repository;
- change repository settings;
- deploy production;
- create credentials/secrets;
- broaden writer permissions;
- publish fundraising/token/investment offers;
- publish personal/sensitive information without the required gate;
- auto-import arbitrary repository content;
- treat editorial readiness as publication approval.

## 12. Minimal metadata contribution from RED

For future WEB metadata synthesis, RED recommends the following editorial fields as **candidate implementation inputs**, not canon:

- `editorial_status`;
- `editorial_result_locator`;
- `intended_audience`;
- `intended_purpose`;
- `content_class`;
- `profile_review_status`;
- `profile_review_locator`;
- `derivative_of`;
- `derivative_type`;
- `superseded_by`;
- `editorial_blocker` or blocker locator.

These fields must coexist with ARH/KAN/SIS fields rather than overwrite them.

## 13. Current unresolved blockers

For this bounded RED result itself:
- no editorial design blocker remains;
- KOO acceptance/revision remains separate;
- WEB Stage B remains blocked until KOO accepts or otherwise competently handles this result and issues the next bounded WEB task;
- production/publication/settings changes remain unauthorized.

## Experience fixation

**Идея:** define "ready" without letting one convenient status swallow source authority, law, security and deployment.

**Проба:** separate source status, RED editorial status, KAN outcome, WEB/SIS technical state and release decision.

**Результат:** RED can give WEB a precise handoff contract while preserving upstream/downstream authority boundaries.

**Успех:** `editorial_ready` becomes useful because it is narrow: it says the text is ready **as text**, not that the world has approved everything around it.

**Фиксация:** future public-information objects should carry multiple orthogonal status dimensions; never infer publication authority from editorial polish.

---
created_by: RED / РЕДАКТОР
purpose: bounded editorial lifecycle/readiness input before WEB Stage B synthesis
