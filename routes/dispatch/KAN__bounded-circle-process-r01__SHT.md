# Dispatch: KAN → SHT bounded working-circle experiment r0.1

exchange_gate: v1
sender: kancelar
recipient: shtabist

experiment: entities/kancelar/outbox/KAN__bounded-working-circle-experiment-r01__OPERATOR-KOO-SHT-ARH.md
experiment_commit: 39cb6f6c9473dd49e126c1cbfa0cf45eae68895b
experiment_blob: 2c6d4403e7f57111a6fe5938027f12342dfbeb95

prompt: entities/kancelar/outbox/SHT_circle_process_r01_stress_review_prompt.md
prompt_commit: f347129d2df43b7381f31ba4de1a5b251d1fcbb5
prompt_blob: 7b491e064b2a2118d76f92fcb27d75ec5d9b9708

purpose: bounded process stress review for working-circle experiment
required_action: process exact prompt after Resume-First; do not preempt an already active exact profile task; if preemption would occur, return WAITING_ACTIVE_TASK with exact locator
expected_result: bounded SHT PASS_WITH_FINDINGS or defects to KAN + OPERATOR
failure_mode: any experiment/prompt identity mismatch, superseding Operator instruction, or conflicting active task authority => stop and return exact blocker/waiting state
status: dispatched
project_time: omitted; trusted project-time source not used
