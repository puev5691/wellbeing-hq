# KOO current active queue r0.28

status: CURRENT_QUEUE

## ACTIVE SLOT 1 — KOD / ASTRA ALLOWLIST

Task:
`c1c0a07cba90227c1e18f4c8fb3492f58118da5d`

Inbox:
`c61aa8a8213708f26b2fa29adad670bc63fd5620`

Basis:
SIS cost-matrix blocker `8139700f5f31523073d7bbe3ee93e393308d0775`.

Goal:
add only `gpt-6-astra` to existing verified OpenAI runtime allowlist, preserving all existing live boundaries.

Next after PASS:
independent runtime verify, then resume four-model live cost matrix.

## ACTIVE SLOT 2 — SHD / TELEGRAM SEMANTIC VERIFY

Task:
`8843c8aa893e904a3aca1e7f11bc002998a84c4e`

Inbox:
`3394e49dd42f0a4377d0aa18e4dfbb15fce63e71`

Candidate:
KOD semantic synthetic PASS `e02534cb73dc472a2c7e8152d18a2eb39d0e94d6`.

Goal:
independent verify of privacy/minimization → SemanticInput → facilitator → candidate-only task boundary.

## WAITING — SIS / OPENAI COST MATRIX

Blocker:
`BLOCKED_OPENAI_COST_MATRIX_ASTRA_NOT_IN_VERIFIED_RUNTIME_ALLOWLIST`

No provider attempts consumed.
Resume after Astra runtime independent verify PASS.

## QUEUED — ARH / SHARD SELECTION

Task:
`d4133f0d50139b6bf6cf3de04e70a85488ab5394`

Start at next genuine infrastructure slot after current verification chain.

## RED

History r0.2 remains without terminal result.
Investment-direction map exists separately and does not close history task.

## VERIFIED LIVE BOUNDARIES

OpenAI Luna D0 PASS:
`28f92b1a72b96fefcb991d1ecccfd57752330301`

Telegram discussion probe PASS:
`09b6fdfd04da84533185b11b0861b2220b72dfb3`

File/Artifact Service final PASS:
`a95ef7308a7a2e2f86c6e021c7f2a4c2f9438232`
