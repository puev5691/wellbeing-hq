# Runtime / dependency declaration

status: OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Tested interpreter:
CPython 3.12.3

Required:
Python 3.12 or newer with standard library.

External Python packages:
NONE

Network:
NOT REQUIRED
FORBIDDEN BY CORE BOUNDARY

Environment variables:
NONE REQUIRED

Credentials:
NONE READ
NONE REQUIRED

Services/daemons:
NONE

Persistent database:
NONE

Core imports:
ast
copy
hashlib
json
pathlib
typing

The offline test runner imports socket/subprocess only to patch external-effect entry points to fail during firewall tests. Core source imports neither.
