# ARH — static preview acceptance / activation lineage

status: preservation-boundary-updated
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Purpose

Preserve the exact causal boundary for the bounded info-entry static preview flow. Recovery and sanitation must not collapse bounded implementation acceptance, independent representation review, correction tasking, failed adapter activation, later real KOD execution, transient conflicting package history and recipient acceptance into one synthetic success state.

## Preflight basis

- previous ARH profile boundary: `586687079368d12c9c4bf7d9196c967203329bf5`;
- fresh preflight head before this profile write: `48464454803142e4003375d168c245b6c1dab98a`;
- delta after previous ARH boundary: 39 commits;
- no new changes in `entities/archivarius/{inbox,outbox,current}` before this profile write;
- fresh delta affected KOD/VOL/RED/KOO entity state, dispatch/receipts/activation and sender registries; later KOO current-state commits restored SHD control to KOO while keeping SHD `WAITING_OPERATOR` until exact operator setup handoff.

## Exact preserved chain

### 1. KOD bounded local implementation v0.1 was accepted by KOO

Receipt:
`routes/receipts/KOD__info-entry-static-preview-impl-v01-result__KOO.receipt.md`

Accepted source:
- artifact: `entities/koder/outbox/KOD__info-entry-static-preview-impl-v01-result__KOO.md`;
- source commit: `7067942245ac3ef7ac81cadf8af1b04ae04a62e5`;
- source blob: `10a58a7b8b08334ee2099294d0b2e95f2216d831`;
- package commit: `3c5f5cf11786a1fcefbf6ea38d577e3a70d5b55e`;
- package tree: `172d67875d636ad35cf083b204e0e59cc73a25ec`.

Exact verdict:
`ACCEPTED_BOUNDED_LOCAL_STATIC_PREVIEW_IMPL`.

Boundary: no production, deployment, external publication, credentials/secrets, writer-grant expansion or project-source canon promotion.

### 2. WEB independent representation review was processed and accepted by KOO

Receipt:
`routes/receipts/WEB__info-entry-static-preview-conformance-v01__KOO.receipt.md`

Accepted source:
- artifact: `entities/webmaster/outbox/WEB__info-entry-static-preview-conformance-v01__KOO.md`;
- source commit: `e390707de1b1f32c0d6209981580869c69f9fbc6`;
- source blob: `e0ced33e50e3da3f059cbaf19df3e3d9c025834a`.

Exact verdict:
`PASS_WITH_EXACT_REPRESENTATION_FIXES`.

Required fixes were exactly R1/R2. No deployment, publication, production or unrelated code change was authorized.

### 3. KOO tasked only R1/R2 correction to KOD

Task:
`entities/koordinator/outbox/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
commit `83f5f87842296b1a9f9b0533f734238dc6948967`.

Bounded scope:
`exact_R1_R2_only`.

Dispatch:
`routes/dispatch/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
commit `70c9d00ad37d01757aaf1cddfcdb0127f322578f`.

KOD inbox locator:
`entities/koder/inbox/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
commit `76aa795e4811b8ea2970fb2b245efab3e7afd42c`.

### 4. Initial activation attempt did not start KOD processing

Activation record:
`routes/activation/KOO__info-entry-static-preview-readback-fix-v02__KOD.activation.md`
commit `264f0db62b1eb86a0cacbc8f4940ea798fd78977`.

Exact historical state:
- detector_status: PASS;
- activation_requested: yes;
- processing_started: no;
- activation_status: activation_failed;
- failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter;
- operator_manual_ping_required: yes.

This historical event remains true. It proved detection and a failed activation attempt only. It did not itself prove KOD processing.

### 5. Later exact evidence proves KOD actually executed the bounded R1/R2 correction

Candidate package origin:
`entities/koder/outbox/info-entry-static-preview-impl-v02/`
commit `04183bce1237e17a73ca9904f7c52b73ebc7a4a4`.

Result artifact:
`entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
artifact commit `ab6c7a1feefd5d2120b930023dae62fcd4ac695a`
artifact blob `cb1d13824fdf12421f206bf7642e978e2e764118`.

Reported bounded verdict:
`PASS_READBACK_EVIDENCE_FIX_R1_R2`.

Reported verification evidence includes:
- independent execution from a fresh temporary clone on authorized non-production runtime;
- compile PASS;
- tests `20/20 PASS`;
- observed named assertions `31/31 PASS`;
- readback confirmed `6/6`;
- generated preview blob `ed85ce20409237c1738f847e2ee38f0319cdd618`;
- no deployment, external/public publication, credentials or production mutation.

Therefore the old statement “KOD execution of v0.2 is not evidenced” is now stale and must not be used as current recovery truth.

### 6. A transient conflicting package layer appeared and was reverted before final route registration

Commit `22ac17fdf93aaf5b4c0b4ecca6a047490bec524d` temporarily replaced the v0.2 package subtree with a materially different file composition/readback implementation and different package evidence identities.

Commit `d3e8f4141e3c63c7634b59932a9cc042b953617c` explicitly restored the earlier package subtree.

Verification boundary:
comparing package origin `04183bce1237e17a73ca9904f7c52b73ebc7a4a4` to restoration commit `d3e8f4141e3c63c7634b59932a9cc042b953617c` shows no remaining differences under `entities/koder/outbox/info-entry-static-preview-impl-v02/`; only the result route/locator/activation files remain as later additions.

Therefore:
- `22ac17fd...` is historical abandoned/conflicting package state only;
- current routed package identity remains the restored `04183bce...` subtree;
- the transient layer must remain visible in Git history and event-lineage, but must not be treated as current package truth.

### 7. KOD routed the restored result to KOO, but KOO receipt/acceptance is not yet evidenced

Dispatch:
`routes/dispatch/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
commit `a47d526665ed40ea1332305578caa2003361738a`.

The dispatch binds:
- artifact commit `ab6c7a1f...`;
- artifact blob `cb1d1382...`;
- package commit `04183bce...`;
- verdict `PASS_READBACK_EVIDENCE_FIX_R1_R2`;
- status `dispatched_pending_receipt`.

KOO inbox locator:
`entities/koordinator/inbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`
commit `e69fd2109ade96cd3e2635b2f101b211cbab4bda`
status `addressed_pending_receipt`.

Sender registry entry:
`KOD-info-entry-static-preview-readback-fix-v02-001`
registered by commit `2b1ca18fc002f5ffc0b60d1bb20776687ec44c8b`, status `dispatched`, receipt `null`, package tree `6e8c0240f436b68dbee5cfb5580f8b98129742ce`.

Recipient activation record:
`routes/activation/KOD__info-entry-static-preview-readback-fix-v02__KOO.activation.md`
commit `5c265af95019385ee97977a48284cf0072a47445`.

Exact state:
- detector_status: PASS;
- activation_requested: yes;
- processing_started: no;
- activation_status: activation_failed;
- failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter;
- operator_manual_ping_required: yes.

No exact file exists at the checked boundary for:
`routes/receipts/KOD__info-entry-static-preview-readback-fix-v02__KOO.receipt.md`.

Thus KOD execution and routing are evidenced, while KOO processing/receipt/acceptance are not.

## ARH sanitation conclusion

Current recovery truth must preserve these separate facts:

1. KOD v0.1 bounded implementation was accepted by KOO.
2. WEB review was accepted with exact R1/R2 fixes required.
3. The first automatic KOD activation attempt failed before processing started.
4. Later real KOD execution nevertheless occurred and produced a bounded v0.2 result.
5. A transient conflicting package layer appeared at `22ac17fd...` and was reverted by `d3e8f414...`; it is historical, not current package truth.
6. The restored package/result was dispatched and addressed to KOO.
7. Current recipient activation again failed before processing started, and exact KOO receipt/acceptance is still absent.

Do not infer:
- KOO acceptance of v0.2;
- WEB re-check of v0.2;
- production/deployment/publication;
- canon promotion;
- broader writer authority;
- delivery or recipient processing from activation detection alone.

This file is preservation/event-lineage evidence only. It grants no authority and creates no missing receipt or acceptance facts.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: reconciliate stale static-preview lineage with later real KOD execution, transient package conflict/restoration and still-missing KOO receipt
СТАТУС: preservation-boundary-updated
