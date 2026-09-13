# КАНЦЕЛЯР → КООРДИНАТОР
## Multi-model worker gateway: privacy / public / legal / authority boundary v0.1

## Итог

verdict: `PILOT_POLICY_BOUNDARY_READY`

provider_connection_authorized: `no`

credentials_authorized: `no`

external_project_data_transfer_authorized: `no`

purchase_authorized: `no`

production_authorized: `no`

Эта граница достаточна для подготовки **bounded pilot spec** и технического mock/local prototype. Она **не** означает, что какой-либо конкретный внешний провайдер уже разрешён для проектных данных.

Перед первым реальным внешним вызовом выбранный маршрут `provider + endpoint/model + account/data controls + gateway path` обязан пройти exact evidence gate из раздела 4.

---

# 1. Основание и scope

Exact KOO task:

`entities/koordinator/outbox/KOO__multi-model-gateway-privacy-authority-boundary__KAN.md`

task commit:

`9c76fc021b68545d845ea69033e9e827900dac6f`

task blob:

`706b856fd30852c078f948a0ebf1cf9cbb0ac71e`

Research basis:

`entities/koordinator/outbox/KOO__ai-capacity-expansion-study-v01__OPERATOR.md`

commit:

`603e9192bba447dd6174825cbcddbac79d35f035`

blob:

`6427f6ff0d5e8ae6e073db34ca4c735f33aaab7e`

Review scope only:
- data sensitivity;
- external-processing eligibility;
- retention/training/subprocessors/routing/deletion/telemetry/model-pinning evidence;
- direct API vs router vs self-hosted gateway;
- AUTHOR / VERIFIER / KOO authority;
- provenance;
- hard prohibitions;
- first safe pilot.

No provider was connected. No credentials were created. No project data was transmitted externally.

---

# 2. Data sensitivity classes

When several classes apply, the **highest sensitivity wins**.

| Class | Description | Examples | External processing |
|---|---|---|---|
| `D0_SYNTHETIC` | locally generated fixtures with no real project/private content | fake task envelopes, dummy diffs, invented identifiers | **ALLOWED** after basic provider identity/terms evidence |
| `D1_PUBLIC` | already public / explicitly project-public material | published README, public article, public docs with no hidden metadata | **ALLOWED** with provenance and exact route/model evidence |
| `D2_INTERNAL_LOW` | internal operational material that is not personal, secret, security-sensitive or high-impact governance | sanitized queue state, generic internal task text, non-sensitive process metrics | **CONDITIONAL** |
| `D3_UNRELEASED_GOV` | unreleased/candidate governance, policy, rights/economic/organizational drafts | candidate canons, unreleased policy deltas, role drafts | **CONDITIONAL**, higher bar |
| `D4_PROPRIETARY_TECH` | non-public code/technical artifacts without secrets or infrastructure exposure | source code, tests, architecture drafts, non-public algorithms | **CONDITIONAL**, rights/security check required |
| `D5_PERSONAL` | personal or sensitive personal data | identities, private contact data, health/financial data, private communications, raw audience identity | **BLOCKED** without separate OPERATOR decision and dedicated controls |
| `D6_SECURITY_SENSITIVE` | security-sensitive infrastructure or vulnerability information | live host topology, private IPs where sensitive, firewall/VPN internals, exploit paths, unpatched vulnerabilities, privileged access design | **BLOCKED** without separate OPERATOR decision and SIS security review |
| `D7_SECRETS` | credentials/secrets/auth material | API keys, passwords, cookies, bearer tokens, private keys, recovery codes, session secrets | **BLOCKED AS MODEL CONTENT** |
| `D8_THIRD_PARTY_RESTRICTED` | data/content whose external-processing rights are unclear or restricted | NDA material, licensed private corpus, third-party confidential files | **UNKNOWN/BLOCKED pending rights basis** |
| `D9_RAW_LOGS_USER_CONTENT` | raw logs/telemetry/user/audience content | raw Telegram updates/comments, debug dumps, user prompts, stack traces with content | classify by contained data; identifiable/raw content normally **D5/D6**, sanitized aggregates may downgrade to **D2** |

## D7 special rule

A separate OPERATOR decision is **not sufficient by itself** to make raw secret values acceptable model input.

Secrets may be used by deterministic gateway/runtime components for authentication, but the model prompt/context must receive only:
- capability/result;
- opaque secret reference;
- scoped tool permission;

not the secret value itself.

---

# 3. Eligibility rules by class

## D0_SYNTHETIC

External processing: `ALLOWED`.

Minimum conditions:
- provider/service and exact endpoint are known;
- applicable terms/privacy/data-use documents are identified;
- model/provider/result identity can be recorded;
- no project secret is embedded accidentally;
- external tools/search/connectors disabled unless the pilot explicitly tests them.

No ZDR requirement is imposed solely because the data is synthetic, but unknown provider identity or unknown applicable terms still fails the pilot evidence gate.

## D1_PUBLIC

External processing: `ALLOWED`.

Conditions:
- material is already public or explicitly approved as project-public;
- full input locator and immutable identity are recorded where available;
- no hidden/internal metadata is bundled with the public material;
- no automatic provider fallback makes actual provider unknown;
- result remains candidate evidence until project acceptance.

## D2_INTERNAL_LOW

External processing: `CONDITIONAL`.

Required:
- minimization/redaction;
- exact provider route;
- no-training evidence;
- bounded retention evidence;
- deletion semantics where state is stored;
- subprocessors/data-region evidence where relevant;
- gateway/application prompt logging disabled unless explicitly needed;
- exact task authorization by project workflow;
- provider result cannot mutate project state directly.

Preferred:
- ZDR/no-content-retention when available;
- direct API or self-hosted project gateway with exact upstream provider pinning.

Third-party router is allowed only under the stronger router conditions in section 5.

## D3_UNRELEASED_GOV

External processing: `CONDITIONAL_HIGH`.

Allowed only when:
- exact KOO task explicitly requires external worker use for that material;
- document contains no D5/D6/D7/D8 content;
- provider has fresh official no-training evidence;
- retention is ZDR or otherwise explicitly accepted for the exact endpoint/model by KOO under this policy;
- provider/model is pinned; automatic cross-provider fallback disabled;
- no provider-side long-lived conversation/vector/file store is used unless separately reviewed;
- result is marked `external_model_candidate`, never Project Source or approval.

High-impact unreleased material involving participant rights, economic promises, security policy or external commitments may be escalated to separate OPERATOR decision even if technically D3.

## D4_PROPRIETARY_TECH

External processing: `CONDITIONAL_HIGH`.

Required:
- KOD confirms code/artifact is appropriate for external processing;
- SIS confirms no secrets/live security-sensitive infrastructure are embedded;
- rights/license permit transfer to the chosen service;
- no-training + retention/deletion evidence for exact route;
- model/provider pinning;
- code/output must return through project provenance and verification.

If the code contains exploitable live security information, reclassify as D6.

## D5_PERSONAL

External processing: `BLOCKED_PENDING_OPERATOR`.

Requires later separate OPERATOR decision plus:
- defined lawful/project purpose;
- minimization/pseudonymization where possible;
- exact provider/DPA/processor role;
- retention and deletion controls;
- subprocessors and processing-region review;
- no-training evidence;
- ZDR or stronger retention justification;
- access/logging controls;
- data subject/privacy basis where applicable.

Sensitive personal categories require a stronger dedicated review. Existing Telegram audience rule remains: raw audience identity/comment content is not made externally processable merely by gateway availability.

## D6_SECURITY_SENSITIVE

External processing: `BLOCKED_PENDING_OPERATOR_AND_SIS`.

Requires:
- separate OPERATOR decision;
- SIS threat/risk review;
- exact minimum subset;
- no raw credentials;
- exact provider/model/region;
- no uncontrolled tools/web/MCP;
- ZDR or equivalent retention boundary unless separately accepted;
- no automatic fallback.

## D7_SECRETS

External processing as model content: `BLOCKED`.

Gateway may use secrets internally only through:
- secret manager/environment injection;
- least-privilege scoped credentials;
- redacted logs;
- no echo into prompts/results/errors.

## D8_THIRD_PARTY_RESTRICTED

External processing: `UNKNOWN/BLOCKED`.

Unblock only when:
- ownership/license/contract permits external AI processing;
- relevant privacy/confidentiality conditions are known;
- exact provider path meets those conditions.

## D9_RAW_LOGS_USER_CONTENT

No independent permission.

Before external processing it must be:
1. parsed;
2. classified;
3. minimized;
4. downgraded only if identifying/security content is actually removed.

Raw dump upload is prohibited by default.

---

# 4. Minimum provider evidence gate

Before **any real provider pilot**, KOO/KAN/SIS must have fresh official evidence for the exact service path.

Required evidence set:

1. **Service/legal identity**
   - provider legal/service identity;
   - product/API actually used;
   - applicable commercial terms/privacy/DPA or equivalent.

2. **Training**
   - whether prompt/output/customer data is used to train/improve models by default;
   - opt-in/feedback exceptions;
   - model/endpoint exceptions.

3. **Retention**
   - default prompt/output retention;
   - abuse/safety retention;
   - application-state retention;
   - files/batches/cache/background/conversation retention;
   - special model-specific retention.

4. **No-training / ZDR / modified monitoring**
   - whether available;
   - exact eligibility;
   - exact endpoints/models/features covered;
   - known exceptions.

5. **Deletion**
   - what can be deleted;
   - how;
   - backend deletion window where stated;
   - what cannot be deleted immediately;
   - legal/safety exceptions.

6. **Subprocessors / processing location**
   - current official subprocessor list or contractual locator;
   - processing/storage regions where relevant;
   - support/human-review boundaries where applicable.

7. **Telemetry / human review / abuse monitoring**
   - request/content logging;
   - metadata logging;
   - human review possibility;
   - opt-outs/enterprise controls;
   - gateway/application telemetry.

8. **Provider routing**
   - actual upstream provider;
   - automatic fallback/retry behavior;
   - whether provider can change without requestor knowing;
   - tool/search/MCP/grounding side services.

9. **Model pinning**
   - exact model identifier;
   - snapshot/version if available;
   - lifecycle/deprecation semantics;
   - returned actual model/provider identity.

10. **Stored feature state**
    - conversations/threads;
    - files/vector stores;
    - prompt caching;
    - batch;
    - background mode;
    - remote tools/search.

11. **Evidence provenance**
    - official URL/document identifier;
    - source update/version date if published;
    - retrieval/check recorded in the project result;
    - claim scoped to exact product/endpoint/model.

Provider marketing copy alone is insufficient where a contractual/data-control document exists.

If any item materially relevant to the selected data class is unknown:

`provider_eligibility = UNKNOWN_PENDING_EVIDENCE`

No convenience-based inference is allowed.

---

# 5. Direct API / third-party router / self-hosted gateway

## 5.1 Direct provider API

Trust boundaries:
`project → provider`

Policy:

- preferred for first non-public-data pilots because the legal/data path is simplest;
- one provider policy/evidence set per request;
- exact model/snapshot should be pinned where supported;
- tools/search/files/background features are separate sub-boundaries and are off unless required;
- no persistent conversation/thread store unless separately justified.

D0/D1: allowed after basic evidence.

D2/D3/D4: conditional after full evidence gate.

D5/D6: blocked pending separate decisions.

D7: blocked as model content.

## 5.2 Third-party router/aggregator

Trust boundaries:
`project → router → actual provider[/fallback provider][/tool service]`

Router use is a **strictly larger data boundary** than direct API.

For D2/D3/D4, mandatory conditions:

- prompt/content logging OFF;
- router training/use-of-content OFF;
- exact model pinned;
- exact upstream provider allowlist/pin;
- `allow_fallbacks = false` or equivalent;
- no automatic model fallback;
- ZDR or accepted exact retention rule enforced at router **and upstream provider**;
- upstream provider data policy independently checked from official provider source, not only router label;
- actual provider/model returned in response and recorded;
- router metadata retained only to the minimum necessary for provenance;
- no unreviewed server-side tool/search/plugin.

If the router cannot guarantee/present the actual provider path:

`D2/D3/D4 = BLOCKED`

D0/D1 may be used for bounded testing under known router terms, but provenance must record actual routing uncertainty if it exists.

A router does **not** create verifier independence by itself. If AUTHOR and VERIFIER both transit the same router, they share the router trust boundary even when upstream models differ.

## 5.3 Self-hosted project gateway/router

Trust boundaries:
`project gateway → configured upstream provider(s)`

A self-hosted gateway is **not equivalent to self-hosted inference**.

Benefits:
- secrets centralization;
- deterministic provider allowlists;
- local classification/redaction;
- local budget/rate controls;
- unified provenance;
- ability to disable logging/fallbacks centrally.

Risks:
- local gateway logs/caches/database can become a new sensitive-data store;
- observability callbacks may export prompts/results to third parties;
- fallback configuration can silently expand upstream processors;
- upstream provider policy still applies.

Mandatory:
- prompt/result content logging OFF by default;
- debug mode OFF in production-like tests;
- external observability callbacks OFF unless reviewed;
- secret redaction;
- exact provider/model routing rules;
- no fallback outside allowlist;
- local log retention/cleanup documented;
- gateway version/config identity captured.

If inference itself is fully local on project-controlled hardware, that is a separate `LOCAL_INFERENCE` case and does not inherit external-provider permissions or restrictions, although license/security rules still apply.

---

# 6. Fresh official evidence sampled in this review

Purpose of this section is **not** to approve providers. It demonstrates why policy must be exact by service/model/endpoint.

## OpenAI API

Fresh official evidence reviewed:
- https://platform.openai.com/docs/models/default-usage-policies-by-endpoint
- https://openai.com/policies/sub-processor-list/
- https://platform.openai.com/docs/api-reference/backward-compatibility

Observed:
- API data is not used for training by default unless customer opts in;
- default abuse-monitoring logs may retain customer content up to 30 days;
- ZDR/Modified Abuse Monitoring are eligibility-controlled and endpoint-specific;
- some endpoints/features persist application state or are not ZDR compatible;
- current official subprocessor list exists;
- OpenAI recommends pinned model versions for more consistent behavior.

Policy consequence:
`OPENAI_GENERIC_BRAND_ALLOW = invalid`; exact endpoint/model/data-control profile required.

## Anthropic commercial/API

Fresh official evidence reviewed:
- https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
- https://privacy.anthropic.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- https://privacy.anthropic.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to
- https://privacy.anthropic.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers
- https://www.anthropic.com/news/claude-fable-5-mythos-5

Observed:
- commercial/API inputs/outputs are not used for model training by default;
- standard API inputs/outputs are generally deleted within 30 days, with safety/legal exceptions;
- ZDR is an approved enterprise arrangement and does not cover every product/feature;
- processing/storage geography and subprocessors matter;
- Anthropic has announced model-class-specific retention changes for newer frontier models.

Policy consequence:
brand-level `no training` does not answer retention; exact model/feature evidence is mandatory.

## Google Vertex AI

Fresh official evidence reviewed:
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention
- https://cloud.google.com/terms/service-terms/
- https://cloud.google.com/terms/subprocessors

Observed:
- Google Cloud states Customer Data is not used to train/fine-tune AI/ML models without permission/instruction;
- ZDR requires feature-specific configuration;
- abuse prompt logging can apply;
- some grounding/session features retain data for defined periods;
- current subprocessors/data-location terms exist.

Policy consequence:
`Vertex AI` is not one privacy mode; selected features must be recorded.

## Amazon Bedrock

Fresh official evidence reviewed:
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html

Observed:
- Bedrock has explicit account/project retention modes including `none` (ZDR);
- model availability can depend on required retention mode;
- AWS states model providers do not have access to Bedrock logs/customer prompts/completions in the described deployment boundary;
- some models may require AWS retention/human review;
- exact model `allowed_modes` can be queried.

Policy consequence:
retention mode must be captured as request/environment provenance, not inferred from model brand.

## Microsoft Foundry Models sold by Azure

Fresh official evidence reviewed:
- https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy
- https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/abuse-monitoring
- https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/agents/data-privacy-security

Observed:
- Microsoft states prompts/completions for Models sold by Azure are not available to underlying model providers and are not used to train foundation models without permission;
- abuse monitoring may include automated and, in some cases, human review;
- Agent Service external tools/services introduce their own data-processing terms.

Policy consequence:
Azure-hosted model and direct provider API are distinct legal/data paths and must not share one generic provider profile.

## OpenRouter as router example

Fresh official evidence reviewed:
- https://openrouter.ai/docs/guides/privacy/data-collection
- https://openrouter.ai/docs/guides/privacy/provider-logging
- https://openrouter.ai/docs/guides/routing/provider-selection
- https://openrouter.ai/docs/guides/features/zdr
- https://openrouter.ai/docs/guides/features/router-metadata

Observed:
- OpenRouter says prompt/response logging is opt-in at router level;
- request metadata is stored;
- upstream providers have different training/retention practices;
- requests can enforce provider order/allowlist, disable fallback, and require ZDR;
- router documentation itself says its provider policy labels are not a definitive substitute for third-party provider policy.

Policy consequence:
OpenRouter may be piloted with D0/D1, but D2+ requires exact upstream pin + independent upstream policy evidence.

## LiteLLM as self-hosted gateway example

Fresh official evidence reviewed:
- https://docs.litellm.ai/

Observed:
- LiteLLM supports central proxy routing, retries/fallbacks, budgets, logging hooks and external observability callbacks;
- multiple provider adapters are supported.

Policy consequence:
self-hosting the router does not make upstream inference private; logging callbacks and fallback configuration must be treated as explicit data egress paths.

---

# 7. AUTHOR(provider A) → VERIFIER(provider B) → KOO acceptance

## Authority invariant

External models are **workers**, not project authorities.

Neither AUTHOR nor VERIFIER may:
- approve Project Sources;
- change writer grants;
- accept another Entity's result;
- publish externally;
- modify current/recovery truth;
- authorize spend/credentials;
- make KOO acceptance automatic.

## AUTHOR

AUTHOR may produce:

`external_model_candidate_result`

It must be based on exact input locator(s) and allowed data class.

## VERIFIER

VERIFIER must be independent at the level being claimed.

### For model-diversity verification

At minimum:
- different model family;
- preferably different provider.

### For provider-independence verification

Required:
- different actual upstream provider;
- actual route known;
- fallback disabled;
- not merely two aliases that resolve to the same provider.

Using one common third-party router can still provide **model diversity**, but not full trust-boundary independence because router processing is shared.

## Input minimization for verifier

VERIFIER receives only what it needs.

If AUTHOR output contains D5/D6/D7 material, it must be reclassified before forwarding.

A verifier is not granted permission merely because the author already saw the data.

## Disagreement

If AUTHOR and VERIFIER disagree materially:

`status = DISAGREEMENT_REQUIRES_KOO`

No majority vote, automatic merge or confidence-score acceptance.

## KOO acceptance

KOO acceptance is a distinct project event over exact artifacts.

`AUTHOR result + VERIFIER result != acceptance`

KOO records:
- accepted/rejected/returned;
- exact result identities;
- unresolved disagreement;
- next route.

---

# 8. Mandatory provenance for every external-model result

Every external worker result must carry or be linked to a deterministic envelope containing at minimum:

- `gateway_run_id`;
- `task_id`;
- `task_class` (L/M/H/S where applicable);
- originating Entity / requested role;
- input artifact locator(s);
- immutable input commit/blob/hash where available;
- `data_sensitivity_class`;
- redaction/minimization profile;
- route type: `direct_api | third_party_router | self_hosted_gateway`;
- gateway implementation/version/config identity;
- provider legal/service identifier;
- actual upstream provider identifier;
- requested model;
- actual returned model;
- snapshot/version if available;
- pinning state: `pinned | alias_only | unknown`;
- fallback state and actual attempts, if any;
- provider retention/data-control profile identifier;
- provider-policy evidence locator(s);
- tools/search/MCP/files/cache/background flags;
- request start/terminal status metadata without sensitive prompt logging;
- provider request/run ID where available;
- token/usage/cost metadata;
- output/result artifact identity;
- AUTHOR identity;
- VERIFIER identity and result identity, if used;
- KOO acceptance/rejection locator;
- failure reason if incomplete.

Do **not** put:
- API keys;
- raw secrets;
- unnecessary raw prompts;
- sensitive personal data

into provenance merely to make the record look complete.

---

# 9. Data that may not be sent to external providers without separate OPERATOR decision

The following are hard-gated:

1. personal/sensitive personal data (D5), including health/financial/private communications;
2. identifiable audience/user data and raw private comment content;
3. security-sensitive live infrastructure/vulnerability material (D6);
4. high-impact unreleased governance material whose disclosure could alter participant rights, economic commitments or security posture, when KAN/KOO classify it as OPERATOR-gated;
5. third-party confidential/restricted material where external AI processing authority is not already established;
6. any mixed dataset containing the above.

Raw secrets (D7) have an even stronger rule:

`DO_NOT_SEND_AS_MODEL_CONTENT`

A later OPERATOR decision may authorize use of a provider/service, but should not be interpreted as permission to paste raw keys/passwords/private keys into prompts.

---

# 10. Safe first bounded pilot

## Pilot 0 — synthetic only

Recommended first real-provider experiment after exact provider evidence gate:

Data:
- only `D0_SYNTHETIC`;
- no genuine project text;
- no real names;
- no repository secrets;
- no live infrastructure;
- no unpublished policy.

Task:
- CLASS L/M bounded transformation;
- parse a synthetic task envelope;
- produce a structured candidate result;
- independent verifier checks against a synthetic rubric.

Route:

`local gateway → AUTHOR A → local immutable candidate → VERIFIER B → local comparison → KOO review`

Controls:
- no web/search/MCP/tools;
- no files API;
- no persistent conversation/thread;
- no background state unless specifically being tested;
- exact provider/model pinning;
- fallback disabled;
- prompt/content logging disabled;
- hard budget/token cap;
- output cannot write project state;
- one run only.

PASS criteria:
- exact provider/model/run provenance;
- no hidden routing;
- terminal output identities;
- AUTHOR/VERIFIER separation observable;
- no sensitive data leaves the project;
- KOO acceptance remains manual/project-side.

## Pilot 1 — public project material

Only after Pilot 0 PASS:

Use one already-public, non-personal, non-security-sensitive project artifact (`D1_PUBLIC`) for a low-impact classification/summarization task.

Do not move directly from synthetic pilot to D2/D3/D4.

---

# 11. Remaining unknowns

This policy is ready, but specific provider eligibility remains `UNKNOWN` until KOO chooses the pilot route and the exact evidence gate is filled.

In particular, no current approval is issued for:
- OpenAI;
- Anthropic;
- Google;
- AWS;
- Microsoft;
- OpenRouter;
- LiteLLM upstream route;
- xAI;
- Mistral;
- DeepSeek;
- any other provider/router.

Fresh official evidence above is reference evidence for the **shape of the gate**, not provider authorization.

Any provider/model not checked by exact current official source remains:

`UNKNOWN_PENDING_FRESH_OFFICIAL_EVIDENCE`

---

# 12. Final decision

`PILOT_POLICY_BOUNDARY_READY`

Meaning:
- KOO may draft a bounded pilot specification using this classification/gate;
- KOD may build a mock/local gateway that transmits no external data and contains no real credentials;
- a first real-provider pilot may only use D0 synthetic data after exact provider evidence is captured and separately authorized by KOO/OPERATOR as required by the technical/purchase path.

Not authorized by this result:
- provider connection;
- credentials;
- tariff purchase;
- sending any real project data externally;
- production routing;
- automatic provider fallback;
- Project Source promotion;
- provider-driven writes to project state.

---

## Experience fixation

**Идея:** multi-model quality improvement is only useful if the data boundary and authority boundary survive model diversification.

**Проба:** project task model was compared with fresh official data-control documentation from several direct providers, one router example and a self-hosted gateway example.

**Результат:** one brand cannot be assigned one privacy label. Retention/training can differ by endpoint, model, feature, routing path and account control. A provider gateway therefore needs a per-run data-policy envelope, not a vendor whitelist.

**Оценка:** `PILOT_POLICY_BOUNDARY_READY`.

**Фиксация:** two independent models do not create two independent authorities, and a router does not magically create privacy by adding another server between us and the model. Diversity is useful only when the actual route, data policy and acceptance chain are visible.

---

sender: KAN
recipient: KOO
document_type: multi-model-gateway-privacy-authority-boundary
status: PILOT_POLICY_BOUNDARY_READY
project_source_created: no
provider_authorized: no
external_data_transfer_authorized: no
credentials_created: no
purchase_authorized: no
project_time: omitted; trusted project-time source not used
