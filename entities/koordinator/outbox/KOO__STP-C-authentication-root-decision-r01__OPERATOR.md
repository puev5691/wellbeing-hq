# KOO → OPERATOR: STP-C authentication-root decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current governance:
- C1 seats: KOO / KAN / SIS
- ordinary quorum: Q2 2-of-3, current REJECT blocks
- emergency freeze: R3, KAN or SIS single-seat freeze-only
- signer model: S1, each seat authenticates its own decision evidence

Purpose:
select only the authentication-root family that will later allow verification that a seat decision actually came from the authorized seat identity.

This gate does NOT create keys, credentials, accounts, runtime separation, or technical independence.

## Option A1 — Git-backed identity binding + pinned verification key

Token:
SELECT_STPC_ROOT_A1_GIT_BINDING_PINNED_KEY

Meaning:
seat identity/authority binding is anchored in an exact Git artifact/policy, while each seat's decision evidence is verified against an explicitly pinned verification key/identity.

Consequence:
- fits existing canonical Git information field;
- relatively simple provenance and versioning;
- requires later key lifecycle/custody/rotation/revocation design;
- Git publication alone never creates authority.

## Option A2 — offline root

Token:
SELECT_STPC_ROOT_A2_OFFLINE_ROOT

Meaning:
a separately controlled offline root establishes or signs the trust binding used to verify seat authentication identities.

Consequence:
- stronger separation from online runtime;
- heavier human/key handling and recovery burden;
- key custody and operational procedure become critical.

## Option A3 — threshold root

Token:
SELECT_STPC_ROOT_A3_THRESHOLD_ROOT

Meaning:
root-level trust changes require a threshold/multi-party root mechanism.

Consequence:
- reduces single-root-key risk;
- highest implementation and recovery complexity;
- probably disproportionate while the system still lives in one shared technical control domain.

## Option A4 — defer concrete root technology, keep abstract authenticated-seat requirement

Token:
DEFER_STPC_ROOT_TECHNOLOGY_KEEP_ABSTRACT_BINDING

Meaning:
preserve only the requirement that every seat decision must be authentically bound to its authorized seat identity, but do not yet choose Git-key/offline/threshold technology.

Consequence:
- avoids premature cryptographic/infrastructure design;
- blocks concrete implementation of authenticated decision evidence until root technology is later chosen.

## Not part of this gate

No:
- key generation;
- credential creation;
- key custody assignment;
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
- SELECT_STPC_ROOT_A1_GIT_BINDING_PINNED_KEY
- SELECT_STPC_ROOT_A2_OFFLINE_ROOT
- SELECT_STPC_ROOT_A3_THRESHOLD_ROOT
- DEFER_STPC_ROOT_TECHNOLOGY_KEEP_ABSTRACT_BINDING
