# Environment evidence

status:
PRE_EXECUTION_PROBES_RECORDED

project_time:
omitted

Local execution environment observed:

python:
Python 3.13.5

git:
git version 2.47.3

kernel:
Linux 6.18.57 x86_64

uid:
0

bubblewrap:
NOT_FOUND

unshare:
 /usr/bin/unshare

unshare network namespace probe:
FAILED
error: Operation not permitted
exit: 1

GitHub DNS probe:

command:
timeout 5 git ls-remote https://github.com/puev5691/wellbeing-hq.git HEAD

result:
fatal: unable to access 'https://github.com/puev5691/wellbeing-hq.git/': Could not resolve host: github.com

exit:
128

raw GitHub fixed-IP probe:

command class:
curl --resolve raw.githubusercontent.com:443:185.199.108.133 <immutable-raw-commit-url>

result:
Failed to connect to raw.githubusercontent.com port 443

exit:
7

Local exact-tree checkout/object-store probe:
NO_LOCAL_GIT_REPOSITORY_WITH_R02_TREE_FOUND

Remote Desktop Commander fresh probe:
3 configured devices
all status:
OFFLINE

Files/Library exact R02 source package search:
NO_MATERIALIZABLE_EXACT_R02_PACKAGE_FOUND

Local evidence probe SHA-256:
44a44b2b350438cb6dd5ee413185350fa437616ab810b65960b4f4758ddafd21

tests_executed:
NO

real_sandbox_effect:
NOT_EXECUTED
