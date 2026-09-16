# KOO → OPERATOR: chat-instance admission guard r0.1

status: `CANDIDATE_FOR_OPERATOR_WORKFLOW`
project_time: omitted; trusted project-time source not used

## Purpose

Prevent a wake prompt for an active Entity from being executed by a retired, replacement-preparation, reinit, or otherwise wrong chat instance.

## Admission rule

Before any profile task, the chat instance must verify the current-writer artifact named in the wake prompt against fresh HQ.

For SIS current boundary:
- current-writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
- expected blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
- initiation status in artifact: `initiation_verified`.

If the current chat cannot reconcile itself with the required current-writer boundary, or instead starts a reinit/initiation/recovery flow not requested by the exact task, it must stop profile execution and return:

`WRONG_INSTANCE_OR_WRONG_CHAT`

with the conflicting evidence.

It must not:
- initiate or reinitiate itself;
- import an unrelated old chat package as current authority;
- run retired-instance lifecycle probes on itself unless explicitly tasked;
- replace the exact current task with an older local contour;
- mutate current/recovery/writer state.

## Wake-prompt convention

Future KOO wake prompts should include:
- `REQUIRED_CURRENT_WRITER_PATH`
- `REQUIRED_CURRENT_WRITER_BLOB`
- explicit `THIS_IS_NOT_AN_INITIATION` when the Entity is already established;
- stop condition `WRONG_INSTANCE_OR_WRONG_CHAT`.

This is an operational guard candidate, not a project canon amendment.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: не допускать выполнения current task старым или неправильным chat-instance
СТАТУС: `candidate_for_operator_workflow_r01`
