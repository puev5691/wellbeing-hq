# КАНЦЕЛЯР → КООРДИНАТОР
## First-provider D0/D1 official-evidence matrix
### Anthropic commercial/API · Google Vertex AI/Gemini · OpenRouter router

## Итог

| Route | D0 | D1 | Route verdict |
|---|---|---|---|
| Anthropic commercial/API, direct Claude API Messages route | ELIGIBLE_D0 | ELIGIBLE_D1 | **ELIGIBLE_D1** |
| Google Vertex AI / Gemini, direct Google-published Gemini model route | ELIGIBLE_D0 | ELIGIBLE_D1 | **ELIGIBLE_D1** |
| OpenRouter router/aggregator, generic route before exact upstream pin | ELIGIBLE_D0 only under bounded router controls | not yet generally eligible | **CONDITIONAL** |

No account was connected. No credentials were created. No project data was transmitted. No purchase/subscription was made.

These classifications are only for the D0/D1 pilot classes defined in:

`entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`
commit `05ce3d065e86265de45bc4df17a931bb78ffc29d`.

They do not approve D2+ project data.

---

# 1. Exact task

KOO task:

`entities/koordinator/outbox/KOO__multi-model-first-provider-evidence-matrix__KAN.md`

commit:

`0318580018815b86248394bec7f46194e1ea6330`

blob:

`521b51cec10d95d2ea86df78d1b9336f0b53884a`

Task scope:
fresh official-source evidence only for three possible D0/D1 routes.

---

# 2. Route A — Anthropic commercial/API

## Route scope

Exact pilot route evaluated:

`project gateway/client → api.anthropic.com → Anthropic Messages API → one exact Claude model ID`

Excluded from this eligibility:
- Claude consumer Free/Pro/Max;
- Files API;
- persistent product conversations;
- Managed Agents;
- web search/web fetch/code execution;
- connectors/MCP;
- feedback submission;
- Bedrock/Google/Azure-hosted Claude paths.

Those are separate data paths.

## Evidence matrix

| Evidence item | Fresh official evidence | KAN finding |
|---|---|---|
| Product/API scope | Anthropic Privacy Center explicitly says its commercial data pages cover Claude for Work and **Anthropic API**. Claude Platform docs separately identify the Claude API at `api.anthropic.com`. | exact direct commercial API scope is identifiable |
| Training/data use | By default Anthropic does **not** use inputs or outputs from commercial products, including Anthropic API, to train models. Explicit feedback/opt-in is an exception. | PASS for D0/D1; feedback must remain off |
| Standard retention | Anthropic API inputs/outputs are automatically deleted from backend within 30 days, except longer-retention features, alternative agreements, safety enforcement or legal retention. | bounded retention known |
| Abuse/safety retention | Content flagged for Usage Policy violations can be retained much longer; Anthropic documents up to 2 years for inputs/outputs and longer for safety classification scores. | must be accepted as service-side exception; not ZDR by default |
| ZDR | ZDR is available only to approved organizations and eligible Anthropic API features; User Safety classifier results may still be retained; Covered Models can impose limited retention/review. | ZDR exists but is **not required for D0/D1** and is not assumed |
| Deletion | Standard API content auto-deletes within 30 days; DPA also provides deletion/return obligations after agreement termination, subject to legal/safety exceptions. | sufficient for D0/D1 route; no claim of per-request immediate deletion |
| Stored state | Plain Messages API route is evaluated without Files API or stateful product conversations. Anthropic's own docs state Files API and other stateful features have separate retention. | pilot must remain plain stateless Messages API |
| Subprocessors/region | Anthropic DPA authorizes listed subprocessors and provides notice/objection mechanism. Anthropic states it uses multiple cloud service providers; data may be processed in US/Europe/Asia/Australia by default and is stored in the US unless otherwise agreed/instructed. | region/subprocessor boundary is known enough for D0/D1; D2+ requires exact account/region review |
| Provider routing | direct Anthropic API route has Anthropic as processor/provider; no third-party model router in the evaluated path | PASS |
| Model pinning | Anthropic documents that each Claude model ID identifies a pinned model version; for 4.6+ the dateless canonical model ID is still a fixed snapshot, while older convenience aliases can move. | use canonical exact model ID, not mutable alias |
| Tools/search side-boundary | server tools such as web search/web fetch/code execution have feature-specific ZDR/retention behavior. Some newer web-search modes are not ZDR-eligible unless configured for direct invocation. | all tools/search OFF for first D0/D1 pilot |

## Exact official locators

1. Training:
   `https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training`
2. Retention:
   `https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data`
3. ZDR:
   `https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to`
4. Region/subprocessors:
   `https://privacy.claude.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers`
5. DPA:
   `https://www.anthropic.com/legal/data-processing-addendum`
6. API retention feature matrix:
   `https://platform.claude.com/docs/en/manage-claude/api-and-data-retention`
7. Model IDs/versioning:
   `https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions`
8. Server-tool boundary:
   `https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools`

## Classification

### D0
`ELIGIBLE_D0`

### D1
`ELIGIBLE_D1`

Conditions:
- direct `api.anthropic.com`;
- commercial/API account, not consumer route;
- exact canonical model ID;
- no Files API;
- no server tools/search/code execution;
- no feedback/opt-in training path;
- no project/private content beyond D1;
- provenance records Anthropic + exact model ID + API route.

No credentials/provider connection are authorized by this evidence card.

---

# 3. Route B — Google Vertex AI / Gemini

## Route scope

Exact pilot route evaluated:

`project gateway/client → Google Cloud regional or jurisdictional endpoint → Google-published Gemini model on Gemini Enterprise Agent Platform / Vertex AI managed generative API`

Excluded:
- Gemini consumer app;
- Google AI Studio / Gemini Developer API as a separate commercial path;
- Partner Models/MaaS;
- Agent products;
- Interactions API with stored state;
- Grounding with Google Search/Maps;
- request-response logging;
- Live session resumption;
- RAG/vector stores;
- Deep Research;
- external tools.

## Evidence matrix

| Evidence item | Fresh official evidence | KAN finding |
|---|---|---|
| Product/API scope | Google current docs describe managed models on Gemini Enterprise Agent Platform, formerly Vertex AI, including Google-published Gemini models and regional/global endpoints. | exact Cloud managed route is identifiable |
| Training/data use | Google states it won't use customer data to train/fine-tune managed AI/ML models without prior permission/instruction; docs say this covers GA and pre-GA managed models. | PASS for D0/D1 |
| Retention/abuse monitoring | Google may log prompts for abuse monitoring under applicable GCP terms; certain Advanced AI models/features can add prompt/response logging and may prevent ZDR. | known conditional service-side logging |
| ZDR/no-retention | Google documents exact actions needed for ZDR; abuse-monitoring exception may need approval. Request-response logging must remain disabled. | ZDR possible but feature/config dependent; not assumed |
| Stored state | Interactions API defaults `store=true` if unspecified; must set `store=false` for ZDR. Live session resumption stores data up to 24h when enabled. In-memory Gemini cache has a 24h TTL but Google says it remains ZDR-compatible and can be disabled project-wide. | pilot must avoid Interactions stored state and session resumption |
| Deletion | Some agent/session products expose explicit deletion; for the evaluated stateless route the key control is to avoid stored-state features. Google documents auto-TTL/deletion for several stateful services. | adequate for D0/D1 stateless pilot; no claim of universal per-request deletion |
| Subprocessors | Google publishes a current GCP subprocessor table and identifies AI/Agent Platform support/data-labeling subprocessors and processing countries. | official current locator exists |
| Region | Google documents data residency and processing behavior for regional, jurisdictional multi-region and global endpoints; global endpoints do not give regional isolation. | use explicit regional or jurisdictional endpoint for provenance; avoid global in first pilot |
| Routing/fallback visibility | direct Google Cloud route uses Google-published Gemini model; no multi-provider router in evaluated path. | PASS |
| Model pinning | Google publishes explicit Gemini model IDs and lifecycle/retirement dates. Model/version registry also supports immutable version IDs for customer model resources; for published Gemini route, record exact published model ID and lifecycle state rather than an informal "latest" label. | sufficient for D0/D1 reproducibility, but not equivalent to Anthropic's explicit fixed-weight model-ID guarantee |
| Search/grounding side-boundary | Grounding with Google Search stores derived queries/context up to 3 days and cannot disable that storage; Maps grounding has longer retention. Request-response logging and stored interactions are separate features. | all grounding/search/tool/state features OFF for first pilot |

## Exact official locators

1. Current ZDR/training/retention controls:
   `https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention`
2. Data residency:
   `https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency`
3. Deployment/endpoints:
   `https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations`
4. Model versions/lifecycle:
   `https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions`
5. Current GCP subprocessors:
   `https://cloud.google.com/terms/subprocessors`
6. Security controls by model/capability:
   `https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls`

## Classification

### D0
`ELIGIBLE_D0`

### D1
`ELIGIBLE_D1`

Conditions:
- Google Cloud managed Gemini route, not consumer Gemini;
- Google-published model;
- exact model ID recorded;
- explicit regional/jurisdictional endpoint recorded;
- request-response logging OFF;
- no Grounding with Google Search/Maps;
- no Interactions stored state; if Interactions is used later, `store=false`;
- no Live session resumption;
- no external tools;
- no D2+ content.

The existence of abuse/safety logging does not block D0/D1 because those classes contain synthetic or already-public data. It becomes materially relevant before D2+.

No Google account/project/credential creation is authorized here.

---

# 4. Route C — OpenRouter router/aggregator

## Route scope

Evaluated route:

`project gateway/client → OpenRouter API → one pinned model → one explicitly allowed upstream provider endpoint`

The generic default OpenRouter behavior is **not** accepted as a D1 route because routing/fallback may select among multiple actual providers.

## Evidence matrix

| Evidence item | Fresh official evidence | KAN finding |
|---|---|---|
| Product/API scope | OpenRouter is a routing API between client and many model providers. | route necessarily has two data boundaries: OpenRouter + actual upstream |
| OpenRouter training/data use | OpenRouter says prompt/response retention is opt-in and use of inputs/outputs for product improvement is off by default. | router-level prompt use is bounded by settings |
| OpenRouter retention | OpenRouter says it does not store prompts/responses unless I/O logging or input/output use is opted in. It does retain request metadata such as token counts and latency. | D0/D1 acceptable with logging/IO-use OFF; metadata remains |
| Upstream provider retention/training | OpenRouter explicitly says each provider has its own data policy and that OpenRouter labels are not definitive substitutes for third-party policies. | upstream policy must be independently evidenced for D1 |
| ZDR | OpenRouter can enforce `provider.zdr=true` and route only to endpoints OpenRouter classifies as ZDR. It also exposes `data_collection=deny`. | useful routing control, but upstream official evidence remains required for D1 |
| Deletion | Standard prompt/response content is not stored by OpenRouter when logging/use is off; persistent Files API content is retained until deleted/account closure; privacy policy provides account/data deletion rights. | pilot must not use Files API or persistent storage |
| Stored state | Files, response caching, observability logging and other features are separate storage paths. | all persistent/stateful features OFF |
| Subprocessors/region | OpenRouter privacy policy allows cross-border processing and has its own service providers; actual model provider adds a second processor/data-location boundary. | generic route cannot inherit one region claim |
| Routing/fallback | OpenRouter can pin provider `only`/full endpoint slug, set `order`, and disable provider fallback with `allow_fallbacks=false`. Model-level fallbacks are separately supported and must not be configured. | deterministic route is technically possible |
| Model/provider visibility | OpenRouter response includes model identity; Router Metadata can surface the routing pipeline, which may otherwise be opaque. | enable router metadata for pilot provenance |
| Model pinning | exact model ID can be requested, but actual upstream serving endpoint must also be pinned. Broad provider slugs can cover several regional/variant endpoints. | require exact model + full provider endpoint slug where available |
| Tools/search side-boundary | OpenRouter can run server-side tools/plugins such as web search; Auto Exacto can reorder providers on tool-calling requests by default. Router metadata docs state pipeline may invoke tools/guardrails/fallbacks. | tools/plugins OFF; no Auto Exacto/tool route in first pilot |

## Exact official locators

1. Data collection:
   `https://openrouter.ai/docs/guides/privacy/data-collection`
2. Provider logging/data policies:
   `https://openrouter.ai/docs/guides/privacy/provider-logging`
3. Provider selection/pinning/fallback:
   `https://openrouter.ai/docs/guides/routing/provider-selection`
4. Model fallbacks:
   `https://openrouter.ai/docs/guides/routing/model-fallbacks`
5. ZDR:
   `https://openrouter.ai/docs/guides/features/zdr`
6. Router metadata:
   `https://openrouter.ai/docs/guides/features/router-metadata`
7. Privacy/deletion/files:
   `https://openrouter.ai/privacy/`
8. Tool/web-search side-boundary:
   `https://openrouter.ai/docs/guides/features/plugins/web-search`
9. Auto Exacto provider reordering on tool calls:
   `https://openrouter.ai/docs/guides/routing/auto-exacto`

## Classification

### D0

`ELIGIBLE_D0` only if the pilot request fixes all of:

- I/O logging OFF;
- OpenRouter input/output-use opt-in OFF;
- one exact model;
- one explicit upstream provider/endpoint allowlist;
- `allow_fallbacks=false`;
- no model fallback array;
- `data_collection=deny`;
- preferably `zdr=true`;
- router metadata ON for provenance;
- no tools/plugins/files/cache.

Because D0 is synthetic, upstream retention uncertainty is not a project-data exposure.

### D1

`CONDITIONAL`

To promote the exact OpenRouter D1 route to `ELIGIBLE_D1`, KOO must attach fresh official evidence for the **actual pinned upstream provider/endpoint** and verify that the configured OpenRouter route cannot silently escape to another provider/endpoint.

OpenRouter's own provider-policy label is useful operational evidence but is not sufficient as the sole policy evidence for D1 under the KAN gateway boundary.

---

# 5. Comparative recommendation for first real D0/D1 route selection

This document does not choose or authorize a provider, but the evidence burden differs.

## Lowest policy complexity

1. **Anthropic direct API — ELIGIBLE_D1**
   - one direct data boundary;
   - no-training default documented;
   - bounded standard retention documented;
   - exact fixed model IDs documented.

2. **Google Vertex AI/Gemini direct — ELIGIBLE_D1**
   - one primary Cloud route;
   - strong training restriction;
   - detailed ZDR/feature-retention documentation;
   - more configuration-dependent state/logging/grounding controls.

3. **OpenRouter — CONDITIONAL for D1**
   - router plus upstream provider;
   - technically good pinning/ZDR/fallback controls;
   - requires two policy evidence sets;
   - best suited to D0 multi-provider mechanics pilot before D1.

This ordering is about **policy/evidence simplicity only**, not quality, price, latency or procurement preference.

---

# 6. Exact first-pilot route envelopes

## Anthropic D0/D1 candidate envelope

`route_type=direct_api`
`provider=Anthropic`
`api=Messages API`
`tools=off`
`files=off`
`feedback=off`
`model=canonical exact Claude model ID`
`fallback=none`

## Google D0/D1 candidate envelope

`route_type=direct_api`
`provider=Google Cloud`
`service=Gemini Enterprise Agent Platform / Vertex AI managed Gemini`
`model=exact Google-published Gemini model ID`
`endpoint=explicit regional/jurisdictional endpoint`
`request_response_logging=off`
`grounding=off`
`stored_interactions=off`
`session_resumption=off`

## OpenRouter D0 candidate envelope

`route_type=third_party_router`
`router=OpenRouter`
`model=exact model ID`
`provider_only=[exact upstream endpoint]`
`allow_fallbacks=false`
`model_fallbacks=none`
`data_collection=deny`
`zdr=true`
`router_metadata=on`
`io_logging=off`
`tools=off`
`files/cache=off`

For D1, add an independent official-policy evidence card for the exact upstream provider.

---

# 7. Unknowns / blockers that remain

## Anthropic

No blocker for D0/D1 evidence classification.

Before D2+:
- exact organization ZDR eligibility if required;
- exact Covered Model retention if selected;
- exact traffic routing/account configuration;
- current subprocessor snapshot.

## Google

No blocker for D0/D1 evidence classification under the stateless route constraints above.

Before D2+:
- whether selected model/feature is subject to Advanced AI logging;
- abuse-monitoring exception/ZDR eligibility if required;
- exact regional processing commitment for selected model;
- any stored-state feature enabled by the eventual SDK/API path.

## OpenRouter

D1 blocker remains:

`ACTUAL_UPSTREAM_PROVIDER_POLICY_EVIDENCE_REQUIRED`

and:

`DETERMINISTIC_UPSTREAM_PIN_AND_NO_FALLBACK_MUST_BE_VERIFIED_IN_REQUEST_CONFIG`

Until then:

`OpenRouter D1 = CONDITIONAL`

---

# 8. Final classification

- Anthropic commercial/API direct route: **ELIGIBLE_D1**
- Google Vertex AI / Gemini direct route: **ELIGIBLE_D1**
- OpenRouter router/aggregator:
  - synthetic D0 route under exact controls: **ELIGIBLE_D0**
  - generic D1 route: **CONDITIONAL**

No route is authorized for use by this file. This is evidence classification only.

---

## Experience fixation

**Идея:** first-provider selection should compare not only "privacy promises" but exact data-path complexity.

**Проба:** each candidate was decomposed into product scope, retention/training state, stored features, routing and exact model/provider identity using fresh official documentation.

**Результат:** Anthropic and Google direct routes have enough official evidence for D0/D1 eligibility; OpenRouter is suitable for synthetic D0 mechanics but D1 requires independent evidence for the pinned upstream provider.

**Оценка:** `evidence_matrix_complete`.

**Фиксация:** routers are excellent at hiding infrastructure complexity and therefore equally talented at hiding evidence complexity. For D1, "the router says this provider is ZDR" is a control signal, not the entire proof chain.

---

sender: KAN
recipient: KOO
document_type: multi-model-first-provider-evidence-matrix
status: evidence_matrix_complete
provider_connection_authorized: no
credentials_created: no
external_data_transfer_authorized: no
purchase_authorized: no
project_time: omitted; trusted project-time source not used
