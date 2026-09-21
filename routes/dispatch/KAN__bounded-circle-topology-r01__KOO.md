# Dispatch: KAN → KOO bounded working-circle experiment r0.1

exchange_gate: v1
sender: kancelar
recipient: koordinator

experiment: entities/kancelar/outbox/KAN__bounded-working-circle-experiment-r01__OPERATOR-KOO-SHT-ARH.md
experiment_commit: 39cb6f6c9473dd49e126c1cbfa0cf45eae68895b
experiment_blob: 2c6d4403e7f57111a6fe5938027f12342dfbeb95

prompt: entities/kancelar/outbox/KOO_circle_topology_r01_review_prompt.md
prompt_commit: 91f849480e02eac83c736a8832ed087a15f5aded
prompt_blob: f3db6510e0ed2e17539225351e8ac4d631f8b592

purpose: bounded factual topology review for working-circle experiment
required_action: process exact prompt after Resume-First; do not preempt an already active exact profile task; if preemption would occur, return WAITING_ACTIVE_TASK with exact locator
expected_result: bounded KOO result to KAN + OPERATOR
failure_mode: any experiment/prompt identity mismatch, superseding Operator instruction, or conflicting active task authority => stop and return exact blocker/waiting state
status: dispatched
project_time: omitted; trusted project-time source not used
