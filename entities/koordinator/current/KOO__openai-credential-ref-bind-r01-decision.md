# OPERATOR decision — authorize OpenAI restricted credential reference binding r0.1

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_OPENAI_RESTRICTED_CREDENTIAL_REF_BIND_R01
project_time: omitted; trusted project-time source not used

## Meaning

OPERATOR authorizes one bounded infrastructure verification step to establish the exact reference identifier for the already provisioned restricted OpenAI project credential.

Allowed:
- locate or establish the exact `secretref:openai:<identifier>` reference for the existing restricted project credential;
- verify reference existence/identity only;
- return the reference identifier and bounded evidence that the value was not read/exposed.

Not authorized:
- reading/using/printing/copying/hashing the credential value;
- provider calls;
- billing/account mutation;
- credential replacement/creation unless a separate blocker proves this is unavoidable and a new authority is granted;
- production deployment;
- Project Sources changes;
- project acceptance.

After PASS, KOO may prepare the separate one-call D0 live-execution decision gate.