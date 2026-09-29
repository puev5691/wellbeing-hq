# SEMANTIC_DIALOGUE_ENGINE_R01 — application profiles r0.1

status: DESIGN_INPUT_CANDIDATE
project_time: omitted

## MEDIA_PORTAL_PROFILE_R01

Purpose:
turn project publications into a source-grounded, argument-aware, human-friendly dialogue surface without advertising influence.

Input:
publication, source set, user question, current corrections/updates.

Semantic objects:
PUBLICATION
CLAIM
SOURCE
EVIDENCE
ARGUMENT
COUNTERARGUMENT
INTERPRETATION
UNCERTAINTY
CORRECTION
UPDATE
QUESTION

Required behavior:
- distinguish claim / evidence / interpretation;
- show source provenance;
- expose uncertainty and disagreement;
- compare arguments without majority-vote truth;
- explain in normal human language;
- keep ad/sponsor influence outside reasoning and answer ranking;
- support publication-linked dialogue history.

Candidate user modes:
EXPLAIN
VERIFY
SHOW_ARGUMENTS
WHAT_IS_DISPUTED
SHOW_SOURCE
WHAT_CHANGED
CONSEQUENCES_BY_EXPLICIT_CONDITIONS

Boundary:
no hidden promotion, no advertising ranking, no sponsor-based answer shaping.

## PROJECT_ECONOMY_PROFILE_R01

Purpose:
connect project dialogue and verified work to contribution accounting, task marketplace, contracts and crypto-platform settlement.

Semantic objects:
CONTRIBUTION
TASK
TASK_CANDIDATE
OFFER
DELIVERY
ACCEPTANCE
OBLIGATION
CONTRACT
REWARD
PENALTY
ENTITLEMENT
SETTLEMENT
DISPUTE
REPUTATION
RESOURCE
ACCOUNTING_EVENT
CONTRACT_EVENT

Core causal chain:
dialogue/observation
-> contribution or task candidate
-> task
-> assignment/offer
-> execution
-> result/delivery
-> verification
-> acceptance
-> accounting event
-> contract/settlement event

Critical rules:
- model praise/opinion never creates entitlement;
- contribution accounting needs evidence and identity/provenance;
- acceptance is separate from delivery;
- reward is separate from acceptance unless contract says otherwise;
- blockchain stores/executes economic/contract facts, not semantic truth;
- dispute can block settlement without erasing prior evidence;
- marketplace task lifecycle must remain explicit and auditable.

Blockchain/crypto-platform integration target:
- task/contract identifiers;
- accepted contribution events;
- obligations;
- entitlements;
- reward/settlement events;
- dispute/hold state;
- participant accounting/statistics;
- WBN/WBNP-related economic events where future approved contracts specify them.

Boundary:
no live chain mutation, token movement, contract deployment or economic effect authorized by this design input.

## SHARED PRINCIPLE

One Semantic Dialogue Engine core.
Different application profiles select:
- semantic object vocabulary;
- relation subset;
- context selection policy;
- model roles;
- output rendering;
- authority/effect rules.

Profiles do not duplicate the core engine.

terminal:
SEMANTIC_DIALOGUE_ENGINE_R01_APPLICATION_PROFILES_R01_READY
