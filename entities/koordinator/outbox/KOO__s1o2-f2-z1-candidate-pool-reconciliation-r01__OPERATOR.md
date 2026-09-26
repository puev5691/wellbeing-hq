# KOO → OPERATOR: reconciliation of three-resource Z1 candidate pool r0.1

status: Z1_CANDIDATE_POOL_SELECTED_PROVIDER_SEMANTICS_VERIFICATION_REQUIRED
project_time: omitted

## Human meaning

OPERATOR selected three existing resources as the Z1 candidate pool:
- erefia / Moscow by hoster assurance;
- burzh / London by hoster assurance;
- mazhor / Astana by hoster assurance.

This is enough to stop asking OPERATOR to choose a pair.

The next useful step is to verify whether these provider-stated locations are meaningful independent failure domains for the relevant compute/storage service.

The current hoster assurances are useful planning evidence but are not yet independent Z1 proof.

## What is already known

Resource identities are established from existing project evidence.

Provider-stated city/location mapping is supplied directly by OPERATOR:
- erefia → Moscow;
- burzh → London;
- mazhor → Astana.

No contradiction found in the checked project chain.

## What is still not proven

For each resource:
- exact provider zone/site identifier;
- whether city label maps to a physical site or availability zone;
- whether storage is site-local or shared across locations;
- whether provider may migrate resources across sites without changing the visible identity;
- whether any common critical storage/control-plane dependency invalidates Z1.

Therefore:
Z1_documentary_proof = NOT_ESTABLISHED.

## Minimal next step

One bounded SIS documentary verification should compare all three resources and provider semantics without host login, provider API, credentials, or runtime testing.

Goal:
determine whether the existing evidence can support any pair among:
- erefia ↔ burzh
- erefia ↔ mazhor
- burzh ↔ mazhor

For each pair classify:
- PROVABLE_DISTINCT_FAILURE_DOMAIN
- NOT_PROVABLE_FROM_AVAILABLE_EVIDENCE
- CONFLICT/BLOCKED

Required evidence sources may include only already available project evidence and public/provider documentation or non-secret metadata already available without credentials.

If exact provider resource placement cannot be proven from those sources, SIS must return the minimum missing provider/account fact rather than infer independence from city names alone.

## Next authority gate

Required OPERATOR authority:

AUTHORIZE_SIS_S1O2_F2_Z1_THREE_PLACEMENT_DOCUMENTARY_VERIFICATION_R01_READ_ONLY

This does NOT authorize:
- host login;
- provider account/API access;
- credentials;
- runtime testing;
- shard WRITE;
- provisioning;
- backend selection;
- owner appointment;
- Project Sources/canon mutation;
- resume authority;
- memory-layering attempt 3.

## Current truth

candidate pool:
SELECTED

hoster-stated locations:
Moscow / London / Astana

independent Z1 proof:
NOT_ESTABLISHED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## Terminal

PASS_KOO_Z1_CANDIDATE_POOL_RECONCILED_PROVIDER_SEMANTICS_VERIFICATION_GATE_REQUIRED_R01
