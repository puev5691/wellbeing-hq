# SANDBOX_EPHEMERAL_FILE_CREATE — R02 corrected design
status: DESIGN_ONLY

Effect class remains unchanged in size and purpose: one exclusive regular-file creation in one isolated attempt-owned sandbox.

Exact path surface is narrowed to one admitted basename component only.

Confinement profile:
SECE_SANDBOX_CONFINEMENT_PROFILE_R02.

The effect's success criterion additionally requires created-object identity and same-object continuity evidence through outcome.

No target selected. No larger effect class introduced.
