# OPERATOR decision — authorize durable OpenAI reference binding r0.1

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_OPENAI_DURABLE_SECRETREF_BIND_R01
project_time: omitted; trusted project-time source not used

Authorized canonical reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

Authorized host:
`ruvds-xnqc6`

Authorized storage mechanism:
`systemd-creds`

Authorized object name:
`openai-wellbeing-entity-boosters-restricted`

Scope:
- bind the already existing restricted OpenAI project credential to the canonical reference;
- OPERATOR performs the interactive no-echo value entry locally;
- Entities verify only reference/object metadata and mapping;
- no provider call;
- no account/billing mutation;
- no production deployment;
- no Project Sources change;
- no project acceptance;
- no live execution authority.

After PASS, KOO may prepare the separate one-call D0 live execution decision gate.