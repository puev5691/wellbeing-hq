# R02 Outcome Evidence identity extension
status: DESIGN_ONLY

R01 outcome classes preserved:
EVIDENCED_SUCCESS | EVIDENCED_FAILURE | UNRESOLVED | NOT_EXECUTED.

EVIDENCED_SUCCESS additionally requires:
exact confinement profile/version;
anchored root object identity;
CREATED_SANDBOX_OBJECT_IDENTITY;
same-object evidence for write/stat/readback/hash;
regular-file/no-symlink-reparse evidence from the object;
platform non-replacement/hardlink evidence required by selected profile;
payload/length/hash/readback match.

Path string alone cannot prove success.

If effect may have happened but created-object continuity/replacement state cannot be proved => UNRESOLVED.

NOT_EXECUTED is permitted only with positive evidence mutation did not occur, such as invocation rejection before create.
