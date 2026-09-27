# KOO → OPERATOR: STP-C signer/attestor separation decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current governance:
- C1 seats: KOO / KAN / SIS
- ordinary quorum: Q2 2-of-3, current REJECT blocks
- emergency freeze: R3, KAN or SIS single-seat freeze-only

Purpose:
select only how governance decisions are authenticated/attested.
This gate does NOT select cryptographic root technology or keys.

## Option S1 — approval seats authenticate their own decisions

Token:
SELECT_STPC_SIGNER_S1_SEATS_AUTHENTICATE_OWN_DECISIONS

Meaning:
each seat produces its own authenticated APPROVE/REJECT/FREEZE evidence under a future approved identity/authentication mechanism.

Consequence:
- simplest model;
- fewer moving parts;
- governance seat and authentication capability are colocated for that seat;
- must still prevent one shared technical account/control domain from being misrepresented as independent technical signing domains.

No concrete key/provider/root selected.

## Option S2 — separate mechanical attestor/signing layer

Token:
SELECT_STPC_SIGNER_S2_SEPARATE_MECHANICAL_ATTESTOR

Meaning:
KOO/KAN/SIS make governance decisions, but a separate mechanical signer/attestor emits authenticated evidence only after verifying exact decision objects and scope.

Hard boundary:
the attestor does NOT decide governance truth.
It only authenticates/attests already valid decision evidence.

Consequence:
- cleaner separation between decision and cryptographic/authentication mechanism;
- extra component and failure point;
- requires later exact attestor authority, runtime, custody, replay/scope/currentness rules.

## Option S3 — defer signer model until authentication-root decision

Token:
DEFER_STPC_SIGNER_MODEL_UNTIL_ROOT_DESIGN

Meaning:
keep signer/attestor separation unresolved until the authentication-root architecture is chosen.

Consequence:
- avoids premature design;
- blocks any later concrete authenticated approval format until resolved.

## Not part of this gate

No:
- authentication-root technology;
- key custody;
- credentials;
- backend/host/operator;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
Memory-layering attempt 3 remains NOT_AUTHORIZED.

Return exactly one:
- SELECT_STPC_SIGNER_S1_SEATS_AUTHENTICATE_OWN_DECISIONS
- SELECT_STPC_SIGNER_S2_SEPARATE_MECHANICAL_ATTESTOR
- DEFER_STPC_SIGNER_MODEL_UNTIL_ROOT_DESIGN
