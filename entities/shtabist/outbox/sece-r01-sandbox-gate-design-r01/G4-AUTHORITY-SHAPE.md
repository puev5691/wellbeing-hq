# Future G4 OPERATOR Authority Shape
status: DESIGN_CANDIDATE_NOT_AUTHORITY

Candidate decision token:
AUTHORIZE_SECE_R01_SANDBOX_EXECUTION_G4_<ATTEMPT> = YES

Required bound fields:
execution_attempt_id
exact candidate commit/tree/package path/relevant blobs
exact reviewed static result
exact combined offline runtime PASS
sandbox environment class
exact sandbox target identity
target ownership/isolation evidence
adapter class EphemeralFileSandboxEffectAdapterR01
effect class SANDBOX_EPHEMERAL_FILE_CREATE
exact relative path/payload digest/max bytes
task authority/currentness evidence
actor/writer/Recovery requirement/evidence
adapter/effect authority
sandbox target mutation authority
durable evidence carrier
rollback/cleanup scope
stop conditions
terminal criterion
G5 review disposition

Explicit:
production_authority=NO
deployment_authority=NO
reusable_authority=NO unless separately and explicitly decided
automatic_retry=NO
automatic_downstream=NO

This schema is not authority and must not be treated as one.
