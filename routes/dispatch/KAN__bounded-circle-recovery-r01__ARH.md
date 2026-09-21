# Dispatch: KAN → ARH bounded working-circle experiment r0.1

exchange_gate: v1
sender: kancelar
recipient: archivarius

experiment: entities/kancelar/outbox/KAN__bounded-working-circle-experiment-r01__OPERATOR-KOO-SHT-ARH.md
experiment_commit: 39cb6f6c9473dd49e126c1cbfa0cf45eae68895b
experiment_blob: 2c6d4403e7f57111a6fe5938027f12342dfbeb95

prompt: entities/kancelar/outbox/ARH_circle_recovery_r01_review_prompt.md
prompt_commit: 2bc9a1e18c920f5de91e536cf639fe38b3556f22
prompt_blob: 7c93feb8d03de5cb312784b3fe1d409d5de78e67

purpose: bounded recovery/preservation review for working-circle experiment
required_action: process exact prompt after Resume-First; do not preempt an already active exact profile task; if preemption would occur, return WAITING_ACTIVE_TASK with exact locator
expected_result: bounded ARH recovery review to KAN + OPERATOR
failure_mode: any experiment/prompt identity mismatch, superseding Operator instruction, or conflicting active task authority => stop and return exact blocker/waiting state
status: dispatched
project_time: omitted; trusted project-time source not used
