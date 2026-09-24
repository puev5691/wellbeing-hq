# ARH delivery-rule supersede lineage r0.1

status: PRESERVED_VERIFIED_SUPERSESSION_LINEAGE
entity: ARH / АРХИВАРИУС
project_time: omitted

## Event

OPERATOR normative decision selected locator-based delivery as valid project routing semantics and superseded only the obsolete physical-upload-only implication of historical source-loading-policy v2 section 5.

Decision artifact:
entities/koordinator/current/KOO__delivery-rule-operator-decision.md

decision blob:
e6846a36e7970c4d61419b5421b2d08c74975a4d

decision basis commit recorded by KOO:
b8b74a7ad58111b58e02f6a82b693d152e09a39b

## Historical predecessor

Historical source lineage:
source-loading-policy-v2-approved.md

Preservation rule:
retain predecessor bytes as provenance/evidence; do not rewrite historical source in place.

Semantic disposition:
SUPERSEDED_FOR_CURRENT_DELIVERY_SEMANTICS

The supersession scope is bounded to the old physical-upload-only implication. Other historical content is not silently reclassified by this record.

## Activated successor

Approved successor:
entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md

Git blob:
69eb657f260a019f76e8e707c880ea88c1dfa0bf

SHA-256:
2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e

Activation evidence:
entities/koordinator/outbox/KOO__source-set-r03-activation-result__OPERATOR.md

activation verdict:
PASS_KOO_SOURCE_SET_R03_ACTIVATED

activation blob:
2804f043d1648b5f61dbd29bbb0f423ed09e3585

Successor service-card field:
supersedes_after_activation_barrier_pass: source-loading-policy-v2-approved.md plus any explicitly withdrawn/rejected predecessor candidate

Verified current semantics in successor §5:
- referenced artifacts need not be physically transferred by OPERATOR when exact locator + immutable identity are available;
- physical transfer is fallback for unavailable locator or external file outside shared information field;
- publication/dispatch/activation remain distinct from processing/delivery/acceptance.

## Lineage relation

predecessor:
source-loading-policy-v2-approved.md

successor:
source-loading-policy-v2_2-approved.md

relation:
predecessor -> superseded_by -> source-loading-policy-v2_2-approved.md
successor -> supersedes -> source-loading-policy-v2-approved.md

activation condition:
SATISFIED_BY_PASS_KOO_SOURCE_SET_R03_ACTIVATED

## Boundary

No destructive cleanup performed.
No historical bytes rewritten.
No candidate publication treated as activation.
No Project Source changed by ARH.
No delivery/receipt/acceptance inferred beyond exact evidence.

---
КТО: ARH / АРХИВАРИУС
СТАТУС: PRESERVED_VERIFIED_SUPERSESSION_LINEAGE
