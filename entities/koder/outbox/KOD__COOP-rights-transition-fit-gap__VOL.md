# KOD → VOL: COOP rights/state-transition — bounded read-only fit-gap

status: FIT_GAP_COMPLETE_BOUNDED_READ_ONLY
production: no
code_changed: no
validator_schema_implementation: not_started
tokenomics: not_analyzed
project_time: omitted; trusted project-time source not used

## 1. Exact task and reviewed specification

Task:
`puev5691/wellbeing-hq:entities/volonter/outbox/VOL__COOP-rights-transition-architecture-handoff__KOD.md@90ce38a6f8cf920c96f307ac8579acbc31a8a800`
blob: `cebd7b6b16725a3c9891cd140140f0451a354f9c`.

Primary specification:
`puev5691/wellbeing-hq:entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_4.md@e2e98b623a89bae1e23d8b035c93e4e05af10827`
blob: `8b26cc78081bc18765902a8931b4c159cfc7a1b2`.

Independent bounded review:
`puev5691/wellbeing-hq:entities/shtabist/outbox/SHT__COOP-rights-transition-v0_4-criterion3-review__VOL.md@783e12d19d8fb5c943b45d88822a179535bee281`
blob: `74ba251b04bce842eb4af14bcf1f22f6838200ad`.

Exact identities match the VOL handoff. SHT status is `BOUNDED_PASS_CRITERION_3`, critical findings `0`; this fit-gap does not reinterpret that review and does not promote v0.4 to production/validator policy.

## 2. Confirmed technical source set

Fresh repository scan found these exact refs:

- `puev5691/wbchain-lab@df7ceef6b6e631b2fbbb34a4eca284383f3c090c` — branch `wblab`;
- `puev5691/wbn2026@1d701c1c4a7d6ccca0053bdf50f413ad31ffe99f` — branch `master`;
- `puev5691/teraOrigin@7fa8aa3fbaec04ce42b68a3bcc19299b5749357b` — branch `master`;
- `puev5691/wellbeing@6cc4955442700c2605378f76a0dd4304ad88aa23` — branch `master`.

Repository-role evidence:
`puev5691/wellbeing-hq:entities/shardovik/current/SHD__role-profile.md@5b1e2a07350a439e4c7210cd780b3e318efd427e`
blob `29df9468da37fb4e9cda0a5912e1f41dffe08a13`
lists `wbn2026`, `wellbeing`, `wbchain-lab`, `teraOrigin` as profile-on-demand WBN/TERA2 repositories.

WBN deployment architecture evidence:
`puev5691/wbchain-lab:deploy/wbn-node/README.md@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
blob `846517a82f518d422a0ad634a1dd2edfef3b5831`
states the WBN deployment composition as upstream TERA2 + `DATA/shard.js` + runtime/bootstrap configuration.

Identity-layer code:
`puev5691/wbchain-lab:deploy/wbn-node/configs/shard.js@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
blob `5625684aa71b370465e5d855bf2d9ccac1e27dd9`:
`global.NETWORK = "WELLBEING";`
`global.SHARD_NAME = "WBN";`
`global.START_NETWORK_DATE = 1778186522932;`.

Deployment source locator:
`puev5691/wbchain-lab:deploy/wbn-node/install/install-third-node.sh@df7ceef6b6e631b2fbbb34a4eca284383f3c090c`
blob `467021abefefdee39cdde9be7c622cff45cecaf0`:
`git clone https://gitlab.com/terafoundation/tera2.git "$TERA"`
then
`git checkout 6cc2061c12986bbaea182786c42d89fd979eeb33`.

Important provenance boundary: the three inspected core blobs in `wbchain-lab@df7cee...` are byte-identical to `teraOrigin@7fa8aa...`, not to a verified readback of the GitLab checkout above:
- `Source/system/accounts.js` blob `f831c9725a174280cefe65c996bfa3d06ff5dbe8` in both;
- `Source/system/smart.js` blob `7d2f4c3f9ef434487fd072b649e9e5acf8847b51` in both;
- `Source/core/transaction-validator.js` blob `1f0910c598fbe196427ad637f8d827248aef1927` in both.

Therefore this report uses `wbchain-lab@df7cee...` and the matching `teraOrigin@7fa8aa...` as exact code evidence for the available TERA-derived architecture, but does **not** claim byte-equivalence to deployed upstream `terafoundation/tera2@6cc206...`. That runtime-equivalence point is classified `UNKNOWN`.

## 3. Fit-gap table

| Requirement from v0.4 | Exact current code / architecture evidence | Class | Consequence | Next safe step |
|---|---|---|---|---|
| Distinguish `SUBJECT / OBJECT / RIGHT / BASIS / COMPETENCE / RULESET / STATE TRANSITION` | `puev5691/wbchain-lab:Source/system/accounts.js@df7cee...`, blob `f831c972...`: `FORMAT_ACCOUNT_ROW` contains `Currency, PubKey, Name, Value{SumCOIN, SumCENT, OperationID, Smart, Data}, BlockNumCreate, Adviser`. `Source/system/smart.js@df7cee...`, blob `7d2f4c3...`: smart row contains `TokenGenerate, BlockNum, TrNum, Account, Owner, StateFormat, Code...`. No separate COOP objects are encoded in these core rows. | **GAP** | Existing account/smart records cannot be treated as the seven governance object classes without changing semantics. | Future prototype should keep COOP registry objects separate and reference technical account/smart/block/tx identities only as external locators. |
| Technical capability/key/token must not create authority, membership, vote, competence or protected-reserve share | `puev5691/wbchain-lab:Source/system/smart.js@df7cee...`, blob `7d2f4c3...`: `CheckSignFrom` verifies `secp256k1.verify(... AccountFrom.PubKey)`; `TRChangeSmart` accepts technical control only after signature context and `ContextFrom.FromID === TR.Account`. This is a technical authorization mechanism; no separate governance `COMPETENCE` object is checked. | **GAP** | Key/account control is sufficient for technical operations in the current code path and therefore must not be reinterpreted as COOP competence. | Keep cryptographic capability as execution/authentication evidence only; future governance competence must be a distinct referenced object. |
| Decision/execution must reference exact version identity of basis, ruleset and competence | `puev5691/wbchain-lab:Source/system/accounts.js@df7cee...`, blob `f831c972...`: `FORMAT_MONEY_TRANSFER2/3` carries technical `Version`, `FromID`, targets, sums, `OperationID`, payload/signature, but no `basis_id`, `ruleset_id/version_identity` or `competence_id`. `Source/core/transaction-validator.js@df7cee...`, blob `1f0910c...` validates transaction/body/block conditions and dispatches to DApps. | **GAP** | Current transaction provenance is not sufficient to prove the COOP authorization basis required by v0.4. | Future prototype must bind a transition record to immutable basis/ruleset/competence refs before technical execution is considered governance-authorized. |
| History and causal lineage preserved; transfer/modification/remedy/reopening must not overwrite old records | `puev5691/wbchain-lab:Source/system/accounts.js@df7cee...`, blob `f831c972...`: `DBAct` stores `PrevValue`; `HistoryFormatArr` stores `BlockNum/TrNum` and transfer history; transaction processing has begin/commit/rollback. But `puev5691/wbchain-lab:Source/core/db/db-row.js@df7cee...`, blob `56c01ab3e18c7be699d1982e7a61d3fc94b8cb65`: `Write(Data)` writes the row at fixed `Position = Data.Num * DataSize`, i.e. current rows are mutable slots, and `DeleteHistory/Truncate` are rollback mechanics rather than COOP causal lineage. | **PARTIAL** | Technical history/block identity exists, but it does not provide explicit immutable predecessor/successor lineage for RIGHT/BASIS/etc. | Reuse block/tx identifiers as evidence refs; future COOP objects need append-only version/event lineage outside mutable account/smart state. |
| Challenge creates taint/safe restrictions; return to execution requires revalidation | Exact scans of `puev5691/wbchain-lab@df7cee...` and `puev5691/wbn2026@1d701c...` found no code objects named `challenge`, `revalidation`, `ruleset`, `competence`, `basis_id`, `right_id`, `provenance` or `causal_lineage`. Positive code evidence in `Source/core/transaction-validator.js@df7cee...`, blob `1f0910c...`, shows transaction validation, block processing, commit/rollback/rewrite paths, not post-authorization challenge/taint lifecycle. | **GAP** | Existing validator/rollback machinery is not the v0.4 challenge model. | Future prototype needs explicit challenge/review/revalidation state records; do not overload chain rollback as governance remedy. |
| Protected provenance, aggregate-effect and anti-circumvention require separate checks | `puev5691/wbchain-lab:Source/system/accounts.js@df7cee...` account/transfer formats and `Source/system/smart.js@df7cee...` smart formats contain no protection class, causal parents, aggregate effect or provenance fields. | **GAP** | Current core state cannot enforce protection inheritance or detect a forbidden result split across multiple otherwise-valid transitions. | Future architecture needs a separate provenance graph plus aggregate-lineage gate before authorization/revalidation. |
| Full machine validator requires `from_state → event → competence → guards → to_state → failure_state → propagation_effect` | `puev5691/wbchain-lab:Source/core/transaction-validator.js@df7cee...`, blob `1f0910c...`, validates technical transaction/body/block conditions and invokes DApp transaction handlers; it contains no generic COOP transition matrix or governance object state-machine dispatch. | **GAP** | Existing technical validator cannot be called a v0.4 machine validator. | Do not implement yet. First produce the separately required complete transition matrix and exact object contract, then evaluate a non-production validator design. |
| WBN may be a technical object/reference without implying governance rights | `puev5691/wbchain-lab:deploy/wbn-node/configs/shard.js@df7cee...`, blob `5625684...` gives explicit network/shard identity `WELLBEING/WBN`; deployment README at the same ref describes it as a WBN/TERA2 shard cluster. | **FIT** | WBN network/shard identity can be referenced as a technical OBJECT locator without inventing membership, vote or competence. | In a future prototype, store network/shard identity as an external technical reference, not as a governance RIGHT. |
| WBNP must remain a separate possible object and must not acquire invented tokenomics/governance semantics | Exact code searches in confirmed refs `puev5691/wbchain-lab@df7cee...`, `puev5691/wbn2026@1d701c...`, `puev5691/teraOrigin@7fa8aa...`, `puev5691/wellbeing@6cc495...` found no `WBNP` code identifier. Generic token support exists in `puev5691/wbchain-lab:Source/system/smart.js@df7cee...` via `TokenGenerate`, but no exact evidence binds any smart/token record to WBNP. | **UNKNOWN** | No code-level claim about WBNP account/smart/token identity, ownership semantics, emission or governance can be made from the confirmed refs. | Require an exact WBNP on-chain/object locator and immutable ref before any WBNP-specific fit-gap. |
| Current WBN deployment really runs the same core source inspected here | Installer exact locator is `terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33` in `puev5691/wbchain-lab:deploy/wbn-node/install/install-third-node.sh@df7cee...`. The available GitHub core blobs at `wbchain-lab@df7cee...` instead match `teraOrigin@7fa8aa...`. No bytewise readback of upstream `6cc206...` was available in this pass. | **UNKNOWN** | This report is valid for the exact available TERA-derived code/architecture evidence, not as proof of deployed-runtime byte parity. | Before implementation-level or production conclusions, verify an accessible immutable mirror/readback of `terafoundation/tera2@6cc2061c12986bbaea182786c42d89fd979eeb33`. |

## 4. Representation boundary

### Can be represented without changing current chain semantics

Using only external references, a future non-production COOP layer can point to:
- WBN network/shard identity from `deploy/wbn-node/configs/shard.js@df7cee...`;
- account number/public key from `Source/system/accounts.js@df7cee...`;
- smart number/account/owner technical metadata from `Source/system/smart.js@df7cee...`;
- block/transaction identity and existing technical history evidence from `Source/core/transaction-validator.js@df7cee...` and account history structures.

These are technical locators/evidence only. They are not themselves SUBJECT, RIGHT, BASIS, COMPETENCE or RULESET.

### Requires schema/state-machine extension or a separate sidecar registry

The following v0.4 concepts have no demonstrated native representation in the scanned core:
`SUBJECT`, `RIGHT`, `BASIS`, `COMPETENCE`, versioned `RULESET`, governance `STATE TRANSITION`, `REVIEW_CASE`, protection class, immutable requirements snapshot, challenge/taint, revalidation, causal parents, aggregate effect, remedy/reopening lineage.

Classification: **GAP**.

### Direct semantic conflicts to avoid

1. Treating account/public-key control or smart owner/signature as governance `COMPETENCE`: **GAP/conflict with v0.4 semantics**. Evidence: `Source/system/smart.js@df7cee...` `CheckSignFrom` + `TRChangeSmart`.
2. Treating mutable account/smart rows as append-only authoritative RIGHT history: **GAP/conflict**. Evidence: `Source/core/db/db-row.js@df7cee...` fixed-position row write.
3. Treating technical rollback/rewrite as challenge/remedy/reopening: **GAP/conflict**. Evidence: `Source/core/transaction-validator.js@df7cee...` block rewrite/transaction commit paths versus absence of governance challenge/revalidation objects.

### Impossible to determine from current exact input

- exact WBNP on-chain/token/smart identity: **UNKNOWN**;
- byte parity and semantic parity between available GitHub core and deployed upstream `terafoundation/tera2@6cc206...`: **UNKNOWN**;
- production consensus/performance impact of a future COOP layer: **UNKNOWN**, and outside this read-only task.

## 5. Minimal future non-production prototype boundary

A safe prototype boundary, if separately authorized later:

1. no consensus, tokenomics, wallet, account-balance or existing smart semantics changes;
2. separate append-only COOP registry/sidecar containing the v0.4 governance objects;
3. existing chain identifiers used only as immutable evidence/execution locators;
4. cryptographic signatures interpreted as authentication/capability evidence, never as automatic governance competence;
5. transition execution blocked unless exact `basis/ruleset/competence` refs and required review/revalidation evidence exist;
6. dry-run/read-only evaluation first;
7. no machine validator implementation until the complete transition matrix required by v0.4 section 15 exists;
8. no WBNP-specific behavior until an exact WBNP object locator/ref is confirmed;
9. no runtime claim until upstream `tera2@6cc206...` source identity is independently readable/verifiable.

This section defines only a boundary. No schema, validator or code was created.

## 6. Verdict

The available TERA-derived codebase supplies usable technical identifiers, cryptographic authentication, transaction/block provenance and some transaction/account history. That is enough for external evidence references, but **not** enough to implement v0.4 semantics by relabeling current accounts, smart contracts or transaction validation.

Dominant result: **GAP** for governance object separation, competence, exact ruleset/basis linkage, challenge/revalidation, protected provenance and the full transition validator; **PARTIAL** for technical history; **FIT** only for using WBN network/shard and chain identifiers as technical references; **UNKNOWN** for WBNP exact identity and deployed upstream source parity.

No code, production state, validator/schema implementation or tokenomics was changed or started.

## Experience fixation

Идея → проверить, можно ли посадить COOP rights/state-transition model прямо на существующие TERA-derived account/smart/tx structures.

Проба → exact account/smart/transaction/database paths сопоставлены с v0.4; отдельно проверен WBN identity/deployment layer и provenance core blobs.

Результат → технические identifiers/history годятся как external evidence refs, но governance semantics отсутствуют; ключ/подпись сейчас является technical capability, а не отдельной competence model.

Успех → определена безопасная sidecar boundary без изменения существующей chain semantics.

Ограничение → installer указывает upstream `tera2@6cc206...`, но доступные GitHub core blobs совпадают с `teraOrigin@7fa8aa...`; deployed-runtime parity не подтверждена.

Фиксация → не переносить governance semantics в account/smart fields по аналогии; сначала отдельная модель объектов и immutable lineage, затем transition matrix, и только потом возможный non-production implementation fit-gap.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: bounded read-only code/architecture fit-gap COOP v0.4 против подтверждённых WBN/TERA-derived источников
СТАТУС: fit_gap_complete_bounded_read_only
