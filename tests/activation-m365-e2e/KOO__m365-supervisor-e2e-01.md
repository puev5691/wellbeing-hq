# M365 supervisor E2E marker

entity_id: ent:KOO-M365-E2E-01
task_id: task:KOO-M365-SUPERVISOR-E2E-01
purpose: prove that Microsoft Power Automate can create the activation pull request without an OPERATOR chat message
production: no
writer_authority: none
base_branch: main
head_branch: m365/activation-e2e-koo-01
expected_pr_creator_path: Microsoft Power Automate GitHub connector
expected_next_stage: ChatGPT Work PR-triggered run with recovery/checkpoint verification
must_not_claim: exact existing-chat resume, writer transfer, production-safe autonomy

---
WHO: KOO / КООРДИНАТОР
PURPOSE: inert marker for bounded Microsoft Power Automate -> GitHub PR activation test
STATUS: test_marker_only
