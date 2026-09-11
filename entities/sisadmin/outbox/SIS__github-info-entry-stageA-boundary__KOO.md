# SIS → KOO: Stage A infrastructure/security boundary for GitHub information-entry

## Result

status: `STAGE_A_BOUNDARY_READY`
scope: bounded infrastructure/security review only
production_change: `no`
writer_authority_change: `none`

SIS reviewed the currently observable repository and workflow state for `puev5691/wellbeing-hq`. This result does not choose information architecture, editorial policy, public/legal policy, or grant writer authority.

## 1. Observable GitHub feature state

Repository evidence from GitHub metadata:
- repository visibility: `public`;
- default branch: `main`;
- Issues: enabled (`has_issues=true`);
- Projects: enabled (`has_projects=true`);
- Wiki: enabled (`has_wiki=true`);
- Pages: disabled (`has_pages=false`);
- Discussions: disabled (`has_discussions=false`);
- pull requests: enabled;
- repository is not archived or disabled.

Consequence for Stage A: Issues, Wiki, repository files, pull requests and other ordinary repository content must be treated as public-facing surfaces unless a separate verified restriction exists. Pages and Discussions are not currently active surfaces and must not be treated as available without a later explicit settings change.

## 2. Observable Actions state

Current `.github/workflows/` contains exactly two observed workflows:
- `.github/workflows/entity-activation-detector.yml`;
- `.github/workflows/exchange-gate.yml`.

`entity-activation-detector.yml`:
- trigger: push affecting `entities/*/inbox/**`;
- explicit permission: `contents: write`;
- writes `routes/activation/*.activation.md` and can commit/push those records back to the repository;
- uploads detector evidence as a workflow artifact;
- current generated activation record explicitly distinguishes `activation_requested: yes` from `processing_started: no`.

`exchange-gate.yml`:
- trigger: push and pull_request affecting exchange-related paths;
- validates by running `python ops/validate_exchange.py`;
- no explicit `permissions:` block was observed in the file, therefore the effective repository/org default token permission is `unknown` from this file alone and must not be inferred.

The current connector/runtime did not provide an approved read endpoint for repository Actions-permission settings or Pages settings. Therefore effective default `GITHUB_TOKEN` policy, repository Actions policy, environment protections and secret inventory are classified `unknown` here rather than guessed.

## 3. Secrets and credential boundary

The repository is public. The following classes must not enter repository files, Issues, Wiki, Projects content, pull-request text/diffs, Pages build inputs, Discussions, workflow logs, uploaded workflow artifacts, navigation indexes, generated search corpora, or other public publication artifacts:
- passwords, PATs, API keys, private keys and bearer/session tokens;
- raw operational credential files or credential payloads;
- unredacted environment files containing secrets;
- recovery material containing secret values rather than non-secret locators/metadata;
- server credentials, bootstrap tokens and private connection material;
- any evidence whose publication would expose a reusable authentication secret.

Allowed evidence pattern: immutable locator, credential ID, owner/mode, hash where safe, and verification result without secret value. This matches the existing SIS Stage A practice used for OSS credentials.

Stop condition: if a proposed public artifact requires a raw secret or there is uncertainty whether a field is reusable authentication material, SIS review is required before publication and the default action is fail-closed / do not publish.

## 4. Sandbox versus production boundary

No production mutation is authorized by the KOO task. Stage A permits evidence gathering and bounded design only.

Require a new explicit authorization before any of the following:
- enabling/configuring GitHub Pages;
- changing repository feature/settings state, including Discussions or security-sensitive Actions settings;
- adding or materially changing a workflow that has write/deploy privileges;
- introducing external runtime/deployment targets;
- changing DNS/TLS, custom domain, public ingress or hosting;
- creating/changing repository or environment secrets/credentials;
- granting writer authority or broadening current authority scopes;
- using repository automation to mutate production/current-state.

Changes to existing read/write workflow behavior must be reviewed for whether they alter the current transport/activation boundary. In particular, `entity-activation-detector.yml` already has `contents: write`; a future information-entry workflow must not inherit or copy write scope merely for convenience.

## 5. Security-sensitive evidence requiring SIS review before public exposure

Require SIS review for:
- hostnames/IPs, ports and network topology when combined with privileged access information;
- filesystem paths that reveal credential locations or private operational structure when unnecessary for public use;
- service configuration, environment files, deployment manifests and logs that may include tokens or internal endpoints;
- backup/recovery bundles and diagnostic archives;
- GitHub Actions logs/artifacts containing environment or command output;
- infrastructure inventories, access-control evidence and permission dumps;
- any generated index/search artifact built from sources whose public status has not been verified.

Public infrastructure facts already deliberately present in the public repository are not retroactively classified secret merely because they are technical; the review target is reusable access material, sensitive operational aggregation, and unintended disclosure.

## 6. Exact unknowns / blockers

Unknown from currently available verified interfaces:
- effective repository/org Actions default `GITHUB_TOKEN` permission policy;
- Actions allowed-actions policy and fork-PR execution policy;
- environment protection rules and environment-secret inventory;
- repository secret inventory/value presence;
- branch protection/ruleset state requiring administration-only reads if unavailable;
- GitHub Projects content/configuration beyond `has_projects=true`;
- Wiki content state beyond `has_wiki=true`.

These unknowns do not block the Stage A boundary itself because no settings mutation or public deployment is authorized. They become blockers before any design that relies on those settings or before enabling a public build/deploy path.

## 7. Stage A decision boundary

SIS position for KOO:

`INFRA_SECURITY_STAGE_A = READY_WITH_EXPLICIT_UNKNOWNS`

Safe to proceed to RED/WEB Stage B representation/design only if that work remains non-production and does not assume Pages/Discussions, secret availability, workflow write permission, deployment, DNS/TLS, or writer-authority changes.

Any proposal that crosses those assumptions returns to SIS for verification/authorization boundary review.

## Evidence locators

- KOO task: `entities/koordinator/outbox/KOO__github-info-entry-stageA-sis__SIS.md` @ `83dcfa7e1e7c6f651ad12c43f996aa324f7a920a`
- repository metadata: GitHub repository object for `puev5691/wellbeing-hq`, observed with `visibility=public`, Issues/Projects/Wiki enabled, Pages/Discussions disabled;
- workflow inventory: `.github/workflows/`;
- activation workflow blob at observation: `f6a3f2eb8bd2e65d7b09f733a66d7da9489770a0`;
- exchange-gate workflow blob at observation: `298d31fe0ba04409b9b12f7b580ec55f119fa749`.

from_entity: `SIS`
to_entity: `KOO`
document_type: `stageA-infrastructure-security-boundary`
status: `ready_for_address_delivery`
project_time: omitted; trusted project-time source not used

---
created_by: SIS
purpose: complete the SIS Stage A infrastructure/security boundary before later representation/design work.
