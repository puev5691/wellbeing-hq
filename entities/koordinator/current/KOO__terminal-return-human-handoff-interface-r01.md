# KOO terminal-return human handoff interface r0.1

status:
KOO_LOCAL_INTERFACE_RULE_ACTIVE

entity:
KOO / КООРДИНАТОР r1.3

project_time:
omitted

## Purpose

Fix a repeated human-interface failure in Entity task prompts.

Observed failure pattern:
task text says "return terminal/locator/commit/blob to KOO" and the Entity returns only a terse locator line.

This is machine-correct but human-interface-incomplete.

## Mandatory KOO task-construction rule

For every future manual Entity task prepared by KOO, if the task result must be returned through OPERATOR to another Entity chat, the prompt MUST explicitly require one final copy-paste return block.

Required shape:

АДРЕСАТ: <recipient Entity / callsign>

Resume-First.

<exact result state and immutable locators>

<what is established>

<what is NOT authorized / NOT started>

<exact request to recipient: fresh reconcile / review / decide>

STOP.

The return block is a transport/handoff object only.

It does NOT:
- create successor task authority;
- approve the result;
- infer receipt or acceptance;
- authorize automatic downstream continuation;
- replace recipient Resume-First/currentness checks.

## Specific requirement for return to KOO

When an Entity must return a terminal result to KOO, its task prompt MUST require:

- literal header: "АДРЕСАТ: КООРДИНАТОР / KOO";
- literal "Resume-First.";
- exact terminal;
- exact result locator;
- commit;
- blob;
- exact successor package locator/tree when applicable;
- compact verdicts;
- explicit boundaries;
- instruction: "Fresh-reconcile this exact result; do not infer downstream authority.";
- STOP.

A bare phrase such as:
"КООРДИНАТОРУ terminal locator <sha>"
is insufficient for the human handoff interface even if the durable result itself is complete.

## Basis

This rule operationalizes the already loaded KOO human-interface requirement that exact prompts/tasks be complete and copyable and that the human not assemble a task from scattered fragments.

It is a KOO local task-interface rule only.

Project Sources/canons:
UNCHANGED

role authority:
UNCHANGED

automatic activation:
NO
